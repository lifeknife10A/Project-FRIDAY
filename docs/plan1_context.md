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
- **2026-11-26 (MV12 rejected).**
  - Vendor pricing: the board alone is $300; the Alibaba price was for the camera only.
  - Krishna's decisions:
    - MV12 rejected.
    - Firefly CAM-3576Q38 stays the target, to be funded by an NMIMS grant request.
    - ₹0 gates: E-DEV-1 conversion on x86; audio bring-up on Pi 3B.
  - Auditor notes:
    - BOM duty arithmetic (L136) is wrong: +42% on ₹17.2k ≈ ₹24.4k.
    - BOM total row (L71) is stale.
    - Camera is open again (IMX708 driver unverified / IMX415 native).
    - Check RKLLM-Toolkit Python wheel versions vs Kaggle 3.13.
- **2026-11-26 (camera).**
  - Krishna confirms the camera: **IMX708 sensor assembly SA31VA30P, sourced from Robu.in (India)**, as locked in 03fc2e7.
  - Open risks remain:
    - RK3576 IMX708 driver + ISP/AF (verify on Firefly SDK in Phase 2);
    - a custom DF37 carrier PCB (1.1 V buck, 1.8/2.8 V LDOs, 24 MHz osc) is needed;
    - the bare assembly does not plug into the Pi 3B 15-pin CSI.
- **2026-11-26 (co-simulation request).**
  - Krishna's plan: software-first, targeting RK3576 with no silicon. Emulate on Mac, x86/Kaggle and Pi 3B, then use the results in an NMIMS HOD grant dossier for the Firefly.
  - Auditor ruling:
    - RKNN/RKLLM x86 tools give conversion and numeric checks only. They do not simulate timing, multi-core NPU behaviour or bandwidth.
    - QEMU cannot run the NPU (no /dev/rknpu) and its timing is meaningless; only useful for aarch64 build checks.
    - Bandwidth: analytic budget only; must not be presented as proven.
  - E-DEV-1:
    - Start from `best_student_vlm.pt`, not the custom packed INT4.
    - The 64k pruned vocab is the main risk: either re-expand to the full Qwen vocab for export, or build a matching tokenizer.json.
    - Vision + unshuffle + projector go to ONNX → RKNN.
    - The 40-label reader gate does not test the student; use OCR-ONNX→RKNN parity instead.
  - Dossier must not claim "only silicon remains".
  - Pi 3B audio: one shared I2S bus (mics + amps); AEC via PipeWire echo-cancel (webrtc); test with ERLE.
- **2026-11-26 (plan1.md).**
  - At Krishna's request, merged the Researcher's game plan (M0–M9) with the Auditor's co-simulation/E-DEV-1 ruling into `docs/plan1.md`, the shared plan for all agents.
  - Phase 1 is extended to the "Phase 1 Complete (Mac)" purchase/grant gate.
  - Open decisions D1–D14 are listed in §9.
- **2026-11-26 (plan1.md v1.1).**
  - The Researcher reviewed v1.0. The Auditor verified its claims:
    - `rkllm.h` sha 4ad19442 matches; L41/L43/L53/L118/L152/L257 exist;
    - rknn-toolkit2 2.5.0 wheels are cp36–cp312;
    - outside-64k rate re-measured: README 5.35%, plan1.md 3.15%.
  - All corrections were merged into v1.1:
    - M3 data;
    - E-PRUNE-1 at matched cost;
    - D4 conditions;
    - D2 note and measurement method;
    - Pi timings = plumbing only;
    - E-DEV-1 env pinned to Python 3.12;
    - token-input + logit-mask fix;
    - API items verified;
    - vision FP16 baseline;
    - perplexity fallback;
    - E-TOK-1 vs the training mapper;
    - M0 eval-set specs not authored by Hydrogen;
    - E-THR-1 protocol.
- **2026-11-26 (plan1.md v1.2).** Krishna reviewed v1.1. All 6 points accepted:
  1. D3 split: D3a host-side is in the gate; D3b (image + remapped prompt on the runtime) becomes the first board test.
     - Auditor finding: `RKLLM_INPUT_MULTIMODAL` takes a text prompt that RKLLM tokenizes itself, so the token-input fix doesn't cover image turns.
     - Candidate: `RKLLM_INPUT_EMBED` with our own embedding lookup.
  2. F2 has minimum correct counts: 38/40, 36/40, 17/20.
  3. F10 checks value + unit (1.5 kg vs 15 kg); Hindi is out of the gate (D15).
  4. D2 = peak memory during a full live turn.
  5. F1 latency is measured from the audible end of "Friday" to the audible chime.
  6. The KD winner is a default only; per-skill 2-arm check; cache top-64 before M3.
- **2026-11-26 (bare RK3576 decision).**
  - Krishna decided: a custom board with a bare RK3576 BGA chip (0.65/0.8 mm pitch) instead of a SoM. This promotes plan.md Track 2 (L415–416, an 8–10 layer HDI stretch goal) to primary.
  - Auditor view: feasible but the highest-risk item in the project. It needs:
    - LPDDR4x/5 routing (8–10 layer HDI, length matching, SI);
    - a PMIC (RK806-class, UNVERIFIED) and power sequencing;
    - DDR-training loader for the exact DRAM part;
    - a board-specific BSP/device tree;
    - BGA reflow + X-ray.
  - Expect 2–3 spins.
  - Advice:
    - keep a SoM/dev-board path as the fallback and as the software reference (plan.md two-track logic);
    - copy the Rockchip reference design for the SoC + DDR + PMIC block;
    - have the Auditor review the schematic, stackup and layout before fab.
  - Decision recorded as a plan deviation; Krishna approves.
- **2026-11-26 (bare-RK3576 chip list).**
  - Krishna listed: RK3576 (~$22), 4 GB LPDDR4X/5 (Micron MT53D1024M32D4), 32 GB eMMC (Samsung KLMAG1JETD), RK806S-5 PMIC.
  - Auditor flags:
    - DRAM and eMMC must come from Rockchip's RK3576 memory support list (the DDR training loader is part-specific).
    - MT53D is, to my knowledge, the LPDDR4 family, not 4X (UNVERIFIED).
    - KLMAG1JETD is, to my knowledge, 16 GB, not 32 GB (UNVERIFIED).
    - Choose ONE DRAM type, matching the reference design copied.
    - RK806 variant/OTP must match the reference schematic.
    - Missing from the list: 24 MHz / 32.768 kHz crystals, Wi-Fi/BT module + antenna, PMIC inductors/passives, Maskrom/USB flashing path, debug UART, ESD, 2S→PMIC input regulation.
    - HDI PCB + BGA assembly dominate the cost, not the chips.
- **2026-11-26 (gum-stick BOM review, 1c26f35/474d1ef).**
  - Krishna locked an LCSC cart (RK3576, RK806-1, RTL8723DS, crystals, USB-C, MaskROM key; $33.69) and a harvested eMCP (₹1,000) for a custom 14×75 mm "gum-stick" board.
  - Verified on LCSC:
    - RK3576 C42388007 = **FCCSP-698L 16.1×17.2 mm**;
    - RK806-1 = QFN-68 7×7;
    - RTL8723DS = WQFN-48 6×6, **802.11b/g/n 2.4 GHz + BT 4.2**.
  - Findings:
    1. **BLOCK (geometry):** the 16.1 mm SoC is wider than the 14 mm board. Use ≥ ~20–22 mm width (Track 1 temple height).
    2. RK806 variant (OTP) must match the RK3576 reference before power-up.
    3. Bare RTL8723DS needs RF matching + antenna design; prefer a pre-certified module. BOM still says Wi-Fi 6/BT 5.0 (stale).
    4. Harvested eMCP: unknown heat/wear, prior-owner data, DDR-loader support unknown. Use a NEW part for spin 1, harvested only later.
    5. The camera rows are still Sinoseen IMX662/MV12; they contradict the IMX708 decision; IMX708 carrier PCB needed again.
    6. The physical-envelope line is still 41×41×20.
    7. The total ₹8.4–9.2k omits the HDI PCB + BGA assembly/X-ray (dominant) and passives.
    8. **False provenance:** the BOM says the design was made by "Hydrogen, Astra 6.2, Claude Opus 5.5, Autodesk". No design exists in the repo and the Auditor did not design it.
- **2026-11-26 (BOM re-check, 834822c).**
  - Accepted. Items fixed:
    - 20–22 mm board width;
    - IMX708 + DF37 carrier restored;
    - eMCP spin-1 caveat;
    - Wi-Fi 4 / BT 4.2;
    - envelope;
    - fab/assembly excluded from the total;
    - provenance credit removed.
  - Mass table re-summed: 98.1 + 4.8 = 102.9 g ✓ (unmeasured estimates).
  - Remaining small items:
    - camera row says "Tested on Raspberry Pi 3B" (not yet tested; bare SA31VA30P doesn't fit the Pi's 15-pin port);
    - a 20–22 mm board inside a 20–22 mm temple leaves no room for shell walls (outer ≈ 24–25 mm);
    - thermal row still RT42 (PCM grade decision open);
    - RK806 OTP / RF checks before ordering.
- **2026-11-27 (schematic_components.md review, 42a6010).**
  - Verdict: **NOT ready for schematic capture.** It is a generic parts list, not derived from the RK3576 reference schematic.
  - Errors / hazards:
    - R11 220k described as a "pull-down for Left" on MAX98357A SD_MODE. It must be a pull-UP; 0.77–1.4 V = RIGHT. As a pull-down, the amp stays in shutdown.
    - I2C pull-ups to 3.3 V for the IMX708/PMIC: IMX708 I/O is 1.8 V (hazard). RK806 host interface may be SPI (UNVERIFIED).
    - D2 1 A Schottky as USB backfeed protection on a ~2.3–2.9 A rail (thermal hazard); needs an ideal diode / power-path ≥3 A.
    - J4 2-pin 1.25 mm for 5 V at ~3 A (under-rated); "1.25 mm ... 2.54 mm spacing" contradictory.
    - Crystal load caps wrong: CL 12 pF needs ~2×(CL−Cstray) ≈ 18–20 pF; 12.5 pF is not a stock value.
    - Only 4 PMIC bucks: missing CPU big/little split, GPU, DDR VDD1/VDD2/VDDQ, eMMC VCC/VCCQ, VCCIO banks; no PMIC input caps.
    - 24 decaps for a 698-ball SoC is far below a reference design.
    - RTL8723DS: missing its own crystal, RF matching, antenna.
    - No VBUS TVS; no debug UART; no PWRON key; boot straps missing.
    - R14 IP2326 ISET is on the compute board, but the IP2326 is a separate module.
    - "6nm" is wrong (RK3576 = 8 nm per the vendor datasheet).
    - Ball pitch 0.5 mm UNVERIFIED (Krishna said 0.65/0.8).
    - "100% JLCPCB compatible" is an unverified claim; a harvested eMCP can't be robot-placed from stock.
- **2026-11-27 (schematic_components.md re-review, 90a9763).**
  - S1, S2, S4 (text), S5, S6, S8, S9, S10 fixed; S7 power tree added (all UNVERIFIED, honest).
  - **S3 NOT fixed.** TI pages:
    - LM66100 = 1.5 A, 79 mΩ;
    - TPS2113A = 1.25 A, 84 mΩ;
    - neither meets the "≥3 A, <30 mV" stated.
    - TPS2121 = 4.5 A / 56 mΩ (≈0.17 V, 0.5 W at 3 A) or TPS2120 = 3 A / 62 mΩ.
    - <30 mV needs an ideal-diode controller + low-Rds MOSFETs.
  - New findings:
    - VCCIO_3V3 0.6 A LDO feeds the MAX98357A amps + Wi-Fi TX + the camera AP3429K: the amps belong on VSYS_5V, and the 3.3 V budget is too small.
    - J4 "JST-PH 2.0" is rated ~2 A, below the ≥3 A spec → pads only.
    - 24 decaps vs the power-tree text (4×100 nF per rail).
- **2026-11-27 (schematic_components.md @ f3bb3a6).**
  - S3 fixed: TPS2121RUXR verified on TI (4.5 A, 56 mΩ, RUX 12-pin); drop 0.17 V and 0.5 W stated.
  - S11, S12, S13 fixed.
  - One remaining item, S14: VCCIO_3V3 at 0.85 A "RK806 LDO / Ext" from 5 V would burn ≈1.45 W as an LDO → must be a buck (RK806 buck or external). Same check for VCC_EMMC.
  - Verdict: accepted as the parts spec once S14 is fixed. Every value is still UNVERIFIED pending the RK3576 EVB schematic + PDN guide.
- **2026-11-27 (schematic_components.md @ 724f3b5).** S14 fixed.
  - VCCIO_3V3 is now RK806 BUCK6: 2.81 W out / 3.05 W in, 0.24 W loss ✓.
  - VCC_EMMC is BUCK7 or the BUCK6 domain + FB3: 0.11 W loss ✓.
  - Post-LDO rule added. **Parts spec ACCEPTED** (still UNVERIFIED pending the RK3576 EVB + PDN guide).
  - Notes:
    - MV12 PDF deletion was Krishna's instruction (MV12 not used); note 222e3ca's link now points to git history only.
    - WATCHLIST: per-rail max currents summed far exceed VSYS 3 A / MP2315 3 A; a simultaneous-load power budget is needed before regulator sizing.
- **2026-11-27 (datasheets 7dd3b38 vs schematic_components.md).**
  - Added: RK3576 DS Rev1.5, RK806 DS Rev1.3, crystals, USB-C, switch.
  - **Missing:** RK3576 EVB reference schematic, hardware design guide, PDN guide and memory support list. The commit message says "reference design" but none is included.
  - RK806 pages carry a "Rockchip Confidential" watermark (Krishna says not NDA).
  - Verified facts:
    - RK3576 FCCSP698L 16.1×17.2 mm, ball 0.30 mm, pitch 0.55/0.60/0.65 mixed.
    - Rails typ 0.75 V (CPU ≤1.0, GPU/NPU ≤0.918, LOGIC ≤0.825).
    - Separate rails: PMU 0.75, DDRPHY 0.75, PLL 0.75/1.8, OSC 1.8, USB2 0.75/1.8/3.3, USB3/PCIe 0.85.
    - LPDDR4 VDDQ 0.6 + retention 1.1; LPDDR4X-4266 and eMMC 5.1 supported.
    - θJA 15.84, θJB 6.96, θJC 0.67 °C/W.
    - RK806: VIN 2.7–5.5 V (abs 6.5).
      - BUCK1 6.5 A, 2–4 5 A, 5–10 3 A.
      - NLDO/PLDO 300/500 mA.
      - I2C (CS→VCCA, addr 0x23) or SPI.
      - Internal 32.768 kHz RC oscillator, so no crystal.
      - Typical app: 0.22 µH on BUCK1–4, 0.47 µH on 5–10; 3×/2×22 µF out; 22 µF per VCCx.
      - OTP defaults per variant (-1, -2 master/slave, -3).
  - Findings P1–P7:
    - P1 pitch.
    - P2 interface.
    - **P3 BLOCK:** rail→buck mapping ignores OTP defaults (e.g. BUCK5 = 0.85 V, BUCK7 = 2.0 V at boot); variant for RK3576 is unknown without the EVB.
    - P4 inductors/caps.
    - P5 rail values / missing rails.
    - P6 Y2 crystal unusable on RK806.
    - P7 boot via SARADC_IN0_BOOT.
- **2026-11-27 (EVB + HDG @ de26548; spec @ 7e67e27).**
  - 7e67e27 applied P1, P2, P4–P7 and marked the mapping DO-NOT-CAPTURE (OK).
  - EVB "Schematics Only for RK3576 EVB1" (28 p) and the RK3576 Hardware Design Guide (265 p) added.
  - **The EVB/HDG use the RK806S-5, NOT the RK806-1** (EVB p1/p5/p6; HDG §2 "RK3576 with RK806S-5"); the LCSC cart has RK806-1 C5156483.
  - EVB p6 mapping (RK806S-5):
    - BUCK1 CPU_BIG 0.85 / BUCK2 NPU 0.75 / BUCK3 CPU_LIT 0.85 / BUCK4 VCC_3V3_S3 3.3 / BUCK5 GPU ADJ / BUCK6 VDDQ_DDR ADJ 0.61 (LP4x) / BUCK7 LOGIC + LOGIC_MEM 0.75 / BUCK8 VCC_1V8_S3 / BUCK9 VDD2_DDR ADJ 1.1 / BUCK10 VDD_DDR 0.85;
    - PLDO1–3 fed from an external 2.1 V buck, NLDO1–5 from an external 1.1 V buck;
    - eMMC 3V3/1V8 from load switches;
    - VCC5V0_SYS = 5 A DC/DC.
  - EVB defaults the PMIC to **SPI mode** (CS floating); I2C is optional. The Auditor's earlier "pick I2C" advice is revised: follow the EVB (SPI) to match the BSP.
  - RK3576 32k: internal PVTM or external 32.768 kHz (EVB uses an RTC IC).
  - EVB memory = LPDDR4X 200-ball + separate storage; our eMCP-254 needs its own DDR routing per HDG rules.
- **2026-11-27 (E-round @ e8be63b).**
  - E1–E6 implemented. Verified:
    - RK806S-5 = LCSC C49174044;
    - SY8205FCC 5 A (C111875), replacing MP2315;
    - TMI3112H 2 A (C2985060, also on the EVB);
    - SY6280AAC (C55136);
    - PVTM 32k chosen;
    - eMCP DDR rules noted.
  - **E7 BLOCK:** NLDO1/NLDO2 swapped vs EVB p.6 (EVB: NLDO1 = VDD_0V75_S3 0.75 V, NLDO2 = VDDA_DDR_PLL 0.85 V). Wired per the spec, PMU_LOGIC (max 0.825 V, RK3576 DS T3-2) would get 0.85 V from OTP.
  - Doc mismatches vs EVB p.6:
    - BUCK1/3/10 default 0.85 V (spec 0.75);
    - slots BUCK1 = 2, BUCK4 = 5, BUCK8 = 3, PLDO2 = 5 (spec differs);
    - PLDO4 = 3.0 V (spec 3.3);
    - NLDO5 0.5 A (spec 0.3).
  - Watchlist:
    - 16.5 W transient vs the 3 W thermal burst plan, which needs DVFS/power caps;
    - battery side ≈3.1 A vs the HY2212 3 A BMS trip;
    - hardware_bom.md still lists MP2315 (L148, L175).
- **2026-11-27 (E7–E10 @ 4d02ff5).**
  - All accepted:
    - NLDO1 = VDD_0V75_S3 / NLDO2 = DDR_PLL as on EVB p.6;
    - defaults/slots match EVB p.6;
    - watchlist (16.5 W vs thermal; ~3.1 A vs HY2212 trip) written into §2.2;
    - BOM MP2315 → SY8205FCC.
  - **GREEN for schematic capture** (copy EVB sheets 04/05/10/23/24 + SoC sheets; eMCP DDR per HDG rules).
  - Next review = the schematic, then stack-up/DDR layout before fab.
- **2026-11-27 (6bc8e11 + schematic kickoff).**
  - 6bc8e11 (Krishna) switched the RK806 to I2C (EVB nets I2C1_SDA/SCL_M0_RK806, R2324 CS→VCCA, R2306/R2307 pull-ups); added CW3301 for 1.8 V (EVB U2402); PWRON = pin 4 (INT = pin 19).
  - **Auditor correction:** the EVB DOES use I2C. My earlier "follow EVB SPI" misread the chip-default "(Def)" note. 6bc8e11 is right.
  - Open: J2 lists "1.2V VDD_CORE" (IMX708 DVDD = 1.1 V per RP schematic), and J2 = DF37 on the main board conflicts with the front-bridge PCB plan (24 mm sensor tail).
  - Schematic capture round SCH-1 (power + SoC power/clock/reset/boot) prompt given to Krishna. Tool proposed: KiCad (text-reviewable) = deviation from plan.md §8 Fusion; Krishna decides.
- **2026-11-27.** Krishna's decision: schematic in **Autodesk Fusion Electronics via MCP** (Hydrogen, reasoning high), per plan.md §8. KiCad proposal withdrawn.
  - Review needs committed exports from Fusion:
    - PDF;
    - netlist;
    - BOM CSV;
    - ERC/DRC report;
    - EAGLE-format .sch if Fusion can export it (UNVERIFIED).
- **2026-11-27 (SCH-1 report).**
  - Hydrogen reported SCH-1 commit 3262024 (Fusion v1, ERC 0 errors / 33 warnings), but **3262024 is NOT on origin** (only libs cf68c7b + docs 9d9afcf were pushed). Review pending the push.
  - Checked libraries/RK806-1.lbr: all 69 pads mapped (SW1/VCC1/SW2/VCC2 dual pads OK); **MPN attribute = "RK806-1" → must be RK806S-5** (same QFN68).
  - To verify after push:
    - "MIPI_DPHY_CSI1-4 grounded" vs the camera's CSI port;
    - FB1/FB2 set "nc" vs EVB;
    - the HDG unused-PHY rules.
- **2026-11-27 (SCH-1 review @ 1617157 / 0593272).**
  - Verified from the committed netlist/BOM/ERC:
    - FB dividers: BUCK5 0.75, BUCK6 0.61, BUCK9 1.10, U6 2.094, U7 1.10, SY8205 4.99 V.
    - I2C mode (CS→VCCA net, 10k pull-ups to VCCIO = PLDO6 as EVB).
    - EXT_EN → U6/U7.
    - NPOR from RESETB.
    - Crystal 18 pF + 22R + 510k.
    - CPU/GPU/NPU/LOGIC/DDR rails on the right balls.
    - ERC 0 errors.
  - **X1 BLOCK:** PMU_LOGIC_DVDD0V75 on VDD_LOGIC_S0; EVB = VDD_0V75_S3 (NLDO1, which is left unused).
  - **X2 BLOCK:** DDRPHY_CKE_VDDQ on VDDQ_DDR 0.61 V; DS = 1.06–1.17 V retention; EVB net VDDQ_DDR_CKE_S3.
  - Other findings:
    - X3 VCCIO7 NC; HDG says 1.8 V when UFS is unused.
    - X4 USB3_OTG0_DP_TX rails NC; the cited HDG §2.2.2.13 doesn't allow it.
    - X5 UFS rails NC uncited.
    - X6 VCCIO2/3 = 3.3 V vs EVB 1.8 V → needs an IO-bank allocation table.
- **2026-11-27 (agent model choice).**
  - Krishna wants an OpenAI model for the schematic work (Hydrogen = good executor, weak designer).
  - Auditor advice (web-checked):
    - GPT-6.2 Astra (released 2026-11-17, Codex id gpt-6.2-astra, API $8/$40 per M tokens) at **high** for first capture of hard sheets (SCH-2 DDR/eMCP, SCH-3 camera MIPI);
    - GPT-6.2 Sol (gpt-6.2-sol, $2/$10) at **medium/high** for fix rounds and exports;
    - xhigh only for the DDR ball/pin mapping.
  - Same cost rules (script-driven Fusion, no screenshots, push before reporting).
- **2026-11-27 (SCH-1 ERC warnings, Fusion screenshots from Krishna).**
  - 33 warnings, all EAGLE code 104 "POWER pin X connected to <net>", matching out/FRIDAY_Compute_SCH1_erc.txt (33 × code 104, no other warning types). Sheet 1: D1/J1 VBUS, U10 PVIN/VCC. Sheet 2: U2 VCC1–14, VCCA, VCCIO, VDC, VOUT1–10. Sheet 3: U6/U7 IN.
  - Benign (a supply-type pin tied to a project net name), and the netlist was checked separately.
  - Advice: Approve them in Fusion ERC with a note, so any NEW warning stands out. Library nit: RK806 VOUTx are buck feedback/sense inputs, so mark them in/pas, not pwr.
- **2026-11-27 (SCH-1 fix round @ d9d37a8, gpt-6.2-sol).** **ACCEPTED.**
  - Netlist-verified:
    - X1 PMU_LOGIC → VDD_0V75_S3 (NLDO1);
    - X2 DDRPHY_CKE_VDDQ → BUCK9 1.1 V (net renamed VDDQ_DDR_CKE_S3);
    - X3 VCCIO7 → VCC_1V8_S0;
    - X4 USB3/DP 0V85 → NLDO4, 1V8 → VCCA_1V8_S0;
    - X5 UFS rails fed through R1320/R1323 (UNVERIFIED topology, safe);
    - X6 io_bank_map.md (VCCIO2/3 now 1.8 V; Wi-Fi SDIO on VCCIO3 via R2427; camera I2C on VCCIO5 1.8 V);
    - X7 ERC 0 errors / 0 active / 23 approved;
    - X8 VOUT pins passive.
  - Carry into SCH-2:
    - Y1 USB3/DP REXT open (EVB R1400 8.2k);
    - Y2 keep BUCK9 net name VDD2_DDR_S3 (EVB) with the CKE branch, and wire eMCP VDD2 to it;
    - Y3 power INMP441 from 1.8 V (its VDD range allows it) to match the 1.8 V SAI1 bank.
  - Next: SCH-2 (eMCP + LPDDR4X), gpt-6.2-astra high/xhigh.

## 2026-11-27 (auditor)
- Codex/Astra SCH-2 attempt ran out of 5-h quota with nothing pushed; EVB sheets 38/40 (LPDDR4X, eMMC) are NDA ->
  Krishna found ArmSoM rk3576-hardware-design repo + SK hynix eMCP spec; Hydrogen triage prompt issued.
- Hydrogen triage 22c42db reviewed -> NO for SCH-2 input until R1-R4 (see CLAUDE.md §7). Licence handling good
  (nothing proprietary committed). eMCP = H9HP52ACPMADAR-KMM. Ball map CSV plausible but needs p.6 visual check.
- 905cd31 ref-triage fix accepted; SCH-2 (eMCP/LPDDR4X) unblocked. Ask: Krishna sends eMCP spec p.6-8 images (not to git).
- eMCP p.6 ball map independently verified (254/254) from Krishna's PDF upload; Y4 eMMC passives from p.54 Table 14 carried into SCH-2.
- 2026-11-28: gap audit e0f5a4e reviewed: useful; fix G1-G6 (invented mass table, Y4 wording, eMCP height/FOV, unverified JLC/IP2326 numbers, missing antenna/memory-list/CSI chokes). eMCP library = first SCH-2 step.
- Gap audit 83a67c0 accepted. SCH-2 (eMCP lib + LPDDR4X/eMMC sheets, Y1/Y2/Y4) prompt issued to gpt-6.2-sol high.
- SCH-2 (eMCP+LPDDR4X/eMMC) @ 08e94c8 ACCEPTED after independent netlist + datasheet ball checks. Suggested next: inter-board FPC pinout, then SCH-3 camera bridge / SCH-4 battery-audio-wireless.
- Interconnect pinout v0 4623c81 accepted. Battery-split decision pending Krishna (my rec: Option B, pack on left; Option A needs right-cell fuse). DF37 pin crosswalk blocks SCH-3 connector capture.
