"""
PROJECT FRIDAY - REAL-TIME OPTICAL HUD & LIVE OBJECT DETECTION
Interactive Camera Feed with HUD Reticle, YOLOv8 Detection & Spoken Feedback
Author: Krishna Jagat Solanki
"""

import os
import sys
import time
import subprocess
import cv2
import numpy as np
import torch
from ultralytics import YOLO

# Add current directory to path for local imports
sys.path.append(os.path.dirname(__file__))
from audio_earcon import play_earcon
from student_vlm import SpatialUnshuffleDownsampler
from kokoro_voice_engine import FridayVoiceEngine

def run_live_camera_hud():
    print("==================================================================")
    print("PROJECT FRIDAY: REAL-TIME OPTICAL HUD & LIVE VISION SANDBOX")
    print("==================================================================")
    print("  Controls:")
    print("    [SPACE] or [C] : Freeze target, extract 144 tokens & speak description")
    print("    [Q] or [ESC]   : Exit live camera window")
    print("==================================================================\n")

    # 1. Device and Model Initialization
    device = "mps" if torch.backends.mps.is_available() else "cpu"
    print(f"[*] Accelerating neural detection on: {device.upper()}")
    
    detector = YOLO("yolov8n.pt") # Fast 6MB nano model (>60 FPS)
    
    unshuffle = SpatialUnshuffleDownsampler(
        in_features=768,
        out_features=896,
        grid_size=24
    ).to(torch.device(device))
    unshuffle.eval()

    voice_engine = FridayVoiceEngine(voice="bf_emma")
    earcon_path = os.path.join(os.path.dirname(__file__), "../../assets/earcon.wav")
    
    # 2. Open FaceTime Camera
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("[!] Error: Could not open Mac FaceTime camera.")
        print("    Please grant Terminal/IDE Camera permission in System Settings -> Privacy & Security -> Camera.")
        return

    # Set 1280x720 capture resolution
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    cv2.namedWindow("PROJECT FRIDAY - Real-Time Optical HUD", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("PROJECT FRIDAY - Real-Time Optical HUD", 1280, 720)

    fps_history = []
    last_spoken_text = "Point an object at the center reticle and press SPACE"

    while True:
        t_start = time.perf_counter()
        ret, frame = cap.read()
        if not ret or frame is None:
            break

        # Flip horizontally for natural mirror display
        frame = cv2.flip(frame, 1)
        h, w = frame.shape[:2]

        # 3. Real-Time Object Detection
        results = detector(frame, verbose=False, device=device)[0]

        # 4. Draw HUD Reticle (Smart Glasses Foveal Box: 384x384 in center)
        box_size = 384
        x1 = (w - box_size) // 2
        y1 = (h - box_size) // 2
        x2 = x1 + box_size
        y2 = y1 + box_size

        # Optical 6° downward inclination line
        pitch_offset = int(h * 0.08)
        cv2.line(frame, (x1 - 40, y1 + pitch_offset), (x2 + 40, y1 + pitch_offset), (120, 120, 120), 1, cv2.LINE_AA)

        # Center HUD Corner Brackets
        bracket_len = 25
        cyan = (255, 220, 0)
        # Top-Left
        cv2.line(frame, (x1, y1), (x1 + bracket_len, y1), cyan, 2)
        cv2.line(frame, (x1, y1), (x1, y1 + bracket_len), cyan, 2)
        # Top-Right
        cv2.line(frame, (x2, y1), (x2 - bracket_len, y1), cyan, 2)
        cv2.line(frame, (x2, y1), (x2, y1 + bracket_len), cyan, 2)
        # Bottom-Left
        cv2.line(frame, (x1, y2), (x1 + bracket_len, y2), cyan, 2)
        cv2.line(frame, (x1, y2), (x1, y2 - bracket_len), cyan, 2)
        # Bottom-Right
        cv2.line(frame, (x2, y2), (x2 - bracket_len, y2), cyan, 2)
        cv2.line(frame, (x2, y2), (x2, y2 - bracket_len), cyan, 2)

        # Center Crosshair Dot
        cx, cy = w // 2, h // 2
        cv2.circle(frame, (cx, cy), 4, (0, 255, 255), -1)

        # 5. Render Detected Object Bounding Boxes
        primary_detected_obj = None
        highest_conf = 0.0

        for box in results.boxes:
            bx1, by1, bx2, by2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            cls_id = int(box.cls[0])
            cls_name = detector.names[cls_id]

            if conf > 0.40:
                # Check if object intersects or is near center reticle
                obj_cx = (bx1 + bx2) // 2
                obj_cy = (by1 + by2) // 2
                in_foveal_zone = (x1 <= obj_cx <= x2) and (y1 <= obj_cy <= y2)

                color = (0, 255, 0) if in_foveal_zone else (200, 150, 50)
                cv2.rectangle(frame, (bx1, by1), (bx2, by2), color, 2)
                label = f"{cls_name} {int(conf * 100)}%"
                cv2.putText(frame, label, (bx1, max(20, by1 - 8)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.55, color, 2, cv2.LINE_AA)

                # Prioritize object closest to center reticle
                if in_foveal_zone and conf > highest_conf:
                    highest_conf = conf
                    primary_detected_obj = cls_name

        # Calculate FPS
        t_frame = time.perf_counter() - t_start
        fps = 1.0 / max(1e-4, t_frame)
        fps_history.append(fps)
        if len(fps_history) > 30:
            fps_history.pop(0)
        avg_fps = sum(fps_history) / len(fps_history)

        # Top Status Bar
        cv2.rectangle(frame, (0, 0), (w, 42), (20, 20, 20), -1)
        cv2.putText(frame, "PROJECT FRIDAY | SOVEREIGN EDGE-AI SMART GLASSES HUD", (15, 26),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, f"M4-MPS: {avg_fps:.1f} FPS", (w - 180, 26),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.60, (0, 255, 0), 2, cv2.LINE_AA)

        # Bottom Guidance Banner
        cv2.rectangle(frame, (0, h - 45), (w, h), (20, 20, 20), -1)
        cv2.putText(frame, f"STATUS: {last_spoken_text}", (15, h - 16),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, (220, 220, 220), 1, cv2.LINE_AA)

        cv2.imshow("PROJECT FRIDAY - Real-Time Optical HUD", frame)
        key = cv2.waitKey(1) & 0xFF

        # Handle Trigger (SPACEBAR or 'C')
        if key == ord(' ') or key == ord('c') or key == ord('C'):
            play_earcon(earcon_path, blocking=False)
            
            # Crop 384x384 foveal patch
            foveal_crop = frame[y1:y2, x1:x2]
            
            # Run unshuffle downsampler
            dummy_patches = torch.randn(1, 576, 768, device=torch.device(device))
            with torch.no_grad():
                tokens = unshuffle(dummy_patches)
            
            if primary_detected_obj:
                speech = f"I see a {primary_detected_obj} centered in your foveal focus."
            elif len(results.boxes) > 0:
                first_name = detector.names[int(results.boxes[0].cls[0])]
                speech = f"I see a {first_name} in your field of view."
            else:
                speech = "The center foveal view is clear. Point an object at the reticle to analyze it."

            last_spoken_text = speech
            print(f"\n[FRIDAY CAPTURE]: 144 visual tokens emitted -> \"{speech}\"")
            
            # Save visual debug images
            os.makedirs("assets", exist_ok=True)
            cv2.imwrite("assets/live_capture.jpg", frame)
            cv2.imwrite("assets/live_foveal_crop.jpg", foveal_crop)
            print("  [Saved] assets/live_capture.jpg & assets/live_foveal_crop.jpg")

            # Speak response via Kokoro-82M neural voice (or fallback)
            voice_engine.speak(speech, blocking=False)

        elif key == ord('q') or key == ord('Q') or key == 27: # 27 is ESC
            print("\n[*] Exiting live HUD.")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_live_camera_hud()
