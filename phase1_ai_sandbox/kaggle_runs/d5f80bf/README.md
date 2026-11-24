# Kaggle Execution Run: d5f80bf (superseded by 7571e39)

> **Note**: This run is superseded by 7571e39.

- **Git Commit Provenance**: `d5f80bf1b2b38cf48b961033fc02ebbaafbb82f5`
- **Execution Environment**: Kaggle Notebook Session (2x NVIDIA T4, Python 3.13.16, machine_shape: `NvidiaTeslaT4`)
- **Kernel Run ID**: `lifeknife/friday-distillation` (Version 4)
- **Artifacts Recorded**: Executed Jupyter notebooks (`friday-distillation.ipynb` and `friday_distillation_colab.ipynb`), `milestone_1_5_gate_report.json`, `weights_manifest.json`

## Verbatim Cell Outputs from Notebook

### Cell 1: Environment & Pip Check
```
[*] Python Version: 3.13.16 (main, Oct  1 2026, 15:40:24) [GCC 13.3.0]
[✓] Auditor Item J1 Verified: Zero broken requirements in Friday dependencies (13 unrelated preinstalled package warnings).
[✓] Auditor Item KB5 Verified: numpy==2.1.3, pyarrow==26.0.1, datasets==5.0.1
[✓] Runtime Environment: Kaggle
[✓] Git Commit SHA: d5f80bf1b2b38cf48b961033fc02ebbaafbb82f5
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

### Cell 5: Standardized Benchmark Dataset
```
[✓] Loaded 40 standardized benchmark samples from: /kaggle/input/friday-benchmark-dataset/benchmark_manifest.json
    Auditor Item KB1/N1 Verified: Dataset 'friday-benchmark-dataset' sha256 verified (1244838b6fa5fc07...). Checksum source: assets/benchmark_dataset/benchmark_manifest.sha256
    Auditor Item F4 Verified: Answer leakage eliminated, 100% verified external assets.
```

### Cell 6: PP-OCRv6 Evaluation & Unit Tests
```
[✓] ALL 7 BR1-BR5 LITERAL READER UNIT TESTS PASSED!
=================================================================
PP-OCRv6 BENCHMARK AUDIT (HONEST EXECUTION ON STANDARDIZED BENCHMARK)
=================================================================
  Total Images Evaluated       : 40
  Raw Unstripped CER           : 6.24% (Target: <= 5.0%)
  Raw Unstripped WER           : 28.98% (Target: <= 30.0%)
  Space-Normalized CER         : 5.77% (Target: <= 5.0%)
  Space-Normalized WER         : 28.98% (Target: <= 30.0%)
  Key-Field Match (Space-Ins)  : 72.50% (Target: >= 95.0%)
  Verbatim Number/Dose Safety  : 85.00% (Target: >= 95.0%)
=================================================================
```

### Cell 7: Model Loading & Memory Allocation
```
[*] Loading Multimodal Teacher: Qwen/Qwen2-VL-2B-Instruct on cuda (torch.float16)...
[✓] Teacher loaded (torch.float16). Parameters: 2,208,985,600
[✓] Verified: 100% token string equality across all 64,000 vocabulary subset IDs.
[✓] Student Model Initialized with Pruned Weights: 415,242,112 parameters
```

### Cell 8: Multimodal Distillation (Stages 1a & 1b)
```
[✓] Stage 1a Pairs: 1760 train, 440 val
[✓] Stage 1b Pairs: 880 train, 320 val
=================================================================
[*] COMMENCING STAGE 1a: 2x2 SPATIAL UNSHUFFLE PROJECTOR ALIGNMENT
=================================================================
 --> Step-0 Baseline Held-Out Stage 1a Caption Loss: 6.3472
  [Stage 1a Step 40/200] Train Loss: 4.7863, Grad Norm: 22.8850, LR: 0.000100
  [Stage 1a Held-Out Loss @ Step 50/200]: 5.5480 (Baseline: 6.3472)
  [Stage 1a Step 80/200] Train Loss: 3.6497, Grad Norm: 221.8941, LR: 0.000100
  [Stage 1a Held-Out Loss @ Step 100/200]: 5.2052 (Baseline: 6.3472)
  [Stage 1a Step 120/200] Train Loss: 4.5434, Grad Norm: 26.6105, LR: 0.000100
  [Stage 1a Held-Out Loss @ Step 150/200]: 4.9452 (Baseline: 6.3472)
  [Stage 1a Step 160/200] Train Loss: 2.9318, Grad Norm: 11.0234, LR: 0.000100
  [Stage 1a Step 200/200] Train Loss: 2.5926, Grad Norm: 11.3050, LR: 0.000100
  [Stage 1a Held-Out Loss @ Step 200/200]: 4.7660 (Baseline: 6.3472)
 --> Final Held-Out Stage 1a Caption Loss: 4.7660 (Baseline: 6.3472)
[✓] Stage 1a Projector Alignment Verified: Held-out loss strictly decreased (6.3472 -> 4.7660).
=================================================================
[*] COMMENCING STAGE 1b: BOUNDED TOP-64 FORWARD-KL DISTILLATION
=================================================================
[✓] Auditor Item C2 Verified: All KD loss unit tests passed.
[✓] Auditor Item C3 Verified: Cached 320 validation targets; teacher forwards eliminated during validation.
 --> Step-0 Held-Out Multimodal KD Loss: 3.2788
  [✓] Step 8: Held-out validation loss strictly improved to 2.3004 -> Checkpoint saved.
  [✓] Step 16: Held-out validation loss strictly improved to 1.9361 -> Checkpoint saved.
  [✓] Step 24: Held-out validation loss strictly improved to 1.9066 -> Checkpoint saved.
  [✓] Step 32: Held-out validation loss strictly improved to 1.8538 -> Checkpoint saved.
  [✓] Step 40: Held-out validation loss strictly improved to 1.7827 -> Checkpoint saved.
  [✓] Step 48: Held-out validation loss strictly improved to 1.6844 -> Checkpoint saved.
  [✓] Step 56: Held-out validation loss strictly improved to 1.6528 -> Checkpoint saved.
  [✓] Step 64: Held-out validation loss strictly improved to 1.6356 -> Checkpoint saved.
  [✓] Step 72: Held-out validation loss strictly improved to 1.6014 -> Checkpoint saved.
  [✓] Step 80: Held-out validation loss strictly improved to 1.5706 -> Checkpoint saved.
  [✓] Step 88: Held-out validation loss strictly improved to 1.5691 -> Checkpoint saved.
 --> Final Held-Out Multimodal KD Loss: 1.6389 (Best: 1.5691, Step-0 Baseline: 3.2788)
[✓] Checkpoint state persisted at: /kaggle/working/FRIDAY_weights/best_student_vlm.pt
[*] Teacher hf_device_map: {'': device(type='cuda', index=1)}
[*] CUDA Device 0 (Tesla T4) Max Memory Allocated: 8481.19 MB
[*] CUDA Device 1 (Tesla T4) Max Memory Allocated: 4419.65 MB
```

### Cell 9: Projector Deployment Loader Verification
```
[✓] Spatial Unshuffle Downsampler saved to: /kaggle/working/FRIDAY_weights/spatial_unshuffle_downsampler.pt (from best checkpoint)
[*] Verifying deployment loader parity with live_wearable_emulator.py...
[✓] Auditor Item C4 Verified: Projector deployment loader check (max abs diff: 0.00e+00)
[✓] End-to-End Multimodal Forward Pass Verified: Shape [1, 145, 64000]
```

### Cell 10: Comparative Model Scoring & Safety Audit
```
=================================================================
END-TO-END PIPELINE MODEL SCORING & SAFETY AUDIT (A2, A3, B2, B3)
=================================================================
  Literal Path (Product)  : Correct = 29, Safe-Refusal = 5, Wrong-Spoken = 0, Incomplete = 6, No-Answer = 0
  Student Free-Gen (Comp) : (student free-gen, NOT the product path)
  Vision Path             : Correct = 0, Safe-Refusal = 0, Wrong-Spoken = 28, Incomplete = 12, No-Answer = 0
  Pre-Distill             : Correct = 1, Safe-Refusal = 0, Wrong-Spoken = 17, Incomplete = 22, No-Answer = 0
  Teacher Model           : Correct = 7, Safe-Refusal = 0, Wrong-Spoken = 22, Incomplete = 11, No-Answer = 0
  Literal Path Key Accuracy: 72.5%
=================================================================
[*] Teacher hf_device_map: {'': device(type='cuda', index=1)}
[*] CUDA Device 0 (Tesla T4) Max Memory Allocated: 8481.19 MB
[*] CUDA Device 1 (Tesla T4) Max Memory Allocated: 4440.98 MB
```

### Cell 11: Real Packed W4A16 Serialization
```
[*] Serializing True All-INT4 Packed Binary (including tied embed_tokens/lm_head) to: /kaggle/working/FRIDAY_weights/friday_student_w4a16_packed.pt...
[✓] Physical Artifact Written to Disk: /kaggle/working/FRIDAY_weights/friday_student_w4a16_packed.pt
  Binary File Size: 199.68 MiB (209.38 MB)
  Target Theoretical Footprint: ~208.63 MB (Contract Limit: <= 233.00 MB)
[✓] Artifact size verified strictly below 233.0 MB limit.
```

### Cell 12: Unified Milestone 1.5 Gate Decision
```
=================================================================
PROJECT FRIDAY: MILESTONE 1.5 UNIFIED FINANCIAL & TECHNICAL GATE
=================================================================
  [GATE 1] Optical Resolution (>=10 px/char)      : PASS [✓] (12.8 px/char, Analytic)
  [GATE 2] Spatial Unshuffle (strictly 144 tokens) : PASS [✓]
  [GATE 3] Memory Bandwidth (<14.00 GB/s)          : PASS [✓] (5.75 GB/s @ 25 tok/s, Analytic)
  [GATE 4] Kokoro Neural Speech Synthesis          : FAIL [X] (NOT TESTED (Kokoro runtime not loaded in this session))
  [GATE 5] Downstream 40-Sample Benchmark          : FAIL [X] (CER: 6.24%, Wrong-Spoken: 0, No-Answer: 0)
  [GATE 6] Distillation Convergence (>=5% drop)   : PASS [✓] (Val KD: 1.5691 vs Baseline: 3.2788)
=================================================================
>>> OVERALL FINANCIAL & TECHNICAL GATE DECISION: HALTED (CRITERIA NOT MET) <<<
=================================================================
[✓] Gate Report Saved to: /kaggle/working/FRIDAY_weights/milestone_1_5_gate_report.json
```
