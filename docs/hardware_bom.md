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

| Component / Subassembly | Specific Target Part | Purpose in Wearable | Qty | Unit Price (INR) | Total (INR) | Verified Sourcing Channel & Direct URL |
| :--- | :--- | :--- | :---: | :---: | :---: | :--- |
| **Compute Core Module** | **Firefly CAM-3576Q38** (Rockchip RK3576, 6.0 TOPS NPU, **4GB LPDDR4x**, onboard Wi-Fi 6 + BT 5.4, 38×38×11.5 mm, 14.2g, 40-pin 0.5mm FPC MIPI-CSI camera connector) | Primary on-device AI inference engine mounted inside the 20mm right temple enclosure. Integrated dual-band Wi-Fi 6 + Bluetooth 5.4 directly enables Directives 03, 04, and Milestone 4.2 without USB dongles. | 1 | ₹5,400 | ₹5,400 | [Firefly Store / ThinkRobotics / Evelta](https://www.firefly.store) |
| **Camera Sensor Module** | **Sony IMX219 / OV5647 160° Wide-Angle** MIPI CSI Camera Module (with 40-pin/15-pin 0.5mm FPC cable) | Optical input mounted in center bridge with $6^\circ$ down-pitch, plugging directly into the CAM-3576Q38 onboard MIPI connector. | 1 | ₹1,450 | ₹1,450 | [Robu.in IMX219 Wide-Angle](https://robu.in/product/raspberry-pi-camera-module-v2-8mp-imx219-sensor/) |
| **MEMS Microphones** | **INMP441 Omnidirectional Digital I2S MEMS** Breakouts | Dual front-right beamforming microphone array for voice queries and spatial audio capture. | 2 | ₹145 | ₹290 | [Robu.in INMP441 Module](https://robu.in/product/inmp441-omnidirectional-microphone-module-i2s-interface/) |
| **Audio Amplifiers** | **MAX98357A I2S Mono 3.2W Class-D** Breakout Modules | Dual mono audio amps (one per temple) with resistor-coupled SD_MODE channel select ($10\text{ k}\Omega$ Left, $220\text{ k}\Omega$ Right against internal $100\text{ k}\Omega$ pulldown). | 2 | ₹125 | ₹250 | [Robu.in MAX98357A Amp](https://robu.in/product/max98357a-i2s-3w-class-d-amplifier-interface-audio-dac-module/) |
| **Speaker Transducers** | **8Ω 1W Micro Bone-Conduction / Directional** Transducers | Ear-canal directed audio drivers integrated into temple tips for private speech feedback. | 2 | ₹150 | ₹300 | [Robu.in 8Ω 1W Transducer](https://robu.in/product/bone-conduction-speaker-transducer-8-ohm-1w/) |
| **LiPo Battery Cells** | **GNB / Tattu 3.7V 300mAh 30C/60C High-Discharge** LiPo Pouch Cells | Series 2S configuration ($7.4\text{V}$ nominal, 1 cell per temple arm, 16.0g total). 30C continuous discharge rating (9.0A capability) easily supplies the 1.85A (6.2C) peak board surge at 6.0V cutoff with zero voltage sag. | 2 | ₹190 | ₹380 | [Robu.in GNB 300mAh 30C LiPo](https://robu.in/product/gao-neng-gnb-300mah-1s-30c-lipo-battery/) |
| **2S Boost Charger** | **IP2326 Type-C 2S Boost Charger Module** ($R_{ISET}$ sense resistor modified to $0.33\,\Omega$ for 300mA 1C charge) | Boosts 5V USB-C to 8.4V. Charge current set to strictly 300mA via $R_{ISET} = 0.33\,\Omega$ sense resistor, verified via inline digital ammeter. | 1 | ₹110 | ₹110 | [Robu.in IP2326 2S Charger](https://robu.in/product/ip2326-type-c-2s-boost-charging-board/) |
| **2S Battery Protection & Balancing** | **2S 3A/5A LiPo BMS with Active Cell Balancing** (HY2212 balance IC, 4.20V ± 25mV balance threshold, 35mA bleed shunt) | Active cell balancing prevents series cell drift during charging; overcharge (4.25V/cell), overdischarge (2.8V/cell), and short-circuit protection. | 1 | ₹120 | ₹120 | [Robu.in 2S Balancing BMS](https://robu.in/product/2s-3a-bms-balance-protection-board/) |
| **2S-to-5V System Buck** | **MP2315 / MP2307 High-Efficiency Synchronous Step-Down Buck** Module (17×11×3.8 mm) | True synchronous buck with integrated High/Low-Side N-MOSFETs (95% efficiency, zero external Schottky catch diode drop), eliminating diode thermal buildup inside temple. | 1 | ₹95 | ₹95 | [Robu.in MP2315 Synchronous Buck](https://robu.in/product/mp2315-dc-dc-step-down-voltage-regulator-module-5v-3a/) |
| **User Interaction** | **TTP223 Capacitive Touch Sensor** Module | Capacitive touch trigger on right temple arm to start queries and control audio volume. | 1 | ₹25 | ₹25 | [Robu.in TTP223 Touch Module](https://robu.in/product/ttp223-touch-key-switch-module/) |
| **3D Frame Fabrication** | **Black PETG Filament** (0.12mm layer height, 100% infill) | 3D-printed front frame and thick temple arms ($75^\circ\text{C}$ heat deflection, 42.0g net frame mass). | 1 | ₹300 | ₹300 | [Robu.in PETG Filament](https://robu.in/product/petg-filament-1-75mm-black/) / NMIMS FabLab |
| **Carrier Interconnect** | **Standard 2-Layer FR4 Low-Speed Breakout PCBs** (Batch of 5) | Left & Right temple breakout boards routing low-speed I2S audio, power rails, and GPIO. High-speed MIPI stays entirely on the CAM-3576Q38 module. | 1 | ₹350 | ₹350 | [JLCPCB 2-Layer FR4 Batch](https://jlcpcb.com) / Robu PCB |
| **Harness & Wiring** | **0.5mm FPC Ribbon Jumpers + 30 AWG Ultra-flexible Silicone Wire** | Through-bridge hinge wiring (power pairs doubled for $R_{DC} < 0.030\,\Omega$). | 1 | ₹120 | ₹120 | [Robu.in 30 AWG Silicone Wire](https://robu.in/product/30-awg-flexible-silicone-wire/) |
| **Thermal Dissipation** | **0.3mm Copper Shim + Paraffin Phase-Change Wax (4.0g) + Arctic MX-4** | Conductive heat spreader sinking RK3576 junction heat into the 600 J PCM buffer and exterior frame. | 1 | ₹190 | ₹190 | [Amazon.in Copper Shim & Thermal Compound](https://www.amazon.in) |
| **Assembly Hardware & Contingency** | M1.6/M2 brass threaded heatset inserts, screws, Kapton tape | Mechanical fasteners and assembly prototyping buffer. | 1 | ₹215 | ₹215 | Local Hardware Store / Robu |
| **TOTAL WEARABLE SPEND** | — | **Complete, Untethered Autonomous Glasses** | — | — | **₹9,595 INR** | ~$115 USD (Strictly under ₹10,000 Cap, with ₹405 Headroom) |

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
