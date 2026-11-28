#!/usr/bin/env python3
"""Check the native SCH-3 netlist, reset timing and flex budget before writing outputs."""

import csv
import json
import shutil
import xml.etree.ElementTree as ElementTree
from pathlib import Path

from gen_sch3 import (
    AVDD, BOARD_DIRECTORY, DOVDD, DVDD, ENABLE, ENABLE_LOCAL, INPUT, MIC_POWER,
    REPOSITORY, SCHEMATIC_NAME,
)
from check_sch4a_exports import expected_rows, native_rows, require


FUSION_EXPORTS = Path("/tmp/friday-sch3-fusion")
OUTPUT = BOARD_DIRECTORY / "out"
NETLIST = "FRIDAY_Bridge_SCH3_netlist.txt"


def read_table(path):
    with path.open(newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))


def check_connections(pins, source, native_schematic):
    def match(reference, connections):
        for pad, expected_net in connections.items():
            require(pins.get((reference, pad)) == expected_net,
                    f"{reference}.{pad} must be on {expected_net}")

    def part_pads(reference):
        return {pad: net for (part, pad), net in pins.items() if part == reference}

    with (REPOSITORY / "hardware/interconnect/pinout_right_bridge.csv").open(newline="") as stream:
        flex_pins = {row["pin"]: row["net"] for row in csv.DictReader(stream)}
    require(len(flex_pins) == 24 and part_pads("J2") == flex_pins, "J2 differs from the 24-pin flex CSV")
    require(not part_pads("J1"), "J1 must remain electrically open until the DF37 crosswalk is proven")
    crosswalk = read_table(BOARD_DIRECTORY / "df37_crosswalk.csv")
    sensor_pins = read_table(REPOSITORY / "hardware/interconnect/pinout_bridge_sensor.csv")
    require(len(crosswalk) == 30 and all(row["hirose_contact_no"] == row["footprint_pad"] == "UNPROVEN"
                                        for row in crosswalk), "Unproven DF37 crosswalk changed")
    require([(row["pi_j2_pin"], row["signal"]) for row in crosswalk]
            == [(row["pin"], row["net"]) for row in sensor_pins], "Crosswalk logical pins differ from sensor CSV")
    flex_pairs = {net for net in flex_pins.values() if net.startswith("CSI0_")}
    sensor_pairs = {row["net"] for row in sensor_pins if row["type"] == "HS-diff"}
    require(len(flex_pairs) == 6 and flex_pairs == sensor_pairs, "CSI names differ between CSVs")
    for reference, lane in (("L2", "D0"), ("L3", "D1"), ("L4", "CLK")):
        negative, positive = f"CSI0_{lane}_N", f"CSI0_{lane}_P"
        match(reference, {"1": negative, "4": positive, "2": f"{negative}_SENSOR", "3": f"{positive}_SENSOR"})

    match("U1", {"1": ENABLE_LOCAL, "3": "CAM_DVDD_SW", "4": INPUT, "5": "CAM_DVDD_FB"})
    match("L1", {"1": "CAM_DVDD_SW", "2": DVDD})
    match("U2", {"1": INPUT, "3": ENABLE_LOCAL, "5": AVDD})
    match("U3", {"1": INPUT, "3": ENABLE_LOCAL, "5": DOVDD})
    match("U4", {"2": ENABLE, "4": ENABLE_LOCAL, "5": INPUT})
    match("X1", {"1": DOVDD, "2": "GND", "3": "CAM_MCLK_XO", "4": DOVDD})
    match("R5", {"1": "CAM_MCLK_XO", "2": "MCLK"})
    match("U5", {"1": ENABLE_LOCAL, "3": None, "4": None, "5": None,
                 "8": "POR_SENSE_AVDD", "9": "POR_SENSE_DOVDD", "10": "POR_SENSE_DVDD",
                 "14": INPUT, "15": "XCLR", "16": "XCLR", "17": "XCLR"})
    for top, bottom, rail, sense in (("R6", "R7", DVDD, "POR_SENSE_DVDD"),
                                      ("R8", "R9", DOVDD, "POR_SENSE_DOVDD"),
                                      ("R10", "R11", AVDD, "POR_SENSE_AVDD")):
        match(top, {"1": rail, "2": sense})
        match(bottom, {"1": sense, "2": "GND"})
    match("R12", {"1": DOVDD, "2": "XCLR"})
    match("R13", {"1": "CAM_MCLK_RESERVED", "2": "MCLK"})
    match("R14", {"1": "CAM_RST_L_RESERVED", "2": "XCLR"})
    pullups = (("R15", "I2C_CAM_SCL"), ("R16", "I2C_CAM_SDA"))
    for reference, net in pullups:
        match(reference, {"1": DOVDD, "2": net})
        require({part for (part, pad), candidate_net in pins.items() if candidate_net == net} == {reference, "J2"},
                f"Unexpected second pull-up or branch on {net}")
    for schematic in (source, native_schematic):
        unpopulated = {part.get("name") for part in schematic.findall("parts/part")
                       if part.find("variant[@name='default'][@populate='no']") is not None}
        require(unpopulated == {"R13", "R14"}, "Both host overrides must be DNP in Fusion and source")

    for reference, channel in (("MK1", "GND"), ("MK2", MIC_POWER)):
        match(reference, {"1": "SAI1_BCLK_M0", "2": "SAI1_SDI0_M0", "3": "SAI1_LRCK_M0",
                          "4": channel, "6": "GND", "7": MIC_POWER, "8": MIC_POWER})
    for reference, supply in (("C16", MIC_POWER), ("C17", MIC_POWER)):
        match(reference, {"1": supply, "2": "GND"})
    match("R17", {"1": "SAI1_SDI0_M0", "2": "GND"})
    host_supply_endpoints = {contact for contact, net in pins.items() if net == MIC_POWER}
    require(host_supply_endpoints == {("J2", "20"), ("MK1", "7"), ("MK1", "8"), ("MK2", "4"),
                                      ("MK2", "7"), ("MK2", "8"), ("C16", "1"), ("C17", "1")},
            "A camera supply or another load is attached to the host microphone rail")
    for index, net in enumerate((DVDD, AVDD, DOVDD, "MCLK", "XCLR", ENABLE, "CAM_MCLK_RESERVED",
                                 "CAM_RST_L_RESERVED", "CAM_CRADLE_NTC_RESERVED", "SAI1_SDI0_M0"), start=1):
        match(f"TP{index}", {"1": net})


def calculations(values):
    def ohms(reference):
        value = values[reference].split()[0]
        require(value.endswith("k"), f"Expected kilo-ohm value on {reference}")
        return float(value[:-1]) * 1000

    def sense_bounds(top, bottom):
        upper = ohms(top)
        lower = ohms(bottom)
        tolerance = 0.001
        maximum_leakage = 25e-9
        # TPS386000 p.7: 396–404 mV falling plus 3.5–10 mV hysteresis.
        low = 0.3995 * (1 + upper * (1 - tolerance) / (lower * (1 + tolerance)))
        high = 0.414 * (1 + upper * (1 + tolerance) / (lower * (1 - tolerance)))
        error = maximum_leakage * upper * (1 + tolerance)
        return low - error, high + error

    dvdd_min, dvdd_max = sense_bounds("R6", "R7")
    dovdd_min, dovdd_max = sense_bounds("R8", "R9")
    avdd_min, avdd_max = sense_bounds("R10", "R11")
    oscillator_supply_min = 1.62
    oscillator_start_ms = 5.0
    reset_delay_min_ms = 14.0
    require(values["X1"] == "SIT1602BI-71-18E-24.000000D" and values["U5"] == "TPS386000RGPR",
            "Recheck startup guarantees if POR or oscillator changes")
    require(dovdd_min > oscillator_supply_min and reset_delay_min_ms > oscillator_start_ms,
            "POR may release before guaranteed oscillator startup")
    require(dvdd_max < 1.07 and dovdd_max < 1.8 * 0.98 and avdd_max < 2.8 * 0.98,
            "POR reset may remain asserted near the low output tolerance")
    nominal_buck = 0.6 * (1 + ohms("R1") / ohms("R2"))
    require(abs(nominal_buck - 1.1) < 0.0001, "DVDD target changed")

    maximum_pullup = ohms("R15") * 1.01
    require(values["R15"] == values["R16"] == "2.2k 1%", "I2C pull-up expectation changed")
    estimated_bus_pf = 70.0
    rise_ns = 0.8473 * maximum_pullup * estimated_bus_pf / 1000
    fast_mode_limit_pf = 300.0 * 1000 / (0.8473 * maximum_pullup)
    require(rise_ns < 300, "I2C estimate exceeds the Fast-mode rise-time limit")

    current_screen = 0.350
    loop_ohms = 0.228
    drop_at_screen = current_screen * loop_ohms
    assumed_efficiency = 0.85
    dvdd_watts = 1.1 * 0.60
    linear_and_overhead_amps = 0.050 + 0.050 + 0.006 + 0.001
    nominal_current = dvdd_watts / (assumed_efficiency * (3.3 - drop_at_screen)) + linear_and_overhead_amps
    corner_current = dvdd_watts / (assumed_efficiency * (3.3 * 0.95 - drop_at_screen)) + linear_and_overhead_amps
    require(nominal_current < current_screen < corner_current, "Re-evaluate the camera input-screen status")

    return [
        "J2: 24/24 pins exactly match the right–bridge CSV. J1: 0 of 30 pads connected; crosswalk UNPROVEN.",
        "All six CSI names and polarities match both CSVs. L2–L4 sensor-side endpoints remain isolated from J1.",
        "All three camera regulators draw from VCC_3V3_S3. VCC_1V8_S0 serves the two microphones only.",
        "Host clock/reset links R13/R14 are DNP in the source and native Fusion export.",
        f"POR rising windows: DVDD {dvdd_min:.3f}–{dvdd_max:.3f} V, DOVDD {dovdd_min:.3f}–{dovdd_max:.3f} V, "
        f"AVDD/AFVDD {avdd_min:.3f}–{avdd_max:.3f} V.",
        f"POR healthy-start margin: {reset_delay_min_ms:g} ms min − {oscillator_start_ms:g} ms max "
        f"= {reset_delay_min_ms - oscillator_start_ms:g} ms. DOVDD release sensing starts above 1.62 V.",
        f"I2C: 2.2 kΩ ±1% bridge-only pull-ups, {rise_ns:.0f} ns at estimated {estimated_bus_pf:.0f} pF; "
        f"{fast_mode_limit_pf:.0f} pF modeled ceiling at 300 ns.",
        f"VCC_3V3_S3, 2+2 contacts, 0.350 A provisional screen: {drop_at_screen * 1000:.1f} mV flex drop at screen.",
        f"3.300 V nominal source: {nominal_current * 1000:.0f} mA estimated. 3.135 V source corner: "
        f"{corner_current * 1000:.0f} mA estimated at 85% efficiency — OVER SCREEN.",
        "Current estimates exclude unmeasured startup and real flex sharing. Qualification remains open.",
    ]


def build_bom(schematic):
    fitted_parts = {
        "J1": "DF37NC-30DS-0.4V(51)", "J2": "FH12-24S-0.5SH(55)",
        "U1": "AP3429KTTR-G1", "U2": "AP7331-28WG-7", "U3": "AP7331-18WG-7",
        "U4": "SN74LV1T34DBVR", "U5": "TPS386000RGPR",
        "X1": "SIT1602BI-71-18E-24.000000D", "L1": "XFL4020-222MEC",
        **{f"L{index}": "DLP11SN900HL2L" for index in range(2, 5)}, "MK1": "INMP441", "MK2": "INMP441",
    }
    rows = []
    for part in schematic.findall("parts/part"):
        reference = part.get("name")
        if reference.startswith("FRAME"):
            continue
        library = part.get("library")
        deviceset = part.get("deviceset")
        package = schematic.find(f"libraries/library[@name='{library}']"
                                 f"/devicesets/deviceset[@name='{deviceset}']/devices/device").get("package")
        assembly = "fit"
        if part.find("variant[@name='default'][@populate='no']") is not None:
            assembly = "DNP"
        elif reference == "J1":
            assembly = "crosswalk hold"
        elif reference.startswith("TP"):
            assembly = "test land only"
        rows.append((reference, part.get("value"), package, fitted_parts.get(reference, ""), assembly))
    return rows


def erc_text(result, checks, net_count, terminal_count):
    issues = result["issues"]
    errors = [issue for issue in issues if issue["type"] == 0]
    active = [issue for issue in issues if issue["type"] == 1 and issue["state"] == 0]
    approvals = [issue for issue in issues if issue["type"] == 1 and issue["state"] == 2]
    require(result["checked"] and not errors and not approvals and len(active) == len(issues),
            f"Native ERC failed or unexpected approvals are present: {issues}")
    lines = [
        f"Fusion ERC — {result['document']} (Autodesk Fusion {result['fusion']})",
        f"{len(errors)} errors, {len(active)} active warnings, {len(approvals)} warning approvals.",
        f"Native source comparison: {net_count} nets and {terminal_count} connected physical pads.",
        "", *checks, "", "Active warnings",
    ]
    for issue in active:
        description = issue["description"]
        if issue["code"] == 104 and description in {
            f"POWER pin MK1 VDD connected to {MIC_POWER}", f"POWER pin MK2 VDD connected to {MIC_POWER}",
        }:
            reason = "Mic VDD uses the documented 1.8 V host rail."
        elif issue["code"] == 106 and description.startswith("Only one pin on net CSI0_") and description.endswith("_SENSOR"):
            reason = "Sensor-side choke node awaits the DF37 contact crosswalk."
        else:
            raise ValueError(f"Unexpected active ERC warning: {issue}")
        lines.append(f"Sheet {issue['sheet']} / code {issue['code']} / {description}. {reason}")
    return "\n".join(lines) + "\n"


def write_csv(path, fields, rows):
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(fields)
        writer.writerows(rows)


def main():
    source = ElementTree.parse(BOARD_DIRECTORY / SCHEMATIC_NAME).find("drawing/schematic")
    native_schematic = ElementTree.parse(FUSION_EXPORTS / SCHEMATIC_NAME).find("drawing/schematic")
    rows = native_rows(FUSION_EXPORTS / NETLIST)
    native = set(rows)
    expected = expected_rows(source)
    require(len(rows) == len(native) and native == expected,
            f"Fusion/source mismatch. Missing: {sorted(expected - native)}. Extra: {sorted(native - expected)}.")
    pins = {(part, pad): net for net, part, pad, pin, sheet in rows}
    check_connections(pins, source, native_schematic)
    values = {part.get("name"): part.get("value") for part in source.findall("parts/part")}
    checks = calculations(values)
    result = json.loads((FUSION_EXPORTS / "erc.json").read_text(encoding="utf-8"))
    report = erc_text(result, checks, len({row[0] for row in rows}), len(pins))

    OUTPUT.mkdir(exist_ok=True)
    shutil.copyfile(FUSION_EXPORTS / "SCH-3.pdf", OUTPUT / "SCH-3.pdf")
    native_text = (FUSION_EXPORTS / NETLIST).read_text(encoding="utf-8")
    (OUTPUT / NETLIST).write_text(native_text.rstrip() + "\n", encoding="utf-8")
    write_csv(OUTPUT / NETLIST.replace(".txt", ".csv"), ("net", "part", "pad", "pin", "sheet"), rows)
    write_csv(OUTPUT / "FRIDAY_Bridge_SCH3_BOM.csv",
              ("refdes", "value", "package", "manufacturer_part", "assembly"), build_bom(source))
    (OUTPUT / "FRIDAY_Bridge_SCH3_ERC.txt").write_text(report, encoding="utf-8")
    print(report, end="")


if __name__ == "__main__":
    main()
