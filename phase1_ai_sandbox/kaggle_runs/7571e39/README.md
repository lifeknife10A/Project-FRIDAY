# Kaggle Execution Run: 7571e39

- **Git Commit Provenance**: `7571e392f45830ea1ad1d146758a5e9bd0a40d9e`
- **Execution Environment**: Kaggle Notebook Session (2x NVIDIA T4, Python 3.13.16, machine_shape: `NvidiaTeslaT4`)
- **Kernel Run ID**: `lifeknife/friday-distillation` (Version 5)
- **Artifacts Recorded**: Executed Jupyter notebooks (`friday-distillation.ipynb` and `friday_distillation_colab.ipynb`), `milestone_1_5_gate_report.json`, `weights_manifest.json`

## Verbatim Cell Outputs from Notebook

### Cell 1: Environment & Pip Check
```
[✓] Auditor Item J1 Verified: Scoped pip check unit tests passed.
[*] Installing pinned dependencies on Kaggle BEFORE any library imports (Auditor Items KB4, KB5, H2 & C7)...
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
bigframes 2.51.0 requires google-cloud-bigquery-storage<3.0.0,>=2.30.0, which is not installed.
litellm 1.109.1 requires tokenizers<1.0,>=0.21.0, but you have tokenizers 0.20.3 which is incompatible.
cudf-cu13 26.6.0 requires pyarrow<24,>=19.0.0, but you have pyarrow 26.0.1 which is incompatible.
gradio-client 2.7.2 requires huggingface-hub<3.0,>=1.16.0, but you have huggingface-hub 0.36.2 which is incompatible.
gradio 6.30.0 requires huggingface-hub<3.0,>=1.16.0, but you have huggingface-hub 0.36.2 which is incompatible.
gradio 6.30.0 requires pillow<13.0,>=8.0, but you have pillow 13.0.0 which is incompatible.
diffusers 0.42.0 requires huggingface-hub<3.0,>=1.32.0, but you have huggingface-hub 0.36.2 which is incompatible.
[*] Python Version: 3.13.16 (main, Oct  1 2026, 15:40:24) [GCC 13.3.0]
[WARN] unrelated preinstalled package: bigframes 2.51.0 requires google-cloud-bigquery-storage, which is not installed.
[WARN] unrelated preinstalled package: litellm 1.109.1 has requirement tokenizers<1.0,>=0.21.0, but you have tokenizers 0.20.3.
[WARN] unrelated preinstalled package: google-colab 1.0.0 has requirement jupyter-server==2.20.0, but you have jupyter-server 2.12.5.
[WARN] unrelated preinstalled package: google-colab 1.0.0 has requirement pandas==2.2.3, but you have pandas 2.3.3.
[WARN] unrelated preinstalled package: google-colab 1.0.0 has requirement requests==2.32.4, but you have requests 2.34.2.
[WARN] unrelated preinstalled package: dopamine-rl 4.1.2 has requirement gym<=0.25.2, but you have gym 0.26.2.
[WARN] unrelated preinstalled package: moviepy 1.0.3 has requirement decorator<5.0,>=4.0.2, but you have decorator 5.3.1.
[WARN] unrelated preinstalled package: cudf-cu13 26.6.0 has requirement pyarrow<24,>=19.0.0, but you have pyarrow 26.0.1.
[WARN] unrelated preinstalled package: ydf 0.15.0 has requirement protobuf<7.0.0,>=5.29.1, but you have protobuf 7.36.2.
[WARN] unrelated preinstalled package: gradio-client 2.7.2 has requirement huggingface-hub<3.0,>=1.16.0, but you have huggingface-hub 0.36.2.
[WARN] unrelated preinstalled package: gradio 6.30.0 has requirement huggingface-hub<3.0,>=1.16.0, but you have huggingface-hub 0.36.2.
[WARN] unrelated preinstalled package: gradio 6.30.0 has requirement pillow<13.0,>=8.0, but you have pillow 13.0.0.
[WARN] unrelated preinstalled package: diffusers 0.42.0 has requirement huggingface-hub<3.0,>=1.32.0, but you have huggingface-hub 0.36.2.
[✓] Auditor Item J1 Verified: Zero broken requirements in Friday dependencies (13 unrelated preinstalled package warnings).
[✓] Auditor Item KB5 Verified: numpy==2.1.3, pyarrow==26.0.1, datasets==5.0.1
[✓] Runtime Environment: Kaggle
[✓] Git Commit SHA: 7571e392f45830ea1ad1d146758a5e9bd0a40d9e
[✓] Checkpoint Directory Initialized: /kaggle/working/FRIDAY_weights
```

### Cell 2: Hardware & Compute Placement
```
[✓] Multi-GPU Mode Enabled (Auditor Item C6): Student on cuda:0, Teacher on cuda:1
[*] Active Compute Device: cuda
[✓] Active Accelerator: Tesla T4 (2 GPU(s))
    Memory Allocated: 0.00 MB
    Memory Reserved: 0.00 MB
```

### Cell 5: Standardized Benchmark Dataset (Auditor Item G2)
```
[*] DATASET_VARIANT: spec (canonical)
[✓] Canonical SPEC-resolution DEV set loaded: 40 samples from /kaggle/input/friday-benchmark-dataset/benchmark_dataset_spec/benchmark_manifest.json
[✓] Low-res (1080p-class) stress DEV set loaded: 40 samples from /kaggle/input/friday-benchmark-dataset/benchmark_dataset/benchmark_manifest.json
    Auditor Item G2 Verified: 100% per-image sha256 verified on both sets (40 spec + 40 low-res). Zero silent fallback.
```

### Cell 6: PP-OCRv6 Evaluation & Unit Tests (Canonical Spec & Stress Low-Res Passes)
```
[✓] ALL 16 BR1-BR5 & ROUND D/F/G LITERAL READER UNIT TESTS PASSED!

[*] RUNNING PP-OCRv6 (RapidOCR 3.10.0) INFERENCE (Auditor Item G2 — DATASET_VARIANT: spec):
  --> Pass 1/2: CANONICAL SPEC-RESOLUTION DEV SET (plan.md IMX415 camera, 12.8 px/char)...
[32m[INFO] 2026-11-24 00:20:47,808 [RapidOCR] base.py:23: Using engine_name: onnxruntime[0m
[32m[INFO] 2026-11-24 00:20:47,918 [RapidOCR] download_file.py:60: File exists and is valid: /usr/local/lib/python3.13/dist-packages/rapidocr/models/PP-OCRv6_det_small.onnx[0m
[32m[INFO] 2026-11-24 00:20:47,919 [RapidOCR] main.py:63: Using /usr/local/lib/python3.13/dist-packages/rapidocr/models/PP-OCRv6_det_small.onnx[0m
[32m[INFO] 2026-11-24 00:20:49,522 [RapidOCR] base.py:23: Using engine_name: onnxruntime[0m
[32m[INFO] 2026-11-24 00:20:49,526 [RapidOCR] download_file.py:60: File exists and is valid: /usr/local/lib/python3.13/dist-packages/rapidocr/models/ch_ppocr_mobile_v2.0_cls_mobile.onnx[0m
[32m[INFO] 2026-11-24 00:20:49,527 [RapidOCR] main.py:63: Using /usr/local/lib/python3.13/dist-packages/rapidocr/models/ch_ppocr_mobile_v2.0_cls_mobile.onnx[0m
[32m[INFO] 2026-11-24 00:20:49,575 [RapidOCR] base.py:23: Using engine_name: onnxruntime[0m
[32m[INFO] 2026-11-24 00:20:49,654 [RapidOCR] download_file.py:60: File exists and is valid: /usr/local/lib/python3.13/dist-packages/rapidocr/models/PP-OCRv6_rec_small.onnx[0m
[32m[INFO] 2026-11-24 00:20:49,654 [RapidOCR] main.py:63: Using /usr/local/lib/python3.13/dist-packages/rapidocr/models/PP-OCRv6_rec_small.onnx[0m
  --> Pass 2/2: STRESS LOW-RES DEV SET (1080p-class, 5.5 px/char)...

======================================================================
PP-OCRv6 BENCHMARK AUDIT (Auditor Item G2 — DATASET_VARIANT: spec)
======================================================================
  CANONICAL SET: SPEC-RESOLUTION DEV (plan.md IMX415 camera, 12.8 px/char):
    Total Images Evaluated       : 40
    Raw Unstripped CER           : 4.60% (Target: <= 5.0%)
    Raw Unstripped WER           : 5.68% (Target: <= 30.0%)
    Space-Normalized CER         : 4.15% (Target: <= 5.0%)
    Space-Normalized WER         : 5.68% (Target: <= 30.0%)
    Key-Field Match (Space-Ins)  : 95.00% (38/40, Target: >= 95.0%)
    Verbatim Number/Dose Safety  : 95.00% (Target: >= 95.0%)
----------------------------------------------------------------------
  STRESS SET: LOW-RES (1080p-class) DEV (5.5 px/char):
    Total Images Evaluated       : 40
    Raw Unstripped CER           : 6.15% (stress)
    Raw Unstripped WER           : 26.90% (stress)
    Key-Field Match (Space-Ins)  : 90.00% (36/40)
    Verbatim Number/Dose Safety  : 92.50%
======================================================================
```

### Cell 7: Model Loading & Memory Allocation
```
[*] Cell 7 Start CUDA Allocated Memory: 431.27 MB
[*] Loading Multimodal Teacher: Qwen/Qwen2-VL-2B-Instruct on cuda (torch.float16)...
`Qwen2VLRotaryEmbedding` can now be fully parameterized by passing the model config through the `config` argument. All other arguments will be removed in v4.46
[✓] Teacher loaded (torch.float16). Parameters: 2,208,985,600
[*] Verifying 1-to-1 token string equality between Qwen2-VL and Qwen2.5 across all 64,000 subset ids...
[✓] Verified: 100% token string equality across all 64,000 vocabulary subset IDs.
[*] Initializing Student Model from: Qwen/Qwen2.5-0.5B...
[✓] Student Model Initialized with Pruned Weights: 415,242,112 parameters
[✓] Captured Pre-Distillation Student State for Cell 10 comparative benchmark.
[✓] Step-0 Student Logits Verified: Shape [1, T, 64000].
```

### Cell 8: Multimodal Distillation (Stages 1a & 1b)
```
[*] Cell 8 Start CUDA Allocated Memory: 2017.98 MB
[*] Streaming real Stage 1a multimodal dataset via datasets (target: 2200 pairs)...
  --> Attempting streaming load from 'Multimodal-Fatima/COCO_captions_train' (train)...
  [✓] Successfully collected 2200 real pairs from 'Multimodal-Fatima/COCO_captions_train'.
[✓] Persisted Stage 1a manifest cache (loader_version=3.0, sha=7571e39) to: /kaggle/working/phase1_ai_sandbox/external_train_data/manifest_1a.json
[*] Streaming real Stage 1b multimodal dataset via datasets (target: 1200 pairs)...
  --> Attempting streaming load from 'Multimodal-Fatima/TextVQA_train' (train)...
  [✓] Successfully collected 1200 real pairs from 'Multimodal-Fatima/TextVQA_train'.
[✓] Persisted Stage 1b manifest cache (loader_version=3.0, sha=7571e39) to: /kaggle/working/phase1_ai_sandbox/external_train_data/manifest_1b.json
[✓] Stage 1a Pairs: 1760 train, 440 val
[✓] Stage 1b Pairs: 880 train, 320 val
=================================================================
[*] COMMENCING STAGE 1a: 2x2 SPATIAL UNSHUFFLE PROJECTOR ALIGNMENT
=================================================================
 --> Step-0 Baseline Held-Out Stage 1a Caption Loss: 6.4752
  [Stage 1a Step 40/200] Train Loss: 4.9119, Grad Norm: 20.5204, LR: 0.000100
  [Stage 1a Held-Out Loss @ Step 50/200]: 5.6063 (Baseline: 6.4752)
  [Stage 1a Step 80/200] Train Loss: 3.6005, Grad Norm: 23.2087, LR: 0.000100
  [Stage 1a Held-Out Loss @ Step 100/200]: 5.1695 (Baseline: 6.4752)
  [Stage 1a Step 120/200] Train Loss: 3.9328, Grad Norm: 24.2632, LR: 0.000100
  [Stage 1a Held-Out Loss @ Step 150/200]: 4.9308 (Baseline: 6.4752)
  [Stage 1a Step 160/200] Train Loss: 3.2300, Grad Norm: 13.9568, LR: 0.000100
  [Stage 1a Step 200/200] Train Loss: 2.5960, Grad Norm: 10.4034, LR: 0.000100
  [Stage 1a Held-Out Loss @ Step 200/200]: 4.7724 (Baseline: 6.4752)
 --> Final Held-Out Stage 1a Caption Loss: 4.7724 (Baseline: 6.4752)
[✓] Stage 1a Projector Alignment Verified: Held-out loss strictly decreased (6.4752 -> 4.7724).
=================================================================
[*] COMMENCING STAGE 1b: BOUNDED TOP-64 FORWARD-KL DISTILLATION
=================================================================
[✓] Auditor Item C2 Verified: All KD loss unit tests passed.
[*] Precomputing teacher top-64 targets and SigLIP patches for 320 validation items (Auditor Item C3)...
[✓] Auditor Item C3 Verified: Cached 320 validation targets; teacher forwards eliminated during validation.
 --> Step-0 Held-Out Multimodal KD Loss: 3.4275
[*] Distilling with gradient accumulation over 100 steps...
  [Stage 1b Step 2/100] Forward-KL Loss: 6.2484, Grad Norm: 0.0000
  [Stage 1b Step 4/100] Forward-KL Loss: 2.7572, Grad Norm: 0.0000
  [Stage 1b Step 6/100] Forward-KL Loss: 5.2663, Grad Norm: 0.0000
  [✓] Step 8: Held-out validation loss strictly improved to 2.4394 -> Checkpoint saved.
  [Stage 1b Step 8/100] Forward-KL Loss: 5.8268, Grad Norm: 191.2724
  [Stage 1b Step 10/100] Forward-KL Loss: 2.0978, Grad Norm: 191.2724
  [Stage 1b Step 12/100] Forward-KL Loss: 3.5566, Grad Norm: 191.2724
  [Stage 1b Step 14/100] Forward-KL Loss: 4.0215, Grad Norm: 191.2724
  [✓] Step 16: Held-out validation loss strictly improved to 1.9309 -> Checkpoint saved.
  [Stage 1b Step 16/100] Forward-KL Loss: 1.7670, Grad Norm: 146.2370
  [Stage 1b Step 18/100] Forward-KL Loss: 0.6874, Grad Norm: 146.2370
  [Stage 1b Step 20/100] Forward-KL Loss: 2.0403, Grad Norm: 146.2370
  [Stage 1b Step 22/100] Forward-KL Loss: 2.6186, Grad Norm: 146.2370
  [✓] Step 24: Held-out validation loss strictly improved to 1.9263 -> Checkpoint saved.
  [Stage 1b Step 24/100] Forward-KL Loss: 3.5051, Grad Norm: 63.8653
  [Stage 1b Step 26/100] Forward-KL Loss: 4.0830, Grad Norm: 63.8653
  [Stage 1b Step 28/100] Forward-KL Loss: 2.7119, Grad Norm: 63.8653
  [Stage 1b Step 30/100] Forward-KL Loss: 1.2964, Grad Norm: 63.8653
  [Stage 1b Step 32/100] Forward-KL Loss: 3.7898, Grad Norm: 95.1604
  [Stage 1b Step 34/100] Forward-KL Loss: 1.9979, Grad Norm: 95.1604
  [Stage 1b Step 36/100] Forward-KL Loss: 1.5049, Grad Norm: 95.1604
  [Stage 1b Step 38/100] Forward-KL Loss: 3.5644, Grad Norm: 95.1604
  [✓] Step 40: Held-out validation loss strictly improved to 1.8565 -> Checkpoint saved.
  [Stage 1b Step 40/100] Forward-KL Loss: 2.2796, Grad Norm: 63.8369
  [Stage 1b Step 42/100] Forward-KL Loss: 0.7720, Grad Norm: 63.8369
  [Stage 1b Step 44/100] Forward-KL Loss: 2.3430, Grad Norm: 63.8369
  [Stage 1b Step 46/100] Forward-KL Loss: 2.0066, Grad Norm: 63.8369
  [✓] Step 48: Held-out validation loss strictly improved to 1.7348 -> Checkpoint saved.
  [Stage 1b Step 48/100] Forward-KL Loss: 0.3439, Grad Norm: 35.5884
  [Stage 1b Step 50/100] Forward-KL Loss: 2.1465, Grad Norm: 35.5884
  [Stage 1b Step 52/100] Forward-KL Loss: 1.8370, Grad Norm: 35.5884
  [Stage 1b Step 54/100] Forward-KL Loss: 1.5409, Grad Norm: 35.5884
  [✓] Step 56: Held-out validation loss strictly improved to 1.7109 -> Checkpoint saved.
  [Stage 1b Step 56/100] Forward-KL Loss: 3.2566, Grad Norm: 53.0771
  [Stage 1b Step 58/100] Forward-KL Loss: 1.5178, Grad Norm: 53.0771
  [Stage 1b Step 60/100] Forward-KL Loss: 1.9210, Grad Norm: 53.0771
  [Stage 1b Step 62/100] Forward-KL Loss: 7.7283, Grad Norm: 53.0771
  [Stage 1b Step 64/100] Forward-KL Loss: 3.9733, Grad Norm: 54.9718
  [Stage 1b Step 66/100] Forward-KL Loss: 2.5432, Grad Norm: 54.9718
  [Stage 1b Step 68/100] Forward-KL Loss: 1.1726, Grad Norm: 54.9718
  [Stage 1b Step 70/100] Forward-KL Loss: 1.5383, Grad Norm: 54.9718
  [Stage 1b Step 72/100] Forward-KL Loss: 0.3178, Grad Norm: 51.2650
  [Stage 1b Step 74/100] Forward-KL Loss: 1.5914, Grad Norm: 51.2650
  [Stage 1b Step 76/100] Forward-KL Loss: 1.4417, Grad Norm: 51.2650
  [Stage 1b Step 78/100] Forward-KL Loss: 0.8155, Grad Norm: 51.2650
  [✓] Step 80: Held-out validation loss strictly improved to 1.6960 -> Checkpoint saved.
  [Stage 1b Step 80/100] Forward-KL Loss: 0.3983, Grad Norm: 50.7968
  [Stage 1b Step 82/100] Forward-KL Loss: 1.4329, Grad Norm: 50.7968
  [Stage 1b Step 84/100] Forward-KL Loss: 1.5962, Grad Norm: 50.7968
  [Stage 1b Step 86/100] Forward-KL Loss: 0.9815, Grad Norm: 50.7968
  [✓] Step 88: Held-out validation loss strictly improved to 1.6693 -> Checkpoint saved.
  [Stage 1b Step 88/100] Forward-KL Loss: 1.1510, Grad Norm: 61.4201
  [Stage 1b Step 90/100] Forward-KL Loss: 5.0863, Grad Norm: 61.4201
  [Stage 1b Step 92/100] Forward-KL Loss: 0.0991, Grad Norm: 61.4201
  [Stage 1b Step 94/100] Forward-KL Loss: 1.8195, Grad Norm: 61.4201
  [Stage 1b Step 96/100] Forward-KL Loss: 1.5518, Grad Norm: 38.1681
  [Stage 1b Step 98/100] Forward-KL Loss: 4.0182, Grad Norm: 38.1681
  [Stage 1b Step 100/100] Forward-KL Loss: 2.5253, Grad Norm: 34.3824
 --> Final Held-Out Multimodal KD Loss: 1.7038 (Best: 1.6693, Step-0 Baseline: 3.4275)
[✓] Checkpoint state persisted at: /kaggle/working/FRIDAY_weights/best_student_vlm.pt
[*] Teacher hf_device_map: {'': device(type='cuda', index=1)}
[*] CUDA Device 0 (Tesla T4) Max Memory Allocated: 8481.19 MB
[*] CUDA Device 1 (Tesla T4) Max Memory Allocated: 4419.65 MB
```

### Cell 9: Projector Reload Parity Check
```
[✓] Loaded student_state_dict from best validation checkpoint.
[✓] Loaded projector_state_dict from best validation checkpoint.
[✓] Loaded best validation checkpoint from: /kaggle/working/FRIDAY_weights/best_student_vlm.pt
[✓] Spatial Unshuffle Downsampler saved to: /kaggle/working/FRIDAY_weights/spatial_unshuffle_downsampler.pt (from best checkpoint)
[*] Verifying deployment loader parity with live_wearable_emulator.py...
[✓] Auditor Item C4 Verified: Projector deployment loader check (max abs diff: 0.00e+00)
[✓] End-to-End Multimodal Forward Pass Verified: Shape [1, 145, 64000]
```

### Cell 10: End-to-End Multimodal Evaluation & Model Comparison
```
[*] Cell 10 Start CUDA Allocated Memory: 6934.53 MB
[✓] All Auditor Items A2 & A3 score_response unit tests passed successfully!

[*] EVALUATING MODELS ON BENCHMARK DATASET (Auditor Items A2, A3, A6, B2, B3):
[*] DATASET_VARIANT: spec (evaluating canonical SPEC set)
/usr/local/lib/python3.13/dist-packages/transformers/generation/configuration_utils.py:590: UserWarning: `do_sample` is set to `False`. However, `temperature` is set to `0.01` -- this flag is only used in sample-based generation modes. You should set `do_sample=True` or unset `temperature`.
  warnings.warn(
/usr/local/lib/python3.13/dist-packages/transformers/generation/configuration_utils.py:595: UserWarning: `do_sample` is set to `False`. However, `top_p` is set to `0.001` -- this flag is only used in sample-based generation modes. You should set `do_sample=True` or unset `top_p`.
  warnings.warn(
/usr/local/lib/python3.13/dist-packages/transformers/generation/configuration_utils.py:612: UserWarning: `do_sample` is set to `False`. However, `top_k` is set to `1` -- this flag is only used in sample-based generation modes. You should set `do_sample=True` or unset `top_k`.
  warnings.warn(

--- Sample [med_01]: Amoxicillin 500mg Capsule Bottle ---
  Target Key              : 'Amoxicillin 500mg' (Safety: '500mg')
  Literal Path (Product)  : 'AMOXICILLIN 500 MG CAPSULE. TAKE 1 CAPSULE BY MOUTH TWICE DAILY FOR 10 DAYS.' -> correct
  Student Free-Gen (Comp) : 'The prescribed dose of METROPOLIS RX #101 is 500 mg of amoxycillin once daily for 10 days. The recommended dosage is 500 mg of amoxycillin once daily' -> wrong_spoken (student free-gen, NOT the product path)
  Vision Path Ans         : 'The prescribed dose of the drug is 10mg per day.
The prescribed dose of the drug is 10mg per day.
The prescribed dose of the drug is 10mg per day.
The prescribed dose of the drug' -> wrong_spoken
  Pre-Distill Ans         : 'Metoprolol (500 mg) is a medication prescribed for the treatment of hypertension. The recommended dose is 1 capsule taken twice daily for 10 days. It is important to follow the instructions provided by the healthcare provider' -> wrong_spoken
  Teacher Model Ans       : 'The medication is Amoxicillin 500 mg capsules. The prescribed dose is 1 capsule by mouth twice daily for 10 days.' -> correct

--- Sample [med_02]: Metformin 500mg Extended Release ---
  Target Key              : 'Metformin 500mg' (Safety: '500mg')
  Literal Path (Product)  : 'METFORMIN HCL 500 MG TABLET. TAKE 1 TABLET TWICE DAILY WITH MEALS.' -> correct
  Student Free-Gen (Comp) : 'The prescribed dose of metformin hydrocholate tablets is 500 mg twice daily with meals. The recommended dosage is 60 tablets per day. The recommended duration of treatment is 10 days. The recommended duration of' -> wrong_spoken (student free-gen, NOT the product path)
  Vision Path Ans         : 'The prescribed dose of the drug is 10mg per day.
The prescribed dose of the drug is 10mg per day.
The prescribed dose of the drug is 10mg per day.
The prescribed dose of the drug' -> wrong_spoken
  Pre-Distill Ans         : 'Metformin Hydrocholate 500 mg tablet' -> wrong_spoken
  Teacher Model Ans       : 'The medication is Metformin HCL 500 mg tablet. The prescribed dose is 60 tablets, taken twice daily with meals.' -> wrong_spoken

--- Sample [med_03]: Lisinopril 10mg Blood Pressure Tablet ---
  Target Key              : 'Lisinopril 10mg' (Safety: '10mg')
  Literal Path (Product)  : 'LISINOPRIL 10 MG TABLET. TAKE 1 TABLET DAILY IN THE MORNING.' -> correct
  Student Free-Gen (Comp) : 'The prescribed dose of OAKVALE COMMUNITY RX #305 RX # 4901283-7721 is 1 tablet daily in the morning. The patient is advised to take the medication in' -> wrong_spoken (student free-gen, NOT the product path)
  Vision Path Ans         : 'The drug is the drug is the drug is the drug is the drug is the drug is the drug is the drug is the drug is the drug is the drug is the drug is the drug is the drug is the drug is the drug is' -> wrong_spoken
  Pre-Distill Ans         : 'OAKVALE COMMUNITY RX #305 RX # 4901283-7721

The prescribed dose for this medication is 1 tablet per day.' -> wrong_spoken
  Teacher Model Ans       : 'The medication is Lisinopril 10 mg tablet. The prescribed dose is 30 tablets.' -> incomplete

--- Sample [med_04]: Atorvastatin 20mg Cholesterol Tablet ---
  Target Key              : 'Atorvastatin 20mg' (Safety: '20mg')
  Literal Path (Product)  : 'ATORVASTATIN CALCIUM 20 MG TABLET. TAKE 1 TABLET DAILY AT BEDTIME.' -> correct
  Student Free-Gen (Comp) : 'SUMMIT CREST PHARMACY #412 RX # 9021844-3310 DATE:11/19/2026 PATIENT: ARJUN MEHTA AT' -> incomplete (student free-gen, NOT the product path)
  Vision Path Ans         : 'The prescribed dose of the drug is 100mg of the prescribed dose of the drug is 100mg of the prescribed dose of the drug is 100mg of the prescribed dose of the drug is 1' -> wrong_spoken
  Pre-Distill Ans         : 'Arjun Mehta ATORVASTATIN CALCIUM 20 MG TABLET' -> incomplete
  Teacher Model Ans       : 'The medication is Atorvastatin Calcium 20 mg Tablet. The prescribed dose is 30 tablets taken at bedtime.' -> wrong_spoken

=================================================================
END-TO-END PIPELINE MODEL SCORING & SAFETY AUDIT (A2, A3, B2, B3)
=================================================================
  Literal Path (Product)  : Correct = 38, Safe-Refusal = 0, Wrong-Spoken = 0, Incomplete = 2, No-Answer = 0
  Student Free-Gen (Comp) : (student free-gen, NOT the product path)
  Vision Path             : Correct = 0, Safe-Refusal = 0, Wrong-Spoken = 27, Incomplete = 13, No-Answer = 0
  Pre-Distill             : Correct = 0, Safe-Refusal = 0, Wrong-Spoken = 16, Incomplete = 24, No-Answer = 0
  Teacher Model           : Correct = 11, Safe-Refusal = 0, Wrong-Spoken = 16, Incomplete = 13, No-Answer = 0
  Literal Path Key Accuracy: 95.0%
  Literal Path (Stress Low-Res): Correct = 36, Safe-Refusal = 1, Wrong-Spoken = 0, Incomplete = 3, No-Answer = 0
  Stress Low-Res Accuracy      : 90.0%
=================================================================
[*] Teacher hf_device_map: {'': device(type='cuda', index=1)}
[*] CUDA Device 0 (Tesla T4) Max Memory Allocated: 8481.19 MB
[*] CUDA Device 1 (Tesla T4) Max Memory Allocated: 4440.98 MB
```

### Cell 11: Real Packed W4A16 Quantization & Emulator Loader Parity
```
[*] Serializing True All-INT4 Packed Binary (including tied embed_tokens/lm_head) to: /kaggle/working/FRIDAY_weights/friday_student_w4a16_packed.pt...
[✓] Physical Artifact Written to Disk: /kaggle/working/FRIDAY_weights/friday_student_w4a16_packed.pt
  Binary File Size: 199.68 MiB (209.38 MB)
  Target Theoretical Footprint: ~208.63 MB (Contract Limit: <= 233.00 MB)
[✓] Artifact size verified strictly below 233.0 MB limit.
[*] Verifying packed INT4 emulator loader parity (Auditor Item C4')...
[✓] Auditor Item C4' Verified: Packed INT4 emulator loader check (max abs diff: 0.00e+00)
```

### Cell 12: Unified Financial & Technical Gate Decision
```
=================================================================
PROJECT FRIDAY: MILESTONE 1.5 UNIFIED FINANCIAL & TECHNICAL GATE
=================================================================
[*] DATASET_VARIANT: spec (Gate 5 evaluates canonical SPEC pass)
  [GATE 1] Optical Resolution (>=10 px/char)      : PASS [✓] (12.8 px/char, Analytic)
  [GATE 2] Spatial Unshuffle (strictly 144 tokens) : PASS [✓]
  [GATE 3] Memory Bandwidth (<14.00 GB/s)          : PASS [✓] (5.75 GB/s @ 25 tok/s, Analytic)
  [GATE 4] Kokoro Neural Speech Synthesis          : PASS [✓] (measured offline on host CPU (MacBook Air M4, 16 GB), commit bc30294; NOT measured on RK3576)
  [GATE 5] Downstream Benchmark [CANONICAL SPEC-RES (DATASET_VARIANT=spec)] : PASS [✓] (CER: 4.60%, WER: 5.68%, Correct: 38/40, Wrong-Spoken: 0, No-Answer: 0)
           [STRESS SET: low-res (1080p-class) stress set]                                : (CER: 6.15%, WER: 26.90%, Correct: 36/40, Wrong-Spoken: 0, No-Answer: 0)
  [GATE 6] Distillation Convergence (>=5% drop)   : PASS [✓] (Stage 1a Caption: 6.4752 -> 4.7724 (decreased: yes); Stage 1b Val KD: 1.6693 vs Baseline: 3.4275)
=================================================================
>>> OVERALL FINANCIAL & TECHNICAL GATE DECISION: PROCEED TO TARGET PROCUREMENT <<<
=================================================================
[✓] Gate Report Saved to: /kaggle/working/FRIDAY_weights/milestone_1_5_gate_report.json
```
