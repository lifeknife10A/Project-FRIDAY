# 2026-11-25 — Game plan: complete FRIDAY on macOS before buying hardware

Author: Claude Researcher. Status: PROPOSAL, awaiting Krishna and the Auditor.

**Krishna's goal:** the entire FRIDAY model functional and working on the MacBook (M4) before any hardware is bought.

This note defines what "done" means, the order of work, the compute and time budget, and the gate that justifies buying the RK3576 module.

## 1. Definition of done: "Phase 1 Complete (Mac)" gate

FRIDAY passes when **all** of the following hold, each backed by committed run output (plan §0 step 7).

**A. Functions**, live on the Mac (webcam + mic + speaker, Wi-Fi off unless stated):

| # | Function | Pass criterion (proposed; Krishna fixes before the run) |
|---|---|---|
| F1 | "Hey Friday" wake | Chime on the first try in ≥95% of 100 wake attempts; ≤1 false wake per hour of background speech/TV; chime <80 ms after detection |
| F2 | Safe reader | Existing gate kept: 0 wrong numbers on spec/stress/TEST sets plus a live sticky-note/label check |
| F3 | Visual Q&A | E-VIS-1 and E-VIS-2 pass (Q4 note): objects and colours ≥70% on FRIDAY-Real-100, confident-wrong ≤10%, ≥ SmolVLM-256M on public sets |
| F4 | Follow-ups | 3-turn follow-ups ("what colour is it?", "is it full?") answered about the same object in ≥80% of 30 scripted dialogues |
| F5 | People + Easter egg | Description-only policy, with 0 sensitive inferences on 30 people photos. Easter egg: 0 false triggers on 500 other faces, ≥90% on Krishna |
| F6 | Math | Spoken and whiteboard questions: model writes the expression, parser computes it. ≥90% exact on a held-out set; **0 spoken numbers that did not come from the parser** |
| F7 | Conversation | Persona and tone consistent in ≥80% of 50 judged turns; no invented numbers; remembers the last 3 turns |
| F8 | Router | Correct skill for ≥95% of 200 held-out utterances (fixes the live bug "What does this say?" → NONE) |
| F9 | Online fallback | With Wi-Fi on: an answer with the source named in ≥90% of 30 web questions. With Wi-Fi off: the Directive-04 offline sentence, never a made-up answer |
| F10 | Hindi | Hindi speech in → Hindi speech out via translation (English core). **Every digit in the spoken Hindi equals a digit in the English answer**, else it speaks English (safety rule) |

**B. Device-faithfulness**, so that "works on Mac" transfers to the glasses:

| # | Criterion |
|---|---|
| D1 | The Mac runs the **same artifacts that will ship**: INT4 student (W4A16), same vision tower, same STT/TTS/OCR models. No fp16-only demo. |
| D2 | **Memory budget:** summed resident memory of all on-device models, measured on the Mac, ≤ the device AI budget (proposed 2.0 GB; see §4). |
| D3 | **Convertibility:** every on-device model converts with RKLLM-Toolkit / RKNN-Toolkit2 for target RK3576 (E-DEV-1; runs on x86 Linux such as a Kaggle CPU session, no hardware needed). |
| D4 | **Latency honesty:** Mac latencies are reported as Mac numbers. RK3576 latency is a *projection* from Rockchip's official benchmark.md and is labelled so. |

**C. Live acceptance session.**
- Krishna runs a 50-turn unscripted session covering F1–F9. Every turn is logged by TurnLogger (exists in `friday_live.py`).
- **Pass:** 0 crashes, 0 wrong spoken numbers, and per-function criteria met.

**Hardware purchase decision** = gate A + B + C passed. One exception: D3 (convertibility) is checked in week 2. If it fails, the hardware plan must change before any training money or time is spent.

## 2. What exists today (from the repo, `phase1_ai_sandbox/src/friday_live.py`)

| Component | State |
|---|---|
| Camera | ring buffer in a spawn process |
| Wake | `WakeWordDetector`: Whisper on 1.5 s windows. Needs 5–6 tries; to be replaced. |
| STT | faster-whisper `AudioQueryCapture` |
| Frame selection | `FrameScorer` (2.1–2.7 s; slow) |
| Router | `route_intent` (rule-based; known bug) |
| Safe reader | `run_literal_pipeline` (PASS) |
| Description | `DescriptionPipeline`: Phase 1 student, no grounding |
| TTS | Kokoro |
| Logging and preview | `TurnLogger`, preview server |
| Known bugs | `speak(mute=…)` crash L1994, tokenizers fork warning |

**Missing:** custom wake word, visual grounding, math, conversation/persona, follow-up memory, Easter egg, online fallback, Hindi layer, memory measurement, RKLLM conversion check.

## 3. Milestones (in order; each is its own SHA through the 7-step protocol)

All estimates in GPU-h are mine and are redone after M0 measures real throughput.

| M | Weeks | What | GPU-h (Kaggle) | Mac/CPU work |
|---|---|---|---|---|
| **M0 Foundations** | 1–2 | Fix live bugs (router "this say", `mute` kwarg, `TOKENIZERS_PARALLELISM`). **Freeze all held-out eval sets now** (FRIDAY-Real-100, math set, router set, persona set, people set) before any training. **E-THR-1** (tokens/s per T4). **E-DEV-1** (RKLLM/RKNN conversion of the Phase 1 student + SigLIP + projector on x86 CPU). Memory table v0 (§4). | ~1 | yes |
| **M1 Wake word** | 2–3 | Custom "Hey Friday" model (openWakeWord-style, trained on synthetic TTS clips + Krishna's recordings; method per openWakeWord README, UNVERIFIED details). Chime on detection, before any other processing. | 0 (CPU/Colab-CPU) | yes |
| **M2 KD method** | 3–4 | **E-KD-1** on the math skill (exact-match metric): SeqKD vs top-k forward KL vs on-policy, at equal GPU-h. The winner is used in M3–M5. | ~10 | — |
| **M3 Visual** | 4–7 | Q4 note stages V0–V4: teacher Qwen3-VL-2B labels, student KD, uncertainty U-A, follow-up dialogues, people policy, Easter egg (YuNet + SFace, CPU). | ~25–30 | Easter egg |
| **M4 Math** | 6–8 | Expression format (a safe arithmetic subset, parsed by our own evaluator; never `eval`). Teacher labels from Qwen3-1.7B or DeepSeek-R1-Distill-Qwen-1.5B (both Apache/MIT, same tokenizer). Whiteboard via OCR → expression. | ~10 | parser + tests |
| **M5 Conversation** | 8–10 | Persona ("Donna") distilled from Qwen3-4B (non-thinking, persona system prompt). Tone tag → Kokoro voice/speed mapping. 3-turn memory. Number filter (chat never speaks digits unless they come from the reader or parser). | ~20 | TTS mapping |
| **M6 Merge + router** | 10–13 | One student with all skills vs per-skill LoRA adapters. **Forgetting matrix:** every skill's eval after each added skill (core thesis experiment). Router: the student emits a skill tag vs a tiny classifier vs rules. | ~40–60 | router eval |
| **M7 Online fallback** | 12–14 | Search API (Krishna picks) with source naming; "not sure locally" → search when online, offline sentence when not. | 0 | yes |
| **M8 Hindi layer** | 14–15 | STT (Qwen3-ASR-0.6B supports hi) → IndicTrans2-Dist hi→en → student → en→hi → Hindi TTS (Kokoro has hi voices; quality to test). **Digit-preservation check** (F10). | ~2 (eval) | yes |
| **M9 Acceptance** | 15–17 | Full live session (gate C), memory measurement (D2), conversion of every model (D3), final report. → **purchase decision** | ~2 | yes |

**Totals:**
- About 110–135 GPU-h over about 17 weeks. Quota in that window is about 500 GPU-h (17 × 30), so there is **room for re-runs and for the research tracks**.
- About 4 months (to about end of March 2027), leaving about 8 months for Phases 2–4 (hardware) against the 1-year deadline.

**Research tracks in parallel, not blocking the purchase:**
- E-PRUNE-1 (Qwen3-0.6B pruned + healed);
- E-EDIT-0, then model editing on the student.

They share the spare quota. If pruned Qwen3 wins, it replaces the student base after M9 as a separate decision.

## 4. Memory budget v0 (on-device; estimates, to be replaced by Mac measurements in M0/M9)

| Component | Estimate | Source / basis |
|---|---|---|
| LLM student, RKLLM w4a16 | 443 MB | official RK3576 benchmark.md, Qwen2 0.5B w4a16 |
| SigLIP-B/16 vision tower, FP16 on RKNN | ~190 MB | about 93M params × 2 bytes (param count UNVERIFIED) |
| STT (Whisper base) | ~150 MB | 74M params (Whisper paper, from memory, UNVERIFIED) × 2 bytes |
| TTS Kokoro-82M | ~165 MB | 82M × 2 bytes |
| OCR (PP-OCR small det + rec) | ~20–50 MB | UNVERIFIED |
| Wake word, face models | ~10–40 MB | UNVERIFIED |
| **Subtotal without Hindi** | **~1.0 GB** | |
| Hindi layer: IndicTrans2-Dist 2 × 211M | ~840 MB fp16 / ~420 MB int8 | §7.6 IndicTrans2 paper (211M), × bytes |
| **Total with Hindi** | **~1.4–1.85 GB** | |

**Consequences:**
- Without Hindi the stack plausibly fits a 2 GB AI budget.
- **The Hindi translation layer is the largest single add-on.** It may need int8, or loading on demand (load when a Hindi utterance is detected). Measure it in M8.
- OS + camera + ISP memory on the RK3576 is unknown until Phase 2. The 2.0 GB AI budget is a planning number.

## 5. Rules that keep the Mac result honest (lessons from plan1_context.md)

1. **Evaluate the INT4 student, not fp16.**
2. **Freeze eval sets in M0** (sha256 manifest), before any training. No test-set words in rules (the earlier "brew" and keyword-contamination lessons).
3. **No scripted "live" demos.** Gate C is unscripted, with mic, camera and speaker actually on (the Milestone 1.6 lesson).
4. **Every number spoken comes from the reader, the parser or a named web source.** Chat, VQA and the translator never originate digits.
5. **One approval = one SHA;** each milestone follows plan §0.

## Recommendation

1. Adopt this definition of done (§1) and milestone order (§3).
2. Do M0 first. Its E-DEV-1 conversion check is the cheapest test that could invalidate the hardware plan.
3. Keep Qwen2.5-0.5B as the student base for Phase 1 completion. Pruned Qwen3 runs in parallel and can replace it after M9.

## Experiments (pass/fail)

As listed per function in §1 (F1–F10, D1–D4, gate C). The thresholds are proposals; Krishna fixes each before the corresponding run.

## Kaggle budget

About 110–135 GPU-h for M0–M9 over about 17 weeks (about 25% of available quota). The remainder goes to re-runs and the research tracks.

## Risks

- **0.5B may not hold all skills** (M6 forgetting). The fallback is per-skill LoRA adapters; RKLLM LoRA support is UNVERIFIED and is checked in E-DEV-1.
- **The visual student may lose to SmolVLM-256M.** This is reportable. The product could then use SmolVLM for vision (a deviation for Krishna to decide).
- **Mac speed hides RK3576 slowness.** D4 projections from the official benchmark are mandatory.
- **Wake-word quality on Mac may differ** with the glasses' MEMS microphone (Phase 2 re-check).
- **The Hindi layer's memory** (§4).

## Decisions needed from Krishna

1. Approve the "Phase 1 Complete (Mac)" definition (§1) as the hardware-purchase gate, and fix the thresholds.
2. Approve the milestone order M0 → M9, with M0 (bug fixes + eval freeze + E-DEV-1) as agy's next task.
3. Do FRIDAY-Real-100 (your photos) in M0 so the eval is frozen before training.
4. Choose the search API for M7 (any key stays out of the repo).
