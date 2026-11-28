#!/usr/bin/env python3
"""Check the native Fusion SCH-2 exports before writing the audit files."""

import csv
import json
import re
import shutil
import subprocess
import xml.etree.ElementTree as ElementTree
from collections import defaultdict
from pathlib import Path

from gen_sch2 import BASELINE, BOARD_DIRECTORY, DDR_POWER, EMMC_POWER, EMCP_PART, SCHEMATIC_NAME


FUSION_EXPORTS = Path("/tmp/friday-sch2-fusion")
NETLIST = "FRIDAY_Compute_SCH2_netlist.txt"
OUTPUT = BOARD_DIRECTORY / "out"


def read_native_netlist(path):
    contents = path.read_text(encoding="utf-8")
    rows = []
    net_name = ""
    for line in contents.split("Pin        Sheet", 1)[1].splitlines():
        if line.strip():
            fields = line.split()
            if not line[0].isspace():
                net_name = fields.pop(0)
            part_name, pad, pin, sheet = fields
            rows.append((net_name, part_name, pad, pin, sheet))
    return rows


def check_netlist(rows, source):
    with (BOARD_DIRECTORY / "emcp_ballmap_source.csv").open(newline="", encoding="utf-8") as stream:
        ball_map = {row["ball"]: row["signal"] for row in csv.DictReader(stream)}
    native_pins = defaultdict(list)
    for net_name, part_name, pad, pin, _sheet in rows:
        native_pins[part_name, pad].append(net_name)
        if part_name == EMCP_PART and pin.casefold() != ball_map[pad].casefold():
            raise ValueError(f"Native pin name for {pad} differs from the ball map: {pin}")

    memory_device = source.find("libraries/library[@name='H9HP52ACPMADAR']/devicesets/deviceset/devices/device")
    pads = {(item.get("gate"), item.get("pin")): item.get("pad") for item in memory_device.findall("connects/connect")}
    expected = defaultdict(list)
    for net in source.findall("sheets/sheet/nets/net"):
        for pinref in net.findall(f"segment/pinref[@part='{EMCP_PART}']"):
            pad = pads[pinref.get("gate"), pinref.get("pin")]
            expected[pad].append(net.get("name"))
    native_balls = {pad: nets for (part_name, pad), nets in native_pins.items() if part_name == EMCP_PART}
    no_connects = {pad for pad, signal in ball_map.items()
                   if signal in ("NC", "DNU") or re.fullmatch(r"VSF[1-9]", signal)}
    if native_balls != expected or native_balls.keys() != ball_map.keys() - no_connects:
        raise ValueError("Native eMCP pad connections differ from the generated schematic or ball map")
    power = {**DDR_POWER, **EMMC_POWER, "VSS": "GND", "VSSm": "GND"}
    for pad, nets in native_balls.items():
        if len(nets) != 1:
            raise ValueError(f"Native netlist must contain one connection for {pad}: {nets}")
        signal = ball_map[pad]
        if signal in power and nets != [power[signal]]:
            raise ValueError(f"Incorrect supply connection for {pad}: {nets}")
        if signal not in power and nets[0] in power.values():
            raise ValueError(f"Signal {signal} ({pad}) on power or ground: {nets}")

    with (BOARD_DIRECTORY / "SCH-2_ddr_pinmap.csv").open(newline="", encoding="utf-8") as stream:
        pinmap = list(csv.DictReader(stream))
    if len(pinmap) != 69 or len({row["emcp_ball"] for row in pinmap}) != 69:
        raise ValueError("Expected 69 unique DDR connections between the SoC and eMCP")
    for row in pinmap:
        if (native_pins["U1", row["soc_ball"]] != [row["net"]]
                or native_balls[row["emcp_ball"]] != [row["net"]]
                or ball_map[row["emcp_ball"]] != row["emcp_signal"]):
            raise ValueError(f"DDR pin-map row disagrees with native Fusion export: {row}")

    for net, connections in {
        "VDD2_DDR_S3": (("L9", "2"), ("U2", "67"), ("R3809", "1")),
        "VDDQ_DDR_CKE_S3": (("R3809", "2"), ("U1", "2B2"), ("C1214", "1")),
        "VDDQ_DDR_S0": (("L6", "2"), ("R1200", "2"), ("R1201", "2"), ("R3802", "2"), ("R3804", "2")),
        "VCC_1V8_S3": (("L8", "2"),),
        "VCC_3V3_S0": (("U8", "1"),),
        "VCC_1V8_S0": (("U9", "A1"), ("U1", "1J20")),
        "DDRPHY_ZQ_A": (("U1", "1R6"), ("R1200", "1")),
        "DDRPHY_ZQ_B": (("U1", "1J6"), ("R1201", "1")),
        "EMMC_CLK": (("U1", "1G23"), ("R4000", "1")),
        "EMMC_CLKOUT": ((EMCP_PART, "P12"), ("R4000", "2")),
        "EMMC_STRB": (("U1", "1F23"), (EMCP_PART, "M12")),
        "USB3_OTG0_REXT_DP_TX_REXT": (("U1", "2T7"), ("R1400", "1")),
        "GND": (("R1400", "2"), ("C4004", "2")),
    }.items():
        for connection in connections:
            if native_pins[connection] != [net]:
                raise ValueError(f"Native {connection} uses {native_pins[connection]}, expected {net}")
    supply_count = sum(ball_map[pad] in power for pad in native_balls)
    return len(pinmap), len(native_balls) - supply_count, supply_count, len(no_connects)


def build_bom(schematic):
    libraries = {library.get("name"): library for library in schematic.findall("libraries/library")}
    bom = []
    for part in schematic.findall("parts/part"):
        name, library_name = part.get("name"), part.get("library")
        deviceset, device = part.get("deviceset"), part.get("device")
        library = libraries[library_name]
        package = library.find(f"devicesets/deviceset[@name='{deviceset}']/devices/device[@name='{device}']").get("package")
        if not package or name.startswith("FRAME"):
            continue
        attributes = {attribute.get("name"): attribute.get("value", "") for attribute in part.findall("attribute")}
        variant = part.find("variant[@name='default']")
        populate = variant.get("populate", "yes") if variant is not None else "yes"
        manufacturer_part = "H9HP52ACPMADAR-KMM" if name == EMCP_PART else attributes.get("MPN", "")
        bom.append((name, part.get("value", ""), package, deviceset, library_name, manufacturer_part,
                    attributes.get("LCSC", ""), populate))
    if [(row[0], row[-1]) for row in bom if row[0] == "R4010"] != [("R4010", "no")]:
        raise ValueError("The native BOM must retain the optional eMMC reset pull-up as DNP")
    return bom


def erc_report(source, counts):
    results = json.loads((FUSION_EXPORTS / "erc.json").read_text(encoding="utf-8"))
    issues = results["issues"]
    error_count = sum(issue["type"] == 0 for issue in issues)
    warnings = [issue for issue in issues if issue["type"] == 1 and issue["state"] == 0]
    approvals = [issue for issue in issues if issue["type"] == 1 and issue["state"] == 2]
    existing_approvals = {item.get("hash") for item in source.findall("errors/approved")}
    baseline = subprocess.check_output(
        ["git", "show", f"{BASELINE}:hardware/compute_board/FRIDAY_Compute_SCH1.sch"],
        cwd=BOARD_DIRECTORY,
    )
    baseline_approvals = {item.get("hash") for item in ElementTree.fromstring(baseline).findall(
        "drawing/schematic/errors/approved")}
    if existing_approvals != baseline_approvals or {issue["signature"] for issue in approvals} != baseline_approvals:
        raise ValueError("Fusion must retain only the SCH-1 ERC approvals")
    if not results["checked"] or error_count or len(warnings) + len(approvals) != len(issues):
        raise ValueError(f"Fusion ERC reported {error_count} errors or an unexpected state")
    power_gate = source.find("sheets/sheet/instances/instance[@part='U11'][@gate='POWER']")
    library = source.find("libraries/library[@name='H9HP52ACPMADAR']")
    power_symbol = library.find("symbols/symbol[@name='POWER']")
    pads_by_location = {}
    for pin in power_symbol.findall("pin[@direction='pwr']"):
        signal, _, pad = pin.get("name").partition("@")
        position = tuple(round(float(power_gate.get(axis)) + float(pin.get(axis)), 2) for axis in ("x", "y"))
        pads_by_location[position] = (signal, pad)
    supply = {**DDR_POWER, **EMMC_POWER}
    seen_pads = set()
    lines = [
        f"Fusion ERC — {results['document']} (Autodesk Fusion {results['fusion']})",
        f"Schematic checked: {results['checked']}",
        f"{error_count} errors, {len(warnings)} active warnings, {len(approvals)} inherited approvals and 0 new approvals.",
        "Active code 104 warnings are eMCP power pins on the named FRIDAY rails.",
        "",
        f"Native netlist: {counts[1] + counts[2]} eMCP balls wired once ({counts[1]} signal, {counts[2]} supply/ground).",
        f"{counts[3]} VSF/DNU/NC balls open. DDR pin-map matches {counts[0]} native SoC-to-eMCP connections.",
        "",
        "Sheet | Code | Position (mm) | Ball | Fusion message | State",
    ]
    for issue in issues:
        _, sheet, x_position, y_position, part, signal, net_name, *_ = issue["signature"].split("\t")
        pad = ""
        if issue["state"] == 0:
            location = (float(x_position), float(y_position))
            expected_signal, pad = pads_by_location.get(location, ("", ""))
            if (issue["code"] != 104 or sheet != "7" or part != "U11POWER"
                    or signal != expected_signal or net_name != supply.get(signal) or pad in seen_pads):
                raise ValueError(f"Unexpected active Fusion warning: {issue['description']}")
            seen_pads.add(pad)
        state = "active" if issue["state"] == 0 else "approved in SCH-1"
        lines.append(f"{sheet} | {issue['code']} | ({x_position}, {y_position}) | {pad} | {issue['description']} | {state}")
    if len(seen_pads) != len(pads_by_location):
        raise ValueError("Expected one named-rail warning per eMCP input power pin")
    return "\n".join(lines) + "\n"


def check_pdf(path, bom):
    info = subprocess.check_output(["pdfinfo", str(path)], text=True)
    if not re.search(r"^Pages:\s+8$", info, re.MULTILINE):
        raise ValueError("Expected an eight-page Fusion PDF")
    pages = subprocess.check_output(["pdftotext", "-f", "6", "-l", "8", str(path), "-"], text=True)
    for number in range(6, 9):
        if f"PROJECT FRIDAY - S{number}:" not in pages:
            raise ValueError(f"Missing SCH-2 title for sheet {number}")
    identifiers = set(re.findall(r"\b[CR]\d+\b", pages))
    new_passives = {row[0] for row in bom if row[0] in ("R1200", "R1201", "R1400")
                    or re.fullmatch(r"[CR](38|40)\d{2}", row[0])}
    if new_passives - identifiers:
        raise ValueError(f"Missing PDF reference designators: {sorted(new_passives - identifiers)}")


def write_csv(path, headers, rows):
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(headers)
        writer.writerows(rows)


def main():
    source = ElementTree.parse(BOARD_DIRECTORY / SCHEMATIC_NAME).find("drawing/schematic")
    native = ElementTree.parse(FUSION_EXPORTS / SCHEMATIC_NAME).find("drawing/schematic")
    rows = read_native_netlist(FUSION_EXPORTS / NETLIST)
    counts = check_netlist(rows, source)
    bom = build_bom(native)
    report = erc_report(source, counts)
    check_pdf(FUSION_EXPORTS / "SCH-2.pdf", bom)

    shutil.copyfile(FUSION_EXPORTS / "SCH-2.pdf", OUTPUT / "SCH-2.pdf")
    native_text = (FUSION_EXPORTS / NETLIST).read_text(encoding="utf-8").rstrip("\n")
    (OUTPUT / NETLIST).write_text(native_text + "\n", encoding="utf-8")
    write_csv(OUTPUT / "FRIDAY_Compute_SCH2_netlist.csv", ("Net", "Part", "Pad", "Pin", "Sheet"), rows)
    write_csv(OUTPUT / "FRIDAY_Compute_SCH2_bom.csv",
              ("RefDes", "Value", "Package", "Deviceset", "Library", "MPN", "LCSC", "Populate"), bom)
    (OUTPUT / "FRIDAY_Compute_SCH2_erc.txt").write_text(report, encoding="utf-8")
    net_names = {row[0] for row in rows}
    print(f"{len(net_names)} nets, {len(rows)} native pin rows, {len(bom)} BOM entries.")
    print("\n".join(report.splitlines()[2:7]))


if __name__ == "__main__":
    main()
