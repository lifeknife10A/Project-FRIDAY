# SCH-2 eMCP reference cross-check

Project Lead Krishna. Auditor Claude. Schematic baseline `d9d37a8`.

U11 is the SK hynix H9HP52ACPMADAR-KMM, with two LPDDR4X x16 channels, two ranks and an eMMC 5.1 x8 interface. Hynix citations refer to Rev 1.0, March 2018. HDG citations use the printed pages of the RK3576 Hardware Design Guide V1.1. EVB citations use the PDF pages of RK3576 EVB1 V1.2. The full EVB memory drawings are on pp. 24–25. [HDG](../../docs/datasheets/Rockchip%20RK3576%20Hardware%20Design%20Guide.pdf) · [EVB extract](../../docs/datasheets/Schematics%20Only%20for%20RK3576%20EVB1.pdf) · [Reference file inventory](../../docs/reference_designs/INVENTORY.md)

## DDR and eMMC signal mapping

The [DDR pin map](SCH-2_ddr_pinmap.csv) contains 69 direct SoC-to-memory rows, 34 for each channel plus the shared reset. It preserves the channel, data bit, byte lane and differential polarity. Both CKE and CS pins are wired on each channel. The HDG prohibits DQ and CA sequence swapping in §2.1.7.2, p. 15. All 69 RK3576 pin and ball pairs match HDG Table 2-4, printed pp. 13–15 (PDF pp. 32–34). Hynix pp. 6 and 8 specify U11's assignments and the shared DDR reset. EVB pp. 12 and 24, Sige5 sheets 4 and 14, and DshanPI sheets 10 and 18 show the corresponding controller and DRAM signals.

The eMMC clock (U1 1G23 to U11 P12) passes through R4000. CMD, DAT0–DAT7, DS and RST_n connect directly to their U1 interface pins. U11 N9 is the eMMC reset and U11 AA16 is the separate DDR reset. The eMMC VCCIO0 interface runs at 1.8 V. Hynix pp. 6–7 and 54, HDG §§2.1.8.2–2.1.8.4 pp. 19–21, EVB pp. 13 and 25. [I/O bank map](io_bank_map.md)

## Power and ground

| Connection | FRIDAY connection | Source |
| --- | --- | --- |
| U11 VDD1, 10 balls | `VCC_1V8_S3`, RK806 BUCK8 through L8 | Hynix pp. 8, 19–20. HDG §2.1.7.5 pp. 16–18. Sige5 sheet 14 R3806, DshanPI sheet 18 R66 both select `VCC_1V8_S3`. FRIDAY uses the existing rail directly. |
| U11 VDD2, 24 balls | `VDD2_DDR_S3`, RK806 BUCK9 through L9, nominal 1.10 V | Hynix pp. 8 and 19. HDG pp. 16–17 and 44, Figure 2-14. EVB pp. 6 and 21 U2300 BUCK9 and R2313/R2315. Sige5 sheet 14 U3800A and DshanPI sheet 18 U2A use this rail for the memory core. |
| Y2 U1 DDRPHY_CKE_VDDQ, ball 2B2 | BUCK9 `VDD2_DDR_S3` → R3809 0 Ω, 0603 → `VDDQ_DDR_CKE_S3` → U1 2B2 and its existing C1214 | HDG p. 44 permits the shared VDD2 source. EVB pp. 12 and 24 C1214/R3809 and Sige5 sheets 4 and 14 use the named branch through R3809. DshanPI sheets 10 and 18 use R69. |
| U11 VDDQ, 20 balls | `VDDQ_DDR_S0`, RK806 BUCK6 through L6, nominal 0.61 V | Hynix pp. 8 and 19. HDG pp. 16–17 and 44, Figures 2-13 and 2-15. Sige5 sheet 14 R3807 and DshanPI sheet 18 R67 select this source for LPDDR4X. FRIDAY connects it directly. |
| U11 VCC, 3 balls | `VCC_3V3_S0`, existing U8 switched 3.3 V output | Hynix pp. 7, 16 and 54. EVB pp. 22 and 25 U2403/R4003. Sige5 sheet 15 C4004–C4006 on the 3.3 V VCC bank. |
| U11 VCCQ, 8 balls | `VCC_1V8_S0`, existing U9 switched 1.8 V output shared with U1 VCCIO0 | Hynix pp. 7, 16 and 54. HDG §2.1.8.4 p. 21 and §2.1.11.1 p. 28. EVB pp. 13, 22 and 25 C1308/U2402/R4002. Sige5 sheet 15 C4000–C4002 and DshanPI sheet 19 C167–C169 show the 1.8 V I/O bypass. |
| U11 VDDI, L17 | `EMMC_VDDI`, C4004 to GND | Hynix pp. 7 and 54, Figure 16 and Table 14. Sige5 sheet 15 C4007 and DshanPI sheet 19 C174 are the corresponding discrete-eMMC bypasses. |
| U11 VSS and VSSm, 72 balls | Common `GND` | Hynix pp. 6–8. The DRAM and eMMC grounds both return to the board ground. |
| U11 VSF, DNU and NC, 33 balls | Physical pads in the library with NC electrical direction. No schematic pin references. | Hynix pp. 6–7, including the VSF note. |

## DDR passives

FRIDAY uses the requested eMCP capacitor counts and packages from §1.2 of the [passives note](../../docs/reference_designs/notes/lpddr4x_emmc_passives.md). The reference capacitors below indicate comparable values and footprints. The three reference banks distribute some values differently across the rails, as shown on Sige5 sheet 14 and DshanPI sheet 18. The actual FRIDAY rails are listed for every group. See Hynix pp. 19–20 for the operating rails and power-up conditions, and HDG pp. 16–18 and 44–45 for supply and filtering guidance.

| FRIDAY designators | Value and connection | Reference |
| --- | --- | --- |
| R3802, R3804 | One 240 Ω ±1% 0201 per U11 ZQ ball. ZQ0 B16 and ZQ1 C16 each connect through their own resistor to `VDDQ_DDR_S0`. | Hynix p. 8 and §2.34.2.1 p. 229. HDG §2.1.7.3 p. 15. Sige5 sheet 14 R3802/R3804. DshanPI sheet 18 R64/R65. |
| R1200, R1201 | One 240 Ω ±1% 0201 per SoC DDR PHY ZQ ball. U1 1R6 and 1J6 each connect through their own resistor to `VDDQ_DDR_S0`. | HDG §2.1.7.2 p. 15, EVB p. 12 and Sige5 sheet 4 R1200/R1201, DshanPI sheet 10 R11/R12. |
| C3800 | 1 × 10 µF, 0603, VDD1 → GND | Sige5 C3836, DshanPI C158. |
| C3801 | 1 × 1 µF, 0402, VDD1 → GND | Sige5 C3824, DshanPI C146 are value and package examples on VDD2. |
| C3802–C3805 | 4 × 100 nF, 0201, VDD1 → GND | Sige5 C3837–C3840, DshanPI C159–C162. |
| C3806–C3807 | 2 × 22 µF, 0603, VDD2 → GND | Sige5 C3821 and C3801, DshanPI C143 and C123. C3801 and C123 are value and package examples on VDDQ. |
| C3808–C3809 | 2 × 10 µF, 0603, VDD2 → GND | Sige5 C3822–C3823, DshanPI C144–C145. |
| C3810–C3812 | 3 × 1 µF, 0402, VDD2 → GND | Sige5 C3824/C3825 and C3804, DshanPI C146/C147 and C126. C3804 and C126 are examples on VDDQ. |
| C3813–C3822 | 10 × 100 nF, 0201, VDD2 → GND | Sige5 C3826–C3835, DshanPI C148–C157. |
| C3823–C3824 | 2 × 10 µF, 0603, VDDQ → GND | Sige5 C3802–C3803, DshanPI C124–C125. |
| C3825 | 1 × 10 µF, 0402, VDDQ → GND | Sige5 C3820. DshanPI C142 uses 0603 at the same position. |
| C3826–C3842 | 17 × 100 nF, 0201, VDDQ → GND | Sige5 C3806–C3819 and C3837–C3839, DshanPI C128–C141 and C159–C161. C3837–C3839 and C159–C161 are examples on VDD1. |

All 43 added DDR capacitors are specified as 10 V X5R. The existing SCH-1 SoC and regulator bypass capacitors remain in the design.

## Y4 eMMC passives and Y1 USB3 REXT

| FRIDAY designators | Value and connection | Reference |
| --- | --- | --- |
| C4000–C4001 | 2 × 2.2 µF, 0402, `VCC_1V8_S0` → GND | Hynix p. 54 Table 14 C1/C2. Sige5 sheet 15 C4000–C4002 and DshanPI sheet 19 C167–C169 show discrete-eMMC I/O bypass with a different mix of values. |
| C4002–C4003 | 2 × 4.7 µF, 0402, `VCC_3V3_S0` → GND | Hynix p. 54 Table 14 C3/C4. Sige5 sheet 15 C4006 and DshanPI sheet 19 C173 show 4.7 µF on the discrete-eMMC core supply. |
| C4004 | 0.1 µF, 0201, `EMMC_VDDI` → GND | Hynix p. 54 Table 14 C5/C6 and its internal 1 µF note. Sige5 sheet 15 C4007 and DshanPI sheet 19 C174 use 2.2 µF for their discrete packages. |
| R4000 | 27 Ω, 0201, from `EMMC_CLK` to `EMMC_CLKOUT`, placed near U1 in PCB layout | Hynix p. 54 Table 14 R_CLK. HDG pp. 20 and 159, Table 2-5 and Figure 3-13. The host-side examples are Sige5 sheet 5 R1310 (22 Ω) and DshanPI sheet 11 R24 (0 Ω). The eMCP guide recommends removing the series resistance for HS200. |
| R4001 | 10 kΩ, 0201, CMD → `VCC_1V8_S0` | Hynix p. 54 Table 14 R_CMD and HDG p. 20 Table 2-5. Sige5 sheet 15 R4000, DshanPI sheet 19 R70. |
| R4002–R4009 | 8 × 50 kΩ, 0201, one pull-up per DAT0–DAT7 to `VCC_1V8_S0` | Hynix p. 54 Table 14 R_DAT. Sige5 sheet 15 R4001 and DshanPI sheet 19 R71 show an optional DAT0 pull-up in their discrete designs. |
| R4010 | 50 kΩ, 0201, RSTn → `VCC_1V8_S0`, default DNP | Hynix p. 54 Table 14 R_RSTn. Sige5 sheet 15 R4006 and DshanPI sheet 19 R74 are optional reset pull-ups. |
| DS | U11 M12 directly to U1 1F23 | Hynix p. 54 Table 14 R_DS calls for a direct connection with an internal pull-down. Sige5 sheet 15 R4004/R4005 and DshanPI sheet 19 R72/R73 show the discrete-eMMC strobe options. |
| R1400 | 8.2 kΩ ±1%, 0201, U1 2T7 `USB3_OTG0_REXT_DP_TX_REXT` → GND | EVB p. 14 U1000L/R1400. |

## Fusion verification

Fusion 2706.1.17 checked the imported schematic and reported **0 errors, 65 active warnings, 23 inherited SCH-1 approvals and 0 new approvals**. The active entries are code 104, tied to 10 VDD1, 24 VDD2, 20 VDDQ, 3 VCC and 8 VCCQ input balls on the named FRIDAY rails. Each warning is itemized by ball and position. [Fusion ERC](out/FRIDAY_Compute_SCH2_erc.txt)

The generated schematic and the native Fusion netlist independently account for **221 wired balls**. Each of the 83 signal balls and 138 supply or ground balls appears once. The **33 VSF/DNU/NC balls are open** and zero signal balls touch a supply or ground net. The native netlist matches all 69 DDR rows. The export has 196 nets, 1,481 native pin rows, 345 BOM entries and eight vector PDF pages. [Netlist CSV](out/FRIDAY_Compute_SCH2_netlist.csv) · [BOM CSV](out/FRIDAY_Compute_SCH2_bom.csv) · [Schematic PDF](out/SCH-2.pdf)

To reproduce, run `python3 scripts/gen_emcp_lbr.py` and `python3 hardware/compute_board/gen_sch2.py` from the repository root. Run `export_sch2_fusion.py` in Fusion's scripting environment to produce the native exports under `/tmp/friday-sch2-fusion`. Run `python3 hardware/compute_board/format_sch2_exports.py` to validate the native exports and write the deliverables to `out/`.

## Open for the hardware review

- Confirm H9HP52ACPMADAR-KMM support in the RK3576 DDR initialization and eMMC speed configurations. The HDG points to the model support lists in §§2.1.7.6 and 2.1.8.5, pp. 19 and 21.
- Confirm the PCB land and solder-mask geometry with the board fabricator. The library uses Ø0.300 mm copper pads based on the nominal ball diameter in Hynix p. 9. That drawing gives the package geometry and ball diameter. The RK3576 footprint keeps its existing SCH-1 verification status.
- Confirm the intended eMMC speed mode before layout and account for the Hynix HS200 guidance on the clock resistor. [HDG](../../docs/datasheets/Rockchip%20RK3576%20Hardware%20Design%20Guide.pdf)
