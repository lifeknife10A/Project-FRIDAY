# Round SCH-1 EVB Cross-Reference & Deviations Report

## 1. Fusion Design & Export Summary
- **Fusion Design Name:** `FRIDAY_Compute_SCH1`
- **Fusion Project:** `Friday` (`202611261174942881`)
- **Fusion DataFile ID:** `urn:adsk.wipprod:dm.lineage:Obb-HeBISf6nfqQgUaSukA`
- **Fusion Design Version / Revision Exported:** **`v1`** (Autodesk Fusion 2706.1.17)
- **Fusion ERC Result:** **`0` Errors, `33` Warnings** (`Schematic Checked: True`; full log in `out/FRIDAY_Compute_SCH1_erc.txt`)
- **Exported Deliverables (`hardware/compute_board/out/`):**
  - `SCH-1.pdf` (5-sheet A3 Landscape vector PDF, uncropped)
  - `FRIDAY_Compute_SCH1_erc.txt` (Fusion ERC report: 0 errors, 33 itemized warnings)
  - `FRIDAY_Compute_SCH1_netlist.txt` & `FRIDAY_Compute_SCH1_netlist.csv` (104 nets exported from Fusion)
  - `FRIDAY_Compute_SCH1_bom.csv` (266 BOM components exported from Fusion)
  - `FRIDAY_Compute_SCH1.sch` & `FRIDAY_SCH1_Support.lbr`

## 2. Footprint Verification Status (Mandatory Disclosure)
- **RK3576 FCCSP-698L (`U1`, `libraries/RK3576.lbr`)**: **`UNVERIFIED vs RK3576 DS §2 package drawing`** — all 698 ball coordinates, mixed pitch zones (0.55 / 0.60 / 0.65 mm), and solder mask openings MUST be verified ball-by-ball against RK3576 Datasheet Rev 1.5 §2 prior to PCB layout / fabrication.

## 3. Fusion ERC Warning Itemization (`0` Errors / `33` Warnings)
All `33` warnings are benign EAGLE/Fusion **code `104`** notices (`POWER pin <part> <pin> connected to <net>`), caused by library pins typed `dir=pwr` whose symbol pin names (e.g., `VCC9`, `VOUT1`, `PVIN`, `VBUS`, `IN`) intentionally differ from PROJECT FRIDAY's system/EVB net names (e.g., `VCC5V0_SYS_S5`, `VDD_CPU_BIG_S0`, `VBAT_2S_IN`). Zero overlap, floating-pin, missing-junction, or mixed-direction errors exist:

| # | Sheet | Coords (mm) | Code | Fusion ERC Warning | Engineering Explanation |
| :--- | :---: | :--- | :---: | :--- | :--- |
| 1 | S1 | (121.92,233.68) | 104 | `POWER pin U10 PVIN connected to VBAT_2S_IN` | Pin name differs from rail net name; net voltage and direction verified against EVB/datasheet. |
| 2 | S1 | (121.92,231.14) | 104 | `POWER pin U10 VCC connected to U10_VCC` | Pin name differs from rail net name; net voltage and direction verified against EVB/datasheet. |
| 3 | S1 | (73.66,132.08) | 104 | `POWER pin J1 VBUS connected to VBUS_5V` | Pin name differs from rail net name; net voltage and direction verified against EVB/datasheet. |
| 4 | S1 | (172.72,119.38) | 104 | `POWER pin D1 VBUS connected to VBUS_5V` | Pin name differs from rail net name; net voltage and direction verified against EVB/datasheet. |
| 5 | S2 | (213.36,114.30) | 104 | `POWER pin U2 VCC9 connected to VCC5V0_SYS_S5` | Pin name differs from rail net name; net voltage and direction verified against EVB/datasheet. |
| 6 | S2 | (213.36,119.38) | 104 | `POWER pin U2 VOUT8 connected to VCC_1V8_S3` | Pin name differs from rail net name; net voltage and direction verified against EVB/datasheet. |
| 7 | S2 | (213.36,124.46) | 104 | `POWER pin U2 VCC8 connected to VCC5V0_SYS_S5` | Pin name differs from rail net name; net voltage and direction verified against EVB/datasheet. |
| 8 | S2 | (167.64,137.16) | 104 | `POWER pin U2 VCC14 connected to VCC_1V1_NLDO_S3` | Pin name differs from rail net name; net voltage and direction verified against EVB/datasheet. |
| 9 | S2 | (167.64,147.32) | 104 | `POWER pin U2 VCC13 connected to VCC_1V1_NLDO_S3` | Pin name differs from rail net name; net voltage and direction verified against EVB/datasheet. |
| 10 | S2 | (213.36,195.58) | 104 | `POWER pin U2 VCCIO connected to VCCA1V8_PLDO6_S3` | Pin name differs from rail net name; net voltage and direction verified against EVB/datasheet. |
| 11 | S2 | (213.36,193.04) | 104 | `POWER pin U2 VCCA connected to VCC5V0_SYS_S5` | Pin name differs from rail net name; net voltage and direction verified against EVB/datasheet. |
| 12 | S2 | (213.36,170.18) | 104 | `POWER pin U2 VCC4 connected to VCC5V0_SYS_S5` | Pin name differs from rail net name; net voltage and direction verified against EVB/datasheet. |
| 13 | S2 | (213.36,165.10) | 104 | `POWER pin U2 VOUT4 connected to VCC_3V3_S3` | Pin name differs from rail net name; net voltage and direction verified against EVB/datasheet. |
| 14 | S2 | (213.36,96.52) | 104 | `POWER pin U2 VOUT10 connected to VDD_DDR_S0` | Pin name differs from rail net name; net voltage and direction verified against EVB/datasheet. |
| 15 | S2 | (213.36,101.60) | 104 | `POWER pin U2 VCC10 connected to VCC5V0_SYS_S5` | Pin name differs from rail net name; net voltage and direction verified against EVB/datasheet. |
| 16 | S2 | (213.36,147.32) | 104 | `POWER pin U2 VCC6 connected to VCC5V0_SYS_S5` | Pin name differs from rail net name; net voltage and direction verified against EVB/datasheet. |
| 17 | S2 | (213.36,142.24) | 104 | `POWER pin U2 VOUT6 connected to VDDQ_DDR_S0` | Pin name differs from rail net name; net voltage and direction verified against EVB/datasheet. |
| 18 | S2 | (213.36,190.50) | 104 | `POWER pin U2 VDC connected to PMIC_VDC` | Pin name differs from rail net name; net voltage and direction verified against EVB/datasheet. |
| 19 | S2 | (167.64,96.52) | 104 | `POWER pin U2 VCC2 connected to VCC5V0_SYS_S5` | Pin name differs from rail net name; net voltage and direction verified against EVB/datasheet. |
| 20 | S2 | (167.64,91.44) | 104 | `POWER pin U2 VOUT2 connected to VDD_NPU_S0` | Pin name differs from rail net name; net voltage and direction verified against EVB/datasheet. |
| 21 | S2 | (213.36,129.54) | 104 | `POWER pin U2 VOUT7 connected to VDD_LOGIC_S0` | Pin name differs from rail net name; net voltage and direction verified against EVB/datasheet. |
| 22 | S2 | (213.36,134.62) | 104 | `POWER pin U2 VCC7 connected to VCC5V0_SYS_S5` | Pin name differs from rail net name; net voltage and direction verified against EVB/datasheet. |
| 23 | S2 | (213.36,160.02) | 104 | `POWER pin U2 VCC5 connected to VCC5V0_SYS_S5` | Pin name differs from rail net name; net voltage and direction verified against EVB/datasheet. |
| 24 | S2 | (213.36,154.94) | 104 | `POWER pin U2 VOUT5 connected to VDD_GPU_S0` | Pin name differs from rail net name; net voltage and direction verified against EVB/datasheet. |
| 25 | S2 | (167.64,104.14) | 104 | `POWER pin U2 VOUT1 connected to VDD_CPU_BIG_S0` | Pin name differs from rail net name; net voltage and direction verified against EVB/datasheet. |
| 26 | S2 | (167.64,109.22) | 104 | `POWER pin U2 VCC1 connected to VCC5V0_SYS_S5` | Pin name differs from rail net name; net voltage and direction verified against EVB/datasheet. |
| 27 | S2 | (213.36,180.34) | 104 | `POWER pin U2 VCC3 connected to VCC5V0_SYS_S5` | Pin name differs from rail net name; net voltage and direction verified against EVB/datasheet. |
| 28 | S2 | (213.36,175.26) | 104 | `POWER pin U2 VOUT3 connected to VDD_CPU_LIT_S0` | Pin name differs from rail net name; net voltage and direction verified against EVB/datasheet. |
| 29 | S2 | (167.64,124.46) | 104 | `POWER pin U2 VCC11 connected to VCC_2V0_PLDO_S3` | Pin name differs from rail net name; net voltage and direction verified against EVB/datasheet. |
| 30 | S2 | (167.64,114.30) | 104 | `POWER pin U2 VCC12 connected to VCC5V0_SYS_S5` | Pin name differs from rail net name; net voltage and direction verified against EVB/datasheet. |
| 31 | S2 | (213.36,109.22) | 104 | `POWER pin U2 VOUT9 connected to VDD2_DDR_S3` | Pin name differs from rail net name; net voltage and direction verified against EVB/datasheet. |
| 32 | S3 | (60.96,223.52) | 104 | `POWER pin U6 IN connected to VCC5V0_SYS_S5` | Pin name differs from rail net name; net voltage and direction verified against EVB/datasheet. |
| 33 | S3 | (246.38,223.52) | 104 | `POWER pin U7 IN connected to VCC5V0_SYS_S5` | Pin name differs from rail net name; net voltage and direction verified against EVB/datasheet. |

## 4. Intentional Deviations from RK3576 EVB1 (`RK_EVB1_RK3576_LP4XD200P132SD6_V12`)
1. **Dual-Input Power Architecture (`J4` + `U10 SY8205FCC` + `U5 TPS2121RUXR`)**: EVB uses a 12 V DC barrel adapter + Type-C PD (`FUSB302B`) into discrete FETs (`VCC12V_DCIN` -> `VCC5V0_SYS`). FRIDAY replaces this with 2S LiPo battery pads (`J4`, `6.0-8.4 V`) stepped down by `U10` (`SY8205FCC`, `5.0 V @ 5 A`) and auto-muxed against USB-C `VBUS_5V` via `U5` (`TPS2121RUXR`) into `VCC5V0_SYS_S5`.
2. **USB 2.0-Only Type-C Receptacle (`J1 TYPE-C-31-M-12`)**: Replaces EVB's USB3.0/DP1.4 full-featured Type-C + PD controller with a 16-pin USB 2.0-only receptacle, dual `5.1 kΩ` `Rd` pull-downs (`R1/R2`), `D2` VBUS TVS, and `D1` `USBLC6-2SC6`. *Note:* Because `USBLC6-2SC6` protects `DP/DN` + `VBUS`, `CC1/CC2` ESD diodes are omitted vs the earlier 4-channel note in `schematic_components.md`.
3. **32.768 kHz RTC Eliminated (`PMU_PVTM`)**: Uses RK3576 internal `PMU_PVTM` oscillator per HDG §2 Table 2-1 (`Y2`, `C3`, `C4` omitted) rather than EVB's external `HYM8563TS` RTC.
4. **Removed Unused Peripherals (HDG §2.2.2)**:
   - **HDMI 2.1 / eDP 1.3 TX (`HDMI_TX_EDP_TX_AVDD*`)**: SoC power balls grounded (`GND`) per HDG §2.2.2.17; PMIC `NLDO3` (`VDDA0V75_HDMI_S0`) remains terminated with `C2367 2.2 uF`.
   - **PCIe 2.1 / SATA 3.1 / USB3 OTG1 (`PCIE0/1*_AVDD*`)**: SoC power balls grounded (`GND`) per HDG §2.2.2.14.
   - **MIPI DPHY CSI1-4 (`MIPI_DPHY_CSI1/2/3/4_RX_AVDD*`)**: Grounded (`GND`) per HDG §2.2.2.15 (only `MIPI_DCPHY` is used for `J2` IMX708).
   - **UFS (`UFS_AVDD0V85/1V8`, `OSC_UFS_AVDD`, `VCCIO7_VCC`) & USB3/DP1.4 (`USB3_OTG0_DP_TX_AVDD*`)**: Left unpowered (`NC`) per HDG Table 2-14 / §2.2.2.11 / §2.2.2.13 (UFS & USB3 omitted; eMCP runs on `VCCIO0` and firmware downloads via `USB2_OTG0`).
5. **Library Pin Direction Notes (`RK806-1`, `FRIDAY_SCH1_Support`)**:
   - `U2.FB1` and `U2.FB2` set to `direction="nc"` inside the schematic's embedded `RK806-1` definition matching EVB Sheet 23 `X` (internal DVS DAC mode per RK806 DS p.19).
   - Non-`GND` off-sheet power rail flags use `direction="pas"` to avoid EAGLE `OUTPUT+SUPPLY mixed` (`code 208`) false errors with regulator `out` pins.
6. **Contradictions Fixed in `docs/schematic_components.md`**:
   - `D1` (`L134`): Updated from generic 4-ch ESD note to match committed `USBLC6-2SC6.lbr` (2-ch `DP/DN` + `VBUS`).
   - `R19-R24` (`L154-155`): Fixed BUCK6 (`22k/100k` EVB `R2308/R2310`, `0.61 V`) and BUCK9 (`120k/100k` EVB `R2313/R2315`, `1.10 V`), plus noted BUCK5 (`R2302=49.9k/R2305=100k`).
   - `J4` (`L189`): Corrected signal label from `VBAT_BUCK_5V (5.0V)` to `VBAT_2S_IN (6.0-8.4 V)` upstream of `U10`.

## 5. Power Net Cross-Reference
| Power Net | Voltage | Source | EVB Citation / Sheet | Status | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `DDR_PLL_AVDD1V8` | 1.80V | R1202 0R from VCCA_1V8_S0 | EVB Sheet 12 p.12 | Same | Filtered 1.8V DDR PLL supply. |
| `MIPI_DCPHY_AVDD` | 0.75V | R1502 0.1R from VDDA_0V75_S0 | EVB Sheet 15 p.15 | Same | Filtered 0.75V MIPI DCPHY analog supply (CSI0 camera). |
| `OSC_1V8` | 1.80V | R1119 0.1R from VCCA_1V8_S0 | EVB Sheet 11 p.11 | Same | Filtered 1.8V OSC_AVDD1V8. |
| `SARADC_AVDD1V8` | 1.80V | R1147 0.1R from VCCA1V8_PLDO2_S0 | EVB Sheet 11 p.11 | Same | Filtered 1.8V SARADC/TSADC/OTP & MaskROM divider supply. |
| `VBAT_2S_IN` | 6.0V - 8.4V | J4 Battery Pads -> U10 IN | Project 2S LiPo spec | Deviation | 2S pack direct input instead of EVB 12V DC barrel. |
| `VBAT_BUCK_5V` | 5.00V | U10 (SY8205FCC) -> U5 IN2 | SY8205 DS Fig. 2 | Deviation | Dedicated 5.0V pre-buck from 2S battery into power mux. |
| `VBUS_5V` | 5.00V | J1 USB-C VBUS -> U5 IN1 / VBUSDET | EVB Sheet 25 p.23 / TPS2121 DS | Deviation | Routed via TPS2121 IN1 instead of EVB discrete barrel/PD path. |
| `VCC5V0_SYS_S5` | 5.00V | U5 (TPS2121RUXR) OUT -> PMIC/S3 | EVB Sheet 05 p.6 & Sheet 23 | Same (source deviated) | Same EVB net name/voltage; sourced from U5 mux. |
| `VCCA1V8_PLDO2_S0` | 1.80V | RK806S-5 PLDO2 (0.3A) | EVB Sheet 05 p.6 & Sheet 23 | Same | Feeds SARADC_AVDD1V8 via R1147 0.1R. |
| `VCCA1V8_PLDO6_S3` | 1.80V | RK806S-5 PLDO6 internal -> VCCIO | EVB Sheet 05 p.6 & Sheet 23 | Same | PMIC VCCIO + I2C1 10k pull-ups. |
| `VCCA_1V8_S0` | 1.80V | RK806S-5 PLDO1 (0.5A) | EVB Sheet 05 p.6 & Sheet 23 | Same | Analog 1.8V for PLL, OSC, USB2 PHY, MIPI DCPHY. |
| `VCCA_3V3_S0` | 3.30V | RK806S-5 PLDO4 (0.5A) | EVB Sheet 05 p.6 & Sheet 23 | Same | 3.3V analog S0 rail. |
| `VCCIO_SD_S0` | 3.30V | RK806S-5 PLDO5 (0.3A) | EVB Sheet 05 p.6 & Sheet 23 | Same | RK3576 VCCIO1 bias. |
| `VCC_1V1_NLDO_S3` | 1.10V | U7 TMI3112H (2.0A) | EVB Sheet 24 p.22 (U2401) | Same | Pre-regulator for RK806 VCC13/VCC14 (NLDO1-5 input). |
| `VCC_1V8_S0` | 1.80V | U9 CW3301 | EVB Sheet 24 p.22 (U2402) | Same | Switched 1.8V S0 rail (VCCIO0/VCCIO5, eMCP VCCQ in SCH-2, Camera I/O in SCH-3). |
| `VCC_1V8_S3` | 1.80V | RK806S-5 BUCK8 (3.0A) | EVB Sheet 05 p.6 & Sheet 23 | Same | Always-on S3 1.8V PMUIO0, U9 input, RESET_L pull-up. |
| `VCC_2V0_PLDO_S3` | 2.094V | U6 TMI3112H (2.0A) | EVB Sheet 24 p.22 (U2400) | Same | Pre-regulator for RK806 VCC11 (PLDO1-3 input). |
| `VCC_3V3_S0` | 3.30V | U8 SY6280AAC | EVB Sheet 24 p.22 (U2403) | Same | Switched 3.3V S0 rail (VCCIO2/4/6, USB2_OTG_AVDD3V3, Peripherals). |
| `VCC_3V3_S3` | 3.30V | RK806S-5 BUCK4 (5.0A) | EVB Sheet 05 p.6 & Sheet 23 | Same | Always-on S3 3.3V IO/PMUIO1/VCCIO3 & U8 input. |
| `VDD2_DDR_S3` | 1.10V | RK806S-5 BUCK9 (3.0A, FB9) | EVB Sheet 05 p.6 & Sheet 23 | Same | LPDDR4X VDD2 rail (1.10V via R22=120k, R24=100k). |
| `VDDA0V75_HDMI_S0` | 0.75V | RK806S-5 NLDO3 (0.5A) | EVB Sheet 05 p.6 & Sheet 23 | Deviation (HDMI unused on SoC) | NLDO3 rail terminated at EVB C2367 2.2uF; SoC HDMI pins grounded per HDG §2.2.2.17. |
| `VDDA_0V75_S0` | 0.75V | RK806S-5 NLDO5 (0.5A) | EVB Sheet 05 p.6 & Sheet 23 | Same | RK3576 PLL_DVDD0V75, OTP_DVDD0V75, USB2_OTG_DVDD0V75, MIPI_DCPHY_AVDD. |
| `VDDA_0V85_S0` | 0.85V | RK806S-5 NLDO4 (0.5A) | EVB Sheet 05 p.6 & Sheet 23 | Deviation (PCIe/USB3 unused) | NLDO4 rail terminated at EVB C2370 2.2uF; SoC PCIe grounded & USB3 NC per HDG. |
| `VDDA_1V2_S0` | 1.20V | RK806S-5 PLDO3 (0.3A) | EVB Sheet 05 p.6 & Sheet 23 | Same | MIPI_DCPHY_AVDD1V2. |
| `VDDA_DDR_PLL_S0` | 0.85V | RK806S-5 NLDO2 (0.3A) | EVB Sheet 05 p.6 & Sheet 23 | Same | RK3576 DDRPHY_PLL_DVDD. |
| `VDDQ_DDR_S0` | 0.61V | RK806S-5 BUCK6 (3.0A, FB6) | EVB Sheet 05 p.6 & Sheet 23 | Same | LPDDR4X VDDQ rail (0.61V via R19=22k, R21=100k). |
| `VDD_0V75_S3` | 0.75V | RK806S-5 NLDO1 (0.3A) | EVB Sheet 05 p.6 & Sheet 23 | Same | RK3576 PMU_LOGIC_DVDD0V75. |
| `VDD_CPU_BIG_S0` | 0.75V (I2C DVS) | RK806S-5 BUCK1 (6.5A) | EVB Sheet 05 p.6 & Sheet 23 | Same | RK3576 CPU_BIG_DVDD. |
| `VDD_CPU_LIT_S0` | 0.75V (I2C DVS) | RK806S-5 BUCK3 (5.0A) | EVB Sheet 05 p.6 & Sheet 23 | Same | RK3576 CPU_LIT_DVDD. |
| `VDD_DDR_S0` | 0.85V | RK806S-5 BUCK10 (3.0A) | EVB Sheet 05 p.6 & Sheet 23 | Same | RK3576 DDRPHY_DVDD. |
| `VDD_GPU_S0` | 0.75V | RK806S-5 BUCK5 (3.0A, FB5) | EVB Sheet 05 p.6 & Sheet 23 | Same | RK3576 GPU_DVDD (R2302=49.9k, R2305=100k). |
| `VDD_LOGIC_S0` | 0.75V | RK806S-5 BUCK7 (3.0A) | EVB Sheet 05 p.6 & Sheet 23 | Same | RK3576 LOGIC_DVDD & LOGIC_MEM_DVDD. |
| `VDD_NPU_S0` | 0.75V (I2C DVS) | RK806S-5 BUCK2 (5.0A) | EVB Sheet 05 p.6 & Sheet 23 | Same | RK3576 NPU_DVDD. |

## 6. Complete Component Cross-Reference (266 BOM Components)
| Sheet | Our RefDes | Value | Package / Device | EVB RefDes / Datasheet Citation | Status | Reason / Function |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| S1 | `J4` | `2S_BATT_PADS_6-8.4V` | `BATT_PADS_2PIN` | Project 2S battery spec (schematic_components.md §1/§8) | Deviation (EVB uses 12V DC barrel) | 2-pad solder terminal (VBAT_2S_IN 6.0-8.4V into U10 SY8205FCC). |
| S1 | `U10` | `SY8205FCC` | `SY8205FCC` | SY8205 DS Fig. 2, p.3, p.5 | Deviation (EVB has no 2S battery buck) | 2S LiPo (6.0-8.4V) synchronous buck to VBAT_BUCK_5V (5.0V @ 5A). |
| S1 | `C83` | `10uF 25V` | `C_0603` | SY8205 DS Fig. 2 & p.5 / USB-C VBUS decoupling | Deviation (new U10/J1 stage) | U10 FB=0.6*(1+73.2k/10k)=4.992V, EN UVLO, SS, BST, input/output caps & J1 decoupling. |
| S1 | `C84` | `10uF 25V` | `C_0603` | SY8205 DS Fig. 2 & p.5 / USB-C VBUS decoupling | Deviation (new U10/J1 stage) | U10 FB=0.6*(1+73.2k/10k)=4.992V, EN UVLO, SS, BST, input/output caps & J1 decoupling. |
| S1 | `R100` | `100k 1%` | `R_0402` | SY8205 DS Fig. 2 & p.5 / USB-C VBUS decoupling | Deviation (new U10/J1 stage) | U10 FB=0.6*(1+73.2k/10k)=4.992V, EN UVLO, SS, BST, input/output caps & J1 decoupling. |
| S1 | `R101` | `27k 1%` | `R_0402` | SY8205 DS Fig. 2 & p.5 / USB-C VBUS decoupling | Deviation (new U10/J1 stage) | U10 FB=0.6*(1+73.2k/10k)=4.992V, EN UVLO, SS, BST, input/output caps & J1 decoupling. |
| S1 | `C100` | `100nF 10V` | `C_0402` | SY8205 DS Fig. 2 & p.5 / USB-C VBUS decoupling | Deviation (new U10/J1 stage) | U10 FB=0.6*(1+73.2k/10k)=4.992V, EN UVLO, SS, BST, input/output caps & J1 decoupling. |
| S1 | `C82` | `1uF 10V` | `C_0402` | SY8205 DS Fig. 2 & p.5 / USB-C VBUS decoupling | Deviation (new U10/J1 stage) | U10 FB=0.6*(1+73.2k/10k)=4.992V, EN UVLO, SS, BST, input/output caps & J1 decoupling. |
| S1 | `C81` | `100nF 25V` | `C_0402` | SY8205 DS Fig. 2 & p.5 / USB-C VBUS decoupling | Deviation (new U10/J1 stage) | U10 FB=0.6*(1+73.2k/10k)=4.992V, EN UVLO, SS, BST, input/output caps & J1 decoupling. |
| S1 | `L13` | `2.2uH 6.5A` | `IND_4040` | SY8205 DS Fig. 2 / p.8 (2.2uH >=6.5A) | Deviation (new U10 stage) | 2.2uH 4040 power inductor for 5V@5A SY8205FCC buck. |
| S1 | `R31` | `73.2k 1%` | `R_0402` | SY8205 DS Fig. 2 & p.5 / USB-C VBUS decoupling | Deviation (new U10/J1 stage) | U10 FB=0.6*(1+73.2k/10k)=4.992V, EN UVLO, SS, BST, input/output caps & J1 decoupling. |
| S1 | `R32` | `10k 1%` | `R_0402` | SY8205 DS Fig. 2 & p.5 / USB-C VBUS decoupling | Deviation (new U10/J1 stage) | U10 FB=0.6*(1+73.2k/10k)=4.992V, EN UVLO, SS, BST, input/output caps & J1 decoupling. |
| S1 | `C102` | `100pF 50V C0G` | `C_0402` | SY8205 DS Fig. 2 & p.5 / USB-C VBUS decoupling | Deviation (new U10/J1 stage) | U10 FB=0.6*(1+73.2k/10k)=4.992V, EN UVLO, SS, BST, input/output caps & J1 decoupling. |
| S1 | `C85` | `22uF 10V` | `C_0603` | SY8205 DS Fig. 2 & p.5 / USB-C VBUS decoupling | Deviation (new U10/J1 stage) | U10 FB=0.6*(1+73.2k/10k)=4.992V, EN UVLO, SS, BST, input/output caps & J1 decoupling. |
| S1 | `C86` | `22uF 10V` | `C_0603` | SY8205 DS Fig. 2 & p.5 / USB-C VBUS decoupling | Deviation (new U10/J1 stage) | U10 FB=0.6*(1+73.2k/10k)=4.992V, EN UVLO, SS, BST, input/output caps & J1 decoupling. |
| S1 | `C101` | `100nF 10V` | `C_0402` | SY8205 DS Fig. 2 & p.5 / USB-C VBUS decoupling | Deviation (new U10/J1 stage) | U10 FB=0.6*(1+73.2k/10k)=4.992V, EN UVLO, SS, BST, input/output caps & J1 decoupling. |
| S1 | `J1` | `TYPE-C-31-M-12` | `TYPE-C-31-M-12` | EVB Sheet 25 p.23 (TYPE-C, USB2.0 subset) | Deviation (USB 2.0-only 16-pin TYPE-C-31-M-12 vs USB3.0 DRP on EVB) | USB 2.0 OTG0 (DP/DM), VBUS_5V, 5.1k CC1/CC2 Rd UFP pull-downs; no USB3 SS lanes. |
| S1 | `R1` | `5.1k 1%` | `R_0402` | EVB Sheet 25 p.23 (CC 5.1k Rd) | Same | USB-C UFP sink Rd pull-downs on CC1/CC2. |
| S1 | `R2` | `5.1k 1%` | `R_0402` | EVB Sheet 25 p.23 (CC 5.1k Rd) | Same | USB-C UFP sink Rd pull-downs on CC1/CC2. |
| S1 | `D2` | `SMF5.0A / 5V TVS` | `TVS_VBUS` | EVB Sheet 25 p.23 VBUS TVS | Same | Unidirectional 5.0V/6.0V VBUS TVS (SMF5.0A class). |
| S1 | `C47` | `10uF 25V` | `C_0603` | TPS2121 DS Fig. 1 & Table 6 (VREF=1.06V, RILIM=21.5k) | Deviation (new U5 mux stage) | U5 OV1/OV2/PR1 thresholds, ILIM=4.5A (21.5k), SS=100nF, ST 100k pull-up & output caps. |
| S1 | `C103` | `100nF 25V` | `C_0402` | SY8205 DS Fig. 2 & p.5 / USB-C VBUS decoupling | Deviation (new U10/J1 stage) | U10 FB=0.6*(1+73.2k/10k)=4.992V, EN UVLO, SS, BST, input/output caps & J1 decoupling. |
| S1 | `D1` | `USBLC6-2SC6` | `USBLC6-2SC6` | USBLC6-2SC6 DS; schematic_components.md §5 | Deviation (2-ch+VBUS ESD vs EVB USB3 ESD arrays) | Protects USB_CONN_DP/DN & VBUS_5V; CC1/CC2 ESD omitted (USBLC6-2SC6 covers DP/DN+VBUS). |
| S1 | `C104` | `100nF 10V` | `C_0402` | SY8205 DS Fig. 2 & p.5 / USB-C VBUS decoupling | Deviation (new U10/J1 stage) | U10 FB=0.6*(1+73.2k/10k)=4.992V, EN UVLO, SS, BST, input/output caps & J1 decoupling. |
| S1 | `R102` | `10k 1%` | `R_0402` | HDG §2.3.4 (USB2_OTG0_VBUSDET 3.0V typ) | Same | 10k/15k resistor divider from VBUS_5V -> 3.0V at RK3576 VBUSDET. |
| S1 | `R103` | `15k 1%` | `R_0402` | HDG §2.3.4 (USB2_OTG0_VBUSDET 3.0V typ) | Same | 10k/15k resistor divider from VBUS_5V -> 3.0V at RK3576 VBUSDET. |
| S1 | `C105` | `100nF 10V` | `C_0402` | SY8205 DS Fig. 2 & p.5 / USB-C VBUS decoupling | Deviation (new U10/J1 stage) | U10 FB=0.6*(1+73.2k/10k)=4.992V, EN UVLO, SS, BST, input/output caps & J1 decoupling. |
| S1 | `U5` | `TPS2121RUXR` | `TPS2121RUXR` | TPS2120/2121 DS Fig. 1, p.4, Table 6 | Deviation (EVB uses barrel/PD mux) | Auto-switching power mux selecting USB-C VBUS_5V vs VBAT_BUCK_5V -> VCC5V0_SYS_S5. |
| S1 | `C106` | `10uF 16V` | `C_0603` | TPS2121 DS Fig. 1 & Table 6 (VREF=1.06V, RILIM=21.5k) | Deviation (new U5 mux stage) | U5 OV1/OV2/PR1 thresholds, ILIM=4.5A (21.5k), SS=100nF, ST 100k pull-up & output caps. |
| S1 | `C107` | `10uF 16V` | `C_0603` | TPS2121 DS Fig. 1 & Table 6 (VREF=1.06V, RILIM=21.5k) | Deviation (new U5 mux stage) | U5 OV1/OV2/PR1 thresholds, ILIM=4.5A (21.5k), SS=100nF, ST 100k pull-up & output caps. |
| S1 | `R104` | `100k 1%` | `R_0402` | TPS2121 DS Fig. 1 & Table 6 (VREF=1.06V, RILIM=21.5k) | Deviation (new U5 mux stage) | U5 OV1/OV2/PR1 thresholds, ILIM=4.5A (21.5k), SS=100nF, ST 100k pull-up & output caps. |
| S1 | `R105` | `33k 1%` | `R_0402` | TPS2121 DS Fig. 1 & Table 6 (VREF=1.06V, RILIM=21.5k) | Deviation (new U5 mux stage) | U5 OV1/OV2/PR1 thresholds, ILIM=4.5A (21.5k), SS=100nF, ST 100k pull-up & output caps. |
| S1 | `R106` | `100k 1%` | `R_0402` | TPS2121 DS Fig. 1 & Table 6 (VREF=1.06V, RILIM=21.5k) | Deviation (new U5 mux stage) | U5 OV1/OV2/PR1 thresholds, ILIM=4.5A (21.5k), SS=100nF, ST 100k pull-up & output caps. |
| S1 | `R107` | `22k 1%` | `R_0402` | TPS2121 DS Fig. 1 & Table 6 (VREF=1.06V, RILIM=21.5k) | Deviation (new U5 mux stage) | U5 OV1/OV2/PR1 thresholds, ILIM=4.5A (21.5k), SS=100nF, ST 100k pull-up & output caps. |
| S1 | `R108` | `100k 1%` | `R_0402` | TPS2121 DS Fig. 1 & Table 6 (VREF=1.06V, RILIM=21.5k) | Deviation (new U5 mux stage) | U5 OV1/OV2/PR1 thresholds, ILIM=4.5A (21.5k), SS=100nF, ST 100k pull-up & output caps. |
| S1 | `R109` | `22k 1%` | `R_0402` | TPS2121 DS Fig. 1 & Table 6 (VREF=1.06V, RILIM=21.5k) | Deviation (new U5 mux stage) | U5 OV1/OV2/PR1 thresholds, ILIM=4.5A (21.5k), SS=100nF, ST 100k pull-up & output caps. |
| S1 | `R110` | `21.5k 1%` | `R_0402` | TPS2121 DS Fig. 1 & Table 6 (VREF=1.06V, RILIM=21.5k) | Deviation (new U5 mux stage) | U5 OV1/OV2/PR1 thresholds, ILIM=4.5A (21.5k), SS=100nF, ST 100k pull-up & output caps. |
| S1 | `C110` | `100nF 10V` | `C_0402` | TPS2121 DS Fig. 1 & Table 6 (VREF=1.06V, RILIM=21.5k) | Deviation (new U5 mux stage) | U5 OV1/OV2/PR1 thresholds, ILIM=4.5A (21.5k), SS=100nF, ST 100k pull-up & output caps. |
| S1 | `R111` | `100k 1%` | `R_0402` | TPS2121 DS Fig. 1 & Table 6 (VREF=1.06V, RILIM=21.5k) | Deviation (new U5 mux stage) | U5 OV1/OV2/PR1 thresholds, ILIM=4.5A (21.5k), SS=100nF, ST 100k pull-up & output caps. |
| S1 | `C48` | `10uF 16V` | `C_0603` | TPS2121 DS Fig. 1 & Table 6 (VREF=1.06V, RILIM=21.5k) | Deviation (new U5 mux stage) | U5 OV1/OV2/PR1 thresholds, ILIM=4.5A (21.5k), SS=100nF, ST 100k pull-up & output caps. |
| S1 | `C111` | `22uF 10V` | `C_0603` | TPS2121 DS Fig. 1 & Table 6 (VREF=1.06V, RILIM=21.5k) | Deviation (new U5 mux stage) | U5 OV1/OV2/PR1 thresholds, ILIM=4.5A (21.5k), SS=100nF, ST 100k pull-up & output caps. |
| S1 | `D3` | `PSUR1610DNV07` | `PSUR1610DNV07` | EVB Sheet 23 p.21 (D2300 'DO NOT DELETE IT!') | Same | PSUR1610DNV07 TVS protection on VCC5V0_SYS_S5. |
| S2 | `U2` | `RK806S-5` | `RK806-1` | EVB Sheet 23 p.21 (U2300A/B/C); HDG §2.2.3 | Same | RK806S-5 PMIC; I2C mode (CS->VCCA via R2324 0R); FB1/FB2 NC (internal DVS DAC mode per EVB Sheet 23 & RK806 DS p.19). |
| S2 | `L1` | `0.22uH 6.5A` | `IND_2016` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C7` | `22uF 10V` | `C_0805` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C53` | `22uF 6.3V` | `C_0603` | EVB Sheet 23 p.21 (C2307/C2308 47uF x2) / schematic_components.md C53-55 | Same (normalized to 22uF x3) | BUCK1 output bulk capacitors matching schematic_components.md C53-C55. |
| S2 | `C54` | `22uF 6.3V` | `C_0603` | EVB Sheet 23 p.21 (C2307/C2308 47uF x2) / schematic_components.md C53-55 | Same (normalized to 22uF x3) | BUCK1 output bulk capacitors matching schematic_components.md C53-C55. |
| S2 | `C55` | `22uF 6.3V` | `C_0603` | EVB Sheet 23 p.21 (C2307/C2308 47uF x2) / schematic_components.md C53-55 | Same (normalized to 22uF x3) | BUCK1 output bulk capacitors matching schematic_components.md C53-C55. |
| S2 | `R2304` | `100R 1%` | `R_0402` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C2311` | `1uF 10V` | `C_0402` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `L2` | `0.22uH 5.0A` | `IND_2016` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C8` | `22uF 10V` | `C_0805` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C56` | `22uF 6.3V` | `C_0603` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C57` | `22uF 6.3V` | `C_0603` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C58` | `22uF 6.3V` | `C_0603` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `L3` | `0.22uH 5.0A` | `IND_2016` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C9` | `22uF 10V` | `C_0805` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C59` | `22uF 6.3V` | `C_0603` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C60` | `22uF 6.3V` | `C_0603` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C61` | `22uF 6.3V` | `C_0603` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `R2314` | `100R 1%` | `R_0402` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C2334` | `1uF 10V` | `C_0402` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `L4` | `0.22uH 5.0A` | `IND_2016` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C10` | `22uF 10V` | `C_0805` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C62` | `22uF 6.3V` | `C_0603` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C63` | `22uF 6.3V` | `C_0603` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C64` | `22uF 6.3V` | `C_0603` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `L5` | `0.47uH 3.0A` | `IND_2016` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C11` | `10uF 10V` | `C_0603` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C65` | `22uF 6.3V` | `C_0603` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C66` | `22uF 6.3V` | `C_0603` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `R2302` | `49.9k 1%` | `R_0402` | EVB Sheet 23 p.21 (R2302=49.9k, R2305=100k) | Same | BUCK5 FB5 divider for 0.75V VDD_GPU_S0: 0.5*(1+49.9k/100k)=0.7495V. |
| S2 | `R2305` | `100k 1%` | `R_0402` | EVB Sheet 23 p.21 (R2302=49.9k, R2305=100k) | Same | BUCK5 FB5 divider for 0.75V VDD_GPU_S0: 0.5*(1+49.9k/100k)=0.7495V. |
| S2 | `L6` | `0.47uH 3.0A` | `IND_2016` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C12` | `10uF 10V` | `C_0603` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C67` | `22uF 6.3V` | `C_0603` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C68` | `22uF 6.3V` | `C_0603` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `R19` | `22k 1%` | `R_0402` | EVB Sheet 23 p.21 (R2308=22k, R2310=100k) | Same (fixes schematic_components.md typo) | BUCK6 FB6 divider for 0.61V LPDDR4X VDDQ_DDR_S0: 0.5*(1+22k/100k)=0.61V. |
| S2 | `R21` | `100k 1%` | `R_0402` | EVB Sheet 23 p.21 (R2308=22k, R2310=100k) | Same (fixes schematic_components.md typo) | BUCK6 FB6 divider for 0.61V LPDDR4X VDDQ_DDR_S0: 0.5*(1+22k/100k)=0.61V. |
| S2 | `C2317` | `100pF 50V C0G` | `C_0402` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `L7` | `0.47uH 3.0A` | `IND_2016` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C13` | `22uF 10V` | `C_0805` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C71` | `22uF 6.3V` | `C_0603` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C72` | `22uF 6.3V` | `C_0603` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `R2321` | `100R 1%` | `R_0402` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C2352` | `1uF 10V` | `C_0402` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `L8` | `0.47uH 3.0A` | `IND_2016` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C14` | `10uF 10V` | `C_0603` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C73` | `22uF 6.3V` | `C_0603` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C74` | `22uF 6.3V` | `C_0603` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `L9` | `0.47uH 3.0A` | `IND_2016` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C15` | `10uF 10V` | `C_0603` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C75` | `22uF 6.3V` | `C_0603` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C76` | `22uF 6.3V` | `C_0603` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `R22` | `120k 1%` | `R_0402` | EVB Sheet 23 p.21 (R2313=120k, R2315=100k) | Same (fixes schematic_components.md typo) | BUCK9 FB9 divider for 1.10V LPDDR4X VDD2_DDR_S3: 0.5*(1+120k/100k)=1.10V. |
| S2 | `R24` | `100k 1%` | `R_0402` | EVB Sheet 23 p.21 (R2313=120k, R2315=100k) | Same (fixes schematic_components.md typo) | BUCK9 FB9 divider for 1.10V LPDDR4X VDD2_DDR_S3: 0.5*(1+120k/100k)=1.10V. |
| S2 | `C2329` | `100pF 50V C0G` | `C_0402` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `L10` | `0.47uH 3.0A` | `IND_2016` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C16` | `10uF 10V` | `C_0603` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C77` | `22uF 6.3V` | `C_0603` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C78` | `22uF 6.3V` | `C_0603` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `R2320` | `100R 1%` | `R_0402` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C2351` | `1uF 10V` | `C_0402` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C35` | `1uF 6.3V` | `C_0402` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C36` | `1uF 10V` | `C_0402` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C37` | `1uF 6.3V` | `C_0402` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C38` | `1uF 6.3V` | `C_0402` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C39` | `2.2uF 6.3V` | `C_0402` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C40` | `2.2uF 6.3V` | `C_0402` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C41` | `2.2uF 6.3V` | `C_0402` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C42` | `2.2uF 6.3V` | `C_0402` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C2360` | `2.2uF 6.3V` | `C_0402` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C2363` | `2.2uF 6.3V` | `C_0402` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C2365` | `2.2uF 6.3V` | `C_0402` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C2367` | `2.2uF 6.3V` | `C_0402` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C2370` | `2.2uF 6.3V` | `C_0402` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C2372` | `2.2uF 6.3V` | `C_0402` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C2357` | `1uF 6.3V` | `C_0402` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C2361` | `4.7uF 10V` | `C_0402` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C2362` | `1uF 10V` | `C_0402` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `R2324` | `0R` | `R_0402` | EVB Sheet 23 p.21 (R2324 0R, I2C pull-ups) | Same | RK806 I2C mode select (CS->VCCA) and 10k pull-ups on I2C1_SCL/SDA. |
| S2 | `R5` | `10k 1%` | `R_0402` | EVB Sheet 23 p.21 (R2324 0R, I2C pull-ups) | Same | RK806 I2C mode select (CS->VCCA) and 10k pull-ups on I2C1_SCL/SDA. |
| S2 | `R6` | `10k 1%` | `R_0402` | EVB Sheet 23 p.21 (R2324 0R, I2C pull-ups) | Same | RK806 I2C mode select (CS->VCCA) and 10k pull-ups on I2C1_SCL/SDA. |
| S2 | `TP2318` | `TP_PWRCTRL3` | `TP_1MM` | EVB Sheet 23 p.21 (TP2318) | Same | 1.0mm SMD test pad on RK806 MISO/PWRCTRL3. |
| S2 | `C2366` | `10nF 25V` | `C_0402` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `R2330` | `200k 1%` | `R_0402` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `R2332` | `200k 1%` | `R_0402` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `C2368` | `1nF 25V C0G` | `C_0402` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `D2301` | `B5819WS` | `B5819WS` | EVB Sheet 23 p.21 (D2301) | Same | B5819WS Schottky feeding PMIC_VDC alongside R2330/R2332. |
| S2 | `C2369` | `100nF 6.3V` | `C_0402` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `R9006` | `100R 1%` | `R_0402` | EVB Sheet 23 p.21 | Same | RK806S-5 Buck/LDO/Management passive matching EVB Sheet 23. |
| S2 | `SW2` | `PWRON_KEY` | `TS-1187A-B-A-B` | EVB Sheet 28 p.26 (PWRON_KEY) | Same | TS-1187A-B-A-B power-on key pulling PWRON_L to GND via R9006. |
| S3 | `U6` | `TMI3112H` | `TMI3112H` | EVB Sheet 24 p.22 (U2400) | Same | TMI3112H pre-regulators feeding PLDO/NLDO banks (2.094V / 1.10V). |
| S3 | `C17` | `10uF 10V` | `C_0603` | EVB Sheet 24 p.22 (U2400 TMI3112H) | Same | VCC_2V0_PLDO_S3 pre-regulator passives (0.6*(1+249k/100k)=2.094V). |
| S3 | `R2405` | `100k 1%` | `R_0402` | EVB Sheet 24 p.22 (U2400 TMI3112H) | Same | VCC_2V0_PLDO_S3 pre-regulator passives (0.6*(1+249k/100k)=2.094V). |
| S3 | `L11` | `1.0uH 3.2A` | `IND_2520` | EVB Sheet 24 p.22 (U2400 TMI3112H) | Same | VCC_2V0_PLDO_S3 pre-regulator passives (0.6*(1+249k/100k)=2.094V). |
| S3 | `R25` | `249k 1%` | `R_0402` | EVB Sheet 24 p.22 (U2400 TMI3112H) | Same | VCC_2V0_PLDO_S3 pre-regulator passives (0.6*(1+249k/100k)=2.094V). |
| S3 | `R26` | `100k 1%` | `R_0402` | EVB Sheet 24 p.22 (U2400 TMI3112H) | Same | VCC_2V0_PLDO_S3 pre-regulator passives (0.6*(1+249k/100k)=2.094V). |
| S3 | `C2403` | `100pF 50V C0G` | `C_0402` | EVB Sheet 24 p.22 (U2400 TMI3112H) | Same | VCC_2V0_PLDO_S3 pre-regulator passives (0.6*(1+249k/100k)=2.094V). |
| S3 | `C79` | `22uF 6.3V` | `C_0603` | EVB Sheet 24 p.22 (U2400 TMI3112H) | Same | VCC_2V0_PLDO_S3 pre-regulator passives (0.6*(1+249k/100k)=2.094V). |
| S3 | `C2405` | `100nF 6.3V` | `C_0402` | EVB Sheet 24 p.22 (U2400 TMI3112H) | Same | VCC_2V0_PLDO_S3 pre-regulator passives (0.6*(1+249k/100k)=2.094V). |
| S3 | `U7` | `TMI3112H` | `TMI3112H` | EVB Sheet 24 p.22 (U2401) | Same | TMI3112H pre-regulators feeding PLDO/NLDO banks (2.094V / 1.10V). |
| S3 | `C18` | `10uF 10V` | `C_0603` | EVB Sheet 24 p.22 (U2401 TMI3112H) | Same | VCC_1V1_NLDO_S3 pre-regulator passives (0.6*(1+100k/120k)=1.10V). |
| S3 | `R2406` | `10k 1%` | `R_0402` | EVB Sheet 24 p.22 (U2401 TMI3112H) | Same | VCC_1V1_NLDO_S3 pre-regulator passives (0.6*(1+100k/120k)=1.10V). |
| S3 | `L12` | `1.0uH 3.2A` | `IND_2520` | EVB Sheet 24 p.22 (U2401 TMI3112H) | Same | VCC_1V1_NLDO_S3 pre-regulator passives (0.6*(1+100k/120k)=1.10V). |
| S3 | `R27` | `100k 1%` | `R_0402` | EVB Sheet 24 p.22 (U2401 TMI3112H) | Same | VCC_1V1_NLDO_S3 pre-regulator passives (0.6*(1+100k/120k)=1.10V). |
| S3 | `R28` | `120k 1%` | `R_0402` | EVB Sheet 24 p.22 (U2401 TMI3112H) | Same | VCC_1V1_NLDO_S3 pre-regulator passives (0.6*(1+100k/120k)=1.10V). |
| S3 | `C2402` | `100pF 50V C0G` | `C_0402` | EVB Sheet 24 p.22 (U2401 TMI3112H) | Same | VCC_1V1_NLDO_S3 pre-regulator passives (0.6*(1+100k/120k)=1.10V). |
| S3 | `C80` | `22uF 6.3V` | `C_0603` | EVB Sheet 24 p.22 (U2401 TMI3112H) | Same | VCC_1V1_NLDO_S3 pre-regulator passives (0.6*(1+100k/120k)=1.10V). |
| S3 | `C2407` | `100nF 6.3V` | `C_0402` | EVB Sheet 24 p.22 (U2401 TMI3112H) | Same | VCC_1V1_NLDO_S3 pre-regulator passives (0.6*(1+100k/120k)=1.10V). |
| S3 | `U9` | `CW3301` | `CW3301` | EVB Sheet 24 p.22 (U2402) | Same | CW3301 load switch for VCC_1V8_S0 (ON=U9_ON via R2411/R2413). |
| S3 | `C2410` | `10uF 6.3V` | `C_0603` | EVB Sheet 24 p.22 (U2402/U2403 load switches) | Same | VCC_1V8_S0 / VCC_3V3_S0 load switch passives. |
| S3 | `R2411` | `10k 1%` | `R_0402` | EVB Sheet 24 p.22 (U2402/U2403 load switches) | Same | VCC_1V8_S0 / VCC_3V3_S0 load switch passives. |
| S3 | `R2413` | `100k 1%` | `R_0402` | EVB Sheet 24 p.22 (U2402/U2403 load switches) | Same | VCC_1V8_S0 / VCC_3V3_S0 load switch passives. |
| S3 | `C2411` | `10uF 6.3V` | `C_0603` | EVB Sheet 24 p.22 (U2402/U2403 load switches) | Same | VCC_1V8_S0 / VCC_3V3_S0 load switch passives. |
| S3 | `U8` | `SY6280AAC` | `SY6280AAC` | EVB Sheet 24 p.22 (U2403) | Same | SY6280AAC load switch for VCC_3V3_S0 (EN=U8_EN via R2412/R2414, ISET=3.3k). |
| S3 | `C2412` | `10uF 6.3V` | `C_0603` | EVB Sheet 24 p.22 (U2402/U2403 load switches) | Same | VCC_1V8_S0 / VCC_3V3_S0 load switch passives. |
| S3 | `R2412` | `10k 1%` | `R_0402` | EVB Sheet 24 p.22 (U2402/U2403 load switches) | Same | VCC_1V8_S0 / VCC_3V3_S0 load switch passives. |
| S3 | `R2414` | `100k 1%` | `R_0402` | EVB Sheet 24 p.22 (U2402/U2403 load switches) | Same | VCC_1V8_S0 / VCC_3V3_S0 load switch passives. |
| S3 | `C2413` | `10uF 6.3V` | `C_0603` | EVB Sheet 24 p.22 (U2402/U2403 load switches) | Same | VCC_1V8_S0 / VCC_3V3_S0 load switch passives. |
| S3 | `R29` | `3.3k 1%` | `R_0402` | EVB Sheet 24 p.22 (U2402/U2403 load switches) | Same | VCC_1V8_S0 / VCC_3V3_S0 load switch passives. |
| S4,S5 | `U1` | `RK3576` | `RK3576` | EVB Sheets 10-19 (U1000); RK3576 DS Table 3-2 | Same / Partial | Only power/GND/clock/reset/boot/I2C1/UART0/USB2_OTG0 connected in SCH-1; HDMI/eDP/PCIe/MIPI CSI1-4 grounded per HDG §2.2.2; UFS/USB3_OTG0_DP_TX left unpowered/NC (unused); **RK3576 FCCSP-698L footprint UNVERIFIED vs RK3576 DS §2 package drawing**. |
| S4 | `C1000` | `100nF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1001` | `100nF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1002` | `1uF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1003` | `1uF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1004` | `1uF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1005` | `1uF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1006` | `10uF 4V` | `C_0402_BGA` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1007` | `22uF 6.3V` | `C_0603` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1009` | `100nF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1010` | `1uF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1011` | `1uF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1012` | `10uF 4V` | `C_0402_BGA` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1013` | `22uF 6.3V` | `C_0603` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1015` | `100nF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1016` | `100nF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1017` | `1uF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1018` | `1uF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1020` | `10uF 4V` | `C_0402_BGA` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1021` | `22uF 6.3V` | `C_0603` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1023` | `1uF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1024` | `100nF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1026` | `100nF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1027` | `1uF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1028` | `1uF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1029` | `10uF 4V` | `C_0402_BGA` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1030` | `22uF 6.3V` | `C_0603` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1031` | `22uF 6.3V` | `C_0603` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1039` | `22uF 6.3V` | `C_0603` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1032` | `100nF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1033` | `1uF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1034` | `1uF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1035` | `1uF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1036` | `10uF 4V` | `C_0402_BGA` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1037` | `22uF 6.3V` | `C_0603` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1038` | `22uF 6.3V` | `C_0603` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1040` | `47uF 6.3V` | `C_0805` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1200` | `100nF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1201` | `1uF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1202` | `1uF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1203` | `10uF 4V` | `C_0402_BGA` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1204` | `22uF 6.3V` | `C_0603` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1205` | `22uF 6.3V` | `C_0603` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1206` | `100nF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1207` | `1uF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1208` | `1uF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1209` | `10uF 4V` | `C_0402_BGA` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1210` | `22uF 6.3V` | `C_0603` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1211` | `22uF 6.3V` | `C_0603` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1214` | `1uF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1212` | `1uF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1213` | `1uF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1107` | `100nF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1118` | `100nF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1104` | `100nF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1117` | `100nF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1405` | `100nF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1105` | `100nF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1406` | `100nF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1509` | `1uF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1504` | `1uF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1505` | `1uF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1503` | `1uF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1506` | `1uF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1103` | `100nF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1106` | `100nF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1801` | `100nF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1308` | `1uF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1903` | `1uF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1309` | `100nF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1408` | `100nF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1901` | `1uF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `C1802` | `100nF 6.3V` | `C_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `R1202` | `0R` | `R_0402` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `R1502` | `0.1R 1%` | `R_0603` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `R1401` | `200R 1%` | `R_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S4 | `R1402` | `200R 1%` | `R_0201` | EVB Sheets 10-15, 18-19; HDG §2.2.2 | Same | RK3576 power domain decoupling / PLL filter / USB2 REXT bias per EVB. |
| S5 | `Y1` | `24.000MHz 12pF 10ppm` | `X322524MSB4SI` | EVB Sheet 11 p.11 (Y1100 24MHz) | Same | X322524MOB4SI 24 MHz crystal (12pF spec; 18pF EVB load caps). |
| S5 | `R14` | `22R 1%` | `R_0402` | EVB Sheet 11 p.11 (R1100/R1101/C1100/C1101) | Same | 24 MHz crystal load caps (18pF), feedback (510k), and series damping (22R). |
| S5 | `R37` | `510k 1%` | `R_0402` | EVB Sheet 11 p.11 (R1100/R1101/C1100/C1101) | Same | 24 MHz crystal load caps (18pF), feedback (510k), and series damping (22R). |
| S5 | `C1` | `18pF 50V C0G` | `C_0402` | EVB Sheet 11 p.11 (R1100/R1101/C1100/C1101) | Same | 24 MHz crystal load caps (18pF), feedback (510k), and series damping (22R). |
| S5 | `C2` | `18pF 50V C0G` | `C_0402` | EVB Sheet 11 p.11 (R1100/R1101/C1100/C1101) | Same | 24 MHz crystal load caps (18pF), feedback (510k), and series damping (22R). |
| S5 | `R1119` | `0.1R 1%` | `R_0603` | EVB Sheet 11 p.11 | Same | RK3576 OSC/SARADC filter, Reset pull-up, and PMIC control 0R straps. |
| S5 | `C1102` | `100nF 6.3V` | `C_0201` | EVB Sheet 11 p.11 | Same | RK3576 OSC/SARADC filter, Reset pull-up, and PMIC control 0R straps. |
| S5 | `R1147` | `0.1R 1%` | `R_0603` | EVB Sheet 11 p.11 | Same | RK3576 OSC/SARADC filter, Reset pull-up, and PMIC control 0R straps. |
| S5 | `C1116` | `100nF 6.3V` | `C_0201` | EVB Sheet 11 p.11 | Same | RK3576 OSC/SARADC filter, Reset pull-up, and PMIC control 0R straps. |
| S5 | `R16` | `10k 1%` | `R_0402` | EVB Sheet 11 p.11 & Sheet 28 p.26 (SARADC0_BOOT) | Same | MaskROM boot strap divider (10k/88.7k/1nF) + 100R key isolation. |
| S5 | `R17` | `88.7k 1%` | `R_0402` | EVB Sheet 11 p.11 & Sheet 28 p.26 (SARADC0_BOOT) | Same | MaskROM boot strap divider (10k/88.7k/1nF) + 100R key isolation. |
| S5 | `C1108` | `1nF 25V` | `C_0201` | EVB Sheet 11 p.11 & Sheet 28 p.26 (SARADC0_BOOT) | Same | MaskROM boot strap divider (10k/88.7k/1nF) + 100R key isolation. |
| S5 | `R18` | `100R 1%` | `R_0402` | EVB Sheet 11 p.11 & Sheet 28 p.26 (SARADC0_BOOT) | Same | MaskROM boot strap divider (10k/88.7k/1nF) + 100R key isolation. |
| S5 | `SW1` | `MASKROM_KEY` | `TS-1187A-B-A-B` | EVB Sheet 28 p.26 (MASKROM_KEY) | Same | TS-1187A-B-A-B MaskROM recovery key pulling SARADC_IN0_BOOT to GND via R18. |
| S5 | `R1106` | `0R` | `R_0201` | EVB Sheet 11 p.11 | Same | RK3576 OSC/SARADC filter, Reset pull-up, and PMIC control 0R straps. |
| S5 | `R1107` | `0R` | `R_0201` | EVB Sheet 11 p.11 | Same | RK3576 OSC/SARADC filter, Reset pull-up, and PMIC control 0R straps. |
| S5 | `C1119` | `100nF 6.3V` | `C_0201` | EVB Sheet 11 p.11 | Same | RK3576 OSC/SARADC filter, Reset pull-up, and PMIC control 0R straps. |
| S5 | `R1105` | `10k 1%` | `R_0402` | EVB Sheet 11 p.11 | Same | RK3576 OSC/SARADC filter, Reset pull-up, and PMIC control 0R straps. |
| S5 | `R1112` | `0R` | `R_0201` | EVB Sheet 11 p.11 | Same | RK3576 OSC/SARADC filter, Reset pull-up, and PMIC control 0R straps. |
| S5 | `R1114` | `0R` | `R_0201` | EVB Sheet 11 p.11 | Same | RK3576 OSC/SARADC filter, Reset pull-up, and PMIC control 0R straps. |
| S5 | `R1116` | `0R` | `R_0201` | EVB Sheet 11 p.11 | Same | RK3576 OSC/SARADC filter, Reset pull-up, and PMIC control 0R straps. |
| S5 | `R1122` | `0R` | `R_0201` | EVB Sheet 11 p.11 | Same | RK3576 OSC/SARADC filter, Reset pull-up, and PMIC control 0R straps. |
| S5 | `R1123` | `0R` | `R_0201` | EVB Sheet 11 p.11 | Same | RK3576 OSC/SARADC filter, Reset pull-up, and PMIC control 0R straps. |
| S5 | `R9906` | `100R 1%` | `R_0201` | EVB Sheet 29 p.27 (R9905/R9906 100R) | Same | Series 100R isolation to UART0 debug test pads. |
| S5 | `TP1` | `UART0_TX` | `TP_1MM` | EVB Sheet 29 p.27 (UART0_DEBUG) | Same | 1.0mm SMD test pads for UART0_TX_M0, UART0_RX_M0, GND. |
| S5 | `R9905` | `100R 1%` | `R_0201` | EVB Sheet 29 p.27 (R9905/R9906 100R) | Same | Series 100R isolation to UART0 debug test pads. |
| S5 | `TP2` | `UART0_RX` | `TP_1MM` | EVB Sheet 29 p.27 (UART0_DEBUG) | Same | 1.0mm SMD test pads for UART0_TX_M0, UART0_RX_M0, GND. |
| S5 | `TP3` | `UART_GND` | `TP_1MM` | EVB Sheet 29 p.27 (UART0_DEBUG) | Same | 1.0mm SMD test pads for UART0_TX_M0, UART0_RX_M0, GND. |
