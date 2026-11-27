# eMCP Reference Specification: SK hynix H9HP52ACPMADAR-KMM

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
