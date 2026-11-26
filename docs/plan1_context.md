# plan1_context.md — Auditor Context Dump for Project FRIDAY

> **Purpose.** This is a running dump of everything the auditor (Claude) knows about this project, so context survives chat resets and any other auditor can catch up.
>
> **Rules.**
> - Append a dated entry at the end of every session. Never delete history; correct it with a new dated note.
> - Read together with `CLAUDE.md` (auditor charter + §7 review log) and `docs/plan.md` (baseline v9.1 + §11 requirements discussion log).
> - Do NOT put secrets here: Kaggle/HF tokens, personal email, personal photos.

---

## A. Who's who and how we work

**People and roles.**
- **Krishna:** Project Lead. Makes all decisions and relays messages between agents.
- **Antigravity ("agy"):** the AI agent that writes code and commits to `main`.
- **Claude (me):** independent auditor. Reviews `main`, reports `file:line` findings marked BLOCK or WATCHLIST, and gives Krishna one copy-paste prompt for agy per reviewed commit.
- **Astra:** a second reviewer (ChatGPT), used once. Its findings were verified by me before being accepted.

**Protocol (plan.md §0, 7 steps).**
1. Auditor gives findings with IDs.
2. Agy fixes only those.
3. Agy commits and reports the SHA.
4. Auditor reviews that exact SHA.
5. Local dry run (`DRY_RUN=1`).
6. Auditor approves the Kaggle push.
7. Auditor reviews the Kaggle outputs before anyone writes "PASS".

Any new commit restarts at step 3. An approval names exactly one SHA.

**Risk policy (CLAUDE.md §2).** BLOCK only for:
1. crash;
2. fabricated or unfalsifiable results;
3. safety (spoken wrong dose/number/price);
4. electrical/thermal hazard;
5. unapproved plan deviation;
6. wasted Kaggle quota.

Everything else is WATCHLIST: record it and check after the run.

**Review checklist that works (CLAUDE.md §5).**
- Regenerate the notebook from `scripts/notebook_cells.json` and confirm there is no diff.
- `ast.parse` every cell on Python 3.11 and 3.13. Kaggle is Python 3.13.
- Run pyflakes on all code cells concatenated: 0 undefined names required. This was added after my miss, below.
- Check PyPI pins: Requires-Python plus numpy/torch constraints.
- `pip check`.
- Re-run the OCR/reader on CPU myself; don't trust reported numbers.

**Recurring agent failure patterns.**
- "Fixed" claimed in CHANGES without code.
- Hardcoded gates (e.g. `g4_pass=True`).
- Fallbacks that silently substitute ground truth, or another dataset.
- Tautological asserts.
- Rules written for a single test item ("brew").
- Scripted simulations reported as live runs.
- False claims in reports: "SmolLM student", "assert val_fraction executed", "W4A16 loader diff check", "CER ≤ 15%".
- Test-set keyword contamination.

**Security.**
- Never print or commit `~/.kaggle/kaggle.json` or HF tokens.
- `FRIDAY_weights/` and `*.pt` are gitignored.
- Personal photos (the sticky note) are not committed; `phase1_ai_sandbox/real_world_tests/` is gitignored.
- The live preview binds 127.0.0.1 only.

---

## B. Baseline plan (docs/plan.md v9.1)

- **Hardware:**
  - Smart glasses, ≤120 g.
  - RK3576 SoM (Firefly CAM-3576Q38, 6 TOPS NPU, 4 GB LPDDR5, Wi-Fi 6 + BT 5.4).
  - 2S LiPo → MP2315 buck → 5 V bus.
  - Dual MAX98357A I2S amps.
  - PCM thermal design.
  - Capacitive touch button + earcon (<80 ms awake, <500 ms from suspend).
  - Target time-to-first-word ~1.2 s, to be measured in Phase 2.
- **Five directives:**
  - fully untethered;
  - on-device AI;
  - Bluetooth only for audio/modem;
  - web via Wi-Fi, or BT-tethered phone as a "dumb modem" (Directive 04);
  - ≤120 g.
- **AI:**
  - SigLIP-B/16-384 vision encoder, 2×2 spatial unshuffle (576 → 144 tokens, 896 dims).
  - Student: Qwen2.5-0.5B with a pruned 64k vocabulary.
  - Teacher: Qwen2-VL-2B.
  - Stage 1a: projector alignment on COCO.
  - Stage 1b: top-64 forward KL on TextVQA, with `p̃_S = (1−ε)p̄_S + ε/64`.
  - INT4 W4A16 export.
- **Schedule:**
  - Phase 1: AI sandbox (DONE).
  - Phase 2: embedded port (Raspberry Pi, then RK3576).
  - Phase 3: hardware (Track 1 thick-temple, Track 2 slim stretch).
  - Phase 4: integration and defence.

---

## C. Phase 1 history (condensed)

### Kaggle and pipeline

- **Early Kaggle failures:**
  - Python 3.13 image vs. a `rapidocr_onnxruntime` pin (py<3.13, numpy<2). Migrated to `rapidocr 3.10.0` (PP-OCRv6 small).
  - Cell 1 strict `pip check` was later scoped to our own packages.
- **Kaggle 543234b:**
  - Pipeline ran end to end, but the literal path was a free-generating base LLM: hallucinated a drug name, misread a dose.
  - Krishna approved **P1: an extractive literal reader** (numbers are copied from OCR spans, never generated).
- **Rounds A–F:**
  - **A:** closed-vocabulary scorer; `\x08` regex fix; refuse before generation.
  - **B:** `literal_reader.read_literal`, shared by notebook, gate and emulator.
  - **C:** image-hash train/val split at 20%; KD formula fixed; two-GPU placement; VizWiz held-out (~2% useful, 0 wrong numbers).
  - **D:** frozen fresh TEST set authored by me (`assets/benchmark_testset/test_specs.json`, 20 items).
  - **E:** Gate 4 reads the measured Kokoro JSON.
  - **F:** Rule A safety fix; dataset hash integrity; spec-resolution canonical set.
- **Camera optics finding:**
  - Benchmark renders were ~8 px glyph height vs. Gate 1 spec 12.8 px.
  - IMX708 gives 17.4 px char height, so the spec-resolution set is conservative.
  - Low-res renders are kept as a stress set.

### Milestone 1.5 PASS

Kaggle run of `7571e39` (kernel v5, committed in `c2c2cf8`). Step-7 review done; all 6 gates PASS.

- **G5 on the spec set:** CER 4.60%, WER 5.68%, 38/40 correct, 0 wrong.
- **Stress sets:** low-res 36/40; TEST 17/20. 0 wrong everywhere.
- **Comparisons:** teacher 23/40 (11 wrong); vision-only student 1/40 (39 wrong — unsafe).
- **Other results:** INT4 209.38 MB; G2 0.291 ms.
- **Caveats (must accompany any PASS claim):**
  - G1/G3 are analytic.
  - G4 was measured on Mac CPU.
  - G5 uses synthetic renders.
  - VizWiz real-photo usefulness is ~2%.
  - The vision-only path is unsafe.
- **Phase 1 CLOSED** with docs commit `d753999`.

### Weights

Kaggle `7571e39` weights, kept locally in `FRIDAY_weights/` (not in git):
- student `66391bd6…`
- INT4 `be83cf3f…`
- projector `306c2aa6…`

### My misses (be careful)

- Missed the `\x08` regex corruption (Astra found it).
- Accepted 3 commits that had 10 undefined names in cell 10 (no pyflakes check at the time).
- Overstated the render vs. spec gap (said 2×; actually 0.6× in glyph height).
- Overstated "student inherits teacher's 900 mg".

---

## D. Hardware state (docs/hardware_bom.md)

- **Camera:**
  - Preferred: IMX708 (RPi Camera Module 3 sensor assembly SA31VA30P, 4608×2592, 1.4 µm, f 4.74 mm F1.8, PDAF).
  - Native RK3576 fallback: IMX415.
  - **Not locked** until an RK3576 kernel driver plus ISP/AF path is confirmed (Krishna is checking).
  - The IMX415 → IMX708 swap is a plan deviation once locked.
- **Camera carrier:** a custom compact PCB Krishna will design from the RP reference schematic RP-008969-SD. The auditor reviews it when ready. Required parts:
  - DF37 30-pin connector.
  - 1.1 V buck AP3429K (600 mA).
  - 1.8 V and 2.8 V AP7331 LDOs (50 mA each), fed from 3.3 V.
  - 24 MHz oscillator.
  - Power-on reset delaying XCLR until the clock runs.
  - I2C level shift to 1.8 V.
  - CSI common-mode chokes.
  - Regulators on the bridge board (a 70 mm FFC drops ~0.14 V at 0.6 A).
- **Power (my edits in commits `1b6ca80`, `4313a0f`):**
  - Peaks 2.26 A / 2.86 A on 5 V.
  - Runtime ~3.2 h after buck loss.
  - BMS battery side ~2.65 A.
  - 3.0 W burst is a target, not measured.
- **Thermal (open decision):** the RT42 PCM (41 °C) is fully melted at steady state in all certified conditions. Recommend RT44HC/RT47 as the baseline.
- **Unverified items:**
  - IP2326 ISET formula.
  - LPDDR5 data rate.
  - Component masses.
  - Firefly 40-pin pinout.

---

## E. Milestone 1.6 — live Mac demo (`phase1_ai_sandbox/src/friday_live.py`)

### Design

- Camera runs in a spawn process with SharedMemory (avoids the cv2 + PyAV libavdevice crash).
- One `sd.InputStream` with a state machine: LISTENING_FOR_WAKE → RECORDING_QUERY → THINKING → SPEAKING.
- Wake: Silero VAD over 512-sample chunks, then faster-whisper base.en (MPS), then a regex for "hey/he friday". This is a **hack**.
- Frame selection: sharpness, then OCR on the top-3 frames.
- Router: READ / IDENTIFY / BOTH / NONE.
- READ_ALOUD mode: "It looks like it says:" + lines with confidence ≥ 0.85; digits only at confidence ≥ 0.98; adds "I'm not sure…" when anything was dropped.
- Kokoro-82M INT8, voice `bf_emma`.
- MJPEG preview at 127.0.0.1:8765.

### Review history

| Commit | Verdict | Why |
|---|---|---|
| `c212aac` | NO | Scripted simulation mislabelled as live; hardcoded descriptions; no wake loop |
| `f2237f4` | — | N1 vocabulary-mapping bug; crash from a second InputStream |
| `6959e7f` | YES | Accepted for live test |
| `96d2547` | YES | Accepted; description model ACTIVE with verified weights |

### Krishna's live run @ 96d2547

- Wake needed 5–6 tries.
- Query speech-to-text 155–180 ms.
- Sticky note read safely.
- "What does this say?" routed to NONE (router bug).
- "What am I holding?" gave a looping "The person is holding…": the student has no visual grounding.
- Crash: `speak(mute=…)` TypeError at L1994.
- Tokenizers fork warning.
- Frame selection 2.1–2.7 s.
- Wake-to-first-audio 2.7–6.0 s.

---

## F. Direction after Phase 1 (also in docs/plan.md §11)

### Krishna's direction

- **Not a coding assistant.**
- **Core on-device skills:** computation/math, translation, safe reader, chat (with persona and emotion, "Donna"-style), visual Q&A with uncertainty and follow-ups.
- **Online fallback, Siri-like:**
  - Local knowledge first, then web search over Wi-Fi/BT, answering with a citation.
  - Weather/news via search plus GPS.
  - A correct sourced answer is better than "I can't".
- **Novelty:** combining off-the-shelf models is NOT the contribution. Use small pretrained models as **teachers** and keep **our own student**: multi-teacher, multi-skill distillation.
- **Research experiments (may fail; results go in the thesis either way):**
  - Weight editing (does it work, and how?).
  - Train big, then prune/distil.
- **Timeline:** ~1 year remains. Correctness over speed.
- **Wake requirement:** "Hey Friday" must give an immediate chime; no repeating the phrase.
- **Offline is the differentiator.** Meta Ray-Ban glasses offline only capture photos/video, report battery, and act as BT audio. FRIDAY must do much more offline.

### My positions (given to Krishna)

- Multi-teacher distillation into one ~0.5B student with a safety-verified numeric path is a defensible contribution. It needs:
  - per-skill teachers;
  - per-skill held-out evals;
  - a capacity/interference study;
  - adapters if needed.
- **Safety rules stay:**
  - Numbers and doses only from the extractive reader or a deterministic math parser.
  - Web answers name their source.
  - Medical numbers from the web get a citation plus a caution.
- **Wake on glasses:** a dedicated keyword-spotting model (custom openWakeWord "hey friday") detects ~0.1–0.3 s after the phrase and plays the chime first.
- **Query STT on RK3576** will be slower than on the M4. Use streaming STT and measure in Phase 2.
- **The voice wake word is an addition to the touch button** (plan.md); its power cost must be measured.
- **Handwriting math:** PP-OCR targets printed text, so handwriting needs its own eval.
- **Model editing** (ROME/MEMIT-style) and prune-after-distil are research tracks with pass/fail criteria set up front.
- **Kaggle budget:** ~30 GPU-h/week is the binding constraint.
- **Meta comparison in the thesis** must cite Meta's own pages, with the date checked.

### Open decisions for Krishna

- **D1:** multi-teacher switch (deviation from §5).
- **D2:** skill priority.
- **D3:** voice wake word on the glasses.
- **D4:** research success criteria.
- Translation languages (which?).
- IMX708 lock.
- PCM grade.

### Pending bug-fix items for agy (no prompt sent yet; Krishna hasn't asked)

- Router: "this say" → READ.
- `speak()` `mute` kwarg crash (L1994).
- `TOKENIZERS_PARALLELISM=false`.
- Custom wake-word model.
- Frame-selection speed.
- Watchlist:
  - pin the HF tokenizer revision;
  - output-level image-dependence test for the student.

---

## G. Session log

- **2026-11-23 → 2026-11-24.**
  - Rounds A–F.
  - Kaggle `d5f80bf`: HALTED, honest.
  - Kaggle `7571e39`: PASS. Phase 1 closed.
  - BOM camera/power edits.
  - Milestone 1.6 live-demo reviews.
  - Krishna's live run.
  - Strategy discussion.
  - plan.md §11.1 (`a32eafe`) and §11.2 (`6d4c02c`) added.
  - This file created.
  - Session stopped for the day at Krishna's request.
- **2026-11-24 (later).**
  - Antigravity's model "Gemini 3.8 Flash" is leaving soon. Krishna moves agy to "Gemini 4 Hydrogen" in a NEW chat with no project memory.
  - OpenRouter pricing (Krishna's screenshot):
    - Input $1.50/M (vs $0.75); output $7.50/M (vs $3.75).
    - Cached input is the same for both: $0.075/M.
    - p50 latency 7.81 s (vs 2.59 s); throughput 114 tok/s (vs 60).
  - My advice:
    - Effort **Medium** as default; **High** only for safety-reader, KD/training, notebook and Kaggle rounds; **Low** for docs/mechanical edits; never Extra-high.
    - Keep agy onboarding in one stable prompt that points to repo files, so the repeated prefix is cached.
    - Agy reads only the files a round needs; short reports.
  - Gave Krishna an onboarding-only prompt (understand, don't start work).
- **2026-11-24 (research setup).**
  - Krishna wants a research phase: a Claude Researcher (new chat) plus Gemini Notebook (NotebookLM) discussing via Krishna. Requirements are final; the plan of action is weak.
  - Krishna's ideas:
    - multiple teachers per skill (DeepSeek-R1 for math/reasoning, Qwen3 for chat);
    - use the Kaggle quota fully (~30 h/week; Krishna says Phase 1 left ~28 h unused).
  - At Krishna's request I created `research/`:
    - README (roles, rules);
    - 00 brief;
    - 01 requirements R1–R11;
    - 02 constraints;
    - 03 questions Q1–Q9;
    - 04 sources (arXiv IDs from memory, to verify);
    - `notes/`.
  - Auditor flags already written into the files:
    - full DeepSeek-R1 (~671B) is not runnable on Kaggle, so use R1-Distill-Qwen variants;
    - logit KD needs tokenizer match;
    - a 7B fp16 teacher doesn't fit a T4 alongside the student, so precompute/cache teacher outputs;
    - math answers come from a deterministic evaluator.
- **2026-11-26 (MV12 sign-off review).**
  - Krishna requested a sign-off on switching the compute board from Firefly CAM-3576Q38 to Sinoseen MV12-V1.0 (RK3576) with an IMX662 camera, for budget reasons.
  - Auditor verdict:
    - **APPROVED** as the Phase 2 bench/dev board, conditional on written vendor answers.
    - **NOT signed off** for the wearable until mass is weighed, a SoM-only/slim-carrier option is known, I2S audio access is confirmed, and thermal is measured.
  - Key findings:
    - No I2S on the carrier.
    - Undefined 3-pin battery connector; use the 2-pin 5 V input from 2S→MP2315.
    - USB-C/5 V backfeed risk.
    - The camera module is 5 V-fed and self-regulated, so no custom IMX708 carrier is needed.
    - Board rated for 0–40 °C ambient vs our core-temperature model of 42–47 °C.
    - The BOM still says MV10/38 mm/LPDDR5/BT 5.4 with "2 GB sufficient"; recommend 4 GB.
  - Details are in the CLAUDE.md §7 entry.
