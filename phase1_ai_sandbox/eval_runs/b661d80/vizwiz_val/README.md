# VizWiz-VQA Validation Held-Out Benchmark Evaluation (Auditor Item C9)

## Provenance
- **Git Commit SHA**: `b661d8095af548cbe4ac9cae4a7ad3d336682d70` (Short: `b661d80`)
- **Dirty Tree**: `True` (Diff Hash: `2760b13443e9a6860dce393526a1940639c0ac25545e65b456d07e2616577fa5`)
- **Dataset Source**: `https://vizwiz.cs.colorado.edu/VizWiz_final/vqa_data/Annotations.zip`
- **Annotations SHA256**: `dbc32fc1e3f1b1039aea906030d569d6c238b4ddb2eea5e3453a6a565c829ec9`
- **Images Source**: `https://vizwiz.cs.colorado.edu/VizWiz_final/images/val.zip`
- **License**: `Creative Commons Attribution 4.0 International License (CC BY 4.0)`

### Official License Verbatim
> Creative Commons Attribution 4.0 International License (CC BY 4.0)
> VizWiz dataset is made publicly available for research under the Creative Commons Attribution 4.0 International License (CC BY 4.0).

## Methodology & Protocol
- **Zero Training/Tuning on VizWiz**: This evaluation is strictly zero-shot held-out inference on real-world photos taken by blind users.
- **Rule-Based Subset Selection (Frozen Before Evaluation)**:
  - Total val set annotations: 4319
  - Total questions matching text-reading criteria: 683
  - Deterministically sampled subset size: 500 (Seed: 42)
  - Answerable: 289, Unanswerable: 211
- **Inference Pipeline**: `run_ocr` (PP-OCRv6 via RapidOCR 3.10.0) + `read_literal(ocr_lines, category="auto", question)` exactly matching the Project FRIDAY wearable emulator product path.

## Evaluation Results
- **Total Images Evaluated**: 500
- **Answerable (289 items)**:
  - `answer_found`: 6 (2.08%)
  - `refused`: 262
  - `mismatch`: 21
- **Unanswerable (211 items)**:
  - `correct_refusal` [SAFE]: 203 (96.21%)
  - `spoke_on_unanswerable` [RISK]: 8
- **Candidate Numeric Review Items**: 1 items listed in `review_numeric.json`.

### Medicine-Like Subset (14 items)
- `answer_found`: 0
- `refused`: 7
- `mismatch`: 0
- `correct_refusal`: 7
- `spoke_on_unanswerable`: 0
