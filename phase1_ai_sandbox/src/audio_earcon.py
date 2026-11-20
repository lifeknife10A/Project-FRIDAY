"""
PROJECT FRIDAY - PHASE 1 AUDIO EARCON ENGINE
Component: Instantaneous (<80ms) Two-Tone Wake Acknowledgement Earcon
Author: Krishna Jagat Solanki
"""

import os
import subprocess
import numpy as np
import soundfile as sf

def generate_earcon_wav(output_path: str = "assets/earcon.wav", sample_rate: int = 16000) -> str:
    """
    Synthesizes a pleasant, instantaneous two-tone chime:
    Tone 1: 587.33 Hz (D5) for 35 ms
    Tone 2: 880.00 Hz (A5) for 35 ms
    Total duration = 70 ms (< 80 ms latency contract).
    Smooth sinusoidal Tukey/Hann windowing prevents clicks.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    t_tone = 0.035 # 35ms each
    n_samples = int(sample_rate * t_tone)
    t = np.linspace(0, t_tone, n_samples, endpoint=False)
    
    # Hann window for smooth envelope
    envelope = np.hanning(n_samples)
    
    tone1 = 0.35 * np.sin(2 * np.pi * 587.33 * t) * envelope
    tone2 = 0.45 * np.sin(2 * np.pi * 880.00 * t) * envelope
    
    earcon_signal = np.concatenate([tone1, tone2]).astype(np.float32)
    sf.write(output_path, earcon_signal, sample_rate)
    return output_path

def play_earcon(wav_path: str = "assets/earcon.wav", blocking: bool = False):
    """
    Plays the earcon chime instantly on macOS using afplay.
    """
    if not os.path.exists(wav_path):
        generate_earcon_wav(wav_path)
        
    cmd = ["afplay", wav_path]
    if blocking:
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

if __name__ == "__main__":
    test_path = os.path.join(os.path.dirname(__file__), "../../assets/earcon.wav")
    print(f"Generating earcon audio at: {test_path}...")
    generate_earcon_wav(test_path)
    
    info = sf.info(test_path)
    duration_ms = info.duration * 1000.0
    print(f"Earcon Duration: {duration_ms:.1f} ms (Contract: < 80.0 ms)")
    assert duration_ms <= 80.0, f"Earcon duration {duration_ms} exceeds 80ms!"
    print(">>> Earcon generated and verified within <80ms contract! <<<")
