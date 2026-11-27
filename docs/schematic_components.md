# PROJECT FRIDAY: COMPLETE SCHEMATIC COMPONENT SPECIFICATION & LIBRARY DIRECTORY
## Custom 20–22mm x 75mm Wearable Compute Board (Rockchip RK3576 Architecture)

This document itemizes every electrical component required for the schematic capture of Project FRIDAY's custom compute PCB. 
**Source of Truth:** Official Rockchip RK3576 Reference/EVB Schematic and Rockchip Hardware Design Guide (to be provided by student). Every value must cite schematic page/net or component datasheet; any value without a verified source is marked explicitly as **UNVERIFIED**.

---

## 1. Primary Active Silicon (Integrated Circuits)

| Reference | Component Name & Role | Manufacturer & MPN | Sourcing Status | Package / Footprint | Pin Count & Pitch | Design Rules & Electrical Constraints | Autodesk / Eagle Library Source |
|:---:|:---|:---|:---:|:---|:---:|:---|:---|
| **U1** | **Rockchip RK3576 SoC**<br>Core 8 nm FinFET 8-Core Application Processor & 6-TOPS NPU | Rockchip<br>`RK3576` | LCSC `C42388007`<br>(Catalog orderable) | **FCCSP-698L**<br>(16.1 x 17.2 mm) | 698 Balls<br>**Ball Pitch: 0.55 / 0.60 / 0.65 mm mixed**<br>Ball Size: 0.30 mm | • Mixed 0.55/0.60/0.65 mm pitch strictly drives 6-layer HDI fabrication rules (laser-drilled microvias L1-L2, minimum 0.09 mm trace/space, via-in-pad)<br>• LPDDR4X 32-bit bus length matching: skew < 0.2 mm<br>• 100Ω differential impedance on MIPI CSI-2 camera pairs<br>• 90Ω differential impedance on USB 2.0 D+/D- lines | RK3576 DS Rev 1.5 §1.2 p.23 & §2 p.24; library UNVERIFIED (pending EVB import) |
| **U2** | **Rockchip RK806S-5 PMIC**<br>Multi-rail companion power management IC (Dedicated RK3576 OTP Variant) | Rockchip<br>`RK806S-5` | **UNVERIFIED Sourcing**<br>(Requires Rockchip authorized distributor / franchised channel; not standard LCSC catalog orderable) | **QFN-68**<br>(7.0 x 7.0 mm) | 68 Pins + EP<br>0.35 mm pin pitch | • **Host Control Interface:** Follows **EVB default SPI mode** with **CS (Pin 18) floating / connected to GND** (EVB Sheet 23 p.21 note). Optional I2C mode available if CS tied to VCCA.<br>• **OTP Rails & Voltage Defaults:** Configured with RK3576-specific OTP power tree (EVB Sheet 05 p.6 & HDG §2).<br>• Exposed ground thermal pad requires minimum 16 vias to solid GND plane.<br>• Inductor and input/output cap placement strictly adheres to HDG §3.7 layout guidelines. | EVB Sheet 05 p.6, Sheet 23 p.21; HDG §2; Library: UNVERIFIED |
| **U3** | **Samsung 4GB LPDDR4X + 64GB eMMC eMCP**<br>Unified RAM & fast OS flash memory | Samsung<br>`KM3V...` series | Consigned Part<br>(Harvested locally; not catalog-orderable from JLCPCB) | **BGA-254**<br>(11.5 x 13.0 mm) | 254 Balls<br>0.5 mm ball pitch | • Sits directly adjacent to RK3576 DDR controller ball bank<br>• High-speed DQ/DQS traces routed on Layer 3 (stripline between solid GND planes)<br>• Guard traces and GND stitching vias every 3 mm along DDR bus | Standard JEDEC BGA-254 (`bga254.lbr` / SnapEDA) |
| **U4** | **Realtek RTL8723DS Wi-Fi / Bluetooth IC**<br>2.4 GHz 802.11b/g/n + BT 4.2 radio | Realtek<br>`RTL8723DS-CG` | LCSC `C2762334`<br>(Catalog orderable) | **WQFN-48**<br>(6.0 x 6.0 mm) | 48 Pins + EP<br>0.4 mm pin pitch | • 50Ω coplanar waveguide with ground reference to antenna matching network<br>• Solid ground keepout under RF matching pi-network<br>• SDIO clock and data lines length matched within 1.0 mm | LCSC / EasyEDA Pre-Made Footprint (`C2762334.lbr`) |
| **U5** | **Priority Power Multiplexer (Power-Path)**<br>Reverse-blocking dual-input selector (4.5 A rated) | Texas Instruments<br>`TPS2121RUXR` | LCSC / TI<br>(Catalog orderable) | **WQFN-12**<br>(2.0 x 2.5 mm, 0.5mm pitch) | 12 Pins + EP | • Rated continuous current: 4.5 A (R_DS(on) = 56 mΩ typical)<br>• Auto-switches between `VBUS_5V` (USB-C) and `VBAT_BUCK_5V` (MP2315 buck)<br>• Electrical drop at 3.0 A load: ΔV = 3.0A * 0.056Ω = 0.17 V<br>• Heat dissipation at 3.0 A: P_loss = (3.0A)^2 * 0.056Ω = 0.50 W | TI Footprint (`TPS2121_RUX.lbr`) |

---

## 2. Power Tree & Voltage Sequencing Table
**Source of Truth:** Official Rockchip RK3576 EVB1 Schematic (`RK_EVB1_RK3576_LP4XD200P132SD6_V12`, Sheets 04, 05, 23, 24) & RK3576 Hardware Design Guide (HDG §2.2 & §3.7).

### 2.1 RK806S-5 PMIC & Discrete Power Rail Distribution (EVB Sheet 05 p.6 "Power Description")

| Power Rail Name | Work Voltage | Source Regulator & Channel | Time Slot | Default State | Rated Current | Passives & Decoupling Sizing (EVB Sheet 05/23/24) | Source Citation |
|---|:---:|---|:---:|:---:|:---:|---|:---:|
| **VCC5V0_SYS_S5** | **5.00 V** | Primary System Bus via U5 (TPS2121) | Slot: 0 | ON | **5.0 A** | Input bypass: 22 µF at each PMIC buck VCC pin; bulk 10 µF | EVB Sheet 05 p.6 |
| **VDD_CPU_BIG_S0** | **0.75 V (DVFS)** | **RK806S-5 BUCK 1** | Slot: 5 | ON | 6.5 A | Inductor: **0.22 µH** (Isat ≥ 6.5A); Output: **3x 22 µF** 6.3V; total cap > 130 µF behind BGA (HDG §2.2.2.5) | EVB Sheet 05 p.6 |
| **VDD_NPU_S0** | **0.75 V (DVFS)** | **RK806S-5 BUCK 2** | Slot: 2 | ON | 5.0 A | Inductor: **0.22 µH** (Isat ≥ 5.0A); Output: **3x 22 µF** 6.3V; total cap > 90 µF (HDG §2.2.2.8) | EVB Sheet 05 p.6 |
| **VDD_CPU_LIT_S0** | **0.75 V (DVFS)** | **RK806S-5 BUCK 3** | Slot: 2 | ON | 5.0 A | Inductor: **0.22 µH** (Isat ≥ 5.0A); Output: **3x 22 µF** 6.3V; total cap > 88 µF (HDG §2.2.2.6) | EVB Sheet 05 p.6 |
| **VCC_3V3_S3** | **3.30 V** | **RK806S-5 BUCK 4** | Slot: 2 | ON | 5.0 A | Inductor: **0.22 µH** (Isat ≥ 5.0A); Output: **3x 22 µF** 10V; feeds 3.3V sleep domains & load switch | EVB Sheet 05 p.6 |
| **VDD_GPU_S0** | **0.75 V (DVFS)** | **RK806S-5 BUCK 5** | Slot: 2 | ON | 3.0 A | Inductor: **0.47 µH** (Isat ≥ 3.0A); Output: **2x 22 µF** 6.3V; FB ADJ ($V_{\text{fb}} = 0.5\text{ V}$) | EVB Sheet 05 p.6 |
| **VDDQ_DDR_S0** | **0.61 V (LP4X)** | **RK806S-5 BUCK 6** | Slot: 7 | ON | 3.0 A | Inductor: **0.47 µH**; Output: **2x 22 µF**; FB ADJ via HDG Fig 2-13 divider (0.61V for LPDDR4X, 0.51V for LP5) | EVB Sheet 05 p.6 & HDG Fig 2-13 |
| **VDD_LOGIC_S0 / MEM**| **0.75 V** | **RK806S-5 BUCK 7** | Slot: 2 | ON | 3.0 A | Inductor: **0.47 µH** (Isat ≥ 3.0A); Output: **2x 22 µF** 6.3V; powers core logic & logic RAM array | EVB Sheet 05 p.6 & HDG §2.2.2.9 |
| **VCC_1V8_S3** | **1.80 V** | **RK806S-5 BUCK 8** | Slot: 5 | ON | 3.0 A | Inductor: **0.47 µH** (Isat ≥ 3.0A); Output: **2x 22 µF** 10V; feeds 1.8V sleep domains & load switch | EVB Sheet 05 p.6 |
| **VDD2_DDR_S3** | **1.10 V (LP4X)** | **RK806S-5 BUCK 9** | Slot: 4 | ON | 3.0 A | Inductor: **0.47 µH**; Output: **2x 22 µF**; FB ADJ via HDG Fig 2-14 divider (1.10V for LPDDR4X, 1.05V for LP5) | EVB Sheet 05 p.6 & HDG Fig 2-14 |
| **VDD_DDR_S0** | **0.75 V** | **RK806S-5 BUCK 10** | Slot: 2 | ON | 3.0 A | Inductor: **0.47 µH** (Isat ≥ 3.0A); Output: **2x 22 µF** 6.3V; powers DDR controller digital logic | EVB Sheet 05 p.6 |
| **VCC_2V0_PLDO_S3** | **2.094 V (~2.1V)**| **External Discrete Buck 1** (TMI3112H / MP2143) | Slot: 1 | ON | 2.0 A | Inductor: **1.0 µH** (Isat ≥ 3.2A); Input: 10 µF; Output: 2x 22 µF; feeds PMIC PLDO inputs (VCC11/12) | EVB Sheet 24 p.22 |
| **VCC_1V1_NLDO_S3** | **1.10 V** | **External Discrete Buck 2** (TMI3112H / MP2143) | Slot: 1 | ON | 2.0 A | Inductor: **1.0 µH** (Isat ≥ 3.2A); Input: 10 µF; Output: 2x 22 µF; feeds PMIC NLDO inputs (VCC13/14) | EVB Sheet 24 p.22 |
| **VCCA_1V8_S0** | **1.80 V** | **RK806S-5 PLDO 1** | Slot: 3 | ON | 0.5 A | Output: **2.2 µF** 10V X5R (fed from intermediate rail `VCC_2V0_PLDO_S3`, $\Delta V = 0.3\text{ V}$) | EVB Sheet 05 p.6 |
| **VCCA1V8_PLDO2_S0** | **1.80 V** | **RK806S-5 PLDO 2** | Slot: 3 | ON | 0.3 A | Output: **2.2 µF** 10V X5R (fed from intermediate rail `VCC_2V0_PLDO_S3`, $\Delta V = 0.3\text{ V}$) | EVB Sheet 05 p.6 |
| **VDDA_1V2_S0** | **1.20 V** | **RK806S-5 PLDO 3** | Slot: 4 | ON | 0.3 A | Output: **2.2 µF** 10V X5R (fed from `VCC_2V0_PLDO_S3`; powers MIPI DCPHY / UFS MPHY) | EVB Sheet 05 p.6 |
| **VCCA_3V3_S0** | **3.30 V** | **RK806S-5 PLDO 4** | Slot: 5 | ON | 0.5 A | Output: **2.2 µF** 10V X5R (fed from `VCC5V0_SYS_S5`) | EVB Sheet 05 p.6 |
| **VCCIO_SD_S0** | **3.30 V / 1.80 V** | **RK806S-5 PLDO 5** | Slot: 5 | ON | 0.3 A | Output: **2.2 µF** 10V X5R (powers SDIO / MicroSD card I/O) | EVB Sheet 05 p.6 |
| **VCCA1V8_PLDO6_S3** | **1.80 V** | **RK806S-5 PLDO 6** | Slot: 3 | ON | 0.3 A | Output: **2.2 µF** 10V X5R (powers `RESETB` & analog control blocks) | EVB Sheet 05 p.6 |
| **VDDA_DDR_PLL_S0** | **0.85 V** | **RK806S-5 NLDO 1** | Slot: 2 | ON | 0.3 A | Output: **2.2 µF** 6.3V X5R (fed from intermediate rail `VCC_1V1_NLDO_S3`, $\Delta V = 0.25\text{ V}$) | EVB Sheet 05 p.6 |
| **VDD_0V75_S3** | **0.75 V** | **RK806S-5 NLDO 2** | Slot: 2 | ON | 0.3 A | Output: **2.2 µF** 6.3V X5R (fed from `VCC_1V1_NLDO_S3`; powers PMU core in sleep) | EVB Sheet 05 p.6 |
| **VDDA0V75_HDMI_S0**| **0.75 V** | **RK806S-5 NLDO 3** | Slot: 2 | ON | 0.5 A | Output: **2.2 µF** 6.3V X5R (fed from `VCC_1V1_NLDO_S3`; powers HDMI/eDP digital core) | EVB Sheet 05 p.6 |
| **VDDA_0V85_S0** | **0.85 V** | **RK806S-5 NLDO 4** | Slot: 2 | ON | 0.5 A | Output: **2.2 µF** 6.3V X5R (fed from `VCC_1V1_NLDO_S3`; powers USB3 OTG & PCIe Combo PHYs) | EVB Sheet 05 p.6 |
| **VDDA_0V75_S0** | **0.75 V** | **RK806S-5 NLDO 5** | Slot: 2 | ON | 0.3 A | Output: **2.2 µF** 6.3V X5R (fed from `VCC_1V1_NLDO_S3`; powers MIPI CSI RX & USB2 PHYs) | EVB Sheet 05 p.6 |
| **VCC_3V3_S0** | **3.30 V** | **Load Switch U2403** (SGM2590D / CW3301) | Slot: 5A | ON | 2.0 A | Switched from `VCC_3V3_S3`. **Powers eMMC 3.3V `VCC` core and active 3.3V peripherals** (no dedicated buck) | EVB Sheet 22 p.22 |
| **VCC_1V8_S0** | **1.80 V** | **Load Switch U2402** (CW3301 / SGM2590D) | Slot: 3A | ON | 2.0 A | Switched from `VCC_1V8_S3`. **Powers eMMC 1.8V `VCCQ` bus, camera 1.8V I/O, and audio logic** | EVB Sheet 22 p.22 |

---

### 2.2 System Power Bus (VSYS_5V) Simultaneous-Load Sizing & Current Budget Analysis

Rockchip RK3576 EVB1 specifies a **5.0 A rated 5.0 V primary regulator** (`VCC5V0_SYS_S5`, EVB Sheet 04/05). The following table analyzes simultaneous real-world operating loads on the glasses compute platform using current specifications from HDG §2.2:

| Platform Operating State | Active Silicon & Core Load Elements | Typical System Power | Primary Bus Current @ 5.0 V (`VSYS_5V`) | MP2315 Battery Buck (3.0 A Rating) | TI TPS2121 Mux (4.5 A Rating) | Engineering Verdict & Sizing Flag |
|---|---|:---:|:---:|:---:|:---:|---|
| **Standby / Audio Idle** | A53 cores in low-power idle; A72 & NPU clock-gated; Wi-Fi in DTIM3 beacon listen; audio muted; camera sensor powered down. | ~1.0 W | **0.20 A** | **PASS** (7% load) | **PASS** (4% load) | Ample headroom. |
| **Live Vision OCR / Translation** | Camera capturing 1080p @ 30fps; A72 cluster active preprocessing; NPU running periodic quantized OCR inference bursts; Wi-Fi idle. | ~5.8 W | **1.16 A** | **PASS** (39% load) | **PASS** (26% load) | Stable continuous wearable operation. |
| **Worst-Case Peak: Concurrent Edge-AI LLM Generation + Audio TTS + Wi-Fi TX** | Quad-core A72 @ 2.2 GHz full prompt evaluation (>4 A core, HDG §2.2.2.5); NPU @ 6 TOPS burst (>4 A, HDG §2.2.2.8); LPDDR4X 4GB bus bursting; dual MAX98357A speakers at loud volume (~2 W audio); Wi-Fi active TX packet burst (~1 W). | ~16.5 W (transient peak) | **Nominal: 2.45 A<br>Transient Spike: 3.2 A – 3.5 A** | **FLAGGED: INSUFFICIENT / MARGINAL** (Exceeds 3.0A continuous rating; risks OCP shutdown or thermal throttling) | **PASS** (78% of 4.5A continuous limit; drop ΔV = 0.19V, heat = 0.68W) | **DESIGN SIZING MANDATE:** Sits within TPS2121 capacity, but **MP2315 (3.0 A) must be upgraded to a 5.0 A synchronous buck converter** (e.g., MPS MP2315S, SGMICRO SGM61320, or TI TPS62864 rated ≥ 5.0 A, matching EVB's 5.0 A `VCC5V0_SYS_S5` design) to guarantee stability under concurrent peak Edge-AI compute. |

---

### 2.3 Standby RTC Clock Architecture Selection (HDG §2 Table 2-1)
* **Architecture Selection:** **Internal PMU_PVTM Module (No External Crystal / Oscillator Required)**.
* **Technical Rationale:** Per Rockchip RK3576 Hardware Design Guide §2 (Page 5–6, Table 2-1), RK3576 supports switching its standby clock to the internal `PMU_PVTM` module, allowing the external 24 MHz crystal to power down during sleep while maintaining PMUIO wake-up. For an ultra-dense $20\text{--}22\text{ mm} \times 75\text{ mm}$ wearable glasses PCB, selecting `PMU_PVTM` eliminates discrete 32.768 kHz crystals and RTC ICs, saving critical board area and BOM cost.

---

### 2.4 Memory & Storage Architecture: eMCP-254 vs. EVB Reference Design (HDG §2.1.7 & §3.6)
* **EVB Configuration:** EVB1 uses discrete 200-ball LPDDR4X SDRAM (`DRAM-LPDDR4X_1X32bit_200P`, Sheet 38) and discrete 153-ball eMMC 5.1 Flash (Sheet 40).
* **Project FRIDAY Wearable Configuration:** Integrated single-package **BGA-254 eMCP** (Samsung 4GB LPDDR4X + 64GB eMMC).
* **Layout Rule Mandate:** The EVB memory layout **cannot be copied directly**. eMCP-254 ball breakout, stripline impedance (Layer 3/5 sandwiched between solid GND planes), length matching ($\Delta L \le 0.2\text{ mm}$ for DQ/DQS, $\le 0.5\text{ mm}$ for CA/CLK), and decoupling must strictly follow **Rockchip RK3576 HDG §2.1.7 (DDR Schematic Design) and §3.6 (DDR PCB Layout Guidelines)**.

---

## 3. Frequency Control & Clocks

| Reference | Frequency | Tolerance & Load | Manufacturer & MPN | LCSC Part # | Package / Footprint | Design Rules & Load Sizing (Formula: C = 2*(CL - Cstray)) | Library Source |
|:---:|:---:|:---:|---|:---:|---|:---|:---|
| **Y1** | **24.000 MHz** | ±10 ppm<br>CL = 12 pF | YXC<br>`X322524MOB4SI` | `C70590` | **SMD-3225-4P**<br>(3.2 x 2.5 mm) | Master SoC clock. Load caps C1, C2 = 18 pF (0402 C0G), calculated via 2*(12 pF - 3 pF stray) = 18 pF. Guard ring of solid GND surrounding traces; no digital routing under crystal. | Fusion `crystal.lbr` / LCSC `C70590` |
| **Y2 (REMOVED)** | *N/A* | *Internal PVTM* | *N/A* | *N/A* | *N/A* | **PMU Standby Clock Selection (HDG §2 Table 2-1):** Choice confirmed as **Internal PMU_PVTM module** (requires zero external crystal or oscillator components; saves critical board area on glasses frame). RK806S-5 integrates an internal 32.768 kHz RC oscillator; no external RTC crystal required. Discrete Y2 and C3/C4 removed. | HDG §2 Table 2-1 p.5–6; EVB Sheet 04 |
| **Y3** | **26.000 MHz** | ±10 ppm<br>CL = 12 pF | Standard 26MHz (UNVERIFIED) | LCSC / generic | **SMD-2016-4P**<br>(2.0 x 1.6 mm) | Dedicated reference clock for RTL8723DS Wi-Fi/BT transceiver. Load caps C5, C6 = 18 pF (0402 C0G). Placed adjacent to RTL8723DS XTAL pins. | UNVERIFIED (pending RTL8723DS ref design) |

---

## 4. Power Inductors & Ferrite Beads (Sized per RK806S-5 EVB Sheet 05/23/24 & HDG §2.2)

| Reference | Value / Inductance | Rating & Specs | Package | Qty | Circuit Function & Target Rail | Design Rules & Datasheet Citation |
|:---:|:---:|:---|:---:|:---:|:---|:---|
| **L1** | **0.22 µH** | Isat ≥ 6.5 A, DCR < 25 mΩ | SMD 2016 (2.0 x 1.6 mm) | 1 | **RK806S-5 Buck 1 Switching Node:** Powers `VDD_CPU_BIG_S0` | Place < 1.5 mm from PMIC SW1 pin (EVB Sheet 05 p.6 & HDG §2.2.2.5) |
| **L2** | **0.22 µH** | Isat ≥ 5.0 A, DCR < 25 mΩ | SMD 2016 (2.0 x 1.6 mm) | 1 | **RK806S-5 Buck 2 Switching Node:** Powers `VDD_NPU_S0` | Place < 1.5 mm from PMIC SW2 pin (EVB Sheet 05 p.6 & HDG §2.2.2.8) |
| **L3** | **0.22 µH** | Isat ≥ 5.0 A, DCR < 25 mΩ | SMD 2016 (2.0 x 1.6 mm) | 1 | **RK806S-5 Buck 3 Switching Node:** Powers `VDD_CPU_LIT_S0` | Place < 1.5 mm from PMIC SW3 pin (EVB Sheet 05 p.6 & HDG §2.2.2.6) |
| **L4** | **0.22 µH** | Isat ≥ 5.0 A, DCR < 25 mΩ | SMD 2016 (2.0 x 1.6 mm) | 1 | **RK806S-5 Buck 4 Switching Node:** Powers `VCC_3V3_S3` | Place < 1.5 mm from PMIC SW4 pin (EVB Sheet 05 p.6) |
| **L5** | **0.47 µH** | Isat ≥ 3.0 A, DCR < 35 mΩ | SMD 2016 (2.0 x 1.6 mm) | 1 | **RK806S-5 Buck 5 Switching Node:** Powers `VDD_GPU_S0` | Place < 1.5 mm from PMIC SW5 pin (EVB Sheet 05 p.6 & HDG §2.2.2.7) |
| **L6** | **0.47 µH** | Isat ≥ 3.0 A, DCR < 35 mΩ | SMD 2016 (2.0 x 1.6 mm) | 1 | **RK806S-5 Buck 6 Switching Node:** Powers `VDDQ_DDR_S0` (0.61V LP4X) | Place < 1.5 mm from PMIC SW6 pin (EVB Sheet 05 p.6 & HDG Fig 2-13) |
| **L7** | **0.47 µH** | Isat ≥ 3.0 A, DCR < 35 mΩ | SMD 2016 (2.0 x 1.6 mm) | 1 | **RK806S-5 Buck 7 Switching Node:** Powers `VDD_LOGIC_S0 / MEM` | Place < 1.5 mm from PMIC SW7 pin (EVB Sheet 05 p.6 & HDG §2.2.2.9) |
| **L8** | **0.47 µH** | Isat ≥ 3.0 A, DCR < 35 mΩ | SMD 2016 (2.0 x 1.6 mm) | 1 | **RK806S-5 Buck 8 Switching Node:** Powers `VCC_1V8_S3` | Place < 1.5 mm from PMIC SW8 pin (EVB Sheet 05 p.6) |
| **L9** | **0.47 µH** | Isat ≥ 3.0 A, DCR < 35 mΩ | SMD 2016 (2.0 x 1.6 mm) | 1 | **RK806S-5 Buck 9 Switching Node:** Powers `VDD2_DDR_S3` (1.10V LP4X) | Place < 1.5 mm from PMIC SW9 pin (EVB Sheet 05 p.6 & HDG Fig 2-14) |
| **L10**| **0.47 µH** | Isat ≥ 3.0 A, DCR < 35 mΩ | SMD 2016 (2.0 x 1.6 mm) | 1 | **RK806S-5 Buck 10 Switching Node:** Powers `VDD_DDR_S0` | Place < 1.5 mm from PMIC SW10 pin (EVB Sheet 05 p.6) |
| **L11**| **1.0 µH** | Isat ≥ 3.2 A, DCR < 65 mΩ | SMD 2520 (2.5 x 2.0 mm) | 1 | **External Buck 1 Switching Node (L2400):** Powers `VCC_2V0_PLDO_S3` | Sits between U2400 (TMI3112H/MP2143) and PMIC VCC11/12 (EVB Sheet 24 p.22) |
| **L12**| **1.0 µH** | Isat ≥ 3.2 A, DCR < 65 mΩ | SMD 2520 (2.5 x 2.0 mm) | 1 | **External Buck 2 Switching Node (L2401):** Powers `VCC_1V1_NLDO_S3` | Sits between U2401 (TMI3112H/MP2143) and PMIC VCC13/14 (EVB Sheet 24 p.22) |
| **FB1** | **120 Ω @ 100MHz** | 2.0 A Continuous, DCR < 40 mΩ | SMD 0603 (1.6 x 0.8 mm) | 1 | **Audio Rail Filter:** Isolates 5.0V audio supply from switching ripple | Place at boundary between system 5.0V and audio amplifier VDD island |
| **FB2** | **120 Ω @ 100MHz** | 2.0 A Continuous, DCR < 40 mΩ | SMD 0603 (1.6 x 0.8 mm) | 1 | **Wi-Fi RF Filter:** Isolates RTL8723DS 3.3V power from CPU noise | Place at entrance of RTL8723DS power plane |

---

## 5. Protection Devices & Power-Path

| Reference | Component Type | Specifications | Package | Qty | Circuit Function & Target Nets |
|:---:|:---|:---|:---:|:---:|:---|
| **D1** | **TVS ESD Diode Array** | 4-Channel, 5.0 V clamp, ultra-low capacitance (< 0.5 pF) | SOT-23-6 / DFN-10 | 1 | **USB-C High-Speed Line ESD Protection:** Clamps static shock on `USB_DP`, `USB_DN`, `USB_CC1`, and `USB_CC2`. Place immediately behind USB-C connector pads. |
| **D2** | **VBUS High-Energy TVS Diode** | Unidirectional 5.0 V / 6.0 V clamp, high surge capability | SOD-323 / SMA | 1 | **USB VBUS Transient Clamp:** Clamps inductive voltage spikes when hot-plugging USB-C 5V charger. Place directly at `VBUS` entry pad. |
| **U5** | **Priority Power Multiplexer (Power-Path)** | Texas Instruments `TPS2121RUXR` (continuous rating 4.5 A, R_DS(on) = 56 mΩ typ) | WQFN-12 (2.0 x 2.5 mm, 0.5mm pitch) | 1 | **Power-Path Control:** Sits between `VBUS_5V` and `VBAT_BUCK_5V`. Automatically priority-switches system `VSYS_5V` to USB-C power when plugged in, preventing backfeeding into MP2315 battery buck.<br>• Electrical drop at 3.0 A: **ΔV = 0.17 V** (3.0A * 0.056Ω)<br>• Heat dissipation at 3.0 A: **P_loss = 0.50 W** ((3.0A)^2 * 0.056Ω) |

---

## 6. Resistors (All SMD 0402, 1% Tolerance, 1/16 W / 62.5 mW unless noted)

| Reference | Resistance | Tolerance | Wattage | Package | Qty | Target Circuit & Functional Role | Source / Design Citation |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---|
| **R1, R2** | **5.1 kΩ** | ±1% | 1/16 W | SMD 0402 | 2 | **USB-C CC Pull-Downs:** Connects `CC1` and `CC2` to GND (advertises 5V sink capability to host charger). | USB Type-C Cable & Connector Specification §4.5.1 |
| **R3, R4** | **2.2 kΩ** | ±1% | 1/16 W | SMD 0402 | 2 | **Camera I2C Pull-Ups:** Pulls up `I2C_CAM_SDA` and `I2C_CAM_SCL` strictly to **1.8 V (`VCCIO_1V8`)**, matching Sony IMX708 sensor digital I/O domain. | Sony IMX708 Datasheet & RPi Camera V3 Schematic |
| **R5, R6** | **22 Ω / Jumper**| ±1% | 1/16 W | SMD 0402 | 2 | **Host PMIC Control Bus (EVB Default SPI Mode):** Follows **EVB default SPI mode** with **CS (Pin 18) floating or tied to GND** (EVB Sheet 23 p.21 note). Optional in-line damping on `SPI_CLK` and `SPI_MOSI`. (If I2C mode is chosen later, CS is tied to VCCA and 10k pull-ups are populated). | EVB Sheet 23 p.21 note |
| **R7, R8** | **10 kΩ** | ±1% | 1/16 W | SMD 0402 | 2 | **Logic Pull-Ups & Straps:** Pulls up `PMIC_PWRON` and hardware reset lines to matching I/O domain. | UNVERIFIED |
| **R9** | **10 kΩ** | ±1% | 1/16 W | SMD 0402 | 1 | **Mic Channel Select:** Sets INMP441 `L/R` channel address. | InvenSense INMP441 Datasheet Table 4 |
| **R10** | **10 kΩ** | ±1% | 1/16 W | SMD 0402 | 1 | **MAX98357A Left Channel Pull-Up:** Pulls up `SD_MODE` to 3.3 V on Left amplifier (yields ~3.0 V with internal 100k pulldown; threshold > 1.39 V selects Left channel). Amplifier VDD is 5.0 V (`VSYS_5V`). *Note: Verify whether breakout module already carries onboard resistor.* | Maxim MAX98357A Datasheet Table 1 |
| **R11** | **220 kΩ** | ±1% | 1/16 W | SMD 0402 | 1 | **MAX98357A Right Channel Pull-Up:** Pulls up `SD_MODE` to 3.3 V on Right amplifier (yields ~1.03 V with internal 100k pulldown; voltage falls inside 0.77 V – 1.39 V window selecting Right channel). Amplifier VDD is 5.0 V (`VSYS_5V`). *Note: Verify whether breakout module already carries onboard resistor.* | Maxim MAX98357A Datasheet Table 1 |
| **R12, R13**| **100 kΩ** | ±1% | 1/16 W | SMD 0402 | 2 | **Audio Gain Limiting:** Ties MAX98357A `GAIN` pin to VDD (configures lowest +3 dB gain setting, capping power below 0.8 W RMS to prevent speaker voice-coil damage). Amplifier VDD is 5.0 V (`VSYS_5V`). | Maxim MAX98357A Datasheet Table 2 |
| **R14, R15**| **22 Ω** | ±1% | 1/16 W | SMD 0402 | 2 | **Master Clock Series Damping:** In-line on 24.000 MHz crystal `OSC_OUT` to eliminate harmonic ringing. | UNVERIFIED (Rockchip hardware design guide) |
| **R16–R18**| **10k, 88.7k, 100R**| ±1% | 1/16 W | SMD 0402 | 3 | **Boot Strapping & MaskROM Network:** `R16` (10 kΩ pull-up to `SARADC_AVDD1V8`) and `R17` (88.7 kΩ pull-down to GND) configure default eMMC boot order (`Config 1: EMMC->SDMMC0->USB`, ADC value 3680). `R18` (100 Ω) provides in-line damping to MaskROM switch `SW1`. | EVB Sheet 11 p.11 & Sheet 42 p.26 |
| **R19–R21**| **110k, 22k, 120k**| ±1% | 1/16 W | SMD 0402 | 3 | **RK806S-5 BUCK6 FB Divider (R2314/R2308/R2309):** Sets `VDDQ_DDR_S0` to **0.61 V** for LPDDR4X. | HDG Fig 2-13 p.36 & EVB Sheet 23 p.21 |
| **R22–R24**| **120k, 100k, 100k**| ±1% | 1/16 W | SMD 0402 | 3 | **RK806S-5 BUCK9 FB Divider (R2313/R2310/R2315):** Sets `VDD2_DDR_S3` to **1.10 V** for LPDDR4X. | HDG Fig 2-14 p.36 & EVB Sheet 23 p.21 |
| **R25, R26**| **249k, 100k** | ±1% | 1/16 W | SMD 0402 | 2 | **External Buck 1 FB Divider (R2404/R2405):** Sets `VCC_2V0_PLDO_S3` output to **2.094 V (~2.1 V)** from 0.6 V reference. | EVB Sheet 24 p.22 |
| **R27, R28**| **120k, 100k** | ±1% | 1/16 W | SMD 0402 | 2 | **External Buck 2 FB Divider (R2407/R2408):** Sets `VCC_1V1_NLDO_S3` output to **1.10 V** from 0.6 V reference. | EVB Sheet 24 p.22 |
| **R29–R32**| **0 Ω (Jumper)**| — | 1/16 W | SMD 0402 | 4 | **RF & Ground Tuning Links:** In-line antenna 50Ω jumper and ground isolation star connections. | UNVERIFIED |

---

## 7. Capacitors (SMD Multilayer Ceramic - MLCC)

| Reference | Capacitance | Voltage Rating | Dielectric | Package | Qty | Target Circuit & Functional Role | Source / Sizing Rule |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---|
| **C1, C2** | **18 pF** | 50 V | C0G / NP0 | SMD 0402 | 2 | **24.000 MHz Crystal Load Capacitors:** From `OSC_IN` / `OSC_OUT` to crystal GND. | Formula: 2*(12 pF - 3 pF stray) = 18 pF |
| **C3, C4 (REMOVED)**| *N/A* | *N/A* | *N/A* | *N/A* | *N/A* | **Removed with Y2:** System uses RK3576 internal PMU_PVTM oscillator (HDG §2 Table 2-1 & EVB Sheet 11 p.11); zero external 32.768 kHz crystal or load capacitors required. | HDG §2 Table 2-1 & EVB Sheet 11 p.11 |
| **C5, C6** | **18 pF** | 50 V | C0G / NP0 | SMD 0402 | 2 | **26.000 MHz Wi-Fi Crystal Load Capacitors:** From RTL8723DS XTAL pins to GND. | Formula: 2*(12 pF - 3 pF stray) = 18 pF (UNVERIFIED) |
| **C7–C18** | **22 µF / 10 µF** | 10 V | X5R | SMD 0603 | 12 | **PMIC & Discrete Buck Input Bypass Capacitors:** 1x 22 µF placed directly at each PMIC buck supply input pin (VCC1 through VCC10) from `VCC5V0_SYS_S5`, plus 10 µF input ceramic caps placed at inputs of external bucks U2400/U2401. | EVB Sheet 23 p.21 & Sheet 24 p.22 |
| **C19–C34** | **100 nF (0.1 µF)**| 10 V | X5R / X7R | SMD 0402 | 16 | **High-Frequency Decoupling Array:** Distributed on the back side of PCB under RK3576 BGA power balls and eMCP balls. | **UNVERIFIED (exact capacitor count, values, and rail distribution pending official RK3576 PDN design guide)** |
| **C35–C42**| **2.2 µF / 1.0 µF** | 10 V | X5R | SMD 0402 | 8 | **PMIC LDO Output & Input Decoupling:** 2.2 µF placed at each active LDO output; 1.0 µF placed at LDO input supply pins (VCC11/12 fed from `VCC_2V0_PLDO_S3`, VCC13/14 fed from `VCC_1V1_NLDO_S3`, and VCCA). | EVB Sheet 23 p.21 |
| **C43–C46**| **4.7 µF** | 10 V | X5R / X7R | SMD 0603 | 4 | **Peripherals Decoupling:** RTL8723DS Wi-Fi 3.3V rail and IMX708 camera interface connector. | UNVERIFIED |
| **C47–C52**| **10 µF** | 16 V / 25 V | X5R / X7R | SMD 0603 | 6 | **Bulk Input Filters:** Placed at 5.0V system power bus entry (`VSYS_5V`), USB-C VBUS, and dual MAX98357A audio amplifier 5.0V VDD pins. | UNVERIFIED |
| **C53–C80**| **22 µF** | 6.3V / 10V | X5R | SMD 0603 | 28 | **PMIC & External Buck Switching Output Filters:** Sized per EVB1 reference schematics: **3x 22 µF** in parallel at high-current buck outputs (BUCK1–BUCK4: `VDD_CPU_BIG`, `VDD_NPU`, `VDD_CPU_LIT`, `VCC_3V3_S3`); **2x 22 µF** in parallel at remaining PMIC buck outputs (BUCK5–BUCK10: `VDD_GPU`, `VDDQ_DDR`, `VDD_LOGIC`, `VCC_1V8_S3`, `VDD2_DDR`, `VDD_DDR`); and **2x 22 µF** in parallel at external bucks U2400 (`VCC_2V0_PLDO_S3`) and U2401 (`VCC_1V1_NLDO_S3`). | EVB Sheet 23 p.21 & Sheet 24 p.22 |

---

## 8. Connectors, Mechanical Controls & Debug Test Points

| Reference | Component Description | Manufacturer & MPN | Package / Footprint | Pin Count & Signals | Physical Location & Electrical Specs |
|:---:|:---|:---|:---|:---|:---|
| **J1** | **USB Type-C Receptacle (16-Pin)** | Korean Hroparts `TYPE-C-31-M-12` (LCSC `C165948`) | 16-Pin SMD Right Angle | 5V Power, GND, D+, D-, CC1, CC2 | Bottom-rear of right temple arm (5V / 3A rating) |
| **J2** | **MIPI CSI Camera FPC Connector** | Hirose / Amphenol 0.5mm pitch | 26-Pin 0.5mm Bottom Contact | 2-Lane MIPI CSI (Clk ±, D0 ±, D1 ±), 1.8V VCCIO, 3.3V, I2C, Reset, PWDN | Front-right browline edge (connects to front-bridge sensor PCB) |
| **J3** | **Audio & Mic Interconnect Header** | 0.5mm pitch FPC | 10-Pin 0.5mm Bottom Contact | I2S DOUT, DIN, BCLK, LRCK, 3.3V, GND | Lower-front temple interior |
| **J4** | **Battery Power In Solder Pads** | **SMD Solder Pads Only (No JST-PH)** | **2.5 x 3.0 mm bare copper pads with thermal relief** | System +5.0V (`VBAT_BUCK_5V`) and GND | **Rated ≥ 5.0 A peak**; sized for **20 AWG to 22 AWG ultra-flexible silicone wire** (fed from upgraded ≥ 5.0 A synchronous battery buck to match EVB 5A `VCC5V0_SYS_S5` rail and prevent brownouts during concurrent LLM/NPU bursts) |
| **J5** | **Wi-Fi / Bluetooth RF Antenna Connector** | Hirose / I-PEX MHF4 / U.FL | Ultra-miniature coaxial SMD | 50Ω RF Signal + GND | Upper temple edge; connects to miniature flexible PCB antenna |
| **SW1** | **MaskROM Recovery Key Switch** | XKB `TS-1187A-B-A-B` (LCSC `C318884`) | SMD (3.0 x 4.0 x 1.5 mm) | Tactile push button | Connected to **`SARADC_IN0_BOOT` (Ball A25)** net via 100 Ω damping resistor `R18`. Pressing switch during power-on pulls line to 0V (GND) to force RK3576 USB MaskROM download/flashing mode (EVB Sheet 11 p.11 & Sheet 42 p.26). |
| **SW2** | **System Power-On (PWRON) Switch** | XKB `TS-1187A-B-A-B` (LCSC `C318884`) | SMD (3.0 x 4.0 x 1.5 mm) | Tactile push button | Outer temple arm; signals RK806S-5 PMIC `PWRON` pin (Pin 19) to initiate hardware power-up sequence (EVB Sheet 23 p.21 & Sheet 42 p.26). |
| **TP1–TP3**| **Debug UART Test Pads** | Surface test pads (1.0 mm round) | Test Pad | `UART_TX`, `UART_RX`, `GND` | Unpopulated test pads on interior board face for early boot debug |

---

## 9. Fabrication & SMT Assembly Verification Status

* **JLCPCB PCBA Compatibility:** **UNVERIFIED** (Requires formal JLCPCB engineering DFM review and HDI stackup quote for FCCSP-698L package before declaring 100% compatibility).
* **RK3576 Symbol & Footprint Library:** **UNVERIFIED** (Official Rockchip reference design symbol/footprint must be imported and verified against official mechanical package drawing).
* **eMCP Memory Sourcing:** **Consigned Part** (Harvested locally from scrap donor smartphone; not catalog-orderable from JLCPCB).
* **Total Component Count:** ~114 individual parts on the 20–22mm x 75mm board outline.
