# RK3576 & RK806S-5 Power Architecture Comparison

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

Across all reference designs and FRIDAY SCH-1, the PMIC core topology and rail assignments match:
- **I2C Control Mode:** Pin 18 (`CS`) tied to Pin 21 (`VCCA`) via 0 Ω resistor (`R2324`); 10 kΩ pull-ups on I2C bus (`R5`, `R6`) to `VCCA1V8_PLDO6_S3` / `VCCIO6_1V8`.
- **Buck Inductance & Capacitance:**
  - BUCK1, BUCK2, BUCK3: 0.22 µH inductors (`L1`, `L2`, `L3` / 2016 size, e.g. TFM201610ALM-R22MTAA) with 2× 22 µF + 2× 10 µF output caps.
  - BUCK4, BUCK5, BUCK6, BUCK7, BUCK8, BUCK9, BUCK10: 0.47 µH inductors (`L4`–`L10` / 2016 size) with 1× 22 µF + 2× 10 µF output caps.
- **Buck Rail Assignments & External Feedback Dividers:**
  - `BUCK1` (`VDD_CPU_BIG_S0`): Internal DVS, feeds Cortex-A72 Big cluster cores.
  - `BUCK2` (`VDD_NPU_S0`): Internal DVS, feeds RK3576 NPU core.
  - `BUCK3` (`VDD_CPU_LIT_S0`): Internal DVS, feeds Cortex-A53 Little cluster cores.
  - `BUCK4` (`VCC_3V3_S3`): 3.30 V fixed.
  - `BUCK5` (`VDD_GPU_S0`): R_top (`R2302`) = 49.9 kΩ, R_bot (`R2305`) = 100 kΩ -> 0.75 V nominal (matches EVB R2302/R2305, Sige5 sheet 12).
  - `BUCK6` (`VDDQ_DDR_S0`): R_top (`R19`) = 22 kΩ, R_bot (`R21`) = 100 kΩ -> 0.61 V nominal (matches EVB R2308/R2310, Sige5 sheet 12).
  - `BUCK7` (`VDD_LOGIC_S0`): Internal DVS, feeds RK3576 main logic.
  - `BUCK8` (`VCC_1V8_S3`): 1.80 V fixed.
  - `BUCK9` (`VDD2_DDR_S3` / `VDDQ_DDR_CKE_S3`): R_top (`R22`) = 120 kΩ, R_bot (`R24`) = 100 kΩ -> 1.10 V nominal (matches EVB R2313/R2315, Sige5 sheet 12; feeds eMCP LPDDR4X VDD2 and SoC DDR PHY CKE).
  - `BUCK10` (`VDD_DDR_S0`): Internal DVS, feeds RK3576 DDR controller/PHY core logic.
- **PLDO & NLDO Decoupling:**
  - PLDO1–6 and NLDO1–5 decoupling capacitor values (1.0 µF to 4.7 µF) are completely identical between Sige5 sheet 12, EVB1 sheet 23, and FRIDAY SCH-1 sheet S2.

---

## 3. Discrete Power (U6, U7, U8, U9) Comparison

Both ArmSoM Sige5 (sheet 13) and Project FRIDAY (sheet S3) utilize the exact same discrete power topology:
- **`U6` (TMI3112H):** `VCC_2V0_PLDO_S3` (2.10 V @ 2A buck, FB: `R25` = 249 kΩ 1% / `R26` = 100 kΩ 1%) providing input power to PMIC PLDOs (`U2.VCC11`).
- **`U7` (TMI3112H):** `VCC_1V1_NLDO_S3` (1.10 V @ 2A buck, FB: `R27` = 100 kΩ 1% / `R28` = 120 kΩ 1%) providing input power to PMIC NLDOs only (`U2.VCC13`, `U2.VCC14`).
  *(Note: eMCP VDD2 is NOT powered by U7; it is powered by PMIC BUCK9 `VDD2_DDR_S3` per SCH-1 netlist).*
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
