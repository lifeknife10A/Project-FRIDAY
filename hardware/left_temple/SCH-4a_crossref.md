# FRIDAY SCH-4a left-temple power board

Project lead Krishna · Auditor Claude · D16 and D17 · Schematic capture for audit

[D16/D17 decisions](../../docs/plan1.md#L317) · [Interconnect](../../docs/interconnect_pinout.md#3-current-voltage-and-ir-drop-screen) · [Round 2 cell selection](../../docs/battery_cell_selection.md#L107) · [Bench qualification](../../docs/battery_bench_test.md)

## Pack, protection and current sense

| References | Value and connection | Source |
| --- | --- | --- |
| BT1, BT2 | Generic upper and lower 1S pouch tab lands with local strain-relief provisions. Upper cell from `CELL_POS` to `CELL_MID`. Lower cell from `CELL_MID` to `CELL_NEG`. The expected 300 mAh GNB LiHV cell is a bench candidate. | D16 and D17, battery selection Round 2 §§5.2–5.3. Pad size, hole fit, tab finish, strain relief and cell geometry are **UNVERIFIED** until mechanical design and cell qualification. |
| U2 | HY2120-CB. Per-cell overcharge detect 4.28 ± 0.025 V, undervoltage detect 2.90 ± 0.08 V. Discharge overcurrent sense 200 ± 30 mV and charge overcurrent sense −210 ± 30 mV. | Local HYCON HY2120 pp. 6–7 §§6–7. |
| R1, R2 | 330 Ω each. Raw positive to VDD and cell midpoint to VC, respectively. | Local HY2120 p. 10 §10 application circuit. |
| C1, C2 | 100 nF each from filtered VDD and VC to raw VSS. Selected 25 V, 0603. | Local HY2120 p. 10 §10 application circuit. Voltage rating and package are design selections. |
| R3 | 2 kΩ from `PACK-_PROT` to CS. This places the shunt contribution in the protection sense path. | Local HY2120 pp. 8–10 §§8–10, plus D17. |
| Q1 | AON5816 common-drain dual N-FET. G1 is OD and S1 is raw negative. G2 is OC and S2 leads to RS1. The common-drain pad is a local copper island. | Local HY2120 p. 10 §10 application circuit, [AON5816 pp. 1–2](../../docs/datasheets/AOS_AON5816.pdf#page=1) and [AOS package drawing p. 1](../../docs/datasheets/AOS_DFN2x5A.pdf). [AOS lifecycle lists Last Time Buy](https://www.aosmd.com/products/mosfets/lv-common-drain-battery-mosfets/aon5816). |
| F1 | Littelfuse Nano2 0451002.MRL, 2 A, 125 V, 36.7 mΩ nominal cold, 0.530 A²s nominal melting. Between raw cell positive and `PACK+_PROT`. | [Littelfuse 451/453 pp. 2–3](../../docs/datasheets/Littelfuse_Nano2_451_453.pdf#page=2), 2 A row, curve and ordering suffix. |
| RS1, TP4, TP5 | Vishay WSK2512R0500FEA, 50 mΩ ±1%, 1 W at 70 °C. The force terminals sit between Q1 and `PACK-_PROT`. TP4 and TP5 land on separate Kelvin terminals. Positive TP5 relative to TP4 on discharge. | [Vishay WSK2512 pp. 1–3](../../docs/datasheets/Vishay_WSK2512.pdf#page=1), including four-terminal package and derating, and D17. |
| J2 | Local solder lands for a keyed two-lead harness. Pin 1 is fused `PACK+_PROT`. Pin 2 is `PACK-_PROT` after both protection FETs and the shunt. | D16/D17 and [protected harness pin table](../interconnect/pinout_split_pack.csv). Mating hardware, polarizing feature and current-carrying geometry are **UNVERIFIED**. |

At 1.5 A, RS1 reads **75 mV** and dissipates **0.1125 W** nominal. At 3 A, it reads **150 mV** and dissipates **0.45 W**. The fuse runs at 75% of rating for 1.5 A and 150% for 3 A. Its nominal cold resistance adds about **55 mV** and **110 mV** respectively, before heating. The fuse datasheet specifies a minimum four-hour opening time at 100% and maximum five seconds at 200% for this rating. The 3 A result depends on pulse duration, ambient, PCB temperature and repetition. The Round 2 cell test uses 3 A for 10 s. Fuse and protector coordination must be checked separately with a protected-pack fixture.

At 3 A the shunt alone produces 150 mV. Using the AON5816 p. 2 per-device 6.5 mΩ maximum at 4.5 V gate drive for a room-temperature screen, the two channel drops add at most about 39 mV under those conditions. The combined **189 mV** screen lies inside the protector’s **170–230 mV** detection band. Gate drive, component variation, temperature and copper resistance can shift the trip. The design therefore does not guarantee that a 3 A board pulse survives, or establish exact trip current. D17's operating screen remains 1.5 A continuous.

## Charger, balance and thermal sense

| References | Value and connection | Source |
| --- | --- | --- |
| U1 | IP2326_NPD V1.6. Pin 13 VIN from `VBUS_OR` through R4. LX 15–17 to L1 and C5. VSYS 19/20 to C6/C7. VOUT 21/22 to fused positive. PGND 18, EP and VBAT_GND 24 to the protected return. | [Injoinic pp. 2, 10, 14 and 17](../../docs/datasheets/Injoinic_IP2326_V1.6.pdf#page=2), pin table, balance, application and package. Figure 5 connects balance return pin 24 to `BAT1-`, on the external side of its low-side protection. |
| U1 options | VSET 3 and CON_SEL 10 open for nominal 8.4 V and 2S. OVSET 9 open for 8.75 V typical secondary charger OVP. DM/DP open for 5 V-only operation. LED output is unused because the charge-state interface uses BAT_STAT. | [Injoinic pp. 2, 10, 12–14](../../docs/datasheets/Injoinic_IP2326_V1.6.pdf#page=10). |
| R4, C3, C4 | 0.5 Ω, 5% input series resistor to pin 13, with 10 µF/25 V at each end. L1 takes boost power directly from the OR node. | [Injoinic pp. 14–15](../../docs/datasheets/Injoinic_IP2326_V1.6.pdf#page=14), Fig. 5 R1, C1 and C3. 1206 is selected for ceramic effective capacitance under bias. |
| R5 | 450 kΩ, 1%, at pin 11 ISET. `I_CHG [mA] = 90000 / R_ISET [kΩ] = 90000 / 450 = 200 mA`. This supersedes the 300 kΩ project BOM entry. | [Injoinic p. 11](../../docs/datasheets/Injoinic_IP2326_V1.6.pdf#page=11), which calls for the NPD variant below 700 mA. |
| R6, R7 | 120 kΩ sets the nominal 12 h safety timeout. 68 kΩ sets 4.35 V typical VIN undervoltage regulation. Both 1%. | [Injoinic pp. 11–12 and 14](../../docs/datasheets/Injoinic_IP2326_V1.6.pdf#page=11), ROT and RUV tables. |
| TH1, R8 | Pack-mounted HNT-GR1 family thermistor, 100 kΩ at 25 °C, B25/50 4100 K, in parallel with 82 kΩ 1% from pin 4 to protected return. Example thresholds are 0 °C stop cold, 45 °C half current and 55 °C stop hot. | [Injoinic p. 13](../../docs/datasheets/Injoinic_IP2326_V1.6.pdf#page=13) and [Hokuriku HNT-GR pp. 1, 4](../../docs/datasheets/Hokuriku_HNT-GR.pdf#page=4). Exact lead finish, tolerance, orderable thermistor suffix and pack-specific thermal limits await qualification. |
| L1 | Coilcraft XAL5030-222MEC, 2.2 µH, DCR 14.5 mΩ maximum, 9.2 A typical saturation and 7.2 A typical RMS at 20 °C rise. | Injoinic pp. 14–15 requires 2.2 µH, less than 20 mΩ DCR and above 5 A for Isat and temperature rise. [Coilcraft XAL50xx p. 1](../../docs/datasheets/Coilcraft_XAL50xx.pdf). |
| C5 | 100 nF/25 V X7R between BST 14 and LX. | Injoinic pp. 2, 14–15, reference C2. |
| C6, C7 | Two 22 µF/25 V X7R in parallel between VSYS and protected return. | Injoinic pp. 2, 14–15, reference C4/C5. Verify 1206 DC bias at VSYS. |
| C8, C9 | Two 10 µF/25 V X7R in parallel between fused output and protected return. | Injoinic pp. 14–15, reference C6/C7. Verify 1206 DC bias at pack voltage. |
| C10, C11 | 100 nF/25 V X7R each from VOUT and VBATM to pin 24 protected return, respectively. | Injoinic pp. 14–15, balance bypasses. |
| Q2, R9, R10 | AO3401A P-FET in the midpoint sense path. Drain to `CELL_MID`, source toward R11, gate pulled toward protected return with 5.1 kΩ and referenced to source with 3.1 MΩ. Both resistors 5%. | Injoinic pp. 14–15 Figure 5 Q1, R6 and R7, and [AOS AO3401A pp. 1–2](../../docs/datasheets/AOS_AO3401A.pdf#page=1). |
| R11 | 120 Ω 1%, 0.25 W, from Q2 source to VBATM 23. At 4.20 V its ideal bleed bound is 35 mA. At 4.25 V and −1% resistance the bound is 35.8 mA and 0.152 W, before internal path losses. | Injoinic p. 10 requires RCB greater than 100 Ω and balance current below 40 mA. Typical balance turn-on is 4.1 V. Values and power class are calculation-based selections. |

During charge the positive path is U1 VOUT → `PACK+_PROT` → F1 → cells. Return runs through Q1 and RS1 to the charger's protected `BAT1-` equivalent. Pin 24 senses this protected return. The upper and lower cell imbalance must be checked with this protection and shunt drop present.

**Charge release limit.** With VSET open the electrical table gives **8.3–8.5 V** for the 2S CV setting. The selected setting targets **4.20 V nominal per cell** when balanced. The specified CV tolerance allows a cell voltage above 4.20 V. HY2120-CB backup overvoltage detection is higher. The generic charger description also gives 200 mA typical CV cutoff with a 30 s interval, which overlaps the requested 200 mA setting. Verify actual NPD termination, recharge and both cell terminal voltages before using cells. If 4.20 V/cell is a strict ceiling, the pack requires a verified limit or an alternate charge setting/architecture approved by Krishna. The NTC limits must also agree with the qualified cell. [Injoinic pp. 4, 9–11 and 13](../../docs/datasheets/Injoinic_IP2326_V1.6.pdf#page=4)

## Input OR, connectors and controls

| References | Value and connection | Source |
| --- | --- | --- |
| U3, U4 | TI TPS259470ARPW auto-retry eFuses, one on each incoming rail. Both outputs join `VBUS_OR`. The 470 option provides active reverse blocking and adjustable OVLO. AUXOFF and FLT open. ITIMER open on each branch. | [TI TPS25947 pp. 4–7, 29–32, 34–35, 46–48 and 73](../../docs/datasheets/TI_TPS25947.pdf#page=4), options, pin functions, overcurrent, reverse blocking, active OR and RPW PCB example. |
| D1, D2 | SMF6.0A unidirectional TVS. Cathode on the raw input, anode to protected return. 6.0 V standoff and 10.3 V specified clamp under the datasheet test condition. | [Littelfuse SMF pp. 1–2, 5](../../docs/datasheets/Littelfuse_SMF.pdf#page=2). OVP disconnect is supplied separately by each eFuse. |
| R12/R13, R17/R18 | 374 kΩ top and 150 kΩ bottom, 1%. UVLO rising ≈4.19 V using the 1.20 V typical comparator threshold. | TI pp. 7, 9, 28, UVLO thresholds and equation. |
| R14/R15, R19/R20 | 365 kΩ top and 100 kΩ bottom, 1%. OVLO rising ≈5.58 V typical. | TI pp. 7–9, 28, OVLO thresholds, divider equation and reverse-input guidance. |
| R16, R21 | 6.04 kΩ, 1% each. Eq. 7 sets approximately 3334 / 6040 = 0.552 A typical branch current limit. | TI pp. 9, 31–32. The 0.50 A auxiliary route allocation is a separate right-board branch target. Verify worst-case current limit, insertion transient and sharing rather than identifying 0.552 A as a guaranteed maximum. |
| C12, C14 | 1 µF/25 V X7R at each IN terminal. | TI pp. 60–63, input bypass and cable-transient guidance. |
| C13, C15 | 1 nF/25 V C0G on each DVDT. Eq. 4 gives roughly 2 V/ms nominal, a design setting for input insertion. | TI pp. 29, 44, slew-rate control. |
| J1 | EDAC 686E0321250110E mates with 685E0321350120E. Three contacts at 2.7 mm pitch, gold flash over nickel. Drawing rates each contact at 12 V and 2 A. FRIDAY logical assignment pin 1 VBUS, pin 2 protected return, pin 3 DET. | Local EDAC drawings p. 1 each. Both magnets key the pair. Pogo land drill, mounting, reference face and polarity through the docking cable need a mechanical continuity check before assembly. |
| Q3, R22, R23 | DMN2058U-7 open-drain dock detect. Dock-sourced DET passes through 47 kΩ to the insulated gate with a 100 kΩ pulldown. A 5 V dock drives roughly 3.4 V at the gate and pulls J3.10 low. On the right, VCCIO7 pulls the line to 1.8 V when the dock is absent. | [Diodes DMN2058U pp. 1–2, 6](../../docs/datasheets/Diodes_DMN2058U.pdf#page=1), and interconnect §2. Resistors 1%, design-selected. |
| Q4, R24, R25 | DMN2058U-7 open-drain BAT_STAT inverter. Gate fed through 4.7 kΩ with 1 MΩ pulldown, both 1%. Injoinic describes BAT_STAT low in trickle and high after entering constant-current charge. Validate its voltage and idle behavior on actual NPD silicon. | Injoinic pp. 2, 13 and Diodes pp. 1–2, 6. |
| Q5, R26–R28 | DMN2058U-7 sinks U1 EN with a high right-hand `CHG_EN`. 4.7 kΩ series gate, 1 MΩ gate pulldown and 5.1 kΩ EN pullup to `VBUS_OR`, all 1%. Low or absent right-hand drive permits charge whenever a valid input is present. | Injoinic pp. 2, 14 for EN, Diodes pp. 1–2, 6 and interconnect §2. Resistors are design selections. |
| J3 | Hirose FH12-24S-0.5SH(55). Pins 19–21 are USB charge input. Pins 22–24 are its return contacts. Pins 10/12/13 carry dock/status/enable, 15–17 open. Pin 1 is at negative X on the stock footprint, bottom-contact copper down, right pin 1 to left pin 1. | [Interconnect pin table](../interconnect/pinout_right_left_aux.csv), [library pads](../../libraries/FH12-24S-0.5SH_55_.lbr#L103) and [Hirose FH12 catalog p. 2](https://www.hirose.com/en/product/series/FH12). |
| TP1–TP3, TP6–TP8 | TP1/TP2 fused-positive and protected-negative harness nodes. TP3 raw midpoint. TP6 OR supply. TP7 LX switching node. TP8 NTC input. Generic 1 mm pads. | D17 and [existing FRIDAY test-land library](../../libraries/FRIDAY_SCH1_Support.lbr#L196). |

AUX ground and pogo ground share `PACK-_PROT`. Intended exposed driven voltages come from the dock or right board. The right board also connects J4 negative to its ground plane, so the mated auxiliary-ground path is electrically in parallel with the harness negative. A harness-open or high-resistance return could send system current through the auxiliary flex. Test that fault and resolve any excess return current as part of the right-board design.

### Native ERC and topology checks

[ERC and printed topology checks](out/FRIDAY_Left_SCH4a_ERC.txt) · [Native PDF](out/SCH-4a.pdf) · [Native text netlist](out/FRIDAY_Left_SCH4a_netlist.txt) · [CSV netlist](out/FRIDAY_Left_SCH4a_netlist.csv) · [BOM](out/FRIDAY_Left_SCH4a_BOM.csv)

Fusion returned zero errors, five active code 106 warnings and zero warning approvals. Q1 common drain is a local exposed-pad island. The other four warnings come from the SAI1 and amp shutdown terminals reserved on J3 for later audio capture.

The checker compares every physical connected pad against the source and verifies the harness, fusing, return path, charger input, ISET and shunt. Its directed DC source model permits a conservative internal charger back path even with VIN absent, then confirms that neither raw positive, fused positive nor midpoint can source a non-return pogo or auxiliary terminal. Pogo pin 2 and auxiliary grounds are the shared protected return. Isolation under hot plug, ESD, failed parts and unintended external connections requires bench verification.

### Compute SCH-1/2 change list

1. Branch right J1 `VBUS_5V` upstream of TPS2121 U5 IN1 into a separately protected, current-limited `VBUS_5V_CHG` path to auxiliary pins 19–21. Keep USB D+/D− and CC local. Coordinate the provisional 0.50 A charger allocation with total USB source current, flash demand, source detection, the three-return flex and U4 startup. Verify the pack cannot energize right USB VBUS.
2. Route J3.10 to GPIO4_D0 (1AD2) and J3.12 to GPIO4_D1 (AK4). Bring each up to VCCIO7 at 1.8 V with candidate 10 kΩ pull-ups. Route J3.13 to GPIO0_A7 (1U21) as open drain with a candidate 4.7 kΩ pull-up to PMUIO0 at 1.8 V. Define boot, sleep and power-off states with firmware. Verify the polarity and behavior of all three lines. [I/O bank map](../compute_board/io_bank_map.md#L7)
3. Add a pack-monitor divider from right J4 `VBAT_2S_IN` to a spare SARADC input, with `SARADC_IN2` (1B19) the candidate. Keep the boot and recovery inputs for their existing roles. A provisional 150 kΩ/33 kΩ divider produces 1.53 V at 8.5 V nominal. Check tolerance, input injection when the ADC rail is off, sampling impedance, filtering, calibration and fault maximum before capture. Use a switched divider or buffer if the input power-off limits require it. [RK3576 HDG PDF pp. 85–86](../../docs/datasheets/Rockchip%20RK3576%20Hardware%20Design%20Guide.pdf#page=85) · [RK3576 library mapping](../../libraries/RK3576.lbr#L1803) · [SCH-2 netlist](../compute_board/out/FRIDAY_Compute_SCH2_netlist.csv#L1013)
4. Keep the physical pack pair on J4 with keyed pin 1 positive and pin 2 return. Qualify current division and safe shutdown if either pack conductor opens while the auxiliary flex or a USB source is attached. Existing J4 and SY8205 VIN stay on `VBAT_2S_IN`. [SCH-2 netlist](../compute_board/out/FRIDAY_Compute_SCH2_netlist.csv#L1013)

### Open items for Krishna

1. Approve the cell after Round 2 bench qualification. Confirm exact tab/strain relief, thermal limits and the 4.20 V/cell requirement against the charger's specified tolerance and real NPD termination behavior.
2. Approve a pulse envelope after fuse/protector coordination and shunt temperature testing. Confirm AON5816 availability or qualify a replacement before release.
3. Confirm dock pin face/keying, harness return behavior and USB input budget before board release. Measure both input sources independently and together, reverse leakage, powered-off GPIO behavior and short/unplug conditions.
4. Review the custom footprints against manufacturer land and paste drawings before PCB export. In particular verify QFN EP paste, TI RPW stepped lands, Vishay Kelvin land geometry, actual EDAC board fit and the generic tab pads. The schematic records terminal assignments for audit.

### Restricted datasheets on the workstation

The originals remain in the ignored `references_local/SCH-4a_preflight/` directory.

| Local file inside that directory | Pages used | SHA-256 |
| --- | --- | --- |
| HY2120.pdf | 6–10 | `844f87e84a0b25dcf434852dba31442e03db3767d25b508c09533ea08ee5b15b` |
| EDAC-686E0321250110E.pdf | 1 | `e415b80ade0a00fc43a168c98f721b5d79b3361e99c43f8e0ca915fff2c75ce8` |
| EDAC-685E0321350120E.pdf | 1 | `b7b8201ac3c27242d194b8429f8486d9c16f847ecd01be74a23d76bb9b694629` |
