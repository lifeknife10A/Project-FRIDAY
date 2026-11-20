# PHASE 1: AI DISTILLATION & LOCAL MAC M4 SANDBOX
## Project FRIDAY Sovereign Vision-Language Model Pipeline

This directory contains the PyTorch source code, configuration files, and mathematical loss engines for Phase 1 of Project FRIDAY.

---

## 1. Directory Structure

```
phase1_ai_sandbox/
├── README.md                          # Phase 1 technical specification & execution guide
├── requirements.txt                   # Phase 1 Python dependencies (PyTorch MPS / Colab CUDA)
├── configs/
│   ├── model_config.json              # Student VLM dimensions & distillation parameters
│   └── vocab_subset_spec.json         # 64,000-token subset pruning policy
└── src/
    ├── __init__.py
    ├── audio_earcon.py                # <80ms instant two-tone acknowledgment earcon
    ├── optical_foveation.py           # 6° down-pitch transform & 2-stage dynamic foveation
    ├── mac_sandbox_emulator.py        # Milestone 1.4 end-to-end voice-to-vision emulator
    ├── distillation_loss.py           # Normalized, Epsilon-Smoothed Top-64 Forward KD Loss
    ├── student_vlm.py                 # SigLIP-B + 2x2 Spatial Unshuffle + Qwen2.5-0.5B architecture
    └── tokenizer_vocab_pruner.py      # Tokenizer vocabulary subset generation script
```

---

## 2. Core Architectural Pillars

### 2.1 2x2 Spatial Pixel-Unshuffle Downsampling ($576 \to 144$ Tokens)
Standard vision transformers project $384 \times 384$ images into 576 patch embeddings ($24 \times 24$ grid). Ingesting 576 visual tokens into a language decoder consumes prohibitive memory bandwidth during prefill.
* `SpatialUnshuffleDownsampler` (in `src/student_vlm.py`) applies `F.pixel_unshuffle(downscale_factor=2)`, compressing the $24 \times 24$ patch grid into a $12 \times 12 = 144$ token sequence while concatenating $4\times$ feature channels ($768 \times 4 = 3072$).
* A two-layer MLP projector maps the 3072-dim representations down to the language model's hidden dimension ($D = 896$).
* **Result:** 75% reduction in visual prefix length, slashing prefix prefill time to $< 45\text{ ms}$.

### 2.2 Discrete Vocabulary Pruning (64,000 Tokens)
The native Qwen2.5 vocabulary (151,936 tokens) creates a 136.1 MB LM-head that saturates the RK3576 LPDDR4x bus.
* `tokenizer_vocab_pruner.py` derives a strict 64k vocabulary subset ($\mathcal{V}_S \subset \mathcal{V}_T$) preserving:
  1. All special control tokens ($500$ tokens).
  2. All raw single-byte tokens ($256$ tokens).
  3. Devanagari Hindi script tokens ($4,500$ tokens).
  4. Frequency-ranked English & Hinglish conversational tokens ($58,744$ tokens).
* **Result:** LM-head footprint is compressed from $136.1\text{ MB}$ down to **$57.34\text{ MB}$** at INT8 precision.

### 2.3 Normalized Bounded Forward KL Divergence Loss
Implemented in `src/distillation_loss.py`:
$$\Omega_{64} = \text{Top-64}\left( \left\{ v \in \mathcal{V}_S \mid p_T(v) \right\} \right) \quad \implies \quad \Omega_{64} \subseteq \mathcal{V}_S$$
$$\tilde{p}_T(v) = \frac{p_T(v)}{\sum_{u \in \Omega_{64}} p_T(u)}, \qquad \bar{p}_S(v) = \frac{p_S(v)}{\sum_{u \in \Omega_{64}} p_S(u)}$$
$$\tilde{p}_S(v) = (1 - \epsilon)\bar{p}_S(v) + \frac{\epsilon}{|\Omega_{64}|}, \quad \epsilon = 10^{-5}$$
$$\mathcal{L}_{\text{KD}} = \sum_{v \in \Omega_{64}} \tilde{p}_T(v) \log \left( \frac{\tilde{p}_T(v)}{\tilde{p}_S(v)} \right)$$
* **Mathematical Closure:** Both distributions sum to exactly $1.000$ over the common support $\Omega_{64}$, and $\tilde{p}_S(v) \ge \frac{\epsilon}{64} > 0$, guaranteeing zero loss spikes or gradient instability.

---

## 3. Environment Setup & Running Unit Tests Locally (Mac M4)

To install dependencies and verify the components on your local machine:
```bash
# 0. Install Dependencies (₹0 Outlay)
pip3 install -r phase1_ai_sandbox/requirements.txt

# 1. Verify the Distillation Loss Engine
python3 phase1_ai_sandbox/src/distillation_loss.py

# 2. Verify the 576 -> 144 Spatial Unshuffle & VLM Forward Pass
python3 phase1_ai_sandbox/src/student_vlm.py

# 3. Verify Vocabulary Pruning Policy
python3 phase1_ai_sandbox/src/tokenizer_vocab_pruner.py

# 4. Verify Earcon (<80ms Audio Chime)
python3 phase1_ai_sandbox/src/audio_earcon.py

# 5. Verify Optical Foveation (6° Down-Pitch & Centroid Text Crop)
python3 phase1_ai_sandbox/src/optical_foveation.py

# 6. Run Milestone 1.4 End-to-End Voice-to-Vision Emulator (Spoken Audio via Mac Speakers)
python3 phase1_ai_sandbox/src/mac_sandbox_emulator.py

# Optional: Run with real webcam or silent test mode
python3 phase1_ai_sandbox/src/mac_sandbox_emulator.py --camera
python3 phase1_ai_sandbox/src/mac_sandbox_emulator.py --mute
```
