# Project Friday: Spec Benchmark Dataset (Milestone 1.5)

This directory contains the 40-sample standardized evaluation benchmark rendered according to the IMX415 camera optical specification (12.8 ± 1 px/char character scale at 35 cm distance using DejaVu Sans Mono).

## Manifest Integrity
- `benchmark_manifest.json` sha256: `1244838b6fa5fc07b1780df27b21add05850145da28ae6524f2785cb2f99989e`
- Identical text content, ground truth, required fields, and IDs as `assets/benchmark_dataset/`.

## Offline Speech Synthesis Verification
- `kokoro_eval.json` sha256: `875c81933a6a571f129d2cb318b029cdebe877b7f68dc442cfc34f4d77e5f1c2`
- Offline speech evaluation metrics across all 40 DEV samples + REFUSAL_TEXT on host CPU.
