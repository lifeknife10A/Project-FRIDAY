import time
import os
import soundfile as sf
import numpy as np
from faster_whisper import WhisperModel

def main():
    audio_path = "/Users/krish/NMIMS/Friday/teardown_analysis/audio.wav"
    output_md = "/Users/krish/NMIMS/Friday/teardown_analysis/transcription.md"
    
    print(f"Reading audio with soundfile...")
    audio, sr = sf.read(audio_path)
    if sr != 16000:
        raise ValueError(f"Expected 16000Hz, got {sr}Hz")
    audio = audio.astype(np.float32)
    print(f"Audio loaded: {len(audio)} samples, {len(audio)/sr:.2f}s (~{len(audio)/(sr*60):.1f}m)")
    
    print(f"Loading Whisper model (base.en)...")
    t0 = time.time()
    model = WhisperModel("base.en", device="cpu", compute_type="int8")
    print(f"Model loaded in {time.time() - t0:.2f}s")
    
    print(f"Transcribing audio array...")
    t_start = time.time()
    segments, info = model.transcribe(audio, beam_size=5)
    print(f"Detected language: {info.language} with probability {info.language_probability:.2f}")
    
    lines = []
    lines.append("# Ray-Ban Meta Smart Glasses Teardown — Full Video Transcription\n\n")
    lines.append(f"- **Video Source:** `Ray-Ban Meta Smart Glasses Teardown.mp4`\n")
    lines.append(f"- **Duration:** {int(info.duration//60)}m {int(info.duration%60)}s ({info.duration:.2f} seconds)\n")
    lines.append(f"- **Transcription Engine:** Faster-Whisper (base.en, int8)\n\n")
    lines.append("---\n\n")
    lines.append("## Timestamped Video Transcript\n\n")
    
    count = 0
    for segment in segments:
        m_start = int(segment.start // 60)
        s_start = int(segment.start % 60)
        m_end = int(segment.end // 60)
        s_end = int(segment.end % 60)
        ts_str = f"[{m_start:02d}:{s_start:02d} -> {m_end:02d}:{s_end:02d}]"
        text = segment.text.strip()
        lines.append(f"* **{ts_str}** {text}\n")
        count += 1
        if count % 10 == 0:
            print(f"  {ts_str} {text}")
            
    print(f"Writing {len(lines)} lines to {output_md}...")
    with open(output_md, "w", encoding="utf-8") as f:
        f.writelines(lines)
        
    print(f"Transcription complete in {time.time() - t_start:.2f}s!")

if __name__ == "__main__":
    main()
