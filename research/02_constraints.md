# 02 — Constraints (numbers the plan must fit)

## Training compute

**Kaggle:**
- Hardware: 2× NVIDIA T4, 16 GB each; fp16, no bf16. Python 3.13 image.
- Quota: about **30 GPU-hours per week**.
- Phase 1 (the full Milestone 1.5 run) fitted well inside the weekly quota. Krishna reports about 28 h remaining.
  - *Exact Phase 1 runtime: UNVERIFIED (not recorded in the committed README).*
- Per-GPU memory, T4 16 GB:

| Item | Memory |
|---|---|
| 7B fp16 teacher | ~15 GB — **does not fit with a student on the same GPU** |
| 7B in 4-bit | ~5 GB |
| 2B fp16 | ~4.5 GB |
| Phase 1 peak, teacher (2B) | 8.48 GB |
| Phase 1 peak, student | 4.44 GB |

- Practical pattern:
  1. Precompute teacher outputs (top-k logits or generated text) once and cache them.
  2. Then train the student without the teacher in memory.

**Mac (Krishna, MacBook Air M4):** for dry runs and the live demo (MPS backend).

## On-device: RK3576

- **Memory:** 4 GB LPDDR5 in total, shared by OS, camera, speech-to-text, text-to-speech, OCR and the LLM. Budget for all AI models together: roughly **≤1.5–2 GB** (*to be measured*).
- **Phase 1 student:** INT4, 209 MB.
- **NPU:**
  - 6 TOPS.
  - Supported model and operator coverage must be checked in Rockchip RKLLM/RKNN docs. *UNVERIFIED which architectures RKLLM supports for RK3576.*
- **Speed:** RK3576 is far slower than an M4. Example: Whisper base took 155–180 ms on M4 MPS; on RK3576 it is unknown.
- **Power and thermal:** sustained inference is limited by the PCM thermal budget. Average power 0.615 W is the planning number; 3.0 W bursts.

## Model and licence

- **Student family:** Qwen2.5-0.5B (plan baseline, Apache-2.0). Any change of student family is a plan deviation.
- **Teachers:** licences must allow distillation into our model. Check each model card.
  - Some licences restrict use (e.g. some Llama/Gemma terms; NLLB is CC-BY-NC).
- **Logit distillation needs tokenizer compatibility.**
  - Same tokenizer family (Qwen2.5 ↔ Qwen2/Qwen2-VL; DeepSeek-R1-Distill-Qwen; Qwen3 *to verify*) allows logit KD.
  - Otherwise use sequence-level KD: train on the teacher's generated text.

## Plan constraints

- `docs/plan.md` v9.1 is the approved baseline. Deviations need Krishna's approval.
- Weight ≤120 g, skin ≤37.5 °C, untethered. The phone may only be an internet modem, never an AI coprocessor.
