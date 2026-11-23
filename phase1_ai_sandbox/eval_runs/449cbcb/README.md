# Evaluation Run 449cbcb Note (Round D)

Produced by Round D reader, OCR calibration (`RapidOCR(params={"Det.unclip_ratio": 1.8})`), and Kokoro-82M INT8 ONNX voice synthesis on CPU.
Base commit `449cbcb` is the parent commit freezing the held-out 20-sample test set (manifest SHA256 `7aa465e991b919be14f178966b8b8fbc427729a14af928006ec21f3b864ad94e`).

- `literal_reader.json`: 40 DEV images benchmark (35 correct / 1 safe_refusal / 4 incomplete / 0 wrong_spoken / 0 no_answer).
- `kokoro/`: 41 speeches synthesized on CPU (24,000 Hz, mean RTF 0.213, peak RAM 643.8 MB), with 6 listening WAVs and `kokoro_eval.json`.
