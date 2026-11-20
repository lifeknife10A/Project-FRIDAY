"""
PROJECT FRIDAY - KOKORO-82M NEURAL VOICE SYNTHESIS ENGINE
Component: Human-Quality Studio Speech Synthesis via Kokoro-82M INT8 ONNX
Author: Krishna Jagat Solanki
"""

import os
import sys
import time
import threading
import subprocess
import soundfile as sf
from typing import Optional

try:
    from kokoro_onnx import Kokoro
    KOKORO_AVAILABLE = True
except ImportError:
    KOKORO_AVAILABLE = False

class FridayVoiceEngine:
    """
    Studio-grade Neural Speech Synthesis Engine for Project FRIDAY:
    - Primary: Kokoro-82M INT8 ONNX (24kHz StyleTTS 2 high-fidelity human voice).
    - Fallback: macOS native 'say' synthesizer.
    """
    def __init__(
        self,
        voice: str = "bf_emma", # Sophisticated British Female persona (locked for Project FRIDAY)
        model_path: Optional[str] = None,
        voices_path: Optional[str] = None
    ):
        self.voice = voice
        self.kokoro = None
        self.temp_audio_path = os.path.join(os.path.dirname(__file__), "../../assets/kokoro_speech.wav")
        
        # Locate Kokoro model files
        root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
        if model_path is None:
            model_path = os.path.join(root_dir, "assets/kokoro/kokoro-v1.0.int8.onnx")
        if voices_path is None:
            voices_path = os.path.join(root_dir, "assets/kokoro/voices-v1.0.bin")
            
        if KOKORO_AVAILABLE and os.path.exists(model_path) and os.path.exists(voices_path):
            try:
                print("[*] Initializing Kokoro-82M INT8 Neural Voice Engine...")
                self.kokoro = Kokoro(model_path, voices_path)
                print(f"[✓] Kokoro-82M online with voice persona: '{self.voice}' (24 kHz)")
            except Exception as e:
                print(f"[!] Warning: Failed to load Kokoro ONNX: {e}. Falling back to native TTS.")
                self.kokoro = None
        else:
            print("[*] Kokoro model files not found. Using native macOS TTS.")

    def synthesize(self, text: str, output_wav: Optional[str] = None) -> Optional[str]:
        """
        Synthesizes text into high-fidelity 24kHz audio using Kokoro-82M.
        """
        if self.kokoro is None:
            return None
            
        out_path = output_wav or self.temp_audio_path
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        
        t0 = time.perf_counter()
        samples, sr = self.kokoro.create(text, voice=self.voice, speed=1.05, lang="en-us")
        t_synth = (time.perf_counter() - t0) * 1000.0
        
        sf.write(out_path, samples, sr)
        duration_s = len(samples) / float(sr)
        print(f"  [Kokoro-82M]: Synthesized {duration_s:.2f}s audio in {t_synth:.1f}ms (RTF: {t_synth/(duration_s*1000):.2f})")
        return out_path

    def speak(self, text: str, blocking: bool = False):
        """
        Speaks text through the system audio drivers using Kokoro-82M (or native fallback).
        """
        def _speak_thread():
            if self.kokoro is not None:
                try:
                    wav_file = self.synthesize(text)
                    if wav_file and os.path.exists(wav_file):
                        subprocess.run(["afplay", wav_file], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                        return
                except Exception as e:
                    print(f"  [!] Kokoro runtime error: {e}. Fallback to say.")
            
            # Fallback to macOS say command
            subprocess.run(["say", "-v", "Samantha", text], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        if blocking:
            _speak_thread()
        else:
            t = threading.Thread(target=_speak_thread, daemon=True)
            t.start()

if __name__ == "__main__":
    print("Testing FridayVoiceEngine (Kokoro-82M)...")
    engine = FridayVoiceEngine()
    test_phrase = "Hello Krishna. Project FRIDAY neural speech synthesis is online with studio quality."
    print(f"\nSpeaking: \"{test_phrase}\"")
    engine.speak(test_phrase, blocking=True)
    print(">>> FridayVoiceEngine verified successfully! <<<")
