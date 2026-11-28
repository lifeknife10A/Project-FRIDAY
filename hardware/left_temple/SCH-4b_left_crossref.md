# FRIDAY SCH-4b left board

Project lead Krishna · Auditor Claude · Baseline [SCH-4a e000598](FRIDAY_Left_SCH4a.sch)

The left board adds a local mono amplifier to the accepted D16/D17 pack and charger. The source check preserves the original connection set outside the replaced Q1, including both series cells, F1, the Kelvin points, the protected two-lead harness, the pogo/input OR and the 200 mA charger setting. [SCH-4a references](SCH-4a_crossref.md) · [SCH-4b preflight sources](SCH-4b_sources.md)

## S1 and S2

| Reference | Selection and connection | Source |
| --- | --- | --- |
| RS1 | Vishay WSK2512R0200FEA, 20 mΩ ±1%, 1 W at 70 °C. Four-terminal connection and TP4/TP5 Kelvin points retained. | [Vishay WSK2512 pp. 1–3](../../docs/datasheets/Vishay_WSK2512.pdf), including derating and ordering table. |
| Q1 | Active Vishay SiSF04DN-T1-GE3, 30 V VDS breakdown, common-drain dual N-channel. 6 mΩ maximum measured source-to-source at 4.5 V gate drive and 25 °C. PowerPAK 1212-8SCD, datasheet-recommended copper pattern. Pins 1/4 keep discharge/charge gates, joined 7/8 keep CELL_NEG, joined 5/6 keep SHUNT_FET_SIDE, and pins 2/3 keep FET_COMMON_DRAIN. | [Vishay datasheet pp. 1–2, 7–8](../../docs/datasheets/Vishay_SiSF04DN.pdf) · [Active orderable status](https://www.digikey.com/en/products/detail/vishay-siliconix/SISF04DN-T1-GE3/11576898) |
| U2, F1 | HY2120-CB discharge-OC threshold 170–230 mV. F1 remains Littelfuse 0451002.MRL, 2 A. | HY2120 p. 6 from the [SCH-4a restricted source record](SCH-4a_crossref.md#restricted-datasheets-on-the-workstation) · [Littelfuse pp. 2–3](../../docs/datasheets/Littelfuse_Nano2_451_453.pdf#page=2) |

With the maximum specified pair resistance in the model, `Rpath = 20 mΩ + 6 mΩ` and `170–230 mV / 26 mΩ = 6.54–8.85 A`. The 6 mΩ is already the total for both FETs. Equivalently the pair contributes 2 × 3 mΩ in this calculation, with no per-channel matching assumption. The shunt produces **30 mV at 1.5 A**, **60 mV at 3 A**, and **0.180 W at 3 A**. The pair plus shunt produces about 78 mV at 3 A under the stated conditions. This trip estimate is conditional on gate voltage, temperature, copper loss and actual part resistance. Qualify the short-circuit response and 2 A fuse time coordination separately from the 3 A pulse budget.

## A1 amplifier and speaker

| References | Selection and connection | Source |
| --- | --- | --- |
| U5 | MAX98357AETE+T, 16-pin TQFN. J3.2/3 provide `VCC5V0_SYS_S5_AMP`, J3.5 BCLK, J3.7 LRCLK, J3.8 SDO0, and J3.9 left enable. Ground and EP use `PACK-_PROT`. | [MAX98357A pp. 4, 6–7, 15, 17–18 and 33](../../docs/datasheets/MAX98357A%20Datasheet.PDF#page=15) · [auxiliary CSV](../interconnect/pinout_right_left_aux.csv) |
| U6, Q6, R29–R31, R35–R36 | TLV7041DBVR compares host input through 1 kΩ with 100 kΩ fail-low bias against a 56 kΩ/10 kΩ local-rail reference. The open-drain output sinks the AO3401A gate when host high. A 100 kΩ gate pull-up switches the P-FET off otherwise. Resistors are 1%. Host voltage does not set the analog SD_MODE level. | [TI TLV7041 pp. 3–4, 6, 8 and 21](../../docs/datasheets/TI_TLV7041.pdf#page=8) · [AO3401A pp. 1–2](../../docs/datasheets/AOS_AO3401A.pdf) · [RK3576 Table 3-3 p. 43](../../docs/datasheets/Rockchip%20RK3576%20Datasheet.pdf#page=43). Resistors are design selections. |
| R32, R33 | 1 kΩ 1% from the switched amp rail and 4.7 kΩ 1% to protected return. The internal 92–108 kΩ pulldown is in parallel with 4.7 kΩ. With the enabled path and 4.50–5.50 V supply, the worst-corner SD_MODE level is 3.656–4.517 V. | MAX98357A p. 7 and Table 5 p. 17. |
| R34 | 100 kΩ 1% from `GAIN_SLOT` to amp VDD gives **+3 dB** in I²S mode. | MAX98357A Table 8 p. 28. |
| C16–C19 | C16 100 nF/16 V X7R and C17 10 µF/16 V X7R at amplifier VDD. C18 100 nF/16 V X7R at comparator VCC. C19 22 µF/16 V X7R additional amp bulk for the long auxiliary feed. | MAX98357A p. 33 power-supply input guidance, TI TLV7041 pp. 20–21 bypass guidance. Extra bulk is a design choice to validate under inrush. |
| J4 | Local floating BTL `SPK_L_P/N` solder lands. Use 8 Ω and 0.8 W as design assumptions. Exact 1510 impedance, power and voice-coil inductance are **UNKNOWN**. | [Plan §2.2](../../docs/plan.md#L173) · [BOM §4.D](../../docs/hardware_bom.md#L230) · MAX98357A pp. 15, 28, 33. |

| MAX98357A p. 7, Table 5 p. 17 | Comparator trip limits | Guaranteed decoding screen |
| --- | --- | --- |
| B0 | 0.080–0.355 V | Shutdown below 0.080 V |
| B1 | 0.650–0.825 V | Right above 0.825 V |
| B2 | 1.245–1.500 V | Right below 1.245 V, left above 1.500 V |

The host low/high guarantee used is 0.25 × 1.95 V maximum low and 0.75 × 1.65 V minimum high. The comparator reference screen tolerates ±30 mV for comparator variation and is about 0.64–0.88 V over the amp supply range. At host low, the AO3401A drain leakage limit at 55 °C gives `5 µA × (4.7 kΩ ∥ 108 kΩ)`, including resistor tolerance, or **22.7 mV** maximum modeled SD_MODE. At host high, even minimum supply and component corners give **3.656 V**, above the left threshold. Confirm both endpoints at hot and low supply.

The speaker connection is local and the datasheet's filterless application uses a voice-coil inductance above 10 µH. The capture uses short paired speaker wires without output ferrites or capacitors. Verify inductance, real lead length and EMI before release. To honor 0.8 W at an assumed 8 Ω, enforce and measure **2.53 V RMS** maximum across the differential output. Gain selection alone does not enforce the power limit. [MAX98357A p. 33](../../docs/datasheets/MAX98357A%20Datasheet.PDF#page=33)

**ERC:** 0 errors and 4 active warnings. Three are the VDD, EP and GND names on U5's defined supplies. One is the local Q1 common drain. The inherited SCH-4a power checks pass with the new shunt, and native Fusion confirmed the speaker/flex connections. [ERC and topology checks](out/FRIDAY_Left_SCH4b_ERC.txt) · [PDF](out/SCH-4b_Left.pdf) · [Netlist CSV](out/FRIDAY_Left_SCH4b_netlist.csv) · [BOM](out/FRIDAY_Left_SCH4b_BOM.csv)

Open checks are cell qualification, hot short-circuit and fuse coordination, speaker unit data and EMC, and the existing parallel auxiliary-return fault if the dedicated pack return opens.
