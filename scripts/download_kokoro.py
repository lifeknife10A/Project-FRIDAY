"""
PROJECT FRIDAY - KOKORO-82M ONNX DOWNLOADER
Downloads Kokoro v1.0 INT8 model and voices binary into assets/kokoro/
Author: Krishna Jagat Solanki
"""

import os
import sys
import urllib.request
from tqdm import tqdm

class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)

def download_file(url: str, output_path: str):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    if os.path.exists(output_path):
        print(f"[*] Already exists: {output_path} ({os.path.getsize(output_path)/1e6:.1f} MB)")
        return
        
    print(f"[*] Downloading {os.path.basename(output_path)} from {url}...")
    with DownloadProgressBar(unit='B', unit_scale=True, miniters=1, desc=os.path.basename(output_path)) as t:
        urllib.request.urlretrieve(url, filename=output_path, reporthook=t.update_to)
    print(f"[✓] Downloaded to: {output_path}\n")

if __name__ == "__main__":
    base_url = "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.1"
    model_url = f"{base_url}/kokoro-v1.0.int8.onnx"
    voices_url = f"{base_url}/voices-v1.0.bin"
    
    target_dir = os.path.join(os.path.dirname(__file__), "../assets/kokoro")
    os.makedirs(target_dir, exist_ok=True)
    
    download_file(voices_url, os.path.join(target_dir, "voices-v1.0.bin"))
    download_file(model_url, os.path.join(target_dir, "kokoro-v1.0.int8.onnx"))
    print("[✓] All Kokoro-82M assets downloaded successfully!")
