# PROJECT FRIDAY: LEAN STUDENT FINANCIAL MATRIX & HARDWARE BOM
## Systems Architecture v9.1.0 – Zero-Waste Student Financial Sourcing Guide

This document defines the exact financial decision framework and itemized component procurement plan for Project FRIDAY. It is engineered specifically for an undergraduate student budget, enforcing a **strict zero-waste rule**: **No intermediate development boards, no throwaway test hardware, and ₹0 spent until the software and AI are empirically proven.**

---

## 1. The ₹0 Zero-Risk Phase: What You Already Own

Before spending a single rupee of your own money, the entire core intelligence, speech processing, audio echo-cancellation, and peripheral communication can be developed and validated using hardware already in your possession:

| Asset Already in Hand | Hardware Specifications | Role in Project FRIDAY | Out-of-Pocket Cost |
| :--- | :--- | :--- | :---: |
| **MacBook Air 15" M4** | Apple M4, 16 GB Unified Memory, 120 GB/s bus, 16-Core Neural Engine | **Phase 1 AI Distillation Sandbox:** Runs student VLM, 64k token vocabulary pruning, 2×2 spatial unshuffle, INT4 quantization simulation, speech-to-text (Whisper.cpp), and TTS (Piper) on webcam/phone video feed. | **₹0** |
| **Free Cloud Compute** | Google Colab (Free T4 GPU) & Kaggle (Free 30 hrs/wk Dual T4 GPUs) | **Model Training & Loss Distillation:** Bounded forward-KL divergence training and Sequence DPO on synthetic first-person QA pairs. | **₹0** |
| **Raspberry Pi 3B** | Quad Cortex-A53 @ 1.2 GHz, 1 GB LPDDR2, 40-pin GPIO (I2S, I2C, SPI) | **Peripheral & Audio Bring-Up Testbed:** Hardware I2S interface (`GPIO 18, 19, 21`) to test MAX98357A audio amps, INMP441 MEMS microphone arrays, and WebRTC AEC3 echo cancellation without buying an expensive SBC. | **₹0** |
| **Personal Eyewear Lenses** | High-Index Prescription / Plano Lenses | **Optomechanical Integration:** Repurposed into 3D-printed front frame eyewire bezels, saving ₹3,500+ in lab-cut optical glass. | **₹0** |
| **TOTAL INITIAL CASH OUTLAY** | — | **Full AI & Software Simulation Validated** | **₹0 INR** |

---

## 2. The Financial Gate: Go / No-Go Decision Rule

```
                                      START
                                        │
                                        ▼
                  PHASE 1: Zero-Rupee Sandbox on MacBook Air M4
                  - Run 64k tokenizer vocabulary pruner
                  - Run 2x2 spatial downsampler (144 tokens)
                  - Benchmark student 0.5B VLM on webcam feed (OCR & scene QA)
                  - Validate WebRTC AEC3 audio loop on Raspberry Pi 3B
                                        │
                                        ▼
                     [ IS THE DISTILLED VLM ACTUALLY USEFUL? ]
                     (Accurate close-up text reading & <1.5s latency)
                                        │
                         ┌──────────────┴──────────────┐
                         │ NO                          │ YES
                         ▼                             ▼
                 [ ABORT PROJECT ]             [ HARDWARE PROCUREMENT ]
             Total Spent: Exactly ₹0       Proceed to Single-Shot Order:
             No drawer regret.             Buy ONLY the wearable hardware
             No wasted scholarship.        (₹7,800 – ₹9,200 INR total).
```

---

## 3. The Lean "Single-Shot" Wearable Hardware BOM (Track 1 Thick-Temple Wearable)

If and only if Phase 1 passes the zero-rupee gate, procurement is executed in a **single lean batch**. Every component listed below is installed **directly onto the wearable prototype** that you will wear on your face and defend in front of the NMIMS evaluation committee (satisfying Directive 01: all compute, sensors, and power contained within the eyewear frame). Zero intermediate throwaway hardware.

| Component / Subassembly | Specific Target Part | Purpose in Wearable | Qty | Unit Price (INR) | Total (INR) | Verified Sourcing Channel |
| :--- | :--- | :--- | :---: | :---: | :---: | :--- |
| **Compute Core Module** | Luckfox Core3576 / Omni3576 Compact SoM (RK3576, 6 TOPS NPU, **4GB LPDDR4x**) | Primary on-device AI inference engine mounted inside the 20mm right temple enclosure (40mm x 40mm compact SoM form factor). | 1 | ₹5,500 | ₹5,500 | Robu.in / ElectronicsComp |
| **Camera Sensor Module** | Sony IMX415 (or GC4653/OV5648) MIPI CSI-2 Module | 4K / 1080p wide-FOV camera mounted in center bridge ($6^\circ$ down-pitch). | 1 | ₹1,650 | ₹1,650 | Robu.in / ElectronicsComp |
| **MEMS Microphones** | INMP441 Omnidirectional Digital I2S MEMS Breakouts | Dual front-right beamforming microphone array for voice queries. | 2 | ₹150 | ₹300 | Robu.in |
| **Audio Amplifiers** | MAX98357A I2S Mono 3.2W Class-D Amplifiers | Dual mono audio amps (one per temple) with resistor-coupled SD_MODE channel select. | 2 | ₹120 | ₹240 | Robu.in |
| **Speaker Transducers** | 8Ω 1W Micro Bone-Conduction / Directional Transducers | Ear-canal directed audio drivers integrated into temple tips. | 2 | ₹150 | ₹300 | Robu.in / Amazon.in |
| **LiPo Battery Cells** | 3.7V 300mAh – 350mAh High-Drain LiPo Pouch Cells | Series 2S configuration ($7.4\text{V}$ nominal, 1 cell per temple arm). | 2 | ₹175 | ₹350 | Robu.in |
| **2S Boost Charger** | IP2326 Type-C 2S Boost Charger Module ($R_{ISET}$ set for 300mA 1C charge) | Boosts 5V USB to 8.4V with safe 300mA charge current (configured via sense resistor). | 1 | ₹95 | ₹95 | Robu.in / Amazon.in |
| **2S Battery Protection** | 2S 3A Li-ion / LiPo BMS Protection Board | Overcharge (4.25V/cell), overdischarge (2.8V/cell), and short-circuit protection. | 1 | ₹45 | ₹45 | Robu.in |
| **2S-to-5V System Buck** | MP1584EN / Mini DC-DC Synchronous Step-Down Buck Module | Efficiently drops 2S battery pack (6.0V–8.4V) to regulated 5.0V @ 2A for RK3576 SoM rail. | 1 | ₹70 | ₹70 | Robu.in |
| **User Interaction** | TTP223 Capacitive Touch Sensor / Tactile Micro-Switch | Touch trigger on right temple arm to start queries and control audio. | 1 | ₹25 | ₹25 | Robu.in |
| **3D Frame Fabrication** | Black PETG Filament (0.12mm layer height, 100% infill) | 3D-printed front frame and thick temple arms ($75^\circ\text{C}$ heat resistant, ~60g). | 1 | ₹300 | ₹300 | NMIMS FabLab / Local Print Lab |
| **Carrier Interconnect** | Standard 2-Layer FR4 Breakout PCBs (Batch of 5) | Left & Right temple breakout boards routing power and audio signals. | 1 | ₹350 | ₹350 | JLCPCB / Robu PCB |
| **Harness & Wiring** | 0.5mm FFC Ribbon Cables + 30 AWG Silicone Wire | Through-bridge hinge wiring (power pairs doubled for $<0.03\,\Omega$). | 1 | ₹120 | ₹120 | Robu.in |
| **Thermal Dissipation** | 0.3mm Copper Shim + Arctic MX-4 Thermal Paste | Conductive heat spreader sinking RK3576 junction heat to exterior frame. | 1 | ₹150 | ₹150 | Amazon.in |
| **Contingency Buffer** | Fasteners, Kapton tape, flux, heatshrink | Assembly hardware and prototyping buffer. | 1 | ₹300 | ₹300 | Local Hardware Store |
| **TOTAL WEARABLE SPEND** | — | **Complete, Untethered Autonomous Glasses** | — | — | **₹9,795 INR** | ~$117 USD (Strictly under ₹10,000 Cap) |

---

## 4. Comparison: The Expensive Path vs. The Lean Student Path

| Engineering Dimension | Traditional / Throwaway Path | Lean Zero-Waste Path (Project FRIDAY) | Student Savings |
| :--- | :--- | :--- | :--- |
| **Phase 1 Exploration** | Buy Orange Pi 5 just to test ($₹12,500$) | 100% on MacBook Air M4 + Free Kaggle/Colab | **Save ₹12,500** |
| **Audio & Peripheral Testing** | Buy auxiliary test rigs ($₹3,000$) | Repurpose owned Raspberry Pi 3B | **Save ₹3,000** |
| **Optical Lenses** | Custom optical lab cutting ($₹3,500$) | Reuse existing glasses lenses ($₹0$) | **Save ₹3,500** |
| **Frame Material** | Industrial SLS Nylon PA12 ($₹8,000$) | Local FDM PETG 3D printing ($₹350$) | **Save ₹7,650** |
| **PCB Prototyping** | 10-layer custom rigid-flex ($₹45,000$) | 2-layer FR4 + 0.5mm FFC ribbons ($₹600$) | **Save ₹44,400** |
| **Drawer Waste** | 2–3 boards sitting unused forever | **Zero items in drawer; 100% on the wearable** | **Priceless** |
| **NET PROJECT COST** | **₹72,000+ INR** | **₹9,795 INR total (Ceiling: ₹10,000)** | **86.4% Total Savings** |

---

## 5. Local Vendor Directory (Mumbai / Online Delivery)

1. **[Robu.in](https://robu.in):** Best for INMP441 microphones, MAX98357A amplifiers, LiPo cells, IP2326 boost chargers, and FFC ribbon cables. Standard delivery to Mumbai within 48–72 hours.
2. **[Robocraze](https://robocraze.com) / [ElectronicsComp](https://electronicscomp.com):** Fast backup for camera modules, jumper wires, silicon cables, and breakout boards.
3. **[JLCPCB](https://jlcpcb.com):** Cheapest 2-layer FR4 boards ($2 USD for 5 boards + shipping).
4. **Local 3D Print Vendors (Lamington Road / Vile Parle / College Lab):** Cost for printing PETG frame parts is typically ₹3 to ₹5 per gram (~₹300 to ₹400 total).
