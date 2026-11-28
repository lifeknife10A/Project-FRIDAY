#!/usr/bin/env python3
"""Verify the Fusion export, then write the SCH-4a audit files."""

import csv
import json
import re
import shutil
import xml.etree.ElementTree as ElementTree
from collections import defaultdict
from pathlib import Path

from gen_sch4a import BOARD_DIRECTORY, REPOSITORY, SCHEMATIC_NAME


FUSION_EXPORTS = Path("/tmp/friday-sch4a-fusion")
OUTPUT = BOARD_DIRECTORY / "out"
NETLIST = "FRIDAY_Left_SCH4a_netlist.txt"
PACK_POSITIVE = "PACK+_PROT"
PACK_RETURN = "PACK-_PROT"

MANUFACTURER_PARTS = {
    "U1": "IP2326_NPD",
    "U2": "HY2120-CB",
    "U3": "TPS259470ARPW",
    "U4": "TPS259470ARPW",
    "Q1": "AON5816",
    "Q2": "AO3401A",
    "Q3": "DMN2058U-7",
    "Q4": "DMN2058U-7",
    "Q5": "DMN2058U-7",
    "RS1": "WSK2512R0500FEA",
    "F1": "0451002.MRL",
    "L1": "XAL5030-222MEC",
    "D1": "SMF6.0A",
    "D2": "SMF6.0A",
    "J1": "686E0321250110E",
    "J3": "FH12-24S-0.5SH(55)",
    "TH1": "HNT-GR1, 100k/B4100 option",
}


def require(condition, explanation):
    if not condition:
        raise ValueError(explanation)


def native_rows(path):
    rows = []
    net_name = ""
    for line in path.read_text(encoding="utf-8").split("Pin        Sheet", 1)[1].splitlines():
        if not line.strip():
            continue
        fields = line.split()
        if not line[0].isspace():
            net_name = fields.pop(0)
        part, pad, pin, sheet = fields
        rows.append((net_name, part, pad, pin.upper(), sheet))
    return rows


def expected_rows(schematic):
    mappings = {}
    for part in schematic.findall("parts/part"):
        reference = part.get("name")
        library = schematic.find(f"libraries/library[@name='{part.get('library')}']")
        device = library.find(f"devicesets/deviceset[@name='{part.get('deviceset')}']"
                              f"/devices/device[@name='{part.get('device')}']")
        mappings[reference] = {
            (connection.get("gate"), connection.get("pin")): connection.get("pad").split()
            for connection in device.findall("connects/connect")
        }
    rows = set()
    physical_nets = {}
    for sheet_number, sheet in enumerate(schematic.findall("sheets/sheet"), start=1):
        for net in sheet.findall("nets/net"):
            for pinref in net.findall("segment/pinref"):
                part, gate, pin = (pinref.get(key) for key in ("part", "gate", "pin"))
                net_name = net.get("name")
                for pad in mappings[part][gate, pin]:
                    require((part, pad) not in physical_nets, f"Duplicate source pad {part}.{pad}")
                    physical_nets[part, pad] = net_name
                    rows.add((net_name, part, pad, pin.upper(), str(sheet_number)))
    return rows


def check_paths(pins, values, protection_pads=None, shunt_ohms=0.050):
    if protection_pads is None:
        protection_pads = {"G1": "G1", "G2": "G2", "S1A": "S1A", "S1B": "S1B",
                           "S2A": "S2A", "S2B": "S2B", "EP": "EP"}
    def match(part, expected):
        for pad, net_name in expected.items():
            require(pins.get((part, pad)) == net_name, f"{part}.{pad} must be on {net_name}")

    match("BT1", {"1": "CELL_POS", "2": "CELL_MID"})
    match("BT2", {"1": "CELL_MID", "2": "CELL_NEG"})
    match("F1", {"1": "CELL_POS", "2": PACK_POSITIVE})
    match("U2", {"1": "DISCHARGE_GATE", "2": "CHARGE_GATE", "3": "PROTECT_CS",
                 "4": "PROTECT_VC", "5": "PROTECT_VDD", "6": "CELL_NEG"})
    match("R3", {"1": PACK_RETURN, "2": "PROTECT_CS"})
    protection_nets = {"G1": "DISCHARGE_GATE", "G2": "CHARGE_GATE", "S1A": "CELL_NEG",
                       "S1B": "CELL_NEG", "S2A": "SHUNT_FET_SIDE", "S2B": "SHUNT_FET_SIDE",
                       "EP": "FET_COMMON_DRAIN"}
    match("Q1", {physical: protection_nets[alias] for physical, alias in protection_pads.items()})
    match("RS1", {"P1": "SHUNT_FET_SIDE", "P2": PACK_RETURN, "K1": "SHUNT_K-", "K2": "SHUNT_K+"})
    match("J1", {"1": "POGO_VBUS_IN", "2": PACK_RETURN, "3": "POGO_DET_RAW"})
    match("J2", {"1": PACK_POSITIVE, "2": PACK_RETURN})
    require({pad for part, pad in pins if part == "J2"} == {"1", "2"}, "Only two harness leads are allowed")

    with (REPOSITORY / "hardware/interconnect/pinout_right_left_aux.csv").open(newline="") as stream:
        for row in csv.DictReader(stream):
            expected = None if row["type"] == "NC" else row["net"]
            match("J3", {row["pin"]: PACK_RETURN if expected == "GND" else expected})

    match("U1", {"1": None, "2": None, "3": None, "4": "CHARGER_NTC", "6": None, "9": None, "10": None,
                 "11": "CHARGER_ISET", "12": "CHARGER_RUN", "13": "CHARGER_VIN", "15": "CHARGER_SW",
                 "16": "CHARGER_SW", "17": "CHARGER_SW", "18": PACK_RETURN, "21": PACK_POSITIVE,
                 "22": PACK_POSITIVE, "23": "CHARGER_VBATM", "24": PACK_RETURN, "EP": PACK_RETURN})
    match("Q2", {"3": "CELL_MID", "2": "MIDPOINT_SWITCHED", "1": "BALANCE_GATE"})
    match("R11", {"1": "MIDPOINT_SWITCHED", "2": "CHARGER_VBATM"})

    match("U3", {"5": "POGO_VBUS_IN", "6": "VBUS_OR", "8": PACK_RETURN})
    match("U4", {"5": "VBUS_5V_CHG", "6": "VBUS_OR", "8": PACK_RETURN})
    match("R4", {"1": "VBUS_OR", "2": "CHARGER_VIN"})
    match("L1", {"1": "VBUS_OR", "2": "CHARGER_SW"})
    match("D1", {"1": "POGO_VBUS_IN", "2": PACK_RETURN})
    match("D2", {"1": "VBUS_5V_CHG", "2": PACK_RETURN})
    match("Q3", {"1": "DETECT_GATE", "2": PACK_RETURN, "3": "DOCK_DET"})
    match("Q4", {"1": "STATUS_GATE", "2": PACK_RETURN, "3": "CHG_STAT"})
    match("Q5", {"1": "ENABLE_GATE", "2": PACK_RETURN, "3": "CHARGER_RUN"})
    for test_number, net_name in enumerate((PACK_POSITIVE, PACK_RETURN, "CELL_MID", "SHUNT_K-",
                                            "SHUNT_K+", "VBUS_OR", "CHARGER_SW", "CHARGER_NTC"), start=1):
        match(f"TP{test_number}", {"1": net_name})

    require({connection for connection, net in pins.items() if net == "CHARGER_VIN"}
            == {("U1", "13"), ("R4", "2"), ("C4", "1")}, "Unexpected charger VIN branch")
    require({connection for connection, net in pins.items() if net == "VBUS_OR"}
            == {("U3", "6"), ("U4", "6"), ("L1", "1"), ("R4", "1"), ("R28", "1"),
                ("C3", "1"), ("TP6", "1")}, "Unexpected VBUS_OR branch")
    require({connection for connection, net in pins.items() if net == "CELL_POS"}
            == {("BT1", "1"), ("F1", "1"), ("R1", "1")}, "Raw cell positive leaves its intended local nodes")

    # Model steady-state sourcing through ohmic parts and named semiconductor paths.
    # Protected return is a sink/reference, and transient/leakage validation is a bench task.
    # Conservatively allow reverse feed inside U1 from the pack to both VIN and LX.
    edges = defaultdict(set)

    def connect(source_net, destination_net, both_directions=False):
        edges[source_net].add(destination_net)
        if both_directions:
            edges[destination_net].add(source_net)

    def pair(part, first_pad, second_pad, both_directions=False):
        connect(pins[part, first_pad], pins[part, second_pad], both_directions)

    for part in values:
        if re.fullmatch(r"R[0-9]+", part):
            pair(part, "1", "2", True)
    for part in ("F1", "L1", "TH1"):
        pair(part, "1", "2", True)
    pair("RS1", "P1", "P2", True)
    pair("RS1", "P1", "K1", True)
    pair("RS1", "P2", "K2", True)
    first_source = next(pad for pad, alias in protection_pads.items() if alias == "S1A")
    second_source = next(pad for pad, alias in protection_pads.items() if alias == "S2A")
    pair("Q1", first_source, second_source, True)
    pair("Q2", "3", "2", True)
    for part in ("U3", "U4"):
        pair(part, "5", "6")
    for part in ("D1", "D2"):
        pair(part, "1", "2")  # Clamp accepts sourcing toward return only.
    for part in ("Q3", "Q4", "Q5"):
        pair(part, "3", "2")  # Open drain sinks. Insulated gate has no ohmic connection.
    pair("U1", "21", "5")
    pair("U1", "21", "13")
    pair("U1", "21", "15")

    def reachable(starting_node):
        seen = set()
        pending = [starting_node]
        while pending:
            net_name = pending.pop()
            if net_name not in seen:
                seen.add(net_name)
                if net_name != PACK_RETURN:
                    pending.extend(edges[net_name] - seen)
        return seen

    external_nonreturn = {net for (part, pad), net in pins.items() if part in ("J1", "J3")} - {PACK_RETURN}
    for start in ("CELL_POS", "CELL_MID", PACK_POSITIVE):
        require(reachable(start).isdisjoint(external_nonreturn), f"{start} can source a pogo or auxiliary pad")
    for input_net, other_input in (("POGO_VBUS_IN", "VBUS_5V_CHG"), ("VBUS_5V_CHG", "POGO_VBUS_IN")):
        driven = reachable(input_net)
        require({"VBUS_OR", "CHARGER_VIN"} <= driven and other_input not in driven,
                f"{input_net} lacks a charger path or can back-feed the other connector")

    require(values["R5"] == "450k 1%" and values["F1"] == "0451002.MRL 2A"
            and f"{shunt_ohms * 1000:g}mR 1W" in values["RS1"], "ISET, fuse or shunt rating changed")
    iset_kilohms = float(values["R5"].split("k")[0])
    nominal_charge_milliamps = 90000 / iset_kilohms
    fuse_amps = 2.0
    continuous_amps = 1.5
    pulse_amps = 3.0
    require(nominal_charge_milliamps == 200, "Charge setting differs from 200 mA")
    require(continuous_amps < fuse_amps < pulse_amps and pulse_amps ** 2 * shunt_ohms < 1.0,
            "Fuse or shunt requires re-screening against D17")
    return [
        "DC sourcing model: CELL_POS, CELL_MID and PACK+_PROT cannot source any non-return J1 or J3 terminal.",
        "Protected pogo and aux grounds are the shared PACK-_PROT return. Leakage and fault currents are bench checks.",
        "U3/U4 source VBUS_OR only in the forward direction. Neither input can source the other in the model.",
        "U1.13 VIN is fed only from VBUS_OR through R4. L1 also starts on VBUS_OR.",
        "Harness J2: pad 1 PACK+_PROT after F1, pad 2 PACK-_PROT after Q1 and RS1.",
        f"ISET: 90000 / {iset_kilohms:g} kΩ = {nominal_charge_milliamps:g} mA nominal.",
        f"F1: {fuse_amps:g} A, {continuous_amps / fuse_amps:.0%} of rating continuous and "
        f"{pulse_amps / fuse_amps:.0%} at pulse. Pulse duration and repetitive-pulse qualification remain open.",
        f"RS1: {shunt_ohms * 1000:g} mΩ, 1 W at 70 °C. "
        f"{continuous_amps * shunt_ohms * 1000:g} mV / {continuous_amps ** 2 * shunt_ohms:.4f} W at 1.5 A; "
        f"{pulse_amps * shunt_ohms * 1000:g} mV / {pulse_amps ** 2 * shunt_ohms:.3f} W at 3 A.",
    ]


def build_bom(schematic):
    rows = []
    for part in schematic.findall("parts/part"):
        reference = part.get("name")
        if reference.startswith("FRAME"):
            continue
        library_name = part.get("library")
        deviceset = part.get("deviceset")
        package = schematic.find(f"libraries/library[@name='{library_name}']"
                                 f"/devicesets/deviceset[@name='{deviceset}']/devices/device").get("package")
        status = "fit"
        if reference in ("BT1", "BT2", "J2"):
            status = "solder lands only"
        elif reference == "TH1":
            status = "wired to pack"
        elif reference.startswith("TP"):
            status = "test land only"
        rows.append((reference, part.get("value"), package, deviceset, MANUFACTURER_PARTS.get(reference, ""), status))
    return rows


def erc_report(result, checks, net_total, pad_total):
    error_count = sum(issue["type"] == 0 for issue in result["issues"])
    warnings = [issue for issue in result["issues"] if issue["type"] == 1 and issue["state"] == 0]
    approvals = [issue for issue in result["issues"] if issue["type"] == 1 and issue["state"] == 2]
    require(result["checked"] and error_count == 0 and len(warnings) + len(approvals) == len(result["issues"]),
            "Native ERC failed or returned an unknown issue state")
    require(not approvals, "SCH-4a records zero warning approvals")
    warning_reasons = {
        "FET_COMMON_DRAIN": "Q1 common drain and exposed pad form a local copper island.",
        "SAI1_BCLK_M0": "Left amp clock terminal is reserved for SCH-4b.",
        "SAI1_LRCK_M0": "Left amp word-clock terminal is reserved for SCH-4b.",
        "SAI1_SDO0_M0": "Left amp data terminal is reserved for SCH-4b.",
        "SD_MODE_L": "Left amp shutdown terminal is reserved for SCH-4b.",
    }
    lines = [
        f"Fusion ERC — {result['document']} (Autodesk Fusion {result['fusion']})",
        f"Schematic checked: {result['checked']}",
        f"{error_count} errors, {len(warnings)} active warnings, {len(approvals)} warning approvals.",
        f"Native vs source: matched {net_total} named nets and {pad_total} connected physical pads.",
        "",
        *checks,
        "",
        "Active issues (no approvals)",
    ]
    for issue in warnings:
        net_name = issue["description"].rsplit(" ", 1)[-1]
        require(issue["code"] == 106 and net_name in warning_reasons, f"Unexpected warning: {issue}")
        lines.append(f"Sheet {issue['sheet']} / code 106 / {issue['description']}. {warning_reasons[net_name]}")
    return "\n".join(lines) + "\n"


def main():
    source = ElementTree.parse(BOARD_DIRECTORY / SCHEMATIC_NAME).find("drawing/schematic")
    rows = native_rows(FUSION_EXPORTS / NETLIST)
    expected = expected_rows(source)
    native = set(rows)
    require(len(rows) == len(native), "Duplicate Fusion netlist row")
    require(native == expected, f"Missing in Fusion: {sorted(expected - native)}. Unexpected: {sorted(native - expected)}")
    pins = {(part, pad): net_name for net_name, part, pad, pin, sheet in rows}
    values = {part.get("name"): part.get("value") for part in source.findall("parts/part")}
    checks = check_paths(pins, values)
    results = json.loads((FUSION_EXPORTS / "erc.json").read_text(encoding="utf-8"))
    report = erc_report(results, checks, len({row[0] for row in rows}), len(pins))
    output_bom = build_bom(source)

    OUTPUT.mkdir(exist_ok=True)
    shutil.copyfile(FUSION_EXPORTS / "SCH-4a.pdf", OUTPUT / "SCH-4a.pdf")
    native_text = (FUSION_EXPORTS / NETLIST).read_text(encoding="utf-8")
    (OUTPUT / NETLIST).write_text(native_text.rstrip() + "\n", encoding="utf-8")
    with (OUTPUT / NETLIST.replace(".txt", ".csv")).open("w", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(("net", "part", "pad", "pin", "sheet"))
        writer.writerows(rows)
    with (OUTPUT / "FRIDAY_Left_SCH4a_BOM.csv").open("w", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(("refdes", "value", "package", "deviceset", "manufacturer_part", "assembly"))
        writer.writerows(output_bom)
    (OUTPUT / "FRIDAY_Left_SCH4a_ERC.txt").write_text(report, encoding="utf-8")
    print(report, end="")


if __name__ == "__main__":
    main()
