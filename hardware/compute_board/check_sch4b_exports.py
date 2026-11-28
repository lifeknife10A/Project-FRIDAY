#!/usr/bin/env python3
"""Verify both native SCH-4b exports, or capture the audited eMCP warning set."""

import argparse
import csv
import json
import shutil
import xml.etree.ElementTree as ElementTree
from pathlib import Path

from gen_sch4b_compute import (
    ADC_REFERENCE_SOURCE, APPROVAL_REASON, APPROVALS_PATH, BOARD_DIRECTORY, PACK_INPUT,
    REPOSITORY, SCHEMATIC_NAME, SOC_BALLS, connector_pins,
)
from check_sch4a_exports import expected_rows, native_rows, require
from check_sch4b_left import check_left
from sch4b_audio import gpio_channel_screen, sd_mode_screen


FUSION_DIRECTORY = Path("/tmp/friday-sch4b-fusion")
LEFT_DIRECTORY = BOARD_DIRECTORY.parent / "left_temple"
LEFT_FILE = "FRIDAY_Left_SCH4b.sch"
BRIDGE_DIRECTORY = BOARD_DIRECTORY.parent / "bridge_board"
BASELINE_COMPUTE_OUT = BOARD_DIRECTORY / "out/FRIDAY_Compute_SCH2_netlist.csv"
BASELINE_LEFT_OUT = LEFT_DIRECTORY / "out/FRIDAY_Left_SCH4a_netlist.csv"


def report_for(board):
    return json.loads((FUSION_DIRECTORY / board / "erc.json").read_text(encoding="utf-8"))


def record_audited_approvals():
    audited = set()
    source_report = BOARD_DIRECTORY / "out/FRIDAY_Compute_SCH2_ERC.txt"
    for line in source_report.read_text(encoding="utf-8").splitlines():
        if "POWER pin U11POWER " not in line or not line.endswith("| active"):
            continue
        sheet, code, location, ball, description, state = (field.strip() for field in line.split("|"))
        x, y = (float(coordinate) for coordinate in location.strip("()").split(","))
        require(code == "104" and bool(ball) and state == "active", f"Unexpected baseline warning: {line}")
        audited.add((sheet, x, y, description))

    candidate_signatures = []
    matched = set()
    native = report_for("Compute")
    require(native["checked"] and not any(issue["type"] == 0 for issue in native["issues"]),
            "Native ERC must finish with zero errors before applying approvals")
    for issue in native["issues"]:
        if issue["code"] == 104 and issue["state"] == 0 and issue["description"].startswith("POWER pin U11POWER "):
            signature = issue["signature"]
            code, sheet, x, y, part, pin, net, *unused = signature.split("\t")
            key = (sheet, float(x), float(y), issue["description"])
            require(key in audited and key not in matched and part == "U11POWER",
                    f"eMCP warning differs from the audited report: {signature}")
            matched.add(key)
            candidate_signatures.append(signature)
    require(len(audited) == len(matched) == len(candidate_signatures) == 65,
            "Expected all 65 inherited eMCP warnings from SCH-2")
    records = {"reason": APPROVAL_REASON, "signatures": sorted(candidate_signatures)}
    APPROVALS_PATH.write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Matched 65 inherited code-104 signatures exactly to {source_report.name}.")


def read_csv_connections(path):
    with path.open(newline="", encoding="utf-8") as stream:
        rows = csv.DictReader(stream)
        rows.fieldnames = [field.lower() for field in rows.fieldnames]
        return {(row["part"], row["pad"]): row["net"] for row in rows}


def verify_native(board_directory, schematic_name, board_label):
    source = ElementTree.parse(board_directory / schematic_name).find("drawing/schematic")
    native_copy = ElementTree.parse(FUSION_DIRECTORY / board_label / schematic_name).find("drawing/schematic")
    native_text = FUSION_DIRECTORY / board_label / (Path(schematic_name).stem + "_netlist.txt")
    rows = native_rows(native_text)
    expected = {(net, part, pad, sheet) for net, part, pad, pin, sheet in expected_rows(source)}
    physical = {(net, part, pad, sheet) for net, part, pad, pin, sheet in rows}
    require(len(physical) == len(rows) and physical == expected,
            f"{board_label} native/source mismatch. Missing {sorted(expected - physical)[:12]}. "
            f"Extra {sorted(physical - expected)[:12]}.")
    pins = {(part, pad): net for net, part, pad, pin, sheet in rows}
    values = {part.get("name"): part.get("value") for part in source.findall("parts/part")}
    return source, native_copy, native_text, rows, pins, values


def compare_baseline(reference_file, pins, skip=()):
    baseline = read_csv_connections(reference_file)
    for connection, net in baseline.items():
        if connection[0] not in skip:
            require(pins.get(connection) == net, f"Baseline connection changed: {connection} expected {net}")
    return sum(part not in skip for part, pad in baseline)


def check_compute(pins, values, left_pins, native_copy):
    for ball, net in SOC_BALLS.items():
        require(pins.get(("U1", ball)) == net, f"RK3576 U1.{ball} must be on {net}")
    bridge_pins = read_csv_connections(BRIDGE_DIRECTORY / "out/FRIDAY_Bridge_SCH3_netlist.csv")
    for host, template, other, other_connector in (
        ("J5", "pinout_right_bridge.csv", bridge_pins, "J2"),
        ("J6", "pinout_right_left_aux.csv", left_pins, "J3"),
    ):
        expected = connector_pins(template)
        actual = {pad: net for (part, pad), net in pins.items() if part == host and pad.isdigit()}
        require(actual == expected, f"{host} differs from {template}")
        actual_other = {pad: net for (part, pad), net in other.items() if part == other_connector and pad.isdigit()}
        expected_other = {pad: "PACK-_PROT" if host == "J6" and net == "GND" else net for pad, net in expected.items()}
        require(actual_other == expected_other, f"{host} mate differs from {template}")
    matches = {
        ("J4", "1"): PACK_INPUT, ("J4", "2"): "GND", ("U10", "7"): PACK_INPUT,
        ("R801", "1"): "SAI1_BCLK_SOC", ("R801", "2"): "SAI1_BCLK_M0",
        ("R802", "1"): "SAI1_LRCK_SOC", ("R802", "2"): "SAI1_LRCK_M0",
        ("R803", "1"): "VCC5V0_SYS_S5", ("R803", "2"): "VCC5V0_SYS_S5_AMP",
        ("R804", "1"): "CAM_ENABLE_SOC", ("U12", "4"): "CAM_ENABLE",
        ("U13", "1"): "USB_CHG_ALLOW", ("U13", "5"): "VBUS_5V", ("U13", "6"): "VBUS_5V_CHG",
        ("U13", "9"): "USB_CHG_ILM", ("R807", "1"): "USB_CHG_ILM", ("R807", "2"): "GND",
        ("U14", "2"): "USB_CHG_ALLOW_SOC", ("U14", "4"): "USB_CHG_ALLOW",
        ("U18", "2"): "CHG_EN_SINK_CTRL", ("U18", "3"): "GND", ("U18", "4"): "CHG_EN",
        ("R810", "1"): "VCC_1V8_S0", ("R810", "2"): "DOCK_DET",
        ("R811", "1"): "VCC_1V8_S0", ("R811", "2"): "CHG_STAT",
        ("R812", "1"): "VCC_1V8_S3", ("R812", "2"): "CHG_EN",
        ("R814", "1"): PACK_INPUT, ("R814", "2"): "PACK_DIV_FILTER",
        ("R815", "1"): "PACK_DIV_FILTER", ("R815", "2"): "GND",
        ("R816", "1"): "PACK_SARADC_IN2", ("R816", "2"): "GND",
        ("U15", "14"): ADC_REFERENCE_SOURCE, ("U15", "1"): ADC_REFERENCE_SOURCE,
        ("U15", "2"): "PACK_DIV_FILTER", ("U15", "3"): "PACK_SARADC_IN2",
        ("U16", "1"): "SAI1_SDO0_M0", ("U16", "4"): "AMP_R_SD_MODE",
        ("U16", "16"): "SAI1_BCLK_M0", ("U16", "14"): "SAI1_LRCK_M0",
        ("J7", "1"): "SPK_R_P", ("J7", "2"): "SPK_R_N",
    }
    for connection, net in matches.items():
        require(pins.get(connection) == net, f"{connection} must be on {net}")
    for net, contact, ball in (("I2C_CAM_SCL", "11", "1E9"), ("I2C_CAM_SDA", "12", "1D12")):
        require({connection for connection, candidate in pins.items() if candidate == net}
                == {("J5", contact), ("U1", ball)}, f"Unexpected compute pull-up on {net}")
    dnp = {part.get("name") for part in native_copy.findall("parts/part")
           if part.find("variant[@name='default'][@populate='no']") is not None}
    require({"TP801", "TP802", "TP803"} <= dnp, "Missing native DNP camera reservations")
    require(values["R801"] == values["R802"] == "22R 1%", "SAI clock damping changed")
    require(values["R823"] == "16.2k 1%" and values["R824"] == "4.7k 1%" and values["R825"] == "100k 1%",
            "Right audio channel or gain strap changed")

    right_low, right_high, right_off = sd_mode_screen(16200)
    require(0.825 < right_low < right_high < 1.245 and right_off < 0.080,
            "Right channel or shutdown fails MAX98357A thresholds")
    require((values["R814"], values["R815"], values["R816"]) == ("1M 1%", "220k 1%", "100k 1%"),
            "Pack ADC divider values changed")
    lower = 1 / (1 / 220000 + 1 / 100000)
    pack_max = 8.5
    adc_nominal = pack_max * lower / (1000000 + lower)
    adc_max = pack_max * (lower * 1.01) / (1000000 * 0.99 + lower * 1.01)
    adc_input_max_disconnected = pack_max * (220000 * 1.01) / (1000000 * 0.99 + 220000 * 1.01)
    adc_current_max = pack_max / ((1000000 + lower) * 0.99)
    require(adc_input_max_disconnected < 1.62 and adc_current_max < 10e-6, "ADC range or pack leakage screen failed")
    require(values["R812"] == "22k 1%" and values["U18"] == "SN74LVC1G06DBVR",
            "CHG_EN sink or pull-up changed")
    chg_sink_max = 1.95 / (22000 * 0.99)
    require(chg_sink_max < 100e-6, "CHG_EN exceeds the 100 µA guaranteed low-voltage test condition")
    require(values["R807"] == "6.57k 0.1%", "USB eFuse limit changed")
    ilim_typ = 3334 / 6570
    ilim_high_screen = 0.575 * 6650 / 6570 * 1.001
    ilim_low_screen = 0.425 * 6650 / 6570 * 0.999
    charger_nominal = 8.4 * 0.20 / (5 * 0.85)
    charger_low_line = 8.5 * 0.20 / (4.5 * 0.85)
    require(charger_nominal < ilim_typ and ilim_high_screen < 3 * 0.25,
            "eFuse is outside the nominal charger or flex-current screen")

    return [
        "J5 and J6 match both CSVs and their far-end netlists. J6 reserved contacts 15–17 open; "
        "left protected return maps to compute GND.",
        "All six CSI signal names and polarities match the bridge, including clock. Compute I2C has no local pull-ups.",
        "All 20 RK3576 ball connections and the existing J4/SY8205 path verified.",
        f"CHG_EN open-drain low: ≤0.100 V with ≤{chg_sink_max * 1e6:.1f} µA from its 22 kΩ pull-up.",
        gpio_channel_screen(),
        "SAI1 BCLK/LRCK: 22 Ω at the SoC. 65 mm + 130 mm flex estimate plus local branches: about 46 pF per clock.",
        f"Right SD_MODE high: {right_low:.3f}–{right_high:.3f} V at 4.50–5.50 V, wholly within "
        f"0.825–1.245 V. Shutdown screen ≤{right_off * 1000:.1f} mV at the rated 55 °C P-FET leakage point.",
        f"SARADC at 8.5 V: {adc_nominal:.3f} V nominal, {adc_max:.3f} V resistor-tolerance high, "
        f"and {adc_input_max_disconnected:.3f} V unloaded vs 1.62 V minimum full-scale rail.",
        f"SARADC divider maximum direct pack draw {adc_current_max * 1e6:.2f} µA. "
        "TMUX1511 powered-off isolation is backed by the ADC-side 100 kΩ resistor.",
        f"USB eFuse {ilim_typ:.3f} A typical. Scaled screen {ilim_low_screen:.3f}–{ilim_high_screen:.3f} A; "
        "three flex contacts in each direction screen at 0.750 A total.",
        f"0.20 A charging estimates {charger_nominal:.3f} A at 5.0 V and {charger_low_line:.3f} A at "
        "4.5 V / 8.5 V pack, assuming 85% efficiency. Full current is not guaranteed at the low-line/current-limit corner.",
    ]


def native_erc_text(result, source, reference, diagnostics, rows, compute):
    errors = [issue for issue in result["issues"] if issue["type"] == 0]
    active = [issue for issue in result["issues"] if issue["type"] == 1 and issue["state"] == 0]
    approved = [issue for issue in result["issues"] if issue["type"] == 1 and issue["state"] == 2]
    require(result["checked"] and not errors and len(active) + len(approved) == len(result["issues"]),
            f"Unexpected native ERC result for {result['document']}")
    approved_signatures = {issue["signature"] for issue in approved}
    memory = set(json.loads(APPROVALS_PATH.read_text(encoding="utf-8"))["signatures"]) if compute else set()
    baseline_signatures = {item.get("hash") for item in reference.findall("errors/approved")}
    source_signatures = {item.get("hash") for item in source.findall("errors/approved")}
    require(approved_signatures == source_signatures == baseline_signatures | memory,
            "Native and generated approvals must equal the baseline plus only the audited memory signatures")
    lines = [
        f"Fusion ERC — {result['document']} (Autodesk Fusion {result['fusion']})",
        f"{len(errors)} errors, {len(active)} active warnings, {len(baseline_signatures)} inherited approvals, "
        f"{len(memory)} newly approved inherited eMCP warnings.",
        f"Matched {len({row[0] for row in rows})} native nets and {len(rows)} physical pad connections.", "",
        *diagnostics, "", "Active warnings",
    ]
    amplifier = "U16" if compute else "U5"
    messages = {
        f"POWER pin {amplifier} VDD connected to {'VCC5V0_SYS_S5' if compute else 'VCC5V0_SYS_S5_AMP'}":
            "MAX98357A power input uses the named local 5 V supply.",
        f"POWER pin {amplifier} EP connected to {'GND' if compute else 'PACK-_PROT'}":
            "Connect the exposed pad to the local ground as specified by MAX98357A.",
        "POWER pin U5 GND connected to PACK-_PROT": "Left-board return is the protected pack negative.",
        "Only one pin on net FET_COMMON_DRAIN": "Q1 has one logical common-drain terminal covering physical pins 2 and 3.",
    }
    for issue in active:
        message = issue["description"]
        require(message in messages, f"Unexpected active warning: {message}")
        lines.append(f"Sheet {issue['sheet']} / code {issue['code']} / {message}. {messages[message]}")
    if memory:
        lines.extend(("", f"Newly approved inherited eMCP power warnings: {APPROVAL_REASON}",
                      f"Exact signatures: {APPROVALS_PATH.name}"))
    return "\n".join(lines) + "\n"


def write_bom(output, source):
    with output.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(("refdes", "value", "package", "library", "assembly"))
        libraries = {library.get("name"): library for library in source.findall("libraries/library")}
        for part in source.findall("parts/part"):
            name, library_name, deviceset, device = (part.get(key) for key in ("name", "library", "deviceset", "device"))
            device_xml = libraries[library_name].find(f"devicesets/deviceset[@name='{deviceset}']"
                                                      f"/devices/device[@name='{device}']")
            package = device_xml.get("package")
            if not package or name.startswith("FRAME"):
                continue
            assembly = "DNP" if part.find("variant[@name='default'][@populate='no']") is not None else "fit"
            if assembly == "fit" and (name.startswith("TP") or deviceset in ("CELL_TABS", "HARNESS_PADS", "BTL_SPEAKER")):
                assembly = "solder or test lands"
            writer.writerow((name, part.get("value"), package, library_name, assembly))


def export_files(directory, schematic_name, board_label, data, diagnostics):
    source, native_copy, native_text, rows, pins, values = data
    reference_file = "FRIDAY_Compute_SCH2.sch" if board_label == "Compute" else "FRIDAY_Left_SCH4a.sch"
    reference = ElementTree.parse(directory / reference_file).find("drawing/schematic")
    report = native_erc_text(report_for(board_label), source, reference, diagnostics, rows, board_label == "Compute")
    output = directory / "out"
    stem = Path(schematic_name).stem
    shutil.copyfile(FUSION_DIRECTORY / board_label / f"SCH-4b_{board_label}.pdf",
                    output / f"SCH-4b_{board_label}.pdf")
    (output / f"{stem}_netlist.txt").write_text(native_text.read_text(encoding="utf-8").rstrip() + "\n",
                                               encoding="utf-8")
    with (output / f"{stem}_netlist.csv").open("w", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(("net", "part", "pad", "pin", "sheet"))
        writer.writerows(rows)
    write_bom(output / f"{stem}_BOM.csv", source)
    (output / f"{stem}_ERC.txt").write_text(report, encoding="utf-8")
    print(report, end="")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record-emcp-approvals", action="store_true")
    arguments = parser.parse_args()
    if arguments.record_emcp_approvals:
        record_audited_approvals()
        return
    left = verify_native(LEFT_DIRECTORY, LEFT_FILE, "Left")
    compute = verify_native(BOARD_DIRECTORY, SCHEMATIC_NAME, "Compute")
    left_checks = check_left(left[4], left[5])
    compute_checks = check_compute(compute[4], compute[5], left[4], compute[1])
    left_checks.append(f"Preserved {compare_baseline(BASELINE_LEFT_OUT, left[4], skip=('Q1',))} baseline pads outside replaced Q1.")
    compute_checks.append(f"All {compare_baseline(BASELINE_COMPUTE_OUT, compute[4])} SCH-2 physical pad connections preserved.")
    export_files(LEFT_DIRECTORY, LEFT_FILE, "Left", left, left_checks)
    export_files(BOARD_DIRECTORY, SCHEMATIC_NAME, "Compute", compute, compute_checks)


if __name__ == "__main__":
    main()
