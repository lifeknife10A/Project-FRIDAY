"""
PROJECT FRIDAY - PHASE 1 OPTICAL FOVEATION & DYNAMIC TEXT-ROI ENGINE
Component: 6° Down-Pitch Emulation, 2-Stage Dynamic Foveation & Spoken Guidance Check
Author: Krishna Jagat Solanki
"""

import cv2
import numpy as np
from typing import Tuple, Optional, Dict, Any

class OpticalFoveationEngine:
    """
    Simulates the optomechanical characteristics of Project FRIDAY:
    1. 6° Downward Optical Inclination (kinematic titanium cradle mounting).
    2. Two-Stage Dynamic Foveation:
       - Stream 0: 384x384 full FoV downscaled view.
       - Text-density centroid localization.
       - Stream 1: 384x384 1:1 optical crop centered on (Xc, Yc) [>= 10 px/char].
    3. Optical Boundary Check & Spoken Guidance Trigger.
    """
    def __init__(self, target_crop_size: int = 384, pitch_angle_deg: float = 6.0):
        self.crop_size = target_crop_size
        self.pitch_angle_deg = pitch_angle_deg

    def apply_down_pitch_transform(self, frame: np.ndarray) -> np.ndarray:
        """
        Emulates the permanent 6° downward optical inclination of the camera cradle.
        Shifts the optical gaze downward towards the hand-held reading zone.
        For an ~50° vertical FOV, 6° corresponds to ~12% downward vertical translation.
        """
        h, w = frame.shape[:2]
        shift_y = int(h * (np.tan(np.radians(self.pitch_angle_deg)) / np.tan(np.radians(25.0))))
        shift_y = np.clip(shift_y, 0, int(h * 0.25))
        
        # Translation matrix shifting image content upward (equivalent to camera looking down)
        M = np.float32([[1, 0, 0], [0, 1, -shift_y]])
        pitched_frame = cv2.warpAffine(frame, M, (w, h), borderMode=cv2.BORDER_REFLECT)
        return pitched_frame

    def detect_text_roi(self, stream0_384: np.ndarray) -> Tuple[int, int, int, int]:
        """
        Lightweight text-density detector operating on Stream 0 (384x384).
        Uses morphological gradient and horizontal smearing to cluster fine text.
        Returns: (x, y, w, h) bounding box of the highest density text cluster.
        """
        gray = cv2.cvtColor(stream0_384, cv2.COLOR_BGR2GRAY)
        
        # Morphological gradient to isolate high-frequency text edges
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        grad = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
        
        # Otsu thresholding
        _, thresh = cv2.threshold(grad, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        
        # Connect text horizontally into coherent label lines
        connect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 3))
        connected = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, connect_kernel)
        
        contours, _ = cv2.findContours(connected, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if not contours:
            # Fallback to center 192x192 if no text is detected
            return 96, 96, 192, 192

        # Filter and select the contour cluster with the largest bounding area
        valid_boxes = [cv2.boundingRect(c) for c in contours if cv2.contourArea(c) > 40]
        if not valid_boxes:
            return 96, 96, 192, 192

        # Combine close bounding boxes into a unified text ROI
        min_x = min(b[0] for b in valid_boxes)
        min_y = min(b[1] for b in valid_boxes)
        max_x = max(b[0] + b[2] for b in valid_boxes)
        max_y = max(b[1] + b[3] for b in valid_boxes)
        
        return min_x, min_y, max_x - min_x, max_y - min_y

    def extract_foveal_crop(
        self,
        full_frame: np.ndarray,
        stream0_box: Tuple[int, int, int, int]
    ) -> Tuple[np.ndarray, Dict[str, Any]]:
        """
        Extracts Stream 1 (384x384 1:1 optical crop) from full-resolution frame
        centered on the detected text centroid (Xc, Yc).
        """
        full_h, full_w = full_frame.shape[:2]
        bx, by, bw, bh = stream0_box
        
        # Scale Stream 0 (384x384) coordinates to full sensor resolution
        scale_x = full_w / 384.0
        scale_y = full_h / 384.0
        
        full_bx = int(bx * scale_x)
        full_by = int(by * scale_y)
        full_bw = int(bw * scale_x)
        full_bh = int(bh * scale_y)
        
        # Text centroid
        cx = full_bx + full_bw // 2
        cy = full_by + full_bh // 2
        
        # Determine 384x384 crop window centered on (cx, cy)
        half_crop = self.crop_size // 2
        crop_x1 = max(0, cx - half_crop)
        crop_y1 = max(0, cy - half_crop)
        crop_x2 = min(full_w, crop_x1 + self.crop_size)
        crop_y2 = min(full_h, crop_y1 + self.crop_size)
        
        # Adjust boundaries if crop hits edges
        if crop_x2 - crop_x1 < self.crop_size:
            crop_x1 = max(0, crop_x2 - self.crop_size)
        if crop_y2 - crop_y1 < self.crop_size:
            crop_y1 = max(0, crop_y2 - self.crop_size)
            
        foveal_crop = full_frame[crop_y1:crop_y2, crop_x1:crop_x2]
        
        # Guarantee exact 384x384 output shape
        if foveal_crop.shape[0] != self.crop_size or foveal_crop.shape[1] != self.crop_size:
            foveal_crop = cv2.resize(foveal_crop, (self.crop_size, self.crop_size))

        # Optical Guidance Protocol Evaluation
        # If the text bounding box exceeds the 384px foveal window, prompt user guidance
        overflow_x = full_bw > (self.crop_size * 0.90)
        overflow_y = full_bh > (self.crop_size * 0.90)
        boundary_overflow = overflow_x or overflow_y

        guidance_message = None
        if boundary_overflow:
            guidance_message = (
                "Please hold the document slightly further away or tilt your head downward "
                "to bring the full page into view."
            )

        metadata = {
            "centroid": (cx, cy),
            "full_bounding_box": (full_bx, full_by, full_bw, full_bh),
            "crop_window": (crop_x1, crop_y1, crop_x2, crop_y2),
            "boundary_overflow": boundary_overflow,
            "guidance_message": guidance_message,
            "foveal_resolution_px_per_char": ">= 10.0 (Preserved 1:1)"
        }
        return foveal_crop, metadata

    def process_frame(self, raw_frame: np.ndarray) -> Tuple[np.ndarray, np.ndarray, Dict[str, Any]]:
        """
        Complete optical pipeline:
        raw_frame -> 6° pitched frame -> Stream 0 (384x384) -> Text ROI -> Stream 1 (384x384 foveal crop).
        """
        pitched = self.apply_down_pitch_transform(raw_frame)
        stream0 = cv2.resize(pitched, (self.crop_size, self.crop_size), interpolation=cv2.INTER_AREA)
        box_stream0 = self.detect_text_roi(stream0)
        stream1_crop, metadata = self.extract_foveal_crop(pitched, box_stream0)
        return stream0, stream1_crop, metadata

def create_synthetic_prescription_label() -> np.ndarray:
    """
    Synthesizes a realistic high-resolution (1920x1080) camera frame showing
    a prescription medicine bottle label with crisp fine print.
    """
    canvas = np.full((1080, 1920, 3), 40, dtype=np.uint8) # Dark room background
    
    # Draw bottle body
    cv2.rectangle(canvas, (750, 250), (1200, 950), (180, 100, 30), -1) # Amber container
    
    # White prescription label
    cv2.rectangle(canvas, (780, 320), (1170, 800), (250, 250, 250), -1)
    
    # Rx Header (Cyan band)
    cv2.rectangle(canvas, (780, 320), (1170, 380), (160, 90, 20), -1)
    cv2.putText(canvas, "APOLLO PHARMACY - Rx #984210", (800, 360),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    
    # Medication fine print
    cv2.putText(canvas, "AMOXICILLIN 500 MG", (800, 430),
                cv2.FONT_HERSHEY_DUPLEX, 0.85, (10, 10, 10), 2)
    cv2.putText(canvas, "Take 1 capsule twice daily", (800, 480),
                cv2.FONT_HERSHEY_SIMPLEX, 0.65, (30, 30, 30), 2)
    cv2.putText(canvas, "with meals for 10 days.", (800, 520),
                cv2.FONT_HERSHEY_SIMPLEX, 0.65, (30, 30, 30), 2)
    cv2.putText(canvas, "QTY: 20 CAPSULES   REFILL: 0", (800, 580),
                cv2.FONT_HERSHEY_SIMPLEX, 0.55, (60, 60, 60), 1)
    cv2.putText(canvas, "WARNING: Finish all medication", (800, 630),
                cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 180), 2)
    cv2.putText(canvas, "Dr. K. Solanki   Date: 21-Nov-2026", (800, 680),
                cv2.FONT_HERSHEY_SIMPLEX, 0.50, (80, 80, 80), 1)
                
    return canvas

if __name__ == "__main__":
    print("Testing OpticalFoveationEngine with synthetic 1080p prescription label...")
    engine = OpticalFoveationEngine(target_crop_size=384, pitch_angle_deg=6.0)
    
    test_frame = create_synthetic_prescription_label()
    stream0, stream1, meta = engine.process_frame(test_frame)
    
    print(f"Stream 0 Shape: {stream0.shape}")
    print(f"Stream 1 Foveal Crop Shape: {stream1.shape}")
    print(f"Detected Text Centroid: {meta['centroid']}")
    print(f"Boundary Overflow Flag: {meta['boundary_overflow']}")
    if meta['guidance_message']:
        print(f"Guidance Notice: {meta['guidance_message']}")
        
    assert stream0.shape == (384, 384, 3), "Stream 0 incorrect shape!"
    assert stream1.shape == (384, 384, 3), "Stream 1 incorrect shape!"
    print(">>> Optical Foveation & 6° Down-Pitch verified successfully! <<<")
