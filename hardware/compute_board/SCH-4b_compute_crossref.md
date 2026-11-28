# FRIDAY SCH-4b compute board

Project lead Krishna · Auditor Claude · Baseline SCH-2 `08e94c8`

SCH-4b retains all 1,481 physical pad connections from SCH-2. The new connections are listed in the [I/O bank map](io_bank_map.md#sch-4b-inter-board-and-audio-assignments). [SCH-3 interface](../bridge_board/SCH-3_crossref.md#erc-and-downstream-changes) · [SCH-4a interface](../left_temple/SCH-4a_crossref.md#compute-sch-12-change-list)

## B1 and B2 interconnect

| References | Selection and connection | Source |
| --- | --- | --- |
| J5 and J6 | FH12-24S-0.5SH(55), bottom-contact, both pin-1 to pin-1. J5 matches the bridge and J6 matches the left board. Bridge J2 and left J3 native endpoints confirm the mapping. J6 pins 15–17 and both connectors' mechanical tabs have no electrical assignment. | [Right–bridge CSV](../interconnect/pinout_right_bridge.csv) · [Right–left CSV](../interconnect/pinout_right_left_aux.csv) · [Hirose part](https://www.hirose.com/en/product/p/CL0586-0521-0-55) · [orientation](../../docs/interconnect_pinout.md#2-signals-and-end-orientation) |
| U1 CSI | CSI0 DCPHY D0 P/N AK20/AL20, D1 P/N AK21/AL21, CLK P/N AK22/AL22. Canonical CSI net names follow bridge J2. Baseline state retained for every other CSI port and lane. | [RK3576 DS §2 pp. 32–33](../../docs/datasheets/Rockchip%20RK3576%20Datasheet.pdf#page=32), HDG p. 243 Table 3-30. |
| U1 camera I²C | I2C4_M3 SCL 1E9 and SDA 1D12 at VCCIO5 1.8 V. Only the bridge pulls up to local camera DOVDD. | [I/O bank map](io_bank_map.md#sch-4b-inter-board-and-audio-assignments) · [SCH-3 I²C](../bridge_board/SCH-3_crossref.md) |
| R804, U12, C801 | GPIO3_C6 (1D7) to 100 kΩ 1% pulldown and SN74LV1T34DBVR powered from VCCIO5's 1.8 V rail. The buffer drives J5 CAM_ENABLE. 100 nF/16 V X7R bypass. At minimum 1.65 V rail, U12 VOH is 1.55 V at 20 µA, spanning the bridge buffer's 1.48 V upper threshold with the bridge's 100 kΩ pulldown. | [TI SN74LV1T34 pp. 4, 6, 11](../../docs/datasheets/TI_SN74LV1T34.pdf#page=6) · [SCH-3 U4](../bridge_board/SCH-3_crossref.md#camera-power-and-enable) · RK3576 EVB PDF p. 19. |
| TP801–TP803 | DNP test lands on the three reserved J5 reset, host MCLK and NTC contacts. | Right–bridge CSV pins 14–16 and [existing 1 mm test land](../../libraries/FRIDAY_SCH1_Support.lbr#L196). |
| R801–R802 | 22 Ω 1% BCLK and LRCK source damping at U1. | [RK3576 HDG PDF p. 248](../../docs/datasheets/Rockchip%20RK3576%20Hardware%20Design%20Guide.pdf#page=248). |
| R803 | 0 Ω 0603 jumper, specify at least 1 A rating, between system 5 V and the two J6 left amp feed positions. | [Aux link load screen](../../docs/interconnect_pinout.md#3-current-voltage-and-ir-drop-screen), approximately 0.45 A with two forward contacts. Fit an approved jumper after sourcing. |
| R810, R811 | 10 kΩ 1% on DOCK_DET and CHG_STAT to `VCC_1V8_S0`. Nominal 180 µA per asserted input. GPIO4_D0/1 are in VCCIO7. | [SCH-4a right-board list](../left_temple/SCH-4a_crossref.md#compute-sch-12-change-list) · EVB PDF p. 13 U1000K and [Diodes DMN2058U pp. 1–2](../../docs/datasheets/Diodes_DMN2058U.pdf). |
| U18, R812, R813, C807 | SN74LVC1G06DBVR open-drain inverter driven by GPIO0_A7 on PMUIO0. R813 100 kΩ 1% pulldown, C807 100 nF/16 V X7R bypass, R812 22 kΩ 1% pull-up to `VCC_1V8_S3`. Host high pulls J6 CHG_EN low. Pull-up loads the sink at up to 89.5 µA, within the 100 µA condition for guaranteed 0.100 V VOL. | [TI SN74LVC1G06 pp. 3, 5 and 10](../../docs/datasheets/TI_SN74LVC1G06.pdf#page=5), EVB PDF p. 11 and SCH-4a right-board list. |

BCLK and LRCK drive three loads downstream of the compute board routing, two mics on a shared bridge branch and both amps. At 48 kHz and 64 BCLK periods per frame, BCLK is 3.072 MHz. At an assumed 50 Ω and effective dielectric constant of 3, the 65 mm bridge and 130 mm aux flexes add about 22.5 pF together. Allow about 7 pF for three local 20 mm PCB runs, 6 pF from the two MAX98357A inputs at 3 pF each, and an estimated 10 pF total for two microphones. The resulting **approximately 46 pF per clock** is unverified. Route short branches and use a daisy chain where the connector topology permits. Measure the edges at all loads including the two flex branches. MAX98357A fixed 1.3 V VIH should be checked at the actual 1.8 V rail low corner and worst flex drop. [MAX98357A pp. 6–7](../../docs/datasheets/MAX98357A%20Datasheet.PDF#page=6) · [HDG PDF p. 248](../../docs/datasheets/Rockchip%20RK3576%20Hardware%20Design%20Guide.pdf#page=248)

## Right USB charging branch

| References | Selection and connection | Source |
| --- | --- | --- |
| U13 and C802 | TPS259470ARPW auto-retry, between original `VBUS_5V` and J6 `VBUS_5V_CHG`, with 1 µF/25 V X7R input bypass. Always reverse-blocking topology. Existing raw USB TVS retained. | [TI TPS25947 pp. 4–9, 34–35 and 60](../../docs/datasheets/TI_TPS25947.pdf#page=4) |
| R805/R806 | 365 kΩ / 100 kΩ 1% OVLO ladder. Typical rising cutoff `1.20 × (1 + 365/100) = 5.58 V`. | TI TPS25947 pp. 7–9, 28. |
| R807 | 6.57 kΩ 0.1% ILM resistor, `3334 / 6570 = 0.507 A` typical. This value leaves tolerance below the datasheet's 6.65 kΩ recommended maximum. The nearby 6.65 kΩ datasheet row is 0.425–0.575 A. Inverse-resistance scaling gives an engineering screen of about 0.430–0.583 A at the chosen value. | TI TPS25947 pp. 8–9 and 32 Eq. 7. |
| C803 | 1 nF/25 V C0G dVdt capacitor, about 2 V/ms typical by Eq. 4. ITIMER open. AUXOFF and FLT open. | TI TPS25947 pp. 5–6, 29–32. |
| U14, R808/R809, C804 | A second SN74LV1T34DBVR on the S0 1.8 V rail buffers GPIO3_C4 USB permission, with 100 kΩ 1% pulldowns on buffer input and U13 enable, and 100 nF/16 V X7R bypass. The input defaults off. The 1.8 V high level clears the eFuse EN/UVLO rising maximum of 1.223 V. TPS259470 supplies its internal fixed undervoltage protection. | TI SN74LV1T34 pp. 4, 6, 11 and TPS25947 pp. 7–9, 28. |

Three contacts per direction at 0.25 A/contact derated give a 0.75 A steady screening limit. At 5.0 V with 85% assumed conversion efficiency, the 0.20 A charger estimates `8.4 × 0.20 / (5.0 × 0.85) = 0.395 A`. At 4.5 V and 8.5 V pack the estimate is **0.444 A**, above the scaled 0.430 A low limit. Expect foldback or reduced charge at that corner. Add the modeled 119 mV auxiliary flex drop at 0.50 A and both eFuse losses when calculating actual charger VIN. Characterize both current limit and inrush. USB firmware must allow the charge branch only when measured/advertised USB supply current covers the charger plus system load. [Interconnect §3](../../docs/interconnect_pinout.md#3-current-voltage-and-ir-drop-screen) · [Left charger settings](../left_temple/SCH-4a_crossref.md#charger-balance-and-thermal-sense)

## B3 pack monitor and B4 right audio

| References | Selection and connection | Source |
| --- | --- | --- |
| J4, U5 and U10 | J4.1 remains `VBAT_2S_IN` and mates to left `PACK+_PROT`. J4.2 is compute GND and mates to `PACK-_PROT`. TPS2121/SY8205 path stays on the accepted connections. | [Harness CSV](../interconnect/pinout_split_pack.csv) · [SCH-2 netlist](out/FRIDAY_Compute_SCH2_netlist.csv) |
| R814–R816, C805 | 1 MΩ / 220 kΩ divider, plus 100 kΩ ADC-side bleed/load when the switch is on, all 1%. 100 nF/16 V X7R reservoir before the switch. At 8.5 V, `100k ∥ 220k = 68.75k` yields **0.547 V nominal**, **0.557 V** at tolerance high, and **1.558 V unloaded**. SARADC full-scale is AVDD18, nominal 1.8 V and 1.62 V minimum. Worst direct pack draw is **8.03 µA** when sampling. | [RK3576 DS pp. 42, 46](../../docs/datasheets/Rockchip%20RK3576%20Datasheet.pdf#page=46), HDG PDF pp. 85–86 and SCH-4a recommendations. Values are design selections. |
| U15 and C806 | TMUX1511PWR, one SPST channel gates SARADC_IN2 (1B19), powered and enabled from the existing S0 reference-source rail upstream of R1147. Unused channels disabled. C806 100 nF/16 V X7R on switch VDD. The switch's powered-off protection isolates the ADC; the 100 kΩ bleed gives a 0.2 V screen for 2 µA specified off leakage. The switch draws up to 70 µA from powered S0, separate from direct pack leakage. Allow at least 35 ms settling and verify ADC sampling and scale. | [TI TMUX1511 pp. 3–5, 21–22](../../docs/datasheets/TI_TMUX1511.pdf#page=5). |
| U16, J7 | MAX98357AETE+T and local floating BTL pads. Datasheet filterless layout assumes short local speaker wires and >10 µH speaker inductance. Use assumed 8 Ω and 0.8 W until the 1510 part is characterized. | [MAX98357A pp. 15, 28, 33](../../docs/datasheets/MAX98357A%20Datasheet.PDF#page=15) · [left implementation](../left_temple/SCH-4b_left_crossref.md#a1-amplifier-and-speaker). |
| U17, Q13, R820–R822, R826/R827, C812 | TLV7041DBVR and AO3401A local-rail driver. 1 kΩ input resistor, 100 kΩ input pulldown, 100 kΩ P-FET gate pull-up, 56 kΩ/10 kΩ compare divider, all 1%. 100 nF/16 V X7R comparator bypass. GPIO4_A4 at 1C5 enables right channel when high. | [Left identical control topology and source pages](../left_temple/SCH-4b_left_crossref.md#a1-amplifier-and-speaker) · EVB PDF p. 18. |
| R823/R824 | 16.2 kΩ and 4.7 kΩ 1%. At 4.50–5.50 V and resistor extremes, the enabled voltage with the 92–108 kΩ internal RPD is **0.956–1.215 V**. The guaranteed right window is **0.825–1.245 V**. Leakage screen for shutdown is **22.7 mV**, below the 80 mV guaranteed shutdown threshold. | MAX98357A p. 7, Table 5 p. 17, Figure 5 p. 18 and [AO3401A p. 2](../../docs/datasheets/AOS_AO3401A.pdf#page=2). |
| R825, C810, C811 | 100 kΩ 1% to VDD gives +3 dB gain. Bypass amp VDD with 100 nF and 10 µF, both 16 V X7R. | MAX98357A Table 8 p. 28 and p. 33. |

## C1 ERC and open checks

Applied exactly 65 inherited code-104 eMCP warnings with the reason “power pin tied to named rail — auditor reviewed (SCH-2 accepted 08e94c8)”. Each signature matches the accepted SCH-2 ERC position and message. Fusion reports **0 errors, 2 active warnings**, plus 23 earlier approvals and those 65 requested approvals. The two active warnings are U16 VDD tied to the named 5 V rail and U16 EP tied to ground.

[ERC and script checks](out/FRIDAY_Compute_SCH4b_ERC.txt) · [PDF](out/SCH-4b_Compute.pdf) · [Netlist CSV](out/FRIDAY_Compute_SCH4b_netlist.csv) · [BOM](out/FRIDAY_Compute_SCH4b_BOM.csv)

Open checks for Krishna and audit are the USB source-current firmware policy and dual-eFuse behavior, inrush and left speaker wiring, low-voltage audio signals on the folded flex, calibrated pack measurements and sleep transitions, and the SCH-3 DF37 crosswalk and camera release gates. Qualify the combined pack/aux return fault and S1/S2 fuse coordination before putting a qualified cell pack on the board.
