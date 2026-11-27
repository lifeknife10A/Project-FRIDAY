# PROJECT FRIDAY: COMPLETE SCHEMATIC COMPONENT SPECIFICATION & LIBRARY DIRECTORY
## Custom 20–22mm x 75mm Wearable Compute Board (Rockchip RK3576 Architecture)

This document itemizes every electrical component required for the schematic capture of Project FRIDAY's custom compute PCB. 
**Source of Truth:** Official Rockchip RK3576 Reference/EVB Schematic and Rockchip Hardware Design Guide (to be provided by student). Every value must cite schematic page/net or component datasheet; any value without a verified source is marked explicitly as **UNVERIFIED**.

---

## 1. Primary Active Silicon (Integrated Circuits)

| Reference | Component Name & Role | Manufacturer & MPN | Sourcing Status | Package / Footprint | Pin Count & Pitch | Design Rules & Electrical Constraints | Autodesk / Eagle Library Source |
|:---:|:---|:---|:---:|:---|:---:|:---|:---|
| **U1** | **Rockchip RK3576 SoC**<br>Core 8 nm FinFET 8-Core Application Processor & 6-TOPS NPU | Rockchip<br>`RK3576` | LCSC `C42388007`<br>(Catalog orderable) | **FCCSP-698L**<br>(16.1 x 17.2 mm) | 698 Balls<br>Pitch: UNVERIFIED (pending official RK3576 datasheet) | • 6-Layer HDI board (minimum 0.09mm trace/space)<br>• Laser microvias (L1 to L2/L3) for BGA escape<br>• LPDDR4X 32-bit bus length matching: skew < 0.2 mm<br>• 100Ω differential impedance on MIPI CSI-2 camera pairs<br>• 90Ω differential impedance on USB 2.0 D+/D- lines | UNVERIFIED (pending official Rockchip hardware reference / verified `.lbr` import) |
| **U2** | **Rockchip RK806-1 PMIC**<br>Multi-rail companion power management IC | Rockchip<br>`RK806-1` | LCSC `C5156483`<br>(Catalog orderable) | **QFN-68**<br>(7.0 x 7.0 mm) | 68 Pins + EP<br>0.35 mm pin pitch | • Host Interface: UNVERIFIED (confirm SPI vs I2C from reference schematic)<br>• Exposed ground thermal pad requires minimum 16 vias to solid GND plane<br>• Buck switching inductors (L1–L4) placed immediately adjacent to LX pins<br>• Buck output capacitors grounded directly to PMIC power ground island | LCSC / EasyEDA Pre-Made Footprint (`C5156483.lbr`) |
| **U3** | **Samsung 4GB LPDDR4X + 64GB eMMC eMCP**<br>Unified RAM & fast OS flash memory | Samsung<br>`KM3V...` series | Consigned Part<br>(Harvested locally; not catalog-orderable from JLCPCB) | **BGA-254**<br>(11.5 x 13.0 mm) | 254 Balls<br>0.5 mm ball pitch | • Sits directly adjacent to RK3576 DDR controller ball bank<br>• High-speed DQ/DQS traces routed on Layer 3 (stripline between solid GND planes)<br>• Guard traces and GND stitching vias every 3 mm along DDR bus | Standard JEDEC BGA-254 (`bga254.lbr` / SnapEDA) |
| **U4** | **Realtek RTL8723DS Wi-Fi / Bluetooth IC**<br>2.4 GHz 802.11b/g/n + BT 4.2 radio | Realtek<br>`RTL8723DS-CG` | LCSC `C2762334`<br>(Catalog orderable) | **WQFN-48**<br>(6.0 x 6.0 mm) | 48 Pins + EP<br>0.4 mm pin pitch | • 50Ω coplanar waveguide with ground reference to antenna matching network<br>• Solid ground keepout under RF matching pi-network<br>• SDIO clock and data lines length matched within 1.0 mm | LCSC / EasyEDA Pre-Made Footprint (`C2762334.lbr`) |
| **U5** | **Ideal Diode / Power-Path Controller**<br>Reverse-blocking power multiplexer (≥ 3 A rated) | Texas Instruments `LM66100` / `TPS2113A` (or low-Rdson P-MOSFET circuit) | LCSC / TI<br>(Catalog orderable) | **SC-70-6 / DFN** | 6 Pins | • Rated continuous current: ≥ 3.0 A (peak 5.0 A)<br>• Auto-switches between `VBUS_5V` (USB Type-C) and `VBAT_BUCK_5V` (battery MP2315 buck)<br>• Zero backfeed into battery buck when USB-C is plugged in; voltage drop < 30 mV | Vendor footprint (`LM66100.lbr`) |

---

## 2. Power Tree & Voltage Sequencing Table

> **Source Status:** All voltages, maximum currents, regulator allocations, and sequence orders below are design baselines and marked **UNVERIFIED (pending official RK3576 EVB reference schematic)**.

| Rail Name | Nominal Voltage | Max Current (Est.) | Source Regulator | Sequence Order | Sizing & Decoupling Requirements (Reference Baseline) | Source Citation |
|---|:---:|:---:|---|:---:|---|:---:|
| **VSYS_5V** | 5.00 V | 3.00 A | USB-C / MP2315 Buck via U5 | 0 (Primary) | Input to PMIC: 2x 22 µF 10V X5R (0603) + 1x 100 nF (0402) placed at PMIC VIN | UNVERIFIED |
| **VDD_CPU_BIG** | 0.80 V – 1.05 V | 4.00 A | RK806-1 BUCK 1 | 2 | Inductor: 0.47 µH (Isat ≥ 4.5A); Output: 2x 22 µF 6.3V X5R + 4x 100 nF under BGA | UNVERIFIED |
| **VDD_CPU_LIT** | 0.80 V – 1.05 V | 3.00 A | RK806-1 BUCK 2 | 2 | Inductor: 0.47 µH (Isat ≥ 4.5A); Output: 2x 22 µF 6.3V X5R + 4x 100 nF under BGA | UNVERIFIED |
| **VDD_NPU_GPU** | 0.80 V – 0.95 V | 3.50 A | RK806-1 BUCK 3 | 3 | Inductor: 0.47 µH (Isat ≥ 4.5A); Output: 2x 22 µF 6.3V X5R + 4x 100 nF under BGA | UNVERIFIED |
| **VDD_LOGIC** | 0.80 V | 2.50 A | RK806-1 BUCK 4 | 1 | Inductor: 1.0 µH (Isat ≥ 3.2A); Output: 2x 22 µF 6.3V X5R + 4x 100 nF under BGA | UNVERIFIED |
| **VCC_DDR / VDD2** | 1.10 V | 2.00 A | RK806-1 BUCK 5 | 1 | Inductor: 1.0 µH (Isat ≥ 3.2A); Output: 2x 22 µF 6.3V X5R + 4x 100 nF at eMCP | UNVERIFIED |
| **VDDQ_DDR** | 0.60 V | 0.50 A | RK806-1 LDO | 2 | Output: 1x 4.7 µF 6.3V X5R + 2x 100 nF under memory BGA | UNVERIFIED |
| **VDD1_DDR** | 1.80 V | 0.30 A | RK806-1 LDO | 1 | Output: 1x 2.2 µF 10V X5R + 2x 100 nF at eMCP VDD1 pins | UNVERIFIED |
| **VCC_EMMC** | 3.30 V | 0.30 A | RK806-1 LDO / Ext | 1 | Output: 1x 4.7 µF 10V X5R + 1x 100 nF at eMMC VCC pins | UNVERIFIED |
| **VCCQ_EMMC** | 1.80 V | 0.15 A | RK806-1 LDO | 1 | Output: 1x 2.2 µF 10V X5R + 1x 100 nF at eMMC VCCQ pins | UNVERIFIED |
| **VCCIO_1V8** | 1.80 V | 0.40 A | RK806-1 LDO | 2 | Output: 1x 4.7 µF 10V X5R + decoupling; feeds Camera I2C and 1.8V SoC I/O banks | UNVERIFIED |
| **VCCIO_3V3** | 3.30 V | 0.60 A | RK806-1 LDO / Ext | 2 | Output: 1x 10 µF 10V X5R; feeds Audio amplifiers, Wi-Fi I/O, and peripheral sensors | UNVERIFIED |
| **VDD_0V9** | 0.90 V | 0.20 A | RK806-1 LDO | 2 | Output: 1x 1.0 µF 10V X5R; powers SoC PLL and internal clock generators | UNVERIFIED |
| **AVDD_1V8** | 1.80 V | 0.15 A | RK806-1 LDO | 2 | Output: 1x 1.0 µF 10V X5R; powers analog ADC and MIPI CSI PHY | UNVERIFIED |

---

## 3. Frequency Control & Clocks

| Reference | Frequency | Tolerance & Load | Manufacturer & MPN | LCSC Part # | Package / Footprint | Design Rules & Load Sizing (Formula: C = 2*(CL - Cstray)) | Library Source |
|:---:|:---:|:---:|---|:---:|---|:---|:---|
| **Y1** | **24.000 MHz** | ±10 ppm<br>CL = 12 pF | YXC<br>`X322524MOB4SI` | `C70590` | **SMD-3225-4P**<br>(3.2 x 2.5 mm) | Master SoC clock. Load caps C1, C2 = 18 pF (0402 C0G), calculated via 2*(12 pF - 3 pF stray) = 18 pF. Guard ring of solid GND surrounding traces; no digital routing under crystal. | Fusion `crystal.lbr` / LCSC `C70590` |
| **Y2** | **32.768 kHz** | ±20 ppm<br>CL = 12.5 pF | Epson<br>`Q13FC13500004` | `C32346` | **SMD-3215-2P**<br>(3.2 x 1.5 mm) | RTC sleep clock for RK806-1 PMIC. Load caps C3, C4 = 18 pF or 22 pF (0402 C0G; standard values, calculated via 2*(12.5 pF - 3 pF stray) ≈ 19 pF). Trace length < 8 mm. | Fusion `crystal.lbr` / LCSC `C32346` |
| **Y3** | **26.000 MHz** | ±10 ppm<br>CL = 12 pF | Standard 26MHz (UNVERIFIED) | LCSC / generic | **SMD-2016-4P**<br>(2.0 x 1.6 mm) | Dedicated reference clock for RTL8723DS Wi-Fi/BT transceiver. Load caps C55, C56 = 18 pF (0402 C0G). Placed adjacent to RTL8723DS XTAL pins. | UNVERIFIED (pending RTL8723DS ref design) |

---

## 4. Power Inductors & Ferrite Beads

| Reference | Value / Inductance | Rating & Specs | Package | Qty | Circuit Function & Target Rail | Design Rules |
|:---:|:---:|:---|:---:|:---:|:---|:---|
| **L1** | **0.47 µH** | Isat ≥ 4.5 A, DCR < 35 mΩ | SMD 2016 (2.0 x 1.6 mm) | 1 | **RK806-1 Buck 1 Switching Node:** Powers `VDD_CPU_BIG` | Trace width ≥ 1.0 mm; place < 1.5 mm from PMIC LX1 pin |
| **L2** | **0.47 µH** | Isat ≥ 4.5 A, DCR < 35 mΩ | SMD 2016 (2.0 x 1.6 mm) | 1 | **RK806-1 Buck 2 Switching Node:** Powers `VDD_CPU_LIT` | Trace width ≥ 1.0 mm; place < 1.5 mm from PMIC LX2 pin |
| **L3** | **0.47 µH** | Isat ≥ 4.5 A, DCR < 35 mΩ | SMD 2016 (2.0 x 1.6 mm) | 1 | **RK806-1 Buck 3 Switching Node:** Powers `VDD_NPU_GPU` | Trace width ≥ 1.0 mm; place < 1.5 mm from PMIC LX3 pin |
| **L4** | **1.0 µH** | Isat ≥ 3.2 A, DCR < 50 mΩ | SMD 2016 (2.0 x 1.6 mm) | 1 | **RK806-1 Buck 4 Switching Node:** Powers `VDD_LOGIC` | Trace width ≥ 0.8 mm; place < 1.5 mm from PMIC LX4 pin |
| **L5** | **1.0 µH** | Isat ≥ 3.2 A, DCR < 50 mΩ | SMD 2016 (2.0 x 1.6 mm) | 1 | **RK806-1 Buck 5 Switching Node:** Powers `VCC_DDR` | Trace width ≥ 0.8 mm; place < 1.5 mm from PMIC LX5 pin |
| **FB1** | **120 Ω @ 100MHz** | 2.0 A Continuous, DCR < 40 mΩ | SMD 0603 (1.6 x 0.8 mm) | 1 | **Audio Rail Filter:** Isolates 3.3V analog power from digital switching noise | Place at boundary between system 3.3V and audio supply island |
| **FB2** | **120 Ω @ 100MHz** | 2.0 A Continuous, DCR < 40 mΩ | SMD 0603 (1.6 x 0.8 mm) | 1 | **Wi-Fi RF Filter:** Isolates RTL8723DS 3.3V power from CPU noise | Place at entrance of RTL8723DS power plane |

---

## 5. Protection Devices & Power-Path

| Reference | Component Type | Specifications | Package | Qty | Circuit Function & Target Nets |
|:---:|:---|:---|:---:|:---:|:---|
| **D1** | **TVS ESD Diode Array** | 4-Channel, 5.0 V clamp, ultra-low capacitance (< 0.5 pF) | SOT-23-6 / DFN-10 | 1 | **USB-C High-Speed Line ESD Protection:** Clamps static shock on `USB_DP`, `USB_DN`, `USB_CC1`, and `USB_CC2`. Place immediately behind USB-C connector pads. |
| **D2** | **VBUS High-Energy TVS Diode** | Unidirectional 5.0 V / 6.0 V clamp, high surge capability | SOD-323 / SMA | 1 | **USB VBUS Transient Clamp:** Clamps inductive voltage spikes when hot-plugging USB-C 5V charger. Place directly at `VBUS` entry pad. |
| **U5** | **Ideal Diode Power Multiplexer** | Texas Instruments `LM66100` / `TPS2113A` (continuous rating ≥ 3.0 A) | SC-70-6 / DFN | 1 | **Power-Path Control:** Sits between `VBUS_5V` and `VBAT_BUCK_5V`. Automatically priority-switches system `VSYS_5V` to USB-C power when plugged in, preventing backfeeding into MP2315 battery buck. Voltage drop < 30 mV. |

---

## 6. Resistors (All SMD 0402, 1% Tolerance, 1/16 W / 62.5 mW unless noted)

| Reference | Resistance | Tolerance | Wattage | Package | Qty | Target Circuit & Functional Role | Source / Design Citation |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---|
| **R1, R2** | **5.1 kΩ** | ±1% | 1/16 W | SMD 0402 | 2 | **USB-C CC Pull-Downs:** Connects `CC1` and `CC2` to GND (advertises 5V sink capability to host charger). | USB Type-C Cable & Connector Specification §4.5.1 |
| **R3, R4** | **2.2 kΩ** | ±1% | 1/16 W | SMD 0402 | 2 | **Camera I2C Pull-Ups:** Pulls up `I2C_CAM_SDA` and `I2C_CAM_SCL` strictly to **1.8 V (`VCCIO_1V8`)**, matching Sony IMX708 sensor digital I/O domain. | Sony IMX708 Datasheet & RPi Camera V3 Schematic |
| **R5, R6** | **2.2 kΩ** | ±1% | 1/16 W | SMD 0402 | 2 | **System Control Bus Pull-Ups:** Pulls up host PMIC control bus to matching driving bank `VCCIO` (UNVERIFIED: confirm SPI vs I2C from RK3576 ref schematic). | UNVERIFIED (pending RK3576 ref schematic) |
| **R7, R8** | **10 kΩ** | ±1% | 1/16 W | SMD 0402 | 2 | **Logic Pull-Ups & Straps:** Pulls up `PMIC_PWRON` and hardware reset lines to matching I/O domain. | UNVERIFIED |
| **R9** | **10 kΩ** | ±1% | 1/16 W | SMD 0402 | 1 | **Mic Channel Select:** Sets INMP441 `L/R` channel address. | InvenSense INMP441 Datasheet Table 4 |
| **R10** | **10 kΩ** | ±1% | 1/16 W | SMD 0402 | 1 | **MAX98357A Left Channel Pull-Up:** Pulls up `SD_MODE` to 3.3 V on Left amplifier (yields ~3.0 V with internal 100k pulldown; threshold > 1.39 V selects Left channel). *Note: Verify whether breakout module already carries onboard resistor.* | Maxim MAX98357A Datasheet Table 1 |
| **R11** | **220 kΩ** | ±1% | 1/16 W | SMD 0402 | 1 | **MAX98357A Right Channel Pull-Up:** Pulls up `SD_MODE` to 3.3 V on Right amplifier (yields ~1.03 V with internal 100k pulldown; voltage falls inside 0.77 V – 1.39 V window selecting Right channel). *Note: Verify whether breakout module already carries onboard resistor.* | Maxim MAX98357A Datasheet Table 1 |
| **R12, R13**| **100 kΩ** | ±1% | 1/16 W | SMD 0402 | 2 | **Audio Gain Limiting:** Ties MAX98357A `GAIN` pin to VDD (configures lowest +3 dB gain setting, capping power below 0.8 W RMS to prevent speaker voice-coil damage). | Maxim MAX98357A Datasheet Table 2 |
| **R14, R15**| **22 Ω** | ±1% | 1/16 W | SMD 0402 | 2 | **Master Clock Series Damping:** In-line on 24.000 MHz crystal `OSC_OUT` to eliminate harmonic ringing. | UNVERIFIED (Rockchip hardware design guide) |
| **R16–R18**| **Boot Straps**| ±1% | 1/16 W | SMD 0402 | 3 | **Boot Mode Strapping Resistors:** Pull-up/pull-down pads for eMMC vs USB recovery boot mode. | UNVERIFIED (pending RK3576 EVB schematic) |
| **R19–R22**| **0 Ω (Jumper)**| — | 1/16 W | SMD 0402 | 4 | **RF & Ground Tuning Links:** In-line antenna 50Ω jumper and ground isolation star connections. | UNVERIFIED |

*(Note: R14 300 kΩ for IP2326 has been removed from this board; IP2326 sits on the separate battery charger module).*

---

## 7. Capacitors (SMD Multilayer Ceramic - MLCC)

| Reference | Capacitance | Voltage Rating | Dielectric | Package | Qty | Target Circuit & Functional Role | Source / Sizing Rule |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---|
| **C1, C2** | **18 pF** | 50 V | C0G / NP0 | SMD 0402 | 2 | **24.000 MHz Crystal Load Capacitors:** From `OSC_IN` / `OSC_OUT` to crystal GND. | Formula: 2*(12 pF - 3 pF stray) = 18 pF |
| **C3, C4** | **18 pF** | 50 V | C0G / NP0 | SMD 0402 | 2 | **32.768 kHz RTC Crystal Load Capacitors:** From PMIC RTC oscillator pins to GND. | Standard E12 value (calc: 2*(12.5 pF - 3 pF) ≈ 19 pF) |
| **C5, C6** | **18 pF** | 50 V | C0G / NP0 | SMD 0402 | 2 | **26.000 MHz Wi-Fi Crystal Load Capacitors:** From RTL8723DS XTAL pins to GND. | Formula: 2*(12 pF - 3 pF stray) = 18 pF (UNVERIFIED) |
| **C7, C8** | **22 µF** | 10 V | X5R | SMD 0603 | 2 | **PMIC Main Input Decoupling:** Placed directly at RK806-1 `VSYS_5V` input pins. | RK806-1 Datasheet Reference |
| **C9–C32** | **100 nF (0.1 µF)**| 10 V | X5R / X7R | SMD 0402 | 24 | **High-Frequency Decoupling Array:** Placed directly on the back side of PCB under RK3576 BGA power balls. | UNVERIFIED (pending RK3576 PDN guide) |
| **C33–C40**| **1.0 µF** | 10 V | X5R / X7R | SMD 0402 | 8 | **LDO Rail Output Decoupling:** Placed at RK806-1 LDO outputs (`VDD_1V8`, `VDD_0V9`, `AVDD_1V8`). | UNVERIFIED |
| **C41–C44**| **4.7 µF** | 10 V | X5R / X7R | SMD 0603 | 4 | **Peripherals Decoupling:** RTL8723DS Wi-Fi 3.3V rail and IMX708 camera interface connector. | UNVERIFIED |
| **C45–C50**| **10 µF** | 16 V / 25 V | X5R / X7R | SMD 0603 | 6 | **Bulk Input Filters:** Placed at 5.0V system power bus entry, USB-C VBUS, and audio amplifier supply pins. | UNVERIFIED |
| **C51–C60**| **22 µF** | 10 V | X5R / X7R | SMD 0603 | 10 | **PMIC Buck Switching Filters:** 2 capacitors placed parallel at each of the 5 buck outputs (`CPU_BIG`, `CPU_LIT`, `NPU_GPU`, `LOGIC`, `DDR`). | UNVERIFIED (pending RK806 EVB schematic) |

---

## 8. Connectors, Mechanical Controls & Debug Test Points

| Reference | Component Description | Manufacturer & MPN | Package / Footprint | Pin Count & Signals | Physical Location & Electrical Specs |
|:---:|:---|:---|:---|:---|:---|
| **J1** | **USB Type-C Receptacle (16-Pin)** | Korean Hroparts `TYPE-C-31-M-12` (LCSC `C165948`) | 16-Pin SMD Right Angle | 5V Power, GND, D+, D-, CC1, CC2 | Bottom-rear of right temple arm (5V / 3A rating) |
| **J2** | **MIPI CSI Camera FPC Connector** | Hirose / Amphenol 0.5mm pitch | 26-Pin 0.5mm Bottom Contact | 2-Lane MIPI CSI (Clk ±, D0 ±, D1 ±), 1.8V VCCIO, 3.3V, I2C, Reset, PWDN | Front-right browline edge (connects to front-bridge sensor PCB) |
| **J3** | **Audio & Mic Interconnect Header** | 0.5mm pitch FPC | 10-Pin 0.5mm Bottom Contact | I2S DOUT, DIN, BCLK, LRCK, 3.3V, GND | Lower-front temple interior |
| **J4** | **Battery Power In Header / Pads** | Dedicated high-current solder pads / JST-PH 2.0mm | 2-Pin SMD Pads (20 AWG compatible) | System +5.0V and GND | **Rated ≥ 3.0 A continuous (5.0 A peak)** (fed from MP2315 2S buck) |
| **J5** | **Wi-Fi / Bluetooth RF Antenna Connector** | Hirose / I-PEX MHF4 / U.FL | Ultra-miniature coaxial SMD | 50Ω RF Signal + GND | Upper temple edge; connects to miniature flexible PCB antenna |
| **SW1** | **MaskROM Recovery Key Switch** | XKB `TS-1187A-B-A-B` (LCSC `C318884`) | SMD (3.0 x 4.0 x 1.5 mm) | Tactile push button | Underside right temple; forces RK3576 USB boot flashing mode |
| **SW2** | **System Power-On (PWRON) Switch** | XKB `TS-1187A-B-A-B` (LCSC `C318884`) | SMD (3.0 x 4.0 x 1.5 mm) | Tactile push button | Outer temple arm; signals RK806-1 PMIC to wake up power tree |
| **TP1–TP3**| **Debug UART Test Pads** | Surface test pads (1.0 mm round) | Test Pad | `UART_TX`, `UART_RX`, `GND` | Unpopulated test pads on interior board face for early boot debug |

---

## 9. Fabrication & SMT Assembly Verification Status

* **JLCPCB PCBA Compatibility:** **UNVERIFIED** (Requires formal JLCPCB engineering DFM review and HDI stackup quote for FCCSP-698L package before declaring 100% compatibility).
* **RK3576 Symbol & Footprint Library:** **UNVERIFIED** (Official Rockchip reference design symbol/footprint must be imported and verified against official mechanical package drawing).
* **eMCP Memory Sourcing:** **Consigned Part** (Harvested locally from scrap donor smartphone; not catalog-orderable from JLCPCB).
* **Total Component Count:** ~114 individual parts on the 20–22mm x 75mm board outline.
