# PROJECT FRIDAY: HARDWARE BILL OF MATERIALS (BOM) & SOURCING MATRIX
## Systems Architecture v9.1.0 – Student Capstone vs. Industrial Prototyping

This document itemizes every physical component, development board, integrated circuit, and structural bracket required for Project FRIDAY, comparing the full-scale industrial quote against the optimized student capstone procurement path.

---

## 1. Summary Comparison

| Budget Tier | Target Environment | Total Estimated Spend (INR) | Approx. USD | Key Trade-Offs |
| :--- | :--- | :--- | :--- | :--- |
| **Industrial Prototype** | Custom Flex + SLS Nylon PA12 + Bare Silicon SoMs | ₹55,000 – ₹72,000 | ~$660 – $860 | High NRE tooling costs, 4-week PCB turnarounds. |
| **Student Capstone Hack** | FDM PETG + Standard 2-Layer FR4 + Robu.in / JLCPCB | **₹13,500 – ₹15,500** | **~$160 – $185** | Modular benchtop bring-up, fast iteration, zero tooling debt. |

---

## 2. Itemized Component Sourcing & Pricing Matrix

| Component / Subassembly | Industrial Production Spec | Student Capstone Hack | Qty | Unit Price (INR) | Total (INR) | Sourcing Channel |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Compute Core Board** | Custom RK3576 SoM + Rigid-Flex Carrier | Orange Pi 5 (RK3588S, 6 TOPS NPU) / Luckfox RK3576 | 1 | ₹7,800 | ₹7,800 | [Robu.in](https://robu.in) / Robocraze |
| **Camera Module** | Bare IMX415 sensor on polyimide flex | Sony IMX415 4K MIPI CSI-2 Module | 1 | ₹2,100 | ₹2,100 | Robu.in / Robocraze |
| **MEMS Microphones** | Custom Star-GND flex array | INMP441 / SPH0645 I2S MEMS Breakout | 2 | ₹180 | ₹360 | Robu.in |
| **Audio Amplifiers** | Integrated MAX98357A QFN ICs | MAX98357A I2S Mono 3.2W Breakouts | 2 | ₹150 | ₹300 | Robu.in |
| **Speaker Transducers** | Custom micro-directional exciters | Mini Bone Conduction Exciter / Mini Speaker (8Ω 1W) | 2 | ₹250 | ₹500 | Robu.in / Amazon.in |
| **Coprocessor Node** | Ambiq Apollo4 Lite BGA | RP2040 (Raspberry Pi Pico) / ESP32-S3 Mini | 1 | ₹400 | ₹400 | Robu.in |
| **Energy Storage Cells** | Custom 300mAh high-drain pouch cells | 3.7V 300mAh–400mAh LiPo Cells (Series 2S wired) | 2 | ₹250 | ₹500 | Robu.in |
| **Battery Charger** | TI BQ25887 IC + balance circuit | TP5100 2S 8.4V LiPo Charger Module (Benchtop) | 1 | ₹110 | ₹110 | Robu.in |
| **Frame Prototyping** | SLS 3D Printing in Nylon PA12 + Vapor Polish | FDM 3D Printing in Black PETG (0.12mm layer height) | 1 | ₹350 | ₹350 | College FabLab / 3D Print Lab |
| **Optical Lenses** | High-Index 1.67 Lab Cut Lenses | Reusing Personal Glasses Lenses / Plano Lenses | 1 pair | ₹0 | ₹0 | Self-Provided |
| **Carrier & Power PCB** | 4-layer rigid-flex with immersion gold | Batch of 5 Standard 2-Layer FR4 Boards | 1 batch | ₹750 | ₹750 | [JLCPCB](https://jlcpcb.com) / Robu PCB |
| **Harness Interconnect** | Micro-etched continuous polyimide flex | 0.5mm pitch FFC Flat Ribbon Cables + Enameled Wire | 1 set | ₹180 | ₹180 | Robu.in |
| **Thermal Assembly** | PureTemp 40 Composite PCM Pad + Graphite | Copper Shim (0.3mm) + Arctic MX-4 Thermal Paste | 1 set | ₹380 | ₹380 | Amazon.in |
| **TOTAL ESTIMATED HARDWARE BUDGET** | — | **Complete Benchtop & Wearable Rig** | — | — | **₹13,730 INR** | Fully within capstone budget |

---

## 3. Benchtop Prototyping Substitutions & Strategy

1. **Phase 1 (AI Distillation & Local Emulation):**
   * **Cost: ₹0.**
   * Runs 100% locally on your **MacBook Air 15" M4 (16 GB Unified Memory)** in PyTorch.
   * Emulates camera down-pitch, text cropping, token generation, and audio feedback on-device.

2. **Phase 2 (Benchtop Dev Rig):**
   * Procure the **Orange Pi 5** or **Luckfox RK3576**, **IMX415 camera**, **INMP441 mics**, and **MAX98357A amps**.
   * Mount them flat on an acrylic breadboard base to benchmark kernel boot, Linux `PREEMPT_RT` scheduling, NPU inference, and WebRTC AEC3 audio pipeline before locking mechanical constraints.

3. **Phase 3 (Physical Integration & Wearable Prototype):**
   * Export frame STL models from Autodesk Fusion 360 and print on FDM in **PETG** (superior impact resistance and thermal stability up to $75^\circ\text{C}$ compared to PLA).
   * Assemble carrier boards using JLCPCB 2-layer FR4 boards and FFC ribbon interconnects.
