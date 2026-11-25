# 2026-11-25 — Language scope: English, Hindi, Marathi (Krishna's decision)

Author: Claude Researcher. Krishna stated the language scope on 2026-11-25: **English, Hindi, Marathi only.**

This settles 01_requirements R3 ("language list to be decided"). Krishna should copy it into plan.md §11.

## What this changes, per component

| Component | en | hi | mr | Evidence / status |
|---|---|---|---|---|
| **Script** | Latin | Devanagari | Devanagari | Hindi and Marathi share one script, so there is one OCR recogniser and one vocabulary block. |
| **Student vocab (64k pruned)** | yes | yes | yes | Phase 1 pruning kept byte tokens and Devanagari (plan1_context / notebook cell 3). The Tamil/Bengali vocabulary concern goes away. |
| **LLM base** | yes | ? | ? | Qwen3 Belebele (Table 36) includes hin_Deva and mar_Deva. No 0.5/0.6B scores exist; E-LANG-1 is now 3 languages. |
| **Translation** | — | yes | yes | IndicTrans2-Dist, IN22-Gen chrF++ (Table 22, Dist column): en→hi 56.4, en→mr 50.4, hi→en 63.7, mr→en 63.2. Models MIT. |
| **OCR (Devanagari)** | yes | ? | ? | rapidocr 3.10 default models are Chinese/English. A PP-OCR Devanagari recognition model exists in PaddleOCR (UNVERIFIED for rapidocr 3.10). Needs a Hindi/Marathi label eval set. |
| **STT** | yes | yes | **gap** | Qwen3-ASR-0.6B: en + hi, **no Marathi** (official card). Candidates: AI4Bharat IndicConformer-600M-multilingual (MIT, gated; Marathi coverage and RK3576 feasibility UNVERIFIED); Whisper (Apache-2.0) lists Marathi (quality UNVERIFIED). |
| **TTS** | yes | yes (weak?) | **gap** | Kokoro-82M VOICES.md: Hindi has 2F + 2M voices, with training data listed only as "H hours" (small); **no Marathi**. Options: MMS-TTS mar/hin are **CC-BY-NC-4.0** (non-commercial); AI4Bharat Indic-Parler-TTS is Apache-2.0 (gated; size and RK3576 feasibility UNVERIFIED). |

## New risks created by adding Marathi

- **Marathi speech in (STT) and speech out (TTS) are the weakest links,** not the LLM. Both need a model that fits the RK3576 next to everything else.
- **The memory budget gets tighter.** A separate Marathi STT and TTS could each cost hundreds of MB.

## Recommendation

1. **Keep the scope at en/hi/mr.** It removes about 19 languages of data, evaluation and vocabulary risk.
2. **Run E-LANG-1 on hin, mar and eng only.**
3. **Open two new research items under Q3/Q8:**
   - Marathi STT;
   - Marathi (and better Hindi) TTS.

   Each needs licence, size, RK3576 conversion and a small quality test.

## Experiments (pass/fail)

- **E-LANG-1 (updated):** Belebele zero-shot, hin_Deva, mar_Deva and eng_Latn; Qwen2.5-0.5B vs Qwen3-0.6B (base and instruct).
  - **Rule (proposed):** if Qwen3-0.6B beats Qwen2.5-0.5B by ≥10 points averaged over hi + mr, the language-skill student base is Qwen3-0.6B (pruned per E-PRUNE-1).
- **E-OCR-DEVA-1:** a Devanagari OCR check.
  - Data: 40 rendered + 20 photographed Hindi/Marathi labels (signs, medicine strips).
  - Measure: CER of the best available PP-OCR Devanagari model.
  - **Pass:** CER ≤ 5% on renders, with the same 0-wrong-number rule through the extractive reader.

## Kaggle budget

- E-LANG-1: ≤1 GPU-h (smaller than before: 3 languages).
- E-OCR-DEVA-1: CPU only.

## Risks

- **No small on-device Marathi TTS/STT is verified yet.**
- **Kokoro's Hindi voices have little training data;** quality is untested.

## Decisions needed from Krishna

1. Confirm that the language scope goes into plan.md §11 as APPROVED.
2. Is a non-commercial licence (MMS-TTS, CC-BY-NC) acceptable for a thesis-only Marathi TTS fallback? My default is no: prefer Apache/MIT.
