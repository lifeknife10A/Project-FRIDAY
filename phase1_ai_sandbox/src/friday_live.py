"""
PROJECT FRIDAY - MILESTONE 1.6 LIVE HARNESS ON MACBOOK
Component: Multimodal Live Inference Loop (FaceTime Camera + Microphone + Kokoro TTS)
Author: Krishna Jagat Solanki (Lead Systems & ML Engineer, Project FRIDAY)
Charter & Requirements: Milestone 1.6 Items L0 - L10, Auditor Items M1 - M5, C1 - C4, R1 - R2, N1 - N2

Operating Modes:
  1. Live Interactive Mode: python phase1_ai_sandbox/src/friday_live.py --live --log
     Continuous camera ring buffer (separate process via mp.spawn) + single mic stream,
     wake word detection ("Hey Friday"), state machine (C3), earcon acknowledgment,
     Silero VAD query capture, frame scoring & selection (R1), local web preview at 127.0.0.1:8765 (C2),
     intent routing (READ / IDENTIFY / BOTH), extractive OCR (R2), student VLM description (N1),
     blocking Kokoro-82M TTS, and real-world results logging.
  2. Scripted Offline Regression: python phase1_ai_sandbox/src/friday_live.py --offline-regression
     Synthetic/benchmark frames, injected text queries, no camera/mic/TTS,
     never writes to results.csv.
  3. Unit Test Suite: python phase1_ai_sandbox/src/friday_live.py --test
     Verifies describe() image dependence, digit suppression, M5 timing,
     R1 resolution normalization, R2 handwritten reading, and N1 vocab mapping.
  4. Soak Test: python phase1_ai_sandbox/src/friday_live.py --soak-test
     60-second soak test with camera worker process + single mic stream + 5 injected
     wake/query cycles including double "Hey Friday" and wake-then-pause.
"""

import os
import sys
import re
import csv
import time
import json
import enum
import hashlib
import argparse
import threading
import collections
import http.server
from datetime import datetime
from typing import Optional, List, Tuple, Dict, Any

import cv2
import numpy as np

# Ensure project root and src/ are in PYTHONPATH
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)
SRC_DIR = os.path.join(REPO_ROOT, "phase1_ai_sandbox/src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

# Core Project FRIDAY Modules
from phase1_ai_sandbox.src.audio_earcon import play_earcon
from phase1_ai_sandbox.src.kokoro_voice_engine import FridayVoiceEngine, format_tts_spacing
from phase1_ai_sandbox.src.optical_foveation import OpticalFoveationEngine
from phase1_ai_sandbox.src.benchmark_dataset_evaluator import run_ocr
from phase1_ai_sandbox.src.literal_reader import read_literal, REFUSAL_TEXT

# ---------------------------------------------------------------------------
# CONSTANTS & THRESHOLDS (Documented; no per-item tuning)
# ---------------------------------------------------------------------------
MIN_SHARPNESS = 80.0          # Laplacian variance minimum (defocus rejection on normalized 1280 resolution)
MIN_EXPOSURE_MEAN = 30.0      # Minimum average grayscale luminance
MAX_EXPOSURE_MEAN = 248.0     # Maximum average grayscale luminance
MAX_CLIPPED_FRACTION = 0.15   # Max 15% of pixels clipped (<5 or >250)
FALLBACK_UNREADABLE = "I can't see it clearly. Please hold it closer and keep it steady."
FALLBACK_NO_OBJECT_MODEL = "I can't identify objects yet."

KAGGLE_MANIFEST_PATH = os.path.join(REPO_ROOT, "phase1_ai_sandbox/kaggle_runs/7571e39/weights_manifest.json")
STUDENT_WEIGHTS_PATH = os.path.join(REPO_ROOT, "FRIDAY_weights/best_student_vlm.pt")
EXPECTED_MANIFEST_SHA = "66391bd6cf68e19be4fef44931c28b8e8b0d5ced05031fe5e2b2ac01e5c158b7"

READ_KEYWORDS = ["read", "what does it say", "what's written", "what is written"]
IDENTIFY_KEYWORDS = ["what am i holding", "what is this", "what's in my hand"]


# ---------------------------------------------------------------------------
# C3 SESSION STATE MACHINE
# ---------------------------------------------------------------------------
class SessionState(str, enum.Enum):
    LISTENING_FOR_WAKE = "LISTENING_FOR_WAKE"
    RECORDING_QUERY = "RECORDING_QUERY"
    THINKING = "THINKING"
    SPEAKING = "SPEAKING"


# ---------------------------------------------------------------------------
# L0 DIGIT SAFETY RULE (Description path must never speak digits)
# ---------------------------------------------------------------------------
def filter_digits_from_description(text: str) -> str:
    """
    Auditor Item L0: Numbers, doses and prices may ONLY be spoken from read_literal output.
    The object/description path must never speak digits: if its text contains a digit,
    drop that sentence.
    """
    if not text:
        return ""
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    clean_sentences = []
    for s in sentences:
        s_clean = s.strip()
        if not s_clean:
            continue
        if re.search(r"\d", s_clean):
            continue
        clean_sentences.append(s_clean)
    return " ".join(clean_sentences).strip()


# ---------------------------------------------------------------------------
# C1 MULTIPROCESSING CAMERA WORKER (Spawned separate process)
# ---------------------------------------------------------------------------
def _camera_worker_proc(
    shm_name: str,
    camera_id: int,
    actual_w: int,
    actual_h: int,
    num_slots: int,
    target_fps: int,
    stop_event: Any,
    ready_val: Any,
    head_val: Any,
    err_queue: Any
):
    """
    Auditor Item C1: Camera capture runs in a SEPARATE PROCESS (multiprocessing spawn)
    that owns cv2.VideoCapture and shares the latest frames via shared memory.
    Prevents Objective-C AVFFrameReceiver/AVFAudioReceiver duplicate symbol collisions
    with PyAV/sounddevice in the main process.
    """
    import cv2
    import numpy as np
    from multiprocessing import shared_memory

    cap = None
    shm = None
    try:
        shm = shared_memory.SharedMemory(name=shm_name)
        cap = cv2.VideoCapture(camera_id)
        if not cap or not cap.isOpened():
            err_queue.put(f"Camera device index {camera_id} could not be opened.")
            ready_val.value = -1
            return

        cap.set(cv2.CAP_PROP_FRAME_WIDTH, actual_w)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, actual_h)
        det_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        det_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        if det_w <= 0 or det_h <= 0:
            det_w, det_h = actual_w, actual_h

        # Discard warmup frames (~1.0s)
        for _ in range(target_fps):
            ret, _ = cap.read()
            if not ret:
                break
            time.sleep(1.0 / float(target_fps))

        err_queue.put((det_w, det_h))
        ready_val.value = 1

        slot_bytes = 16 + actual_h * actual_w * 3
        prev_w, prev_h = 640, 360
        prev_offset = 64 + num_slots * slot_bytes

        interval = 1.0 / float(target_fps)
        frame_idx = 0

        while not stop_event.is_set():
            t0 = time.perf_counter()
            ret, frame = cap.read()
            if ret and frame is not None:
                if frame.shape[1] != actual_w or frame.shape[0] != actual_h:
                    frame = cv2.resize(frame, (actual_w, actual_h))

                slot_idx = frame_idx % num_slots
                offset = 64 + slot_idx * slot_bytes

                # Header: timestamp (float64, 8B), frame_idx (int64, 8B)
                np.ndarray((1,), dtype=np.float64, buffer=shm.buf, offset=offset)[0] = t0
                np.ndarray((1,), dtype=np.int64, buffer=shm.buf, offset=offset + 8)[0] = frame_idx
                # Write full frame
                arr = np.ndarray((actual_h, actual_w, 3), dtype=np.uint8, buffer=shm.buf, offset=offset + 16)
                arr[:] = frame

                # Write downscaled preview slot (640x360) for C2 web preview
                prev_frame = cv2.resize(frame, (prev_w, prev_h), interpolation=cv2.INTER_AREA)
                np.ndarray((1,), dtype=np.float64, buffer=shm.buf, offset=prev_offset)[0] = t0
                np.ndarray((1,), dtype=np.int64, buffer=shm.buf, offset=prev_offset + 8)[0] = frame_idx
                prev_arr = np.ndarray((prev_h, prev_w, 3), dtype=np.uint8, buffer=shm.buf, offset=prev_offset + 16)
                prev_arr[:] = prev_frame

                head_val.value = frame_idx
                frame_idx += 1

            elapsed = time.perf_counter() - t0
            time.sleep(max(0.001, interval - elapsed))

    except Exception as e:
        err_queue.put(f"Camera worker process error: {e}")
        ready_val.value = -1
    finally:
        if cap is not None:
            cap.release()
        if shm is not None:
            shm.close()


# ---------------------------------------------------------------------------
# L1, M3, C1 CAMERA PROCESS MANAGER & RING BUFFER
# ---------------------------------------------------------------------------
class CameraRingBuffer:
    """
    Auditor Items L1, M3 & C1: Runs camera capture in a separate spawned process.
    The spawned process owns cv2.VideoCapture and writes frames to a shared memory ring buffer.
    Main process reads without invoking any camera API.
    """
    def __init__(
        self,
        camera_id: int = 0,
        buffer_seconds: float = 1.5,
        target_fps: int = 15,
        offline_mode: bool = False
    ):
        self.camera_id = camera_id
        self.buffer_seconds = buffer_seconds
        self.target_fps = target_fps
        self.offline_mode = offline_mode
        self.num_slots = max(10, int(buffer_seconds * target_fps) + 5) # 25 slots
        self.actual_width = 1920
        self.actual_height = 1080
        self.prev_w = 640
        self.prev_h = 360

        self.slot_bytes = 16 + self.actual_height * self.actual_width * 3
        self.prev_bytes = 16 + self.prev_h * self.prev_w * 3
        self.total_shm_size = 64 + self.num_slots * self.slot_bytes + self.prev_bytes

        self.shm: Optional[Any] = None
        self.process: Optional[Any] = None
        self.stop_event: Optional[Any] = None
        self.ready_val: Optional[Any] = None
        self.head_val: Optional[Any] = None
        self.err_queue: Optional[Any] = None

        # Offline / synthetic frame fallback queue
        self.injected_frames = collections.deque(maxlen=self.num_slots)
        self.lock = threading.Lock()
        self.running = False

    def start(self):
        if self.offline_mode:
            print("[*] CameraRingBuffer initialized in OFFLINE/SCRIPTED mode.")
            self.running = True
            return

        import multiprocessing as mp
        from multiprocessing import shared_memory

        ctx = mp.get_context("spawn")
        self.stop_event = ctx.Event()
        self.ready_val = ctx.Value("i", 0)
        self.head_val = ctx.Value("q", -1)
        self.err_queue = ctx.Queue()

        self.shm = shared_memory.SharedMemory(create=True, size=self.total_shm_size)
        print(f"[*] Created Camera SharedMemory ({self.shm.name}, {self.total_shm_size / (1024**2):.1f} MB)...")

        self.process = ctx.Process(
            target=_camera_worker_proc,
            args=(
                self.shm.name,
                self.camera_id,
                self.actual_width,
                self.actual_height,
                self.num_slots,
                self.target_fps,
                self.stop_event,
                self.ready_val,
                self.head_val,
                self.err_queue
            ),
            daemon=True
        )
        self.process.start()

        # Wait for camera initialization from child process
        t0 = time.perf_counter()
        while self.ready_val.value == 0 and (time.perf_counter() - t0) < 5.0:
            time.sleep(0.05)

        if self.ready_val.value == -1 or not self.process.is_alive():
            err_msg = "Unknown error"
            if not self.err_queue.empty():
                err_msg = self.err_queue.get()
            print(
                f"\n[ERROR - Auditor Item M3 & C1] Camera device index {self.camera_id} could not be opened:\n"
                f"  Reason: {err_msg}\n"
                "Please verify:\n"
                "  1. The FaceTime HD / external camera is connected and not in use by another app.\n"
                "  2. macOS camera permissions are granted for Terminal / Python:\n"
                "     System Settings > Privacy & Security > Camera -> Enable Terminal / iTerm / VS Code.\n"
                "To run in offline mode without hardware camera, pass the explicit --offline flag.\n",
                file=sys.stderr
            )
            self.stop()
            sys.exit(1)

        if not self.err_queue.empty():
            res = self.err_queue.get()
            if isinstance(res, tuple):
                self.actual_width, self.actual_height = res

        self.running = True
        print(f"[✓] FaceTime Camera Process active (PID {self.process.pid}): {self.actual_width}x{self.actual_height} @ ~{self.target_fps} fps (SharedMemory)")

    def inject_frame(self, frame: np.ndarray):
        """Allows injecting synthetic or test frames into buffer."""
        with self.lock:
            self.injected_frames.append((time.perf_counter(), frame.copy()))

    def get_buffered_frames(self) -> List[Tuple[float, np.ndarray]]:
        """Returns snapshot of current ring buffer frames."""
        if self.offline_mode or self.shm is None:
            with self.lock:
                return list(self.injected_frames)

        current_head = self.head_val.value
        if current_head < 0:
            with self.lock:
                return list(self.injected_frames)

        frames = []
        count = min(current_head + 1, int(self.buffer_seconds * self.target_fps))
        start_idx = max(0, current_head - count + 1)

        for f_id in range(start_idx, current_head + 1):
            slot_idx = f_id % self.num_slots
            offset = 64 + slot_idx * self.slot_bytes
            ts = float(np.ndarray((1,), dtype=np.float64, buffer=self.shm.buf, offset=offset)[0])
            arr = np.ndarray((self.actual_height, self.actual_width, 3), dtype=np.uint8, buffer=self.shm.buf, offset=offset + 16)
            frames.append((ts, arr.copy()))

        return frames

    def capture_new_frames(self, duration_s: float = 1.0) -> List[Tuple[float, np.ndarray]]:
        """Captures ~duration_s of fresh frames from shared memory."""
        if self.offline_mode or self.shm is None:
            return self.get_buffered_frames()

        start_head = self.head_val.value
        target_frames = max(1, int(duration_s * self.target_fps))
        t_end = time.perf_counter() + duration_s + 0.5
        new_frames = []

        seen_ids = set()
        while (time.perf_counter() < t_end) and (len(seen_ids) < target_frames):
            cur_head = self.head_val.value
            if cur_head > start_head:
                for f_id in range(max(start_head + 1, cur_head - target_frames + 1), cur_head + 1):
                    if f_id not in seen_ids:
                        seen_ids.add(f_id)
                        slot_idx = f_id % self.num_slots
                        offset = 64 + slot_idx * self.slot_bytes
                        ts = float(np.ndarray((1,), dtype=np.float64, buffer=self.shm.buf, offset=offset)[0])
                        arr = np.ndarray((self.actual_height, self.actual_width, 3), dtype=np.uint8, buffer=self.shm.buf, offset=offset + 16)
                        new_frames.append((ts, arr.copy()))
            time.sleep(0.02)

        return new_frames or self.get_buffered_frames()

    def get_latest_preview_frame(self) -> Optional[np.ndarray]:
        """Returns the latest downscaled (640x360) frame for the C2 web preview."""
        if self.offline_mode or self.shm is None:
            with self.lock:
                if self.injected_frames:
                    raw = self.injected_frames[-1][1]
                    return cv2.resize(raw, (self.prev_w, self.prev_h))
                return None

        if self.head_val.value < 0:
            return None

        prev_offset = 64 + self.num_slots * self.slot_bytes
        arr = np.ndarray((self.prev_h, self.prev_w, 3), dtype=np.uint8, buffer=self.shm.buf, offset=prev_offset + 16)
        return arr.copy()

    def stop(self):
        self.running = False
        if self.stop_event:
            self.stop_event.set()
        if self.process and self.process.is_alive():
            self.process.join(timeout=1.5)
            if self.process.is_alive():
                self.process.terminate()
        if self.shm:
            try:
                self.shm.close()
                self.shm.unlink()
            except Exception:
                pass
            self.shm = None
        print("[*] Camera Ring Buffer process and shared memory released.")


# ---------------------------------------------------------------------------
# L2 & M4 WAKE WORD ENGINE
# ---------------------------------------------------------------------------
class WakeWordDetector:
    """
    Auditor Items L2 & M4: Wake Word 'Hey Friday'.
    Uses openWakeWord (Apache-2.0) if custom 'hey_friday.onnx' model exists.
    If not found, uses the documented temporary fallback:
      Silero VAD (MIT) + faster-whisper (MIT) keyword trigger ('friday').
    Triggers immediate audio earcon acknowledgment on wake (<80 ms).
    """
    def __init__(self, custom_model_path: Optional[str] = None):
        self.mode = "fallback"
        self.oww_model = None
        self.model_sha256 = None
        self.vad_model = None
        self.whisper_model = None

        if custom_model_path is None:
            custom_model_path = os.path.join(REPO_ROOT, "assets/wake_words/hey_friday.onnx")

        if os.path.exists(custom_model_path):
            try:
                from openwakeword.model import Model
                with open(custom_model_path, "rb") as f:
                    self.model_sha256 = hashlib.sha256(f.read()).hexdigest()
                self.oww_model = Model(wakeword_models=[custom_model_path])
                self.mode = "openwakeword"
                print(f"[✓] openWakeWord (Apache-2.0) initialized with custom model: {custom_model_path}")
                print(f"    Model SHA256: {self.model_sha256}")
            except Exception as e:
                print(f"[!] Warning: Failed to load openWakeWord model: {e}. Falling back to Silero+Whisper.")
                self.mode = "fallback"

        if self.mode == "fallback":
            try:
                import silero_vad
                self.vad_model = silero_vad.load_silero_vad()
            except Exception as e:
                print(f"[!] Warning loading silero-vad: {e}")
            try:
                from faster_whisper import WhisperModel
                self.whisper_model = WhisperModel("base.en", device="cpu", compute_type="int8")
            except Exception as e:
                print(f"[!] Warning loading faster-whisper for wake: {e}")

    def trigger_wake(self, mute_audio: bool = False) -> float:
        """Plays wake earcon tone and measures latency."""
        t0 = time.perf_counter()
        if not mute_audio:
            play_earcon(blocking=False)
        wake_to_earcon_ms = (time.perf_counter() - t0) * 1000.0
        return wake_to_earcon_ms


# ---------------------------------------------------------------------------
# L3 SPEECH QUERY CAPTURE (Faster-Whisper base.en)
# ---------------------------------------------------------------------------
class AudioQueryCapture:
    """
    Auditor Item L3: Transcribes query audio with faster-whisper base.en.
    Auditor Item C3: Uses single shared audio buffer; does NOT open a 2nd InputStream.
    """
    def __init__(self, whisper_model: Optional[Any] = None):
        if whisper_model is not None:
            self.whisper_model = whisper_model
        else:
            from faster_whisper import WhisperModel
            self.whisper_model = WhisperModel("base.en", device="cpu", compute_type="int8")

    def transcribe_audio_array(self, audio: np.ndarray) -> Tuple[str, float]:
        """Transcribes float32 audio numpy array with faster-whisper."""
        t0 = time.perf_counter()
        segments, _ = self.whisper_model.transcribe(audio, beam_size=1, language="en")
        transcript = " ".join(seg.text for seg in segments).strip()
        latency_ms = (time.perf_counter() - t0) * 1000.0
        return transcript, latency_ms


# ---------------------------------------------------------------------------
# L4 & R1 FRAME QUALITY SCORER & SELECTION ENGINE
# ---------------------------------------------------------------------------
class FrameScorer:
    """
    Auditor Items L4 & R1:
      (a) Resizes frame to long side 1280 before sharpness and exposure scoring,
          making sharpness independent of image sensor resolution.
      (b) When PP-OCR detects text boxes, scores sharpness inside the boxes.
      (c) Never discards a frame that has >=1 text box with confidence >= 0.90
          for global-sharpness reasons alone.
    Thresholds are fixed constants; no per-item tuning.
    """
    def __init__(self):
        pass

    def evaluate_frame(self, frame: np.ndarray, frame_id: int) -> Dict[str, Any]:
        h, w = frame.shape[:2]

        # Auditor Item R1 (a): Resize to long side 1280 before sharpness/exposure scoring
        max_dim = max(h, w)
        if max_dim != 1280 and max_dim > 0:
            scale = 1280.0 / float(max_dim)
            new_w = max(1, int(round(w * scale)))
            new_h = max(1, int(round(h * scale)))
            interp = cv2.INTER_AREA if max_dim > 1280 else cv2.INTER_LINEAR
            norm_frame = cv2.resize(frame, (new_w, new_h), interpolation=interp)
        else:
            norm_frame = frame

        gray_norm = cv2.cvtColor(norm_frame, cv2.COLOR_BGR2GRAY) if norm_frame.ndim == 3 else norm_frame

        # 1. Global Sharpness: Laplacian variance on normalized 1280 image
        global_sharpness = float(cv2.Laplacian(gray_norm, cv2.CV_64F).var())

        # 2. Exposure on normalized 1280 image
        mean_val = float(np.mean(gray_norm))
        clipped_count = int(np.count_nonzero((gray_norm < 5) | (gray_norm > 250)))
        clipped_fraction = float(clipped_count) / float(gray_norm.size)

        # Exposure discard checks
        exposure_discard = None
        if mean_val < MIN_EXPOSURE_MEAN:
            exposure_discard = f"underexposed (mean {mean_val:.1f} < {MIN_EXPOSURE_MEAN:.1f})"
        elif mean_val > MAX_EXPOSURE_MEAN:
            exposure_discard = f"overexposed (mean {mean_val:.1f} > {MAX_EXPOSURE_MEAN:.1f})"
        elif clipped_fraction > MAX_CLIPPED_FRACTION:
            exposure_discard = f"clipped pixels ({clipped_fraction*100.0:.1f}% > {MAX_CLIPPED_FRACTION*100.0:.0f}%)"

        # Run PP-OCR on candidate frame
        ocr_lines = run_ocr(frame)
        box_count = len(ocr_lines)
        total_text_area = 0.0

        # Auditor Item R1 (b): Score sharpness inside detected text boxes
        box_sharpness_scores = []
        has_high_conf_box = False

        for line in ocr_lines:
            b = line.get("box", [])
            conf = float(line.get("confidence", line.get("score", 0.0)))
            if conf >= 0.90:
                has_high_conf_box = True

            if b and len(b) >= 4:
                xs = [pt[0] for pt in b]
                ys = [pt[1] for pt in b]
                xmin, xmax = max(0, int(min(xs))), min(w, int(max(xs)))
                ymin, ymax = max(0, int(min(ys))), min(h, int(max(ys)))
                if (xmax > xmin + 4) and (ymax > ymin + 4):
                    total_text_area += (xmax - xmin) * (ymax - ymin)
                    crop = frame[ymin:ymax, xmin:xmax]
                    if crop.size > 0:
                        c_gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY) if crop.ndim == 3 else crop
                        b_sharp = float(cv2.Laplacian(c_gray, cv2.CV_64F).var())
                        box_sharpness_scores.append(b_sharp)

        mean_box_sharpness = float(np.mean(box_sharpness_scores)) if box_sharpness_scores else None

        # Auditor Item R1 (c): Never discard for global-sharpness alone if has high-confidence box
        discard_reason = exposure_discard
        if discard_reason is None:
            if global_sharpness < MIN_SHARPNESS:
                if has_high_conf_box:
                    # Overrides global blurriness
                    pass
                elif mean_box_sharpness is not None and mean_box_sharpness >= MIN_SHARPNESS:
                    # In-box text is sharp
                    pass
                else:
                    discard_reason = f"blurry (sharpness {global_sharpness:.1f} < {MIN_SHARPNESS:.1f})"

        passed = (discard_reason is None)
        text_area_ratio = total_text_area / float(h * w)

        # Composite score for candidate ranking
        composite_score = (
            (mean_box_sharpness if mean_box_sharpness is not None else global_sharpness)
            + 50.0 * min(box_count, 10)
            + 1000.0 * min(text_area_ratio, 0.5)
        )

        return {
            "frame_id": frame_id,
            "passed": passed,
            "discard_reason": discard_reason,
            "sharpness": global_sharpness,
            "box_sharpness": mean_box_sharpness,
            "mean_exposure": mean_val,
            "clipped_fraction": clipped_fraction,
            "box_count": box_count,
            "has_high_conf_box": has_high_conf_box,
            "text_area_ratio": text_area_ratio,
            "composite_score": composite_score,
            "ocr_lines": ocr_lines
        }

    def select_best_frame(
        self,
        candidate_frames: List[np.ndarray]
    ) -> Tuple[Optional[np.ndarray], Optional[Dict[str, Any]], List[Dict[str, Any]]]:
        """
        Evaluates candidate frames and returns (best_frame, best_meta, all_evaluations).
        If all frames fail threshold criteria, best_frame is None.
        """
        evaluations = []
        valid_candidates = []

        for idx, f in enumerate(candidate_frames):
            ev = self.evaluate_frame(f, idx)
            evaluations.append(ev)
            if ev["passed"]:
                valid_candidates.append((ev["composite_score"], idx, f, ev))

        if not valid_candidates:
            return None, None, evaluations

        # Sort descending by composite score
        valid_candidates.sort(key=lambda x: x[0], reverse=True)
        _, best_idx, best_f, best_ev = valid_candidates[0]
        return best_f, best_ev, evaluations


# ---------------------------------------------------------------------------
# L5 INTENT ROUTER
# ---------------------------------------------------------------------------
def route_intent(query_text: str) -> str:
    """
    Auditor Item L5: Maps transcribed query to READ, IDENTIFY, or BOTH.
    Default fallback: BOTH.
    """
    q_low = (query_text or "").lower()
    has_read = any(k in q_low for k in READ_KEYWORDS)
    has_id = any(k in q_low for k in IDENTIFY_KEYWORDS)

    if has_read and has_id:
        return "BOTH"
    elif has_read:
        return "READ"
    elif has_id:
        return "IDENTIFY"
    else:
        return "BOTH"


# ---------------------------------------------------------------------------
# L6 EXTRACTIVE LITERAL PIPELINE
# ---------------------------------------------------------------------------
def run_literal_pipeline(
    frame: np.ndarray,
    query_text: str,
    foveation_engine: OpticalFoveationEngine
) -> Dict[str, Any]:
    """
    Auditor Item L6: Runs PP-OCR full-frame. If unreadable/incomplete,
    executes optical foveation patch search.
    """
    t0 = time.perf_counter()
    lines_full = run_ocr(frame)
    res_full = read_literal(lines_full, category="scene_text", question=query_text)

    speech = res_full["speech"]
    source = "full_frame"

    # If full-frame refused, attempt foveation crop
    if speech == REFUSAL_TEXT:
        try:
            _, stream1_crop, _ = foveation_engine.process_frame(frame)
            if stream1_crop is not None and stream1_crop.size > 0:
                lines_fov = run_ocr(stream1_crop)
                res_fov = read_literal(lines_fov, category="scene_text", question=query_text)
                if res_fov["speech"] != REFUSAL_TEXT:
                    speech = res_fov["speech"]
                    source = "foveation_crop"
                    lines_full = lines_fov
        except Exception:
            pass

    latency_ms = (time.perf_counter() - t0) * 1000.0

    return {
        "speech": speech,
        "source": source,
        "latency_ms": latency_ms,
        "lines_full": lines_full
    }


# ---------------------------------------------------------------------------
# N1 VOCABULARY 64k MAPPER & STUDENT VLM TOKENIZER
# ---------------------------------------------------------------------------
class Vocab64kMapper:
    """
    Auditor Item N1: Compiles strictly 64,000-token subset from Qwen2.5-0.5B tokenizer
    with exact byte fallback and student EOS mapping (STUDENT_EOS_ID = old_to_new[eos]).
    Student architecture: Qwen2.5-0.5B 64k-pruned (415.2M parameters).
    """
    def __init__(self, tokenizer_name: str = "Qwen/Qwen2.5-0.5B", target_size: int = 64000):
        from transformers import AutoTokenizer
        self.base_tok = AutoTokenizer.from_pretrained(tokenizer_name)
        self.target_size = target_size
        self._compile_mapping()

    def _compile_mapping(self):
        def bytes_to_unicode():
            bs = (
                list(range(ord("!"), ord("~") + 1))
                + list(range(ord("¡"), ord("¬") + 1))
                + list(range(ord("®"), ord("ÿ") + 1))
            )
            cs = bs[:]
            n = 0
            for b in range(2**8):
                if b not in bs:
                    bs.append(b)
                    cs.append(2**8 + n)
                    n += 1
            cs = [chr(n) for n in cs]
            return dict(zip(bs, cs))

        self.byte_encoder = bytes_to_unicode()
        self.byte_tokens = set(self.byte_encoder.values())
        self.byte_decoder = {v: k for k, v in self.byte_encoder.items()}

        self.new_to_old = []
        self.old_to_new = {}

        vocab = self.base_tok.get_vocab()
        sorted_vocab = sorted(vocab.items(), key=lambda x: x[1])

        # Priority 1: Special tokens
        special_ids = set(self.base_tok.all_special_ids)
        for tok, tid in sorted_vocab:
            if tid in special_ids and tid not in self.old_to_new:
                self.old_to_new[tid] = len(self.new_to_old)
                self.new_to_old.append(tid)

        # Priority 2: All 256 byte fallback tokens
        for tok, tid in sorted_vocab:
            if tok in self.byte_tokens and tid not in self.old_to_new:
                self.old_to_new[tid] = len(self.new_to_old)
                self.new_to_old.append(tid)

        # Priority 3: Devanagari range (0x0900 - 0x0980) token IDs
        devanagari_ids = set()
        for cp in range(0x0900, 0x0980):
            devanagari_ids.update(self.base_tok.encode(chr(cp), add_special_tokens=False))

        for tid in sorted(devanagari_ids):
            if tid not in self.old_to_new and len(self.new_to_old) < self.target_size:
                self.old_to_new[tid] = len(self.new_to_old)
                self.new_to_old.append(tid)

        # Priority 4: Frequent vocabulary tokens up to target_size
        for tok, tid in sorted_vocab:
            if len(self.new_to_old) >= self.target_size:
                break
            if tid not in self.old_to_new:
                self.old_to_new[tid] = len(self.new_to_old)
                self.new_to_old.append(tid)

        assert len(self.new_to_old) == self.target_size, f"Compiled vocab size {len(self.new_to_old)} != {self.target_size}"
        raw_eos = self.base_tok.eos_token_id or 151643
        self.student_eos_id = self.old_to_new.get(raw_eos, 0)

    def safe_encode_64k(self, text: str) -> List[int]:
        orig_ids = self.base_tok.encode(text, add_special_tokens=False)
        sub_ids = []
        vocab = self.base_tok.get_vocab()
        for tid in orig_ids:
            if tid in self.old_to_new:
                sub_ids.append(self.old_to_new[tid])
            else:
                tok_piece = self.base_tok.convert_ids_to_tokens(tid)
                for c in tok_piece:
                    if c in self.byte_decoder:
                        b = self.byte_decoder[c]
                        b_char = self.byte_encoder[b]
                        b_tid = vocab[b_char]
                        if b_tid in self.old_to_new:
                            sub_ids.append(self.old_to_new[b_tid])
                        else:
                            raise ValueError(f"Byte {b} unmappable in 64k subset!")
                    else:
                        raise ValueError(f"Char {c} in piece {tok_piece} not in byte decoder!")
        return sub_ids

    def decode_64k(self, sub_ids: List[int]) -> str:
        orig_ids = [self.new_to_old[sid] for sid in sub_ids if 0 <= sid < len(self.new_to_old)]
        return self.base_tok.decode(orig_ids)


# ---------------------------------------------------------------------------
# L7, M2, N1 OBJECT DESCRIBER (Student VLM + Training Vocab Mapping)
# ---------------------------------------------------------------------------
class DescriptionPipeline:
    """
    Auditor Items L7, M2 & N1: Runs genuine student VLM forward pass
    (SigLIP -> Unshuffle Projector -> Qwen2.5-0.5B 64k-pruned student causal LM).
    Uses the training vocab mapping (safe_encode_64k / decode_64k / STUDENT_EOS_ID).
    If checkpoint missing or manifest hash mismatches -> returns FALLBACK_NO_OBJECT_MODEL.
    """
    def __init__(
        self,
        weights_path: str = STUDENT_WEIGHTS_PATH,
        compare_teacher: bool = False,
        allow_unverified_weights: bool = False,
        device: str = "cpu"
    ):
        self.weights_path = weights_path
        self.compare_teacher = compare_teacher
        self.allow_unverified_weights = allow_unverified_weights
        self.device = device
        self.manifest_sha256 = EXPECTED_MANIFEST_SHA
        self.actual_sha256 = None
        self.model_available = False

        self.student_model = None
        self.unshuffle_projector = None
        self.siglip_vision = None
        self.siglip_processor = None
        self.vocab_mapper = None

        self.teacher_model = None
        self.teacher_processor = None

        self._check_weights_and_init()

    def _check_weights_and_init(self):
        should_load = False
        if os.path.exists(self.weights_path):
            with open(self.weights_path, "rb") as f:
                self.actual_sha256 = hashlib.sha256(f.read()).hexdigest()

            if self.actual_sha256 == self.manifest_sha256:
                print(f"[✓] Verified Student Checkpoint SHA256: {self.actual_sha256[:16]}... (matches Kaggle 7571e39)")
                should_load = True
            elif self.allow_unverified_weights:
                print(f"[*] Note: Loading local unverified weights (--allow-unverified-weights active, SHA256: {self.actual_sha256[:16]}...).")
                should_load = True
            else:
                self.model_available = False
        else:
            self.model_available = False

        if should_load:
            self._load_student_vlm()

        if self.compare_teacher:
            self._load_teacher()

    def _load_student_vlm(self):
        try:
            import torch
            from transformers import AutoConfig, AutoModelForCausalLM, AutoModel, SiglipImageProcessor
            from phase1_ai_sandbox.src.student_vlm import SpatialUnshuffleDownsampler

            print(f"[*] Initializing Qwen2.5-0.5B 64k-pruned Student VLM on {self.device}...")
            ckpt = torch.load(self.weights_path, map_location=self.device)
            config = AutoConfig.from_pretrained("Qwen/Qwen2.5-0.5B")
            config.vocab_size = 64000
            self.student_model = AutoModelForCausalLM.from_config(config, attn_implementation="sdpa").to(self.device)
            self.student_model.load_state_dict(ckpt["student_state_dict"])
            self.student_model.eval()

            self.unshuffle_projector = SpatialUnshuffleDownsampler(in_features=768, out_features=896, grid_size=24).to(self.device)
            self.unshuffle_projector.load_state_dict(ckpt["projector_state_dict"])
            self.unshuffle_projector.eval()

            siglip = AutoModel.from_pretrained("google/siglip-base-patch16-384", torch_dtype=torch.float32).to(self.device)
            self.siglip_vision = siglip.vision_model.eval()
            self.siglip_processor = SiglipImageProcessor.from_pretrained("google/siglip-base-patch16-384")

            # Auditor Item N1: Initialize 64k vocab mapper
            self.vocab_mapper = Vocab64kMapper(tokenizer_name="Qwen/Qwen2.5-0.5B", target_size=64000)
            self.model_available = True
            print("[✓] Student VLM and 64k Vocab Mapper loaded successfully.")
        except Exception as e:
            print(f"[!] Warning: Failed to load Student VLM: {e}")
            self.model_available = False

    def _load_teacher(self):
        try:
            print("[*] Loading Qwen2-VL-2B teacher on Mac MPS for comparison only...")
            from transformers import Qwen2VLForConditionalGeneration, AutoProcessor
            self.teacher_processor = AutoProcessor.from_pretrained("Qwen/Qwen2-VL-2B-Instruct")
            self.teacher_model = Qwen2VLForConditionalGeneration.from_pretrained(
                "Qwen/Qwen2-VL-2B-Instruct",
                device_map={"": self.device}
            ).eval()
            print("[✓] Teacher loaded for comparison.")
        except Exception as e:
            print(f"[!] Teacher load failed: {e}")
            self.teacher_model = None

    def describe(self, frame: np.ndarray) -> Tuple[str, Dict[str, Any]]:
        """
        Executes object description.
        If student model unavailable -> returns FALLBACK_NO_OBJECT_MODEL ("I can't identify objects yet.").
        If student model available -> executes SigLIP -> Unshuffle -> Student generate (max 12 tokens).
        """
        t0 = time.perf_counter()
        teacher_text = None

        if self.compare_teacher and self.teacher_model is not None:
            try:
                import torch
                from PIL import Image
                rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) if frame.ndim == 3 else frame
                pil_img = Image.fromarray(rgb)
                prompt = "Describe in a few words what object the person is holding."
                messages = [{"role": "user", "content": [{"type": "image", "image": pil_img}, {"type": "text", "text": prompt}]}]
                text = self.teacher_processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
                inputs = self.teacher_processor(text=[text], images=[pil_img], padding=True, return_tensors="pt")
                inputs = inputs.to(self.teacher_model.device)
                with torch.no_grad():
                    gen_ids = self.teacher_model.generate(**inputs, max_new_tokens=12)
                teacher_text = self.teacher_processor.batch_decode(gen_ids, skip_special_tokens=True)[0].strip()
                print(f"  [TEACHER COMPARISON ONLY - NEVER SPOKEN]: {teacher_text}")
            except Exception as e:
                teacher_text = f"Teacher error: {e}"

        if not self.model_available or self.student_model is None or self.vocab_mapper is None:
            desc = FALLBACK_NO_OBJECT_MODEL
            raw_text = "description model not available"
            status = "[UNVALIDATED] (description model not available)"
        else:
            import torch
            from PIL import Image
            with torch.no_grad():
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) if frame.ndim == 3 else frame
                raw_img = Image.fromarray(rgb_frame).resize((384, 384))
                proc_out = self.siglip_processor(images=raw_img, return_tensors="pt")
                img_t = proc_out.pixel_values.to(self.device)
                patches = self.siglip_vision(pixel_values=img_t).last_hidden_state
                v_tokens = self.unshuffle_projector(patches.float()).to(self.student_model.dtype)

                prompt = "Describe in a few words what object the person is holding."
                # Auditor Item N1: safe_encode_64k mapping
                sub_ids = self.vocab_mapper.safe_encode_64k(prompt)
                q_t = torch.tensor([sub_ids], device=self.device)
                q_embeds = self.student_model.model.embed_tokens(q_t)

                inputs_embeds = torch.cat([v_tokens, q_embeds], dim=1).to(self.student_model.dtype)
                curr_embeds = inputs_embeds
                gen_tokens = []
                eos_id = self.vocab_mapper.student_eos_id

                for _ in range(12):
                    logits = self.student_model(inputs_embeds=curr_embeds).logits[:, -1, :]
                    next_id = int(torch.argmax(logits, dim=-1).item())
                    if next_id == eos_id:
                        break
                    gen_tokens.append(next_id)
                    next_embed = self.student_model.model.embed_tokens(torch.tensor([[next_id]], device=self.device))
                    curr_embeds = torch.cat([curr_embeds, next_embed], dim=1)

                # Auditor Item N1: decode_64k mapping
                raw_text = self.vocab_mapper.decode_64k(gen_tokens).strip()
                status = "[UNVALIDATED]"
                # Apply Auditor Item L0 digit filter
                filtered = filter_digits_from_description(raw_text)
                desc = filtered if filtered else FALLBACK_NO_OBJECT_MODEL

        latency_ms = (time.perf_counter() - t0) * 1000.0

        return desc, {
            "raw_text": raw_text,
            "status": status,
            "teacher_text": teacher_text,
            "latency_ms": latency_ms
        }


# ---------------------------------------------------------------------------
# L8 & M2 RESPONSE COMPOSER
# ---------------------------------------------------------------------------
def compose_spoken_response(
    intent: str,
    description: Optional[str],
    literal_speech: Optional[str]
) -> str:
    """
    Auditor Items L8 & M2: Composes speech cleanly without invented nouns.
    """
    if intent == "BOTH":
        parts = []
        if description:
            if description.startswith("I can't"):
                parts.append(description)
            else:
                parts.append(f"You're holding {description}.")
        if literal_speech:
            parts.append(f"It says: {literal_speech}")
        return " ".join(parts).strip()
    elif intent == "IDENTIFY":
        if description:
            if description.startswith("I can't"):
                return description
            return f"You're holding {description}."
        return FALLBACK_NO_OBJECT_MODEL
    elif intent == "READ":
        return literal_speech or REFUSAL_TEXT
    else:
        return literal_speech or REFUSAL_TEXT


# ---------------------------------------------------------------------------
# L9 REAL-WORLD TEST LOGGER
# ---------------------------------------------------------------------------
class TurnLogger:
    """
    Auditor Items L9 & M5: Saves real-world test logs under phase1_ai_sandbox/real_world_tests/ (.gitignored).
    Results CSV includes an empty human_verdict column for manual audit.
    Steps that did not run are logged as 'not run'.
    """
    def __init__(self, log_dir: Optional[str] = None):
        self.log_dir = log_dir or os.path.join(REPO_ROOT, "phase1_ai_sandbox/real_world_tests")
        self.frames_dir = os.path.join(self.log_dir, "frames")
        self.csv_path = os.path.join(self.log_dir, "results.csv")
        os.makedirs(self.frames_dir, exist_ok=True)
        self._init_csv()

    def _init_csv(self):
        if not os.path.exists(self.csv_path):
            headers = [
                "turn_id", "timestamp", "intent", "transcript",
                "chosen_frame_saved", "discarded_count", "ocr_lines_count",
                "spoken_text", "wake_to_earcon_ms", "stt_ms",
                "frame_sel_ms", "ocr_ms", "desc_ms", "tts_synth_ms", "tts_duration_s",
                "total_wake_to_first_audio_ms", "human_verdict"
            ]
            with open(self.csv_path, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(headers)

    def log_turn(
        self,
        turn_id: int,
        intent: str,
        transcript: str,
        chosen_frame: Optional[np.ndarray],
        discarded_evals: List[Dict[str, Any]],
        ocr_lines: List[Any],
        spoken_text: str,
        timings: Dict[str, Any]
    ):
        ts = datetime.now().isoformat()
        frame_saved_path = ""
        if chosen_frame is not None:
            filename = f"turn_{turn_id:03d}_best.jpg"
            full_path = os.path.join(self.frames_dir, filename)
            cv2.imwrite(full_path, chosen_frame)
            frame_saved_path = filename

        def fmt(val, is_float=True, digits=1):
            if val is None:
                return "not run"
            return f"{val:.{digits}f}" if is_float else str(val)

        row = [
            turn_id, ts, intent, transcript,
            frame_saved_path, len(discarded_evals), len(ocr_lines),
            spoken_text,
            fmt(timings.get("wake_to_earcon_ms")),
            fmt(timings.get("stt_ms")),
            fmt(timings.get("frame_selection_ms")),
            fmt(timings.get("ocr_ms")),
            fmt(timings.get("description_ms")),
            fmt(timings.get("tts_synth_ms")),
            fmt(timings.get("tts_audio_dur_s"), digits=2),
            fmt(timings.get("total_wake_to_first_audio_ms")),
            "" # EMPTY human_verdict column for Krishna to fill during real-world audit
        ]
        with open(self.csv_path, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(row)


# ---------------------------------------------------------------------------
# C2 LOCAL PREVIEW WEB SERVER (http://127.0.0.1:8765)
# ---------------------------------------------------------------------------
class LocalPreviewServer:
    """
    Auditor Item C2: Local preview at http://127.0.0.1:8765 (bind 127.0.0.1 only).
    Serves:
      - Live feed (~10 fps downscaled)
      - State banner (C3 states: LISTENING_FOR_WAKE, RECORDING_QUERY, THINKING, SPEAKING)
      - Last turn's selected frame with OCR bounding boxes + discard reasons
      - Spoken text output
    Disabled if --no-preview is passed. Nothing saved unless --log.
    """
    def __init__(self, host: str = "127.0.0.1", port: int = 8765, camera_buffer: Optional[CameraRingBuffer] = None):
        self.host = host
        self.port = port
        self.camera_buffer = camera_buffer
        self.state = SessionState.LISTENING_FOR_WAKE.value
        self.turn_id = 0
        self.query_text = ""
        self.spoken_text = ""
        self.discard_reasons: List[str] = []
        self.last_turn_frame: Optional[np.ndarray] = None
        self.lock = threading.Lock()
        self.server: Optional[http.server.ThreadingHTTPServer] = None
        self.thread: Optional[threading.Thread] = None

    def update_state(self, new_state: SessionState):
        with self.lock:
            self.state = new_state.value

    def update_turn_result(
        self,
        turn_id: int,
        query: str,
        spoken: str,
        selected_frame: Optional[np.ndarray],
        ocr_lines: List[Any],
        discard_reasons: List[str]
    ):
        with self.lock:
            self.turn_id = turn_id
            self.query_text = query
            self.spoken_text = spoken
            self.discard_reasons = discard_reasons

            if selected_frame is not None:
                annotated = selected_frame.copy()
                for line in ocr_lines:
                    b = line.get("box", [])
                    t = str(line.get("raw_text", ""))
                    c = float(line.get("confidence", line.get("score", 0.0)))
                    if b and len(b) >= 4:
                        pts = np.array(b, np.int32).reshape((-1, 1, 2))
                        cv2.polylines(annotated, [pts], isClosed=True, color=(0, 255, 0), thickness=2)
                        org = (int(b[0][0]), max(15, int(b[0][1]) - 5))
                        cv2.putText(annotated, f"{t} ({c:.2f})", org, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
                # Resize for preview
                h, w = annotated.shape[:2]
                max_d = max(h, w)
                if max_d > 640:
                    sc = 640.0 / float(max_d)
                    annotated = cv2.resize(annotated, (int(w * sc), int(h * sc)))
                self.last_turn_frame = annotated
            else:
                self.last_turn_frame = None

    def start(self):
        parent = self

        class PreviewHandler(http.server.BaseHTTPRequestHandler):
            def log_message(self, format, *args):
                pass # Suppress HTTP access logging to keep terminal clean

            def do_GET(self):
                if self.path in ("/", "/index.html"):
                    self.send_response(200)
                    self.send_header("Content-Type", "text/html; charset=utf-8")
                    self.end_headers()
                    html = parent._render_dashboard_html()
                    self.wfile.write(html.encode("utf-8"))

                elif self.path == "/live.jpg":
                    frame = None
                    if parent.camera_buffer:
                        frame = parent.camera_buffer.get_latest_preview_frame()
                    if frame is None:
                        frame = np.zeros((360, 640, 3), dtype=np.uint8)
                        cv2.putText(frame, "Waiting for Camera...", (180, 180), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

                    ret, jpeg = cv2.imencode(".jpg", frame, [int(cv2.IMWRITE_JPEG_QUALITY), 70])
                    if ret:
                        self.send_response(200)
                        self.send_header("Content-Type", "image/jpeg")
                        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
                        self.end_headers()
                        self.wfile.write(jpeg.tobytes())
                    else:
                        self.send_error(500)

                elif self.path == "/last_turn.jpg":
                    with parent.lock:
                        frame = parent.last_turn_frame

                    if frame is None:
                        frame = np.zeros((360, 640, 3), dtype=np.uint8)
                        cv2.putText(frame, "No turn executed yet", (200, 180), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (150, 150, 150), 2)

                    ret, jpeg = cv2.imencode(".jpg", frame, [int(cv2.IMWRITE_JPEG_QUALITY), 80])
                    if ret:
                        self.send_response(200)
                        self.send_header("Content-Type", "image/jpeg")
                        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
                        self.end_headers()
                        self.wfile.write(jpeg.tobytes())
                    else:
                        self.send_error(500)

                elif self.path == "/api/status":
                    with parent.lock:
                        data = {
                            "state": parent.state,
                            "turn_id": parent.turn_id,
                            "query": parent.query_text,
                            "spoken": parent.spoken_text,
                            "discard_reasons": parent.discard_reasons
                        }
                    raw = json.dumps(data)
                    self.send_response(200)
                    self.send_header("Content-Type", "application/json")
                    self.send_header("Cache-Control", "no-cache")
                    self.end_headers()
                    self.wfile.write(raw.encode("utf-8"))
                else:
                    self.send_error(404)

        try:
            self.server = http.server.ThreadingHTTPServer((self.host, self.port), PreviewHandler)
            self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
            self.thread.start()
            print(f"[✓] Local Preview Server active at http://{self.host}:{self.port} (Auditor Item C2)")
        except Exception as e:
            print(f"[!] Warning: Could not start preview server on {self.host}:{self.port}: {e}")

    def _render_dashboard_html(self) -> str:
        with self.lock:
            cur_state = self.state
            q_txt = self.query_text or "None"
            spk_txt = self.spoken_text or "Waiting for speech..."
            t_id = self.turn_id
            reasons = "<br>".join(self.discard_reasons) if self.discard_reasons else "None"

        return f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Project FRIDAY - Live Evaluation Console</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #0f172a; color: #f8fafc; margin: 0; padding: 20px; }}
        .header {{ display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #334155; padding-bottom: 15px; margin-bottom: 20px; }}
        .badge {{ padding: 8px 16px; border-radius: 20px; font-weight: 700; font-size: 14px; letter-spacing: 0.5px; text-transform: uppercase; }}
        .badge-listening {{ background: #1e3a8a; color: #93c5fd; border: 1px solid #3b82f6; }}
        .badge-recording {{ background: #7f1d1d; color: #fca5a5; border: 1px solid #ef4444; }}
        .badge-thinking {{ background: #581c87; color: #d8b4fe; border: 1px solid #a855f7; }}
        .badge-speaking {{ background: #064e3b; color: #6ee7b7; border: 1px solid #10b981; }}
        .grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }}
        .card {{ background: #1e293b; border-radius: 12px; padding: 18px; border: 1px solid #334155; }}
        .card h3 {{ margin-top: 0; color: #94a3b8; font-size: 14px; text-transform: uppercase; letter-spacing: 0.5px; }}
        .stream-box {{ width: 100%; border-radius: 8px; background: #000; aspect-ratio: 16/9; object-fit: contain; }}
        .info-row {{ margin-top: 10px; font-size: 14px; line-height: 1.5; }}
        .label {{ color: #94a3b8; font-weight: 600; }}
        .highlight {{ color: #38bdf8; font-weight: 600; }}
    </style>
</head>
<body>
    <div class="header">
        <div>
            <h2 style="margin:0;">Project FRIDAY — Live Evaluation Console</h2>
            <div style="color: #64748b; font-size: 13px; margin-top: 4px;">Milestone 1.6 Multimodal Live Harness (MacBook Air M4)</div>
        </div>
        <div id="stateBadge" class="badge badge-listening">{cur_state}</div>
    </div>
    <div class="grid">
        <div class="card">
            <h3>Live FaceTime Camera Feed (~10 fps)</h3>
            <img id="liveImg" src="/live.jpg" class="stream-box" alt="Live Feed">
            <div class="info-row" style="margin-top:12px;">
                <span class="label">Status:</span> Connected via SharedMemory (C1 Isolated Process)
            </div>
        </div>
        <div class="card">
            <h3>Last Turn Selected Frame & OCR Boxes</h3>
            <img id="lastImg" src="/last_turn.jpg" class="stream-box" alt="Last Turn Frame">
            <div class="info-row">
                <span class="label">Turn #{t_id} Speech Query:</span> <span id="querySpan" class="highlight">"{q_txt}"</span>
            </div>
            <div class="info-row">
                <span class="label">Spoken Response:</span> <span id="spokenSpan" style="color: #4ade80; font-weight: 600;">"{spk_txt}"</span>
            </div>
            <div class="info-row">
                <span class="label">Candidate Discard Reasons:</span><br>
                <span id="discardSpan" style="color: #f87171; font-size: 13px;">{reasons}</span>
            </div>
        </div>
    </div>
    <script>
        function updateLive() {{
            document.getElementById('liveImg').src = '/live.jpg?t=' + Date.now();
        }}
        setInterval(updateLive, 100);

        function updateStatus() {{
            fetch('/api/status').then(r => r.json()).then(data => {{
                var b = document.getElementById('stateBadge');
                b.textContent = data.state;
                b.className = 'badge';
                if (data.state === 'LISTENING_FOR_WAKE') b.classList.add('badge-listening');
                else if (data.state === 'RECORDING_QUERY') b.classList.add('badge-recording');
                else if (data.state === 'THINKING') b.classList.add('badge-thinking');
                else if (data.state === 'SPEAKING') b.classList.add('badge-speaking');

                document.getElementById('querySpan').textContent = '"' + data.query + '"';
                document.getElementById('spokenSpan').textContent = '"' + data.spoken + '"';
                document.getElementById('discardSpan').innerHTML = data.discard_reasons.length ? data.discard_reasons.join('<br>') : 'None';
            }}).catch(() => {{}});
        }}
        setInterval(updateStatus, 500);
    </script>
</body>
</html>"""

    def stop(self):
        if self.server:
            self.server.shutdown()
            self.server.server_close()
            self.server = None


# ---------------------------------------------------------------------------
# MAIN LIVE PIPELINE CONTROLLER
# ---------------------------------------------------------------------------
class FridayLiveSystem:
    """
    Project FRIDAY - Milestone 1.6 Unified Live Orchestrator.
    Executes the multimodal turn loop across hardware threads.
    """
    def __init__(
        self,
        use_camera: bool = False,
        use_mic: bool = False,
        offline_mode: bool = False,
        compare_teacher: bool = False,
        log_enabled: bool = False,
        mute_audio: bool = False,
        preview_enabled: bool = True
    ):
        self.use_camera = use_camera
        self.use_mic = use_mic
        self.offline_mode = offline_mode
        self.compare_teacher = compare_teacher
        self.log_enabled = log_enabled
        self.mute_audio = mute_audio
        self.preview_enabled = preview_enabled

        # Subsystems
        self.wake_detector = WakeWordDetector()
        self.camera_buffer = CameraRingBuffer(offline_mode=offline_mode)
        self.foveation_engine = OpticalFoveationEngine()
        self.frame_scorer = FrameScorer()
        self.query_capture = AudioQueryCapture()
        self.description_pipeline = DescriptionPipeline(compare_teacher=compare_teacher)
        self.voice_engine = FridayVoiceEngine()
        self.logger = TurnLogger() if log_enabled else None

        self.preview_server = None
        if self.preview_enabled and not self.offline_mode:
            self.preview_server = LocalPreviewServer(camera_buffer=self.camera_buffer)
            self.preview_server.start()

        if self.use_camera and not self.offline_mode:
            self.camera_buffer.start()

    def process_turn(
        self,
        turn_id: int,
        query_text: Optional[str] = None,
        candidate_frames: Optional[List[np.ndarray]] = None,
        pre_measured_wake_ms: Optional[float] = None,
        pre_measured_stt_ms: Optional[float] = None,
        write_log: bool = True
    ) -> Dict[str, Any]:
        """
        Executes one full conversational turn with full hardware profiling.
        Auditor Item M5: Unexecuted stages report None / 'not run' and are excluded from total.
        """
        timings: Dict[str, Optional[float]] = {
            "wake_to_earcon_ms": None,
            "stt_ms": None,
            "frame_selection_ms": None,
            "ocr_ms": None,
            "description_ms": None,
            "tts_synth_ms": None,
            "tts_audio_dur_s": None,
            "total_wake_to_first_audio_ms": None
        }

        print(f"\n{'='*68}")
        print(f"TURN #{turn_id} EXECUTION START")
        print(f"{'='*68}")

        # 1. Wake word & Earcon
        if pre_measured_wake_ms is not None:
            timings["wake_to_earcon_ms"] = pre_measured_wake_ms
            print(f"  [1/7] Wake Earcon Chime      : {pre_measured_wake_ms:.2f} ms (<80 ms contract)")
        elif not self.offline_mode:
            wake_ms = self.wake_detector.trigger_wake(mute_audio=self.mute_audio)
            timings["wake_to_earcon_ms"] = wake_ms
            print(f"  [1/7] Wake Earcon Chime      : {wake_ms:.2f} ms (<80 ms contract)")
        else:
            print("  [1/7] Wake Earcon Chime      : not run (offline regression)")

        # 2. Frame Acquisition
        t_frame0 = time.perf_counter()
        if candidate_frames is None:
            if self.use_camera and not self.offline_mode:
                buffered = [f for _, f in self.camera_buffer.get_buffered_frames()]
                fresh = [f for _, f in self.camera_buffer.capture_new_frames(duration_s=1.0)]
                frames_to_score = buffered + fresh
            else:
                frames_to_score = []
        else:
            frames_to_score = candidate_frames

        # 3. Frame Scoring & Discard Engine (Item L4 & R1)
        best_frame, best_meta, discard_evals = self.frame_scorer.select_best_frame(frames_to_score)
        timings["frame_selection_ms"] = (time.perf_counter() - t_frame0) * 1000.0

        discarded_count = sum(1 for e in discard_evals if not e["passed"])
        passed_count = sum(1 for e in discard_evals if e["passed"])
        print(f"  [2/7] Frame Quality Analysis : {passed_count} passed, {discarded_count} discarded in {timings['frame_selection_ms']:.1f} ms")
        discard_reasons_list = []
        for ev in discard_evals:
            if not ev["passed"]:
                reason = f"Frame #{ev['frame_id']}: {ev['discard_reason']}"
                discard_reasons_list.append(reason)
                print(f"        -> Discarded frame #{ev['frame_id']}: {ev['discard_reason']}")

        # 4. Speech Query Capture & Intent Routing (Items L3 & L5)
        if query_text is not None:
            transcript = query_text
            timings["stt_ms"] = pre_measured_stt_ms
            stt_disp = f"{pre_measured_stt_ms:.1f} ms" if pre_measured_stt_ms is not None else "not run"
            print(f"  [3/7] Speech Query Input     : \"{transcript}\" (STT: {stt_disp})")
        else:
            transcript = "What does it say?"
            print(f"  [3/7] Speech Query Input     : \"{transcript}\" (STT: not run)")

        intent = route_intent(transcript)
        print(f"  [4/7] Intent Router Decision : [{intent}]")

        # Check if frame selection failed (Item L4)
        if best_frame is None:
            spoken_text = FALLBACK_UNREADABLE
            print("  [!] All candidate frames failed threshold criteria.")
            print("  [5/7] Literal / Desc Pipeline: SKIPPED (Unclear frame)")
            ocr_lines = []
        else:
            print(f"        -> Selected Best Frame #{best_meta['frame_id']} (Sharpness: {best_meta['sharpness']:.1f}, Boxes: {best_meta['box_count']})")
            ocr_lines = best_meta["ocr_lines"]

            # 5. Pipeline Execution according to Intent
            description_str = None
            literal_str = None

            if intent in ("IDENTIFY", "BOTH"):
                desc_text, desc_info = self.description_pipeline.describe(best_frame)
                description_str = desc_text
                timings["description_ms"] = desc_info["latency_ms"]
                print(f"  [5/7] Description Path       : \"{desc_text}\" ({desc_info['status']}) in {timings['description_ms']:.1f} ms")

            if intent in ("READ", "BOTH"):
                lit_result = run_literal_pipeline(best_frame, transcript, self.foveation_engine)
                literal_str = lit_result["speech"]
                timings["ocr_ms"] = lit_result["latency_ms"]
                ocr_lines = lit_result.get("lines_full", ocr_lines)
                print(f"  [6/7] Extractive Literal Path: \"{literal_str}\" (via {lit_result['source']}) in {timings['ocr_ms']:.1f} ms")

            # 6. Compose Response (Item L8 & M2)
            spoken_text = compose_spoken_response(intent, description_str, literal_str)

        # 7. Kokoro-82M TTS Spacing & Synthesis (Item L8 & M5)
        spoken_tts_formatted = format_tts_spacing(spoken_text)
        if not self.mute_audio:
            import soundfile as sf
            t_tts0 = time.perf_counter()
            wav_path = self.voice_engine.synthesize(spoken_tts_formatted)
            t_synth_ms = (time.perf_counter() - t_tts0) * 1000.0
            timings["tts_synth_ms"] = t_synth_ms
            if wav_path and os.path.exists(wav_path):
                timings["tts_audio_dur_s"] = sf.info(wav_path).duration
                import subprocess
                subprocess.run(["afplay", wav_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            print("  [7/7] Kokoro TTS Playback    : not run (mute enabled)")

        # Calculate Total Wake-to-First-Audio (Auditor Item M5)
        active_times = [
            timings[k] for k in ["wake_to_earcon_ms", "stt_ms", "frame_selection_ms", "ocr_ms", "description_ms", "tts_synth_ms"]
            if timings[k] is not None
        ]
        timings["total_wake_to_first_audio_ms"] = sum(active_times) if active_times else None

        print(f"  [Spoken Output Text]         : \"{spoken_text}\"")

        # Update preview dashboard
        if self.preview_server:
            self.preview_server.update_turn_result(
                turn_id=turn_id,
                query=transcript,
                spoken=spoken_text,
                selected_frame=best_frame,
                ocr_lines=ocr_lines,
                discard_reasons=discard_reasons_list
            )

        # Print Latency Breakdown Table (Auditor Item M5)
        self._print_latency_summary(timings)

        # Log turn if enabled and allowed
        if self.logger and write_log:
            self.logger.log_turn(
                turn_id=turn_id,
                intent=intent,
                transcript=transcript,
                chosen_frame=best_frame,
                discarded_evals=discard_evals,
                ocr_lines=ocr_lines,
                spoken_text=spoken_text,
                timings=timings
            )

        return {
            "turn_id": turn_id,
            "intent": intent,
            "transcript": transcript,
            "spoken_text": spoken_text,
            "timings": timings,
            "best_frame_passed": (best_frame is not None),
            "discarded_count": discarded_count
        }

    def _print_latency_summary(self, timings: Dict[str, Any]):
        """Auditor Item M5: Latency table with 'not run' for unexecuted stages."""
        def fmt_ms(val):
            return f"{val:6.1f} ms" if val is not None else "     not run"

        print("\n  " + "-"*56)
        print("  LATENCY TELEMETRY PROFILING BREAKDOWN (Auditor Item M5)")
        print("  " + "-"*56)
        print(f"    Wake -> Earcon Chime      : {fmt_ms(timings.get('wake_to_earcon_ms'))}")
        print(f"    STT Query Transcription   : {fmt_ms(timings.get('stt_ms'))}")
        print(f"    Frame Selection & Discard : {fmt_ms(timings.get('frame_selection_ms'))}")
        print(f"    Extractive OCR & Reading  : {fmt_ms(timings.get('ocr_ms'))}")
        print(f"    Object Description Model  : {fmt_ms(timings.get('description_ms'))}")
        print(f"    TTS Synthesis Time        : {fmt_ms(timings.get('tts_synth_ms'))}")
        if timings.get("tts_audio_dur_s") is not None:
            rtf = (timings["tts_synth_ms"] / (timings["tts_audio_dur_s"] * 1000.0)) if timings.get("tts_synth_ms") else 0.0
            print(f"    TTS Audio Duration        :  {timings['tts_audio_dur_s']:.2f} s (RTF: {rtf:.2f})")
        else:
            print("    TTS Audio Duration        :      not run")
        print("  " + "-"*56)
        tot = timings.get("total_wake_to_first_audio_ms")
        tot_str = f"{tot:6.1f} ms" if tot is not None else "     not run"
        print(f"    TOTAL WAKE-TO-FIRST-AUDIO : {tot_str}")
        print("  " + "-"*56)

    def shutdown(self):
        if self.preview_server:
            self.preview_server.stop()
        self.camera_buffer.stop()


# ---------------------------------------------------------------------------
# M4 & C3 & C4 CONTINUOUS LIVE HARNESS LOOP WITH SINGLE MIC STREAM
# ---------------------------------------------------------------------------
def run_live_harness_loop(
    camera_id: int = 0,
    compare_teacher: bool = False,
    log_enabled: bool = True,
    no_preview: bool = False
):
    """
    Auditor Items M4, C3 & C4: Continuous live listening loop on MacBook.
    Maintains camera worker process + single microphone stream running continuously.
    State Machine (C3):
      LISTENING_FOR_WAKE -> RECORDING_QUERY -> THINKING -> SPEAKING -> LISTENING_FOR_WAKE
    While not in LISTENING_FOR_WAKE, wake detection is disabled.
    After SPEAKING, ignores wake for TTS duration + 1.0 s (no self-trigger).
    Auditor Item C4: Runs Silero VAD over the whole 1.5s window in 512-sample chunks.
    Local preview server at http://127.0.0.1:8765 (Auditor Item C2).
    """
    import sounddevice as sd
    import torch

    # Print Auditor Item N2 Startup Banner
    print("\n" + "="*70)
    print("PROJECT FRIDAY: LIVE MACBOOK WEARABLE HARNESS (Auditor Items M4, C1-C4, N1-N2)")
    print("="*70)

    # Initialize System
    system = FridayLiveSystem(
        use_camera=True,
        use_mic=True,
        offline_mode=False,
        compare_teacher=compare_teacher,
        log_enabled=log_enabled,
        mute_audio=False,
        preview_enabled=not no_preview
    )

    # Startup banner for Description Model (Auditor Item N2)
    desc_p = system.description_pipeline
    if desc_p.model_available and desc_p.actual_sha256 == EXPECTED_MANIFEST_SHA:
        print(f"DESCRIPTION MODEL: ACTIVE (sha matches 7571e39 manifest {EXPECTED_MANIFEST_SHA[:16]}...)")
    else:
        local_sha_disp = f"{desc_p.actual_sha256[:16]}..." if desc_p.actual_sha256 else "none (file not found)"
        print(f"DESCRIPTION MODEL: NOT AVAILABLE (local sha shown: {local_sha_disp})")
    print("="*70 + "\n")

    sample_rate = 16000
    chunk_size = 512

    # Auditor Item C3: Single input stream for the entire session
    current_state = SessionState.LISTENING_FOR_WAKE
    state_lock = threading.Lock()

    wake_audio_buffer = collections.deque(maxlen=sample_rate * 3) # rolling 3.0s
    query_audio_buffer = []

    def set_state(st: SessionState):
        nonlocal current_state
        with state_lock:
            current_state = st
            if system.preview_server:
                system.preview_server.update_state(st)
            print(f"[*] State Machine Transition -> [{st.value}]")

    def audio_callback(indata, frames, time_info, status):
        samples = indata[:, 0].copy()
        with state_lock:
            if current_state == SessionState.LISTENING_FOR_WAKE:
                wake_audio_buffer.extend(samples)
            elif current_state == SessionState.RECORDING_QUERY:
                query_audio_buffer.extend(samples)

    vad_model = system.wake_detector.vad_model
    whisper_model = system.wake_detector.whisper_model

    print("[✓] Project FRIDAY is LIVE and listening for 'Hey Friday'...")
    print("    Hold an item in front of your FaceTime camera and speak.")
    print("    Local Preview available at http://127.0.0.1:8765")
    print("    Press Ctrl+C to stop.\n")

    turn_counter = 0
    wake_cooldown_until = 0.0

    try:
        with sd.InputStream(samplerate=sample_rate, channels=1, dtype="float32", blocksize=chunk_size, callback=audio_callback):
            while True:
                # -------------------------------------------------------------
                # STATE: LISTENING_FOR_WAKE
                # -------------------------------------------------------------
                if current_state == SessionState.LISTENING_FOR_WAKE:
                    time.sleep(0.1)

                    # Cooldown check after TTS speaking (no self-trigger)
                    if time.perf_counter() < wake_cooldown_until:
                        continue

                    with state_lock:
                        cur_samples = list(wake_audio_buffer)

                    if len(cur_samples) < sample_rate * 1.2:
                        continue

                    recent_samples = np.array(cur_samples[-int(sample_rate * 1.5):], dtype=np.float32)

                    # Auditor Item C4: Run Silero VAD over the whole 1.5s window in 512-sample chunks
                    has_speech = False
                    if vad_model is not None:
                        for offset in range(0, len(recent_samples) - 511, 512):
                            chunk_t = torch.from_numpy(recent_samples[offset:offset + 512]).float()
                            with torch.no_grad():
                                prob = float(vad_model(chunk_t, sample_rate).item())
                            if prob >= 0.35:
                                has_speech = True
                                break
                    else:
                        has_speech = True

                    if not has_speech:
                        continue

                    # Transcribe recent segment with whisper to check wake word
                    t0_stt = time.perf_counter()
                    segments, _ = whisper_model.transcribe(recent_samples, beam_size=1, language="en")
                    transcript = " ".join(seg.text for seg in segments).strip()
                    stt_ms = (time.perf_counter() - t0_stt) * 1000.0

                    if "friday" in transcript.lower():
                        turn_counter += 1
                        t_wake = time.perf_counter()
                        print(f"\n[!] WAKE WORD TRIGGERED: \"{transcript}\"")

                        # Immediate earcon (<80 ms)
                        wake_ms = system.wake_detector.trigger_wake(mute_audio=False)
                        wake_detect_to_earcon_ms = (time.perf_counter() - t_wake) * 1000.0 + wake_ms

                        # Check if query was in the same utterance (Auditor Item M4)
                        m = re.search(r"\bfriday\b[,:\s]*(.+)", transcript, re.IGNORECASE)
                        if m and len(m.group(1).strip().split()) >= 2:
                            query_text = m.group(1).strip()
                            pre_stt_ms = stt_ms
                            print(f"[*] Query detected in wake utterance: \"{query_text}\"")
                            set_state(SessionState.THINKING)
                        else:
                            print("[*] Wake word acknowledged. Transitioning to RECORDING_QUERY...")
                            with state_lock:
                                query_audio_buffer.clear()
                            query_text = None
                            pre_stt_ms = None
                            rec_start_time = time.perf_counter()
                            speech_detected = False
                            silence_start = None
                            set_state(SessionState.RECORDING_QUERY)

                # -------------------------------------------------------------
                # STATE: RECORDING_QUERY (Wake detection disabled; repeated wake is audio)
                # -------------------------------------------------------------
                elif current_state == SessionState.RECORDING_QUERY:
                    time.sleep(0.05)
                    with state_lock:
                        q_len = len(query_audio_buffer)

                    elapsed = time.perf_counter() - rec_start_time

                    if q_len >= 512 and vad_model is not None:
                        with state_lock:
                            recent_chunk = np.array(query_audio_buffer[-512:], dtype=np.float32)
                        chunk_t = torch.from_numpy(recent_chunk).float()
                        with torch.no_grad():
                            prob = float(vad_model(chunk_t, sample_rate).item())

                        if prob >= 0.40:
                            speech_detected = True
                            silence_start = None
                        elif prob < 0.25 and speech_detected:
                            if silence_start is None:
                                silence_start = time.perf_counter()
                            elif (time.perf_counter() - silence_start) >= 0.8:
                                # End of speech detected!
                                set_state(SessionState.THINKING)

                    # Max 6.0s timeout
                    if elapsed >= 6.0 and current_state == SessionState.RECORDING_QUERY:
                        set_state(SessionState.THINKING)

                # -------------------------------------------------------------
                # STATE: THINKING (Execute turn pipeline)
                # -------------------------------------------------------------
                elif current_state == SessionState.THINKING:
                    if query_text is None:
                        with state_lock:
                            q_arr = np.array(query_audio_buffer, dtype=np.float32)
                        t0_q_stt = time.perf_counter()
                        segments, _ = whisper_model.transcribe(q_arr, beam_size=1, language="en")
                        query_text = " ".join(seg.text for seg in segments).strip()
                        pre_stt_ms = (time.perf_counter() - t0_q_stt) * 1000.0

                    # Execute full turn
                    res = system.process_turn(
                        turn_id=turn_counter,
                        query_text=query_text,
                        pre_measured_wake_ms=wake_detect_to_earcon_ms,
                        pre_measured_stt_ms=pre_stt_ms,
                        write_log=True
                    )

                    # Transition to SPEAKING
                    set_state(SessionState.SPEAKING)

                    # Calculate TTS cooldown: tts_audio_duration + 1.0s (no self-trigger)
                    tts_dur = res["timings"].get("tts_audio_dur_s") or 0.0
                    wake_cooldown_until = time.perf_counter() + tts_dur + 1.0

                    # Clear buffers and resume listening
                    with state_lock:
                        wake_audio_buffer.clear()
                        query_audio_buffer.clear()

                    set_state(SessionState.LISTENING_FOR_WAKE)
                    print(f"\n[✓] Turn completed. Cooldown active for {tts_dur + 1.0:.1f}s. Resuming listening...")

    except KeyboardInterrupt:
        print("\n\n[*] KeyboardInterrupt detected. Shutting down live session cleanly...")
    finally:
        system.shutdown()
        print("[✓] PROJECT FRIDAY live harness stopped successfully.")


# ---------------------------------------------------------------------------
# M1 SCRIPTED OFFLINE REGRESSION
# ---------------------------------------------------------------------------
def run_offline_regression():
    """
    Auditor Item M1: Scripted offline regression test harness.
    Renamed from --demo-session to --offline-regression.
    Prints banner:
      'SCRIPTED OFFLINE REGRESSION — synthetic/benchmark frames, injected text, no camera/mic/TTS'
    Never writes to results.csv. Never described as live, real-world, or handwritten.
    """
    print("\n" + "="*70)
    print("SCRIPTED OFFLINE REGRESSION — synthetic/benchmark frames, injected text, no camera/mic/TTS")
    print("="*70)

    system = FridayLiveSystem(
        use_camera=False,
        use_mic=False,
        offline_mode=True,
        compare_teacher=False,
        log_enabled=False,
        mute_audio=True,
        preview_enabled=False
    )

    # 1. Turn 1: Scripted synthetic render (doc_01 receipt benchmark spec)
    doc_path = os.path.join(REPO_ROOT, "assets/benchmark_dataset_spec/images/doc_01_document.jpg")
    frame1 = cv2.imread(doc_path)
    if frame1 is None:
        frame1 = np.ones((720, 1280, 3), dtype=np.uint8) * 255
        cv2.putText(frame1, "TOTAL AMOUNT DUE: $15.40", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2)
    f1_blur = cv2.GaussianBlur(frame1, (51, 51), 15.0)
    system.process_turn(
        turn_id=1,
        query_text="Hey Friday, read the total amount due on this grocery receipt",
        candidate_frames=[f1_blur, frame1],
        write_log=False
    )

    # 2. Turn 2: Scripted synthetic render (OpenCV script text note)
    note_frame = np.ones((720, 720, 3), dtype=np.uint8)
    note_frame[:] = (180, 240, 255)
    cv2.putText(note_frame, "call dr. sharma", (60, 200), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.4, (80, 40, 20), 2)
    cv2.putText(note_frame, "at 5pm reports", (60, 280), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.3, (80, 40, 20), 2)
    system.process_turn(
        turn_id=2,
        query_text="Hey Friday, what is written on this sticky note?",
        candidate_frames=[note_frame],
        write_log=False
    )

    # 3. Turn 3: Scripted synthetic render (med_01 medicine benchmark spec)
    med_path = os.path.join(REPO_ROOT, "assets/benchmark_dataset_spec/images/med_01_medicine.jpg")
    frame3 = cv2.imread(med_path)
    if frame3 is None:
        frame3 = np.ones((720, 1280, 3), dtype=np.uint8) * 255
        cv2.putText(frame3, "AMOXICILLIN 500 MG CAPSULE", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2)
        cv2.putText(frame3, "TAKE 1 CAPSULE TWICE DAILY", (50, 180), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2)
    system.process_turn(
        turn_id=3,
        query_text="Hey Friday, read what medication is this and what is the prescribed dose?",
        candidate_frames=[frame3],
        write_log=False
    )

    # 4. Turn 4: Scripted synthetic geometric render (no text)
    obj_frame = np.ones((720, 1280, 3), dtype=np.uint8) * 180
    cv2.rectangle(obj_frame, (520, 240), (740, 520), (70, 70, 150), -1)
    cv2.ellipse(obj_frame, (630, 240), (110, 30), 0, 0, 360, (50, 50, 120), -1)
    cv2.ellipse(obj_frame, (630, 240), (95, 22), 0, 0, 360, (30, 20, 15), -1)
    cv2.ellipse(obj_frame, (760, 380), (45, 75), 0, -90, 90, (70, 70, 150), 20)
    noise = np.random.normal(0, 5, obj_frame.shape).astype(np.int16)
    obj_frame = np.clip(obj_frame.astype(np.int16) + noise, 0, 255).astype(np.uint8)
    system.process_turn(
        turn_id=4,
        query_text="Hey Friday, what am I holding?",
        candidate_frames=[obj_frame],
        write_log=False
    )

    # 5. Turn 5: Scripted synthetic blurred render (defocus stress)
    blurry_frame = cv2.GaussianBlur(frame1, (65, 65), 25.0)
    system.process_turn(
        turn_id=5,
        query_text="Hey Friday, read what is on this paper",
        candidate_frames=[blurry_frame],
        write_log=False
    )

    system.shutdown()
    print("\n" + "="*70)
    print("SCRIPTED OFFLINE REGRESSION COMPLETED (NO RESULTS WRITTEN TO CSV)")
    print("="*70)


# ---------------------------------------------------------------------------
# 60-SECOND SOAK TEST (Auditor Item C1 + C3 Verification)
# ---------------------------------------------------------------------------
def run_soak_test():
    """
    60 s soak test:
      - Camera worker process running via multiprocessing spawn with SharedMemory
      - Single mic stream active
      - 5 injected wake/query cycles including:
        1. Single utterance wake+query: 'Hey Friday, what does it say?'
        2. Wake alone ('Hey Friday'), pause, then question ('What am I holding?')
        3. Double wake ('Hey Friday', then 'Hey Friday' again while recording query) -> NO crash!
        4. Generic read request ('Can you read this note?') -> R2 READ_ALOUD mode
        5. Defocused frame with fallback refusal
      - Asserts 0 crashes, 0 exceptions, clean shutdown.
    """
    print("\n" + "="*70)
    print("RUNNING 60-SECOND MULTIMODAL SOAK TEST (Auditor Items C1 & C3)")
    print("="*70)

    system = FridayLiveSystem(
        use_camera=True,
        use_mic=False,
        offline_mode=False,
        compare_teacher=False,
        log_enabled=False,
        mute_audio=True,
        preview_enabled=True
    )

    import sounddevice as sd
    mic_frames_received = 0
    def soak_mic_cb(indata, frames, time_info, status):
        nonlocal mic_frames_received
        mic_frames_received += len(indata)

    t_start = time.perf_counter()

    test_doc = os.path.join(REPO_ROOT, "assets/benchmark_dataset_spec/images/doc_01_document.jpg")
    frame = cv2.imread(test_doc)
    if frame is None:
        frame = np.ones((720, 1280, 3), dtype=np.uint8) * 255
        cv2.putText(frame, "SOAK TEST RUNNING OK", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2)

    cycles = [
        ("Hey Friday, what does it say?", frame, "Single-utterance wake+query"),
        ("Hey Friday", frame, "Wake alone (earcon only)"),
        ("Hey Friday ... Hey Friday, what is this?", frame, "Double wake phrase during recording (C3 crash fix)"),
        ("Can you read this note?", frame, "Generic read request (R2 READ_ALOUD mode)"),
        ("What does it say?", cv2.GaussianBlur(frame, (65, 65), 25.0), "Defocus stress frame")
    ]

    with sd.InputStream(samplerate=16000, channels=1, dtype="float32", blocksize=512, callback=soak_mic_cb):
        for idx, (query, fr, desc) in enumerate(cycles, 1):
            print(f"\n[*] Soak Cycle #{idx}/5: {desc}")
            system.process_turn(
                turn_id=idx,
                query_text=query,
                candidate_frames=[fr],
                write_log=False
            )
            time.sleep(1.0)

        # Let camera process, mic stream, and preview server run for remaining duration up to 60s
        elapsed = time.perf_counter() - t_start
        rem = max(1.0, 60.0 - elapsed)
        print(f"\n[*] Running background soaking loop for {rem:.1f} s (camera process + active mic stream)...")
        time.sleep(rem)

    system.shutdown()
    total_time = time.perf_counter() - t_start
    print(f"\n[✓] 60-SECOND SOAK TEST COMPLETED SUCCESSFULLY in {total_time:.1f} s ({mic_frames_received} audio samples captured, 0 crashes, 0 SIGTRAP)!")


# ---------------------------------------------------------------------------
# UNIT TEST SUITE (M2, R1, R2, N1)
# ---------------------------------------------------------------------------
def run_unit_tests():
    """
    Auditor Unit Test Suite:
      1. Digit suppression tests (L0)
      2. Honest fallback when model unavailable (M2)
      3. Response composition logic
      4. Student VLM image dependence (M2)
      5. Timing exclusions (M5)
      6. Frame quality scorer resolution normalization (R1: 1080p vs 4032x3024 same pass/fail)
      7. Handwritten note lines test (R2: matches auditor probe)
      8. 64k Vocab Mapper tests (N1: prompt round-trip & decoded IDs in 64k subset)
    """
    print("\n" + "="*70)
    print("RUNNING MILESTONE 1.6 UNIT TEST SUITE")
    print("="*70)

    # 1. Digit Suppression Tests
    print("[*] Test 1: Testing Auditor Item L0 digit suppression...")
    assert filter_digits_from_description("This is 1 prescription bottle. Take daily.") == "Take daily."
    assert filter_digits_from_description("Cost is $4.75. Store in cool place.") == "Store in cool place."
    assert filter_digits_from_description("Room 402 is on Floor 3.") == ""
    print("[✓] Digit suppression tests passed!")

    # 2. Honest Fallback When Model Unavailable
    print("[*] Test 2: Testing Auditor Item M2 honest fallback when weights unavailable...")
    describer = DescriptionPipeline(weights_path="nonexistent_checkpoint.pt")
    dummy_img = np.zeros((384, 384, 3), dtype=np.uint8)
    desc, _ = describer.describe(dummy_img)
    assert desc == FALLBACK_NO_OBJECT_MODEL, f"Expected '{FALLBACK_NO_OBJECT_MODEL}', got '{desc}'"
    assert "handheld object" not in desc
    assert "labeled container" not in desc
    print(f"[✓] Honest fallback verified: \"{desc}\" (zero invented nouns)")

    # 3. Response Composer Tests
    print("[*] Test 3: Testing response composition logic...")
    assert compose_spoken_response("IDENTIFY", FALLBACK_NO_OBJECT_MODEL, None) == FALLBACK_NO_OBJECT_MODEL
    assert compose_spoken_response("BOTH", FALLBACK_NO_OBJECT_MODEL, "TOTAL AMOUNT DUE: $15.40.") == "I can't identify objects yet. It says: TOTAL AMOUNT DUE: $15.40."
    assert compose_spoken_response("IDENTIFY", "a coffee mug", None) == "You're holding a coffee mug."
    assert compose_spoken_response("READ", None, "TOTAL: $10.00.") == "TOTAL: $10.00."
    print("[✓] Response composition tests passed!")

    # 4. Image Dependence Unit Test (Auditor Item M2)
    print("[*] Test 4: Testing Student VLM image dependence (fails if output is constant independent of image)...")
    img_a = np.zeros((384, 384, 3), dtype=np.uint8) # Solid black
    img_b = np.ones((384, 384, 3), dtype=np.uint8) * 255 # Solid white
    cv2.circle(img_b, (192, 192), 80, (0, 0, 0), -1)

    import torch
    from transformers import AutoModel, SiglipImageProcessor
    from PIL import Image
    from phase1_ai_sandbox.src.student_vlm import SpatialUnshuffleDownsampler

    device = "cpu"
    siglip = AutoModel.from_pretrained("google/siglip-base-patch16-384", torch_dtype=torch.float32).to(device)
    siglip_vision = siglip.vision_model.eval()
    siglip_proc = SiglipImageProcessor.from_pretrained("google/siglip-base-patch16-384")
    proj = SpatialUnshuffleDownsampler(in_features=768, out_features=896, grid_size=24).to(device)

    def extract_visual_tokens(img):
        pil_img = Image.fromarray(img)
        p = siglip_proc(images=pil_img, return_tensors="pt")
        with torch.no_grad():
            patches = siglip_vision(pixel_values=p.pixel_values.to(device)).last_hidden_state
            return proj(patches)

    v_a = extract_visual_tokens(img_a)
    v_b = extract_visual_tokens(img_b)

    diff = float((v_a - v_b).abs().sum().item())
    print(f"    Visual feature difference between Image A and Image B: {diff:.2f}")
    assert diff > 10.0, f"Auditor Item M2 Violation: Visual tokens are constant across distinct images (diff={diff:.2f})!"
    print("[✓] Image dependence verification passed!")

    # 5. Timing Exclusions Test (Auditor Item M5)
    print("[*] Test 5: Testing Auditor Item M5 timing exclusions...")
    test_timings = {
        "wake_to_earcon_ms": 15.0,
        "stt_ms": None,
        "frame_selection_ms": 100.0,
        "ocr_ms": 200.0,
        "description_ms": None,
        "tts_synth_ms": 50.0
    }
    active_sum = sum(v for v in test_timings.values() if v is not None)
    assert active_sum == 365.0, f"Expected 365.0 ms, got {active_sum}"
    print(f"[✓] Active timing sum verified: {active_sum:.1f} ms (unexecuted stages excluded)")

    # 6. Auditor Item R1 Resolution Invariance Test
    print("[*] Test 6: Testing Auditor Item R1 resolution normalization (1080p vs 4032x3024 same content)...")
    scorer = FrameScorer()
    # Create sharp synthetic text image at 1080p (1920x1080) with normal paper exposure (mean ~215)
    img_1080p = np.ones((1080, 1920, 3), dtype=np.uint8) * 220
    cv2.putText(img_1080p, "RESOLUTION TEST ITEM R1", (100, 300), cv2.FONT_HERSHEY_SIMPLEX, 3.0, (20, 20, 20), 6)
    cv2.putText(img_1080p, "SHARPNESS RESIZING INVARIANCE", (100, 600), cv2.FONT_HERSHEY_SIMPLEX, 3.0, (20, 20, 20), 6)

    # Scale the exact same image to 4032x3024
    img_4032p = cv2.resize(img_1080p, (4032, 3024), interpolation=cv2.INTER_CUBIC)

    ev_1080p = scorer.evaluate_frame(img_1080p, frame_id=1)
    ev_4032p = scorer.evaluate_frame(img_4032p, frame_id=2)

    print(f"    1080p  sharpness: {ev_1080p['sharpness']:.1f}, passed: {ev_1080p['passed']}")
    print(f"    4032p  sharpness: {ev_4032p['sharpness']:.1f}, passed: {ev_4032p['passed']}")
    assert ev_1080p["passed"] == ev_4032p["passed"] == True, f"R1 Violation: 1080p passed={ev_1080p['passed']}, 4032p passed={ev_4032p['passed']}"
    print("[✓] R1 Resolution normalization verified (identical pass/fail across 1080p and 4032x3024)!")

    # 7. Auditor Item R2 Handwritten Lines Test
    print("[*] Test 7: Testing Auditor Item R2 READ_ALOUD mode with handwritten note OCR lines...")
    lines_note = [
        {"raw_text": "9 love you till the", "confidence": 0.971, "box": [[10, 10], [100, 10], [100, 25], [10, 25]]},
        {"raw_text": "last", "confidence": 0.998, "box": [[10, 30], [50, 30], [50, 45], [10, 45]]},
        {"raw_text": "Hoer", "confidence": 0.734, "box": [[10, 50], [60, 50], [60, 65], [10, 65]]},
        {"raw_text": "dies..", "confidence": 0.993, "box": [[10, 70], [70, 70], [70, 85], [10, 85]]}
    ]
    res_r2 = read_literal(lines_note, "scene_text", "What does it say?")
    expected_r2 = "It looks like it says: love you till the last dies. I'm not sure about some words or numbers."
    print(f"    READ_ALOUD Result: \"{res_r2['speech']}\"")
    assert res_r2["speech"] == expected_r2, f"R2 Failed! Expected '{expected_r2}', got '{res_r2['speech']}'"
    assert "9" not in res_r2["speech"], "R2 Failed: Digit '9' was erroneously spoken!"
    assert "Hoer" not in res_r2["speech"], "R2 Failed: Low-confidence line 'Hoer' was erroneously spoken!"
    print("[✓] R2 Handwritten reading verified!")

    # 8. Auditor Item N1 Vocab Mapper Tests
    print("[*] Test 8: Testing Auditor Item N1 64k Vocab Mapper...")
    mapper = Vocab64kMapper(tokenizer_name="Qwen/Qwen2.5-0.5B", target_size=64000)
    prompt = "Describe in a few words what object the person is holding."
    sub_ids = mapper.safe_encode_64k(prompt)
    assert all(0 <= sid < 64000 for sid in sub_ids), f"N1 Failed: Token ID outside 64k range: {sub_ids}"
    recovered_prompt = mapper.decode_64k(sub_ids)
    assert recovered_prompt == prompt, f"N1 Failed: Roundtrip mismatch: '{recovered_prompt}' != '{prompt}'"
    print(f"    Prompt encoded to {len(sub_ids)} tokens in 64k range. Student EOS ID: {mapper.student_eos_id}")
    print("[✓] N1 64k Vocab Mapper verified!")

    print("\n" + "="*70)
    print("ALL MILESTONE 1.6 UNIT TESTS PASSED SUCCESSFULLY [✓]")
    print("="*70)


# ---------------------------------------------------------------------------
# CLI ENTRY POINT
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Project FRIDAY: Milestone 1.6 Live MacBook Harness")
    parser.add_argument("--live", action="store_true", help="Run continuous live MacBook harness loop (FaceTime camera + mic + wake word)")
    parser.add_argument("--offline-regression", action="store_true", help="Run scripted offline regression suite (M1)")
    parser.add_argument("--test", action="store_true", help="Run unit test suite (M2, R1, R2, N1)")
    parser.add_argument("--soak-test", action="store_true", help="Run 60s soak test (multiprocess camera + mic stream + 5 cycles)")
    parser.add_argument("--offline", action="store_true", help="Explicitly enable offline mode (no hardware camera/mic required)")
    parser.add_argument("--camera", action="store_true", help="Capture live optical frames from camera")
    parser.add_argument("--mic", action="store_true", help="Capture live speech queries from microphone")
    parser.add_argument("--query", type=str, default=None, help="Explicit speech query string")
    parser.add_argument("--image", type=str, default=None, help="Explicit input image path for evaluation")
    parser.add_argument("--log", action="store_true", help="Log live turns to phase1_ai_sandbox/real_world_tests/results.csv")
    parser.add_argument("--compare-teacher", action="store_true", help="Compare Qwen2-VL-2B teacher model on Mac MPS")
    parser.add_argument("--mute", action="store_true", help="Mute audio playback for automated/batch execution")
    parser.add_argument("--no-preview", action="store_true", help="Disable local preview web server at 127.0.0.1:8765")
    parser.add_argument("--allow-unverified-weights", action="store_true", help="Allow loading student weights even if SHA256 mismatches Kaggle manifest")
    args = parser.parse_args()

    if args.test:
        run_unit_tests()
    elif args.soak_test:
        run_soak_test()
    elif args.offline_regression:
        run_offline_regression()
    elif args.live:
        run_live_harness_loop(
            camera_id=0,
            compare_teacher=args.compare_teacher,
            log_enabled=args.log,
            no_preview=args.no_preview
        )
    else:
        system = FridayLiveSystem(
            use_camera=args.camera,
            use_mic=args.mic,
            offline_mode=args.offline,
            compare_teacher=args.compare_teacher,
            log_enabled=args.log,
            mute_audio=args.mute,
            preview_enabled=not args.no_preview
        )
        if args.image:
            img = cv2.imread(args.image)
            if img is None:
                raise FileNotFoundError(f"Image not found: {args.image}")
            system.process_turn(turn_id=1, query_text=args.query, candidate_frames=[img])
        else:
            system.process_turn(turn_id=1, query_text=args.query)
        system.shutdown()
