# FRIDAY SCH-3 front-bridge camera board

Project lead Krishna · Auditor Claude · Schematic capture for audit

[Preflight sources](SCH-3_sources.md) · [Interconnect pin table](../interconnect/pinout_right_bridge.csv) · [D16/D17](../../docs/plan1.md#L317)

## Connector and CSI

| References | Value and connection | Source |
| --- | --- | --- |
| J2 | Hirose FH12-24S-0.5SH(55). All 24 numbered contacts follow the right–bridge CSV. Pin 1 is at the negative-X end of the unrotated PCB land row. Bottom contacts require exposed copper down at the receptacles. The flex must connect pin 1 to pin 1. Mechanical tabs are open in this schematic. | [Interconnect §2](../../docs/interconnect_pinout.md#2-signals-and-end-orientation), [J2 CSV](../interconnect/pinout_right_bridge.csv), [FH12-24 library](../../libraries/FH12-24S-0.5SH_55_.lbr#L103) and [Hirose product specification](https://www.hirose.com/en/product/p/CL0586-0521-0-55) |
| J1 | DF37NC-30DS-0.4V(51). All 30 contacts open for the **UNPROVEN** crosswalk. RP logical 1/10 share 2.8 V, 3 uses 1.8 V, and 4/11 share 1.1 V. No physical pad assignment is implied. | [RP-008969-SD p. 2 J2](../../docs/datasheets/Raspberry%20Pi%20Camera%20Module%203%20Schematic.pdf#page=2), [Hirose DF37 pp. 2–3, 6](../../docs/datasheets/Hirose_DF37_Series.pdf#page=2), [crosswalk and evidence needed](df37_crosswalk.md) |
| L2, L3, L4 | Murata DLP11SN900HL2L, 90 Ω common-mode impedance at 100 MHz. One each on D0, D1 and CLK. Winding 1→2 carries N and 4→3 carries P. J2-side net names match both CSVs. The separate `_SENSOR` nodes end at the chokes. | RP-008969-SD p. 2 L2–L4 and [Murata pp. 1–2, 4–5](../../docs/datasheets/Murata_DLP11SN900HL2L.pdf#page=1). The RP Rev R1 choke is the schematic reference. Confirm stock or qualify a replacement before ordering. |

Use 100 Ω differential or the HDG's 95 Ω fallback where stack-up limits apply. The reference calls for intra-pair skew below 6 mil, lane-to-clock mismatch below 12 mil, length below 6 in and up to four vias. Apply these as route targets, with a continuous return and no probe stubs on the pairs. Verify the controlled-impedance assembly, choke bandwidth and eye at the actual IMX708 lane rate. [RK3576 HDG PDF p. 243, Table 3-30](../../docs/datasheets/Rockchip%20RK3576%20Hardware%20Design%20Guide.pdf#page=243)

## Camera power and enable

| References | Value and connection | Source |
| --- | --- | --- |
| U1 | Diodes AP3429KTTR-G1, 2 A synchronous converter. This is the documented five-pin AP3429 substitute for the six-pin AP3429K symbol in RP U11. Input range 2.7–5.5 V. The bridge uses an independent POR in place of the RP buck PG pin. | [Diodes AP3429 pp. 1–2, 5, 9–10](../../docs/datasheets/Diodes_AP3429.pdf#page=1), RP p. 2 U11 |
| L1 | Coilcraft XFL4020-222MEC, 2.2 µH, 23.5 mΩ maximum DCR and 3.1 A typical at 10% inductance loss. | [Coilcraft XFL4020 p. 1](../../docs/datasheets/Coilcraft_XFL4020.pdf) · AP3429 p. 2 and RP p. 2 L1 specify 2.2 µH |
| R1, R2 | 20 kΩ and 24 kΩ, 0.1%. Feedback sets `0.600 × (1 + 20 / 24) = 1.100 V` typical. At 0.2 µA specified feedback leakage the 20 kΩ top resistor contributes up to 4 mV. | AP3429 pp. 2 and 5. Divider is a design selection for the 1.1 V RP target. |
| C1–C3 | 22 µF/10 V X7R input, plus two 22 µF/10 V X7R output in parallel. | AP3429 p. 2 typical application. Verify effective capacitance under bias with chosen MLCCs. |
| C4 | 330 pF/25 V C0G from DVDD to FB. Maintaining the datasheet example's approximate feed-forward zero gives `300 kΩ × 22 pF / 20 kΩ = 330 pF`. Confirm loop and load-step response on the assembled alternative. | AP3429 p. 2, 300 kΩ and 22 pF example. |
| U2 and U3 | AP7331-28WG-7 and AP7331-18WG-7, 300 mA rated. U2 provides both camera AVDD and AFVDD from one 2.8 V output. U3 provides local 1.8 V camera DOVDD. Both use `VCC_3V3_S3`. | [Diodes AP7331 pp. 1–4, 8–11](../../docs/datasheets/Diodes_AP7331.pdf#page=1), RP p. 2 U1/U2, J2 |
| C5–C8 | 1 µF/16 V X5R on each LDO input and output. | AP7331 pp. 2, 4 and 8, RP p. 2 C5/C6/C11/C12. Confirm effective bias and temp capacitance at the selected package. |
| U4, R3, R4, C9 | SN74LV1T34DBVR shifts 1.8 V `CAM_ENABLE` to the 3.3 V local level. 100 kΩ 1% pulldowns on input/output, 100 nF/16 V X7R bypass. Measured host VOH must clear the 1.39 V high threshold at 3.0–3.3 V VCC and the 1.48 V limit listed at 3.6 V. The translated rail enables U1–U3 and releases supervisor manual reset. | [TI SN74LV1T34 pp. 4, 6, 11 and 13](../../docs/datasheets/TI_SN74LV1T34.pdf#page=4). AP3429 p. 5 EN ≥1.5 V and AP7331 p. 4 EN ≥1.4 V. Pulldowns are design selections. |
| C10–C13 | Local sensor-end bypass. 1 µF/16 V at DVDD, 1 µF/16 V and 100 nF/25 V at shared AVDD/AFVDD, 1 µF/16 V at DOVDD. | RP p. 2 C3, C2/C14 and C4. |

The common enable follows RP p. 2, with all three camera regulators started by the same signal and their natural ramp rates. The local 1.8 V camera supply follows the Pi power-domain arrangement and leaves the host 1.8 V rail for the microphones. The bridge holds XCLR while the rails settle and while the oscillator starts. The RP sheet shows this sequencing approach. The sensor-level rail order and ramp limits still need verification for the exact assembly. The bridge uses direct 3.3 V feeds with local input bypass in this capture. Review whether the RP input beads FB1/FB2 are needed with the selected host source and flex during conducted-noise and load-step validation.

### 3.3 V current screen

The RP p. 2 design ceilings are 0.60 A at 1.1 V, 0.05 A at the shared 2.8 V supply and 0.05 A on camera 1.8 V. Treat these as budgeting ceilings. Allow a further 6 mA for the oscillator and 1 mA for supervisor, reference dividers, pull-ups and enable overhead. The 2.8 V budget covers both AVDD and AFVDD together. Confirm AF transient demand on the actual unit. [RP p. 2](../../docs/datasheets/Raspberry%20Pi%20Camera%20Module%203%20Schematic.pdf#page=2) · [SiTime pp. 1–3](../../docs/datasheets/SiTime_SiT1602B.pdf#page=1)

At 0.350 A the provisional 0.228 Ω loop model gives 79.8 mV drop, or 0.175 A per power and designated return contact under equal sharing. Using 85% assumed buck efficiency, the input estimate is `0.660 W / (Vbridge × 0.85) + 0.107 A`. A 3.300 V source gives about **348 mA**. The 3.135 V engineering screen corner gives about **361 mA**, above the **350 mA** allocation. Startup, transient loading and actual conductor sharing remain **UNVERIFIED**. Pi's two logical DVDD pins could each carry 0.30 A at the 0.60 A ceiling with equal sharing. That equals the Hirose per-contact rating and exceeds the 0.15 A derated design screen. Verify the current over the actual factory contacts before using J1. [Interconnect §3](../../docs/interconnect_pinout.md#3-current-voltage-and-ir-drop-screen) · [Hirose DF37 p. 2](../../docs/datasheets/Hirose_DF37_Series.pdf#page=2)

## MCLK, POR and I²C

| References | Value and connection | Source |
| --- | --- | --- |
| X1, R5, C14 | 24 MHz SiT1602BI-71-18E-24.000000D, 1.8 V OE variant with OE and VDD on local DOVDD. 22 Ω series and 1 µF/16 V X5R bypass. | [SiTime pp. 1–4, 10, 13](../../docs/datasheets/SiTime_SiT1602B.pdf#page=2) and RP p. 2 X1/R3/C9 |
| U5 and C15 | TPS386000RGPR from 3.3 V with 100 nF/16 V X7R bypass. RESET1–RESET3 are open drain and share XCLR. MR follows translated enable, so enable low asserts RESET1. CT1–CT3 open select the 14–24 ms guaranteed window. Both unused sense-4 inputs and WDI at ground. RESET4, WDO, VREF and CT4 open. Pin 11 and EP ground per TI. | [TI TPS386000 pp. 4–8, 25–29 and 37](../../docs/datasheets/TI_TPS386000.pdf#page=4). This supervisor implements the reset-after-clock intent of RP p. 2 R30/R31/C13. |
| R6/R7, R8/R9, R10/R11 | 15.4 kΩ/10 kΩ for DVDD, 32.4 kΩ/10 kΩ for DOVDD, 54.9 kΩ/10 kΩ for AVDD/AFVDD. All 0.1%. Rising thresholds are 1.013–1.053 V, 1.690–1.759 V and 2.587–2.693 V, respectively. | TI pp. 7 and 25–26. Calculation combines 396–404 mV falling threshold, 3.5–10 mV hysteresis, resistor tolerance and ±25 nA sense leakage. |
| R12 | 10 kΩ 1% XCLR pull-up to local DOVDD. U5 sinks this net during reset. | TI p. 5 open-drain requirement and RP p. 2 R31 nominal 10 kΩ. |
| R13, R14 | 0 Ω DNP host MCLK and reset options. For host MCLK, remove fitted R5 and revalidate the reset timing before installing R13. If installing R14, use an open-drain host reset output. | Project interconnect J2 pins 14–15. Both DNP states are verified in Fusion's exported schematic. |
| R15, R16 | 2.2 kΩ each, 1%, from bridge-local DOVDD to camera SCL/SDA. Install pull-ups at this bridge only. | RP p. 2 R1/R2 and [NXP UM10204 pp. 42–43, 50](../../docs/datasheets/NXP_UM10204.pdf#page=42). |

**Reset timing.** U5 releases XCLR after the last active reset timer expires. Even at the low DOVDD trip bound of 1.690 V, its timer starts above the oscillator's 1.62 V rated minimum. With OE tied high to that rail, X1 takes at most 5 ms to start. U5's 14 ms minimum delay gives **9 ms minimum margin** for a healthy local oscillator and normal supply ramps. Measure MCLK, all three rails and XCLR under cold/warm start and interruption. This timing circuit does not independently detect a failed clock. [SiTime p. 2](../../docs/datasheets/SiTime_SiT1602B.pdf#page=2) · [TI TPS386000 pp. 7–8](../../docs/datasheets/TI_TPS386000.pdf#page=7)

**I²C rise time.** For 65 mm of flex, a screening estimate using 50 Ω single-ended with effective dielectric constant 3 gives about 7.5 pF of flex capacitance. Allow 40 pF for up to four I/O loads at the UM10204 10 pF limit and 20 pF for transitions and board trace, rounded to **70 pF unverified** per line. With 2.222 kΩ worst-case resistance, `tr = 0.8473 × R × C ≈ 132 ns`. The 300 ns Fast-mode limit gives a modeled **159 pF** ceiling. Measure rise time and actual sink behavior with the final assembly. Keep host I²C open drain with internal pulls disabled and no drive while camera DOVDD is off. [Interconnect flex estimate](../../docs/interconnect_pinout.md#1-boards-and-physical-links) · [NXP UM10204 pp. 42–43, 50](../../docs/datasheets/NXP_UM10204.pdf#page=50)

## Microphones and probes

| References | Value and connection | Source |
| --- | --- | --- |
| MK1, MK2 | INMP441 on `VCC_1V8_S0` with CHIPEN high. MK1 L/R low, MK2 L/R high. Share SCK, WS and SD. Host uses 64 BCLK periods per stereo frame. Supply budget 1.6 mA max per mic at 1.8 V. | [INMP441 pp. 5, 8, 11–12](../../docs/datasheets/INMP441%20Datasheet.pdf#page=5), [Y3 and VCCIO2](../compute_board/io_bank_map.md#L11) |
| C16, C17, R17 | 100 nF/16 V X7R at each VDD/pin 6 return and one 100 kΩ 1% pulldown on common SD. | INMP441 pp. 8, 11 (Fig. 7), 12 and 15. |
| TP1–TP3 | DVDD, shared AVDD/AFVDD and local DOVDD. | SCH-3 rail-probe requirement, RP p. 2 |
| TP4–TP6, TP10 | MCLK, XCLR, raw CAM_ENABLE and shared audio SD. | SCH-3 probe requirement and [FRIDAY 1 mm pad library](../../libraries/FRIDAY_SCH1_Support.lbr#L196) |
| TP7–TP9 | J2 pin 15 host clock, pin 14 host reset, pin 16 cradle NTC reservation. NTC is a test land only. | [Right–bridge CSV](../interconnect/pinout_right_bridge.csv) |

Use the bottom-port land pattern and align the PCB and enclosure acoustic openings. Keep solder paste, debris, adhesive and gasket compression clear of the port according to INMP441 pp. 15–17. Review the custom schematic footprints against the manufacturer assembly drawings during PCB release, including QFN EP paste, oscillator pad orientation and the mic acoustic opening.

## ERC and downstream changes

Fusion returned **0 errors, 8 active warnings and 0 approvals**. Six warnings are the deliberate sensor-side choke endpoints. Two are the INMP441 VDD names on the project 1.8 V rail. The checker matched **36 nets and 171 physical pads** with the generated source.

[PDF](out/SCH-3.pdf) · [Netlist CSV](out/FRIDAY_Bridge_SCH3_netlist.csv) · [Netlist TXT](out/FRIDAY_Bridge_SCH3_netlist.txt) · [BOM](out/FRIDAY_Bridge_SCH3_BOM.csv) · [ERC and script checks](out/FRIDAY_Bridge_SCH3_ERC.txt)

SCH-1/SCH-2 and interconnect change list:

1. On the compute board, route CSI0 DCPHY to the right–bridge flex and preserve all six names, polarities and adjacent return assignments. Route I2C4_M3 SCL/SDA at 1E9/1D12 in VCCIO5. Configure the camera I²C pins open drain with internal pulls disabled. [Right–bridge pin table](../interconnect/pinout_right_bridge.csv) · [I/O bank map](../compute_board/io_bank_map.md#L14)
2. Assign J2.13 CAM_ENABLE to a verified spare 1.8 V SoC GPIO and set its startup state low or high-impedance. Keep default host XCLR, MCLK and thermistor unpopulated. Route SAI1 BCLK 1C6, LRCK 1B6 and SDI0 1A6 on VCCIO2, with clocks idle when mic power is off. Check line loading from the planned audio fan-out. [I/O map](../compute_board/io_bank_map.md#L11)
3. Record in the interconnect that bridge pin 20 feeds microphones and the camera 1.8 V rail is local. Verify margin on the present 3.3 V feed before locking the flex, including source tolerance, inrush and return sharing. An increased feed budget or pin/wire change requires D17 review. Update the DF37 mapping only after a proven physical crosswalk. [Interconnect §3](../../docs/interconnect_pinout.md#3-current-voltage-and-ir-drop-screen)

## Open decisions for Krishna

1. Provide the actual numbered SA31VA30P mating-face drawing, or the keyed 30-contact continuity map specified in the crosswalk. Confirm the installed 180° orientation and the connector current split.
2. Resolve the 350 mA feed allocation against measured sensor and autofocus startup/streaming data. Validate XCLR and MCLK timing and whether the RP input ferrites are needed.
3. Confirm the compute enable GPIO, mic clock fan-out, folded flex and optical/mechanical clearances. Verify the chokes are obtainable or select a documented equivalent.
4. Keep the RK3576 IMX708 driver, Rockchip ISP tuning and autofocus initialization as the camera-board ordering gate. [Hardware gap audit G6](../../docs/hardware_gap_audit.md#L290)
