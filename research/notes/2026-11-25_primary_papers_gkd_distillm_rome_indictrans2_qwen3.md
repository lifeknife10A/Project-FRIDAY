# 2026-11-25 — Primary-paper answers: GKD, DistiLLM, ROME/MEMIT, IndicTrans2, Qwen3

Author: Claude Researcher. Status: evidence note, no decisions taken.

**Why this note exists.** Gemini answered "NOT IN SOURCES" to all four questions because these papers are still not in the notebook. I downloaded the PDFs from arXiv (2026-11-25), checked each title against its ID, and extracted the answers myself with `pdftotext`. The titles match:

| arXiv ID | Paper |
|---|---|
| 2306.13649 | On-Policy Distillation of LMs (GKD) |
| 2402.03898 | DistiLLM |
| 2202.05262 | ROME |
| 2210.07229 | MEMIT |
| 2305.16307 | IndicTrans2 |
| 2505.09388 | Qwen3 |
| 2412.15115 | Qwen2.5 |

Numbers read from figures (not tables) are marked "(fig.)": they come from heatmap cell labels and may be less exact.

## 1. GKD (Agarwal et al., ICLR 2024)

- **Setup.**
  - Teacher: supervised-fine-tuned T5-XL (~3B).
  - Students: T5-small (77M), T5-base (250M), T5-large (800M).
  - Tasks: XSum (summarisation), WMT (translation), GSM8K (math, "4-shot-CoT + Calculator").
  - Quote: "We use supervised fine-tuned T5-XL (∼3B params) as the teacher. For students, we use T5-small (77M params), T5-base (250M params), and T5-large (800M params)" (§4).
- **Headline.**
  - "averaged across T5 student models of different sizes, we see relative gains of 2.1× on summarization, 1.7× on machine translation, and 1.9× on arithmetic reasoning tasks, compared to the performance improvements achieved with baseline KD methods" (§1).
  - The baselines are supervised FT, supervised KD and SeqKD.
- **What matters more, the divergence or on-policy data?**
  - Fig. 7 (fig.), T5-XL → T5-base on GSM8K, gives the accuracy gain in points:

  | Student-data fraction λ | Forward KL | Reverse KL |
  |---|---|---|
  | 0% (off-policy) | +4.7 | +5.7 |
  | 100% (on-policy) | +8.8 | +8.0 |

  - Fig. 8 caption: "As we increase fraction of student-generated data beyond 25%, performance typically improves."
  - **Reading:** at these sizes, on-policy sampling matters more than the choice of KL direction.
- **Relevant to our math design.** GKD's GSM8K evaluation uses a calculator: the model writes arithmetic and a tool computes it. That is the same pattern as our safety rule.
- **Compute per run:** not stated in the text I extracted. UNVERIFIED.

## 2. DistiLLM (Ko et al., ICML 2024)

- **Setup.**
  - Pairs: GPT-2 XL (1.5B) → GPT-2 (0.1B); OPT-2.7B → OPT-1.3B; OpenLLaMA2-7B → OpenLLaMA2-3B.
  - Method: skew KL / skew reverse KL plus an adaptive off-policy replay of student-generated outputs.
- **Compute, which is the key fact for Kaggle.**
  - "DistiLLM requires only 1.6× the training time of naïve KD, whereas other methods take 3 ∼ 7×" (§4.1, Fig. 5(d); measured on four A100s).
  - "other methods" includes MiniLLM and GKD.
  - Also from the abstract/intro: "achieving up to 4.3× speedup compared to recent KD techniques".
- **Main per-task scores** are in plotted figures (Fig. 5), not text. Not extracted.

**Consequence.** Any method that samples from the student during training costs about 3–7× a plain KD step (DistiLLM about 1.6×). This also means the teacher must stay live in GPU memory to score student samples. Our Phase 1 trick of caching teacher outputs then no longer works. On 2×T4, the student goes on one GPU and the teacher on the other; this needs a fp16 teacher of 4B or smaller (UNVERIFIED fit).

## 3. ROME (Meng et al., NeurIPS 2022) and MEMIT (Meng et al., ICLR 2023)

- **Smallest model edited: GPT-2 XL (1.5B) in ROME.** MEMIT used only GPT-J (6B) and GPT-NeoX (20B) ("We run experiments on two autoregressive LLMs: GPT-J (6B) and GPT-NeoX (20B)", MEMIT §5).
- **ROME on GPT-2 XL**, CounterFact, Table 4:

  | | Efficacy ES | Paraphrase PS | Neighbourhood NS | Score S |
  |---|---|---|---|---|
  | Unedited GPT-2 XL | 22.2 | 24.7 | 78.1 | 30.5 |
  | ROME | 100.0 | 96.4 | 75.4 | 89.2 |

- **MEMIT, 10,000 edits at once on GPT-J**, CounterFact, Table 2:

  | | ES | PS | NS | S |
  |---|---|---|---|---|
  | MEMIT | 98.9 | 88.6 | 73.7 | 85.8 |
  | ROME at 10,000 edits | 50.2 | 50.4 | 50.2 | 50.3 |

- **How many edits before quality drops.** "ROME performs well up to n = 10 but degrades starting at n = 32 … MEMIT performs best at large n" (MEMIT §5.2.2). MEMIT was tested up to 10,000 edits.
- **Edits on quantised models:** none in either paper.

**Consequence for Q7.** Editing a model under 1B, and editing an INT4 model, are both outside what these papers tested. A clean experiment is therefore novel either way:
- edit our fp16 student, then quantise;
- versus edit after quantisation (dequantise → edit → requantise);
- measure ES, PS and NS as defined above.

## 4. IndicTrans2 (Gala et al., TMLR 2023)

- **Distilled model.** "We distill our IndicTrans2 (1.1B parameters, 12Gb size) models into smaller, efficient counterparts called IndicTrans2-Dist (211M parameters, 2Gb size)" (§7.6).
  - The HF card metadata says "0.3B params" (Gemini). The discrepancy is unexplained, so the 211M figure is the one to trust.
  - One model per direction (en→indic and indic→en), so about 2 × 211M.
- **Method:** word-level KD on about 110M sentence pairs.
- **22 languages** (Table 22 codes): asm, ben, brx, doi, gom, guj, hin, kan, kas, mai, mal, mar, mni, npi, ory, pan, san, sat, snd, tam, tel, urd.
- **chrF++ of the distilled model on IN22-Gen** (Table 22, column "Dist"):

  | Direction | hin | ben | tam | Average (22) |
  |---|---|---|---|---|
  | En → Indic | 56.4 | 51.5 | 49.3 | 48.1 |
  | Indic → En | 63.7 | 63.1 | 58.4 | 61.8 |

  - FLORES numbers are in appendix Tables 52 and 53 (not extracted).
- **Licences** (official IndicTrans2 GitHub README, LICENSE table):
  - models: MIT (HF cards);
  - mined and back-translation corpora: CC0;
  - "Newly Added Seed Corpora (BPCC-H-Wiki & BPCC-H-Daily)" and "IN-22 test set": **CC-BY-4.0** (attribution required).

**Consequence for Q3.** A dedicated 2×211M translator is a strong, permissively licensed baseline. Any "our student translates" claim must be compared against it on IN22-Gen chrF++.

## 5. Qwen2.5 / Qwen3 and Indian languages

- **Qwen3 language coverage.** "Qwen3 expands multilingual support from 29 to 119 languages" (abstract).
- **Indian languages in Qwen3's Belebele evaluation** (Table 36):
  - Indo-Aryan: hin, ben, guj, mar, pan, ory, asm, urd, npi, snd;
  - Dravidian: mal, kan, tel, tam.
- **Belebele scores** (Table 37; 4-way multiple-choice reading comprehension, so chance is 25%; there is **no 0.5B/0.6B row**):

  | Model | Indo-European | Dravidian |
  |---|---|---|
  | Qwen2.5-1.5B-Instruct | 41.5 | **28.6** |
  | Qwen3-1.7B (non-thinking) | 58.8 | **43.3** |
  | Qwen2.5-3B-Instruct | 58.0 | 36.9 |
  | Qwen3-4B (non-thinking) | 76.0 | 65.5 |

- **Small models** (Table 20, non-thinking):

  | Benchmark | Qwen3-0.6B | Qwen2.5-1.5B-Instruct |
  |---|---|---|
  | MMMLU (14 languages) | 37.1 | 40.4 |
  | INCLUDE | 34.4 | 33.1 |
  | MATH-500 | 55.2 | 55.0 |

  Qwen2.5-0.5B is not in the Qwen3 tables.
- **Qwen2.5 report:** "29 languages". My grep found no mention of Hindi or other Indian languages: UNVERIFIED which are included.
- **Prior art that matters for novelty.** Qwen3's small models are themselves produced by distillation (§4.5, "Strong-to-Weak Distillation"):
  - "(1) Off-policy Distillation … (2) On-policy Distillation: … the student model is then fine-tuned by aligning its logits with those of a teacher model (Qwen3-32B or Qwen3-235B-A22B) to minimize the KL divergence."
  - **"We distilled a small Qwen" is therefore not novel in itself.** Our contribution has to be:
    - multi-teacher, multi-skill distillation under an on-device budget;
    - a safety-verified numeric path;
    - sub-1B prune + distil under about 30 GPU-h/week;
    - editing a sub-1B INT4 model.

**Consequence for the student choice.**
- At 1.5–1.7B, Qwen2.5 is near chance on Dravidian reading comprehension (28.6 vs 25 chance); Qwen3 is far better (43.3).
- If that gap holds at 0.5–0.6B (UNVERIFIED; no row exists), Qwen2.5-0.5B would be a poor base for Tamil, Telugu, Kannada and Malayalam. This supports Krishna's idea of starting from **Qwen3-0.6B and pruning it down** to Qwen2.5-0.5B's RK3576 cost.
- It needs one cheap measurement: E-LANG-1.

## Recommendation

1. **Run E-LANG-1 before choosing the student.** It is cheap and decides Qwen2.5-0.5B (faster on RK3576) vs Qwen3-0.6B (likely much better at Indian languages).
2. **Plan KD as off-policy first, on-policy as an upgrade.** On-policy costs 3–7× per step (DistiLLM measurement) and needs a live teacher on the second T4. E-KD-1 must include an on-policy arm because GKD shows the λ effect is larger than the divergence effect.
3. **Q7 editing is in open territory below 1.5B and on INT4.** Design it around ES/PS/NS from ROME, at 1, 10, 100 and 1,000 edits (MEMIT vs ROME).
4. **IndicTrans2-Dist (2×211M, MIT) is the translation baseline** to beat or to adopt.

## Experiments (pass/fail)

- **E-LANG-1** (Kaggle 1 T4 or Mac MPS; no training):
  - Models: Qwen2.5-0.5B and Qwen3-0.6B, both base and instruct.
  - Benchmark: Belebele, zero-shot, for hin, ben, tam, tel, mar, guj, kan, mal plus eng.
  - Measure: accuracy with 95% bootstrap CI.
  - **Decision rule (proposed, Krishna to fix):** if Qwen3-0.6B beats Qwen2.5-0.5B by ≥10 points averaged over the 8 Indian languages, the student base for the language skills is Qwen3-0.6B (pruned per E-PRUNE-1). Otherwise keep Qwen2.5-0.5B.
  - Belebele licence: to check before use (UNVERIFIED).
- **E-EDIT-0** (setup check for Q7): reproduce ROME on GPT-2 XL with the authors' code and CounterFact (100 edits).
  - **Pass:** ES/PS/NS within 5 points of Table 4.
  - This proves our harness before we edit our own student.

## Kaggle budget

- E-LANG-1: ≤1 GPU-h (inference only, 2 small models × 9 languages × 900 questions; my estimate).
- E-EDIT-0: about 1–2 GPU-h; GPT-2 XL fits one T4 in fp16 (my estimate).

## Risks

- **No 0.5/0.6B multilingual numbers exist in either report.** The Qwen2.5-vs-Qwen3 gap at our size is an inference from 1.5B/1.7B rows; E-LANG-1 measures it.
- **On-policy KD may not fit the weekly quota** at useful scale.
- **Figure-derived GKD numbers may be slightly off;** use them only for direction, not values.

## Decisions needed from Krishna

1. Approve E-LANG-1, which decides the student base for the Indian-language skills.
2. Accept the reframed thesis contribution (§5). "Distilling a small Qwen" alone is not novel, since Qwen3 already does it.
3. Translation: is IndicTrans2-Dist acceptable as the baseline (MIT models, CC-BY-4.0 seed data and test set)?
