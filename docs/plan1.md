# plan1.md — Phase 1 (Extended): Shared Plan for All Agents

> **Status.** v1.0, 2026-11-26. Merged by the Auditor from:
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
| F1 | "Hey Friday" wake | Chime on the first try in ≥95% of 100 attempts; ≤1 false wake/hour of background speech; chime <80 ms after detection |
| F2 | Safe reader | 0 wrong numbers on spec / stress / TEST sets, plus a live label check |
| F3 | Visual Q&A | Objects and colours ≥70% on FRIDAY-Real-100; confident-wrong ≤10%; ≥ SmolVLM-256M on public sets |
| F4 | Follow-ups | Same-object follow-ups correct in ≥80% of 30 scripted 3-turn dialogues |
| F5 | People + Easter egg | Description-only policy, 0 sensitive inferences on 30 photos. Easter egg: 0 false triggers on 500 other faces, ≥90% on Krishna |
| F6 | Math | Model writes the expression, parser computes it. ≥90% exact on a held-out set; 0 spoken numbers not from the parser |
| F7 | Conversation / persona | Persona and tone consistent in ≥80% of 50 judged turns; no invented numbers; remembers the last 3 turns |
| F8 | Router | Correct skill for ≥95% of 200 held-out utterances |
| F9 | Online fallback | Wi-Fi on: sourced answer in ≥90% of 30 web questions. Wi-Fi off: the Directive-04 offline sentence, never a made-up answer |
| F10 | Hindi (translation layer) | Hindi in → Hindi out via the English core. Every digit in the Hindi output equals a digit in the English answer, else speak English. **Low priority** (Krishna 2026-11-25) |

### B. Device-faithfulness (so "works on Mac" transfers)

| # | Criterion |
|---|---|
| D1 | The Mac runs the **artifacts that will ship**: INT4 student, same vision tower, same STT/TTS/OCR models. No fp16-only demo. |
| D2 | Summed resident memory of all on-device models (measured on the Mac) ≤ the AI budget (proposed 2.0 GB of the 4 GB board). |
| D3 | Every on-device model converts with RKLLM-Toolkit / RKNN-Toolkit2 for target `rk3576` (E-DEV-1, §4) **and passes the numeric checks**. |
| D4 | Mac latency is reported as Mac latency. RK3576 latency is a **projection** from Rockchip's published benchmark (Qwen2-0.5B w4a16 32.56 tok/s) and is labelled as such. |

### C. Live acceptance

- 50-turn **unscripted** session covering F1–F9.
- Mic, camera and speaker really on; every turn logged by TurnLogger.
- **Pass:** 0 crashes, 0 wrong spoken numbers, per-function criteria met.

**Purchase / grant gate = A + B + C.** Exception: D3 is checked in week 2. If conversion fails, the hardware plan changes *before* any training time is spent.

---

## 3. Milestones (each = its own SHA(s) through the 7-step protocol)

GPU-h are estimates, redone after E-THR-1 measures real throughput. Weeks count from approval of this plan.

| M | Weeks | Content | Kaggle GPU-h | Owner of design |
|---|---|---|---|---|
| **M0 Foundations** | 1–2 | (a) Live-demo bugs (§3.1). (b) **Freeze eval sets**: FRIDAY-Real-100, math, router, persona, people (sha256 manifests). (c) **E-DEV-1** conversion (§4). (d) **E-TOK-1** tokenizer test. (e) E-THR-1 throughput. (f) Memory table v0 measured on the Mac. | ~1 | Auditor (E-DEV-1) + Researcher |
| **M1 Wake word** | 2–3 | Custom "Hey Friday" model (openWakeWord-style; synthetic TTS clips + Krishna's recordings). Chime first, then processing. | 0 | Researcher |
| **M2 KD method** | 3–4 | **E-KD-1** on math (exact-match metric), at equal GPU-h: (a) SeqKD, (b) top-64 forward KL, (c) on-policy / reverse KL. The winner is used in M3–M5. | ~10 | Researcher |
| **M3 Visual** | 4–7 | Teacher Qwen3-VL-2B (deviation, §8). Data: VQAv2 + VizWiz + Visual Genome (CC-BY-4.0). Uncertainty U-A. Follow-up dialogues. People policy. Easter egg (YuNet + SFace, CPU). | ~25–30 | Researcher |
| **M4 Math** | 6–8 | Safe arithmetic expression format; our own parser, **never `eval`**. Teachers Qwen3-1.7B / DeepSeek-R1-Distill-Qwen-1.5B. Whiteboard via OCR → expression. | ~10 | Researcher |
| **M5 Conversation** | 8–10 | "Donna" persona distilled from Qwen3-4B (non-thinking). Tone tag → Kokoro voice/speed. 3-turn memory. Number filter. | ~20 | Researcher |
| **M6 Merge + router** | 10–13 | One student vs per-skill LoRA adapters. **Forgetting matrix** (core thesis experiment). Router choice. | ~40–60 | Researcher |
| **M7 Online fallback** | 12–14 | Search API (Krishna picks; the key is never in the repo). Source naming. Offline sentence. | 0 | Researcher |
| **M8 Hindi layer** | 14–15 | STT (hi) → IndicTrans2-Dist → student → back → TTS. Digit-preservation check. *Low priority; may slip after M9.* | ~2 | Researcher |
| **M9 Acceptance + dossier** | 15–17 | Gate C live session, D2 memory, D3 conversion of the final models, **grant dossier** (§7). | ~2 | All |

**Totals.** About 110–135 GPU-h over about 17 weeks, against about 500 h of quota. The spare quota is for re-runs and research tracks. Target end: about March 2027, leaving about 8 months for Phases 2–4.

**Research tracks (parallel; never block the gate):**
- **E-PRUNE-1:** Qwen3-0.6B pruned + healed vs our student.
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
| Raspberry Pi 3B | Real aarch64; A53 cores = RK3576's little cores, so CPU timings are a **pessimistic** bound; real I2S audio | NPU; 1 GB RAM |

**Bandwidth.** Use an analytic budget only (bytes/token × tok/s; camera 1080p30 NV12 ≈ 93 MB/s; audio ≈ 0.13 MB/s). It is labelled "estimate, measured in Phase 2". It is never presented as proof.

### 4.2 E-DEV-1 steps

0. **Environment.**
   - Linux x86 with the Python version supported by the Rockchip wheels (check the wheel tags: Kaggle's 3.13 may not be supported → use a conda env or a CPU session).
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
3. **Vision → ONNX → `.rknn`.**
   - One module: SigLIP-B/16-384 + 2×2 unshuffle + projector.
   - Fixed input 1×3×384×384, output 1×144×896.
   - fp16 first, then INT8 calibrated on ~100 COCO images.
4. **Multimodal join.** Feed the 144 image embeddings to RKLLM as prompt embeddings (check the `rknn-llm` multimodal example; API UNVERIFIED). LoRA support in RKLLM: check (needed for the M6 adapter option).
5. **OCR → `.rknn`.** PP-OCRv6 det + rec.

### 4.3 E-DEV-1 pass/fail (proposed; Krishna fixes in §5)

| Check | Pass |
|---|---|
| E-TOK-1: tokenizer round-trip (English, Devanagari, digits, emoji) vs training mapping; teacher vs student non-special ids | 0 mismatches |
| HF export vs PyTorch student, same ids, fp32 | max logit diff < 1e-3 |
| Vision ONNX vs PyTorch, 50 images | cosine ≥ 0.999 |
| Vision RKNN (simulator) vs PyTorch, 50 images | cosine ≥ 0.995 fp16 / ≥ 0.98 INT8 |
| LLM w4a16 vs fp16 perplexity on held-out TextVQA answers + own text | ≤ 10% increase |
| OCR RKNN vs onnxruntime on the 40-label spec set | 0 wrong; correct count within ±1 of 38 |
| Multimodal embedding input accepted by RKLLM API/simulator | yes / no (record the exact error if no) |
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
