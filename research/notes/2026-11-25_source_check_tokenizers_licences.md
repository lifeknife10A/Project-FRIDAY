# 2026-11-25 — Source check: Gemini answers #1, tokenizers, licences

Author: Claude Researcher. Status: evidence note, no decisions taken.

## 1. Gemini source pack: what was actually uploaded

Gemini's title table shows that the uploaded pack is **not** the list in `04_sources.md`.

**Missing from the pack (needed):**
- Hinton KD, MiniLLM, GKD, DistiLLM;
- Qwen2.5 and Qwen3 technical reports, Qwen3 text model cards;
- DeepSeek-R1 paper;
- SigLIP, LLaVA, MobileVLM, SmolVLM;
- ROME, MEMIT;
- IndicTrans2 and NLLB papers;
- Whisper, Moonshine, openWakeWord, Kokoro;
- official airockchip RKLLM / RKNN-Toolkit2 docs;
- our `kaggle_runs/7571e39/README.md`.

**Problems in the pack:**
- **Several IDs map to two different titles** ("also indexed as …"). Examples: 2411.14055, 2404.02657, 2603.25562, 2604.00223, 2604.00626, 2609.39884. That suggests NotebookLM merged or mis-parsed sources.
  - From memory, these first titles look right: 2408.11796 (Minitron in practice), 2411.14055 (DRPruning, distributionally robust), 2404.02657 (Wu et al., rethinking KL), 2402.12842 (PromptKD). Their "also indexed as" second titles are wrong.
  - IDs dated after June 2026 (2606.x, 2609.x) I cannot verify: UNVERIFIED. Krishna should open each one.
- **One source is a "Technical Evaluation of Open Language Model Tokenization…" document.** It looks like a generated research report, not a primary source. Several of Gemini's answers quote it, including a MiniLLM quote, even though the MiniLLM paper itself was not uploaded. **Remove it from the notebook.** Answers must cite only primary sources.
- **Many quotes come from third-party re-uploads,** not the official model cards: litert-community, unsloth, marcusmi4n, mobilint, domperidom. These are not acceptable sources for licences or architecture facts.
- **Gemini's Q5 synthesis overreaches its quotes.** "RKL/GKD consistently outperform SeqKD on sub-1B students" and "+19.8% stability gain" are not supported by the sentences it quoted. Treat Q5 as UNANSWERED until MiniLLM, GKD and DistiLLM themselves are uploaded.

## 2. Tokenizer compatibility: measured by me (primary evidence)

**Method:**
- Downloaded `tokenizer.json` from each official Hugging Face repo (branch `main`, 2026-11-25).
- Compared the BPE vocab (token → id), the merges list, the pre-tokenizer and the normalizer against Qwen2.5-0.5B.
- Then diffed the added/special tokens by id.
- Script output is reproduced below; sha256 of each file is recorded.

**Result:**

| Model | BPE vocab | Same token→id as Qwen2.5 | Same merges | Special tokens vs Qwen2.5 | tokenizer.json sha256 (first 12) |
|---|---|---|---|---|---|
| Qwen2.5-0.5B (student base) | 151,643 | — | — | 22 added (ids 151643–151664) | c0382117ea32 |
| Qwen2.5-1.5B-Instruct | 151,643 | yes | yes | identical | c0382117ea32 |
| Qwen2.5-VL-7B-Instruct | 151,643 | yes | yes | identical | c0382117ea32 |
| Qwen2-VL-2B-Instruct (Phase 1 teacher) | 151,643 | yes | yes | lacks ids 151655–151664 (image/video pad, tool_call, fim) | cb63a0a23eef |
| Qwen3-0.6B / Qwen3-1.7B | 151,643 | yes | yes | adds 151665–151668 (`<tool_response>`, `</tool_response>`, `<think>`, `</think>`) | aeb13307a71a |
| Qwen3-VL-2B-Instruct | 151,643 | yes | yes | same 4 additions as Qwen3 | a5d85b6dcc53 |
| DeepSeek-R1-Distill-Qwen-1.5B / 7B | 151,643 | yes | yes | **ids 151643–151649 RE-ASSIGNED:** 151643 `<｜end▁of▁sentence｜>`, 151644 `<｜User｜>`, 151645 `<｜Assistant｜>`, 151646 `<｜begin▁of▁sentence｜>`, 151647 `<|EOT|>`, 151648 `<think>`, 151649 `</think>` | 88145e3c3249 |

**Consequences:**
1. **Logit KD is tokenizer-compatible for every teacher in the table.** On ordinary text, all of them use the same 151,643 BPE ids as our student. This answers Gemini's "NOT IN SOURCES" for Qwen3 and replaces its weak "config vocab_size = 151936" argument. `vocab_size` is the padded embedding size and does not prove the tokenizers match.
2. **Special tokens must be remapped by string, never by id.**
   - For example, DeepSeek id 151648 means `<think>`, but in Qwen2.5 the same id means `<|box_start|>`.
   - Rule for any KD pipeline:
     - exclude special-token positions from the KD loss, or map them through a string table;
     - build each teacher's prompt with that teacher's own chat template.
   - This is a concrete bug risk for agy and must be a unit test.
3. **Our pruned 64k student vocabulary is a subset of these 151,643 ids.** The top-64 KD over Ω₆₄ ⊆ V_S (plan.md §5.1) therefore carries over unchanged to all these teachers.

## 3. Licences: official Hugging Face API tags (primary), 2026-11-25

| Model / data | Licence tag | Notes |
|---|---|---|
| Qwen2.5-0.5B, Qwen2.5-1.5B-Instruct | apache-2.0 | |
| **Qwen2.5-3B-Instruct** | **other: qwen-research** | Non-commercial research licence (terms not read yet). Matters if "train big" starts from 3B. |
| Qwen2-VL-2B-Instruct | apache-2.0 | |
| **Qwen2.5-VL-3B-Instruct** | **qwen-research** | As above. |
| Qwen2.5-VL-7B-Instruct | apache-2.0 | |
| Qwen3-0.6B, Qwen3-1.7B, Qwen3-4B | apache-2.0 | |
| Qwen3-VL-2B-Instruct | apache-2.0 | Candidate newer VLM teacher, same tokenizer. |
| DeepSeek-R1-Distill-Qwen-1.5B, -7B | mit | Card also says the Qwen2.5 base is Apache-2.0. |
| IndicTrans2 en-indic / indic-en dist-200M | mit | Gated (auto-approve). |
| NLLB-200-distilled-600M | **cc-by-nc-4.0** | Non-commercial. |
| Qwen3-ASR-0.6B | apache-2.0 | Candidate multilingual STT (languages: to check). |
| SmolVLM-256M-Instruct | apache-2.0 | |
| google/siglip-base-patch16-384 | apache-2.0 | |

The licence tag is the repo metadata, not the full licence text. Before any model is adopted, the full LICENSE file must be read for output-use clauses. I have not read the qwen-research text: UNVERIFIED.

## 4. What Gemini's answers do establish (with my caveats)

- **RK3576 / RKLLM.**
  - There is only community evidence:
    - a third-party Granite-3B RKLLM build (W4A16, group size 32, 16k context);
    - a third-party "rk3576-qwen3" container with tags 0.6b / 1.7b / 4b w4a16.
  - This suggests Qwen3-family models convert to RKLLM on RK3576. It is not official, and there are no tokens/s or memory numbers.
  - **Q9 remains open.** We need the airockchip supported-model list plus a measured benchmark.
- **Minitron / Sheared-LLaMA.**
  - The smallest pruned targets reported are 4B (Minitron) and 1.3B (Sheared-LLaMA, about 50B tokens).
  - **No evidence exists in the pack for prune + distil at the 0.5B scale.** That makes our "train big, then prune" a genuinely untested regime: a valid research question, but with no prior result to lean on.
- **Kaggle scale gap (my estimate, UNVERIFIED until measured).**
  - Training a 0.5B student costs about 6 × 0.5e9 = 3e9 FLOP per token. A 1.5B teacher's forward pass adds about 3e9 more.
  - At a realistic ~15 TFLOPS per T4 in fp16, that is roughly 2–3k tokens/s per GPU.
  - 30 GPU-h per week then gives about 0.2–0.3B tokens per week.
  - That is about 200× less than Sheared-LLaMA's 50B tokens. Any pruning study must therefore be skill-data-scale (about 10⁸ tokens), compared at equal GPU-hours. It cannot reproduce Minitron-scale results.
  - First Kaggle measurement needed: tokens/s per T4 for our student and teacher setup.

## Recommendation

- Treat tokenizer compatibility as **solved**: same BPE across all Qwen2/2.5/3, Qwen-VL and R1-Distill teachers, with string-based special-token handling.
- Prefer Apache/MIT teachers. Avoid qwen-research models (Qwen2.5-3B, Qwen2.5-VL-3B) unless Krishna accepts research-only terms.
- Fix the Gemini source pack before the next round of questions.

## Experiments (pass/fail)

- **E-TOK-1:** a unit test in the KD pipeline. For each teacher, 1,000 random strings in English, Hindi, Tamil, Bengali and digits/units, plus each teacher's chat-template strings.
  - Check that the non-special token ids from the teacher's and student's tokenizers are identical.
  - Check that every special token is either masked out or string-mapped.
  - **Pass** = 0 mismatches.
  - Cost: CPU only.
- **E-THR-1** (with the first Kaggle KD run): measure training tokens/s per T4 for the 0.5B student with a cached teacher and with an online teacher.
  - This is not pass/fail. It replaces the estimate above, and every later budget depends on it.

## Kaggle budget

- This note: 0 GPU-h.
- E-THR-1 adds about 0.2 GPU-h to the first approved run.

## Risks

- **Special-token id collision** (DeepSeek ids 151643–151649) silently corrupts KD targets if ids are used directly.
- **Source contamination:** the AI-generated "Technical Evaluation" document in NotebookLM.
- **Unverifiable recent arXiv IDs.**

## Decisions needed from Krishna

1. Remove the generated "Technical Evaluation…" document and the third-party model-card copies from Gemini Notebook. Upload the missing primary sources (list in §1).
2. Are qwen-research-licensed models (Qwen2.5-3B, Qwen2.5-VL-3B) acceptable for a thesis-only research track? My default is no: use Apache/MIT models instead (Qwen3-1.7B/4B, Qwen3-VL-2B, Qwen2.5-VL-7B in 4-bit).
