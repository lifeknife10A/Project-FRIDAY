# PROJECT FRIDAY: LEAN STUDENT FINANCIAL MATRIX & HARDWARE BOM
## Systems Architecture v9.2.0 – Clean Itemized Procurement & Sourcing Guide

This document defines the exact financial decision framework and itemized component procurement plan for Project FRIDAY. It is engineered specifically for an undergraduate student budget, enforcing a **strict zero-waste rule**: **No intermediate development boards, no throwaway test hardware, and ₹0 spent until the software and AI are empirically proven.**

---

## 1. The ₹0 Zero-Risk Phase: What You Already Own

Before spending a single rupee of your own money, the entire core intelligence, speech processing, audio echo-cancellation, and peripheral communication can be developed and validated using hardware already in your possession:

| Asset Already in Hand | Hardware Specifications | Role in Project FRIDAY | Out-of-Pocket Cost |
| :--- | :--- | :--- | :---: |
| **MacBook Air 15" M4** | Apple M4, 16 GB Unified Memory, 120 GB/s bus, 16-Core Neural Engine | **Phase 1 AI Distillation Sandbox:** Runs student VLM, 64k token vocabulary pruning, 2x2 spatial unshuffle, INT4 quantization simulation, speech-to-text (Whisper.cpp), and TTS (Piper) on webcam/phone video feed. | **₹0** |
| **Free Cloud Compute** | Google Colab (Free T4 GPU) & Kaggle (Free 30 hrs/wk Dual T4 GPUs) | **Model Training & Loss Distillation:** Bounded forward-KL divergence training and Sequence DPO on synthetic first-person QA pairs. | **₹0** |
| **Raspberry Pi 3B** | Quad Cortex-A53 @ 1.2 GHz, 1 GB LPDDR2, 40-pin GPIO (I2S, I2C, SPI) | **Peripheral & Audio Bring-Up Testbed:** Hardware I2S interface (GPIO 18, 19, 21) to test MAX98357A audio amps, INMP441 MEMS microphone arrays, and WebRTC AEC3 echo cancellation without buying an expensive SBC. | **₹0** |
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
             No drawer regret.             Buy ONLY the wearable hardware.
             No wasted scholarship.
```

---

## 3. Itemized Wearable Hardware BOM (Track 1 Thick-Temple Architecture)

If and only if Phase 1 passes the zero-rupee gate, procurement is executed in clean batches. Every component listed below is installed **directly onto the wearable prototype** that fits inside the glasses frame (satisfying Directive 01: 100% on-device compute, zero pocket pucks).

### A. Compute & Power Silicon (LCSC Locked Cart: Cart_20261126110756)

| # | Item Description | Part # / MPN | Package | Qty | Unit Price (USD) | Line Total (INR) | Sourcing Channel |
|---|---|---|---|:---:|:---:|:---:|---|
| 1 | **Rockchip RK3576 SoC**<br>8-Core (4x A72 + 4x A53), 6-TOPS INT4/INT8 NPU | C42388007<br>`RK3576` | FCCSP-698L<br>(16.1 x 17.2 mm) | 1 | $22.33 | ₹1,880 | [LCSC Electronics](https://lcsc.com) |
| 2 | **Rockchip RK806-1 PMIC**<br>Companion multi-rail power management IC | C5156483<br>`RK806-1` | QFN-68<br>(7 x 7 mm) | 1 | $3.97 | ₹335 | [LCSC Electronics](https://lcsc.com) |
| 3 | **Realtek RTL8723DS Wi-Fi / BT**<br>2.4 GHz 802.11b/g/n + Bluetooth 4.2 | C2762334<br>`RTL8723DS-CG` | WQFN-48<br>(6 x 6 mm) | 1 | $2.22 | ₹187 | [LCSC Electronics](https://lcsc.com) |
| 4 | **24.000 MHz Master Crystal**<br>Main system clock for RK3576 (12pF, 10ppm) | C70590<br>`X322524MOB4SI` | SMD-3225-4P<br>(3.2 x 2.5 mm) | 5 | $0.086 | ₹36 | [LCSC Electronics](https://lcsc.com) |
| 5 | **32.768 kHz RTC Sleep Crystal**<br>Real-time clock for RK806-1 sleep states | C32346<br>`Q13FC13500004` | SMD-3215-2P<br>(3.2 x 1.5 mm) | 5 | $0.151 | ₹63 | [LCSC Electronics](https://lcsc.com) |
| 6 | **USB Type-C 16-Pin Receptacle**<br>5V power input, firmware flashing, ADB debug | C165948<br>`TYPE-C-31-M-12` | 16-Pin SMD | 5 | $0.174 | ₹73 | [LCSC Electronics](https://lcsc.com) |
| 7 | **MaskROM Recovery Key Switch**<br>Micro tactile button for fastboot flashing | C318884<br>`TS-1187A-B-A-B` | SMD (3 x 4 mm) | 20 | $0.020 | ₹34 | [LCSC Electronics](https://lcsc.com) |
| 8 | **LCSC International Shipping**<br>Singapore Post airmail (includes $3 coupon) | Logistics | Tracked Air | 1 | $2.72 | ₹230 | LCSC Direct |
| — | **LCSC Silicon Subtotal** | — | — | **39 pcs** | **$33.69** | **₹2,838** | Locked Cart Total |

---

### B. Memory, Storage & Electronics Passives

| # | Item Description | Specification / Role | Qty | Unit Price (INR) | Total (INR) | Sourcing Channel |
|---|---|---|:---:|:---:|:---:|---|
| 9 | **Samsung 4GB LPDDR4X + 64GB eMMC eMCP**<br>(Samsung KM3V series or equivalent) | Single BGA-254 chip combining 4GB RAM + 64GB fast storage. Harvested from scrap Redmi 9 / POCO M2 donor motherboard + technician BGA reballing. | 1 | ₹1,000 | ₹1,000 | Local Mobile Repair / Donor Scrap Board |
| 10 | **SMD Passives & PMIC Power Circuit Kit**<br>(Itemized component matrix detailed below) | Complete set of 0402/0603 resistors, ceramic decoupling capacitors, PMIC shielded power inductors, and USB ESD TVS diodes. | 1 kit | ₹650 | ₹650 | LCSC Passives / Local Mumbai Electronics |
| — | **Memory & Passives Subtotal** | — | — | — | **₹1,650** | — |

---

### B.1 Itemized Passive Component Specification Matrix (Exact Ohms, Microfarads, Wattage & Ratings)

The table below defines every discrete passive component required on the custom PCB around the RK3576, RK806-1 PMIC, USB-C port, and audio peripherals:

#### 1. Resistors (SMD 0402, 1% Tolerance, 1/16 Watt / 62.5 mW)

| Resistance | Tolerance | Wattage / Rating | Package | Qty | Circuit Function & Target Nets |
|---|:---:|:---:|:---:|:---:|---|
| **5.1 kΩ** | ±1% | 1/16 W (62.5 mW) | SMD 0402 | 2 | **USB-C Port CC1 & CC2 Pull-Downs** (Mandatory for standard 5V/3A Power Delivery sink negotiation). |
| **2.2 kΩ** | ±1% | 1/16 W (62.5 mW) | SMD 0402 | 4 | **I2C Bus Pull-Ups** on `I2C_SDA` and `I2C_SCL` for RK806-1 PMIC control and Sony IMX708 camera sensor. |
| **10 kΩ** | ±1% | 1/16 W (62.5 mW) | SMD 0402 | 4 | **Pull-Up & Channel Select:** Left channel audio divider pull-up, INMP441 L/R select, and PMIC reset line. |
| **220 kΩ** | ±1% | 1/16 W (62.5 mW) | SMD 0402 | 1 | **Left Channel Audio Select Divider Pull-Down** on MAX98357A `SD_MODE` pin (sets 0.77V–1.39V window). |
| **100 kΩ** | ±1% | 1/16 W (62.5 mW) | SMD 0402 | 2 | **Audio Gain Programming** on MAX98357A `GAIN` pin to VDD (sets safe +3 dB lowest gain configuration). |
| **300 kΩ** | ±1% | 1/16 W (62.5 mW) | SMD 0402 | 1 | **IP2326 Battery Charge Rate Setting** on Pin 11 `ISET` (enforces strict 300 mA / 1C LiPo charge ceiling). |
| **22 Ω** | ±1% | 1/16 W (62.5 mW) | SMD 0402 | 2 | **Master Clock Series Damping** on 24.000 MHz crystal `OSC_OUT` pin to suppress clock harmonic ringing. |
| **0 Ω (Jumper)**| — | 1/16 W | SMD 0402 | 4 | Configuration links for RF antenna path tuning and optional audio ground isolation. |

#### 2. Capacitors (SMD Multilayer Ceramic Capacitors - MLCC)

| Capacitance | Voltage Rating | Dielectric | Package | Qty | Circuit Function & Target Nets |
|---|:---:|:---:|:---:|:---:|---|
| **12 pF** | 50 V | C0G / NP0 (Ultra-stable) | SMD 0402 | 2 | **24.000 MHz Master Crystal Load Caps** (`OSC_IN` / `OSC_OUT` to GND). |
| **12.5 pF** | 50 V | C0G / NP0 (Ultra-stable) | SMD 0402 | 2 | **32.768 kHz RTC Sleep Crystal Load Caps** on RK806-1 RTC oscillator inputs. |
| **100 nF (0.1 µF)**| 6.3 V / 10 V | X5R / X7R | SMD 0402 | 24 | **High-Frequency Decoupling Array:** Placed directly under RK3576 BGA balls and PMIC LDO pins. |
| **1.0 µF** | 10 V | X5R / X7R | SMD 0402 | 8 | **Mid-Frequency Rail Bypass** on PMIC LDO outputs (`VDD_1V8`, `VDD_0V9`, `AVDD_1V8`). |
| **4.7 µF** | 10 V | X5R / X7R | SMD 0603 | 4 | **Peripherals Power Smoothing** for IMX708 camera breakout and RTL8723DS Wi-Fi transceiver. |
| **10 µF** | 16 V / 25 V | X5R / X7R | SMD 0603 | 6 | **Bulk Input Filtering** on 5.0V system bus, USB-C VBUS, and MAX98357A audio power pins. |
| **22 µF** | 6.3 V / 10 V | X5R / X7R | SMD 0603 | 8 | **PMIC Buck Output Smoothing Filters** on `VDD_CPU`, `VDD_NPU`, `VDD_LOGIC`, and `VCC_DDR`. |

#### 3. Power Inductors & Protection Devices

| Component Type | Value / Rating | Current Rating (Isat) | Package | Qty | Circuit Function & Target Nets |
|---|:---:|:---:|:---:|:---:|---|
| **Shielded Power Inductor** | **0.47 µH** (DCR < 35 mΩ) | 4.5 A Saturation | SMD 2016 (2.0 x 1.6 mm) | 2 | **PMIC Buck 1 & Buck 2 Switching Nodes** (`VDD_CPU` and `VDD_NPU` high-current switching rails). |
| **Shielded Power Inductor** | **1.0 µH** (DCR < 50 mΩ) | 3.2 A Saturation | SMD 2016 (2.0 x 1.6 mm) | 2 | **PMIC Buck 3 & Buck 4 Switching Nodes** (`VDD_LOGIC` and `VCC_DDR` switching rails). |
| **Ferrite Bead** | 120 Ω @ 100 MHz (2.0 A) | 2.0 A Continuous | SMD 0603 | 2 | **High-Frequency Noise Choke** isolating analog audio power and RF Wi-Fi 3.3V rail. |
| **TVS ESD Protection Diode** | 5.0 V Clamp (Low Cap < 0.5pF) | 4-Channel Array | SOT-23-6 / DFN | 1 | **High-Speed USB-C ESD Protection** on D+, D-, CC1, CC2 lines (prevents human static shock damage). |

---

### C. Vision & Optics

| # | Item Description | Specification / Role | Qty | Unit Price (INR) | Total (INR) | Sourcing Channel |
|---|---|---|:---:|:---:|:---:|---|
| 11 | **Sony IMX708 Camera Sensor Assembly**<br>(Raspberry Pi Camera Module 3 SA31VA30P) | 11.9MP STARVIS 2 CMOS, hardware PDAF autofocus (10 cm to infinity), 1.40 µm pixel pitch, 10.8 x 10.8 mm bare sensor cube with 24 mm flex tail. | 1 | ₹1,800 | ₹1,800 | [Robu.in SA31VA30P](https://robu.in/product/raspberry-pi-camera-module-3-sa31va30p/) |
| 12 | **Front-Bridge Camera Breakout PCB**<br>(Miniature 14 x 12 mm custom board) | Sits behind nose bridge. Hosts 30-pin Hirose DF37 socket, AP3429K 1.1V buck regulator (prevents 1.32W LDO heat waste), 1.8V/2.8V LDOs, and 24MHz camera clock. | 1 | ₹350 | ₹350 | [JLCPCB 2-Layer](https://jlcpcb.com) / Robu PCB |
| 13 | **High-Index Eyewear Lenses** | Clear 1.67 high-index prescription / plano lenses repurposed from student eyewear. | 2 | ₹0 | ₹0 | Reused Personal Asset |
| — | **Vision & Optics Subtotal** | — | — | — | **₹2,150** | — |

---

### D. Audio & Acoustics

| # | Item Description | Specification / Role | Qty | Unit Price (INR) | Total (INR) | Sourcing Channel |
|---|---|---|:---:|:---:|:---:|---|
| 14 | **INMP441 Digital MEMS Microphones** | Omnidirectional I2S digital mic breakouts (front-right beamforming array for voice input and noise cancellation). | 2 | ₹145 | ₹290 | [Robu.in INMP441](https://robu.in/product/inmp441-omnidirectional-microphone-module-i2s-interface/) |
| 15 | **MAX98357A I2S Class-D Mono Amplifiers** | 3.2W Class-D mono amp breakouts (one per temple arm). Hardware-configured via SD_MODE resistor divider. | 2 | ₹125 | ₹250 | [Robu.in MAX98357A](https://robu.in/product/max98357a-i2s-3w-class-d-amplifier-interface-audio-dac-module/) |
| 16 | **1510 Micro Oval Dynamic Speakers** | 8 Ohm, 1W micro speakers (15 x 10 x 3.5 mm). Downward-firing directional acoustic chambers pointing at ear canals. | 2 | ₹55 | ₹110 | [Probots.co.in 1510 Speaker](https://probots.co.in) |
| — | **Audio & Acoustics Subtotal** | — | — | — | **₹650** | — |

---

### E. Battery & Power Delivery System

| # | Item Description | Specification / Role | Qty | Unit Price (INR) | Total (INR) | Sourcing Channel |
|---|---|---|:---:|:---:|:---:|---|
| 17 | **GNB 3.7V 300mAh 30C LiPo Cells** | High-discharge LiPo pouch cells connected in Series 2S (7.4V nominal, 1 cell per temple, 16.0g total). 9.0A burst rating handles peak surges with zero sag. | 2 | ₹190 | ₹380 | [Robu.in GNB 300mAh LiPo](https://robu.in/product/gao-neng-gnb-300mah-1s-30c-lipo-battery/) |
| 18 | **IP2326 Type-C 2S Boost Charger** | Boosts 5V USB-C to 8.4V. Pin 11 ISET resistor set to 300 kOhm to enforce safe 300mA (1C) charge rate. | 1 | ₹110 | ₹110 | [Robu.in IP2326 Charger](https://robu.in/product/ip2326-type-c-2s-boost-charging-board/) |
| 19 | **HY2212 2S BMS Protection & Balance Board** | Cell protection (4.25V overcharge, 2.8V overdischarge) with 35mA passive shunt-bleed cell balancing. | 1 | ₹120 | ₹120 | [Robu.in 2S BMS Board](https://robu.in/product/2s-3a-bms-balance-protection-board/) |
| 20 | **MP2315 High-Efficiency Step-Down Buck** | Synchronous 2S-to-5V step-down regulator (95% efficiency, 3A continuous). Provides clean 5.0V system power bus. | 1 | ₹95 | ₹95 | [Robu.in MP2315 Buck](https://robu.in/product/mp2315-dc-dc-step-down-voltage-regulator-module-5v-3a/) |
| 21 | **TTP223 Capacitive Touch Sensor** | Capacitive touch trigger on right temple arm to activate voice queries and adjust volume. | 1 | ₹25 | ₹25 | [Robu.in TTP223 Module](https://robu.in/product/ttp223-touch-key-switch-module/) |
| — | **Power System Subtotal** | — | — | — | **₹730** | — |

---

### F. Frame, Thermal & Mechanical Assembly

| # | Item Description | Specification / Role | Qty | Unit Price (INR) | Total (INR) | Sourcing Channel |
|---|---|---|:---:|:---:|:---:|---|
| 22 | **Numakers Pitch Black PETG Filament** | 1.75mm, 1 kg Spool, +/- 0.05 mm accuracy. Heat deflection 75°C, sweat/humidity resistant. Yields 40+ frame iterations. | 1 | ₹849 | ₹849 | [Amazon.in Numakers PETG](https://amzn.in/d/074Tf1Tx) |
| 23 | **Custom 0.8mm FR4 Carrier PCBs** | Left & right temple thin 2-layer breakout carriers routing I2S audio, power rails, and GPIO. | 1 set (5 pcs) | ₹350 | ₹350 | [JLCPCB 2-Layer](https://jlcpcb.com) / Robu PCB |
| 24 | **Wiring Harness & Interconnects** | 0.5mm FPC ribbon jumpers + 30 AWG ultra-flexible silicone wire for through-bridge routing. | 1 | ₹120 | ₹120 | [Robu.in 30 AWG Wire](https://robu.in/product/30-awg-flexible-silicone-wire/) |
| 25 | **Thermal Spreader & PCM Buffer** | 0.3mm copper shim + 4.0g Rubitherm RT42 phase-change material (660 J buffer) + 1.0mm silica aerogel blanket (skin barrier). | 1 | ₹350 | ₹350 | Amazon / Robu Aerogel |
| 26 | **Mechanical Hardware & Inserts** | M1.6 and M2 brass heatset threaded inserts, hinge screws, Kapton tape. | 1 | ₹215 | ₹215 | Local Hardware / Robu |
| — | **Mechanical & Thermal Subtotal** | — | — | — | **₹1,884** | — |

---

### G. Financial Grand Total Summary

| Procurement Category | Scope of Hardware Included | Subtotal (INR) | Subtotal (USD) |
|---|---|:---:|:---:|
| **A. Core Compute Silicon** | RK3576 SoC, RK806-1 PMIC, RTL8723DS, Crystals, USB-C, Switch + Shipping | ₹2,838 | $33.69 |
| **B. Memory & Passives** | Harvested eMCP (4GB RAM + 64GB eMMC) + 0402/0603 caps/resistors/inductors kit | ₹1,650 | $19.64 |
| **C. Vision & Optics** | IMX708 autofocus camera sensor + front-bridge regulator breakout PCB | ₹2,150 | $25.60 |
| **D. Audio & Acoustics** | Dual INMP441 mics + dual MAX98357A amps + dual 1510 directional speakers | ₹650 | $7.74 |
| **E. Power Delivery & Battery** | 2S LiPo cells, IP2326 boost charger, HY2212 BMS, MP2315 buck, touch sensor | ₹730 | $8.69 |
| **F. Frame, Thermal & Mechanics** | Numakers PETG 1kg spool, carrier PCBs, wiring harness, thermal shim, inserts | ₹1,884 | $22.43 |
| **GRAND TOTAL (All Wearable Components)** | **Complete Raw Hardware Bill (Directive 01 Untethered Smart Glasses)** | **₹9,902 INR** | **~$118 USD** |

> **Manufacturing Note:** The total above covers 100% of the raw silicon, electronic components, optics, battery, and 3D printing filament. Custom 6-layer HDI PCB bare-board fabrication and BGA assembly services are quoted separately based on JLCPCB/PCBWay prototype run options.

---

## 4. Technical Specifications & Engineering Rules

### A. Camera Character Resolution & Optical Calculations
* **Sensor Model:** Raspberry Pi Camera Module 3 Sensor Assembly (SA31VA30P / Sony IMX708)
* **Active Pixels:** 4608 x 2592 (11.9 Megapixels effective)
* **Pixel Pitch:** 1.40 µm
* **Lens Focal Length:** f = 4.74 mm (Diagonal FoV = 76°, Horizontal FoV ≈ 66°)
* **Autofocus Technology:** Hardware PDAF (Phase Detection Autofocus) with Voice Coil Motor (dynamic range: 10 cm to infinity)
* **Physical Sensor Footprint:** 10.8 x 10.8 mm bare cube with 24 mm flexible ribbon tail
* **Reading Resolution at 35 cm Reading Distance (8pt font, character height 1.8 mm):**
  ```
  Resolution = (h_char * f) / (D * p)
             = (1.8 mm * 4.74 mm) / (350 mm * 0.00140 mm)
             = 8.532 / 0.490
             ≈ 17.4 pixels per character
  ```
  This comfortably exceeds the 10.0 pixels/char minimum required for accurate OCR text recognition (PP-OCRv6 / DBNet).

* **Power Architecture at Nose Bridge (Preventing 1.32W of Heat Waste):**
  Stepping 3.3V down to 1.1V for the sensor core (VDD_CORE at 600mA) using an LDO would generate:
  ```
  P_loss = (3.3V - 1.1V) * 0.60A = 1.32 Watts of pure waste heat!
  ```
  This is completely unacceptable in an eyewear frame with a 3.0W total thermal budget. The Front-Bridge PCB uses an AP3429K synchronous buck converter (90%+ efficiency) to drop heat loss to under 0.07 Watts (>94% thermal reduction).

---

### B. Compute Engine & Memory Sizing Rules
* **Processor Architecture:** Rockchip RK3576 (4x Cortex-A72 @ 2.2 GHz + 4x Cortex-A53 @ 2.0 GHz, 6.0 TOPS INT4/INT8 NPU).
* **Package Dimensions:** FCCSP-698L (16.1 x 17.2 mm).
* **Board Width Rule:** Because the chip is 16.1 mm wide, the custom PCB width is strictly locked to **20–22 mm** (matching the 20–22 mm temple height profile of Track 1 eyewear).
* **Runtime Memory Footprint (Why 4GB is Mandatory):**
  * Headless Linux OS: ~350 MB
  * Camera ISP streaming buffers: ~120 MB
  * RKLLM Qwen2-0.5B (w4a16): 443 MB working memory
  * SigLIP-B vision encoder: ~170 MB
  * RapidOCR text detection/recognition: ~50 MB
  * Kokoro-82M TTS & Speech-to-Text: ~350 MB
  * **English Baseline Working Memory:** **~1.52 GB**
  * **With IndicTrans2-Dist Hindi Translation:** **~1.94 GB to 2.36 GB**
  * A 2GB board would trigger out-of-memory kernel panics. **4GB RAM is strictly required.**

---

### C. Audio Subsystem Wiring & Resistor Thresholds
* **Logic Level:** 3.3V peripheral I/O rail.
* **MAX98357A SD_MODE Pin Configuration:**
  * Shutdown: Voltage < 0.16V
  * Left Channel: Voltage between 0.77V and 1.39V (10 kOhm pull-up to 3.3V, 220 kOhm pull-down to GND)
  * Right Channel: Voltage > 1.39V (10 kOhm pull-up directly to 3.3V)
* **GAIN Pin Configuration:** The GAIN pin is tied to VDD via a 100 kOhm resistor (+3 dB gain). Combined with software volume capped at 70% (-3 dBFS), maximum output power into the 8 Ohm speakers is capped below 0.80W RMS, preventing voice-coil distortion and speaker blowout.

---

### D. Battery Charging & Power Calculations
* **Injoinic IP2326 2S Boost Charger (Pin 11 ISET Formula):**
  ```
  I_charge (mA) = 90,000 / R_iset (kOhm)
  For 300mA 1C charge rate:
  R_iset = 90,000 / 300 = 300 kOhm
  ```
* **System Operating Currents on 5.0V Bus:**
  * Standby / Idle (0.35W): 0.35W / 5.0V = **0.07 A**
  * Active AI Burst (3.0W): 3.0W / 5.0V = **0.60 A**
  * Duty-Cycle Average (0.615W over 120s turn): 0.615W / 5.0V = **0.123 A**
  * Runtime on dual 300mAh cells (2.22 Wh at 90% buck efficiency): **~3.2 hours** continuous duty.

---

### E. Directive 05 Mass Accounting (All-Up Wearable Weight)

| Subsystem | Components Included | Qty | Unit Mass (g) | Extended Mass (g) |
|---|---|:---:|:---:|:---:|
| **Compute Core** | Custom slim PCB (20–22 x 75 mm) with RK3576, PMIC, eMCP, passives | 1 | 12.0 | 12.0 |
| **Optical Module** | Sony IMX708 bare sensor cube (2.5g) + front-bridge PCB (2.0g) | 1 | 4.5 | 4.5 |
| **Optical Lenses** | Pair of 1.67 high-index prescription lenses | 2 | 4.25 | 8.5 |
| **Energy Storage** | GNB 3.7V 300mAh LiPo pouch cells (1 per temple) | 2 | 8.0 | 16.0 |
| **Power Management** | IP2326 charger, HY2212 BMS, MP2315 buck module | 3 | — | 5.8 |
| **Audio Subsystem** | Dual MAX98357A amps, dual 1510 speakers, dual INMP441 mics | 6 | — | 7.2 |
| **User Input** | TTP223 capacitive touch sensor | 1 | 0.6 | 0.6 |
| **Wiring & Carriers** | Thin FR4 carriers + browline FPC ribbon + silicone wiring | — | — | 9.0 |
| **Frame Mechanics** | 3D-printed PETG front frame and thick temple arms | 1 | 24.0 | 24.0 |
| **Thermal Sinks** | Copper shim, 4.0g RT42 bio-PCM pad, aerogel skin barrier | — | — | 8.0 |
| **Fasteners & Reserve** | M1.6/M2 brass heatset inserts, screws, Kapton + tolerance margin | — | — | 7.3 |
| **TOTAL ALL-UP MASS** | **Complete Untethered Wearable Smart Glasses** | — | — | **102.9 g** |

* **Target Margin:** **17.1 g below** the 120.0 g target.
* **Ceiling Margin:** **22.1 g below** the strict 125.0 g Directive 05 ceiling.

---

## 5. Local Sourcing & Vendor Directory (Mumbai / Online)

1. **[LCSC Electronics](https://lcsc.com):** RK3576, RK806-1, RTL8723DS, master crystals, RTC crystals, USB-C ports, micro buttons, SMD passives.
2. **[Robu.in](https://robu.in):** INMP441 mics, MAX98357A amps, GNB LiPo cells, IP2326 chargers, IMX708 camera, silicone wire, and FPC ribbons. Fast delivery to Juhu/Mumbai within 48–72 hours.
3. **[Amazon.in](https://amazon.in):** Numakers Pitch Black PETG 1kg spool ([https://amzn.in/d/074Tf1Tx](https://amzn.in/d/074Tf1Tx)), copper shims, heatset inserts.
4. **[Probots.co.in](https://probots.co.in):** 1510 micro dynamic oval speakers.
5. **Local BGA Rework (Lamington Road / Grant Road / Juhu):** Scrap donor smartphone motherboard (Redmi 9 / POCO M2) desoldering and precision BGA stencil reballing.
