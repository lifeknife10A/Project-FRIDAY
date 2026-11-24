# 03 — Research Questions (priority order)

Each answer goes in a note under `notes/`, with sources, a cost estimate, experiments with pass/fail criteria, and decisions needed.

## Q1. Multi-teacher, multi-skill distillation design (core of the thesis)

1. **Teachers.** Which teacher for which skill (R2–R5)? Krishna's candidates:
   - DeepSeek-R1 (math/reasoning). The full R1 is ~671B and unusable on Kaggle, so consider the **R1-Distill-Qwen-1.5B/7B** variants.
   - **Qwen3** family (chat, multilingual).
   - A VLM teacher for visual Q&A (Qwen2-VL-2B already used; are larger or newer ones better?).
   - A translation teacher for Indian languages.
2. **Fit.** Can ONE ~0.5B student hold all skills, or do skills interfere ("capacity" / "catastrophic forgetting")? Options:
   - a single model;
   - shared model + per-skill LoRA adapters;
   - a small router.
3. **KD method per skill.**
   - Logit KD (top-k forward KL as in Phase 1, reverse KL / MiniLLM, on-policy / GKD), or sequence-level KD (teacher-generated data).
   - Which needs tokenizer match?
4. **Data per skill.** Datasets, licences, size; how to avoid test contamination.
5. **Student.** Keep Qwen2.5-0.5B, or move to a newer ~0.5–1B base (e.g. Qwen3-0.6B)? This is a plan deviation; give evidence.
6. **Kaggle schedule.** How many GPU-hours per skill, fitting about 30 h/week?

## Q2. Math (R2)

- The safety rule says arithmetic must be exact. So should the student learn to *translate the question into an expression or tool call*, with a deterministic evaluator computing the result?
- Handwritten whiteboard OCR: which on-device handwriting OCR, and how accurate?

## Q3. Translation (R3)

- Which languages first?
- Distil into the student, or use a separate small translator (IndicTrans2-distilled, NLLB-distilled — licence)?
- Quality metric (chrF/BLEU) and target.

## Q4. Visual Q&A with uncertainty and follow-ups (R5)

- How to teach the student real visual grounding: data (VQAv2, GQA, VizWiz train…), and how many steps or GPU-hours?
- How to produce calibrated "I'm not sure".
- Multi-turn memory within the 4 GB device budget.

## Q5. Chat + persona + emotion (R4)

- Distil persona from a teacher with a persona system prompt.
- Text-to-speech emotion: Kokoro has voices and speed but no emotion control. Expressive TTS that fits RK3576?

## Q6. Online fallback with citations (R6)

- Tool-use format the student must emit (search call, then answer with source).
- How the student decides "I don't know locally" — confidence threshold.
- Search API choice and cost.

## Q7. Research tracks (R10)

- **Model editing** (e.g. ROME, MEMIT): does it work on a 0.5B INT4-exported student?
  - Edit before or after quantisation?
  - Metrics: edit success, locality, generalisation.
- **"Train big, then prune and distil."** Structured pruning plus distillation (e.g. Minitron-style) from a 1.5B/3B model to ~0.5B, vs. direct distillation into 0.5B, at equal GPU-hours.

## Q8. Speech front-end (R7, R8)

- Custom wake word (openWakeWord or similar): training data (synthetic TTS), false-accept/false-reject targets, power on RK3576.
- Streaming speech-to-text for RK3576 (faster-whisper tiny/base, Moonshine, sherpa-onnx streaming), with measured latency.

## Q9. Deployment on RK3576

- RKLLM/RKNN support for the chosen student architecture plus vision encoder; INT4/INT8.
- Measured tokens/s and memory.
- Fallback: CPU (llama.cpp).
