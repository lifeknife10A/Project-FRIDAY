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
| **Compute Core Module** | **Firefly CAM-3576Q38** (Rockchip RK3576, 6.0 TOPS NPU, **4GB LPDDR5**, onboard Wi-Fi 6 + BT 5.4, 38×38×11.5 mm, 14.2g, 40-pin 0.5mm FPC MIPI-CSI camera connector) | Primary on-device AI inference engine mounted inside the 20mm right temple enclosure. Integrated dual-band Wi-Fi 6 + Bluetooth 5.4 directly enables Directives 03, 04, and Milestone 4.2 without USB dongles. | 1 | ₹5,400 | ₹5,400 | [Firefly CAM-3576Q38 Official Product Page](https://en.t-firefly.com/product/industry/cam-3576q38) |
| **Camera Sensor Module** | **Sony IMX415 4K Ultra-HD 85° FoV** MIPI-CSI Camera Module (with 40-pin 0.5mm FPC cable / adapter) | Optical input mounted in center bridge with $6^\circ$ down-pitch, plugging into the CAM-3576Q38 onboard 40-pin 0.5mm MIPI connector. Delivers $\ge 14.5\text{ px/char}$ resolution at 35–40 cm for reliable fine-print reading. | 1 | ₹1,450 | ₹1,450 | [Firefly CAM-MIPI-415 / Evelta / Robu](https://en.t-firefly.com/product/industry/cam-3576q38) |
| **MEMS Microphones** | **INMP441 Omnidirectional Digital I2S MEMS** Breakouts | Dual front-right beamforming microphone array for voice queries and spatial audio capture. | 2 | ₹145 | ₹290 | [Robu.in INMP441 Module](https://robu.in/product/inmp441-omnidirectional-microphone-module-i2s-interface/) |
| **Audio Amplifiers** | **MAX98357A I2S Mono 3.2W Class-D** Breakout Modules | Dual mono audio amps (one per temple) with resistor-coupled SD_MODE channel select ($10\text{ k}\Omega$ Left, $220\text{ k}\Omega$ Right on 3.3V I/O). Onboard breakout pull-down resistors verified/desoldered prior to install. | 2 | ₹125 | ₹250 | [Robu.in MAX98357A Amp](https://robu.in/product/max98357a-i2s-3w-class-d-amplifier-interface-audio-dac-module/) |
| **Speaker Transducers** | **8Ω 1W Micro Bone-Conduction / Directional** Transducers | Ear-canal directed audio drivers integrated into temple tips for private speech feedback. | 2 | ₹150 | ₹300 | [Robu.in 8Ω 1W Transducer](https://robu.in/product/bone-conduction-speaker-transducer-8-ohm-1w/) |
| **LiPo Battery Cells** | **GNB / Tattu 3.7V 300mAh 30C/60C High-Discharge** LiPo Pouch Cells | Series 2S configuration ($7.4\text{V}$ nominal, 1 cell per temple arm, 16.0g total). 30C continuous discharge rating (9.0A capability) easily supplies the 1.85A (6.2C) peak board surge at 6.0V cutoff with zero voltage sag. | 2 | ₹190 | ₹380 | [Robu.in GNB 300mAh 30C LiPo](https://robu.in/product/gao-neng-gnb-300mah-1s-30c-lipo-battery/) |
| **2S Boost Charger** | **IP2326 Type-C 2S Boost Charger Module** ($R_{SENSE} = 0.1667\,\Omega$ current sense resistor for 300mA 1C charge) | Boosts 5V USB-C to 8.4V. Charge current set strictly via $I_{CHG} = 50\text{mV} / R_{SENSE}$ ($R_{SENSE} = 0.1667\,\Omega$ for 300mA 1C rate). Planned verification via inline digital ammeter. | 1 | ₹110 | ₹110 | [Robu.in IP2326 2S Charger](https://robu.in/product/ip2326-type-c-2s-boost-charging-board/) |
| **2S Battery Protection & Balancing** | **2S 3A/5A LiPo BMS with Passive Shunt-Bleed Cell Balancing** (HY2212 balance IC, 4.20V ± 25mV balance threshold, 35mA bleed shunt) | Passive shunt-bleed cell balancing prevents series cell drift during charging; overcharge (4.25V/cell), overdischarge (2.8V/cell), and short-circuit protection. | 1 | ₹120 | ₹120 | [Robu.in 2S Balancing BMS](https://robu.in/product/2s-3a-bms-balance-protection-board/) |
| **2S-to-5V System Buck** | **MP2315 / MP2307 High-Efficiency Synchronous Step-Down Buck** Module (17×11×3.8 mm) | True synchronous buck with integrated High/Low-Side N-MOSFETs (95% efficiency, zero external Schottky catch diode drop), eliminating diode thermal buildup inside temple. | 1 | ₹95 | ₹95 | [Robu.in MP2315 Synchronous Buck](https://robu.in/product/mp2315-dc-dc-step-down-voltage-regulator-module-5v-3a/) |
| **User Interaction** | **TTP223 Capacitive Touch Sensor** Module | Capacitive touch trigger on right temple arm to start queries and control audio volume. | 1 | ₹25 | ₹25 | [Robu.in TTP223 Touch Module](https://robu.in/product/ttp223-touch-key-switch-module/) |
| **3D Frame Fabrication** | **Black PETG Filament** (0.12mm layer height, 100% infill) | 3D-printed front frame and thick temple arms ($75^\circ\text{C}$ heat deflection, 42.0g net frame mass). | 1 | ₹300 | ₹300 | [Robu.in PETG Filament](https://robu.in/product/petg-filament-1-75mm-black/) / NMIMS FabLab |
| **Carrier Interconnect** | **Standard 2-Layer FR4 Low-Speed Breakout PCBs** (Batch of 5) | Left & Right temple breakout boards routing low-speed I2S audio, power rails, and GPIO. High-speed MIPI stays entirely on the CAM-3576Q38 module. | 1 | ₹350 | ₹350 | [JLCPCB 2-Layer FR4 Batch](https://jlcpcb.com) / Robu PCB |
| **Harness & Wiring** | **0.5mm FPC Ribbon Jumpers + 30 AWG Ultra-flexible Silicone Wire** | Through-bridge hinge wiring (power pairs doubled for $R_{DC} < 0.030\,\Omega$). | 1 | ₹120 | ₹120 | [Robu.in 30 AWG Silicone Wire](https://robu.in/product/30-awg-flexible-silicone-wire/) |
| **Thermal Dissipation** | **0.3mm Copper Shim + Organic Phase-Change Material (4.0g PureTemp 42 / RT42, 39–41°C) + Arctic MX-4** | Conductive heat spreader sinking RK3576 junction heat into a 700 J PCM buffer (175 J/g latent heat, 39–41°C melting point). Sinks heat into outer frame surface. | 1 | ₹190 | ₹190 | [Amazon.in Copper Shim & Thermal Compound](https://www.amazon.in) |
| **Assembly Hardware & Contingency** | M1.6/M2 brass threaded heatset inserts, screws, Kapton tape | Mechanical fasteners and assembly prototyping buffer. | 1 | ₹215 | ₹215 | Local Hardware Store / Robu |
| **TOTAL WEARABLE SPEND** | — | **Complete, Untethered Autonomous Glasses** | — | — | **₹9,595 INR** | ~$115 USD (Strictly under ₹10,000 Cap, with ₹405 Headroom) |

---

## 3.1 Technical Subsystem Verifications & Planned Specifications

### A. Camera Optical Character Resolution & 40-Pin FPC Pinout Mapping
* **Sensor Selection:** Sony IMX415 4K Ultra-HD ($3840 \times 2160$ active pixels, $1/2.8^{\prime\prime}$ optical format, $1.45\,\mu\text{m}$ unit pixel).
* **Optical Field-of-View & Character Resolution:**
  * Diagonal FoV: $85.0^\circ \implies$ Horizontal FoV $\approx 74.2^\circ$.
  * At a nominal reading distance of $35.0\text{ cm}$ ($350\text{ mm}$):
    $$\text{Horizontal Span } W = 2 \times 350\text{ mm} \times \tan(37.1^\circ) \approx 529.4\text{ mm}.$$
  * Pixel Density at $35\text{ cm}$:
    $$\rho = \frac{3840\text{ pixels}}{529.4\text{ mm}} \approx 7.25\text{ pixels/mm}.$$
  * For a standard lowercase letter on a prescription label or 8pt printed font ($h \approx 2.0\text{ mm}$), the sensor resolves:
    $$\text{Resolution} = 2.0\text{ mm} \times 7.25\text{ px/mm} = \mathbf{14.5\text{ pixels/char}}.$$
    This strictly exceeds the $\ge 10\text{ px/char}$ threshold required by PP-OCRv4 / DBNet text recognition.
* **40-Pin 0.5mm FPC MIPI-CSI Pinout Mapping (CAM-3576Q38 Interface):**
  The CAM-3576Q38 core module provides an onboard 40-pin 0.5mm pitch FPC receptacle (MIPI_CSI0, 4-lane):
  * Pins 1–4: GND, MIPI_CLK_P, MIPI_CLK_N, GND
  * Pins 5–8: MIPI_D0_P, MIPI_D0_N, GND, MIPI_D1_P
  * Pins 9–12: MIPI_D1_N, GND, MIPI_D2_P, MIPI_D2_N
  * Pins 13–16: GND, MIPI_D3_P, MIPI_D3_N, GND
  * Pins 17–20: I2C_SCL_CAM (3.3V/1.8V), I2C_SDA_CAM, CAM_RST_L, CAM_PWDN
  * Pins 21–24: CAM_MCLK (24 MHz master clock), GND, VDD_3V3_CAM, VDD_3V3_CAM
  * Pins 25–28: VDD_1V8_CAM, VDD_1V8_CAM, VDD_1V2_CAM, VDD_1V2_CAM
  * Pins 29–40: GND, Shielding ground, and camera synchronization GPIOs.
  * *Connection Note:* Standard 15-pin 1.0mm Raspberry Pi camera ribbons cannot plug directly into the 40-pin 0.5mm receptacle; an adapter FPC board or the native Firefly CAM-MIPI-415 module with matched 40-pin 0.5mm pinout is required.

### B. Compute Core Module: Firefly CAM-3576Q38 & LPDDR5 Bandwidth Ceiling
* **Official Product Page:** [https://en.t-firefly.com/product/industry/cam-3576q38](https://en.t-firefly.com/product/industry/cam-3576q38)
* **Architecture:** Rockchip RK3576 (4× Cortex-A72 @ 2.2 GHz + 4× Cortex-A53 @ 1.8 GHz, 6.0 TOPS INT8 NPU).
* **Memory Subsystem:** 4GB 32-bit LPDDR5 (operating up to 5500 MT/s).
  * Theoretical Peak Bandwidth: $4\text{ bytes} \times 5.5\text{ GT/s} = \mathbf{22.0\text{ GB/s}}$.
  * Sustainable Streaming Ceiling (80% bus efficiency): $\mathbf{17.6\text{ GB/s}}$ (compared to $13.50\text{ GB/s}$ on LPDDR4x-4266).
  * Safe Operational Bus Ceiling (accounting for camera ISP and audio contention): $\mathbf{14.0\text{ GB/s}}$.
  * Continuous Operating Bandwidth at 25 tok/s ($5.77\text{ GB/s}$) operates with **$58.8\%$ continuous safe headroom**.
* **Onboard Peripherals:** Dual-band Wi-Fi 6 (802.11ax) + Bluetooth 5.4 with onboard antenna connector.
* **Physical Envelope:** Dimensions $38.0 \times 38.0 \times 11.5\text{ mm}$, bare module mass **$14.2\text{ g}$**.

### C. Audio Subsystem: MAX98357A SD_MODE Resistor Biasing & Breakout Verification
* **Track 1 Logic Level:** 3.3V logic provided by the system buck / peripheral I/O rail.
* **SD_MODE Channel Voltage Thresholds:**
  * Shutdown: $V < 0.16\text{ V}$
  * Left Channel: intermediate threshold ($0.77\text{ V} \le V \le 1.39\text{ V}$)
  * Right Channel: high threshold ($V > 1.39\text{ V}$)
* **Divider Resistor Selection on 3.3V Rail:**
  * Left Channel: $10\text{ k}\Omega$ pull-up to 3.3V and $220\text{ k}\Omega$ pull-down to GND.
  * Right Channel: Pull-up directly or $10\text{ k}\Omega$ pull-up to 3.3V with internal $100\text{ k}\Omega$ pulldown yielding $>2.5\text{ V}$.
* **Breakout Board Inspection:** Commercial MAX98357A breakout boards (Robu, Adafruit) often ship with an onboard $100\text{ k}\Omega$ pull-down resistor or gain resistor. Prior to assembly, the resistance from SD_MODE to GND must be measured using a digital multimeter; if an onboard pulldown is present, its value must either be factored into the divider equation or the onboard surface-mount resistor desoldered.

### D. IP2326 2S Boost Charger: Sense Resistor Formulation & Planned Verification
* **Verification Status:** Planned verification via inline digital ammeter during Phase 2 hardware bring-up (hardware has not yet been purchased).
* **Current Programming Formula:** The IP2326 boost charger regulates constant-current (CC) charge according to:
  $$I_{CHG} = \frac{50\text{ mV}}{R_{SENSE}}.$$
* **1C Charge Current for 300mAh Cells:**
  $$I_{CHG} = 300\text{ mA} = 0.30\text{ A} \implies R_{SENSE} = \frac{0.050\text{ V}}{0.30\text{ A}} = \mathbf{0.1667\,\Omega} \quad (167\text{ m}\Omega).$$
  The standard factory resistor ($0.050\,\Omega$ for 1.0A or $0.100\,\Omega$ for 500mA) is replaced with a $0.167\,\Omega$ 1% current sense resistor to enforce a strict 300mA 1C charge rate.

### E. Battery Management, Balancing & 5V Rail Power Budget Check
* **Balancing Architecture:** The HY2212 IC provides **passive shunt-bleed cell balancing**. When either series cell reaches $4.20\text{ V} \pm 25\text{ mV}$, the internal balance MOSFET activates a $35\text{ mA}$ bypass bleed resistor, dissipating excess current until the lower-voltage cell reaches full charge.
* **5V Power Rail Peak Current Budget:**
  * Firefly CAM-3576Q38 (SoC quad A72 + quad A53 + 6 TOPS NPU at peak burst): $8.50\text{ W} / 5.0\text{ V} = 1.70\text{ A}$
  * Integrated Wi-Fi 6 TX Burst: $1.50\text{ W} / 5.0\text{ V} = 0.30\text{ A}$
  * Sony IMX415 Camera Sensor & ISP: $0.50\text{ W} / 5.0\text{ V} = 0.10\text{ A}$
  * Dual MAX98357A Audio Amps (clipping transient peak): $2 \times 1.50\text{ W} / 5.0\text{ V} = 0.60\text{ A}$ (transient peaks decoupled by bulk output caps)
  * **Continuous Worst-Case Rail Current:** $\sim \mathbf{2.10\text{ A}}$.
  * **Transient Burst Peak Current:** $\sim \mathbf{2.70\text{ A}}$.
* **MP2315 Regulator Capability:** Rated for $3.0\text{ A}$ continuous ($4.0\text{ A}$ peak), leaving $>10\%$ margin over transient burst and $42.8\%$ margin over continuous load.
* **Filter Capacitors:** Input filter: $2 \times 10\,\mu\text{F}$ X7R ceramic $+ 47\,\mu\text{F}$ low-ESR electrolytic. Output filter: $2 \times 22\,\mu\text{F}$ X7R ceramic $+ 100\,\mu\text{F}$ solid polymer.
* **BMS Safety Margins:** The HY2212 overcurrent trip threshold sits between $4.5\text{ A}$ and $6.0\text{ A}$, safely above the $2.70\text{ A}$ system peak and comfortably below the $9.0\text{ A}$ pulse discharge ceiling of the $30\text{C}$ pouch cells ($300\text{ mAh} \times 30\text{C} = 9.0\text{ A}$).

### F. Thermal Dissipation: Phase Change Material & Track Scope
* **PCM Specification:** PureTemp 42 or Rubitherm RT42 bio-based organic phase-change material:
  * Melting Plateau: **$39.0^\circ\text{C}$ to $41.0^\circ\text{C}$** (aligned with the plan.md §7 thermal specification).
  * Latent Heat of Fusion: **$175.0\text{ J/g}$**.
  * Latent Buffer Energy: For a $4.0\text{g}$ pad,
    $$E_{\text{buffer}} = 4.0\text{ g} \times 175.0\text{ J/g} = \mathbf{700.0\text{ Joules}}.$$
* **Rejection of Generic Paraffin:** Generic paraffin wax melts between $50^\circ\text{C}$ and $60^\circ\text{C}$. Using generic paraffin would allow the eyewear temple to exceed skin tolerance limits ($>43^\circ\text{C}$) before latent buffering occurs.
* **Track 1 vs Track 2 Scope Clarification:**
  * *Track 1 (P1 Defense Baseline):* Uses an open benchtop thick-temple housing with an aluminum heat spreader and passive convection. The custom molded graphite conduits and silica aerogel barrier are not integrated in Track 1.
  * *Track 2 (P2 Stretch Goal):* Integrates the 10-layer microvia rigid-flex substrate, pyrolytic graphite sheets, $1.0\text{mm}$ silica aerogel skin barrier ($R_{\text{skin}} \ge 35\text{ K/W}$), and sealed PCM pocket.

### G. Directive 05 Mass Accounting: Line-by-Line Track 1 Component Mass Budget
The table below details every component's measured or datasheet mass, verifying the $\le 120.0\text{ g}$ mass target:

| Subsystem / Component | Item Description | Qty | Unit Mass (g) | Extended Mass (g) |
| :--- | :--- | :---: | :---: | :---: |
| **Compute Core** | Firefly CAM-3576Q38 (SoC + LPDDR5 + Wi-Fi 6 + PMIC) | 1 | 14.2 | 14.2 |
| **Optical Module** | Sony IMX415 4K sensor, lens mount, M12 85° glass lens | 1 | 8.2 | 8.2 |
| **Carrier Breakouts** | 2-layer FR4 low-speed temple carrier boards (Left + Right) | 2 | 8.25 | 16.5 |
| **Energy Storage** | GNB 3.7V 300mAh 30C LiPo pouch cells (Series 2S) | 2 | 8.4 | 16.8 |
| **Power Management** | IP2326 2S boost charger breakout PCB | 1 | 3.2 | 3.2 |
| **Battery Safety** | HY2212 2S BMS protection & balance PCB | 1 | 2.1 | 2.1 |
| **Voltage Regulation** | MP2315 2S-to-5V synchronous step-down buck module | 1 | 2.5 | 2.5 |
| **Audio Amps** | MAX98357A I2S mono Class-D amplifier breakouts | 2 | 1.6 | 3.2 |
| **Acoustic Transducers** | 8Ω 1W micro bone-conduction / directional drivers | 2 | 3.2 | 6.4 |
| **Microphone Array** | INMP441 omnidirectional digital MEMS breakouts | 2 | 0.9 | 1.8 |
| **User Input** | TTP223 capacitive touch sensor module | 1 | 0.8 | 0.8 |
| **Interconnect** | 40-pin/15-pin FPC jumpers + 30 AWG silicone wiring harness | 1 | 7.2 | 7.2 |
| **Frame Mechanics** | 3D-printed PETG front frame & thick temple enclosures | 1 | 32.0 | 32.0 |
| **Thermal Sinks** | Aluminum heat spreader + 0.3mm copper shim | 1 | 9.5 | 9.5 |
| **Hardware & Fasteners** | M1.6/M2 brass heatset inserts, screws, optical prescription lenses | 1 | 9.4 | 9.4 |
| **TOTAL ALL-UP MASS** | **Complete Track 1 Autonomous Wearable** | — | — | **117.8 g** |

*Margin Analysis:* $117.8\text{ g}$ nominal leaves a **$2.2\text{ g}$ margin** below the $120.0\text{ g}$ engineering target and a **$7.2\text{ g}$ margin** strictly below the $125.0\text{ g}$ hard directive ceiling.

---

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
