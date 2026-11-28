# plan1.md — Phase 1 (Extended): Shared Plan for All Agents

> **Status.** v1.2, 2026-11-26.
> - v1.1 added the Researcher's review of v1.0.
> - v1.2 adds Krishna's review of v1.1 (six acceptance-criteria fixes).
> - Each correction was verified by the Auditor. Merged by the Auditor from:
> - the Researcher's game plan (`research/notes/2026-11-25_gameplan_phase1_complete_on_mac.md`);
> - the Researcher's other notes;
> - the Auditor's co-simulation / E-DEV-1 ruling (`docs/plan1_context.md`, 2026-11-26).
>
> **This is the single plan every agent works from.** Only Krishna approves changes. Any agent may *propose* a change (with evidence), addressed to Krishna.
>
> **Precedence.**
> - `docs/plan.md` v9.1 remains the architecture baseline. Where this file changes it, the change is listed in §8 as a deviation with its approval status.
> - `docs/hardware_bom.md` is the hardware source of truth.

---

## 0. Who does what (sync rules)

| Agent | Role | Reads first | Writes |
|---|---|---|---|
| **Krishna** | Project Lead. Approves every decision, threshold and deviation. Relays all messages. | — | decisions in §9 |
| **Claude Researcher** | Designs methods and experiments, with sources. Answers "how". | this file, `research/` | `research/notes/YYYY-MM-DD_*.md` |
| **Gemini Notebook (NotebookLM)** | Source lookup from uploaded primary sources only. Answers the Researcher's "FOR GEMINI NOTEBOOK" questions. | uploaded sources | answers relayed by Krishna |
| **Antigravity (Hydrogen)** | Implements **only** itemized, approved tasks. One milestone item set = one SHA, then stop. | this file, `CLAUDE.md` §2–§3, §6 | code, run outputs, status line in §6 |
| **Claude Auditor** | Reviews every SHA, run output and proposal. Issues BLOCK/WATCHLIST findings. Owns the electrical/thermal/mass sign-off. | everything | `CLAUDE.md` §7, `docs/plan1_context.md` |

**Rules for everyone:**
1. **Read this file at the start of every session.** Check the status table (§6) and open decisions (§9).
2. **The 7-step protocol (plan.md §0) applies to every milestone:**
   1. findings;
   2. fix;
   3. commit + SHA + stop;
   4. Auditor review;
   5. dry run;
   6. Auditor review;
   7. Kaggle/real run, then Auditor review. Only after that does anyone write PASS.
3. **No claim without committed run output.** "UNVERIFIED" is a valid word; an invented number is not.
4. **Pass/fail thresholds are fixed by Krishna before the run** and written into §5. They are never edited after seeing results.
5. **Eval sets are frozen (sha256 manifest) before any training that could see them.** No test-set words in rules.
6. **Safety rule (non-negotiable).** Every spoken number, dose or price comes from:
   - the extractive reader;
   - the deterministic math parser; or
   - a named web source.

   Chat, visual Q&A and translation never originate digits.

---

## 1. Why Phase 1 is extended

- **Phase 1 (Milestone 1.5) PASSED** (Kaggle `7571e39`): pipeline, distillation, INT4 export, safe reader at 0 wrong numbers.
- **The product is not done.** The student cannot see objects or chat, and wake needs 5–6 tries.
- **No compute board will be bought with personal money.** The Firefly CAM-3576Q38 is to be requested through an NMIMS grant.
- So **Phase 1 now ends at the hardware-purchase gate**: FRIDAY fully working on the Mac, proven convertible to RK3576, with an honest grant dossier.
- **Phase 2 (embedded port) starts only after the board arrives.**

| Sub-phase | Meaning | Status |
|---|---|---|
| **1A** | Milestone 1.5 (pipeline + safe reader) | **DONE** (`7571e39`, closed in `d753999`) |
| **1B** | Milestone 1.6 live Mac demo | Partly done (`96d2547`); bugs carried into M0 |
| **1C** | "Phase 1 Complete (Mac)": M0–M9 below | **NEXT** |

---

## 2. Definition of done: "Phase 1 Complete (Mac)" gate

All items are backed by committed run output. Thresholds are the Researcher's proposals; **Krishna fixes them in §5 before each run.**

### A. Functions (live on the Mac: webcam, mic, speaker; Wi-Fi off unless stated)

| # | Function | Proposed pass criterion |
|---|---|---|
| F1 | "Hey Friday" wake | <ul><li>Chime on the first try in ≥95% of 100 attempts.</li><li>≤1 false wake/hour of background speech.</li><li>**Primary latency:** audible end of "Friday" → audible start of chime, measured on one loopback recording of mic + speaker. Proposed p95 ≤ 300 ms (Krishna fixes).</li><li>**Diagnostic:** detection → chime (proposed ≤ 80 ms), so a slow result can be traced to the detector or to playback.</li></ul> |
| F2 | Safe reader | **0 wrong spoken numbers/entities (hard limit) AND minimum correct counts**, so a reader that refuses everything cannot pass:<ul><li>spec ≥ 38/40;</li><li>stress ≥ 36/40;</li><li>TEST ≥ 17/20.</li></ul>These equal the `7571e39` baseline (no regression allowed). Live check: 20 real labels, minimum correct fixed before the run. |
| F3 | Visual Q&A | Objects and colours ≥70% on FRIDAY-Real-100; confident-wrong ≤10%; ≥ SmolVLM-256M on public sets |
| F4 | Follow-ups | Same-object follow-ups correct in ≥80% of 30 scripted 3-turn dialogues |
| F5 | People + Easter egg | Description-only policy, 0 sensitive inferences on 30 photos. Easter egg: 0 false triggers on 500 other faces, ≥90% on Krishna |
| F6 | Math | Model writes the expression, parser computes it. ≥90% exact on a held-out set; 0 spoken numbers not from the parser |
| F7 | Conversation / persona | Persona and tone consistent in ≥80% of 50 judged turns; no invented numbers; remembers the last 3 turns |
| F8 | Router | Correct skill for ≥95% of 200 held-out utterances |
| F9 | Online fallback | Wi-Fi on: sourced answer in ≥90% of 30 web questions. Wi-Fi off: the Directive-04 offline sentence, never a made-up answer |
| F10 | Hindi (translation layer) | Hindi in → Hindi out via the English core. **Quantity check:** every complete value + unit in the Hindi output (including numbers spoken as words, e.g. "डेढ़ किलो") must equal a value + unit in the verified English answer. Digit-sequence matching is not enough: `1.5 kg` → `15 kg` keeps the digits. Any unmatched quantity → speak the English answer. **Low priority** (Krishna 2026-11-25); **not part of the purchase gate** unless Krishna decides otherwise (§9 D15). |

### B. Device-faithfulness (so "works on Mac" transfers)

| # | Criterion |
|---|---|
| D1 | The Mac runs the **artifacts that will ship**: INT4 student, same vision tower, same STT/TTS/OCR models. No fp16-only demo. |
| D2 | **Gate measurement = peak memory during a complete live turn**:<ul><li>all intended models loaded;</li><li>camera active;</li><li>conversation history populated (3 turns);</li><li>image encode + generation + TTS in that turn.</li></ul>Peak ≤ the AI budget (proposed 2.0 GB of the 4 GB board). Per-model readings are **diagnostics only**: they double-count shared runtime and miss inference temporaries. The Mac peak is an estimate for the board. <ul><li>Estimate: about 1.0 GB without Hindi; 1.4–1.85 GB with it.</li><li>With OS and ISP buffers: about 1.5 GB / 1.9–2.4 GB (Researcher `a1b3853`).</li><li>**The Hindi layer is the budget risk.**</li></ul>Measurement method:<ul><li>fresh process per model;</li><li>psutil RSS after load;</li><li>`torch.mps.current_allocated_memory()` for MPS;</li><li>results committed as JSON.</li></ul> |
| D3 | **D3a (purchase gate, host-side):** every on-device model exports and converts with RKLLM-Toolkit / RKNN-Toolkit2 for `rk3576`, and passes the host-side numeric checks (§4.3). **D3b (first board milestone, E-DEV-2):** the runtime runs an **image + correctly remapped prompt together** with our student (§4.2 step 4). Rockchip documents conversion on PC and inference on the board, so if the pinned SDK cannot run this on x86, D3b is **not** a purchase blocker. It becomes the first test after the board arrives, with the exact test script committed in M0. |
| D4 | Mac latency is reported as Mac latency. RK3576 latency is a **projection** from Rockchip's published benchmark (Qwen2-0.5B w4a16 32.56 tok/s), labelled as such. The benchmark's conditions:<ul><li>maximum CPU/NPU frequency;</li><li>128-token prompt / 64 new tokens;</li><li>memory type unstated.</li></ul>So the projection is an **upper bound**: the glasses run thermally capped. |

### C. Live acceptance

- 50-turn **unscripted** session covering F1–F9.
- Mic, camera and speaker really on; every turn logged by TurnLogger.
- **Pass:** 0 crashes, 0 wrong spoken numbers, per-function criteria met.

**Purchase / grant gate = A (F1–F9) + B (D1, D2, D3a, D4) + C.** Exception: D3a is checked in week 2. If conversion fails, the hardware plan changes *before* any training time is spent.

---

## 3. Milestones (each = its own SHA(s) through the 7-step protocol)

GPU-h are estimates, redone after E-THR-1 measures real throughput. Weeks count from approval of this plan.

| M | Weeks | Content | Kaggle GPU-h | Owner of design |
|---|---|---|---|---|
| **M0 Foundations** | 1–2 | (a) Live-demo bugs (§3.1). (b) **Freeze eval sets**: FRIDAY-Real-100, math, router, persona, people (sha256 manifests).<ul><li>Specs (size, source/licence, ground-truth format, rubric, photo shot list) are drafted by the Researcher.</li><li>Items are **authored by Krishna/Auditor, never Hydrogen**.</li></ul>(e′) **E-THR-1 protocol fixed before running.** Student tokens/s with cached teacher vs with a live teacher on the second T4, plus Qwen3-VL-2B batched-generation tokens/s. (c) **E-DEV-1** conversion (§4). (d) **E-TOK-1** tokenizer test. (e) E-THR-1 throughput. (f) Memory table v0 measured on the Mac. | ~1 | Auditor (E-DEV-1) + Researcher |
| **M1 Wake word** | 2–3 | Custom "Hey Friday" model (openWakeWord-style; synthetic TTS clips + Krishna's recordings). Chime first, then processing. | 0 | Researcher |
| **M2 KD method** | 3–4 | **E-KD-1** on math (exact-match metric), at equal GPU-h: (a) SeqKD, (b) top-64 forward KL, (c) on-policy / reverse KL. The math winner is the **default** only. Each later skill (M3, M5) runs a small 2-arm check (default vs runner-up, ≈2 GPU-h) on its own metric before full training. **The teacher-logit cache size is decided before M3 data generation**: cache top-64, so both (b) and SeqKD stay possible; storage cost recorded. | ~10 (+≈2 per skill) | Researcher |
| **M3 Visual** | 4–7 | Teacher Qwen3-VL-2B (deviation, §8). Data: VQAv2 + VizWiz + Visual Genome (CC-BY-4.0), **plus teacher-generated (Qwen3-VL-2B) single- and multi-turn answers on those images, with top-64 answer-token logits cached for KD** (matches E-KD-1 arm b; v1.1 said top-16). COCO captions for projector re-alignment (stage V1; licence UNVERIFIED). Uncertainty U-A. Follow-up dialogues. People policy. Easter egg (YuNet + SFace, CPU). | ~25–30 | Researcher |
| **M4 Math** | 6–8 | Safe arithmetic expression format; our own parser, **never `eval`**. Teachers Qwen3-1.7B / DeepSeek-R1-Distill-Qwen-1.5B. Whiteboard via OCR → expression. | ~10 | Researcher |
| **M5 Conversation** | 8–10 | "Donna" persona distilled from Qwen3-4B (non-thinking). Tone tag → Kokoro voice/speed. 3-turn memory. Number filter. | ~20 | Researcher |
| **M6 Merge + router** | 10–13 | One student vs per-skill LoRA adapters. **Forgetting matrix** (core thesis experiment). Router choice. | ~40–60 | Researcher |
| **M7 Online fallback** | 12–14 | Search API (Krishna picks; the key is never in the repo). Source naming. Offline sentence. | 0 | Researcher |
| **M8 Hindi layer** | 14–15 | STT (hi) → IndicTrans2-Dist → student → back → TTS. Quantity value + unit check (F10). *Low priority; not in the purchase gate; may slip after M9.* | ~2 | Researcher |
| **M9 Acceptance + dossier** | 15–17 | Gate C live session, D2 memory, D3 conversion of the final models, **grant dossier** (§7). | ~2 | All |

**Totals.** About 110–135 GPU-h over about 17 weeks, against about 500 h of quota. The spare quota is for re-runs and research tracks. Target end: about March 2027, leaving about 8 months for Phases 2–4.

**Research tracks (parallel; never block the gate):**
- **E-PRUNE-1:** prune Qwen3-0.6B to **matched RK3576 cost**: ≤ Qwen2.5-0.5B's non-embedding parameters and KV-cache size, with the same 64k vocabulary.
  - Three arms at equal GPU-h:
    - A: direct distillation into Qwen2.5-0.5B;
    - B: prune + heal;
    - C: prune, no heal.
  - **Pass:** B beats A on ≥3 skill metrics with non-overlapping 95% CIs.
- **E-EDIT-0 → E-EDIT-1:**
  - first reproduce ROME on GPT-2 XL (within 5 points of the paper);
  - then edit our student, before vs after INT4, at 1/10/100/1,000 edits (ROME vs MEMIT).

### 3.1 M0(a) — live-demo bugs (from Krishna's run @ 96d2547)

| ID | Location | Fix |
|---|---|---|
| L1 | router `route_intent` | "What does **this** say?" → NONE. Must route to READ. Add a router eval set; no per-phrase hacks. |
| L2 | `friday_live.py` L1994 | `FridayVoiceEngine.speak()` got unexpected kwarg `mute`. Make the signatures consistent. |
| L3 | startup | Set `TOKENIZERS_PARALLELISM=false` before forking. |
| L4 | `FrameScorer` | 2.1–2.7 s. Target ≤0.5 s on the Mac (e.g. score on a downscaled frame, run OCR only on the best frame). |
| L5 | `WakeWordDetector` | Replaced in M1; keep the current version until then. |

---

## 4. Co-simulation and E-DEV-1 (no board; ₹0)

### 4.1 What simulation can and cannot prove (Auditor ruling, 2026-11-26)

| Tool | Gives | Does NOT give |
|---|---|---|
| RKNN-Toolkit2 simulator (x86) | Numeric check of the converted/quantised graph; unsupported-op detection | Timing, NPU multi-core behaviour, bandwidth |
| RKLLM-Toolkit (x86) | `.rkllm` w4a16 conversion for `rk3576`, real file size. x86 inference for evaluation: UNVERIFIED | tok/s, memory on the board |
| QEMU aarch64 | aarch64 package/build checks only | NPU (no `/dev/rknpu`), any meaningful timing → **skip** |
| v4l2loopback / snd-aloop | Pipeline plumbing with recorded inputs | Real sensor/ISP/I2S behaviour |
| Raspberry Pi 3B | Real aarch64 and real I2S audio. Timings are **plumbing checks only**: A53 at 1.2 GHz with LPDDR2, while the RK3576 runs the LLM on its NPU and CPU work on A72 cores at 2.2 GHz. At most a loose upper bound for CPU tasks; not quantitative. | NPU; 1 GB RAM |

**Bandwidth.** Use an analytic budget only (bytes/token × tok/s; camera 1080p30 NV12 ≈ 93 MB/s; audio ≈ 0.13 MB/s). It is labelled "estimate, measured in Phase 2". It is never presented as proof.

### 4.2 E-DEV-1 steps

0. **Environment.**
   - **Python 3.12, x86 Linux.** Verified:
     - PyPI `rknn-toolkit2` 2.5.0 wheels are cp36–cp312;
     - the rknn-llm README lists Python 3.10–3.12.
   - Kaggle's 3.13 can't run them, so use a separate conda env.
   - Pin `rknn-toolkit2==2.5.0` and one fixed rknn-llm release.
   - `best_student_vlm.pt` (sha `66391bd6…`) must be on that machine.
   - The Mac can't run the toolkits natively.
   - Record exact tool versions.
1. **Source.** Start from `best_student_vlm.pt` (full precision), **not** the custom `friday_student_w4a16_packed.pt`.
2. **LLM → HF dir → `.rkllm`.**
   - **Vocabulary decision (main risk).** The student uses a pruned 64k remap (`old_to_new`), but RKLLM reads the HF tokenizer.
   - **Recommended:**
     - re-expand embeddings to the full 151,936-token Qwen vocab (pruned rows back at their original ids; others from the base model);
     - then use the stock Qwen tokenizer;
     - cost ≈ +40 MB at INT4.
   - **Alternative:** a rebuilt 64k `tokenizer.json` (riskier).
   - **Re-expansion is necessary but not enough.** The stock Qwen tokenizer emits ids outside our 64k set for **2.9–5.4% of ordinary English tokens**. Measured by the Researcher and re-measured by the Auditor with the `friday_live.py` L815+ procedure:
     - README 5.35%;
     - plan1.md 3.15%.
   - In training, `safe_encode_64k` (L855) turned these into byte tokens. Stock ids would hit rows the student never trained with: silent quality loss.
   - **Fix — use the official API (`rkllm.h`, sha `4ad19442…`, verified):**
     - feed **our own encoder's ids** through `RKLLM_INPUT_TOKEN` (L41), mapped via `new_to_old`, so device input = training input;
     - use `RKLLM_INFER_GET_LOGITS` (L53) to mask outputs to the 64k set (or at least measure out-of-set emissions).
3. **Vision → ONNX → `.rknn`.**
   - One module: SigLIP-B/16-384 + 2×2 unshuffle + projector.
   - Fixed input 1×3×384×384, output 1×144×896.
   - **FP16 is the baseline**, matching Rockchip's own multimodal benchmarks (encoder in FP16). D2 counts about 190 MB.
   - INT8 is optional, not a gate.
4. **Multimodal join, LoRA, multi-turn.** The API exists in `rkllm.h` (verified):
   - `RKLLM_INPUT_MULTIMODAL` / `image_embed` (L43, L152);
   - `RKLLMLoraAdapter` (L118–125), for the M6 adapter option;
   - `keep_history` (L257), for follow-ups.

   E-DEV-1 must still *exercise* each one with our model; existing in the header ≠ working.
5. **OCR → `.rknn`.** PP-OCRv6 det + rec.

### 4.3 E-DEV-1 pass/fail (proposed; Krishna fixes in §5)

| Check | Pass |
|---|---|
| E-TOK-1: **deployment encoder vs training `Vocab64kMapper`** on 1,000+ strings (English, Devanagari, digits, emoji, chat templates); teacher vs student non-special ids. Also report the outside-64k rate of the stock tokenizer. | 0 mismatches (rate reported, not gated) |
| HF export vs PyTorch student, same ids, fp32 | max logit diff < 1e-3 |
| Vision ONNX vs PyTorch, 50 images | cosine ≥ 0.999 |
| Vision RKNN FP16 (simulator) vs PyTorch, 50 images | cosine ≥ 0.995 (INT8 optional, reported only) |
| LLM w4a16 vs fp16 perplexity on held-out TextVQA answers + own text | ≤ 10% increase. **If RKLLM x86 inference is unavailable**, use a PyTorch fake-quant w4a16 proxy (labelled "proxy"); the real check moves to E-DEV-2 on the board. Fixed now, not after. |
| OCR RKNN vs onnxruntime on the 40-label spec set | 0 wrong; correct count within ±1 of 38 |
| Image + remapped prompt together (D3b). **Finding (Auditor, `rkllm.h` L149–160):** `RKLLM_INPUT_MULTIMODAL` takes a **text `prompt`** that RKLLM tokenizes itself, so the token-input fix (step 2) does not cover image turns. Two candidate paths, both tried:<ul><li>(i) `RKLLM_INPUT_EMBED` (L42, L128–134): we look up text embeddings with our 64k encoder on the CPU, concatenate the 144 image embeddings, and feed the whole sequence. Extra CPU embedding table ≈ 115 MB fp16; record it in D2.</li><li>(ii) `RKLLM_INPUT_MULTIMODAL` with a rebuilt 64k `tokenizer.json`.</li></ul>**Host-side (M0):** output of path (i) on PyTorch == the training forward pass (max logit diff < 1e-3). **Runtime:** on x86 if the SDK allows, else E-DEV-2 (first board test, script committed in M0). | host: pass/fail; runtime: yes/no + exact error |
| Artifact sizes recorded | within the D2 budget |

**Notes.**
- The 40-label reader set tests the **OCR conversion**, not the student. The student is not in the reading path.
- Passing E-DEV-1 proves the **conversion path**, not student quality.

### 4.4 Pi 3B audio bring-up (Milestone 2.1 pulled forward; parts ₹751)

- **One I2S bus, Pi as clock master:**
  - GPIO18 BCLK;
  - GPIO19 LRCLK;
  - GPIO20 DIN ← 2× INMP441 (L/R pin = left/right slot);
  - GPIO21 DOUT → 2× MAX98357A (SD_MODE resistors select the channel).
- **Overlay:** try `googlevoicehat-soundcard` first (playback + capture), otherwise `max98357a` + an I2S capture overlay. UNVERIFIED which works best.
- **Raw tests:**
  - `arecord -c 2 -r 48000 -f S32_LE` (INMP441 = 24-bit in 32-bit slots, low level → software gain);
  - `speaker-test -c 2` (check left/right).
- **`asound.conf`:** `dmix` + `dsnoop` on the same card; `softvol` with a hard maximum.
- **AEC:** PipeWire `libpipewire-module-echo-cancel` (webrtc). Whether it is AEC3 depends on the webrtc-audio-processing version: UNVERIFIED.
- **Test (thresholds fixed in §5):**
  - ERLE on far-end-only audio (proposed ≥15 dB);
  - double-talk Whisper WER within 10 points of clean;
  - mic level and clipping at 30 cm.
- **Camera on Pi:** needs the full Camera Module 3 board. The bare SA31VA30P (30-pin DF37) won't plug into the Pi's 15-pin CSI.

---

## 5. Thresholds (Krishna fills these before each run; never edited after results)

| Item | Threshold | Fixed by / date |
|---|---|---|
| F1–F10, D2 | (from §2, as proposed) | *pending Krishna* |
| E-DEV-1 table §4.3 | (as proposed) | *pending Krishna* |
| Pi audio ERLE / double-talk | ≥15 dB / ≤+10 WER points | *pending Krishna* |
| E-KD-1 winner rule | ≥ +2 points, non-overlapping 95% CI, else SeqKD | *pending Krishna* |
| E-VIS-1/2 | per Q4 note | *pending Krishna* |

---

## 6. Status (updated in every milestone commit; Auditor verifies)

| Milestone | Status | SHA | Auditor verdict |
|---|---|---|---|
| 1A Milestone 1.5 | DONE | `7571e39` / `c2c2cf8` | PASS (all 6 gates) |
| 1B Milestone 1.6 live demo | PARTIAL | `96d2547` | accepted for live test; bugs → M0 |
| M0 Foundations | NOT STARTED | — | — |
| M1–M9 | NOT STARTED | — | — |
| Pi 3B audio | WAITING FOR PARTS | — | — |

---

## 7. Grant dossier (M9; for NMIMS faculty advisor / HOD)

1. Phase 1 gate results (`7571e39`) with the README caveats.
2. Live Mac demo recording (gate C session).
3. E-DEV-1 report:
   - `.rkllm` / `.rknn` artifacts;
   - the pass/fail table with real numbers;
   - tool versions.
4. Pi 3B audio demo with the ERLE number.
5. Analytic latency / RAM / bandwidth budget, **labelled estimates**, citing Rockchip's benchmark.
6. BOM with the **real landed cost including duty** (≈ ₹24k at 42% duty on $204; the BOM's "past ₹19,000" is wrong).
7. **Risk register:**
   - IMX708 driver / ISP / AF on RK3576;
   - camera carrier PCB;
   - thermal (PCM grade RT44HC/RT47);
   - NPU runtime version;
   - mass margin.

**Wording rule:** never "only the silicon remains". Use: *"Everything that can be validated without the board has been validated; the board is needed to measure the following."*

---

## 8. Deviations from plan.md v9.1

| # | Deviation | Status |
|---|---|---|
| V1 | Camera IMX415 → IMX708 (SA31VA30P, Robu.in) | **APPROVED** by Krishna (`03fc2e7`). RK3576 driver unverified. |
| V2 | Compute: Firefly CAM-3576Q38 kept; funding via NMIMS grant; MV12 rejected | **APPROVED** (`ebe3b84`) |
| V3 | Phase 1 extended to the "Phase 1 Complete (Mac)" gate before any purchase | **This document — pending Krishna's approval** |
| V4 | Multiple skill teachers instead of the single Qwen2-VL-2B (VLM: Qwen3-VL-2B; math: Qwen3-1.7B / R1-Distill-Qwen-1.5B; chat: Qwen3-4B) | pending (D1) |
| V5 | Voice wake word in addition to the touch button | pending (D3) |
| V6 | English-only core + translation layer for hi (later mr, gu) | **APPROVED** by Krishna 2026-11-25 (low priority) |
| V7 | Weight limit ≤120 g vs Directive 05's ≤125 g | pending (plan.md inconsistent) |

---

## 9. Open decisions for Krishna (consolidated)

| # | Decision | Recommended default |
|---|---|---|
| D1 | Multi-teacher switch (V4) | Approve |
| D2 | Skill order | Order as in §3 (visual → math → chat → router → online → Hindi) |
| D3 | Voice wake word on glasses (V5) | Approve for Mac; power measured in Phase 2 |
| D4 | Research-track success criteria (editing, pruning) | As in §3 research tracks |
| D5 | Approve this plan (V3) and **M0 as Hydrogen's next task** | Approve |
| D6 | Fix the thresholds in §5 | — |
| D7 | Make FRIDAY-Real-100 (100 own photos + written ground truth) in M0 | Yes, before any visual training |
| D8 | People-description policy (gender words hedged or not) | Allowed, hedged; fallback "a person" |
| D9 | Student base: stay Qwen2.5-0.5B (32.56 tok/s) vs Qwen3-0.6B (24.85 tok/s) | Stay; revisit after E-PRUNE-1 |
| D10 | qwen-research-licensed models for research tracks | No; Apache/MIT only |
| D11 | Search API for M7 | Krishna picks; the key is never committed |
| D12 | E-DEV-1 vocabulary strategy | Re-expand to full Qwen vocab |
| D13 | Weight limit 120 g vs 125 g | 120 g hard |
| D14 | Clean the Gemini Notebook sources (remove the AI-generated "Technical Evaluation" doc; add primary papers) | Yes |
| D15 | Is Hindi (F10) required for the purchase/grant gate? | No; low priority, after the gate |
| D16 | Battery placement + charging (2026-11-28; deviation from plan.md §2.1 split cells) | Option B: both cells + 2S protection + balance + charger on LEFT temple; only protected PACK+/PACK- cross the frame. Charging: 3-pin magnetic pogo (VBUS/GND/DET) on left tip for daily use + USB-C on right for charge AND flash, ideal-diode OR at the charger input |
