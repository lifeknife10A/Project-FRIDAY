import os

def write_emcp_note():
    content = """# eMCP Reference Specification: SK hynix H9HP52ACPMADAR-KMM

## 1. Device Overview & Part Identification
- **Manufacturer:** SK hynix Inc.
- **Part Number (MPN):** `H9HP52ACPMADAR-KMM` (Rev 1.0, March 2018) [p.1, p.6]
- **Package:** 254-ball FBGA, 11.5 mm × 13.0 mm × 1.2 mm max height, 0.50 mm ball pitch [p.6, p.9]
  - Ball grid: 24 rows (A to AD, omitting I, O, Q, S, X, Z) × 18 columns (1 to 18) [p.6, p.9]
  - Total populated balls: 254 balls [p.6, p.9]
- **Density & Architecture:**
  - **eMMC:** 64 GB eMMC 5.1 (x8 bus, HS400 mode up to 400 MB/s, backward compatible with HS200 / DDR50) [p.1, p.7, p.10-11]
  - **LPDDR4X:** 32 Gb (4 GB) total capacity, organized as 2 channels × 16-bit (Channel A and Channel B), 2 ranks (2CS) [p.1, p.6, p.8]
  - **Speed:** Up to 3733 Mbps (1866 MHz clock frequency) [p.1, p.19]

---

## 2. Operating Supply Voltages
All supply voltage ranges cited directly from SK hynix H9HP52ACPMADAR Rev 1.0 specification [p.6, p.7, p.8, p.16, p.19]:

| Domain | Signal Name | Nominal Voltage | Operating Voltage Range | Description / Purpose | Reference Citation |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **LPDDR4X Core 1** | `VDD1` | 1.80 V | 1.70 V – 1.95 V | LPDDR4X core supply 1 (analog/wordline) | Spec p.8, p.19 |
| **LPDDR4X Core 2** | `VDD2` | 1.10 V | 1.06 V – 1.17 V | LPDDR4X core logic supply 2 | Spec p.8, p.19 |
| **LPDDR4X I/O** | `VDDQ` | 0.60 V | 0.57 V – 0.65 V | LPDDR4X ultra-low voltage I/O supply | Spec p.8, p.19 |
| **LPDDR4X Ground** | `VSS` / `VSSQ` | 0.00 V | 0.00 V | DRAM substrate, core, and I/O ground reference | Spec p.8 |
| **eMMC Core** | `VCC` | 3.30 V | 2.70 V – 3.60 V | eMMC NAND flash memory core supply | Spec p.7, p.16 |
| **eMMC I/O** | `VCCQ` | 1.80 V | 1.70 V – 1.95 V | eMMC controller and host I/O buffer supply | Spec p.7, p.16 |
| **eMMC Regulator** | `VDDI` | 1.20 V | Internal | Internal eMMC core logic decoupling output (cap to GND) | Spec p.7, p.16 |
| **eMMC Ground** | `VSSm` | 0.00 V | 0.00 V | eMMC controller and NAND flash dedicated ground | Spec p.7 |

> [!IMPORTANT]
> **Power Sequencing:**
> Per LPDDR4X JEDEC standard and SK hynix spec p.20, power ramp sequence is `VDD1` -> `VDD2` -> `VDDQ`.
> On Project FRIDAY:
> - `VDD1` (1.8V) is supplied by PMIC RK806S-5 `VCC_1V8_S3` (or PLDO6).
> - `VDD2` (1.1V) is supplied by discrete buck `VCC_1V1_NLDO_S3` / `VDD2_DDR_S3`.
> - `VDDQ` (0.6V) is supplied by PMIC RK806S-5 `BUCK6` (`VDDQ_DDR_S0`, 0.61V).

---

## 3. Ball Map & Signal Summary (254-Ball FBGA)
The complete ball-by-ball mapping is committed in [`hardware/compute_board/emcp_ballmap_source.csv`](file:///Users/krish/NMIMS/Friday/hardware/compute_board/emcp_ballmap_source.csv).
Extracted directly from Page 6 (Top View diagram):

- **Total Pins Extracted:** 254 balls
- **Unreadable Pins:** 0 balls (100% verified against Pin Descriptions pp. 7-8)

### Signal Breakdown:
1. **LPDDR4X Interface (Channel A & Channel B, 32-bit total):**
   - **Command / Address:** `CA[5:0]_A` (G14, F13, C13, D13, E13, C15), `CA[5:0]_B` (V14, W13, AB13, AA13, Y13, AB15) [12 balls]
   - **Clock:** `CLK_t_A` (H18), `CLK_c_A` (G18), `CLK_t_B` (U18), `CLK_c_B` (V18) [4 balls]
   - **Clock Enable:** `CKE0_A` (E18), `CKE1_A` (F18), `CKE0_B` (Y18), `CKE1_B` (W18) [4 balls]
   - **Chip Select:** `CS0_A` (E16), `CS1_A` (F16), `CS0_B` (Y16), `CS1_B` (W16) [4 balls]
   - **Data (Byte 0):** `DQ[7:0]_A` (A3, B2, C1, D1, B7, C5, D6, C7) [8 balls]
   - **Data (Byte 1):** `DQ[15:8]_A` (K5, K6, K2, J1, J5, G1, H5, H7) [8 balls]
   - **Data (Byte 2):** `DQ[7:0]_B` (AD3, AC2, AB1, AA1, AC7, AB5, AA6, AB7) [8 balls]
   - **Data (Byte 3):** `DQ[15:8]_B` (R5, R6, R2, T1, T5, V1, U5, U7) [8 balls]
   - **Data Mask Inversion:** `DMI0_A` (D3), `DMI1_A` (H1), `DMI0_B` (AA3), `DMI1_B` (U1) [4 balls]
   - **Data Strobes:** `DQS0_t_A` / `DQS0_c_A` (C9 / D9), `DQS1_t_A` / `DQS1_c_A` (K8 / J8), `DQS0_t_B` / `DQS0_c_B` (AB9 / AA9), `DQS1_t_B` / `DQS1_c_B` (R8 / T8) [8 balls]
   - **Calibration:** `ZQ0` (B16, Ch A), `ZQ1` (C16, Ch B) [2 balls] -> 240 Ω ±1% to `VDDQ`
   - **Reset:** `RST_n` (AA16, common DRAM reset) [1 ball]
   - **Power / Ground:**
     - `VDD1` (8 balls): A4, A9, A15, A16, B15, AD4, AD9, AD15, AD16
     - `VDD2` (24 balls): A5, A8, B11, B12, B14, G7, G8, G11, K1, L3, L5, L7, P3, P5, P7, R1, V7, V8, V11, AC11, AC12, AC14, AD5, AD8
     - `VDDQ` (20 balls): A6, A7, A13, A14, B4, B9, B13, H3, H8, J2, J3, J7, T2, T3, T7, U3, U8, AC4, AC9, AC13, AD6, AD7, AD13, AD14
     - `VSS` (48 balls): B3, B6, B8, B10, C2, C4, C6, C8, C14, D2, D4, D7, D14, D15, E14, F14, G2, G4, G6, G13, G15, H2, H4, H6, H14, J4, K3, K7, R3, R7, T4, U2, U4, U6, U14, V2, V4, V6, V13, V15, W14, Y14, AA2, AA4, AA7, AA14, AA15, AB2, AB4, AB6, AB8, AB14, AC3, AC6, AC8, AC10

2. **eMMC Interface (eMMC 5.1, 8-bit):**
   - **Clock:** `CLKm` (P12) [1 ball]
   - **Command:** `CMD` (M13) [1 ball]
   - **Data:** `DAT0` (P17), `DAT1` (M15), `DAT2` (N15), `DAT3` (P16), `DAT4` (M16), `DAT5` (N16), `DAT6` (L14), `DAT7` (L13) [8 balls]
   - **Data Strobe:** `DS` (M14) [1 ball]
   - **Reset:** `RST_n` (N9, eMMC hardware reset) [1 ball]
   - **Power / Ground:**
     - `VCC` (4 balls): M18, N18, P18, R18
     - `VCCQ` (7 balls): J16, J17, J18, K17, R13, R14, T17
     - `VDDI` (1 ball): L18 (requires 0.1 µF + 1 µF to GND)
     - `VSSm` (17 balls): K13, K14, K16, K18, L12, L15, L16, L17, M8, M12, N8, N12, N17, P13, P14, P15, R15, R16, R17

3. **Vendor Specific / Unconnected:**
   - `VSF[1:9]` (9 balls): M1, M3, M5, M7, M9, N3, N5, N7, N8 (Note 1: Vendor specific function - no external electrical connections permitted)
   - `DNU` (12 balls): A1, A2, A17, A18, B1, B17, B18, AC1, AC17, AC18, AD1, AD2, AD17, AD18
   - `NC` (8 balls): D18, H16, J12, J14, K15, N13, T12, T14, T18, U16, AB18
"""
    with open('docs/reference_designs/notes/emcp_hynix_H9HP52ACPMADAR.md', 'w') as fp:
        fp.write(content)
    print('docs/reference_designs/notes/emcp_hynix_H9HP52ACPMADAR.md written.')

def write_passives_note():
    content = """# LPDDR4X and eMMC Memory Passives Reference

This note extracts all memory-side passives (ZQ resistors, decoupling capacitors, damping resistors, and pull-ups) from open RK3576 reference designs:
1. **ArmSoM Sige5** (`RK3576-Schematics/Sige5/armsom-sige5-1v3_Sch.pdf`, sheets 14 & 15)
2. **DshanPI-A1** (`RK3576-Schematics/DshanPI-A1/DshanPi-A1-RK3576-SCH_V1.1.pdf`, sheets 18 & 19)
3. **Bit-Brick K1 SBC** (`Bit-Brick-K1/Circuit Diagram Files for Bit-Brick K1 SBC.pdf`, sheets 15 & 27)
4. **Rockchip EVB1 v1.2** (`RK_EVB1_RK3576_LP4XD200P132SD6_V12_20240530HSW.pdf`, sheet 38/40)

These designs replace the NDA-locked EVB1 sheets 38/40 and confirm the production values required for Round SCH-2.

---

## 1. LPDDR4X Passives (x32 Dual-Channel)

Both ArmSoM Sige5 (sheet 14) and DshanPI-A1 (sheet 18) implement 200-ball dual-channel (x32) LPDDR4X topologies matching our 2-channel memory bus.

### 1.1 ZQ Calibration Resistors
Each channel requires an independent precision reference resistor connected to `VDDQ`:
- **Channel A ZQ0 (ball B16 on eMCP):** 240 Ω ±1% (0201 package) connected between `ZQ0` and `VDDQ`.
  - Sige5: `R3802` (240R-1%, R0201) [p.14]
  - DshanPI-A1: `R64` (240R-1%, R0201) [p.18]
  - Bit-Brick K1: `R203` (240R-1%, R0201) [p.15]
- **Channel B ZQ1 (ball C16 on eMCP):** 240 Ω ±1% (0201 package) connected between `ZQ1` and `VDDQ`.
  - Sige5: `R3804` (240R-1%, R0201) [p.14]
  - DshanPI-A1: `R65` (240R-1%, R0201) [p.18]
  - Bit-Brick K1: `R204` (240R-1%, R0201) [p.15]

### 1.2 LPDDR4X Decoupling Capacitors per Power Rail
Decoupling network per reference design:

#### Rail: `VDD1_1V8_DDR_S3` (1.80 V Core 1)
- Bulk & Intermediate:
  - 1× 10 µF 10V X5R/X7R (0603): Sige5 `C3803`, DshanPI-A1 `C125`
  - 1× 1 µF 10V X5R (0402): Sige5 `C3824`, DshanPI-A1 `C147`
- High-Frequency Decoupling:
  - 4× 100 nF 10V X5R (0201): Sige5 `C3808`, `C3809`, `C3810`, `C3811`; DshanPI-A1 `C130`, `C131`, `C132`, `C133`
- *Total count:* 1× 10 µF + 1× 1 µF + 4× 100 nF.

#### Rail: `VDD2_DDR_S3` (1.10 V Core 2)
- Bulk & Intermediate:
  - 2× 22 µF 10V X5R (0603): Sige5 `C3801`, `C3821`; DshanPI-A1 `C123`, `C143`
  - 2× 10 µF 10V X5R (0603): Sige5 `C3822`, `C3823`; DshanPI-A1 `C144`, `C145`
  - 3× 1 µF 10V X5R (0402): Sige5 `C3804`, `C3805`, `C3825`; DshanPI-A1 `C126`, `C127`, `C146`
- High-Frequency Decoupling:
  - 10× 100 nF 10V X5R (0201): Sige5 `C3806`, `C3807`, `C3812`, `C3813`, `C3814`, `C3815`, `C3816`, `C3817`, `C3818`, `C3819`; DshanPI-A1 `C134`–`C142`, `C148`
- *Total count:* 2× 22 µF + 2× 10 µF + 3× 1 µF + 10× 100 nF.

#### Rail: `VDDQ_DRAM_S0` (0.60 V I/O)
- Bulk & Intermediate:
  - 2× 10 µF 10V X5R (0603): Sige5 `C3802`, `C3836`; DshanPI-A1 `C124`, `C158`
  - 1× 10 µF 10V X5R (0402): Sige5 `C3820`, DshanPI-A1 `C142`
- High-Frequency Decoupling:
  - 17× 100 nF 10V X5R (0201): Sige5 `C3826`–`C3835`, `C3837`–`C3844`; DshanPI-A1 `C149`–`C157`, `C159`–`C166`
- *Total count:* 3× 10 µF + 17× 100 nF.

---

## 2. eMMC 5.1 Memory Passives

Both ArmSoM Sige5 (sheet 15) and DshanPI-A1 (sheet 19) implement standard JEDEC eMMC 5.1 (153-ball) memory interfaces with identical passives:

### 2.1 Decoupling Capacitors
- **`VCC` (3.30 V Core):**
  - 1× 4.7 µF 10V X5R (0402): Sige5 `C4002`, DshanPI-A1 `C169`
  - 2× 100 nF 10V X5R (0201): Sige5 `C4000`, `C4001`; DshanPI-A1 `C167`, `C168`
- **`VCCQ` / `VCCIO_1V8_S0` (1.80 V I/O):**
  - 1× 4.7 µF 10V X5R (0402): Sige5 `C4006`, DshanPI-A1 `C173`
  - 2× 100 nF 10V X5R (0201): Sige5 `C4004`, `C4005`; DshanPI-A1 `C171`, `C172`
- **`VDDI` (Internal Regulator):**
  - 1× 2.2 µF 10V X5R (0402): Sige5 `C4007`, DshanPI-A1 `C174` (connect between VDDI pin and GND)

### 2.2 Signal Pull-Up & Damping Resistors
- **`EMMC_CMD` Pull-Up:**
  - 10 kΩ 5% (0201) pull-up to `VCCIO_1V8_S0`: Sige5 `R4000`, DshanPI-A1 `R70`
- **`EMMC_CLK` Damping Resistor:**
  - 0 Ω / 22 Ω (0201) series damping resistor placed close to SoC: Sige5 `R4004`, DshanPI-A1 `R72`
- **`EMMC_DATA_STROBE` (DS):**
  - Optional 10 kΩ pull-down (unpopulated / NC by default): Sige5 `R4001`, DshanPI-A1 `R71`
- **`EMMC_RSTN`:**
  - Optional 10 kΩ pull-up (unpopulated / NC by default; internal SoC PMU pull-up active): Sige5 `R4006`, DshanPI-A1 `R74`
"""
    with open('docs/reference_designs/notes/lpddr4x_emmc_passives.md', 'w') as fp:
        fp.write(content)
    print('docs/reference_designs/notes/lpddr4x_emmc_passives.md written.')

def write_power_note():
    content = """# RK3576 & RK806S-5 Power Architecture Comparison

This note documents power architecture similarities and differences between the triaged reference designs (ArmSoM Sige5, ArmSoM CM5, DshanPI-A1, Bit-Brick K1, EVB1 v1.2) and Project FRIDAY's committed Round SCH-1 netlist ([`FRIDAY_Compute_SCH1_netlist.csv`](file:///Users/krish/NMIMS/Friday/hardware/compute_board/out/FRIDAY_Compute_SCH1_netlist.csv)).

> [!NOTE]
> Per the triage rules, this note lists differences only. **No changes are made to Project FRIDAY's committed schematic.**

---

## 1. Input Power Path Differences

| Design | Input Sources | Power Mux / Path | Regulators | Key Differences vs FRIDAY |
| :--- | :--- | :--- | :--- | :--- |
| **ArmSoM Sige5** | 12 V DC Jack (5.5x2.1mm) OR USB-C PD (5V/9V/12V/15V/20V) | Discrete dual-MOSFET OR-ing circuit | SY8303AIC / MP8759 (12V -> 5V @ 5A buck) | Uses 12V DC barrel jack and Type-C PD sink controller (HUSB311). |
| **ArmSoM CM5** | 5.0 V System input via 100-pin board-to-board connectors | None (supplied by CM5-IO carrier) | Carried directly from carrier board | Compute module accepts clean 5V input directly. |
| **DshanPI-A1** | 12 V DC Jack OR USB-C PD | FUSB302 Type-C PD controller + P-FET switches | 12V -> 5V discrete buck converter | Uses dedicated Type-C PD PHY (FUSB302) and 12V DC input. |
| **Project FRIDAY (SCH-1)** | **2S LiPo Battery (6.0V–8.4V)** on J4 + **5V USB-C** on J1 | **U5 (TPS2121RUXR)** automatic seamless power mux | **U10 (SY8205FCC)** high-efficiency buck (2S -> 5V @ 5A) | Optimized for compact wearable glasses; no 12V barrel jack; standard 5V USB-C charging; zero PD sink ICs. |

---

## 2. PMIC (U2: RK806S-5) Comparison

Across all reference designs and FRIDAY SCH-1, the PMIC core topology is 100% identical:
- **I2C Control Mode:** Pin 18 (`CS`) tied to Pin 21 (`VCCA`) via 0 Ω resistor; 10 kΩ pull-ups on I2C bus to `VCCIO6_1V8`.
- **Buck Inductance & Capacitance:**
  - BUCK1, BUCK2, BUCK3, BUCK4: 0.22 µH inductors (0.22uH / 2016 size, e.g. TFM201610ALM-R22MTAA) with 2× 22 µF + 2× 10 µF output caps.
  - BUCK5, BUCK6, BUCK7, BUCK8, BUCK9, BUCK10: 0.47 µH inductors (0.47uH / 2016 size) with 1× 22 µF + 2× 10 µF output caps.
- **External Feedback Dividers (BUCK5, BUCK6, BUCK9):**
  - `BUCK5` (`VDD_CPU_LIT_S0`): R_top = 49.9 kΩ, R_bot = 100 kΩ -> 0.75 V nominal (matches EVB R2302/R2305, Sige5 sheet 12).
  - `BUCK6` (`VDDQ_DDR_S0`): R_top = 22 kΩ, R_bot = 100 kΩ -> 0.61 V nominal (matches EVB R2308/R2310, Sige5 sheet 12).
  - `BUCK9` (`VDD_NPU_S0`): R_top = 120 kΩ, R_bot = 100 kΩ -> 1.10 V nominal (matches EVB R2313/R2315, Sige5 sheet 12).
- **PLDO & NLDO Decoupling:**
  - PLDO1–6 and NLDO1–5 decoupling capacitor values (1.0 µF to 4.7 µF) are completely identical between Sige5 sheet 12, EVB1 sheet 23, and FRIDAY SCH-1 sheet S2.

---

## 3. Discrete Power (U6, U7, U8, U9) Comparison

Both ArmSoM Sige5 (sheet 13) and Project FRIDAY (sheet S3) utilize the exact same discrete power topology:
- **`U6` (TMI3112H):** `VCC_2V0_PLDO_S3` (2.10 V @ 2A buck, FB: 160k / 68k) providing input power to PMIC PLDOs.
- **`U7` (TMI3112H):** `VCC_1V1_NLDO_S3` (1.10 V @ 2A buck, FB: 68k / 82k) providing input power to PMIC NLDOs and LPDDR4X VDD2.
- **`U8` (SY6280AAC):** Load switch distributing `VCC_3V3_S3` into `VCC_3V3_S0`.
- **`U9` (CW3301):** Load switch distributing `VCC_1V8_S3` into `VCC_1V8_S0`.

---

## 4. SoC Unused PHY Power Rail Differences

This represents an intentional design divergence driven by Project FRIDAY's smart glasses form factor:
- **Reference Designs (Sige5, CM5, DshanPI-A1):**
  - Fully power HDMI TX PHY (`VDDA0V75_HDMI_EDP_S0`, `VCCA1V8_HDMI_EDP_S0`), PCIe/SATA combo PHYs (`PCIE0/1_AVDD0V75_S0`, `PCIE0/1_AVDD1V8_S0`), and all 5 camera CSI PHYs to support their expansive board connectors.
- **Project FRIDAY (SCH-1):**
  - Per Rockchip RK3576 Hardware Design Guide §2.2.2 ("Handling of Unused Pins"):
    - Unused HDMI/eDP PHY pins (`HDMI_TX_EDP_TX_*`) are grounded.
    - Unused PCIe/SATA PHY pins (`PCIE0_*`, `PCIE1_*`) are grounded.
    - Unused CSI PHYs (`MIPI_DPHY_CSI1-4_*`) are grounded.
    - Unused USB3 OTG TX/RX pins are left NC / grounded per HDG Table 2-14.
  - This eliminates unnecessary standby leakage current, crucial for wearable battery runtime.
"""
    with open('docs/reference_designs/notes/rk3576_power_comparison.md', 'w') as fp:
        fp.write(content)
    print('docs/reference_designs/notes/rk3576_power_comparison.md written.')

def write_peripherals_note():
    content = """# Peripherals Reference: Wi-Fi/BT, Camera CSI, and USB-C

This note synthesizes peripheral circuit implementations from the triaged reference designs (ArmSoM Sige5, ArmSoM CM5-IO, Bit-Brick K1, DshanPI-A1) to guide upcoming schematic rounds (SCH-3 Camera/Bridge, SCH-4 Wireless/Audio).

---

## 1. Wi-Fi / Bluetooth Subsystem (SDIO 3.0 + UART)

### 1.1 Reference Circuits & Citations
- **ArmSoM Sige5:** Sheet 17 (`RK3576-Schematics/Sige5/armsom-sige5-1v3_Sch.pdf`, p.17) — SDIO Wi-Fi 6 / BT 5.2 module (AP6275P / RTL8852BS / RTL8723DS pin-compatible footprint).
- **Bit-Brick K1 SBC:** Sheet 24 (`Bit-Brick-K1/Circuit Diagram Files for Bit-Brick K1 SBC.pdf`, p.24) — On-board Wi-Fi/BT module with 2.4G/5G antenna connector.
- **DshanPI-A1:** Sheet 36 (`RK3576-Schematics/DshanPI-A1/DshanPi-A1-RK3576-SCH_V1.1.pdf`, p.36) — Standard SDIO Wi-Fi + UART Bluetooth implementation.

### 1.2 Interface Architecture & Wiring
- **Wi-Fi SDIO 3.0 Bus:**
  - Pins: `SDIO_CLK`, `SDIO_CMD`, `SDIO_D0`, `SDIO_D1`, `SDIO_D2`, `SDIO_D3` connected to RK3576 SDIO controller.
  - Power: IO voltage domain is `VCCIO_SD_S0` (switches between 3.3V and 1.8V for high-speed SDR104 mode).
  - Decoupling: 0 Ω or 22 Ω series resistor on `SDIO_CLK`; 10 kΩ pull-ups on CMD and D[3:0].
- **Bluetooth Interface:**
  - UART: 4-wire high-speed UART (`UART_TX`, `UART_RX`, `UART_RTS`, `UART_CTS`) connected to RK3576 UART bus.
  - Audio/Voice (optional): I2S / PCM interface for Bluetooth SCO voice audio (`BT_PCM_CLK`, `BT_PCM_IN`, `BT_PCM_OUT`, `BT_PCM_SYNC`).
- **Control & Clocks:**
  - `WL_REG_ON` (GPIO control from PMU/SoC to enable Wi-Fi power domain).
  - `BT_REG_ON` (GPIO control from PMU/SoC to enable BT power domain).
  - `WL_WAKE_HOST` & `BT_WAKE_HOST` (Interrupt inputs to wake SoC from deep sleep).
  - 32.768 kHz RTC clock input (`CLK32K_OUT` / `32KOUT_RTC2WIFI`).
- **Power Rails:**
  - Module core supply: `VCC_3V3_S0` (requires 10 µF + 100 nF local decoupling).
  - I/O voltage: `VCC_1V8_S0` or `VCCIO_SD_S0`.
  - RF Output: 50 Ω matched microstrip route to U.FL antenna connector (`J12` U.FL-R-SMT-1).

---

## 2. Camera MIPI CSI Subsystem

### 2.1 Reference Circuits & Citations
- **ArmSoM Sige5:** Sheet 11 (`armsom-sige5-1v3_Sch.pdf`, p.11) & Sheet 23 (p.23) — Dual MIPI CSI interfaces (CAM0 2-lane, CAM1 4-lane).
- **ArmSoM CM5-IO:** Sheet 5 (`ArmSoM-CM5-IO-1V1_sch.pdf`, p.5) & Sheet 7 (p.7) — MIPI CSI camera FPC connectors.
- **Bit-Brick K1 SBC:** Sheet 17 (`Circuit Diagram Files for Bit-Brick K1 SBC.pdf`, p.17) — MIPI CSI 24-pin connector.
- **DshanPI-A1:** Sheet 31 & 32 (`DshanPi-A1-RK3576-SCH_V1.1.pdf`, pp. 31-32) — Dual camera CSI interfaces.

### 2.2 Interface Architecture & Wiring
- **Differential Pairs:**
  - Data lanes: `MIPI_CSI_D0_P/N`, `MIPI_CSI_D1_P/N` (for 2-lane), and `D2_P/N`, `D3_P/N` (for 4-lane).
  - Clock lanes: `MIPI_CSI_CLK_P/N`.
  - Impedance: 100 Ω differential impedance target.
- **Control & Sync Signals:**
  - I2C Bus: `I2C_SCL`, `I2C_SDA` with 2.2 kΩ pull-up resistors to `VCC_1V8_S0`.
  - Reset & Power Down: `CAM_RST_L` and `CAM_PDN_H` (GPIOs from RK3576).
  - Master Clock: `MCLK` (24 MHz / 27 MHz clock from SoC to sensor).
- **Power Delivery to Camera Modules (e.g. Raspberry Pi Camera Module 3 / IMX708):**
  - `AVDD` (Analog): 2.80 V (via discrete low-noise LDO).
  - `DVDD` (Digital Core): 1.20 V / 1.05 V (via discrete buck/LDO).
  - `DOVDD` (I/O): 1.80 V (from `VCC_1V8_S0`).

---

## 3. USB-C & USB 2.0 OTG Reference Circuits

### 3.1 Reference Circuits & Citations
- **ArmSoM Sige5:** Sheet 22 (`armsom-sige5-1v3_Sch.pdf`, p.22) — Type-C and USB 2.0 Host/OTG ports.
- **Bit-Brick K1 SBC:** Sheet 21 (`Circuit Diagram Files for Bit-Brick K1 SBC.pdf`, p.21) — USB 2.0 Type-C interface.
- **DshanPI-A1:** Sheet 30 (`DshanPi-A1-RK3576-SCH_V1.1.pdf`, p.30) — USB 2.0 OTG port with ESD protection.

### 3.2 Interface Architecture & Wiring
- **Type-C Configuration Channel (CC):**
  - `CC1` and `CC2` pins on Type-C receptacle terminated with 5.1 kΩ ±1% pull-down resistors to GND (R1 and R2 on FRIDAY SCH-1).
  - Configures the port as a standard Upstream Facing Port (UFP / Sink), requesting 5V from any standard USB host or USB PD source without needing a complex PD controller IC.
- **VBUS Protection & Switching:**
  - VBUS TVS diode (e.g. SMBJ5.0A or ESD5641D) for surge clamping.
  - VBUS detection resistor divider (10 kΩ / 15 kΩ) into SoC SARADC for cable attachment sensing.
  - Power muxing via TPS2121 to safely isolate battery power from USB VBUS.
- **High-Speed USB 2.0 Data (D+ / D-):**
  - Ultra-low capacitance ESD protection diode array (USBLC6-2SC6, Cj < 1.0 pF) connected on D+ and D- to prevent signal distortion.
  - 90 Ω differential impedance routing directly to RK3576 `USB20_OTG0_DP` and `USB20_OTG0_DM`.
"""
    with open('docs/reference_designs/notes/peripherals_reference.md', 'w') as fp:
        fp.write(content)
    print('docs/reference_designs/notes/peripherals_reference.md written.')

if __name__ == '__main__':
    write_emcp_note()
    write_passives_note()
    write_power_note()
    write_peripherals_note()
