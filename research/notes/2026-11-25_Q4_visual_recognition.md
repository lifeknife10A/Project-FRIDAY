# 2026-11-25 — Q4 Visual recognition: objects, colours, people, uncertainty, follow-ups

Author: Claude Researcher. Status: PROPOSAL, awaiting Krishna and the Auditor.

## 0. Requirement as stated by Krishna (R5 + 2026-11-25 clarification)

- **Objects.** "What am I holding?" / "What is in front of me?"
- **Colours.** "What colour is it?" (as a follow-up).
- **People.** Describe only: "a man in a blue shirt, smiling". Never name anyone.
  - One exception: an Easter egg for **Krishna's own face only** ("you're looking at Krishna, the GOAT").
- **Uncertainty.** Say when it isn't sure.
- **Follow-ups.** Short-term memory of the current image and the conversation about it.
- **Language.** English only (translation layer later, per the language-scope note).

## 1. Where we are (committed evidence)

- **The Phase 1 student cannot ground objects.** It was trained for 100 KD steps on TextVQA only. In the live run "What am I holding?" gave "The person is holdingThe person is holding…" (plan.md §11.1).
  - This is a data and steps problem, not an architecture verdict. The student never saw object or colour questions.
- **Architecture stays as plan v9.1:** SigLIP-B/16-384 (frozen) → 2×2 unshuffle (144 tokens) → projector → Qwen2.5-0.5B. Whether Qwen3-0.6B pruned replaces it is decided by E-PRUNE-1, not here.

## 2. Teacher

| Candidate | Licence | Tokenizer vs student | Fits a T4 | Notes |
|---|---|---|---|---|
| Qwen2-VL-2B-Instruct (Phase 1) | Apache-2.0 | same BPE; lacks ids 151655–151664 (tokenizer note) | yes (8.48 GB peak, Phase 1) | Known pipeline. Weak reader (23/40, 11 wrong) but reading is not this skill. |
| **Qwen3-VL-2B-Instruct** | Apache-2.0 | same BPE; adds 4 special ids (string-map) | yes in fp16 (2B; exact peak to measure) | Officially RKLLM-supported. RK3576: encoder 1.61 s, decode 10.36 tok/s (benchmark.md), so it is also an on-device reference point. |
| Qwen2.5-VL-7B-Instruct | Apache-2.0 | identical | only in 4-bit, alone on a GPU | Strongest; use only offline to generate labels. |
| Qwen2.5-VL-3B | **qwen-research** | — | — | Excluded (licence). |

**Recommendation:**
- **Qwen3-VL-2B as the single visual teacher.** It is newer, Apache-licensed and fits a T4.
- **Qwen2.5-VL-7B (4-bit) as an optional label checker** on items where we need higher-quality references.
- Changing the teacher from Qwen2-VL-2B is a **plan.md §5.1 deviation, so Krishna decides.**
- Teacher quality on *our* tasks is not assumed. It is measured in E-VIS-1 alongside the student.

## 3. Training data (licences checked where stated)

| Data | Use | Licence (source) |
|---|---|---|
| VQAv2 annotations (on COCO images) | object, colour and count questions; 10 human answers each, which gives a correctness signal for the uncertainty labels | annotations **CC-BY-4.0** (visualqa.org/terms.html) |
| VizWiz-VQA train | blind users' real photos plus an "unanswerable" label, which teaches "I can't tell" | **CC-BY-4.0** (vizwiz.org VQA page) |
| Visual Genome | object attributes (colours, clothing) and relations | **cc-by-4.0** (HF tag, ranjaykrishna/visual_genome) |
| COCO images and captions | projector alignment; people and clothing descriptions | COCO terms page not readable from my environment: **UNVERIFIED** (images are under Flickr licences) |
| GQA | attribute/colour questions | **UNVERIFIED** (page fetched, licence string not found) |
| LLaVA-Instruct-150K | multi-turn conversations | cc-by-4.0 (HF tag). It is GPT-4-generated, so OpenAI's terms on outputs may apply: UNVERIFIED. **Prefer our own teacher-generated dialogues instead.** |

**Our own generated data** (teacher outputs, Apache):

| Component | Detail |
|---|---|
| Images | COCO/VQAv2/VizWiz train images |
| Prompts, single-turn | fixed templates: "What is the person holding?", "Describe the person", "What colour is the X?" |
| Prompts, multi-turn | 2–3-turn follow-up dialogues on the same image |
| Teacher output | Qwen3-VL-2B answers |
| Stored per item | the answer text, plus top-16 teacher logits on answer tokens for KD |

**Contamination rule:** every evaluation item (§6) comes from val/test splits or our own photos. It is never in training data, checked by image sha256 as in Phase 1 cell 8.

## 4. Uncertainty ("I'm not sure")

Two methods, compared by experiment:
- **U-A (no training cost):** score the student's answer by its own token probabilities on the answer span (e.g. min or mean log-prob of the noun/colour tokens). Choose the threshold on a validation split, then speak one of:
  - "It looks like a mug."
  - "I think it might be a mug, but I'm not sure."
  - "I can't tell what it is."

  It is deterministic, cheap and measurable.
- **U-B (trained hedges):** label each training item *confident* or *unsure*:
  - VQAv2: the teacher's answer agrees with ≥3 of the 10 human answers (the VQA accuracy rule) → confident; otherwise unsure.
  - VizWiz: "unanswerable" → can't tell.

  The student learns to produce the hedge text itself. Prior art: Lin et al., "Teaching models to express their uncertainty in words" (arXiv 2205.14334; uploaded to Gemini, not yet read by me, so **UNVERIFIED** details).

**Metric for both:**
- the risk–coverage curve;
- **confident-wrong rate** = wrong answers spoken without a hedge ÷ all answers.

This is the visual analogue of our 0-wrong-number rule. It cannot be exactly 0 for open-ended vision, so it needs a threshold.

## 5. Follow-ups, people, colour, Easter egg

- **Follow-ups.**
  - Keep the last image's 144 visual tokens and the dialogue in the context.
  - Context cost is small: KV cache for Qwen2.5-0.5B is 6.29 MB per 1,024 tokens at INT8 (plan §5.2).
  - Train on multi-turn teacher dialogues (§3).
  - A new image (or about 30 s idle) resets memory.
  - Whether RKLLM keeps the KV cache across turns: **UNVERIFIED** (check in E-DEV-1).
- **People-description policy** (proposed, Krishna decides):
  - **Describe:** clothing and colours, action, facial expression (smiling/frowning), position and approximate distance, number of people, broad age band (child/adult/elderly).
  - **Never infer:** name (except the Easter egg), ethnicity/caste/religion, health or disability, or anything sensitive.
  - **Gender words** ("man/woman"): Krishna wants them. They are a visual guess that can be wrong, so U-A/U-B hedging applies, and the fallback is "a person".
- **Colour depends on the camera, not just the model.**
  - The BOM (`hardware_bom.md` L119–120) says IMX708 has no RK3576 colour (rkaiq) tuning, which gives colour casts. IMX415 has official tuning.
  - Colour answers must be tested through the real camera pipeline (E-VIS-3).
  - The model can be correct on photos and wrong on the device.
- **Easter egg ("Krishna the GOAT"):**
  - Separate from the student. Face detector **YuNet (MIT)** plus face embedder **SFace (Apache-2.0)**, both from OpenCV Zoo (README licence sections checked).
  - Enrol about 10 photos of Krishna; the embedding is stored on the device only.
  - Trigger only above a strict cosine threshold, and only when a face is the main subject. Everyone else gets the normal description.
  - Krishna consents for himself; no one else is ever enrolled.
  - Size and latency on RK3576: UNVERIFIED (small CNNs; measure in Phase 2).

## 6. Evaluation (all held out, thresholds fixed before any run)

- **Public sets** (sampled, fixed seed, IDs committed):
  - VQAv2 val: 2,000 questions (VQA accuracy).
  - VizWiz val: 1,000 (accuracy plus unanswerable detection).
  - POPE: object-hallucination yes/no; licence **UNVERIFIED** (README fetched, no licence string found).
- **FRIDAY-Real-100** (new, needs Krishna):
  - 100 phone or webcam photos: 40 held objects, 30 colour questions under 3 lightings (daylight, warm indoor, LED), 30 people/outfit descriptions.
  - Ground truth written before any model sees them; rubric scoring for "object correct", "colour correct", "no invented objects".
  - Krishna declined a self-shot set on 2026-11-23 (CLAUDE.md §7). This skill cannot be validated without one, so it is decision 3.
- **Baselines on the same items:**
  - Phase 1 student;
  - **SmolVLM-256M-Instruct** (Apache-2.0; RK3576 official: encoder 768 ms, 57.73 tok/s), the off-the-shelf small VLM we must beat or honestly lose to;
  - teacher Qwen3-VL-2B (upper reference).

## 7. Training plan (stages, each a separate SHA through the 7-step protocol)

| Stage | What | Est. GPU-h | Basis |
|---|---|---|---|
| V0 | Throughput measurement (E-THR-1) and teacher fit test | 0.5 | — |
| V1 | Projector re-alignment on COCO captions (~118k images, 1 caption each) | ~2 | estimate |
| V2 | Teacher generation: ~200k (image, prompt) items, answers plus top-16 answer logits cached | ~8–12 | estimate: 2B generation on T4, ~60 answer tokens/item; UNVERIFIED until V0 |
| V3 | Student KD on cached targets (SeqKD + top-k forward KL, plus a U-B variant), 2 epochs | ~10–12 | estimate: ~50M tokens per epoch at 2–3k tok/s per T4; UNVERIFIED |
| V4 | Evaluation (E-VIS-1, E-VIS-2) | ~2 | estimate |

**Total ≈ 23–29 GPU-h ≈ one week of Kaggle quota**, if the V0 measurements confirm the throughput assumptions. Otherwise rescale before launching V2.

**Caching cost** (my calculation): top-16 logits on about 60 answer tokens is about 6 KB per item (fp16 values plus int32 ids), so about 1.2 GB for 200k items. That fits Kaggle storage.

**Interaction with other skills.** Training on visual data may degrade chat and math (forgetting). Whether to use one shared student or per-skill adapters is decided in the Q1 note.

## Recommendation

1. **Teacher:** Qwen3-VL-2B (deviation from §5.1 → Krishna).
2. **Data:** VQAv2 + VizWiz + Visual Genome (all CC-BY-4.0) plus our own teacher-generated single- and multi-turn items. Avoid GPT-4-generated sets.
3. **Uncertainty:** ship U-A first (free), test U-B as the research comparison.
4. **People:** description-only policy as in §5. Easter egg via YuNet + SFace, Krishna's face only.
5. **Measure against SmolVLM-256M on the same held-out items.** That is the honest bar for "our student".

## Experiments (pass/fail; thresholds proposed, Krishna fixes them before runs)

- **E-VIS-1 (public):** student vs Phase 1 student vs SmolVLM-256M vs teacher on VQAv2-2k, VizWiz-1k and POPE.
  - **Pass:** student ≥ SmolVLM-256M on VQAv2 and POPE F1 (95% bootstrap CI not below), and student > Phase 1 student by ≥20 points VQA accuracy.
- **E-VIS-2 (FRIDAY-Real-100):**
  - **Pass:** object correct ≥70%, colour correct ≥70% (daylight), people description has 0 sensitive inferences, **confident-wrong ≤10%**.
- **E-VIS-3 (camera colour):** same colour items shot through the target camera pipeline vs a phone.
  - **Pass:** the colour-accuracy drop is ≤10 points.
  - Runs in Phase 2; it decides whether software white balance or the IMX415 is needed.
- **E-UNC-1:** U-A vs U-B on VQAv2 and VizWiz val.
  - **Metric:** area under the risk–coverage curve.
  - **Pass for U-B:** better AURC with non-overlapping CI; otherwise ship U-A.
- **E-EGG-1:**
  - **Pass:** 0 false triggers on 500 non-Krishna faces (public face set, licence to check) and ≥90% trigger rate on 50 new photos of Krishna.

## Kaggle budget

About 25–30 GPU-h for V0–V4 (about 1 week of quota). The estimate is redone after V0 measures real throughput. E-EGG-1 and E-VIS-3 need no GPU.

## Risks

- **0.5B may be too small for good open-ended grounding.** E-VIS-1 vs SmolVLM-256M will show this honestly; a loss is a reportable result.
- **Camera colour casts** (IMX708 without rkaiq tuning).
- **Forgetting other skills** when visual training is added (Q1).
- **Licences still UNVERIFIED:** COCO images, GQA, POPE, and the face set for E-EGG-1.
- **"Confident-wrong ≤10%" is a product choice, not a law.** It must be fixed by Krishna before the run.

## Decisions needed from Krishna

1. Teacher change Qwen2-VL-2B → Qwen3-VL-2B (plan §5.1 deviation).
2. People-description policy (§5), including whether gender words are allowed (my default: allowed, hedged, fallback "a person").
3. Make FRIDAY-Real-100 (100 own photos with written ground truth). Without it, visual Q&A cannot be validated on real use.
4. Fix the pass thresholds in E-VIS-1/2 before any run.
