# PROJECT FRIDAY: AUTONOMOUS EDGE-AI SMART GLASSES
### Sovereign Multimodal Artificial Intelligence Wearable Platform

[![Document Version](https://img.shields.io/badge/Architecture-v9.1.0--Hardware--Locked-success.svg)](file:///Users/krish/NMIMS/Friday/docs/plan.md)
[![Mass Budget](https://img.shields.io/badge/AUW-115.0g%20(Audited)-blue.svg)](file:///Users/krish/NMIMS/Friday/docs/plan.md)
[![Memory Bandwidth](https://img.shields.io/badge/LPDDR5-5.77%20GB%2Fs%20(58.8%25%20Headroom)-purple.svg)](file:///Users/krish/NMIMS/Friday/phase1_ai_sandbox/README.md)
[![Battery Architecture](https://img.shields.io/badge/Power-Series%202S%20(7.4V)-brightgreen.svg)](file:///Users/krish/NMIMS/Friday/docs/hardware_bom.md)
[![Hardware Budget](https://img.shields.io/badge/Lean%20Wearable%20BOM-₹8%2C920%20INR%20(Zero--Waste)-orange.svg)](file:///Users/krish/NMIMS/Friday/docs/hardware_bom.md)
[![Phase 1 Outlay](https://img.shields.io/badge/Initial%20Spend-₹0%20(Mac%20M4%20Sandbox)-brightgreen.svg)](file:///Users/krish/NMIMS/Friday/phase1_ai_sandbox/README.md)

---

## 1. Executive Summary

**Project FRIDAY** is an indigenous, fully autonomous smart glasses wearable targeted to execute computer vision, speech recognition, multimodal reasoning, and speech synthesis entirely on-device with **zero reliance on cloud computation or smartphone-tethered neural inference** (target architecture under active empirical validation, pending complete physical hardware measurement).

Unlike commercial smart glasses (e.g., Meta Ray-Ban, Amazon Echo Frames) that act as tethered peripheral microphones uploading private first-person telemetry to remote hyperscale clouds, FRIDAY aims to compute neural tokens natively on the wearer's face, delivering instantaneous response, unbroken offline availability, and absolute privacy once hardware deployment gates are fully met.

```
                           +-------------------------------------------------------------+
                           |              Front Frame Assembly (31.3g)                   |
                           |  - Front PA12 Frame (12.0g) + High-Index 1.67 Lenses (8.5g) |
                           |  - Titanium Grade 5 Kinematic Camera Skeleton + Lens (3.0g) |
                           |  - Sony IMX415 4K CMOS (6° Downward Tilt + NTC Sensor)      |
                           |  - Dual Front-Right MEMS Mics (15mm Isolated Star-GND, 0.8g)|
                           |  - Spring Hinges & Inserts (3.0g) + Nose Pads/Brackets(1.8g)|
                           |  - Continuous Rigid-Flex Hinge Bridges (2.2g)               |
                           +------------------------------+------------------------------+
                                                          |
                      +-----------------------------------+-----------------------------------+
                      | Left-to-Bridge Flex (18 Conductors):|                                   | Right Hinge Flex (34 Conductors):
                      | - 2x Dedicated 2S Pack (PACK+/-)    |                                   | - 6x 2-Lane MIPI CSI-2 (100Ω Hatched)
                      | - 1x Series Midpoint (CELL_MID)     |                                   | - 2x Camera I2C Control (CAM_SCL/SDA)
                      | - 1x Kelvin MID Sense Line          |                                   | - 2x Camera Control (CAM_MCLK, RST_N)
                      | - 1x Active Balance Bleed Tap       |                                   | - 2x Camera Regulated Power (2.9V, 1.8V)
                      | - 2x Charger I2C Bus (SCL, SDA)     |                                   | - 1x Camera Cradle NTC Thermistor
                      | - 1x Charger INT/STAT Line          |                                   | - 4x Dual MEMS Mic Bus (VDD, BCLK, LR, DATA)
                      | - 1x Hardware CD Interlock Line     |                                   | - 1x Microphone Star-GND Return
                      | - 1x Cell 2 NTC Line (To BQ TS pin) |                                   | - 2x Dedicated 2S Pack (PACK+/-)
                      | - 4x Left Audio Digital I2S Bus     |                                   | - 1x Series Midpoint (CELL_MID)
                      |    (BCLK, LRCLK, DATA_L, SD_MODE_L) |                                   | - 1x Kelvin MID Sense Line
                      | - 1x Auxiliary 1.8V Bootstrapping   |                                   | - 1x Active Balance Bleed Tap
                      | - 2x Isolated DGND & Shield Return  |                                   | - 2x Charger I2C Bus (SCL, SDA)
                      | [Sum = Exactly 18 Conductors]       |                                   | - 1x Charger INT/STAT Line
                      |                                     |                                   | - 1x Hardware CD Interlock Line
                      |                                     |                                   | - 1x Cell 2 NTC Line (From Cell 2 to TS)
                      |                                     |                                   | - 4x Left Audio Bus (BCLK, LRCLK, DATA_L, SD_MODE_L)
                      |                                     |                                   | - 1x Auxiliary 1.8V Bootstrapping Line
+---------------------v---------------------------+   | [Sum = Exactly 34 Conductors]       |
|  Left Temple: Power Subsystem (30.6g)           |   +-------------------------------------v---------------+
|  - Left PA12 Temple Chassis (7.2g)              |   | Right Temple: Compute Subsystem (44.7g)             |
|  - Cell 1: 3.7V 300mAh LiPo (11.5g) + NTC 1     |   | - Right PA12 Temple Chassis (7.2g)                  |
|  - TI BQ25887 2S Boost Charger + Rails (3.7g)   |   | - Rockchip RK3576 Core SoM (11.8g)                  |
|  - TI BQ28Z610 2S Secondary Protector (1.2g)    |   | - Right Carrier PCB + 2S Buck-Boost (1.9g)          |
|  - Auxiliary 5V-to-1.8V LDO Boot Circuit (0.8g) |   | - Wi-Fi/BT 5.2 Murata 1XK Combo SiP Module (0.8g)   |
|  - MAX98357A Left Amp & Speaker Driver (4.8g)   |   | - Cell 2: 3.7V 300mAh LiPo (Series 2S, 11.5g) + NTC2|
|  - 4-Pin Magnetic Pogo Dock (5V/3A, 1.4g)       |   | - Right Protection Board & Balance Tap (1.2g)       |
|                                                 |   | - Thermal Assembly: 4.0g PCM + 1.5g Al Spreader(5.5g|
|                                                 |   | - Ambiq Apollo4 Lite Coprocessor & Audio Mux (1.1g) |
|                                                 |   | - Capacitive Touch Ribbon & Hall Switch (0.7g)      |
|                                                 |   | - MAX98357A Right Amp & Speaker Driver (3.0g)       |
+-------------------------------------------------+   +-----------------------------------------------------+
    [ Distributed Shielding & Solder: 2.9g | Contingency: 5.5g | TOTAL ALL-UP WEIGHT: Exactly 115.0g ]
```

---

## 2. Directory Layout & Organization

```
Friday/
├── README.md                                  # Executive Overview & Repository Guide
├── plan.md -> docs/plan.md                    # Root symlink to Systems Master Plan (v9.1.0)
├── Project_Specification_Report.docx          # Root symlink to Official Academic Word Report
├── Project_Specification_Report.md            # Root symlink to Systems PRD Markdown Report
│
├── docs/                                      # Master Documentation & Academic Submissions
│   ├── Project_Specification_Report.docx     # Formal Institutional Word report (NMIMS template)
│   ├── Project_Specification_Report.md       # Complete 9-Section Capstone Systems PRD
│   ├── plan.md                               # Systems Engineering Master Plan (v9.1.0)
│   └── hardware_bom.md                       # Itemized student vs industrial BOM (Robu.in / JLCPCB)
│
├── scripts/                                   # Automation, Build & Regression Audit Engines
│   ├── verify_architecture_math.py            # Automated audit checking all formulas, pin counts & thermals
│   └── build_spec_report.py                   # Programmatic python-docx compiler for institutional submission
│
├── phase1_ai_sandbox/                         # Phase 1: Local Mac M4 PyTorch Distillation Sandbox
│   ├── README.md                              # Phase 1 execution guide & mathematical proofs
│   ├── configs/
│   │   ├── model_config.json                  # Model hyper-parameters & bandwidth contract
│   │   └── vocab_subset_spec.json             # 64,000-token subset pruning policy
│   └── src/
│       ├── __init__.py
│       ├── distillation_loss.py               # Normalized, Epsilon-Smoothed Top-64 Forward KD Loss
│       ├── student_vlm.py                     # SigLIP-B + 2x2 Spatial Unshuffle (144 tokens) + Qwen VLM
│       └── tokenizer_vocab_pruner.py          # Tokenizer vocabulary pruning engine
│
├── phase2_benchtop_rig/                       # Phase 2: Embedded Bring-Up & Dev Rig
│   ├── README.md                              # Benchtop dev rig instructions & wiring guide
│   └── pinouts/
│       └── hinge_harness_pinout.csv           # Complete netlist for 18C Left and 34C Right flexes
│
├── teardown_analysis/                         # Ray-Ban Meta Hardware Teardown & Inspiration Study
│   ├── meta_rayban_teardown_analysis.md       # Comparative engineering report & hardware lessons
│   ├── transcription.md                       # Full 186-line timestamped video transcription
│   └── frames/                                # 14 high-resolution 1080p extracted hardware frames
│
└── assets/                                    # Hardware block diagrams, schematics & 3D models
```

---

## 3. Commercial Benchmark & Teardown Inspiration (Ray-Ban Meta Gen 2)

To inform our mechanical, thermal, and optomechanical architecture, we conducted an empirical teardown analysis of the commercial gold standard: the **Ray-Ban Meta Smart Glasses (Gen 2 Headliner/Wayfarer)**.

* **Full Comparative Report:** [`teardown_analysis/meta_rayban_teardown_analysis.md`](file:///Users/krish/NMIMS/Friday/teardown_analysis/meta_rayban_teardown_analysis.md)
* **Complete Timestamped Transcript:** [`teardown_analysis/transcription.md`](file:///Users/krish/NMIMS/Friday/teardown_analysis/transcription.md)
* **14 Extracted 1080p Frames:** [`teardown_analysis/frames/`](file:///Users/krish/NMIMS/Friday/teardown_analysis/frames/)

### Key Adopted Innovations for Project FRIDAY:
1. **CNC Aluminum Hinge Bridges:** Meta channels its delicate flex through precision metal hinge blocks rather than bending over raw plastic. FRIDAY implements internal filleted guide channels ($R \ge 3.0\text{ mm}$) at both hinges to prevent cable fatigue.
2. **Nose-Pad Microphone Placement:** Meta embeds a primary MEMS microphone directly into the nasal bracket, achieving optimal vocal pickup near the mouth while leveraging the frame to block temple speaker spillover.
3. **Dual Thermal Compounds:** Meta combines high-conductivity green TIM on the silicon die with black gap-fillers to the outer chassis. FRIDAY pairs direct copper die shims with our **$4.0\text{g}$ PureTemp 40 PCM pad ($600\text{ J}$ latent heat buffer)**.
4. **Where FRIDAY Surpasses Meta:** Meta's tiny single-cell **$154\text{ mAh}$ (0.59 Wh)** battery in one temple forces reliance on cloud offload. FRIDAY deploys balanced **Series 2S dual cells (two 300 mAh cells in series = 300 mAh @ 7.4V nominal, 2.22 Wh total, 600 mAh 1S equivalent)**—delivering **$3.76\times$ the energy** of Meta's cell and halving through-bridge current to run 100% sovereign on-device VLM neural inference.

---

## 4. The Five Non-Negotiable Directives

1. **Directive 01 (Zero External Battery Packs):** Power delivery network and dual LiPo cells are 100% enclosed within the left and right temple arms. No external battery packs, neckbands, or tethered pucks.
2. **Directive 02 (Zero Phone-in-the-Loop AI Inference):** The smartphone never executes neural inference. All STT, vision feature extraction, VLM decoding, and TTS execute locally on the glasses silicon.
3. **Directive 03 (Dedicated Bluetooth Role):** Bluetooth (Bluetooth 5.2 / BT Classic Audio via Murata 1XK / NXP IW416) is restricted strictly to peripheral audio profiles (HFP/A2DP) and fallback internet modem tethering. Never used for cloud AI offload.
4. **Directive 04 (Tiered Connectivity & Graceful Fallback):** Direct Wi-Fi $\to$ Phone Bluetooth PAN modem proxy $\to$ audible offline spoken notice.
5. **Directive 05 (Total Mass Envelope $\le 125\text{g}$):** All-up mass is strictly capped at $125.0\text{g}$ (audited total: **$115.0\text{g}$**), with center of gravity balanced across the ear-temple axis.

---

## 4. Key Engineering Invariants (v9.1.0 Verified)

| Architectural Parameter | Audited Value | Physical / Electrical Basis |
| :--- | :--- | :--- |
| **All-Up Weight (AUW)** | **115.0 grams** | 25 physical items ($109.5\text{g}$) + $5.5\text{g}$ contingency ($4.78\%$). $10.0\text{g}$ below limit. |
| **Harness Conductors** | **18 Left / 34 Right** | Dedicated `PACK+` and `PACK-` power rails isolating DC load current from signal ground. |
| **MAX98357A Biasing** | **Left: $1.62\text{V}$ / Right: $0.99\text{V}$** | Compensates internal $100\text{ k}\Omega$ pulldown: $10\text{k}\Omega$ pullup (Left) and $82\text{k}\Omega$ pullup (Right). |
| **Coprocessor Supply** | **1.8V LDO (`VAUX_1V8`)** | Safely operates Apollo4 Lite within its $1.71\text{V}\text{--}2.2\text{V}$ operating envelope. |
| **Watchdog Coordination** | **$1.0\text{s}$ MCU WDT** | Hardware WDT forces MCU reset on hang, releasing `CD` to float HIGH to terminate charging. |
| **Memory Bandwidth** | **5.77 GB/s (25 tok/s contract, 8.07 GB/s burst)** | Primary all-INT4 packed artifact ($230.61\text{ MB/token}$, $45.0\%$ headroom below $10.50\text{ GB/s}$ safe ceiling; fallback $6.39\text{--}8.95\text{ GB/s}$). |
| **Visual Token Count** | **Strictly 144 tokens** | $2\times 2$ pixel-unshuffle downsampling reduces 576 patches to 144 tokens ($75\%$ sequence cut). |
| **Literal OCR Pipeline** | **PP-OCRv6 (RapidOCR 3.10.0)** | PP-OCRv6 small det/rec models; earlier OCR benchmark numbers used the old PP-OCRv4 engine and are not comparable. |
| **Thermal Contract** | **$t_{\text{cool}} \ge 100\text{s}$ at $28^\circ\text{C}$** | $4.0\text{g}$ PCM pad ($600\text{ J}$ latent buffer) absorbs $31.44\text{ J}$ burst. Skin contact $\le 37.5^\circ\text{C}$. |
| **Zero-Waste Student Budget** | **₹9,795 INR (~$117 USD)** | Phase 1 runs at **₹0** on M4 Mac; single-shot procurement of final wearable hardware only (strictly under ₹10,000 cap). |

---

## 5. Quickstart & Verification Commands

All self-tests and build scripts can be run directly from the workspace:

```bash
# 1. Run the Full Architectural Mathematical & Hardware Regression Audit
python3 scripts/verify_architecture_math.py

# 2. Run the Phase 1 Distillation Loss Unit Test
python3 phase1_ai_sandbox/src/distillation_loss.py

# 3. Run the Phase 1 Student VLM & Spatial Unshuffle Unit Test
python3 phase1_ai_sandbox/src/student_vlm.py

# 4. Generate the 64,000-Token Subset Pruning Policy
python3 phase1_ai_sandbox/src/tokenizer_vocab_pruner.py

# 5. Re-compile the Institutional Word (.docx) Specification Report
python3 scripts/build_spec_report.py
```
