# Kaggle Execution Run: 543234b (superseded by 7571e39)

> **Note**: This run is superseded by 7571e39.

- **Git Commit Provenance**: `543234b1abc87d3786493f0e097535284434c9a6`
- **Execution Environment**: Kaggle Notebook Session (2x NVIDIA T4, Python 3.13.16)
- **Artifacts Recorded**: Executed Jupyter notebook (`friday_distillation_colab.ipynb` / `friday-distillation.ipynb`)

## Results Verbatim from Notebook Output

- **Overall Financial & Technical Gate Decision**: `HALTED (CRITERIA NOT MET)`
- **Gate 1 (Optical Resolution)**: `PASS [✓] (12.8 px/char, Analytic)`
- **Gate 2 (Spatial Unshuffle)**: `PASS [✓] (144 tokens, 896 dim)`
- **Gate 3 (Memory Bandwidth)**: `PASS [✓] (5.51 GB/s @ 25 tok/s, Analytic)`
- **Gate 4 (Kokoro Neural Speech Synthesis)**: `FAIL [X] (NOT TESTED (Kokoro runtime not loaded in this session))`
- **Gate 5 (Downstream 40-Sample Benchmark)**: `FAIL [X] (literal 6 correct / 34 wrong_spoken; CER: 6.24%, Wrong-Spoken: 34, No-Answer: 0)`
  - *Audit Note*: Gate 5 scorer later found defective (Audit #13 A2), counts are not authoritative in either direction.
- **Gate 6 (Distillation Convergence)**: `PASS [✓] (Val KD: 1.3846 vs Baseline: 3.5121; Stage 1a held-out loss: 6.3128 -> 4.5176; Stage 1b step-0 KD: 3.5121 -> best 1.3846 @ step 96)`

## Additional Notes
- The physical binary weights (`friday_student_w4a16_packed.pt`, `best_student_vlm.pt`, `spatial_unshuffle_downsampler.pt`) and standalone gate report JSON were written to `/kaggle/working/FRIDAY_weights/` on the remote Kaggle VM during the session and were not downloaded to local storage; only the executed notebook was exported from the Kaggle web session.
