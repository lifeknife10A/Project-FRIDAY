#!/usr/bin/env python3
"""Apply the SCH-1 auditor changes to the checked-in baseline schematic."""

import argparse
import json
import subprocess
import xml.etree.ElementTree as ElementTree
from pathlib import Path

BOARD_DIRECTORY = Path(__file__).resolve().parent
REPOSITORY = BOARD_DIRECTORY.parent.parent
SCHEMATIC_NAME = "FRIDAY_Compute_SCH1.sch"
BASELINE = "16171571244f55ab616cccfe15c18d352f31362e"
SUPPORT_LIBRARY = "FRIDAY_SCH1_Support"
APPROVAL_NOTE = "power pin tied to named rail — auditor reviewed"


def get_net(sheet, name):
    nets = sheet.find("nets")
    net = nets.find(f"net[@name='{name}']")
    if net is None:
        net = ElementTree.SubElement(nets, "net", name=name, **{"class": "0"})
    return net


def add_segment(sheet, net_name, part, gate, pin, start, end, label=True):
    segment = ElementTree.SubElement(get_net(sheet, net_name), "segment")
    ElementTree.SubElement(segment, "pinref", part=part, gate=gate, pin=pin)
    end_x, end_y = (f"{coordinate:.2f}" for coordinate in end)
    ElementTree.SubElement(
        segment, "wire", x1=f"{start[0]:.2f}", y1=f"{start[1]:.2f}",
        x2=end_x, y2=end_y, width="0.1524", layer="91"
    )
    if label:
        ElementTree.SubElement(segment, "label", x=end_x, y=end_y, size="1.016", layer="95")
    return segment


def remove_rail_flag(schematic, sheet, segment):
    for reference in segment.findall("pinref"):
        flag = reference.get("part")
        if flag.startswith("PWR"):
            segment.remove(reference)
            parts = schematic.find("parts")
            instances = sheet.find("instances")
            parts.remove(parts.find(f"part[@name='{flag}']"))
            instances.remove(instances.find(f"instance[@part='{flag}']"))


def move_pin(schematic, sheet, source, target, part, pin):
    old_net = get_net(sheet, source)
    for segment in old_net.findall("segment"):
        reference = segment.find(f"pinref[@part='{part}'][@pin='{pin}']")
        if reference is not None:
            remove_rail_flag(schematic, sheet, segment)
            if len(segment.findall("pinref")) != 1:
                raise ValueError(f"Expected a separate net stub for {part}.{pin}")
            old_net.remove(segment)
            get_net(sheet, target).append(segment)
            return
    raise ValueError(f"{part}.{pin} is missing from {source}")


def add_part(schematic, sheet, name, deviceset, value, x, y, rotation, populate=True):
    parts = schematic.find("parts")
    if parts.find(f"part[@name='{name}']") is not None:
        raise ValueError(f"Part {name} already exists in the baseline")
    part = ElementTree.SubElement(
        parts, "part", name=name, library=SUPPORT_LIBRARY,
        deviceset=deviceset, device="", value=value
    )
    if not populate:
        ElementTree.SubElement(part, "variant", name="default", populate="no")
    ElementTree.SubElement(
        sheet.find("instances"), "instance", part=name, gate="G$1",
        x=f"{x:.2f}", y=f"{y:.2f}", rot=rotation
    )


def add_capacitor(schematic, sheet, name, deviceset, value, rail, x, y, populate=True):
    add_part(schematic, sheet, name, deviceset, value, x, y, "R270", populate)
    add_segment(sheet, rail, name, "G$1", "1", (x, y + 5.08), (x, y + 7.62))
    ground_flag = f"PWR_{name}"
    add_part(schematic, sheet, ground_flag, "GND", "GND", x, y - 10.16, "R0")
    ground = add_segment(sheet, "GND", name, "G$1", "2",
                         (x, y - 5.08), (x, y - 7.62), label=False)
    ground.insert(1, ElementTree.Element("pinref", part=ground_flag, gate="G$1", pin="GND"))


def add_jumper(schematic, sheet, name, source, output, x, y):
    add_part(schematic, sheet, name, "R_0603", "0R", x, y, "R0")
    add_segment(sheet, source, name, "G$1", "1", (x - 5.08, y), (x - 10.16, y))
    add_segment(sheet, output, name, "G$1", "2", (x + 5.08, y), (x + 10.16, y))


def connect_new_soc_pin(schematic, sheet, pin, rail):
    soc = schematic.find("libraries/library[@name='RK3576']")
    device = soc.find("devicesets/deviceset[@name='RK3576']")
    for gate in device.findall("gates/gate"):
        symbol = soc.find(f"symbols/symbol[@name='{gate.get('symbol')}']")
        symbol_pin = symbol.find(f"pin[@name='{pin}']")
        if symbol_pin is not None:
            gate_name = gate.get("name")
            instance = sheet.find(f"instances/instance[@part='U1'][@gate='{gate_name}']")
            if instance is None or instance.get("rot") not in (None, "R0"):
                raise ValueError(f"Unexpected placement for U1.{pin}")
            x = float(instance.get("x")) + float(symbol_pin.get("x"))
            y = float(instance.get("y")) + float(symbol_pin.get("y"))
            if symbol_pin.get("rot") != "R180":
                raise ValueError(f"Expected a right-facing power stub for U1.{pin}")
            add_segment(sheet, rail, "U1", gate_name, pin, (x, y), (x + 5.08, y))
            return
    raise ValueError(f"Cannot find U1.{pin}")


def update_rk806(library):
    changed = 0
    for pin in library.findall("symbols/symbol/pin"):
        if pin.get("name") in {f"VOUT{number}" for number in range(1, 11)}:
            pin.set("direction", "pas")
            changed += 1
    if changed != 10:
        raise ValueError(f"Expected ten RK806 VOUT sense pins, found {changed}")


def update_schematic(root):
    schematic = root.find("drawing/schematic")
    pmic_sheet = schematic.findall("sheets/sheet")[1]
    soc_sheet = schematic.findall("sheets/sheet")[3]

    # X1. EVB sheets 05 and 11, U1000E / C1107 / C1118.
    for pin in ("PMU_LOGIC_DVDD0V75_0_2L2", "PMU_LOGIC_DVDD0V75_1_2L10"):
        move_pin(schematic, soc_sheet, "VDD_LOGIC_S0", "VDD_0V75_S3", "U1", pin)

    # X2. EVB sheets 05, 12 and 23. BUCK9 is the common, direct supply.
    retention_rail = "VDDQ_DDR_CKE_S3"
    for sheet in (pmic_sheet, soc_sheet):
        net = sheet.find("nets/net[@name='VDD2_DDR_S3']")
        for segment in net.findall("segment"):
            remove_rail_flag(schematic, sheet, segment)
        net.set("name", retention_rail)
    move_pin(schematic, soc_sheet, "VDDQ_DDR_S0", retention_rail, "U1", "DDRPHY_CKE_VDDQ_2B2")

    # X3. EVB sheets 06 and 13, C1300. HDG section 2.1.11.1 selects 1.8 V.
    # X4. EVB sheet 14, C1400-C1403. The two 0.85 V pins share one net.
    # X5. EVB sheet 05 and HDG Figure 2-40, R1320/R1323 and PHY bypass.
    # X6. EVB sheets 05, 06, 18 and 24, including R2427 and C2423.
    connections = {
        "VCCIO7_VCC_2M3": "VCC_1V8_S0",
        "USB3_OTG0_DP_TX_AVDD0V85_2M5": "VDDA_0V85_S0",
        "USB3_OTG0_DP_TX_DVDD0V85_2N5": "VDDA_0V85_S0",
        "USB3_OTG0_DP_TX_AVDD1V8_2N4": "VCCA_1V8_S0",
        "UFS_AVDD0V85_2N2": "UFS_AVDD0V85",
        "UFS_AVDD1V8_2P2": "UFS_AVDD1V8",
        "OSC_UFS_AVDD_2M2": "VCCA_1V8_S0",
    }
    for pin, rail in connections.items():
        connect_new_soc_pin(schematic, soc_sheet, pin, rail)

    move_pin(schematic, soc_sheet, "VCC_3V3_S0", "VCC_1V8_S0", "U1", "VCCIO2_VCC_2A2")
    move_pin(schematic, soc_sheet, "VCC_3V3_S3", "VCCIO_WL", "U1", "VCCIO3_VCC_2B10")
    move_pin(schematic, soc_sheet, "VCC_3V3_S3", "VCCIO_WL", "C1801", "1")

    for name, source, rail, y in (
        ("R1320", "VDDA_0V85_S0", "UFS_AVDD0V85", 226.06),
        ("R1323", "VCCA_1V8_S0", "UFS_AVDD1V8", 200.66),
        ("R2427", "VCC_1V8_S3", "VCCIO_WL", 175.26),
    ):
        add_jumper(schematic, soc_sheet, name, source, rail, 497.84, y)
    for name, deviceset, value, rail, x, y, populate in (
        ("C1300", "C_0201", "100nF 6.3V", "VCC_1V8_S0", 467.36, 259.08, True),
        ("C1400", "C_0201", "1uF 6.3V", "VDDA_0V85_S0", 518.16, 259.08, True),
        ("C1401", "C_0201", "1uF 6.3V", "VDDA_0V85_S0", 563.88, 259.08, False),
        ("C1402", "C_0201", "1uF 6.3V", "VCCA_1V8_S0", 609.60, 259.08, True),
        ("C1403", "C_0201", "1uF 6.3V", "VCCA_1V8_S0", 655.32, 259.08, False),
        ("C1302", "C_0201", "1uF 6.3V", "UFS_AVDD0V85", 556.26, 226.06, True),
        ("C1303", "C_0402", "1uF 6.3V", "UFS_AVDD0V85", 601.98, 226.06, True),
        ("C1305", "C_0201", "1uF 6.3V", "UFS_AVDD1V8", 556.26, 200.66, True),
        ("C1306", "C_0402", "1uF 6.3V", "UFS_AVDD1V8", 601.98, 200.66, True),
        ("C2423", "C_0603", "10uF 6.3V", "VCCIO_WL", 556.26, 175.26, True),
    ):
        add_capacitor(schematic, soc_sheet, name, deviceset, value, rail, x, y, populate)

    # X8. The VOUT pins sense the outputs after each inductor (EVB sheet 23, U2300).
    update_rk806(schematic.find("libraries/library[@name='RK806-1']"))
    for note in soc_sheet.findall("plain/text"):
        if (note.text or "").startswith("CITATIONS:"):
            note.text = (
                "EVB sheets 05, 06, 10-19, 23-24; RK3576 DS Table 3-2; HDG sections "
                "2.1.11.1 and 2.2.2. RK3576 FCCSP-698L footprint: UNVERIFIED vs DS section 2."
            )


def add_erc_approvals(schematic, results):
    # Fusion exposes the same signature that EAGLE stores as the approval hash.
    signatures = {
        result["signature"] for result in results
        if result["code"] == 104
        and result["type"] == 1
        and result["description"].startswith("POWER pin ")
    }
    if not signatures or any(result["type"] not in (0, 1) for result in results):
        raise ValueError("ERC must report power warnings and zero errors before approvals")
    approvals = ElementTree.SubElement(schematic, "errors")
    for signature in sorted(signatures):
        ElementTree.SubElement(approvals, "approved", hash=signature)
    plain = schematic.find("sheets/sheet/plain")
    note = ElementTree.SubElement(plain, "text", x="12.7", y="269.24", size="1.778", layer="94")
    note.text = f"ERC code 104 approval note: {APPROVAL_NOTE}"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", type=Path, help="Original SCH-1 schematic. Defaults to Git baseline 1617157.")
    parser.add_argument("--output", type=Path, default=BOARD_DIRECTORY / SCHEMATIC_NAME)
    parser.add_argument("--erc-before", type=Path, help="Fusion ERC results as a JSON array before approval.")
    arguments = parser.parse_args()
    if arguments.base is None:
        relative_path = (BOARD_DIRECTORY / SCHEMATIC_NAME).relative_to(REPOSITORY)
        source = subprocess.check_output(
            ["git", "show", f"{BASELINE}:{relative_path.as_posix()}"], cwd=REPOSITORY
        )
    else:
        source = arguments.base.read_bytes()
    root = ElementTree.fromstring(source)
    update_schematic(root)
    if arguments.erc_before is not None:
        add_erc_approvals(root.find("drawing/schematic"), json.loads(arguments.erc_before.read_text()))
    ElementTree.indent(root, space="  ")
    arguments.output.write_bytes(
        b'<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE eagle SYSTEM "eagle.dtd">\n'
        + ElementTree.tostring(root, encoding="utf-8")
        + b"\n"
    )


if __name__ == "__main__":
    main()
