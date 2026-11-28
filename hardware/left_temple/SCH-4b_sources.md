# SCH-4b preflight sources

Git working tree and stash were clean at entry. Fusion MCP returned its open-document list. Existing unsaved Fusion tabs belonged to prior rounds. Capture and export use scripts.

| Requirement | Evidence |
| --- | --- |
| Audio amplifier | [MAX98357A datasheet](../../docs/datasheets/MAX98357A%20Datasheet.PDF), electrical comparator limits, Tables 5/6/8, pinout and application circuit. |
| 1510 speaker | Exact manufacturer impedance, power and voice-coil inductance **UNKNOWN**. Use 8 Ω and a 0.8 W engineering ceiling per project instruction and [BOM §4.D](../../docs/hardware_bom.md#L230). The dual-mono design is in [plan §2.2](../../docs/plan.md#L173). |
| S1 shunt | [Vishay WSK2512 pp. 1–3](../../docs/datasheets/Vishay_WSK2512.pdf), includes four terminals, tolerance, thermal derating and pad drawing. |
| S2 protection FET | [Vishay SiSF04DN-T1-GE3 pp. 1–2 and appended mechanical/land drawings](../../docs/datasheets/Vishay_SiSF04DN.pdf). Manufacturer lists the orderable part. Authorized distributor lists lifecycle **Active**. [Vishay product page](https://www.vishay.com/en/product/77230/) · [DigiKey part status](https://www.digikey.com/en/products/detail/vishay-siliconix/SISF04DN-T1-GE3/11576898) |
| USB VBUS branch | [TI TPS25947 pp. 4–9, 27–35 and 73](../../docs/datasheets/TI_TPS25947.pdf), reverse-blocking TPS259470 and current limit. |
| SoC | [RK3576 datasheet](../../docs/datasheets/Rockchip%20RK3576%20Datasheet.pdf), §2 ball list, §3.2 supply ranges and §3.9 SARADC. [RK3576 HDG](../../docs/datasheets/Rockchip%20RK3576%20Hardware%20Design%20Guide.pdf) and [I/O bank map](../compute_board/io_bank_map.md) identify the implemented bank supply and interface routing. |

The added Vishay PDF carries ordinary copyright and product disclaimer notices. Text checking found no confidentiality or redistribution restriction.
