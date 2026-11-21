import cv2
import os

def extract_uniform_frames(video_path, output_dir, interval_seconds=15):
    os.makedirs(output_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error opening video {video_path}")
        return
        
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total_frames / fps
    print(f"Video FPS: {fps:.2f}, Total Frames: {total_frames}, Duration: {duration:.1f}s")
    
    frame_interval = int(fps * interval_seconds)
    frame_idx = 0
    saved_count = 0
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
            
        if frame_idx % frame_interval == 0:
            timestamp_sec = frame_idx / fps
            m = int(timestamp_sec // 60)
            s = int(timestamp_sec % 60)
            filename = f"frame_{m:02d}_{s:02d}.jpg"
            out_path = os.path.join(output_dir, filename)
            cv2.imwrite(out_path, frame, [cv2.IMWRITE_JPEG_QUALITY, 85])
            saved_count += 1
            print(f"Saved {filename} ({m:02d}:{s:02d})")
            
        frame_idx += 1
        
    cap.release()
    print(f"Extracted {saved_count} frames into {output_dir}")

if __name__ == "__main__":
    extract_uniform_frames(
        "/Users/krish/Downloads/Ray-Ban Meta Smart Glasses Teardown.mp4",
        "/Users/krish/NMIMS/Friday/teardown_analysis/frames",
        interval_seconds=15
    )
