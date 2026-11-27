# PROJECT FRIDAY: COMPLETE SCHEMATIC COMPONENT SPECIFICATION & LIBRARY DIRECTORY
## Custom 20–22mm x 75mm Wearable Compute Board (Rockchip RK3576 Architecture)

This document itemizes every single electrical component required for the schematic capture of Project FRIDAY's custom compute PCB. It defines the exact part numbers, footprints, electrical ratings, design constraints, and library sourcing paths for Autodesk Fusion 360 Electronics.

---

## 1. Primary Active Silicon (Integrated Circuits)

| Reference | Component Name & Role | Manufacturer & MPN | LCSC Part # | Package / Footprint | Pin Count & Pitch | Design Rules & Electrical Constraints | Autodesk / Eagle Library Source |
|:---:|:---|:---|:---:|:---|:---:|:---|:---|
| **U1** | **Rockchip RK3576 SoC**<br>Core 6nm 8-Core Application Processor & 6-TOPS NPU | Rockchip<br>`RK3576` | `C42388007` | **FCCSP-698L**<br>(16.1 x 17.2 mm) | 698 Balls<br>0.5 mm ball pitch | • 6-Layer HDI board required (minimum 0.09mm trace/space)<br>• Laser microvias (Layer 1 to Layer 2/3) for BGA ball escape<br>• LPDDR4X 32-bit bus length matching: skew < 0.2 mm<br>• 100Ω differential impedance on MIPI CSI-2 camera pairs<br>• 90Ω differential impedance on USB 2.0 D+/D- lines | Rockchip Official Hardware Reference / EasyEDA Export (`RK3576.lbr`) |
| **U2** | **Rockchip RK806-1 PMIC**<br>Multi-rail companion power management IC | Rockchip<br>`RK806-1` | `C5156483` | **QFN-68**<br>(7.0 x 7.0 mm) | 68 Pins + EP<br>0.35 mm pin pitch | • Exposed ground thermal pad requires minimum 16 vias to solid GND plane<br>• Buck switching inductors (L1–L4) placed immediately adjacent to LX pins<br>• Buck output capacitors grounded directly to PMIC power ground island | LCSC / EasyEDA Pre-Made Footprint (`C5156483.lbr`) |
| **U3** | **Samsung 4GB LPDDR4X + 64GB eMMC eMCP**<br>Unified RAM & fast OS flash memory | Samsung<br>`KM3V...` series | Harvested / Donor | **BGA-254**<br>(11.5 x 13.0 mm) | 254 Balls<br>0.5 mm ball pitch | • Sits directly adjacent to RK3576 DDR controller ball bank<br>• High-speed DQ/DQS traces routed on Layer 3 (stripline between solid GND planes)<br>• Guard traces and GND stitching vias every 3 mm along DDR bus | Standard JEDEC BGA-254 (`bga254.lbr` / SnapEDA) |
| **U4** | **Realtek RTL8723DS Wi-Fi / Bluetooth IC**<br>2.4 GHz 802.11b/g/n + BT 4.2 radio | Realtek<br>`RTL8723DS-CG` | `C2762334` | **WQFN-48**<br>(6.0 x 6.0 mm) | 48 Pins + EP<br>0.4 mm pin pitch | • 50Ω coplanar waveguide with ground reference to antenna connection pad<br>• Solid ground keepout under RF matching network<br>• SDIO clock and data lines length matched within 1.0 mm | LCSC / EasyEDA Pre-Made Footprint (`C2762334.lbr`) |

---

## 2. Frequency Control & Clocks

| Reference | Frequency | Tolerance & Load | Manufacturer & MPN | LCSC Part # | Package / Footprint | Design Rules & Electrical Constraints | Library Source |
|:---:|:---:|:---:|:---|:---:|:---|:---|:---|
| **Y1** | **24.000 MHz** | ±10 ppm<br>CL = 12 pF | YXC<br>`X322524MOB4SI` | `C70590` | **SMD-3225-4P**<br>(3.2 x 2.5 mm) | • Master system clock for RK3576 oscillator circuit<br>• Guard ring of solid GND surrounding crystal traces<br>• No high-speed digital signals routed on inner layers underneath crystal | Fusion Managed `crystal.lbr` / LCSC `C70590` |
| **Y2** | **32.768 kHz** | ±20 ppm<br>CL = 12.5 pF | Epson<br>`Q13FC13500004` | `C32346` | **SMD-3215-2P**<br>(3.2 x 1.5 mm) | • Real-Time Clock (RTC) sleep clock for RK806-1 PMIC<br>• Direct point-to-point routing to PMIC RTC pins (< 8 mm trace length) | Fusion Managed `crystal.lbr` / LCSC `C32346` |

---

## 3. Power Inductors & Ferrite Beads

| Reference | Value / Inductance | Rating & Specs | Package | Qty | Circuit Function & Target Rail | Design Rules |
|:---:|:---:|:---|:---:|:---:|:---|:---|
| **L1** | **0.47 µH** | Isat = 4.5 A, DCR < 35 mΩ | SMD 2016 (2.0 x 1.6 mm) | 1 | **RK806-1 Buck 1 Switching Node:** Powers `VDD_CPU` core rail | High-current trace width ≥ 1.0 mm; place < 1.5 mm from PMIC LX1 pin |
| **L2** | **0.47 µH** | Isat = 4.5 A, DCR < 35 mΩ | SMD 2016 (2.0 x 1.6 mm) | 1 | **RK806-1 Buck 2 Switching Node:** Powers `VDD_NPU` core rail | High-current trace width ≥ 1.0 mm; place < 1.5 mm from PMIC LX2 pin |
| **L3** | **1.0 µH** | Isat = 3.2 A, DCR < 50 mΩ | SMD 2016 (2.0 x 1.6 mm) | 1 | **RK806-1 Buck 3 Switching Node:** Powers `VDD_LOGIC` system rail | High-current trace width ≥ 0.8 mm; place < 1.5 mm from PMIC LX3 pin |
| **L4** | **1.0 µH** | Isat = 3.2 A, DCR < 50 mΩ | SMD 2016 (2.0 x 1.6 mm) | 1 | **RK806-1 Buck 4 Switching Node:** Powers `VCC_DDR` memory rail | High-current trace width ≥ 0.8 mm; place < 1.5 mm from PMIC LX4 pin |
| **FB1** | **120 Ω @ 100MHz** | 2.0 A Continuous, DCR < 40 mΩ | SMD 0603 (1.6 x 0.8 mm) | 1 | **Audio Rail Filter:** Isolates 3.3V analog power from digital switching noise | Place at boundary between system 3.3V and audio supply island |
| **FB2** | **120 Ω @ 100MHz** | 2.0 A Continuous, DCR < 40 mΩ | SMD 0603 (1.6 x 0.8 mm) | 1 | **Wi-Fi RF Filter:** Isolates RTL8723DS 3.3V power from CPU noise | Place at entrance of RTL8723DS power plane |

---

## 4. Protection & Diodes

| Reference | Component Type | Specifications | Package | Qty | Circuit Function & Target Nets |
|:---:|:---|:---|:---:|:---:|:---|
| **D1** | **TVS ESD Protection Diode Array** | 4-Channel, 5.0 V clamp, ultra-low capacitance (< 0.5 pF) | SOT-23-6 / DFN-10 | 1 | **USB-C Port High-Speed ESD Protection:** Clamps static shock on `USB_DP`, `USB_DN`, `USB_CC1`, and `USB_CC2`. Place immediately behind USB-C connector pads. |
| **D2** | **Low-Vf Schottky Barrier Diode** | 20 V, 1.0 A, forward drop Vf < 0.35 V | SOD-323 (SMD) | 1 | **Reverse Backfeed Protection:** Prevents USB-C 5.0V bus from backfeeding into the MP2315 battery buck converter when both USB and battery are connected simultaneously. |

---

## 5. Resistors (All SMD 0402, 1% Tolerance, 1/16 W / 62.5 mW)

| Reference | Resistance | Tolerance | Wattage | Package | Qty | Target Circuit & Functional Role |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| **R1, R2** | **5.1 kΩ** | ±1% | 1/16 W | SMD 0402 | 2 | **USB-C CC Pull-Downs:** Connects `CC1` and `CC2` to GND (tells USB-C charger glasses are a 5V sink). |
| **R3–R6** | **2.2 kΩ** | ±1% | 1/16 W | SMD 0402 | 4 | **I2C Bus Pull-Ups:** Pulls up `I2C_SDA` and `I2C_SCL` to 3.3V for PMIC control and Sony IMX708 sensor. |
| **R7–R10** | **10 kΩ** | ±1% | 1/16 W | SMD 0402 | 4 | **Logic Pull-Ups & Selects:** INMP441 L/R mic channel select, MAX98357A Left divider pull-up, and PMIC reset. |
| **R11** | **220 kΩ** | ±1% | 1/16 W | SMD 0402 | 1 | **Audio Channel Select Divider:** Pull-down on MAX98357A `SD_MODE` to set 0.77V–1.39V Left channel window. |
| **R12, R13**| **100 kΩ** | ±1% | 1/16 W | SMD 0402 | 2 | **Audio Gain Limiting:** Ties MAX98357A `GAIN` pin to VDD (sets +3 dB gain to protect 1510 speakers). |
| **R14** | **300 kΩ** | ±1% | 1/16 W | SMD 0402 | 1 | **IP2326 Charge Current Set:** Connects Pin 11 `ISET` to GND (enforces strict 300 mA 1C battery charge rate). |
| **R15, R16**| **22 Ω** | ±1% | 1/16 W | SMD 0402 | 2 | **Crystal Damping:** Series damping on 24.000 MHz crystal `OSC_OUT` to eliminate harmonic ringing. |
| **R17–R20**| **0 Ω (Jumper)**| — | 1/16 W | SMD 0402 | 4 | **RF & Ground Jumpers:** Optional 50Ω antenna link tuning and analog audio ground star-connection isolation. |

---

## 6. Capacitors (SMD Multilayer Ceramic - MLCC)

| Reference | Capacitance | Voltage Rating | Dielectric | Package | Qty | Target Circuit & Functional Role |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| **C1, C2** | **12 pF** | 50 V | C0G / NP0 | SMD 0402 | 2 | **24.000 MHz Crystal Load Capacitors:** From `OSC_IN` and `OSC_OUT` to crystal GND. |
| **C3, C4** | **12.5 pF** | 50 V | C0G / NP0 | SMD 0402 | 2 | **32.768 kHz RTC Crystal Load Capacitors:** From PMIC RTC oscillator pins to GND. |
| **C5–C28** | **100 nF (0.1 µF)**| 10 V | X5R / X7R | SMD 0402 | 24 | **High-Frequency Decoupling Array:** Placed directly on the back side of PCB under RK3576 BGA power balls. |
| **C29–C36**| **1.0 µF** | 10 V | X5R / X7R | SMD 0402 | 8 | **LDO Rail Output Decoupling:** Placed at RK806-1 LDO outputs (`VDD_1V8`, `VDD_0V9`, `AVDD_1V8`). |
| **C37–C40**| **4.7 µF** | 10 V | X5R / X7R | SMD 0603 | 4 | **Peripherals Decoupling:** RTL8723DS Wi-Fi 3.3V rail and IMX708 camera interface connector. |
| **C41–C46**| **10 µF** | 16 V / 25 V | X5R / X7R | SMD 0603 | 6 | **Bulk Input Filters:** Placed at 5.0V system power bus entry, USB-C VBUS, and audio amplifier supply pins. |
| **C47–C54**| **22 µF** | 10 V | X5R / X7R | SMD 0603 | 8 | **PMIC Buck Switching Filters:** 2 capacitors placed parallel at each buck output (`CPU`, `NPU`, `LOGIC`, `DDR`). |

---

## 7. Connectors & Mechanical Controls

| Reference | Component Description | Manufacturer & MPN | LCSC Part # | Package / Footprint | Pin Count & Signals | Physical Location on Frame |
|:---:|:---|:---|:---:|:---|:---|:---|
| **J1** | **USB Type-C Receptacle (16-Pin)** | Korean Hroparts<br>`TYPE-C-31-M-12` | `C165948` | 16-Pin SMD Right Angle | 5V Power, GND, D+, D-, CC1, CC2 | Bottom-rear of right temple arm (charging & ADB flash port) |
| **J2** | **MIPI CSI Camera FPC Connector** | Hirose / Amphenol 0.5mm pitch | Standard | 26-Pin 0.5mm Bottom Contact | 2-Lane MIPI CSI (Clk ±, D0 ±, D1 ±), 3.3V, I2C, Reset, PowerDown | Front-right browline edge (connects to front-bridge sensor PCB) |
| **J3** | **Audio & Mic Interconnect Header** | 0.5mm pitch FPC | Standard | 10-Pin 0.5mm Bottom Contact | I2S DOUT, DIN, BCLK, LRCK, 3.3V, GND (routes audio to both temples) | Lower-front temple interior |
| **J4** | **Battery Power In Pads / Header** | 2-Pin 1.25mm / SMD Solder Pads | Standard | 2-Pin SMD (2.54mm spacing) | System +5.0V and GND (fed from MP2315 2S buck regulator) | Interior center temple |
| **SW1** | **MaskROM Recovery Key Switch** | XKB Connection<br>`TS-1187A-B-A-B` | `C318884` | SMD (3.0 x 4.0 x 1.5 mm) | Tactile push button (forces RK3576 into USB boot flashing mode) | Recessed underside of right temple arm (pinhole access) |

---

## 8. Summary of Components for DRC & SMT

* **Total Line Items:** 28 distinct component types
* **Total Component Count:** 108 individual parts on the 20–22mm x 75mm board
* **Solder Joint Count:** ~1,150 SMD solder pads / balls
* **Robotic SMT Assembly Compatibility:** 100% compatible with JLCPCB PCBA capabilities (0.5mm BGA, 0402 passives, 6-layer stackup).
