# eMCP Reference Specification: SK hynix H9HP52ACPMADAR-KMM

## 1. Device Overview & Part Identification
- **Manufacturer:** SK hynix Inc.
- **Part Number (MPN):** `H9HP52ACPMADAR-KMM` (Rev 1.0, March 2018) [p. 1, p. 6]
- **Package:** 254-ball FBGA, 11.5 mm × 13.0 mm × 1.2 mm max height, 0.50 mm ball pitch [p. 6, p. 9]
  - Ball grid: 24 rows (A to AD, omitting I, O, Q, S, X, Z) × 18 columns (1 to 18) [p. 6, p. 9]
  - Total populated balls: 254 balls [p. 6, p. 9]
- **Density & Architecture:**
  - **eMMC:** 64 GB eMMC 5.1 (x8 bus, HS400 mode up to 400 MB/s, backward compatible with HS200 / DDR50) [p. 1, p. 7, pp. 10–11]
  - **LPDDR4X:** 32 Gb (4 GB) total capacity, organized as 2 channels × 16-bit (Channel A and Channel B), 2 ranks (2CS) [p. 1, p. 6, p. 8]
  - **Speed:** Up to 3733 Mbps (1866 MHz clock frequency) [p. 1, p. 19]

---

## 2. Operating Supply Voltages & Configuration Rules
All supply voltage ranges and configuration rules cited directly from SK hynix H9HP52ACPMADAR Rev 1.0 specification:

| Domain | Signal Name | Nominal Voltage | Operating Voltage Range | Description / Purpose | Reference Citation |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **LPDDR4X Core 1** | `VDD1` | 1.80 V | 1.70 V – 1.95 V | LPDDR4X core supply 1 (analog/wordline) | Spec p. 8, p. 19 |
| **LPDDR4X Core 2** | `VDD2` | 1.10 V | 1.06 V – 1.17 V | LPDDR4X core logic supply 2 | Spec p. 8, p. 19 |
| **LPDDR4X I/O** | `VDDQ` | 0.60 V | 0.57 V – 0.65 V | LPDDR4X ultra-low voltage I/O supply | Spec p. 8, p. 19 |
| **LPDDR4X Ground** | `VSS` | 0.00 V | 0.00 V | DRAM substrate, core, and I/O ground reference | Spec p. 8 |
| **eMMC Core** | `VCC` | 3.30 V | 2.70 V – 3.60 V | eMMC NAND flash memory core supply | Spec p. 7, p. 16 |
| **eMMC I/O** | `VCCQ` | 1.80 V | 1.70 V – 1.95 V | eMMC controller and host I/O buffer supply | Spec p. 7, p. 16 |
| **eMMC Regulator** | `VDDI` | 1.20 V | Internal | Internal eMMC core logic decoupling output (cap to GND) | Spec p. 7, p. 16, p. 54 |
| **eMMC Ground** | `VSSm` | 0.00 V | 0.00 V | eMMC controller and NAND flash dedicated ground | Spec p. 7 |

### 2.1 Power Sequencing
Per LPDDR4X JEDEC standard and SK hynix spec p. 20, power ramp sequence is `VDD1` -> `VDD2` -> `VDDQ`.
On Project FRIDAY:
- `VDD1` (1.80 V) is supplied by PMIC RK806S-5 `VCC_1V8_S3` (or PLDO6).
- `VDD2` (1.10 V) is supplied by PMIC RK806S-5 `BUCK9` (`VDD2_DDR_S3`).
- `VDDQ` (0.60 V) is supplied by PMIC RK806S-5 `BUCK6` (`VDDQ_DDR_S0`, 0.61 V nominal).

### 2.2 ZQ Calibration Resistor Specification (Exact Datasheet Quotations)
The eMCP specification explicitly mandates that the 240 Ω calibration resistor connects to **`VDDQ`**:
- **Page 8 (DRAM Pin Description, Symbol `ZQ0, ZQ1`):**
  > *"Calibration Reference: Used to calibrate the output drive strength and the termination resistance. This pin shall be connected to VDDQ through a 240-Ω ± 1% resistor."*
- **Page 229 (§2.34.2.1 "ZQ External Resistor, Tolerance, and Capacitive Loading"):**
  > *"To use the ZQ calibration function, a 240 ohm +/- 1% tolerance external resistor must be connected between the ZQ pin and VDDQ."*
- **Page 265 (Figure "Pull-down calibration"):**
  > *"1) First calibrate the pull-down device against a 240 Ohm resister to VDDQ via the ZQ pin."*

### 2.3 VDDi Decoupling Capacitor Specification (Authoritative eMCP Value)
Per Page 54 (Section 4.3 "Connection Guide", Table 14 "Connection guide specification"):
- **`VDDi capacitor value` (C5 & C6):**
  - **Recommended External Value:** `0.1 µF` (Min: 0 µF, Max: 2.2 µF)
  - **Datasheet Remark:** *"Coupling cap should be connected with VDDi and Vssq as closely possible. (Internal Cap : 1uF)"*
- Because the eMCP die package integrates an internal 1 µF capacitor on `VDDI`, the external decoupling capacitor required on Project FRIDAY is **0.1 µF** (authoritative over discrete eMMC reference designs which lack internal capacitors and use 2.2 µF).

---

## 3. Ball Map & Signal Summary (254-Ball FBGA)
Every ball list and count below is generated directly from [`hardware/compute_board/emcp_ballmap_source.csv`](file:///Users/krish/NMIMS/Friday/hardware/compute_board/emcp_ballmap_source.csv), extracted ball-by-ball from Page 6 (Top View diagram):

- **Total Pins in Package Grid:** 254 balls
- **Unreadable Pins:** 0 balls (100% verified against Pin Descriptions pp. 7–8)

### 3.1 LPDDR4X Interface (Dual Channel, x32 Total Bus)
1. **Command / Address (12 balls):**
   - **Channel A (6 balls):** G14 (CA0_A), F13 (CA1_A), C13 (CA2_A), D13 (CA3_A), E13 (CA4_A), C15 (CA5_A)
   - **Channel B (6 balls):** V14 (CA0_B), W13 (CA1_B), AB13 (CA2_B), AA13 (CA3_B), Y13 (CA4_B), AB15 (CA5_B)
2. **Clock (4 balls):**
   - **Channel A (2 balls):** H16 (CLK_t_A), G16 (CLK_c_A)
   - **Channel B (2 balls):** U16 (CLK_t_B), V16 (CLK_c_B)
3. **Clock Enable (4 balls):**
   - **Channel A (2 balls):** E16 (CKE0_A), F16 (CKE1_A)
   - **Channel B (2 balls):** Y16 (CKE0_B), W16 (CKE1_B)
4. **Chip Select (4 balls):**
   - **Channel A (2 balls):** E15 (CS0_A), F15 (CS1_A)
   - **Channel B (2 balls):** Y15 (CS0_B), W15 (CS1_B)
5. **Data I/O (32 balls):**
   - **Channel A Byte 0 (8 balls):** A3 (DQ0_A), B3 (DQ1_A), C3 (DQ2_A), D3 (DQ3_A), B7 (DQ4_A), C6 (DQ5_A), D7 (DQ6_A), C8 (DQ7_A)
   - **Channel A Byte 1 (8 balls):** K5 (DQ8_A), K6 (DQ9_A), K3 (DQ10_A), J3 (DQ11_A), J7 (DQ12_A), G3 (DQ13_A), H6 (DQ14_A), H8 (DQ15_A)
   - **Channel B Byte 0 (8 balls):** AD3 (DQ0_B), AC3 (DQ1_B), AB3 (DQ2_B), AA3 (DQ3_B), AC7 (DQ4_B), AB6 (DQ5_B), AA7 (DQ6_B), AB8 (DQ7_B)
   - **Channel B Byte 1 (8 balls):** R5 (DQ8_B), R6 (DQ9_B), R3 (DQ10_B), T3 (DQ11_B), T7 (DQ12_B), V3 (DQ13_B), U6 (DQ14_B), U8 (DQ15_B)
6. **Data Mask Inversion (4 balls):**
   - **Channel A (2 balls):** D5 (DMI0_A), H3 (DMI1_A)
   - **Channel B (2 balls):** AA5 (DMI0_B), U3 (DMI1_B)
7. **Differential Data Strobes (8 balls):**
   - **Channel A (4 balls):** C9 (DQS0_t_A), D9 (DQS0_c_A), K9 (DQS1_t_A), J9 (DQS1_c_A)
   - **Channel B (4 balls):** AB9 (DQS0_t_B), AA9 (DQS0_c_B), R9 (DQS1_t_B), T9 (DQS1_c_B)
8. **Calibration & Reset (3 balls):**
   - **ZQ0 (Channel A, 1 ball):** B16
   - **ZQ1 (Channel B, 1 ball):** C16
   - **RST_n (DRAM Common Reset, 1 ball):** AA16
9. **LPDDR4X Power & Ground (108 balls):**
   - **`VDD1` (1.80 V, 10 balls):** A4, A9, A15, A16, B15, AC15, AD4, AD9, AD15, AD16
   - **`VDD2` (1.10 V, 24 balls):** A5, A8, B9, B13, B14, G7, G8, G9, K2, L7, L8, L9, P7, P8, P9, R2, V7, V8, V9, AC9, AC13, AC14, AD5, AD8
   - **`VDDQ` (0.60 V, 20 balls):** A6, A7, A13, A14, B5, H5, H9, J4, J5, J8, T4, T5, T8, U5, U9, AC5, AD6, AD7, AD13, AD14
   - **`VSS` (Ground, 54 balls):** B4, B6, B8, C4, C5, C7, C14, D4, D6, D8, D14, D15, E14, F14, G4, G5, G6, G13, G15, H4, H7, H13, H15, J6, K4, K7, K8, R4, R7, R8, T6, U4, U7, U13, U15, V4, V5, V6, V13, V15, W14, Y14, AA4, AA6, AA8, AA14, AA15, AB4, AB5, AB7, AB14, AC4, AC6, AC8

### 3.2 eMMC 5.1 Interface (8-bit Bus)
1. **Control & Data (12 balls):**
   - **Clock `CLKm` (1 ball):** P12
   - **Command `CMD` (1 ball):** M9
   - **Data Strobe `DS` (1 ball):** M12
   - **Reset `RST_n` (eMMC Reset, 1 ball):** N9
   - **Data Bus (8 balls):** P16 (DAT0), M15 (DAT1), N13 (DAT2), P15 (DAT3), M16 (DAT4), N14 (DAT5), L14 (DAT6), L13 (DAT7)
2. **eMMC Power & Ground (30 balls):**
   - **`VCC` (3.30 V Core, 3 balls):** M17, N17, P17
   - **`VCCQ` (1.80 V I/O, 8 balls):** J15, J16, J17, K15, R13, R14, T15, T16
   - **`VDDI` (Internal Regulator Decoupling, 1 ball):** L17
   - **`VSSm` (eMMC Dedicated Ground, 18 balls):** K13, K14, K16, L12, L15, L16, M8, M13, M14, N8, N12, N15, N16, P13, P14, R15, R16, R17

### 3.3 Vendor Specific, No Connect, and Do Not Use
- **`VSF[1:9]` (Vendor Specific Function, 9 balls):** M3 (VSF1), N3 (VSF2), M4 (VSF3), N4 (VSF4), M5 (VSF5), N5 (VSF6), M6 (VSF7), N6 (VSF8), M7 (VSF9)
  *(Note 1 on p. 6: Terminal should not have any external electrical connections)*
- **`DNU` (Do Not Use, 12 balls):** A1, A2, A17, A18, B1, B18, AC1, AC18, AD1, AD2, AD17, AD18
- **`NC` (No Connect, 12 balls):** D16, H14, J13, J14, K17, N7, T13, T14, T17, U14, AB16, AC16

---

### 3.4 Verification & Accounting
- **LPDDR4X Signals + Power/Ground:** 12 (CA) + 4 (CLK) + 4 (CKE) + 4 (CS) + 32 (DQ) + 4 (DMI) + 8 (DQS) + 2 (ZQ) + 1 (RST_n) + 10 (VDD1) + 24 (VDD2) + 20 (VDDQ) + 54 (VSS) = **179 balls**
- **eMMC Signals + Power/Ground:** 1 (CLKm) + 1 (CMD) + 1 (DS) + 1 (RST_n) + 8 (DAT) + 3 (VCC) + 8 (VCCQ) + 1 (VDDI) + 18 (VSSm) = **42 balls**
- **Non-Connected (VSF + DNU + NC):** 9 (VSF) + 12 (DNU) + 12 (NC) = **33 balls**
- **Total Accounting:** 179 + 42 + 33 = **254 balls** (100% matched to physical 254-ball package grid)
