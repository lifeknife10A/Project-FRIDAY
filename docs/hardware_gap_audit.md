# Project FRIDAY Hardware Gap Audit: Schematic, PCB, and 3D Assembly

**Document ID:** `docs/hardware_gap_audit.md`  
**Date:** 2026-11-27  
**Scope:** Complete hardware gap audit for Project FRIDAY custom wearable compute board and peripheral subsystems (RK3576 architecture). Read-only audit across schematics, component libraries, 2D PCB layout inputs, and 3D mechanical CAD/assembly.  
**Baseline References:**
- `docs/plan.md` (v9.1 / v9.2 Systems Architecture)
- `docs/plan1.md` & `docs/plan1_context.md` (Current milestones, decisions D1–D15)
- `CLAUDE.md` §7 (Current hardware state & carry-in items Y1–Y4)
- `docs/schematic_components.md` (Component electrical specification @ 6bc8e11 / 4d02ff5)
- `docs/hardware_bom.md` (Hardware financial matrix & bill of materials)
- `hardware/compute_board/out/` (`FRIDAY_Compute_SCH1.sch`, netlist CSV, BOM CSV, ERC log)
- `hardware/compute_board/io_bank_map.md` & `SCH-1_evb_crossref.md`
- `hardware/compute_board/emcp_ballmap_source.csv` & `docs/reference_designs/notes/`
- `docs/datasheets/` (Rockchip RK3576 DS Rev 1.5, HDG V1.1, RK806 DS Rev 1.3, EVB1 schematic, peripheral datasheets)
- `libraries/*.lbr` (19 EAGLE/Fusion component libraries)

---

## A. Schematic Coverage

Audit of all functional blocks required for Project FRIDAY across the core compute board, front-bridge camera board, and temple carrier/battery boards.

### A.1 Functional Block Coverage Matrix

| Functional Block | Status | Evidence (File Path / Line) | Needed For | Who / What Can Supply It | Blocking Which Step |
| :--- | :---: | :--- | :---: | :--- | :--- |
| **Input Power Path**<br>(USB-C 16-pin, TPS2121 power mux, SY8205FCC 5V buck) | **HAVE** | `hardware/compute_board/out/FRIDAY_Compute_SCH1.sch` (Sheet 1); `hardware/compute_board/out/FRIDAY_Compute_SCH1_netlist.csv` (Nets `VBUS_5V`, `VBAT_2S_IN`, `VCC5V0_SYS_S5`) | SCH / PCB | Captured in SCH-1 | Complete |
| **Battery Subsystem & Charging**<br>(2S LiPo cells, IP2326 boost charger, HY2212 balance, HY2120 protection) | **MISSING** | `docs/hardware_bom.md` (Items 17–19); `docs/schematic_components.md` (§3); not found in any `.sch`; IP2326 `ISET=300k for 300mA` [UNVERIFIED (no source)] | SCH / PCB / MECH | Hydrogen / Sol (design schematic sheet for Left Temple carrier board) | Blocks Left Temple carrier board schematic & PCB |
| **PMIC & Intermediate Bucks**<br>(RK806S-5, TMI3112H x2, SY6280, CW3301 load switches) | **HAVE** | `hardware/compute_board/out/FRIDAY_Compute_SCH1.sch` (Sheets 2 & 3); `FRIDAY_Compute_SCH1_netlist.csv` (104 nets, BUCK1–10, PLDO1–6, NLDO1–5) | SCH / PCB | Captured in SCH-1 | Complete |
| **SoC Core Power, Clocks, Reset & Boot**<br>(RK3576 power/GND balls, decaps, 24MHz crystal X1, NPOR, SARADC boot SW1, PWRON SW2) | **HAVE** | `hardware/compute_board/out/FRIDAY_Compute_SCH1.sch` (Sheets 4 & 5); `io_bank_map.md`; ERC log 0 errors | SCH / PCB | Captured in SCH-1 | Complete |
| **eMCP Memory Subsystem**<br>(Samsung/Hynix 254-ball eMCP: LPDDR4X 2-ch 16-bit + eMMC 5.1 8-bit bus; carry-ins Y1–Y4 in `CLAUDE.md` §7) | **MISSING** | `hardware/compute_board/emcp_ballmap_source.csv`; `docs/reference_designs/notes/emcp_hynix_H9HP52ACPMADAR.md`; not in `.sch` | SCH / PCB | Astra (high/xhigh) / Sol in SCH-2 round | Blocks SCH-2 schematic capture & compute board layout |
| **eMCP Qualification on RK3576 Memory Support List (QVL)** | **MISSING** | Rockchip official RK3576 memory support list not in repo; H9HP52ACPMADAR support unconfirmed | SCH / SW | Researcher / Krishna | Blocks confirmation of DDR/eMMC loader support before fab |
| **Front-Bridge Camera Subsystem**<br>(IMX708 SA31VA30P, DF37 connector, 1.1V buck, 1.8V/2.8V LDOs, 24MHz osc, I2C) | **MISSING** | `docs/datasheets/Raspberry Pi Camera Module 3 Schematic.pdf`; `docs/hardware_bom.md` (Item 13); not found in `.sch` | SCH / PCB / MECH | Astra / Sol in SCH-3 round | Blocks camera bridge PCB & front-frame optical assembly |
| **Camera Bridge Filtering & POR Supervisor**<br>(CSI common-mode chokes + POR holding XCLR until MCLK) | **MISSING** | Raspberry Pi Camera Module 3 reference schematic `RP-008969-SD`; not found in `.sch` | SCH / PCB | Sol / Astra in SCH-3 round | Blocks camera bridge schematic & signal integrity |
| **IMX708 Linux Kernel Driver & ISP Pipeline on RK3576** | **MISSING** | Driver & Rockchip ISP pipeline support unverified in RK3576 BSP | SW / BRINGUP | Researcher / Krishna | Mandatory gate before ordering camera bridge board |
| **MIPI CSI-2 Differential Routing**<br>(RK3576 MIPI_CSI0 2/4-lane receiver to connector) | **MISSING** | `hardware/compute_board/io_bank_map.md` (VCCIO5 planned); HDG §2.3.4 (p.49); not wired in SCH-1 | SCH / PCB | Astra / Sol in SCH-3 round | Blocks SCH-3 schematic capture |
| **Wi-Fi / Bluetooth Wireless Subsystem**<br>(RTL8723DS-CG, 26MHz crystal, U.FL connector, RF pi-filter, SDIO 3.0 bus) | **MISSING** | `docs/datasheets/RTL8723DS-CG Datasheet.pdf`; `hardware/compute_board/io_bank_map.md` (VCCIO3 planned); not in `.sch` | SCH / PCB | Sol / Hydrogen in SCH-4 round | Blocks SCH-4 wireless capture & RF layout |
| **Wi-Fi / BT Antenna Element**<br>(Physical antenna part: ceramic chip or internal FPC) | **MISSING** | `docs/hardware_bom.md` (only U.FL J12/J5 receptacle listed; zero antenna part/MPN in BOM) | SCH / PCB / MECH | Krishna / Researcher | Blocks RF path completion & frame enclosure integration |
| **Audio Subsystem**<br>(Dual INMP441 MEMS mics, dual MAX98357A I2S amps, dual 1510 oval speakers) | **MISSING** | `docs/datasheets/INMP441 Datasheet.pdf`; `docs/datasheets/MAX98357A Datasheet.PDF`; `io_bank_map.md` (VCCIO2 planned); not in `.sch` | SCH / PCB / MECH | Sol / Hydrogen in SCH-4 round | Blocks audio schematic & acoustic chamber design |
| **Tactile Buttons & UI Triggers**<br>(PWRON SW2, MaskROM SW1, TTP223 capacitive touch trigger) | **PARTIAL** | SW1/SW2 captured in `FRIDAY_Compute_SCH1.sch` (Sheets 1 & 5); TTP223 capacitive sensor missing from all `.sch` | SCH / PCB / MECH | Hydrogen / Sol in SCH-4 round | Blocks touch sensor wiring & temple UI |
| **Debug UART**<br>(UART0_M0 TX/RX dedicated test pads TP1/TP2) | **HAVE** | `hardware/compute_board/out/FRIDAY_Compute_SCH1.sch` (Sheet 5, nets `UART0_TX_M0_DEBUG`, `UART0_RX_M0_DEBUG`) | SCH / PCB | Captured in SCH-1 | Complete |
| **USB 2.0 OTG Data Path**<br>(J1 D+/D- through USBLC6-2SC6 TVS D1 to RK3576 USB20_OTG0 balls) | **PARTIAL** | J1/D1 wired in `FRIDAY_Compute_SCH1.sch` (Sheet 1); USB20_OTG0 balls on RK3576 (Sheet 4/5) not wired | SCH / PCB | Astra / Sol in SCH-2/SCH-4 | Blocks USB ADB/firmware flashing |
| **Status & Indicator LEDs**<br>(VBUS, charge status, PMIC power-good, SoC run/status) | **MISSING** | Not found in `FRIDAY_Compute_SCH1.sch` or `docs/schematic_components.md` | SCH / PCB | Hydrogen / Sol | Blocks visual debug/charge status indication |
| **Production & Hardware Test Points**<br>(Power rails, reset, boot, clk, JTAG/SWD, battery sense) | **PARTIAL** | TP1/TP2 (UART0) present in SCH-1; test points for power rails (`VCC5V0_SYS`, `VBAT`, PMIC bucks) missing | SCH / PCB | Hydrogen / Sol in SCH-4 | Blocks bare-board bring-up & bed-of-nails testing |
| **FPC Interconnect Connectors**<br>(FH12-10S-0.5SH & FH12-24S-0.5SH temple-to-bridge flex) | **MISSING** | `libraries/FH12-10S-0.5SH_55_.lbr`; `libraries/FH12-24S-0.5SH_55_.lbr`; pinouts completely undefined | SCH / PCB / MECH | Researcher / Krishna (define flex pinout) | Blocks flex harness design & schematic inter-board links |
| **RK806S-5 Dedicated OTP / Variant Document** | **MISSING** | `docs/datasheets/` (only generic `Rockchip RK806 Datasheet.pdf` Rev 1.3 present; RK806S-5 dedicated OTP register doc missing) | SCH / SW | Researcher / Krishna | Blocks verification of PMIC startup registers and power sequence |

### A.2 Datasheet & Library Availability per Block

| Part Role / MPN | Datasheet Status | Datasheet Path | Library Status | Library Path | In BOM? | In `schematic_components.md`? |
| :--- | :---: | :--- | :---: | :--- | :---: | :---: |
| **RK3576 SoC** | HAVE | `docs/datasheets/Rockchip RK3576 Datasheet.pdf` | HAVE | `libraries/RK3576.lbr` | Yes (Item 1) | Yes (§1 U1) |
| **RK806S-5 PMIC** | PARTIAL | `docs/datasheets/Rockchip RK806 Datasheet.pdf` (generic RK806-1, not RK806S-5 OTP) | HAVE | `libraries/RK806-1.lbr` (needs MPN attribute fix) | Yes (Item 2) | Yes (§1 U2) |
| **H9HP52ACPMADAR (eMCP)** | HAVE (Local) | `references_local/H9HP52ACPMADAR-KMM_Rev1.0.pdf` (quarantined) | **MISSING** | Not found in `libraries/` | Yes (Item 9) | Yes (§1 U3) |
| **RTL8723DS-CG (Wi-Fi/BT)** | HAVE | `docs/datasheets/RTL8723DS-CG Datasheet.pdf` | HAVE | `libraries/RTL8723DS-CG.lbr` | Yes (Item 3) | Yes (§1 U4) |
| **TPS2121RUXR (Power Mux)** | HAVE | `docs/datasheets/TPS2120 Datasheet.PDF` | HAVE | `libraries/TPS2121RUXR.lbr` | Yes (Item 20) | Yes (§1 U5) |
| **SY8205FCC (Battery Buck)**| HAVE | `docs/datasheets/SY8205 Step Down Regulator Application Note.pdf` | HAVE | `libraries/SY8205FCC.lbr` | Yes (Item 20) | Yes (§1 U10) |
| **TMI3112H (Ext Buck x2)** | HAVE | `docs/datasheets/TMI3112H Datasheet.pdf` | PARTIAL | In `FRIDAY_SCH1_Support.lbr` (SOT-23-5 footprint) | Yes (Kit 10) | Yes (§1 U6, U7) |
| **SY6280AAC (Load Switch)** | HAVE | `docs/datasheets/SY6280 Power Distribution.pdf` | HAVE | `libraries/SY6280AAC.lbr` | No (in Kit) | Yes (§1 U8) |
| **CW3301 (Load Switch)** | MISSING | Not found in `docs/datasheets/` | PARTIAL | In `FRIDAY_SCH1_Support.lbr` (WLCSP-4 footprint) | No (in Kit) | Yes (§1 U9) |
| **IP2326 (2S Charger)** | **MISSING** | Not found in `docs/datasheets/` | **MISSING** | Not found in `libraries/` | Yes (Item 18)| Mentioned in §3 |
| **HY2212 / HY2120 (BMS)** | **MISSING** | Not found in `docs/datasheets/` | **MISSING** | Not found in `libraries/` | Yes (Item 19)| Mentioned in §3 |
| **IMX708 Sensor Assembly** | PARTIAL | `docs/datasheets/Raspberry Pi Camera Module 3 Sensor Assembly.pdf` (mechanical only) | **MISSING** | Not found in `libraries/` | Yes (Item 13)| Yes (§1 U11) |
| **DF37NC-30DS-0.4V (B2B)** | MISSING | Not found in `docs/datasheets/` | HAVE | `libraries/DF37NC-30DS-0.4V_51_.lbr` | Yes (in Item 13)| Yes (§6 J2) |
| **INMP441 (MEMS Mic)** | HAVE | `docs/datasheets/INMP441 Datasheet.pdf` | HAVE | `libraries/INMP441.lbr` | Yes (Item 14)| Yes (§8 MIC1/2) |
| **MAX98357AETE+T (Amp)** | HAVE | `docs/datasheets/MAX98357A Datasheet.PDF` | HAVE | `libraries/MAX98357AETE_T.lbr` | Yes (Item 15)| Yes (§8 U12/13) |
| **1510 Dynamic Speaker** | **MISSING** | Not found in `docs/datasheets/` | **MISSING** | Not found in `libraries/` (solder pads needed) | Yes (Item 16)| Mentioned in §8 |
| **TTP223 (Touch Sensor)** | **MISSING** | Not found in `docs/datasheets/` | **MISSING** | Not found in `libraries/` | Yes (Item 21)| Missing (§1) |
| **24MHz Crystal (X3225...)**| HAVE | `docs/datasheets/C70590.pdf` | HAVE | `libraries/X322524MOB4SI_24MHz.lbr` | Yes (Item 4) | Yes (§4 X1) |
| **26MHz Crystal (C1E...)** | MISSING | Not found in `docs/datasheets/` | HAVE | `libraries/C1E-26.000-6-3030-R.lbr` | No (in Kit) | Yes (§4 Y1) |
| **Type-C Receptacle** | HAVE | `docs/datasheets/C165948.pdf` | HAVE | `libraries/TYPE-C-31-M-12.lbr` | Yes (Item 6) | Yes (§6 J1) |
| **Tactile Switch (TS-1187)**| HAVE | `docs/datasheets/C318884.pdf` | HAVE | `libraries/TS-1187A-B-A-B.lbr` | Yes (Item 7) | Yes (§6 SW1/2) |
| **U.FL RF Receptacle** | MISSING | Not found in `docs/datasheets/` | HAVE | `libraries/U.FL-R-SMT-1_01_.lbr` | No (in Kit) | Yes (§6 J12) |
| **USBLC6-2SC6 (TVS)** | MISSING | Not found in `docs/datasheets/` | HAVE | `libraries/USBLC6-2SC6.lbr` | No (in Kit) | Yes (§5 D1) |
| **FH12-10S-0.5SH (FPC 10P)**| MISSING | Not found in `docs/datasheets/` | HAVE | `libraries/FH12-10S-0.5SH_55_.lbr` | Yes (Item 24)| Missing (§6) |
| **FH12-24S-0.5SH (FPC 24P)**| MISSING | Not found in `docs/datasheets/` | HAVE | `libraries/FH12-24S-0.5SH_55_.lbr` | Yes (Item 24)| Missing (§6) |
| **Front-Bridge Regulators** | **MISSING** | 1.1V buck, 1.8V LDO, 2.8V LDO datasheets not present | **MISSING** | Not identified or created | In Item 13 | Generic in §3 |
| **Wi-Fi/BT Antenna Part** | **MISSING** | Not in `docs/datasheets/` | **MISSING** | None in `libraries/` | Missing (only U.FL in BOM) | Missing |
| **Camera CSI Chokes & POR** | PARTIAL | Reference schematic `RP-008969-SD` present; discrete chokes/POR DS missing | **MISSING** | None in `libraries/` | Missing | Missing |

---

## B. Component Libraries & Footprint Verification

Audit of all 19 component library files (`libraries/*.lbr`) against manufacturer land patterns, package dimensions, and symbol accuracy.

### B.1 Library Component Audit Table

| Component / MPN | Symbol Status | Footprint Package | Footprint Verification Status | Evidence / Notes | Needed For | Who Can Supply |
| :--- | :---: | :--- | :---: | :--- | :---: | :--- |
| **RK3576 SoC** (`RK3576.lbr`) | HAVE (6 gates) | `BGA-698_16.1X17.2_0.55-0.65` | **UNVERIFIED** | 698 balls; mixed 0.55/0.60/0.65 mm pitch. Unverified ball-by-ball against RK3576 DS §2 package drawing (p.24). | SCH / PCB | Sol / Researcher |
| **RK806S-5 PMIC** (`RK806-1.lbr`) | HAVE | `QFN-68-EP_7X7_0.35` | **PARTIAL** | Footprint matches standard QFN-68 0.35mm pitch; **MPN attribute is set to `RK806-1` instead of `RK806S-5`**; pins VOUT1–10 must remain passive. | SCH / PCB | Hydrogen / Sol |
| **H9HP52ACPMADAR (eMCP)** | **MISSING** | `BGA-254_11.5X13.0_0.50` | **MISSING** | No 254-ball library exists in repo. Requires JEDEC BGA-254 land pattern (11.5 x 13.0 mm, 0.5 mm pitch, ball diameter 0.30 mm). | SCH / PCB | Astra / Sol (generate from CSV) |
| **RTL8723DS-CG** (`RTL8723DS-CG.lbr`) | HAVE | `QFN48_RTL8723_RTK` | **UNVERIFIED** | 48-pin + EP (6x6 mm, 0.4 mm pitch). Vendor library from EasyEDA; pad dimensions unverified against RTL8723DS DS §8. | SCH / PCB | Researcher / Sol |
| **TPS2121RUXR** (`TPS2121RUXR.lbr`) | HAVE | `WQFN-12_2X2.5_0.5` | **UNVERIFIED** | TI package RUX (12-pin WQFN, 2.0 x 2.5 mm, 0.5 mm pitch). Unverified against TI DS land pattern. | SCH / PCB | Sol |
| **SY8205FCC** (`SY8205FCC.lbr`) | HAVE | `TSOT-23-6` | **UNVERIFIED** | TSOT-23-6 package. Unverified against Silergy land pattern. | SCH / PCB | Sol |
| **TMI3112H** (`FRIDAY_SCH1_Support.lbr`) | HAVE | `SOT-23-5` | **UNVERIFIED** | Generic SOT-23-5 package. Dedicated library `TMI3112H.lbr` does not exist. | SCH / PCB | Sol |
| **SY6280AAC** (`SY6280AAC.lbr`) | HAVE | `SOT-23-5` | **UNVERIFIED** | Standard SOT-23-5 footprint. Unverified against Silergy DS. | SCH / PCB | Sol |
| **CW3301** (`FRIDAY_SCH1_Support.lbr`) | HAVE | `WLCSP-4` | **UNVERIFIED** | 4-ball 0.4 mm pitch wafer chip scale package. Extreme soldering tolerance; unverified. | SCH / PCB | Sol |
| **IP2326 2S Charger** | **MISSING** | `QFN-24` / `ESOP-8` | **MISSING** | No symbol or footprint exists in repo. Injoinic package land pattern needed. | SCH / PCB | Hydrogen / Sol |
| **HY2212 / HY2120 BMS** | **MISSING** | `SOT-23-6` | **MISSING** | No symbol or footprint exists in repo. | SCH / PCB | Hydrogen / Sol |
| **DF37NC-30DS-0.4V** (`DF37NC-30DS...lbr`) | HAVE | `DF37NC-30DS-0.4V(51)` | **UNVERIFIED** | Hirose 30-pin receptacle (0.4 mm pitch). High risk for SMT bridging; unverified against Hirose drawing. | SCH / PCB | Researcher / Sol |
| **FH12-10S-0.5SH** (`FH12-10S...lbr`) | HAVE | `FH12-10S-0.5SH(55)` | **UNVERIFIED** | Hirose 10-pin 0.5 mm pitch FPC connector. Unverified. | SCH / PCB | Sol |
| **FH12-24S-0.5SH** (`FH12-24S...lbr`) | HAVE | `FH12-24S-0.5SH(55)` | **UNVERIFIED** | Hirose 24-pin 0.5 mm pitch FPC connector. Unverified. | SCH / PCB | Sol |
| **INMP441** (`INMP441.lbr`) | HAVE | `LGA-4.72X3.76` | **UNVERIFIED** | Bottom-port MEMS microphone package. Acoustic port hole in PCB unverified against InvenSense DS. | SCH / PCB | Researcher / Sol |
| **MAX98357AETE+T** (`MAX98357AETE_T.lbr`) | HAVE | `TQFN-16-EP_3X3_0.5` | **UNVERIFIED** | Maxim 16-pin TQFN with exposed pad (3x3 mm). Unverified against Maxim DS land pattern. | SCH / PCB | Sol |
| **X322524MOB4SI (24MHz)** (`X3225...lbr`) | HAVE | `SMD-3225-4P` | **UNVERIFIED** | 3.2 x 2.5 mm 4-pad crystal footprint. Unverified. | SCH / PCB | Sol |
| **C1E-26.000-6-3030-R (26MHz)** (`C1E...lbr`)| HAVE | `SMD-3030-4P` | **UNVERIFIED** | 3.0 x 3.0 mm 4-pad crystal footprint. Unverified. | SCH / PCB | Sol |
| **TYPE-C-31-M-12** (`TYPE-C-31-M-12.lbr`) | HAVE | `TYPE-C-16P-SMD` | **UNVERIFIED** | Korean Hroparts 16-pin hybrid SMD/TH shield tabs. Critical alignment with enclosure slot; unverified. | SCH / PCB / MECH | Krishna / Sol |
| **TS-1187A-B-A-B** (`TS-1187...lbr`) | HAVE | `SW-SMD-3X4` | **UNVERIFIED** | 3 x 4 mm SMD tactile button. Unverified. | SCH / PCB / MECH | Sol |
| **U.FL-R-SMT-1** (`U.FL-R-SMT-1_01_.lbr`) | HAVE | `U.FL-R-SMT-1(01)` | **UNVERIFIED** | Hirose ultra-miniature RF receptacle. Ground pad solder mask expansion unverified. | SCH / PCB | Sol |
| **USBLC6-2SC6** (`USBLC6-2SC6.lbr`) | HAVE | `SOT-23-6` | **UNVERIFIED** | ST SOT-23-6 ESD protection diode. Unverified. | SCH / PCB | Sol |
| **Passives: Resistors** (`FRIDAY_SCH1...lbr`)| HAVE | `R0201`, `R0402`, `R0603` | **UNVERIFIED** | Standard IPC-7351 footprints. Decoupling capacitor pitch under BGA unverified. | PCB | Sol |
| **Passives: Capacitors** (`FRIDAY_SCH1...lbr`)| HAVE | `C0201`, `C0402`, `C0402_BGA`, `C0603`, `C0805` | **UNVERIFIED** | `C0402_BGA` requires precise pad clearance for back-side BGA placement. | PCB | Sol |
| **Passives: Inductors** (`FRIDAY_SCH1...lbr`)| HAVE | `IND_2016`, `IND_2520`, `IND_4040` | **UNVERIFIED** | Shielded power inductor footprints. Height and saturation current pad geometry unverified. | PCB / MECH | Sol |

---

## C. 2D PCB Layout Inputs & Design Rules

Audit of mechanical board geometry, layer stack-up, fabrication constraints, and high-speed routing rules across all boards.

### C.1 Board Outlines & Form Factors

| Board | Target Dimensions | Shape / Mounting Details | Status | Evidence (File Path / Line) | Needed For | Who Can Supply |
| :--- | :--- | :--- | :---: | :--- | :---: | :--- |
| **Compute Board (Right Temple)** | 20–22 mm width × 75 mm length | Rectangular with temple contour taper; 2x M1.6 mounting holes; cutouts for Type-C and FPC | **MISSING** | `docs/schematic_components.md` (Title); `docs/plan.md` (L411); no DXF/IDF/BRD file exists | PCB / MECH | Krishna / MCAD Agent (export DXF from glasses frame CAD) |
| **Front-Bridge Board (Center Bridge)** | ~12 mm width × 15–20 mm length | Houses IMX708 SA31VA30P module, DF37 connector, local regulators; 6° downward optical tilt | **MISSING** | `docs/plan.md` (L217, L374); `docs/hardware_bom.md` (Item 13); no DXF file exists | PCB / MECH | Krishna / MCAD Agent |
| **Left Temple Carrier Board (Power/Audio)** | ~18 mm width × 50–60 mm length | Houses IP2326 charger, HY2212 BMS, left MAX98357A amp, 1510 speaker connection | **MISSING** | `docs/plan.md` (L233–238); `docs/hardware_bom.md` (Item 23); no DXF file exists | PCB / MECH | Krishna / MCAD Agent |

### C.2 Layer Stack-Up & HDI Microvia Constraints

| Parameter | Rockchip HDG Recommendation | Project FRIDAY Implementation | Feasibility on JLCPCB | Evidence (HDG / JLCPCB) | Status |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **Layer Count** | 6-Layer or 8-Layer | 6-Layer HDI (or 8-Layer HDI) | Supported (6L/8L HDI 1+N+1 or 2+N+2) | HDG §3.1 p.169, Table 3-3 (p.171); JLCPCB HDI Capabilities | **PARTIAL** |
| **Stackup Order** | L1: TOP (Signal)<br>L2: GND (Reference)<br>L3: POWER (Power/Signal)<br>L4: Signal/POWER<br>L5: GND (Reference)<br>L6: BOTTOM (Signal) | L1: High-Speed Signals & Fanout<br>L2: Continuous Solid GND<br>L3: Power Planes (Core/DDR/Logic)<br>L4: High-Speed DDR Stripline<br>L5: Solid GND Return<br>L6: Power/Peripherals & Decaps | Requires JLCPCB controlled-impedance stackup profile [stackup name `JLC061611-3313` is UNVERIFIED (no source)] | HDG p.171 Table 3-3 | **PARTIAL** (Stackup profile not configured in Fusion) |
| **BGA Fanout & Via Type** | RK3576 mixed 0.55/0.60/0.65 mm; outer 2 rows 3.5 mil trace; inner rows require regular via channels | eMCP 254-ball has **0.50 mm pitch**, which typically requires laser-drilled microvias (via-in-pad / VIPPO) | JLCPCB supports laser microvias: 0.10 mm hole / 0.20 mm pad on 1+N+1 HDI [UNVERIFIED (no source)]. Mechanically drilled through-vias (0.2 mm hole / 0.4 mm pad) make 0.5 mm BGA fanout extremely difficult. | HDG §3.2 pp.171–174; eMCP Ball Map CSV | **LIKELY needs laser microvias — decide at stack-up review (check Sige5/CM5 stack-ups in references_local)** |
| **Trace / Spacing Minimum** | 3.5 mil (0.089 mm) fanout; 4.0 mil general | 3.5 mil / 3.5 mil neck-down in BGA field; 4.0 mil / 4.0 mil general | JLCPCB HDI capability allows 3.0 mil / 3.0 mil (0.075 mm) [UNVERIFIED (no source)] | HDG p.172, Figure 3-2 | **HAVE** (JLCPCB capability target) |

### C.3 High-Speed Routing & Impedance Rules (Rockchip HDG Citations)

| Bus / Interface | Impedance Requirement | Length / Skew Matching Limit | Max Trace Length | Via & Shielding Rules | HDG Citation | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| **LPDDR4X Bus** | 90 Ω ± 10% differential (CLK, DQS, WCLK); single-ended DQ/ADDR 40–50 Ω | • Intra-pair skew (DQS_P/N, CLK_P/N) **≤ 5 mil (0.127 mm)**<br>• DQ/DM to DQS/WCLK (same byte) **≤ 90 mil (2.286 mm)**<br>• Address/Control to CLK **≤ 90 mil**<br>• DQS/WCLK to CLK **≤ 230 mil** | Kept short (< 25 mm target on compute board) | Ground shield between byte lanes; airgap ≥ 2x trace width (3x for DQS/CLK); stripline on L4 preferred | HDG §3.5.3.2, Table 3-21 & Table 3-22 (p.237) | **SPECIFIED** (Ready for layout) |
| **MIPI CSI-2 Camera** | 100 Ω ± 10% differential (95 Ω fallback if stackup limits) | • Intra-pair skew **< 6 mil (0.15 mm)**<br>• Data to clock matching **< 12 mil (0.30 mm)** | < 6 inches (150 mm) | Max vias: ≤ 4; continuous ground reference; stitching vias within 30 mil of signal layer transitions | HDG §3.5.8, Table 3-30 (p.243), Figure 3-144 (p.244) | **SPECIFIED** (Ready for layout) |
| **USB 2.0 High-Speed** | 90 Ω ± 10% differential | Intra-pair skew **< 20 mil (0.50 mm)** | < 6 inches (150 mm) | Max vias: recommend ≤ 2, max 4; void reference plane under ESD diodes | HDG §3.5.6, Table 3-28 (p.242) | **SPECIFIED** (Ready for layout) |
| **USB 3.2 Gen1 (Future)** | 90 Ω ± 10% differential | Intra-pair skew **< 6 mil (0.15 mm)** | < 6 inches (150 mm) | AC caps 100 nF 0201; void reference plane under 0201 caps; max 2 vias | HDG §3.5.7, Table 3-29 (p.243) | **SPECIFIED** |
| **eMMC 5.1 Bus** | 50 Ω ± 10% single-ended | Data/CMD to CLK matching **< 120 mil (3.0 mm)** | < 3.5 inches (90 mm) | Stitching via within 30 mil of signal transition via; max vias ≤ 2 | HDG §3.5.11, Table 3-33 (p.244) | **SPECIFIED** (Ready for layout) |
| **SDIO 3.0 (Wi-Fi)** | 50 Ω ± 10% single-ended | Data/CMD to CLK mismatch **< 120 mil (3.0 mm)** | < 4 inches (100 mm) | Continuous GND reference; airgap ≥ 2x trace width | HDG §3.5.12, Table 3-34 (p.245) | **SPECIFIED** (Ready for layout) |

### C.4 Keep-Outs & Thermal Interface Constraints

| Feature / Keepout | Location | Physical Dimensions / Rule | Status | Evidence (File Path / Line) | Needed For |
| :--- | :--- | :--- | :---: | :--- | :---: |
| **RF Antenna Keep-Out** | Compute board edge around U.FL connector (`J12`) | Minimum 5.0 mm ground and copper keep-out around RF trace and antenna feed point | **MISSING** | HDG §3.5.25.5 (p.250); no PCB layout exists | PCB |
| **Camera Lens Aperture** | Front-bridge board center | Clear optical cone for 75° diagonal / 66° H / 41° V FOV IMX708 standard lens; zero copper or tall components within 3.0 mm of sensor aperture | **MISSING** | `docs/datasheets/Raspberry Pi Camera Module 3 Sensor Assembly.pdf`; `docs/plan.md` (L217) | PCB / MECH |
| **Hinge Flex Relief Bend** | Temple hinge pivot area | Internal filleted guide channel ($R \ge 3.0\text{ mm}$ bend radius) to prevent dynamic flex fatigue and copper shear | **MISSING** | `docs/plan.md` (L382); teardown engineering rules | PCB / MECH |
| **SoC Thermal Dissipation Pad**| Compute board top/bottom over RK3576 SoC | Direct contact area for 0.3 mm copper heat spreader + 4.0 g Rubitherm RT42 PCM packet (surface area $A \approx 20\text{ cm}^2$) | **MISSING** | `docs/plan.md` (L228, L330); `docs/hardware_bom.md` (Item 25) | PCB / MECH |
| **Connector Cutouts** | USB-C connector J1 on right temple | Enclosure cutout for Type-C plug shell (outer dims: ~9.0 x 3.5 mm) | **MISSING** | `docs/datasheets/C165948.pdf`; no CAD model exists | MECH |

---

## D. 3D Mechanical Models & Wearable Assembly

Audit of 3D CAD assets (STEP/IGES/STL), component physical heights, enclosure fitment, mass budget, and physical dimensions required for integration into the glasses frame.

### D.1 Component 3D STEP Model Availability

| Component / MPN | Package | Component Height (mm) | 3D STEP in Repo? | Sourcing Source for 3D Model | Status |
| :--- | :--- | :---: | :---: | :--- | :---: |
| **Rockchip RK3576** | FCCSP-698L (16.1 x 17.2 mm) | 1.40 mm [UNVERIFIED (no source)] | **NO** | Rockchip / Ultra Librarian / SnapEDA | **MISSING** |
| **Rockchip RK806S-5** | QFN-68-EP (7.0 x 7.0 mm) | 0.85 mm [UNVERIFIED (no source)] | **NO** | LCSC `C49174044` / EasyEDA STEP export | **MISSING** |
| **H9HP52ACPMADAR (eMCP)** | BGA-254 (11.5 x 13.0 mm) | **1.20 mm max (DS p.9)** | **NO** | SK hynix / JEDEC standard BGA-254 STEP | **MISSING** |
| **RTL8723DS-CG** | WQFN-48 (6.0 x 6.0 mm) | 0.85 mm [UNVERIFIED (no source)] | **YES** | `libraries/RTL8723DS/Fusion360/QFN48_RTL8723_RTK.step` | **HAVE** |
| **TPS2121RUXR** | WQFN-12 (2.0 x 2.5 mm) | 0.75 mm [UNVERIFIED (no source)] | **NO** | TI.com (CAD/CAE models for RUX package) | **MISSING** |
| **SY8205FCC** | TSOT-23-6 (2.9 x 1.6 mm) | 1.00 mm [UNVERIFIED (no source)] | **NO** | Silergy / LCSC `C111875` EasyEDA STEP | **MISSING** |
| **TMI3112H** | SOT-23-5 (2.9 x 1.6 mm) | 1.10 mm [UNVERIFIED (no source)] | **NO** | LCSC `C2985060` EasyEDA STEP | **MISSING** |
| **SY6280AAC** | SOT-23-5 (2.9 x 1.6 mm) | 1.10 mm [UNVERIFIED (no source)] | **NO** | LCSC `C28956` EasyEDA STEP | **MISSING** |
| **CW3301** | WLCSP-4 (0.8 x 0.8 mm) | 0.50 mm [UNVERIFIED (no source)] | **NO** | Cellwise / Manufacturer | **MISSING** |
| **IP2326 2S Charger** | QFN-24 (4.0 x 4.0 mm) | 0.75 mm [UNVERIFIED (no source)] | **NO** | Injoinic / LCSC EasyEDA STEP | **MISSING** |
| **HY2212 / HY2120 BMS** | SOT-23-6 | 1.10 mm [UNVERIFIED (no source)] | **NO** | Hycon / LCSC EasyEDA STEP | **MISSING** |
| **IMX708 SA31VA30P Module** | Custom camera cube | 5.80 mm [UNVERIFIED (no source)] | **NO** | Raspberry Pi / Arducam 3D STEP | **MISSING** |
| **DF37NC-30DS-0.4V** | 30-pin B2B connector | 0.98 mm (mated) [UNVERIFIED (no source)] | **NO** | Hirose Electric CAD portal | **MISSING** |
| **FH12-10S-0.5SH** | 10-pin 0.5 mm FPC | 2.00 mm [UNVERIFIED (no source)] | **NO** | Hirose Electric CAD portal | **MISSING** |
| **FH12-24S-0.5SH** | 24-pin 0.5 mm FPC | 2.00 mm [UNVERIFIED (no source)] | **NO** | Hirose Electric CAD portal | **MISSING** |
| **INMP441 MEMS Mic** | LGA-4.72x3.76 | 1.00 mm [UNVERIFIED (no source)] | **NO** | TDK InvenSense CAD / SnapEDA | **MISSING** |
| **MAX98357AETE+T** | TQFN-16-EP (3.0 x 3.0 mm) | 0.75 mm [UNVERIFIED (no source)] | **NO** | Analog Devices / Maxim CAD | **MISSING** |
| **1510 Oval Speaker** | Dynamic box (15 x 10 mm) | 3.50 mm [UNVERIFIED (no source)] | **NO** | Probots / CUI Devices / GrabCAD | **MISSING** |
| **GNB 300mAh LiPo Cell** | Pouch cell (35 x 12 mm) | 6.00 mm [UNVERIFIED (no source)] | **NO** | Manufacturer dimensions / manual CAD model | **MISSING** |
| **X322524MOB4SI (24MHz)** | SMD-3225-4P | 0.80 mm [UNVERIFIED (no source)] | **YES** | `libraries/X322524MSB4SI/Fusion360/X322524MSB4SI_YXC.step` | **HAVE** |
| **C1E-26.000-6-3030-R (26MHz)**| SMD-3030-4P | 0.80 mm [UNVERIFIED (no source)] | **NO** | Taitien / LCSC EasyEDA | **MISSING** |
| **TYPE-C-31-M-12** | 16-pin USB-C receptacle | **3.26 mm [UNVERIFIED (no source)]** | **NO** | LCSC `C165948` / Korean Hroparts CAD | **MISSING** |
| **TS-1187A-B-A-B** | 3 x 4 mm tactile button | 1.50 mm [UNVERIFIED (no source)] | **NO** | LCSC `C318884` EasyEDA STEP | **MISSING** |
| **U.FL-R-SMT-1** | Ultra-miniature RF jack | 1.25 mm [UNVERIFIED (no source)] | **NO** | Hirose Electric CAD portal | **MISSING** |
| **USBLC6-2SC6** | SOT-23-6 | 1.10 mm [UNVERIFIED (no source)] | **NO** | STMicroelectronics / SnapEDA | **MISSING** |
| **Power Inductors (4040)** | SMD 4.0 x 4.0 mm | **2.80 mm [UNVERIFIED (no source)]** | **NO** | Murata / TDK / Sunlord EasyEDA | **MISSING** |
| **Power Inductors (2016)** | SMD 2.0 x 1.6 mm | 1.00 mm [UNVERIFIED (no source)] | **NO** | Murata / Sunlord EasyEDA | **MISSING** |

### D.2 Physical Dimensions & Tallest Components per Board

| Board Assembly | Tallest Component | Max Height Above Board | Enclosure Internal Clearance Needed | Status |
| :--- | :--- | :---: | :---: | :---: |
| **Compute Board (Right Temple)** | USB Type-C Receptacle (`TYPE-C-31-M-12`) | **3.26 mm [UNVERIFIED (no source)]** | Minimum 5.0 mm internal cavity depth (3.5mm component + 0.8mm PCB + 0.7mm thermal/clearance) | **CRITICAL CONSTRAINT** |
| **Front-Bridge Board (Center Frame)** | IMX708 Autofocus Lens Barrel | **5.80 mm [UNVERIFIED (no source)]** | Minimum 7.5 mm nose-bridge protrusion / thickness | **CRITICAL CONSTRAINT** |
| **Left Temple Board (Power/Audio)** | 1510 Micro Dynamic Speaker / Battery | **3.50 mm (Speaker) / 6.00 mm (LiPo) [UNVERIFIED (no source)]** | Minimum 7.0–8.0 mm internal temple cavity thickness | **CRITICAL CONSTRAINT** |

### D.3 Glasses Frame CAD & Ergonomic Assembly Status

| Mechanical Feature | Target Specification | Current Status in Repo | Evidence (File Path / Line) | Who Can Supply |
| :--- | :--- | :---: | :--- | :--- |
| **Glasses Frame 3D CAD** | Full 3D assembly (`.step` / `.f3d`): front eyewire, nasal bridge, left/right thick temples | **MISSING** | No frame STEP/STL/F3D found anywhere in repository | Krishna / Fusion 360 MCAD Agent |
| **Temple Cavity Dimensions** | Width: 22 mm, Depth: ≥ 6.5 mm, Length: ≥ 85 mm (housing 75mm PCB + battery) | **MISSING** | `docs/plan.md` L411 (conceptual description only) | Krishna / MCAD Agent |
| **Center Bridge Cavity** | Width: 18–20 mm, Height: 15 mm, Depth: 8 mm (housing IMX708 + front-bridge PCB) | **MISSING** | `docs/plan.md` L217 (conceptual description only) | Krishna / MCAD Agent |
| **Hinge Mechanism & Flex Channels** | Filleted internal conduit ($R \ge 3.0\text{ mm}$) to route FFC across hinge without pinching | **MISSING** | `docs/plan.md` L382; no mechanical drawings | Krishna / MCAD Agent |
| **Battery Pouch Dimensions** | GNB 300mAh 1S LiPo (35.0 mm length × 12.0 mm width × 6.0 mm thickness, 8.0 g each) | **MISSING** (Vendor specs only) | `docs/hardware_bom.md` Item 17; unmeasured on physical cell | Krishna (buy & measure sample) |
| **1510 Box Speaker Dimensions** | 15.0 mm × 10.0 mm × 3.5 mm oval enclosure; downward acoustic exit port | **MISSING** (Vendor specs only) | `docs/hardware_bom.md` Item 16; physical chamber unmodeled | Krishna (buy & measure sample) |
| **Camera Sensor Flex Length** | Raspberry Pi Camera Module 3 / SA31VA30P integrated FPC length (~15–20 mm) | **MISSING** | `docs/datasheets/Raspberry Pi Camera Module 3 Sensor Assembly.pdf` | Krishna (measure physical module) |
| **Through-Bridge FFC Length** | Flex jumper length from Right Temple compute board to Left Temple carrier board (~110–130 mm) | **MISSING** | Estimated from standard 140–145 mm total frame temple-to-temple width | Krishna / MCAD Agent |

### D.4 Mass Budget Audit vs. Wearable Ceilings (Plan1 D13: 120.0 g / Plan.md Directive 05: 125.0 g)

> [!NOTE]
> **ESTIMATE, unmeasured, written for the SoM design — must be redone for the custom board.**  
> The mass budget below is quoted as-is from `docs/plan.md` §3 (L209–241). It establishes a baseline of **115.0 g** (109.5 g physical components + 5.5 g contingency) against the project ceilings:
> - **Plan1 D13:** 120.0 g hard limit
> - **Plan.md Directive 05:** 125.0 g maximum wearable limit

| Subassembly Component | Location | Unit Mass (g) | Subtotal Mass (g) | % of Total Mass |
| :--- | :--- | :--- | :--- | :--- |
| **Front Frame (Nylon PA12, 0.9mm walls)** | Nose/Bridge/Rims | 12.0 | 12.0 | 10.43% |
| **High-Index 1.67 Thin Lenses** | Eyewire sockets | 8.5 (pair) | 8.5 | 7.39% |
| **Titanium Camera Skeleton & IMX415 Lens**| Center bridge | 3.0 | 3.0 | 2.61% |
| **Dual MEMS Microphones (Star-GND)** | Front-right rim | 0.8 | 0.8 | 0.70% |
| **Spring Hinges & Brass Thread Inserts** | Left & Right temples | 3.0 (pair) | 3.0 | 2.61% |
| **Silicone Nose Pads, Brackets & Fasteners**| Bridge & Frame | 1.8 | 1.8 | 1.57% |
| **Continuous Rigid-Flex Hinge Bridges** | Both hinges | 2.2 | 2.2 | 1.91% |
| **Right Temple Chassis (Lightened PA12)**| Right ear | 7.2 | 7.2 | 6.26% |
| **Compute Core SoM (Rockchip RK3576)** | Right temple | 11.8 | 11.8 | 10.26% |
| **Right Carrier PCB + 2S Buck-Boost** | Right temple | 1.9 | 1.9 | 1.65% |
| **Wi-Fi / BT 5.2 Murata 1XK Combo SiP** | Right temple (on SoM) | 0.8 | 0.8 | 0.70% |
| **Cell 2 LiPo (Series 2S, 3.7V 300mAh)** | Right temple | 11.5 | 11.5 | 10.00% |
| **Right Protection Board, NTC & Balance** | Right temple | 1.2 | 1.2 | 1.04% |
| **Thermal Assembly: 4.0g PCM + 1.5g Al** | Right temple exterior | 5.5 | 5.5 | 4.78% |
| **Ambiq Apollo4 Lite Coprocessor & Mux** | Right temple | 1.1 | 1.1 | 0.96% |
| **Capacitive Touch Ribbon & Hall Switch** | Right temple outer | 0.7 | 0.7 | 0.61% |
| **MAX98357A Right Amp & Speaker Driver** | Right temple | 3.0 | 3.0 | 2.61% |
| **Left Temple Chassis (Lightened PA12)** | Left ear | 7.2 | 7.2 | 6.26% |
| **Cell 1 LiPo (Series 2S, 3.7V 300mAh)** | Left temple | 11.5 | 11.5 | 10.00% |
| **TI BQ25887 2S Charger & Power Rails** | Left temple | 3.7 | 3.7 | 3.22% |
| **TI BQ28Z610 2S Protector & Balance Tap**| Left temple | 1.2 | 1.2 | 1.04% |
| **Auxiliary 5V-to-1.8V LDO Board**| Left temple | 0.8 | 0.8 | 0.70% |
| **MAX98357A Left Amp & Speaker Driver** | Left temple | 4.8 | 4.8 | 4.17% |
| **Magnetic Pogo Charging Port (5V/3A)** | Left temple tip | 1.4 | 1.4 | 1.22% |
| **Solder Paste, Potting & Shielding Cans** | Distributed | 2.9 | 2.9 | 2.52% |
| **Contingency Margin (+4.78%)** | Distributed | 5.5 | 5.5 | 4.78% |
| **TOTAL ALL-UP MASS (AUW)** | **System Complete** | — | **115.0 grams** | **100.00%** |

$$\text{Subassembly Rollup: } 31.3\text{g (Front)} + 30.6\text{g (Left)} + 44.7\text{g (Right)} + 2.9\text{g (Shielding)} + 5.5\text{g (Contingency)} = \mathbf{115.0\text{ grams}}.$$

**Rows that change with the custom board implementation:**
1. **Compute Core SoM (11.8 g):** Replaced by the custom 6L/8L HDI compute PCB (RK3576 SoC + eMCP + RK806S-5 PMIC + TMI3112H bucks + passives).
2. **Right Carrier PCB + 2S Buck-Boost (1.9 g):** Merged into the custom compute board power input section (SY8205FCC + TPS2121).
3. **Wi-Fi / BT 5.2 Murata 1XK Combo SiP (0.8 g):** Replaced by discrete on-board RTL8723DS-CG + 26 MHz crystal + U.FL antenna circuitry.
4. **Left Temple Charger & BMS Boards (TI BQ25887 3.7 g, BQ28Z610 1.2 g, Aux LDO 0.8 g):** Replaced by custom Left Temple carrier board with Injoinic IP2326 boost charger + HY2212/HY2120 BMS circuitry.
5. **Titanium Camera Skeleton & IMX415 Lens (3.0 g):** Replaced by Sony IMX708 SA31VA30P module + custom front-bridge PCB (with local 1.1 V buck, 1.8 V / 2.8 V LDOs, and DF37 connector).
6. **Ambiq Apollo4 Lite Coprocessor & Mux (1.1 g):** Omitted / deferred; RK3576 PMU + internal PVTM handles sleep states directly.

### D.5 Physical Measurement & Procurement Checklist for Krishna

The following physical items must be procured or measured with digital calipers by Krishna to unblock MCAD enclosure design and 3D clash detection:
1. **Donor eMCP Physical Dimensions:** Measure exact package length, width, and seated thickness with solder balls using calipers (nominal 11.5 x 13.0 x 1.2 mm max per DS p.9).
2. **Raspberry Pi Camera Module 3 / SA31VA30P:** Measure exact sensor cube dimensions (10.8 x 10.8 mm), lens protrusion at infinity focus vs closest macro focus, and FPC flex tail length and bend radius.
3. **GNB 300mAh LiPo Cells:** Weigh both individual cells on a 0.01 g jewelry scale; measure length, width, and thickness at full 4.2V charge (pouch expansion).
4. **1510 Oval Speakers:** Measure outer plastic casing dimensions, acoustic exit slot position, and terminal solder pad locations.
5. **Personal Eyewear Lenses:** Trace lens perimeter profile (eyewire bevel curve) using a contour gauge or flatbed scanner (1200 DPI) to model matching 3D printed eyewire frames.
6. **User Head Ergonomics:** Measure interpupillary distance (IPD), temple-to-ear length (~100–105 mm), and head width at temporal bone (~140–148 mm) to set temple inward spring tension and hinge stops.

---

## E. Ranked Vital Missing Items

Ranked list of the critical missing hardware items across schematics, component libraries, 2D layout, and 3D mechanicals. Each item specifies the exact next action, responsible agent/person, and schematic change risk.

| Rank | Vital Missing Item | Domain | Severity & Schematic Risk | Single Next Action | Responsible Owner | Target Milestone Unblocked |
| :---: | :--- | :---: | :---: | :--- | :---: | :--- |
| **1** | **eMCP 254-Ball Symbol & Footprint Library** | ECAD Lib | **HIGH** (Schematic blocker) | Generate `libraries/eMCP_BGA254.lbr` from `hardware/compute_board/emcp_ballmap_source.csv` with standard 0.5mm JEDEC land pattern and dual-channel LPDDR4X + eMMC symbols. | **Astra / Sol** | SCH-2 eMCP Schematic Capture |
| **2** | **SCH-2 Carry-In Electrical Net Connections (Y1–Y4)** | Schematic | **HIGH** (Schematic change) | In SCH-2, wire: Y1 (USB3/DP REXT 8.2k resistor R1400), Y2 (BUCK9 rail `VDD2_DDR_S3` and CKE retention branch), Y3 (power INMP441 from 1.8V rail to match SAI1 bank), Y4 (eMMC-side passives per eMCP DS p.54 Table 14: VCCQ 2x2.2 µF, VCC 2x4.7 µF, VDDi 0.1 µF, CMD 10k pull-up, DAT0–7 50k pull-ups, RSTn 50k pull-up optional, DS no resistor, CLK 27 Ω series R). | **Astra (high)** | SCH-2 Capture & ERC Verification |
| **3** | **eMCP Qualification on RK3576 Memory Support List (QVL)** | Firmware / HW | **HIGH** (Boot blocker) | Check H9HP52ACPMADAR part number against official Rockchip RK3576 DDR/eMMC loader support list; verify supported frequencies and channel configurations. | **Researcher / Krishna** | SCH-2 Part Sourcing & Boot Sign-off |
| **4** | **Camera Bridge Board Schematic: Chokes, POR & Regulators** | Schematic | **HIGH** (Entire circuit missing) | Design front-bridge schematic per Raspberry Pi Camera Module 3 ref `RP-008969-SD`: add MIPI CSI common-mode filter chokes, POR supervisor holding XCLR low until MCLK stabilizes, local 1.1V buck, 1.8V/2.8V LDOs, and DF37 connector. | **Sol / Astra** | SCH-3 Camera & Front-Bridge Capture |
| **5** | **IMX708 Linux Kernel Driver & ISP Support Verification** | SW / Bring-Up | **HIGH** (Ordering gate) | Verify IMX708 driver and Rockchip ISP tuning status on RK3576 kernel tree; gate hardware order until sensor initialization on RK3576 is proven. | **Researcher / Krishna** | Front-Bridge Board Fab Order Gate |
| **6** | **Left Temple Power Carrier Schematic (IP2326 + HY2212 BMS)** | Schematic | **HIGH** (Entire circuit missing) | Design standalone schematic for Left Temple carrier board: IP2326 Type-C 2S boost charger (ISET=300k for 300mA charge limit [UNVERIFIED (no source)]), HY2212 35mA shunt balancing, HY2120 2S protection FETs, NTC sensing. | **Hydrogen / Sol** | Left Temple Schematic & Battery Safety |
| **7** | **RK806S-5 Dedicated OTP / Variant Document Acquisition** | Docs / SCH | **HIGH** (Voltage sign-off) | Obtain dedicated Rockchip RK806S-5 OTP documentation (current repo has only generic RK806 DS Rev 1.3) to verify power-on voltage defaults and sequence registers. | **Researcher / Krishna** | PMIC Voltage Verification |
| **8** | **FPC Interconnect Pinout Definition (FH12-10 & FH12-24)** | System / Interconnect | **HIGH** (Forces schematic changes on all boards) | Formulate and document exact pinouts for FH12-10S (Right temple to bridge) and FH12-24S (Left temple to bridge / front-bridge): allocate 2S battery power lines, I2S audio, I2C camera/sensor, MIPI CSI differential pairs. | **Researcher / Krishna** | Inter-Board Schematic Interconnect |
| **9** | **Wi-Fi / BT Antenna Part Sourcing & BOM Inclusion** | Sourcing / BOM | **MED** (RF path incomplete) | Select and specify exact physical antenna part (ceramic chip antenna or custom internal FPC) for 2.4 GHz 802.11b/g/n + BT 4.2; current BOM lists only U.FL receptacle (J12/J5). | **Krishna / Researcher** | SCH-4 Wireless BOM & RF Layout |
| **10** | **Audio Subsystem Schematic (INMP441 + MAX98357A)** | Schematic | **MED** (Peripheral sheet) | Capture SCH-4 audio sheet: dual INMP441 MEMS mics (powered from 1.8V rail per Y3 to match SAI1 bank) and dual MAX98357A I2S mono amps (powered from `VCC5V0_SYS_S5`, SD_MODE configured for Left/Right channel separation). | **Sol / Hydrogen** | SCH-4 Audio / Peripheral Capture |
| **11** | **Wi-Fi / Bluetooth Schematic (RTL8723DS Subsystem)** | Schematic | **MED** (Peripheral sheet) | Capture SCH-4 wireless sheet: RTL8723DS-CG, 26MHz crystal Y1, U.FL RF receptacle J12, 50Ω pi-filter matching network, SDIO 3.0 lines connected to RK3576 VCCIO3 bank via series termination. | **Sol / Hydrogen** | SCH-4 Wireless Capture |
| **12** | **RK3576 FCCSP-698L Footprint Ball-by-Ball Verification** | ECAD Lib | **HIGH** (Fab blocker; board scrap risk) | Audit every pad coordinate and pitch transition (0.55/0.60/0.65 mm) in `libraries/RK3576.lbr` against Rockchip RK3576 Datasheet Rev 1.5 §2 package drawing (p.24); mark verified. | **Sol / Researcher** | Compute Board PCB Layout |
| **13** | **6-Layer / 8-Layer HDI PCB Stack-Up Profile Configuration** | PCB Layout | **HIGH** (Routing blocker) | Configure exact HDI layer stackup in Autodesk Fusion Electronics matching JLCPCB 1+N+1 laser microvia rules (0.1mm laser via, via-in-pad VIPPO on L1-L2, 0.089mm min trace/space, 90Ω diff / 50Ω SE impedance). | **Sol / Krishna** | 2D PCB Routing Initialization |
| **14** | **Glasses Frame Parametric 3D CAD Assembly** | MCAD | **MED** (Enclosure blocker) | Generate initial 3D assembly model (`.step` / `.f3d`) for Track 1 thick-temple smart glasses in Fusion 360: define temple cavity (22x75 mm), front bridge housing (IMX708 aperture), and filleted hinge guide conduits ($R \ge 3.0\text{ mm}$). | **Krishna / MCAD Agent** | 3D Mechanical Clash Detection |
| **15** | **Compute Board Mechanical Outline & Mounting DXF** | PCB / MCAD | **MED** (Board shape blocker) | Export board outline DXF from glasses temple CAD with exact 20–22 mm × 75 mm profile, contour taper, M1.6 mounting bosses, and connector edge cutouts (Type-C J1, FPC connectors). | **Krishna / MCAD Agent** | Compute Board PCB Outline Import |
| **16** | **RK806-1.lbr MPN & Attribute Correction** | ECAD Lib | **LOW** (BOM consistency) | Edit `libraries/RK806-1.lbr` to update device attribute `MPN` from `RK806-1` to `RK806S-5` and verify all feedback pins (VOUT1–10) are marked passive to prevent false ERC power conflict warnings. | **Hydrogen** | Clean BOM Export & ERC Verification |
| **17** | **Missing Component 3D STEP Models Aggregation** | 3D / MCAD | **LOW** (Visual clash detection) | Download manufacturer 3D STEP models for critical tall components: Type-C J1 (`C165948`), 4040 inductors, DF37 connector, FH12 connectors, TS-1187 switch, and attach them to library footprints. | **Researcher / Krishna** | 3D Board Rendering in Fusion |
| **18** | **Hardware Status LEDs & Test Points Schematic Addition** | Schematic | **LOW** (Bring-up debug) | Add standard 0402 diagnostic LEDs (VBUS detect, 5V0_SYS active, PMIC power good) and 1.0mm test pads for primary power rails (`VCC5V0_SYS`, `VBAT`, `VDD_LOGIC`, `VDD_DDR`) to compute schematic. | **Hydrogen** | Board Bring-Up & Diagnostics |
| **19** | **Physical Measurement of Wearable Hardware Samples** | Mechanical | **MED** (Packaging verification) | Purchase and measure physical samples with digital calipers: GNB 300mAh LiPo cells, 1510 oval speakers, IMX708 camera module, personal eyewear lens profile, and user temple/head dimensions. | **Krishna** | Final DFM & Enclosure 3D Print |

---

## F. Audit Summary & Immediate Next Engineering Action

1. **Schematic Capture Status:**
   - **SCH-1 is COMPLETE & ACCEPTED:** Captured @ 1617157, fixed and accepted @ `d9d37a8` (commit `3262024` was reported locally by Hydrogen but never pushed to origin). Power path, PMIC, bucks, and SoC core power/clocks/reset/boot are fully captured (5 sheets, 104 nets, 0 ERC errors).
   - **SCH-2 (eMCP LPDDR4X + eMMC) is READY TO EXECUTE** once the 254-ball library (Rank 1) is generated and carry-ins Y1–Y4 (Rank 2) are applied.
   - **SCH-3 (Camera & Bridge) and SCH-4 (Wireless, Audio & Power)** require library creation, front-bridge chokes/POR definition, and inter-temple FPC pinout definition.

2. **PCB Layout Readiness:**
   - **Stackup Review Prerequisite:** 0.50 mm pitch eMCP BGA LIKELY needs laser microvias (via-in-pad) — decide at stack-up review (check Sige5/CM5 stack-ups in references_local). JLCPCB 1+N+1 HDI stackup must be defined in Fusion before starting routing.
   - **BLOCKED on Board Outline DXF:** Mechanical contours for the 20–22 mm × 75 mm temple board must be imported from frame CAD.

3. **3D / Mechanical Readiness:**
   - **BLOCKED on Glasses Frame CAD:** Zero frame 3D geometry exists in the repository. Parametric modeling of the temple cavities, bridge aperture, and hinge conduits in Fusion 360 is required for packaging and clash detection.
   - **Mass Budget Baseline:** The 115.0 g mass budget is an unmeasured estimate written for the SoM baseline from `docs/plan.md` §3, and must be redone for the custom board against Plan1 D13 (120.0 g hard limit) and `plan.md` Directive 05 (125.0 g).

**IMMEDIATE NEXT DIRECTIVE:**  
Task **Astra (high)** or **Sol** to generate `libraries/eMCP_BGA254.lbr` from `hardware/compute_board/emcp_ballmap_source.csv`, then initiate **Round SCH-2** schematic capture in Fusion Electronics.
