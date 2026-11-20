"""
PROJECT FRIDAY - KOKORO-82M FEMALE VOICE SAMPLER & PREVIEW ENGINE
Synthesizes and plays all available female voices for Project FRIDAY
Author: Krishna Jagat Solanki
"""

import os
import sys
import subprocess
import soundfile as sf
from kokoro_onnx import Kokoro

# Curated list of all top English & Indian accent female voices in Kokoro-82M
FEMALE_VOICES = [
    # American Female Accents (af_*)
    ("af_heart", "American Female - Flagship warm, crisp & ultra-natural"),
    ("af_bella", "American Female - Expressive, articulate & conversational"),
    ("af_sarah", "American Female - Professional, calm & soothing"),
    ("af_nicole", "American Female - Warm, soft & clear"),
    ("af_sky", "American Female - Youthful, bright & vibrant"),
    ("af_nova", "American Female - Dynamic, confident & modern"),
    ("af_alloy", "American Female - Balanced, neutral & clear"),
    ("af_jessica", "American Female - Conversational & friendly"),
    ("af_river", "American Female - Relaxed, smooth & effortless"),
    ("af_kore", "American Female - Gentle, warm & polite"),
    
    # British Female Accents (bf_*)
    ("bf_emma", "British Female - Sophisticated, polished RP accent"),
    ("bf_isabella", "British Female - Warm, articulate British tone"),
    ("bf_alice", "British Female - Classic, distinguished British cadence"),
    ("bf_lily", "British Female - Youthful, light British accent"),
    
    # Indian / South Asian Accent Female (hf_*)
    ("hf_alpha", "Indian English Female - Natural South Asian cadence"),
    ("hf_beta", "Indian English Female - Expressive Indian English tone")
]

def generate_and_play_voice_sample(kokoro: Kokoro, voice_id: str, description: str, sample_dir: str):
    wav_path = os.path.join(sample_dir, f"{voice_id}.wav")
    
    sample_text = (
        f"Hello Krishna. This is {voice_id}. "
        "I am ready to be your eyes and ears on Project Friday."
    )
    
    print(f"\n[{voice_id}] - {description}")
    print(f"  Generating sample text: \"{sample_text}\"...")
    
    if not os.path.exists(wav_path):
        samples, sr = kokoro.create(sample_text, voice=voice_id, speed=1.0, lang="en-us")
        sf.write(wav_path, samples, sr)
        
    print(f"  Playing via Mac audio drivers ({wav_path})...")
    subprocess.run(["afplay", wav_path])

def main():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    model_path = os.path.join(root_dir, "assets/kokoro/kokoro-v1.0.int8.onnx")
    voices_path = os.path.join(root_dir, "assets/kokoro/voices-v1.0.bin")
    sample_dir = os.path.join(root_dir, "assets/voice_samples")
    os.makedirs(sample_dir, exist_ok=True)

    print("==================================================================")
    print("PROJECT FRIDAY: KOKORO-82M FEMALE VOICE AUDITION")
    print("==================================================================")
    print(f"Found {len(FEMALE_VOICES)} curated female voices.")
    
    kokoro = Kokoro(model_path, voices_path)

    # Check for CLI argument: play single voice or all
    if len(sys.argv) > 1:
        target = sys.argv[1].strip()
        matched = [v for v in FEMALE_VOICES if v[0] == target]
        if matched:
            v_id, v_desc = matched[0]
            generate_and_play_voice_sample(kokoro, v_id, v_desc, sample_dir)
            return
        else:
            print(f"[!] Voice '{target}' not in curated list. Available: {[v[0] for v in FEMALE_VOICES]}")
            return

    # Sequentially audition all voices with short pause between each
    for idx, (voice_id, desc) in enumerate(FEMALE_VOICES, 1):
        print(f"\n--- [{idx}/{len(FEMALE_VOICES)}] ---")
        generate_and_play_voice_sample(kokoro, voice_id, desc, sample_dir)

    print("\n==================================================================")
    print("Audition complete! All samples saved in: assets/voice_samples/")
    print("To set your favorite voice in Project FRIDAY, update 'voice' in:")
    print("  phase1_ai_sandbox/src/kokoro_voice_engine.py")
    print("==================================================================")

if __name__ == "__main__":
    main()
