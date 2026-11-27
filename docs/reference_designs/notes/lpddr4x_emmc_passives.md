# LPDDR4X and eMMC Memory Passives Reference

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
  - 1× 2.2 µF 10V X5R (0402): Sige5 `C4007`, DshanPI-A1 `C174` (connect between VDDI pin and GND).
    *(Note: The 2.2 µF value applies only to discrete-eMMC reference boards, not our eMCP. For our SK hynix H9HP52ACPMADAR eMCP, the datasheet p. 54 Table 14 is authoritative: the eMCP die package integrates an internal 1 µF capacitor, and specifies an external coupling capacitor of **0.1 µF** between VDDI and GND/VSS).*

### 2.2 Signal Pull-Up & Damping Resistors
- **`EMMC_CMD` Pull-Up:**
  - 10 kΩ 5% (0201) pull-up to `VCCIO_1V8_S0`: Sige5 `R4000`, DshanPI-A1 `R70`
- **`EMMC_CLK` Damping Resistor:**
  - 0 Ω / 22 Ω (0201) series damping resistor placed close to SoC: Sige5 `R4004`, DshanPI-A1 `R72`
- **`EMMC_DATA_STROBE` (DS):**
  - Optional 10 kΩ pull-down (unpopulated / NC by default): Sige5 `R4001`, DshanPI-A1 `R71`
- **`EMMC_RSTN`:**
  - Optional 10 kΩ pull-up (unpopulated / NC by default; internal SoC PMU pull-up active): Sige5 `R4006`, DshanPI-A1 `R74`
