# PROJECT FRIDAY: COMPLETE SCHEMATIC COMPONENT SPECIFICATION & LIBRARY DIRECTORY
## Custom 20–22mm x 75mm Wearable Compute Board (Rockchip RK3576 Architecture)

This document itemizes every electrical component required for the schematic capture of Project FRIDAY's custom compute PCB. 
**Source of Truth:** Official Rockchip RK3576 Reference/EVB Schematic and Rockchip Hardware Design Guide (to be provided by student). Every value must cite schematic page/net or component datasheet; any value without a verified source is marked explicitly as **UNVERIFIED**.

---

## 1. Primary Active Silicon (Integrated Circuits)

| Reference | Component Name & Role | Manufacturer & MPN | Sourcing Status | Package / Footprint | Pin Count & Pitch | Design Rules & Electrical Constraints | Autodesk / Eagle Library Source |
|:---:|:---|:---|:---:|:---|:---:|:---|:---|
| **U1** | **Rockchip RK3576 SoC**<br>Core 8 nm FinFET 8-Core Application Processor & 6-TOPS NPU | Rockchip<br>`RK3576` | LCSC `C42388007`<br>(Catalog orderable) | **FCCSP-698L**<br>(16.1 x 17.2 mm) | 698 Balls<br>**Ball Pitch: 0.55 / 0.60 / 0.65 mm mixed**<br>Ball Size: 0.30 mm | • Mixed 0.55/0.60/0.65 mm pitch strictly drives 6-layer HDI fabrication rules (laser-drilled microvias L1-L2, minimum 0.09 mm trace/space, via-in-pad)<br>• LPDDR4X 32-bit bus length matching: skew < 0.2 mm<br>• 100Ω differential impedance on MIPI CSI-2 camera pairs<br>• 90Ω differential impedance on USB 2.0 D+/D- lines | RK3576 DS Rev 1.5 §1.2 p.23 & §2 p.24; library UNVERIFIED (pending EVB import) |
| **U2** | **Rockchip RK806-1 PMIC**<br>Multi-rail companion power management IC | Rockchip<br>`RK806-1` | LCSC `C5156483`<br>(Catalog orderable) | **QFN-68**<br>(7.0 x 7.0 mm) | 68 Pins + EP<br>0.35 mm pin pitch | • **Host Interface:** **I2C mode** configured by tying **CS (Pin 18) to VCCA (Pin 21)** (RK806 DS Table 2-2 p.15). 7-bit Master I2C address is **`0x23`** (RK806 DS §I2C p.17).<br>• **I2C Pull-Ups:** 10 kΩ pull-ups on SDA (Pin 15) and SCL (Pin 17) to **`VCCIO` (Pin 20)** (RK806 DS Fig. 1-2 p.10).<br>• Exposed thermal pad requires minimum 16 vias to solid GND plane.<br>• Switching inductors and input/output caps placed immediately adjacent to PMIC pins per Fig. 1-2. | RK806 DS Rev 1.3 p.10, 15, 17; LCSC `C5156483.lbr` |
| **U3** | **Samsung 4GB LPDDR4X + 64GB eMMC eMCP**<br>Unified RAM & fast OS flash memory | Samsung<br>`KM3V...` series | Consigned Part<br>(Harvested locally; not catalog-orderable from JLCPCB) | **BGA-254**<br>(11.5 x 13.0 mm) | 254 Balls<br>0.5 mm ball pitch | • Sits directly adjacent to RK3576 DDR controller ball bank<br>• High-speed DQ/DQS traces routed on Layer 3 (stripline between solid GND planes)<br>• Guard traces and GND stitching vias every 3 mm along DDR bus | Standard JEDEC BGA-254 (`bga254.lbr` / SnapEDA) |
| **U4** | **Realtek RTL8723DS Wi-Fi / Bluetooth IC**<br>2.4 GHz 802.11b/g/n + BT 4.2 radio | Realtek<br>`RTL8723DS-CG` | LCSC `C2762334`<br>(Catalog orderable) | **WQFN-48**<br>(6.0 x 6.0 mm) | 48 Pins + EP<br>0.4 mm pin pitch | • 50Ω coplanar waveguide with ground reference to antenna matching network<br>• Solid ground keepout under RF matching pi-network<br>• SDIO clock and data lines length matched within 1.0 mm | LCSC / EasyEDA Pre-Made Footprint (`C2762334.lbr`) |
| **U5** | **Priority Power Multiplexer (Power-Path)**<br>Reverse-blocking dual-input selector (4.5 A rated) | Texas Instruments<br>`TPS2121RUXR` | LCSC / TI<br>(Catalog orderable) | **WQFN-12**<br>(2.0 x 2.5 mm, 0.5mm pitch) | 12 Pins + EP | • Rated continuous current: 4.5 A (R_DS(on) = 56 mΩ typical)<br>• Auto-switches between `VBUS_5V` (USB-C) and `VBAT_BUCK_5V` (MP2315 buck)<br>• Electrical drop at 3.0 A load: ΔV = 3.0A * 0.056Ω = 0.17 V<br>• Heat dissipation at 3.0 A: P_loss = (3.0A)^2 * 0.056Ω = 0.50 W | TI Footprint (`TPS2121_RUX.lbr`) |

---

## 2. Power Tree & Voltage Sequencing Table

> [!WARNING]
> ### BLOCK: Rail -> RK806 Channel Mapping Status = UNVERIFIED — DO NOT CAPTURE
> **Source of Truth:** Official RK3576 EVB Reference Schematic (pending student upload into `docs/datasheets/`).
> Rail-to-PMIC channel allocations and power sequencing MUST match the specific RK806 OTP variant default voltages and startup sequences (RK806 DS Rev 1.3 Tables 4-1..4-3). 
> **Architectural conflicts in naive channel mapping:**
> - `DDRPHY_CKE_VDDQ / VCC_DDR` requires 1.10 V, whereas RK806-1 BUCK 5 OTP boots at **0.85 V** (Table 4-1).
> - `VCC_EMMC` requires 3.30 V, whereas RK806-1 BUCK 7 OTP boots at **2.00 V** in Sequence 1 (Table 4-1).
> Until the official RK3576 EVB schematic is provided, **all PMIC regulator channel assignments and sequence numbers below are strictly tentative and flagged UNVERIFIED — DO NOT CAPTURE.**

### RK3576 Recommended Operating Voltage Specifications (RK3576 DS Rev 1.5 Table 3-2) & PMIC Sizing Baseline (RK806 DS Rev 1.3 Fig. 1-2):

| Rail Name (Net) | Min Voltage | Typ Voltage | Max Voltage | Target Block & Functional Role | Source Regulator (Tentative Baseline — UNVERIFIED) | PMIC Passives Sizing Baseline (RK806 DS Fig. 1-2 & §Feature) | Source Citation |
|---|:---:|:---:|:---:|---|---|---|:---:|
| **VSYS_5V** | 4.50 V | 5.00 V | 5.50 V | Primary system power bus | USB-C / MP2315 Buck via U5 (TPS2121) | Input bypass: 22 µF 10V X5R at each PMIC VCC pin (VCC1–VCC10); 1 µF at VCC11–14 | RK806 DS Fig. 1-2 |
| **CPU_BIG_DVDD** | 0.675 V | **0.75 V** | 1.000 V | Quad-core Cortex-A72 cluster | RK806 BUCK 1 (6.5 A rated, UNVERIFIED) | Inductor: **0.22 µH** (Isat ≥ 6.5A); Output: **3x 22 µF** 6.3V X5R | RK3576 DS Table 3-2 p.41; RK806 DS Fig. 1-2 p.10 |
| **CPU_LIT_DVDD** | 0.675 V | **0.75 V** | 1.000 V | Quad-core Cortex-A53 cluster & CCI | RK806 BUCK 2 (5.0 A rated, UNVERIFIED) | Inductor: **0.22 µH** (Isat ≥ 5.0A); Output: **3x 22 µF** 6.3V X5R | RK3576 DS Table 3-2 p.41; RK806 DS Fig. 1-2 p.10 |
| **GPU_DVDD** | 0.675 V | **0.75 V** | 0.918 V | ARM Mali-G52 MC3 GPU core (Separate rail for GPU DVFS) | RK806 BUCK 3 (5.0 A rated, UNVERIFIED) | Inductor: **0.22 µH** (Isat ≥ 5.0A); Output: **3x 22 µF** 6.3V X5R | RK3576 DS Table 3-2 p.41; RK806 DS Fig. 1-2 p.10 |
| **NPU_DVDD** | 0.675 V | **0.75 V** | 0.918 V | 6-TOPS Neural Processing Unit (Separate rail for NPU power gating) | RK806 BUCK 4 (5.0 A rated, UNVERIFIED) | Inductor: **0.22 µH** (Isat ≥ 5.0A); Output: **3x 22 µF** 6.3V X5R | RK3576 DS Table 3-2 p.41; RK806 DS Fig. 1-2 p.10 |
| **LOGIC_DVDD** | 0.675 V | **0.75 V** | 0.825 V | Core SoC digital logic (Underdrive: 0.585–0.715 V) | RK806 BUCK 5 (3.0 A rated, UNVERIFIED) | Inductor: **0.47 µH** (Isat ≥ 3.0A); Output: **2x 22 µF** 6.3V X5R | RK3576 DS Table 3-2 p.41; RK806 DS Fig. 1-2 p.10 |
| **LOGIC_MEM_DVDD** | 0.675 V | **0.75 V** | 0.825 V | Internal memory logic array (tied to LOGIC or PMU) | Common LOGIC or PMIC LDO (UNVERIFIED) | Decoupling per RK3576 PDN guide | RK3576 DS Table 3-2 p.41 |
| **PMU_LOGIC_DVDD0V75** | 0.675 V | **0.75 V** | 0.825 V | Low-power always-on Power Management Unit | RK806 NLDO (300/500 mA, UNVERIFIED) | Output: **2.2 µF** 6.3V X5R; Input: 1.0 µF at VCC11–14 | RK3576 DS Table 3-2 p.41; RK806 DS Fig. 1-2 p.10 |
| **DDRPHY_DVDD** | 0.675 V | **0.75 V** | 0.900 V | LPDDR4X physical layer digital logic | RK806 NLDO / Buck (UNVERIFIED) | Output: **2.2 µF** 6.3V X5R | RK3576 DS Table 3-2 p.41 |
| **DDRPHY_PLL_DVDD** | 0.675 V | **0.75 V** | 0.8925 V | DDR PHY PLL digital core | RK806 NLDO (UNVERIFIED) | Output: **2.2 µF** 6.3V X5R | RK3576 DS Table 3-2 p.41 |
| **DDRPHY_PLL_AVDD1V8** | 1.62 V | **1.80 V** | 1.98 V | DDR PHY PLL analog power | RK806 PLDO (UNVERIFIED) | Output: **2.2 µF** 10V X5R | RK3576 DS Table 3-2 p.41 |
| **DDRPHY_VDDQ / CK_VDDQ** | 0.57 V | **0.60 V** | 0.65 V | LPDDR4X I/O interface switching voltage | RK806 LDO / Buck (UNVERIFIED) | Output: **2.2 µF / 4.7 µF** under memory BGA | RK3576 DS Table 3-2 p.41 |
| **DDRPHY_CKE_VDDQ** | 1.06 V | **1.10 V** | 1.17 V | LPDDR4X Retention I/O & eMCP VDD2 core | RK806 BUCK (3.0 A rated, UNVERIFIED) | Inductor: **0.47 µH** (Isat ≥ 3.0A); Output: **2x 22 µF** 6.3V X5R | RK3576 DS Table 3-2 p.41 |
| **PLL_DVDD0V75** | 0.675 V | **0.75 V** | 0.8925 V | SoC master PLL digital power | RK806 NLDO (UNVERIFIED) | Output: **2.2 µF** 6.3V X5R | RK3576 DS Table 3-2 p.41 |
| **PLL_AVDD1V8** | 1.62 V | **1.80 V** | 1.98 V | SoC master PLL analog power | RK806 PLDO (UNVERIFIED) | Output: **2.2 µF** 10V X5R | RK3576 DS Table 3-2 p.41 |
| **OSC_AVDD1V8** | 1.65 V | **1.80 V** | 1.95 V | 24 MHz oscillator analog power | RK806 PLDO (UNVERIFIED) | Output: **2.2 µF** 10V X5R | RK3576 DS Table 3-2 p.42 |
| **USB2_OTG_DVDD0V75** | 0.6975 V | **0.75 V** | 0.825 V | USB 2.0 PHY digital logic core | RK806 NLDO (UNVERIFIED) | Output: **2.2 µF** 6.3V X5R | RK3576 DS Table 3-2 p.42 |
| **USB2_OTG_AVDD1V8** | 1.674 V | **1.80 V** | 1.98 V | USB 2.0 PHY analog core | RK806 PLDO (UNVERIFIED) | Output: **2.2 µF** 10V X5R | RK3576 DS Table 3-2 p.42 |
| **USB2_OTG_AVDD3V3** | 3.069 V | **3.30 V** | 3.63 V | USB 2.0 transceiver high-voltage analog supply | RK806 BUCK 3V3 domain / LDO (UNVERIFIED) | Output: **2.2 µF / 4.7 µF** 10V X5R | RK3576 DS Table 3-2 p.42 |
| **USB3 / PCIe PIPE 0V85** | 0.80 V | **0.85 V** | 0.935 V | USB3 OTG / PCIe Combo PHY analog power | RK806 NLDO / Buck (UNVERIFIED) | Output: **2.2 µF** 10V X5R | RK3576 DS Table 3-2 p.42 |
| **USB3 / PCIe PIPE 1V8** | 1.62 V | **1.80 V** | 1.98 V | USB3 OTG / PCIe Combo PHY analog core | RK806 PLDO (UNVERIFIED) | Output: **2.2 µF** 10V X5R | RK3576 DS Table 3-2 p.42 |
| **PMUIO0_VCC1V8** | 1.65 V | **1.80 V** | 1.95 V | Digital PMU GPIO Domain 0 (1.8 V only) | RK806 PLDO (UNVERIFIED) | Output: **2.2 µF** 10V X5R | RK3576 DS Table 3-2 p.41 |
| **VCCIO0_VCC1V8** | 1.65 V | **1.80 V** | 1.95 V | Digital GPIO Domain 0 (1.8 V only) | RK806 PLDO (UNVERIFIED) | Output: **2.2 µF** 10V X5R | RK3576 DS Table 3-2 p.41 |
| **PMUIO1 / VCCIO1..6** | 1.65 V / 2.7 V | **1.80 V / 3.30 V** | 1.95 V / 3.6 V | General GPIO Banks 1 through 6 | RK806 Buck / LDO (UNVERIFIED) | Output: **2.2 µF – 10 µF** per bank | RK3576 DS Table 3-2 p.41 |
| **OSC_UFS_AVDD / VCCIO7** | 1.08 V / 1.65 V | **1.20 V / 1.80 V** | 1.32 V / 1.95 V | Fast storage / IO Domain 7 | RK806 LDO (UNVERIFIED) | Output: **2.2 µF** 10V X5R | RK3576 DS Table 3-2 p.41 |
| **VCC_EMMC** | 2.70 V | **3.30 V** | 3.60 V | eMMC Core & Flash NAND supply (0.30 A budget) | RK806 Synchronous Buck (UNVERIFIED) | Inductor: **0.47 µH** (Isat ≥ 3.0A); Output: **2x 22 µF** + 4.7 µF at eMMC VCC pins | RK3576 EVB (pending); RK806 DS Fig. 1-2 |
| **VCCIO_3V3** | 3.00 V | **3.30 V** | 3.60 V | System 3.3V Peripheral Rail (0.85 A budget: Wi-Fi, touch, camera bridge) | RK806 Synchronous Buck (UNVERIFIED) | Inductor: **0.47 µH** (Isat ≥ 3.0A); Output: **2x 22 µF** + 10 µF bulk | RK3576 EVB (pending); RK806 DS Fig. 1-2 |

---

## 3. Frequency Control & Clocks

| Reference | Frequency | Tolerance & Load | Manufacturer & MPN | LCSC Part # | Package / Footprint | Design Rules & Load Sizing (Formula: C = 2*(CL - Cstray)) | Library Source |
|:---:|:---:|:---:|---|:---:|---|:---|:---|
| **Y1** | **24.000 MHz** | ±10 ppm<br>CL = 12 pF | YXC<br>`X322524MOB4SI` | `C70590` | **SMD-3225-4P**<br>(3.2 x 2.5 mm) | Master SoC clock. Load caps C1, C2 = 18 pF (0402 C0G), calculated via 2*(12 pF - 3 pF stray) = 18 pF. Guard ring of solid GND surrounding traces; no digital routing under crystal. | Fusion `crystal.lbr` / LCSC `C70590` |
| **Y2 (REMOVED)** | *N/A* | *Internal Oscillator* | *N/A* | *N/A* | *N/A* | **RK806 PMIC Clock:** RK806 integrates an **internal 32.768 kHz RC oscillator** and outputs `SYNC_CLK` (Pin 3). RK806 has no crystal oscillator pins (RK806 DS Table 2-2 p.15). **RK3576 32.768 kHz input:** RK3576 requires `CLK_32K_IN` (Ball B22); whether fed from RK806 `SYNC_CLK` or an external source is **UNVERIFIED until EVB schematic is provided**. Discrete crystal Y2 and C3/C4 removed. | N/A |
| **Y3** | **26.000 MHz** | ±10 ppm<br>CL = 12 pF | Standard 26MHz (UNVERIFIED) | LCSC / generic | **SMD-2016-4P**<br>(2.0 x 1.6 mm) | Dedicated reference clock for RTL8723DS Wi-Fi/BT transceiver. Load caps C5, C6 = 18 pF (0402 C0G). Placed adjacent to RTL8723DS XTAL pins. | UNVERIFIED (pending RTL8723DS ref design) |

---

## 4. Power Inductors & Ferrite Beads (Sized per RK806 DS Rev 1.3 Fig. 1-2 & §1.2)

| Reference | Value / Inductance | Rating & Specs | Package | Qty | Circuit Function & Target Rail | Design Rules & Datasheet Citation |
|:---:|:---:|:---|:---:|:---:|:---|:---|
| **L1** | **0.22 µH** | Isat ≥ 6.5 A, DCR < 25 mΩ | SMD 2016 (2.0 x 1.6 mm) | 1 | **RK806-1 Buck 1 Switching Node:** Powers `CPU_BIG_DVDD` | Place < 1.5 mm from PMIC SW1 pin (RK806 DS Fig. 1-2 p.10 & §1.2 p.8) |
| **L2** | **0.22 µH** | Isat ≥ 5.0 A, DCR < 25 mΩ | SMD 2016 (2.0 x 1.6 mm) | 1 | **RK806-1 Buck 2 Switching Node:** Powers `CPU_LIT_DVDD` | Place < 1.5 mm from PMIC SW2 pin (RK806 DS Fig. 1-2 p.10 & §1.2 p.8) |
| **L3** | **0.22 µH** | Isat ≥ 5.0 A, DCR < 25 mΩ | SMD 2016 (2.0 x 1.6 mm) | 1 | **RK806-1 Buck 3 Switching Node:** Powers `GPU_DVDD` | Place < 1.5 mm from PMIC SW3 pin (RK806 DS Fig. 1-2 p.10 & §1.2 p.8) |
| **L4** | **0.22 µH** | Isat ≥ 5.0 A, DCR < 25 mΩ | SMD 2016 (2.0 x 1.6 mm) | 1 | **RK806-1 Buck 4 Switching Node:** Powers `NPU_DVDD` | Place < 1.5 mm from PMIC SW4 pin (RK806 DS Fig. 1-2 p.10 & §1.2 p.8) |
| **L5** | **0.47 µH** | Isat ≥ 3.0 A, DCR < 35 mΩ | SMD 2016 (2.0 x 1.6 mm) | 1 | **RK806-1 Buck 5 Switching Node:** Powers `LOGIC_DVDD` | Place < 1.5 mm from PMIC SW5 pin (RK806 DS Fig. 1-2 p.10 & §1.2 p.8) |
| **L6** | **0.47 µH** | Isat ≥ 3.0 A, DCR < 35 mΩ | SMD 2016 (2.0 x 1.6 mm) | 1 | **RK806-1 Buck 6 Switching Node:** Powers `VCCIO_3V3` | Place < 1.5 mm from PMIC SW6 pin (RK806 DS Fig. 1-2 p.10 & §1.2 p.8) |
| **L7** | **0.47 µH** | Isat ≥ 3.0 A, DCR < 35 mΩ | SMD 2016 (2.0 x 1.6 mm) | 1 | **RK806-1 Buck 7 Switching Node:** Powers `VCC_EMMC` / `DDRPHY_CKE_VDDQ` | Place < 1.5 mm from PMIC SW7 pin (RK806 DS Fig. 1-2 p.10 & §1.2 p.8) |
| **FB1** | **120 Ω @ 100MHz** | 2.0 A Continuous, DCR < 40 mΩ | SMD 0603 (1.6 x 0.8 mm) | 1 | **Audio Rail Filter:** Isolates 5.0V audio supply from switching ripple | Place at boundary between system 5.0V and audio amplifier VDD island |
| **FB2** | **120 Ω @ 100MHz** | 2.0 A Continuous, DCR < 40 mΩ | SMD 0603 (1.6 x 0.8 mm) | 1 | **Wi-Fi RF Filter:** Isolates RTL8723DS 3.3V power from CPU noise | Place at entrance of RTL8723DS power plane |
| **FB3** | **120 Ω @ 100MHz** | 2.0 A Continuous, DCR < 40 mΩ | SMD 0603 (1.6 x 0.8 mm) | 1 | **eMMC Core Power Filter:** Isolates `VCC_EMMC` 3.3V from Buck switching noise | Place adjacent to eMMC VCC decoupling caps |

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
| **R5, R6** | **10 kΩ** | ±1% | 1/16 W | SMD 0402 | 2 | **PMIC I2C Bus Pull-Ups:** Pulls up host PMIC `SDA` (Pin 15) and `SCL` (Pin 17) to RK806 **`VCCIO` (Pin 20)**. PMIC operates in I2C mode (CS tied to VCCA, address `0x23`). | RK806 DS Rev 1.3 Fig. 1-2 p.10, Table 2-2 p.15, §I2C p.17 |
| **R7, R8** | **10 kΩ** | ±1% | 1/16 W | SMD 0402 | 2 | **Logic Pull-Ups & Straps:** Pulls up `PMIC_PWRON` and hardware reset lines to matching I/O domain. | UNVERIFIED |
| **R9** | **10 kΩ** | ±1% | 1/16 W | SMD 0402 | 1 | **Mic Channel Select:** Sets INMP441 `L/R` channel address. | InvenSense INMP441 Datasheet Table 4 |
| **R10** | **10 kΩ** | ±1% | 1/16 W | SMD 0402 | 1 | **MAX98357A Left Channel Pull-Up:** Pulls up `SD_MODE` to 3.3 V on Left amplifier (yields ~3.0 V with internal 100k pulldown; threshold > 1.39 V selects Left channel). Amplifier VDD is 5.0 V (`VSYS_5V`). *Note: Verify whether breakout module already carries onboard resistor.* | Maxim MAX98357A Datasheet Table 1 |
| **R11** | **220 kΩ** | ±1% | 1/16 W | SMD 0402 | 1 | **MAX98357A Right Channel Pull-Up:** Pulls up `SD_MODE` to 3.3 V on Right amplifier (yields ~1.03 V with internal 100k pulldown; voltage falls inside 0.77 V – 1.39 V window selecting Right channel). Amplifier VDD is 5.0 V (`VSYS_5V`). *Note: Verify whether breakout module already carries onboard resistor.* | Maxim MAX98357A Datasheet Table 1 |
| **R12, R13**| **100 kΩ** | ±1% | 1/16 W | SMD 0402 | 2 | **Audio Gain Limiting:** Ties MAX98357A `GAIN` pin to VDD (configures lowest +3 dB gain setting, capping power below 0.8 W RMS to prevent speaker voice-coil damage). Amplifier VDD is 5.0 V (`VSYS_5V`). | Maxim MAX98357A Datasheet Table 2 |
| **R14, R15**| **22 Ω** | ±1% | 1/16 W | SMD 0402 | 2 | **Master Clock Series Damping:** In-line on 24.000 MHz crystal `OSC_OUT` to eliminate harmonic ringing. | UNVERIFIED (Rockchip hardware design guide) |
| **R16–R18**| **Boot Straps & Divider**| ±1% | 1/16 W | SMD 0402 | 3 | **Boot Mode Strapping & Recovery Circuit:** Pull-up and divider network on **`SARADC_IN0_BOOT` (Ball A25)** net to configure normal eMMC boot vs USB MaskROM recovery mode. | RK3576 DS Rev 1.5 Table 2-1 p.28 (UNVERIFIED pending EVB schematic) |
| **R19–R22**| **0 Ω (Jumper)**| — | 1/16 W | SMD 0402 | 4 | **RF & Ground Tuning Links:** In-line antenna 50Ω jumper and ground isolation star connections. | UNVERIFIED |

---

## 7. Capacitors (SMD Multilayer Ceramic - MLCC)

| Reference | Capacitance | Voltage Rating | Dielectric | Package | Qty | Target Circuit & Functional Role | Source / Sizing Rule |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---|
| **C1, C2** | **18 pF** | 50 V | C0G / NP0 | SMD 0402 | 2 | **24.000 MHz Crystal Load Capacitors:** From `OSC_IN` / `OSC_OUT` to crystal GND. | Formula: 2*(12 pF - 3 pF stray) = 18 pF |
| **C3, C4 (REMOVED)**| *N/A* | *N/A* | *N/A* | *N/A* | *N/A* | **Removed with Y2:** RK806 integrates internal 32.768 kHz RC oscillator; no crystal load capacitors required. RK3576 `CLK_32K_IN` circuit pending EVB. | RK806 DS Table 2-2 p.15 |
| **C5, C6** | **18 pF** | 50 V | C0G / NP0 | SMD 0402 | 2 | **26.000 MHz Wi-Fi Crystal Load Capacitors:** From RTL8723DS XTAL pins to GND. | Formula: 2*(12 pF - 3 pF stray) = 18 pF (UNVERIFIED) |
| **C7–C16** | **22 µF** | 10 V | X5R | SMD 0603 | 10 | **PMIC Buck Input Bypass Capacitors:** 1x 22 µF placed directly at each PMIC buck supply input pin (VCC1 through VCC10) from `VSYS_5V`. | RK806 DS Rev 1.3 Fig. 1-2 p.10 |
| **C17–C32** | **100 nF (0.1 µF)**| 10 V | X5R / X7R | SMD 0402 | 16 | **High-Frequency Decoupling Array:** Distributed on the back side of PCB under RK3576 BGA power balls and eMCP balls. | **UNVERIFIED (exact capacitor count, values, and rail distribution pending official RK3576 PDN design guide)** |
| **C33–C40**| **2.2 µF / 1.0 µF** | 10 V | X5R | SMD 0402 | 8 | **PMIC LDO Output & Input Decoupling:** 2.2 µF placed at each active LDO output; 1.0 µF placed at LDO input supply pins (VCC11, VCC12, VCC13, VCC14, VCCA). | RK806 DS Rev 1.3 Fig. 1-2 p.10 |
| **C41–C44**| **4.7 µF** | 10 V | X5R / X7R | SMD 0603 | 4 | **Peripherals Decoupling:** RTL8723DS Wi-Fi 3.3V rail and IMX708 camera interface connector. | UNVERIFIED |
| **C45–C50**| **10 µF** | 16 V / 25 V | X5R / X7R | SMD 0603 | 6 | **Bulk Input Filters:** Placed at 5.0V system power bus entry (`VSYS_5V`), USB-C VBUS, and dual MAX98357A audio amplifier 5.0V VDD pins. | UNVERIFIED |
| **C51–C68**| **22 µF** | 6.3V / 10V | X5R | SMD 0603 | 18 | **PMIC Buck Switching Output Filters:** Sized per RK806 typical application diagram: **3x 22 µF** in parallel at each high-current buck output (BUCK1–BUCK4: `CPU_BIG`, `CPU_LIT`, `GPU`, `NPU`); **2x 22 µF** in parallel at remaining buck outputs (BUCK5–BUCK7: `LOGIC`, `VCCIO_3V3`, `VCC_EMMC`). | RK806 DS Rev 1.3 Fig. 1-2 p.10 |

---

## 8. Connectors, Mechanical Controls & Debug Test Points

| Reference | Component Description | Manufacturer & MPN | Package / Footprint | Pin Count & Signals | Physical Location & Electrical Specs |
|:---:|:---|:---|:---|:---|:---|
| **J1** | **USB Type-C Receptacle (16-Pin)** | Korean Hroparts `TYPE-C-31-M-12` (LCSC `C165948`) | 16-Pin SMD Right Angle | 5V Power, GND, D+, D-, CC1, CC2 | Bottom-rear of right temple arm (5V / 3A rating) |
| **J2** | **MIPI CSI Camera FPC Connector** | Hirose / Amphenol 0.5mm pitch | 26-Pin 0.5mm Bottom Contact | 2-Lane MIPI CSI (Clk ±, D0 ±, D1 ±), 1.8V VCCIO, 3.3V, I2C, Reset, PWDN | Front-right browline edge (connects to front-bridge sensor PCB) |
| **J3** | **Audio & Mic Interconnect Header** | 0.5mm pitch FPC | 10-Pin 0.5mm Bottom Contact | I2S DOUT, DIN, BCLK, LRCK, 3.3V, GND | Lower-front temple interior |
| **J4** | **Battery Power In Solder Pads** | **SMD Solder Pads Only (No JST-PH)** | **2.5 x 3.0 mm bare copper pads with thermal relief** | System +5.0V (`VBAT_BUCK_5V`) and GND | **Rated ≥ 3.0 A continuous (5.0 A peak)**; sized for **20 AWG to 22 AWG ultra-flexible silicone wire** (fed from MP2315 2S buck) |
| **J5** | **Wi-Fi / Bluetooth RF Antenna Connector** | Hirose / I-PEX MHF4 / U.FL | Ultra-miniature coaxial SMD | 50Ω RF Signal + GND | Upper temple edge; connects to miniature flexible PCB antenna |
| **SW1** | **MaskROM Recovery Key Switch** | XKB `TS-1187A-B-A-B` (LCSC `C318884`) | SMD (3.0 x 4.0 x 1.5 mm) | Tactile push button | Connected to **`SARADC_IN0_BOOT` (Ball A25)** net. Pressing switch during power-on pulls line to divider/GND to force RK3576 USB MaskROM download/flashing mode (UNVERIFIED circuit pending EVB schematic). (RK3576 DS Rev 1.5 Table 2-1 p.28) |
| **SW2** | **System Power-On (PWRON) Switch** | XKB `TS-1187A-B-A-B` (LCSC `C318884`) | SMD (3.0 x 4.0 x 1.5 mm) | Tactile push button | Outer temple arm; signals RK806-1 PMIC to wake up power tree |
| **TP1–TP3**| **Debug UART Test Pads** | Surface test pads (1.0 mm round) | Test Pad | `UART_TX`, `UART_RX`, `GND` | Unpopulated test pads on interior board face for early boot debug |

---

## 9. Fabrication & SMT Assembly Verification Status

* **JLCPCB PCBA Compatibility:** **UNVERIFIED** (Requires formal JLCPCB engineering DFM review and HDI stackup quote for FCCSP-698L package before declaring 100% compatibility).
* **RK3576 Symbol & Footprint Library:** **UNVERIFIED** (Official Rockchip reference design symbol/footprint must be imported and verified against official mechanical package drawing).
* **eMCP Memory Sourcing:** **Consigned Part** (Harvested locally from scrap donor smartphone; not catalog-orderable from JLCPCB).
* **Total Component Count:** ~114 individual parts on the 20–22mm x 75mm board outline.
