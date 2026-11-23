#!/usr/bin/env python3
"""
PROJECT FRIDAY - KOKORO-82M NEURAL VOICE AUDIT & EVALUATION (Auditor Item D1)
Evaluates Kokoro-82M INT8 ONNX on CPU across all 40 DEV speeches (+ REFUSAL_TEXT).
Measures real sample rate, RTF (synthesis time / audio duration), and peak RAM.
Exports 6 listening WAV artifacts under phase1_ai_sandbox/eval_runs/<sha>/kokoro/.
Enforces format_tts_spacing() on all speeches before synthesis.
"""

import os
import sys
import json
import time
import argparse
import resource
import soundfile as sf
import numpy as np

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)
src_dir = os.path.join(REPO_ROOT, "phase1_ai_sandbox/src")
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

from kokoro_onnx import Kokoro
from phase1_ai_sandbox.src.kokoro_voice_engine import format_tts_spacing
from phase1_ai_sandbox.src.benchmark_dataset_evaluator import REFUSAL_TEXT
from phase1_ai_sandbox.src.eval_provenance import get_eval_provenance

SIX_TARGET_PHRASES = [
    ("0.5 mg", "0.5_mg.wav"),
    ("$4.75", "4.75.wav"),
    ("EVERY 4 TO 6 HOURS", "every_4_to_6_hours.wav"),
    ("B24", "b24.wav"),
    ("14:15", "14_15.wav"),
    (REFUSAL_TEXT, "refusal.wav"),
]

def run_kokoro_audit(output_dir: str = None, allow_dirty: bool = False) -> dict:
    full_sha, short_sha, is_dirty, diff_hash = get_eval_provenance(REPO_ROOT, allow_dirty=allow_dirty)

    if output_dir is None:
        output_dir = os.path.join(REPO_ROOT, "phase1_ai_sandbox/eval_runs", short_sha, "kokoro")
    os.makedirs(output_dir, exist_ok=True)

    # 1. Load dev literal_reader.json speeches
    reader_json_candidates = [
        os.path.join(REPO_ROOT, "phase1_ai_sandbox/eval_runs", short_sha, "literal_reader.json"),
        os.path.join(REPO_ROOT, "phase1_ai_sandbox/eval_runs/449cbcb/literal_reader.json"),
        os.path.join(REPO_ROOT, "phase1_ai_sandbox/eval_runs/a8d4439/literal_reader.json"),
    ]
    reader_json = None
    for c in reader_json_candidates:
        if os.path.exists(c):
            reader_json = c
            break

    if not reader_json:
        raise FileNotFoundError(f"Could not locate literal_reader.json for DEV speeches in candidate locations: {reader_json_candidates}")

    with open(reader_json, "r", encoding="utf-8") as f:
        dev_report = json.load(f)

    dev_items = dev_report.get("per_item_results", [])
    if len(dev_items) < 40:
        raise ValueError(f"Expected 40 dev items in {reader_json}, found {len(dev_items)}")

    # Collect 40 speeches
    speeches = []
    for item in dev_items:
        speeches.append({
            "id": item["id"],
            "speech": item["speech"]
        })
    # Add REFUSAL_TEXT as 41st item
    speeches.append({
        "id": "refusal_protocol",
        "speech": REFUSAL_TEXT
    })

    # 2. Initialize Kokoro-82M ONNX model
    model_path = os.path.join(REPO_ROOT, "assets/kokoro/kokoro-v1.0.int8.onnx")
    voices_path = os.path.join(REPO_ROOT, "assets/kokoro/voices-v1.0.bin")
    if not os.path.exists(model_path) or not os.path.exists(voices_path):
        raise FileNotFoundError(f"Kokoro model files missing: {model_path} or {voices_path}")

    print("=" * 70)
    print("PROJECT FRIDAY - KOKORO-82M NEURAL VOICE BENCHMARK (Auditor Item D1)")
    print("=" * 70)
    print(f"Git Commit SHA : {full_sha} (short: {short_sha}, dirty: {is_dirty})")
    print(f"Speech Samples : {len(speeches)} total (40 DEV speeches + 1 REFUSAL_TEXT)")
    print(f"Voice Persona  : bf_emma (Locked British Female)")
    print(f"Model Artifact : {model_path}")
    print(f"Output Target  : {output_dir}\n")

    t_init_0 = time.perf_counter()
    kokoro = Kokoro(model_path, voices_path)
    t_init = (time.perf_counter() - t_init_0) * 1000.0
    print(f"[✓] Kokoro-82M initialized in {t_init:.1f} ms on CPU.\n")

    sample_rate_recorded = None
    rtf_list = []
    synth_time_list = []
    audio_dur_list = []
    item_results = []

    for idx, s_info in enumerate(speeches):
        sid = s_info["id"]
        raw_text = s_info["speech"]
        tts_text = format_tts_spacing(raw_text)

        t0 = time.perf_counter()
        samples, sr = kokoro.create(tts_text, voice="bf_emma", speed=1.0, lang="en-us")
        t_synth = time.perf_counter() - t0

        if sample_rate_recorded is None:
            sample_rate_recorded = int(sr)

        dur_s = len(samples) / float(sr)
        rtf = t_synth / dur_s if dur_s > 0 else 0.0

        rtf_list.append(rtf)
        synth_time_list.append(t_synth)
        audio_dur_list.append(dur_s)

        # Track memory
        # On macOS ru_maxrss is bytes; on Linux it is KB
        rss_raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        if sys.platform == "darwin":
            rss_mb = rss_raw / (1024 * 1024)
        else:
            rss_mb = rss_raw / 1024

        item_results.append({
            "id": sid,
            "raw_text": raw_text,
            "tts_formatted_text": tts_text,
            "sample_rate_hz": int(sr),
            "synthesis_time_s": round(t_synth, 4),
            "audio_duration_s": round(dur_s, 4),
            "rtf": round(rtf, 4),
            "peak_ram_mb": round(rss_mb, 2)
        })

        print(f"[{idx+1:02d}/{len(speeches)}] {sid:<18s} | Dur: {dur_s:5.2f}s | Synth: {t_synth*1000:6.1f}ms | RTF: {rtf:.3f} | Text: '{tts_text}'")

    # 3. Synthesize and export the 6 canonical listening WAV files
    print("\n" + "=" * 70)
    print("SAVING 6 LISTENING WAV ARTIFACTS (Auditor Item D1)")
    print("=" * 70)
    saved_wav_paths = {}
    for phrase, fname in SIX_TARGET_PHRASES:
        tts_phrase = format_tts_spacing(phrase)
        samples, sr = kokoro.create(tts_phrase, voice="bf_emma", speed=1.0, lang="en-us")
        wav_out = os.path.join(output_dir, fname)
        sf.write(wav_out, samples, sr)
        dur = len(samples) / float(sr)
        saved_wav_paths[phrase] = wav_out
        print(f"  [✓] '{phrase}' -> {os.path.relpath(wav_out, REPO_ROOT)} ({dur:.2f}s, {sr} Hz)")

    # 4. Final Aggregates
    mean_rtf = float(np.mean(rtf_list))
    min_rtf = float(np.min(rtf_list))
    max_rtf = float(np.max(rtf_list))
    p95_rtf = float(np.percentile(rtf_list, 95))
    total_audio_s = float(np.sum(audio_dur_list))
    total_synth_s = float(np.sum(synth_time_list))
    peak_ram_mb = float(max(r["peak_ram_mb"] for r in item_results))

    faster_than_realtime = bool(mean_rtf < 1.0)
    g4_passed = bool(faster_than_realtime and sample_rate_recorded == 24000)

    kokoro_audit_report = {
        "git_commit_sha": full_sha,
        "short_sha": short_sha,
        "dirty": is_dirty,
        "diff_hash": diff_hash,
        "model_architecture": "Kokoro-82M",
        "quantization": "INT8 ONNX",
        "device": "CPU",
        "voice_persona": "bf_emma",
        "total_speeches_measured": len(speeches),
        "gate_4_metrics": {
            "passed": g4_passed,
            "sample_rate_hz": sample_rate_recorded,
            "faster_than_realtime": faster_than_realtime,
            "mean_rtf": round(mean_rtf, 4),
            "min_rtf": round(min_rtf, 4),
            "max_rtf": round(max_rtf, 4),
            "p95_rtf": round(p95_rtf, 4),
            "peak_ram_mb": round(peak_ram_mb, 2),
            "total_audio_duration_s": round(total_audio_s, 2),
            "total_synthesis_time_s": round(total_synth_s, 2),
            "speedup_factor": round(1.0 / mean_rtf, 2) if mean_rtf > 0 else None,
            "status": f"MEASURED (Kokoro-82M INT8 ONNX on CPU: {sample_rate_recorded} Hz, RTF {mean_rtf:.3f}, Peak RAM {peak_ram_mb:.1f} MB)"
        },
        "saved_wav_artifacts": saved_wav_paths,
        "per_speech_metrics": item_results
    }

    report_path = os.path.join(output_dir, "kokoro_eval.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(kokoro_audit_report, f, indent=2)

    print("\n" + "=" * 70)
    print("KOKORO-82M VOICE SYNTHESIS GATE 4 SUMMARY")
    print("=" * 70)
    print(f"Sample Rate           : {sample_rate_recorded} Hz")
    print(f"Mean RTF              : {mean_rtf:.3f} ({(1.0/mean_rtf):.1f}x real-time speed)")
    print(f"Min / Max / P95 RTF   : {min_rtf:.3f} / {max_rtf:.3f} / {p95_rtf:.3f}")
    print(f"Total Speech Audio    : {total_audio_s:.2f} s synthesized in {total_synth_s:.2f} s")
    print(f"Peak RAM Usage        : {peak_ram_mb:.2f} MB")
    print(f"Gate 4 Status         : {'PASS [✓]' if g4_passed else 'FAIL [X]'} (Faster than real-time: {faster_than_realtime})")
    print("=" * 70)
    print(f"[✓] Kokoro Report saved to: {report_path}\n")

    return kokoro_audit_report

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Kokoro-82M TTS evaluation across dev speeches.")
    parser.add_argument("--output-dir", type=str, default=None, help="Explicit output directory.")
    parser.add_argument("--allow-dirty", action="store_true", help="Allow running on dirty working tree.")
    args = parser.parse_args()
    run_kokoro_audit(output_dir=args.output_dir, allow_dirty=args.allow_dirty)
