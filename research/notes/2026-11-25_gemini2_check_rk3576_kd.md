# 2026-11-25 — Check of Gemini answers #2: RK3576 benchmarks, KD objectives, ASR

Author: Claude Researcher. Status: evidence note, no decisions taken.

All facts below were checked by me against the primary file (downloaded 2026-11-25; sha256 given) unless marked otherwise.

## 1. Source pack status (Gemini inventory, 94 sources)

- **Still present:** two AI-generated reports, #36 "Hardware Acceleration, Model Compression…" and #64 "Technical Evaluation…". **Remove both.**
- **Still missing:** GKD (2306.13649), DistiLLM (2402.03898), ROME (2202.05262), MEMIT (2210.07229), IndicTrans2 paper (2305.16307), Qwen2.5/Qwen3 reports, Moonshine, openWakeWord, Kokoro. The step-1a URL list was apparently not added.
- **Duplicates fill slots:** about 4 copies of Minitron and about 4 of MiniLLM.
- **About 30 sources are OTHER:** GitHub issues, third-party re-uploads, a class-central page.
- **#35 is our own repo,** mislabelled "third-party".

## 2. RK3576: official RKLLM support and benchmark (answers Q9 in part)

**Sources:**
- `airockchip/rknn-llm` README.md, sha256 b1f258d9…
- `airockchip/rknn-llm` benchmark.md, sha256 b328808a…

Gemini said "NOT IN SOURCES" for the benchmark, but it exists in the official repo.

**Supported models (README "Support Models"):**
- Qwen2/Qwen2.5/Qwen3/Qwen3.5, Qwen2-VL/Qwen3-VL, DeepSeek-R1-Distill, SmolVLM/SmolLM3, InternVL2/3-1B, Gemma2/3/3n/4, and others.
- Platforms: RK3588, **RK3576**, RK3562, RV1126B.
- Our student's architecture (Qwen2/2.5) is on the official list.

**RK3576 text LLMs** (benchmark.md: "collected based on the maximum CPU and NPU frequencies"; seqlen 128, 64 new tokens):

| Model | Dtype | TTFT (ms) | Tokens/s | Memory (MB) |
|---|---|---|---|---|
| Qwen2 0.5B | w4a16 | 342.37 | 32.56 | 443.44 |
| Qwen2 0.5B | w8a8 | 344.27 | 21.73 | 678.43 |
| Qwen3 0.6B | w4a16 | 468.61 | 24.85 | 512.71 |
| Qwen3.5 0.8B | w4a16 | 1369.31 | 18.79 | 689.50 |
| TinyLLAMA 1.1B | w4a16 | 543.68 | 19.71 | 601.09 |
| InternLM2 1.8B | w4a16 | 765.92 | 13.55 | 975.04 |
| Qwen3-VL 2B (LLM part) | w4a16 | 802.94 | 12.68 | 1058.56 |

Qwen2.5-1.5B has no RK3576 row (only RK3588 w8a8: 16.69 tok/s, 1689 MB).

**RK3576 multimodal** (vision encoder on RKNN, FP16, all NPU cores):

| Model | Image encoder | Prefill | Decode |
|---|---|---|---|
| Qwen2-VL-2B | 3.55 s (392²) | 1234.9 ms (len 196) | 14.57 tok/s |
| Qwen3-VL-2B | 1.61 s (448²) | 1587 ms (len 196) | 10.36 tok/s |
| SmolVLM-256M | 768 ms (512²) | 180 ms (len 128) | 57.73 tok/s |
| Qwen3.5-0.8B | 815 ms (448²) | 3.4 s (len 216) | 15.4 tok/s |
| Gemma4-E2B | 1.09 s (448²) | 965 ms (len 118) | 9.29 tok/s |

**Consequences (my analysis):**
1. **Decode speed is not the bottleneck.** A 0.5B model at about 33 tok/s is far faster than speech. plan.md §5.2's 25 tok/s assumption is consistent with the official 32.56.
2. **The vision encoder plus prefill decide time-to-first-word.**
   - There is no official number for our SigLIP-B/16-384 (576 patches).
   - SmolVLM's encoder takes 768 ms for 512² (1024 patches). Scaling linearly by patch count gives roughly 0.4–0.45 s for ours.
   - Prefill of about 200 tokens on 0.5B scales to about 0.5 s from the 342 ms at 128 tokens.
   - That gives about 0.9–1.0 s before the first token, plus TTS. The 1.2 s target (plan §10) is tight but plausible.
   - The whole of this estimate is UNVERIFIED (linear scaling ignores attention and NPU effects).
3. **Memory is about 2× the weight file.** RKLLM runtime memory for 0.5B w4a16 is 443 MB, whereas plan.md §5.2 counts only the 209 MB weight file. A 1.5–2B-class model needs about 1 GB.
   - With the ≤1.5–2 GB budget for all AI (02_constraints), shared with STT, TTS, OCR and the vision encoder, **the on-device student should stay at about 0.5–0.6B.**
   - "Train big" therefore means a big *training-time* model that is pruned or distilled down to about 0.5B. A big deployed model is out.
4. **The numbers are at maximum CPU/NPU frequency.** Our PCM thermal duty cycle (plan §7) may cap the frequency, so real figures will be lower. They must be measured on our module.
5. **Open: can RKLLM convert our customised student?**
   - The questions are the pruned 64k vocabulary and image embeddings coming from our own SigLIP + unshuffle + projector on RKNN.
   - The official multimodal demo does pass RKNN vision output into RKLLM, so the mechanism exists. Whether it accepts our layout is UNVERIFIED.
   - **This can be tested before buying hardware:** RKLLM-Toolkit conversion runs on an x86 Linux PC (experiment E-DEV-1).

## 3. KD objectives: MiniLLM Table 1 (primary, arXiv 2306.08543 HTML)

I extracted the table myself. **Gemini's table has 3 wrong numbers.** In the 120M UnNI column the correct values are KD 22.0 (Gemini 24.8), SeqKD 18.8 (21.0) and MiniLLM 26.6 (30.1). Gemini also left out the **SFT w/o KD baseline**, which changes the conclusion.

DollyEval GPT-4 score (selected rows, students ≤1.5B):

| Student (teacher) | SFT w/o KD | KD (forward, word-level) | SeqKD | MiniLLM (reverse KL, on-policy) |
|---|---|---|---|---|
| GPT-2 120M (1.5B) | 38.6 | 40.3 | 41.2 | 44.7 |
| GPT-2 340M (1.5B) | 51.9 | 51.6 | 50.5 | 52.2 |
| GPT-2 760M (1.5B) | 50.7 | 53.4 | 52.0 | 54.7 |
| OPT 1.3B (13B) | 52.6 | 52.7 | 51.0 | 60.7 |

**What this does and does not tell us:**
- At 340M and 1.3B, forward word-level KD and SeqKD are **no better than plain SFT** on this benchmark. MiniLLM's gain is large at 1.3B (+8 points) and small at 340M.
- MiniLLM's "KD" mixes the distillation loss with the LM loss on ground truth over the full vocabulary. Ours is a renormalised top-64 forward KL. These are not the same method.
- **MiniLLM needs student sampling plus policy-gradient updates.** That has a compute cost on T4s which this note does not estimate (UNVERIFIED; must be measured).
- Their tasks are instruction-following with a GPT-4 judge, not our skills. **Paper result ≠ our result;** it becomes experiment E-KD-1.

## 4. Speech and translation

- **Qwen3-ASR-0.6B** (official card, `Qwen/Qwen3-ASR-0.6B` README L39) lists 30 languages. **Hindi is the only Indian language.** Tamil, Bengali, Telugu, Marathi, Gujarati, Kannada and Malayalam are not supported.
  - Indian-language speech input therefore needs another ASR. Candidates to research: AI4Bharat IndicConformer / IndicWhisper, sherpa-onnx models (UNVERIFIED).
- **IndicTrans2 en-indic dist-200M:**
  - The card metadata says 0.3B params, F32 (Gemini, not checked by me). Both directions need 2 models.
  - BPCC data licence and chrF++ are not in the card. The paper is not in the notebook.

## 5. Model editing

- The ROME and MEMIT primaries are still missing.
- The only evidence is CACHE-UK (arXiv 2607.28292, after my knowledge cutoff, UNVERIFIED). Using their own re-implementations of ROME/MEMIT on 4-bit OpenLLaMA-3B, they report edit success about 100% but paraphrase success of only 12–15%.
- Single, unreplicated evidence. It suggests a hypothesis for Q7: **edit in fp16, then quantise**, rather than editing the INT4 model. That is a candidate experiment, not a finding.

## Recommendation

1. **Student size stays about 0.5–0.6B** (RKLLM memory 443–513 MB at that size). Keep the Qwen2.5-0.5B family; it is officially RKLLM-supported. Qwen3-0.6B is also supported but is 27% slower per token on RK3576 (24.85 vs 32.56 tok/s); see decision 2.
2. **Run E-DEV-1 early.** It is cheap and catches a showstopper (our custom VLM not convertible) before any further training.
3. **For the KD method, do not adopt any paper's winner.** Compare at equal GPU-hours on one skill (E-KD-1).
4. **Indian-language ASR is a new open item.** Qwen3-ASR covers only Hindi.

## Experiments (pass/fail)

- **E-DEV-1 (x86 Linux, no GPU, no hardware purchase):** convert the Phase 1 student (64k vocab, INT4 target w4a16) with RKLLM-Toolkit for target RK3576. Convert SigLIP-B/16-384 + unshuffle + projector with RKNN-Toolkit2.
  - **Pass** = both conversions succeed and the RKLLM model accepts external embeddings in the toolkit's simulator or API.
  - **Fail** = any unsupported op or vocabulary, which is reported with the exact error.
- **E-DEV-2 (on hardware, Phase 2):** measure TTFT, tok/s and memory of our converted student at our thermal-limited frequency, plus SigLIP encoder latency.
  - **Pass:** encoder + prefill ≤ 1.0 s and memory ≤ 600 MB for the LLM part.
  - Thresholds proposed, to be fixed by Krishna before the run.
- **E-KD-1 (Kaggle):** on one skill with an automatic metric, at equal GPU-hours, compare:
  - (a) SFT on teacher-generated text (SeqKD);
  - (b) our top-64 forward KL;
  - (c) reverse-KL / on-policy.
  - **Pass** for choosing (b) or (c) over (a) = at least +2 points on the held-out metric with non-overlapping 95% bootstrap CIs. Otherwise use (a), the cheapest.
  - Exact skill and metric to be set in the Q1 note.

## Kaggle budget

- E-DEV-1: 0 GPU-h (CPU).
- E-KD-1: estimate given in the Q1 note (depends on the tokens/s measured in E-THR-1).

## Risks

- **The benchmark is at maximum frequency;** thermal throttling lowers real throughput.
- **RKLLM may not support our pruned vocabulary or external image embeddings.** E-DEV-1 tests this.
- **Gemini's tables can contain transcription errors** (3 found here). Every number we rely on must be re-checked against the primary source.

## Decisions needed from Krishna

1. Clean the notebook: remove #36 and #64 and the duplicates, then add the step-1a URLs (GKD, DistiLLM, ROME, MEMIT, IndicTrans2 paper, Qwen reports).
2. Should the student stay Qwen2.5-0.5B (fastest on RK3576: 32.56 tok/s) or move to Qwen3-0.6B (24.85 tok/s, newer)? My default is to stay, unless E-KD results show a capability gap.
3. Approve E-DEV-1 as the next implementation task (CPU only, no purchase).
