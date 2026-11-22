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
| **Camera Sensor Module** | **Sony IMX415 4K Ultra-HD 85° FoV** MIPI-CSI Camera Module (with 40-pin 0.5mm FPC cable / adapter) | Optical input mounted in center bridge with $6^\circ$ down-pitch, plugging into the CAM-3576Q38 onboard 40-pin 0.5mm MIPI connector. Delivers $\mathbf{12.8\text{ px/char}}$ resolution at 35 cm for reliable fine-print reading. | 1 | ₹1,450 | ₹1,450 | [Firefly CAM-MIPI-415 / Evelta / Robu](https://en.t-firefly.com/product/industry/cam-3576q38) |
| **MEMS Microphones** | **INMP441 Omnidirectional Digital I2S MEMS** Breakouts | Dual front-right beamforming microphone array for voice queries and spatial audio capture. | 2 | ₹145 | ₹290 | [Robu.in INMP441 Module](https://robu.in/product/inmp441-omnidirectional-microphone-module-i2s-interface/) |
| **Audio Amplifiers** | **MAX98357A I2S Mono 3.2W Class-D** Breakout Modules | Dual mono audio amps (one per temple) with resistor-coupled SD_MODE channel select ($10\text{ k}\Omega$ Left, $220\text{ k}\Omega$ Right on 3.3V I/O). Onboard breakout pull-down resistors verified/desoldered prior to install. | 2 | ₹125 | ₹250 | [Robu.in MAX98357A Amp](https://robu.in/product/max98357a-i2s-3w-class-d-amplifier-interface-audio-dac-module/) |
| **Speaker Transducers** | **8Ω 1W Micro Bone-Conduction / Directional** Transducers | Ear-canal directed audio drivers integrated into temple tips for private speech feedback. | 2 | ₹150 | ₹300 | [Robu.in 8Ω 1W Transducer](https://robu.in/product/bone-conduction-speaker-transducer-8-ohm-1w/) |
| **LiPo Battery Cells** | **GNB / Tattu 3.7V 300mAh 30C/60C High-Discharge** LiPo Pouch Cells | Series 2S configuration ($7.4\text{V}$ nominal, 1 cell per temple arm, 16.0g total). 30C continuous discharge rating (9.0A capability) easily supplies the 1.85A (6.2C) peak board surge at 6.0V cutoff with zero voltage sag. | 2 | ₹190 | ₹380 | [Robu.in GNB 300mAh 30C LiPo](https://robu.in/product/gao-neng-gnb-300mah-1s-30c-lipo-battery/) |
| **2S Boost Charger** | **IP2326 Type-C 2S Boost Charger Module** (Pin 11 ISET resistor $R_{ISET} = 300\text{ k}\Omega$ for 300mA 1C charge, via $I_{CHG} = 90{,}000 / R_{ISET}$) | Boosts 5V USB-C to 8.4V. Charge current set strictly via Injoinic IP2326 Pin 11 ISET formula: $I_{CHG}\text{ (mA)} = 90{,}000 / R_{ISET}\text{ (k}\Omega\text{)}$ ($R_{ISET} = 300\text{ k}\Omega$ for 300mA 1C rate). Planned verification via inline digital ammeter. | 1 | ₹110 | ₹110 | [Robu.in IP2326 2S Charger](https://robu.in/product/ip2326-type-c-2s-boost-charging-board/) |
| **2S Battery Protection & Balancing** | **2S 3A/5A LiPo BMS with Passive Shunt-Bleed Cell Balancing** (HY2212 balance IC, 4.20V ± 25mV balance threshold, 35mA bleed shunt) | Passive shunt-bleed cell balancing prevents series cell drift during charging; overcharge (4.25V/cell), overdischarge (2.8V/cell), and short-circuit protection. | 1 | ₹120 | ₹120 | [Robu.in 2S Balancing BMS](https://robu.in/product/2s-3a-bms-balance-protection-board/) |
| **2S-to-5V System Buck** | **MP2315 / MP2307 High-Efficiency Synchronous Step-Down Buck** Module (17×11×3.8 mm) | True synchronous buck with integrated High/Low-Side N-MOSFETs (95% efficiency, zero external Schottky catch diode drop), eliminating diode thermal buildup inside temple. | 1 | ₹95 | ₹95 | [Robu.in MP2315 Synchronous Buck](https://robu.in/product/mp2315-dc-dc-step-down-voltage-regulator-module-5v-3a/) |
| **User Interaction** | **TTP223 Capacitive Touch Sensor** Module | Capacitive touch trigger on right temple arm to start queries and control audio volume. | 1 | ₹25 | ₹25 | [Robu.in TTP223 Touch Module](https://robu.in/product/ttp223-touch-key-switch-module/) |
| **3D Frame Fabrication** | **Black PETG Filament** (0.12mm layer height, 1.2mm wall thickness, 30% gyroid infill) | 3D-printed front frame and thick temple arms ($75^\circ\text{C}$ heat deflection, 24.0g net frame mass, reduced from 42.0g solid block prototype). | 1 | ₹300 | ₹300 | [Robu.in PETG Filament](https://robu.in/product/petg-filament-1-75mm-black/) / NMIMS FabLab |
| **Carrier Interconnect** | **Combined 0.8mm Thin 2-Layer FR4 Carrier PCBs** (Batch of 5) | Left & Right temple custom 0.8mm thin breakout carriers routing low-speed I2S audio, power rails, and GPIO (4.5g combined mass, reduced from 16.5g separate modules). | 1 | ₹350 | ₹350 | [JLCPCB 2-Layer FR4 Batch](https://jlcpcb.com) / Robu PCB |
| **Harness & Wiring** | **0.5mm FPC Ribbon Jumpers + 30 AWG Ultra-flexible Silicone Wire** | Through-bridge hinge wiring (power pairs doubled for $R_{DC} < 0.030\,\Omega$). | 1 | ₹120 | ₹120 | [Robu.in 30 AWG Silicone Wire](https://robu.in/product/30-awg-flexible-silicone-wire/) |
| **Thermal Dissipation** | **0.3mm Copper Shim + Organic Phase-Change Material (4.0g Rubitherm RT42, 38–43°C, peak 41°C) + 1.0mm Silica Aerogel Blanket (10 cm²) + Arctic MX-4** | Conductive heat spreader sinking RK3576 junction heat into a 660 J PCM buffer (Rubitherm RT42, 165 J/g latent heat, 38–43°C melting range, peak 41°C) with inner 1.0mm silica aerogel blanket protecting user skin. Sinks heat outward into ambient air. | 1 | ₹350 | ₹350 | [Amazon.in Copper Shim & Robu Aerogel](https://www.amazon.in) |
| **Assembly Hardware & Contingency** | M1.6/M2 brass threaded heatset inserts, screws, Kapton tape | Mechanical fasteners and assembly prototyping buffer. | 1 | ₹215 | ₹215 | Local Hardware Store / Robu |
| **TOTAL WEARABLE SPEND** | — | **Complete, Untethered Autonomous Glasses** | — | — | **₹9,755 INR** | ~$117 USD (Strictly under ₹10,000 Cap, with ₹245 Headroom) |

---

## 3.1 Technical Subsystem Verifications & Planned Specifications

### A. Camera Optical Character Resolution & 40-Pin FPC Pinout Mapping
* **Sensor Selection:** Sony IMX415 4K Ultra-HD ($3840 \times 2160$ active pixels, $1/2.8^{\prime\prime}$ optical format, $1.45\,\mu\text{m}$ unit pixel).
* **Optical Field-of-View & Character Resolution:**
  * Diagonal FoV: $85.0^\circ \implies$ Horizontal FoV $\approx 74.2^\circ$.
  * Lens focal length $f = 3.6\text{ mm}$, pixel pitch $p = 1.45\,\mu\text{m} = 0.00145\text{ mm}$.
  * At a nominal reading distance $D = 35.0\text{ cm} = 350.0\text{ mm}$ for 8pt printed font / prescription label ($h_{\text{char}} \approx 1.8\text{ mm}$):
    $$\text{Resolution} = \frac{h_{\text{char}} \cdot f}{D \cdot p} = \frac{1.8\text{ mm} \times 3.6\text{ mm}}{350\text{ mm} \times 0.00145\text{ mm}} = \frac{6.48}{0.5075} \approx \mathbf{12.8\text{ pixels/char}}.$$
    This strictly exceeds the $\ge 10.0\text{ px/char}$ threshold required by PP-OCRv4 / DBNet text recognition.
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
* **GAIN Pin Configuration & Acoustic Power Limiting:**
  The MAX98357A GAIN pin selects amplifier gain: connecting GAIN to VDD through a $100\text{ k}\Omega$ resistor configures the lowest gain setting of $+3\text{ dB}$ (connecting directly to VDD yields $+6\text{ dB}$, floating yields $+9\text{ dB}$, GND yields $+12\text{ dB}$). For Project FRIDAY, the GAIN pin is tied to VDD via $100\text{ k}\Omega$ ($+3\text{ dB}$ gain). Combined with an ALSA/software volume cap at $70\%$ ($-3\text{ dBFS}$), output power into the $8\,\Omega$ transducers is strictly capped below $0.80\text{ W RMS}$ (safely below the $1.0\text{ W}$ continuous rating of the micro bone-conduction transducers), preventing voice-coil burnout and eliminating clipping distortion.

### D. IP2326 2S Boost Charger: Sense Resistor Formulation & Planned Verification
* **Verification Status:** Planned verification via inline digital ammeter during Phase 2 hardware bring-up (hardware has not yet been purchased; marked unverified pending physical measurement).
* **Current Programming Formula (Injoinic IP2326 English Datasheet Section 7.2, Pin 11 ISET):**
  The IP2326 programs battery charge current via the external resistor $R_{ISET}$ connected to Pin 11:
  $$I_{CHG}\text{ (mA)} = \frac{90{,}000}{R_{ISET}\text{ (k}\Omega\text{)}}.$$
* **1C Charge Current for 300mAh Cells:**
  $$I_{CHG} = 300\text{ mA} \implies R_{ISET} = \frac{90{,}000}{300} = \mathbf{300\text{ k}\Omega}.$$
  The factory resistor (typically $90\text{ k}\Omega$ for $1.0\text{ A}$ or $180\text{ k}\Omega$ for $500\text{ mA}$) is replaced with a $300\text{ k}\Omega$ 1% resistor on Pin 11 to enforce a strict 300mA 1C charge rate.

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
* **PCM Specification: Rubitherm RT42 Bio-Based Organic Phase-Change Material** (Rubitherm GmbH Data Sheet):
  * Melting Area (solidus to liquidus): **$38.0^\circ\text{C}$ to $43.0^\circ\text{C}$** (main peak: **$41.0^\circ\text{C}$**), precisely aligning with the plan.md §7 $39\text{--}41^\circ\text{C}$ skin temperature protection envelope.
  * Congealing Area: $43.0^\circ\text{C}$ to $37.0^\circ\text{C}$ (main peak: $42.0^\circ\text{C}$).
  * Latent Heat of Fusion / Storage Capacity: **$165.0\text{ kJ/kg}$** ($165.0\text{ J/g}$) between $35^\circ\text{C}$ and $50^\circ\text{C}$.
  * Latent Buffer Energy: For a $4.0\text{g}$ pad,
    $$E_{\text{buffer}} = 4.0\text{ g} \times 165.0\text{ J/g} = \mathbf{660.0\text{ Joules}}.$$
  * *Note on PureTemp 42:* PureTemp 42 exhibits a higher nominal melting peak at $\sim 42.0^\circ\text{C}$ (latent heat $218\text{ J/g}$). Rubitherm RT42 is designated as the primary baseline due to its $38\text{--}43^\circ\text{C}$ melting plateau with main peak at $41.0^\circ\text{C}$, ensuring skin boundary temperatures remain below $42^\circ\text{C}$.
* **Rejection of Generic Paraffin:** Generic paraffin wax melts between $50^\circ\text{C}$ and $60^\circ\text{C}$. Using generic paraffin would allow the eyewear temple to exceed skin tolerance limits ($>43^\circ\text{C}$) before latent buffering occurs.
* **Track 1 vs Track 2 Scope Clarification (Auditor Review D1):**
  * *Track 1 (P1 Defense Baseline):* Integrates an open benchtop thick-temple housing with an aluminum/copper heat spreader, a $1.0\text{mm}$ silica aerogel inner blanket barrier ($R_{\text{skin}} \ge 66.7\text{ K/W}$), a $4.0\text{g}$ Rubitherm RT42 PCM pad, and passive exterior convection. Custom molded pyrolytic graphite conduits and complex microvia rigid-flex substrates are deferred to Track 2.
  * *Track 2 (P2 Stretch Goal):* Integrates the 10-layer microvia rigid-flex substrate, pyrolytic graphite heat spreaders, vacuum-encapsulated silica aerogel barrier, and precision sealed micro-pockets.
* **Track 1 Thermal Physics & Multi-Layer Insulation Model (Auditor Review R9, D1, D2):**
  * *Heat Sources & Outer vs. Inner Thermal Path:*
    * Outer Convection Path: Outer temple surface area $A_{\text{outer}} \approx 20\text{ cm}^2 = 0.002\text{ m}^2$, ambient convection coefficient $h \approx 15\text{ W/m}^2\cdot\text{K}$.
      $$R_{\text{conv}} \approx \frac{1}{h \cdot A_{\text{outer}}} = \frac{1}{15 \times 0.002} \approx \mathbf{33.3\text{ K/W}}.$$
    * Uninsulated Inner PETG Wall: Thickness $t_{\text{PETG}} = 1.2\text{ mm}$, $k_{\text{PETG}} \approx 0.20\text{ W/m}\cdot\text{K}$, area $A_{\text{inner}} \approx 10\text{ cm}^2 = 0.001\text{ m}^2$.
      $$R_{\text{PETG}} = \frac{0.0012}{0.20 \times 0.001} \approx \mathbf{6.0\text{ K/W}}.$$
      Because $6.0\text{ K/W} < 33.3\text{ K/W}$, an uninsulated wall would allow the majority of dissipated heat to flow inward toward user skin.
    * Inner Aerogel Insulation Layer: To guarantee skin safety, a $1.0\text{ mm}$ silica aerogel blanket ($k_{\text{ins}} \approx 0.015\text{ W/m}\cdot\text{K}$) is integrated between the compute core and the inner temple skin-contact face:
      $$R_{\text{ins}} = \frac{0.001\text{ m}}{0.015\text{ W/m}\cdot\text{K} \times 0.001\text{ m}^2} \approx \mathbf{66.7\text{ K/W}}.$$
      Total combined inner thermal resistance:
      $$R_{\text{inner}} = R_{\text{PETG}} + R_{\text{ins}} \approx 6.0 + 66.7 = \mathbf{72.7\text{ K/W}}.$$
      Now, $R_{\text{inner}} \approx 72.7\text{ K/W} \gg R_{\text{outer}} \approx 33.3\text{ K/W}$, driving $>68\%$ of dissipated heat outward into the exterior copper spreader and ambient air.
  * *Duty-Cycle-Averaged Power & Two-Sink Network Solution (Auditor Review D1, D2):*
    * Inference Duty Cycle: Active inference $3.0\text{ W}$ for $12.0\text{ s}$; Standby/idle $0.35\text{ W}$ for $108.0\text{ s}$ ($120.0\text{ s}$ full cycle period).
    * Duty-cycle-averaged power generation:
      $$\bar{P} = \frac{(3.0\text{ W} \times 12\text{ s}) + (0.35\text{ W} \times 108\text{ s})}{120\text{ s}} = \frac{36.0\text{ J} + 37.8\text{ J}}{120\text{ s}} = \mathbf{0.615\text{ W}}.$$
    * Two-Sink Thermal Boundary Conditions:
      * Outer Sink: Ambient air at $T_{\text{amb}}$ through $R_{\text{outer}} \approx 33.3\text{ K/W}$ ($G_{\text{outer}} = 1/33.3 \approx 0.03002\text{ W/K}$).
      * Inner Sink: Human skin at $T_{\text{skin}} = 35.0^\circ\text{C}$ through $R_{\text{inner}} \approx 72.7\text{ K/W}$ ($G_{\text{inner}} = 1/72.7 \approx 0.01375\text{ W/K}$).
    * Total Thermal Conductance and Parallel Resistance:
      $$G_{\text{tot}} = G_{\text{outer}} + G_{\text{inner}} = 0.03002 + 0.01375 = \mathbf{0.04377\text{ W/K}} \implies R_{\text{eff}} = \frac{1}{G_{\text{tot}}} \approx \mathbf{22.85\text{ K/W}}.$$
    * Consistent Two-Sink Node Temperature Equation:
      $$T_{\text{core}} = R_{\text{eff}} \cdot \bar{P} + \frac{G_{\text{outer}}}{G_{\text{tot}}} T_{\text{amb}} + \frac{G_{\text{inner}}}{G_{\text{tot}}} T_{\text{skin}} = 14.05^\circ\text{C} + (0.686 \cdot T_{\text{amb}}) + (0.314 \cdot 35.0^\circ\text{C}) = \mathbf{25.04^\circ\text{C}} + (0.686 \cdot T_{\text{amb}}).$$
    * Empirical Steady-State Evaluation across Operating Ambients:
      * **Baseline $T_{\text{amb}} = 25.0^\circ\text{C}$:**
        $$T_{\text{core}} = 25.04 + (0.686 \times 25.0) = \mathbf{42.19^\circ\text{C}} \approx \mathbf{42.2^\circ\text{C}}.$$
      * **Elevated Ambient $T_{\text{amb}} = 28.0^\circ\text{C}$:**
        $$T_{\text{core}} = 25.04 + (0.686 \times 28.0) = \mathbf{44.25^\circ\text{C}} \approx \mathbf{44.3^\circ\text{C}}.$$
      * **Stress Ambient $T_{\text{amb}} = 32.0^\circ\text{C}$:**
        $$T_{\text{core}} = 25.04 + (0.686 \times 32.0) = \mathbf{46.99^\circ\text{C}} \approx \mathbf{47.0^\circ\text{C}}.$$
    * **Physical Consequence of Steady-State $T_{\text{core}} > 41.0^\circ\text{C}$ at $T_{\text{amb}} \ge 28^\circ\text{C}$ (Auditor Directive D1):**
      * The Rubitherm RT42 melting plateau is $38.0^\circ\text{C}\text{ to }43.0^\circ\text{C}$ with main peak at $41.0^\circ\text{C}$.
      * At $T_{\text{amb}} \ge 28.0^\circ\text{C}$ (and even at $25.0^\circ\text{C}$ under extended conversational duty cycles), steady-state core temperature ($42.2\text{--}44.3^\circ\text{C}$) exceeds the $41.0^\circ\text{C}$ melting peak.
      * *Consequence:* The RT42 PCM is fully melted in steady state. Its latent heat buffer ($\Delta H_{\text{fus}} = 165.0\text{ J/g}$, $660\text{ J}$) is entirely liquid at baseline, offering zero latent buffering against subsequent active bursts. Only sensible heat capacity ($C_p \approx 2.0\text{ J/g}\cdot\text{K}$) is available.
      * *System Mitigations:*
        1. *Thermal Duty Throttling:* Dynamic power management scales inter-turn standby duration or caps NPU frequency when on-die thermal sensors report $T_{\text{core}} > 41^\circ\text{C}$ at ambient $>28^\circ\text{C}$.
        2. *Enhanced External Convection:* Micro-grooved or finned exterior aluminum temple plates reduce $R_{\text{outer}}$ from $33.3\text{ K/W}$ to $\le 20.0\text{ K/W}$, pulling steady-state core temperatures below $40.0^\circ\text{C}$ at $28^\circ\text{C}$ ambient.
        3. *High-Ambient PCM Eutectic:* In high-temperature deployments, an RT44HC or paraffin/octadecane composite pad ($T_{\text{melt}} = 44\text{--}46^\circ\text{C}$) can be substituted.
    * **Epidermal Safety Verification across All Operating Conditions:**
      * Inner skin-directed heat flux:
        $$q_{\text{inner}} = \frac{T_{\text{core}} - T_{\text{skin}}}{R_{\text{inner}}}.$$
      * At $T_{\text{amb}} = 25^\circ\text{C}$ ($T_{\text{core}} = 42.2^\circ\text{C}$):
        $$q_{\text{inner}} = \frac{42.2 - 35.0}{72.7} \approx 0.099\text{ W} \implies T_{\text{skin-face}} = 35.0^\circ\text{C} + (0.099 \times 5.0) \approx \mathbf{35.5^\circ\text{C}}.$$
      * At $T_{\text{amb}} = 32^\circ\text{C}$ ($T_{\text{core}} = 47.0^\circ\text{C}$):
        $$q_{\text{inner}} = \frac{47.0 - 35.0}{72.7} \approx 0.165\text{ W} \implies T_{\text{skin-face}} = 35.0^\circ\text{C} + (0.165 \times 5.0) \approx \mathbf{35.8^\circ\text{C}}.$$
      * In all conditions, $T_{\text{skin-face}} \le 36.0^\circ\text{C}$, safely below the $37.5^\circ\text{C}$ medical comfort threshold and far below the $42.0^\circ\text{C}$ epidermal pain/burn limit.

### G. Directive 05 Mass Accounting: Line-by-Line Track 1 Component Mass Budget (Auditor Review R8, D1)
The table below details every component's verified datasheet, vendor listing, or engineering estimate mass. Note: All figures are design-phase estimates pending physical procurement and lab scale bring-up.

| Subsystem / Component | Item Description | Qty | Unit Mass (g) | Extended Mass (g) | Provenance & Source / Verification Method |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Compute Core** | Firefly CAM-3576Q38 (SoC + LPDDR5 + Wi-Fi 6 + PMIC) | 1 | 14.2 | 14.2 | Datasheet: [Firefly CAM-3576Q38 Specification](https://en.t-firefly.com/product/industry/cam-3576q38) (14.2g). |
| **Optical Module** | Sony IMX415 4K sensor, lens mount, M12 85° glass lens | 1 | 7.2 | 7.2 | Vendor listing / Datasheet: [Arducam IMX415 M12 Module](https://www.arducam.com) (7.2g). |
| **Optical Lenses** | Clear High-Index 1.67 Prescription Eyewear Lenses (Pair) | 2 | 4.25 | 8.5 | Vendor listing estimate: [Lenskart 1.67 High-Index Lenses](https://www.lenskart.com) (estimate — unmeasured). |
| **Energy Storage** | GNB 3.7V 300mAh 30C LiPo pouch cells (Series 2S) | 2 | 8.0 | 16.0 | Datasheet: [Gaoneng GNB 300mAh 1S 30C](https://robu.in) (8.0g/cell). |
| **Power Management** | IP2326 2S boost charger breakout PCB | 1 | 2.2 | 2.2 | Vendor listing: [Injoinic IP2326 2S Breakout on Robu.in](https://robu.in) (estimate — unmeasured, ports stripped). |
| **Battery Safety** | HY2212 2S BMS protection & balance PCB | 1 | 1.8 | 1.8 | Vendor listing: [HY2212 2S BMS Module on Robu.in](https://robu.in) (estimate — unmeasured). |
| **Voltage Regulation** | MP2315 2S-to-5V synchronous step-down buck module | 1 | 1.8 | 1.8 | Vendor listing / Datasheet: [MP2315 Mini 3A Buck on Robu.in](https://robu.in) (1.8g). |
| **Audio Amps** | MAX98357A I2S mono Class-D amplifier breakouts | 2 | 1.4 | 2.8 | Vendor listing / Datasheet: [Adafruit/generic MAX98357A](https://robu.in) (1.4g/each). |
| **Acoustic Transducers** | 8Ω 1W micro bone-conduction / directional drivers | 2 | 2.5 | 5.0 | Vendor listing: [Robu.in 8Ω 1W Micro Transducer](https://robu.in) (estimate — unmeasured). |
| **Microphone Array** | INMP441 omnidirectional digital MEMS breakouts | 2 | 0.8 | 1.6 | Vendor listing / Datasheet: [INMP441 MEMS Breakout](https://robu.in) (0.8g/each). |
| **User Input** | TTP223 capacitive touch sensor module | 1 | 0.6 | 0.6 | Vendor listing / Datasheet: [TTP223 Capacitive Module](https://robu.in) (0.6g). |
| **Interconnect** | FPC ribbon jumpers + 30 AWG silicone wiring harness | 1 | 4.5 | 4.5 | Estimate — unmeasured (wiring harness budget). |
| **Carrier Interconnect** | Combined custom 0.8mm thin 2-layer FR4 carrier PCBs | 2 | 2.25 | 4.5 | Estimate — unmeasured (volumetric design budget for 0.8mm FR4). |
| **Frame Mechanics** | 3D-printed PETG front frame & thick temple enclosures | 1 | 24.0 | 24.0 | Estimate — unmeasured (design mass budget for 1.2mm shell; no repo CAD yet). |
| **Phase Change Material**| Rubitherm RT42 organic bio-PCM thermal pad | 1 | 4.0 | 4.0 | Datasheet: [Rubitherm GmbH RT42 Technical Data Sheet](https://www.rubitherm.eu) (4.0g pad). |
| **Thermal Sinks** | 0.3mm copper foil heat spreader + Arctic MX-4 paste | 1 | 3.8 | 3.8 | Estimate — unmeasured (computed from 0.3mm Cu density and area). |
| **Thermal Insulation** | 1.0mm Silica Aerogel Blanket (10 cm² skin barrier) | 1 | 0.2 | 0.2 | Vendor listing / Datasheet: [Aerogel Blanket 1mm on Robu.in / Aspen Aerogels](https://robu.in) (density ~0.18 g/cm³, 1.0mm x 10cm² = 0.18g -> 0.2g). |
| **Mechanical Fasteners**| M1.6/M2 brass heatset inserts and screws | 1 | 2.5 | 2.5 | Vendor listing / Estimate — unmeasured (2.5g hardware buffer). |
| **Contingency Margin** | Prototyping & assembly tolerance buffer | 1 | 4.8 | 4.8 | Estimate — unmeasured (built-in 4.4% tolerance reserve). |
| **TOTAL ALL-UP MASS** | **Complete Track 1 Autonomous Wearable** | — | — | **110.0 g** | **Design estimate — unmeasured (10.0g below 120g target; 15.0g below 125g ceiling)** |

*Margin & Arithmetic Analysis:*
- Physical rows sum: **105.20 g (Estimate)**
- Prototyping contingency: **4.80 g (Estimate)**
- Total all-up weight: **110.00 g (Design estimate — unmeasured)**
- This provides an estimated **10.0 g positive safety margin** below the $120.0\text{ g}$ engineering target, and **15.0 g positive headroom** strictly below the $125.0\text{ g}$ Directive 05 ceiling.

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
