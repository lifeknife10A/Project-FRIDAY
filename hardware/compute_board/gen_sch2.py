#!/usr/bin/env python3
"""Extend the approved SCH-1 EAGLE schematic with the SCH-2 memory sheets."""

import csv
import re
import subprocess
import xml.etree.ElementTree as ElementTree
from collections import defaultdict

from gen_sch1 import BOARD_DIRECTORY, REPOSITORY, add_capacitor, add_part, add_segment


BASELINE = "d9d37a8817c88988a9d90a4aec9b9ea61df98dff"
SCHEMATIC_NAME = "FRIDAY_Compute_SCH2.sch"
EMCP_PART = "U11"
EMCP_LIBRARY = "H9HP52ACPMADAR"
EMCP_DEVICE = "H9HP52ACPMADAR-KMM"
DDR_POWER = {"VDD1": "VCC_1V8_S3", "VDD2": "VDD2_DDR_S3", "VDDQ": "VDDQ_DDR_S0"}
EMMC_POWER = {"VCC": "VCC_3V3_S0", "VCCQ": "VCC_1V8_S0", "VDDI": "EMMC_VDDI"}


def add_note(sheet, text, x, y, size="1.778"):
    ElementTree.SubElement(sheet.find("plain"), "text", x=str(x), y=str(y),
                           size=size, layer="94").text = text


def add_sheet(schematic, number, title, sources):
    sheet = ElementTree.SubElement(schematic.find("sheets"), "sheet")
    for name in ("plain", "instances", "busses", "nets"):
        ElementTree.SubElement(sheet, name)
    add_part(schematic, sheet, f"FRAME{number}", "A3_FRAME", "", 0, 0, "R0")
    add_note(sheet, f"PROJECT FRIDAY - S{number}: {title} | REV SCH-2", 12.7, 281.94, "2.54")
    add_note(sheet, sources, 12.7, 274.32)
    return sheet


def add_memory(schematic, ddr_sheet, power_sheet, emmc_sheet):
    library = ElementTree.parse(REPOSITORY / f"libraries/{EMCP_LIBRARY}.lbr").find("drawing/library")
    library.set("name", EMCP_LIBRARY)
    schematic.find("libraries").append(library)
    ElementTree.SubElement(schematic.find("parts"), "part", name=EMCP_PART, library=EMCP_LIBRARY,
                           deviceset=EMCP_DEVICE, device="", value=EMCP_DEVICE)
    for sheet, gate_name, x, y in (
        (ddr_sheet, "LPDDR4X_CHA", "106.68", "180.34"),
        (ddr_sheet, "LPDDR4X_CHB", "304.80", "180.34"),
        (power_sheet, "POWER", "91.44", "205.74"),
        (power_sheet, "GND", "294.64", "205.74"),
        (emmc_sheet, "EMMC", "106.68", "205.74"),
    ):
        ElementTree.SubElement(sheet.find("instances"), "instance", part=EMCP_PART,
                               gate=gate_name, x=x, y=y, rot="R0")
    return library


def pin_locations(schematic, part_name, library, deviceset):
    locations = {}
    symbols = {symbol.get("name"): symbol for symbol in library.findall("symbols/symbol")}
    for gate in deviceset.findall("gates/gate"):
        gate_name = gate.get("name")
        for sheet in schematic.findall("sheets/sheet"):
            instance = sheet.find(f"instances/instance[@part='{part_name}'][@gate='{gate_name}']")
            if instance is None:
                continue
            if instance.get("rot", "R0") != "R0":
                raise ValueError(f"Unexpected rotation for {part_name}.{gate_name}")
            for pin in symbols[gate.get("symbol")].findall("pin"):
                position_x = float(instance.get("x")) + float(pin.get("x"))
                position_y = float(instance.get("y")) + float(pin.get("y"))
                if pin.get("rot", "R0") not in ("R0", "R180"):
                    raise ValueError(f"Expected a horizontal pin on {part_name}.{gate_name}")
                direction = 1 if pin.get("rot") == "R180" else -1
                locations[gate_name, pin.get("name")] = (sheet, position_x, position_y, direction)
    return locations


def horizontal_stub(sheet, net_name, part_name, gate_name, pin_name, x, y, direction):
    end_x = x + (2.54 if direction > 0 else -20.32)
    add_segment(sheet, net_name, part_name, gate_name, pin_name, (x, y), (end_x, y))


def connect_pin(locations, part_name, connection, net_name):
    gate_name, pin_name = connection.get("gate"), connection.get("pin")
    sheet, x, y, direction = locations[gate_name, pin_name]
    horizontal_stub(sheet, net_name, part_name, gate_name, pin_name, x, y, direction)


def add_resistor(schematic, sheet, name, value, left_net, right_net, x, y,
                 deviceset="R_0201", populate=True):
    add_part(schematic, sheet, name, deviceset, value, x, y, "R0", populate)
    horizontal_stub(sheet, left_net, name, "G$1", "1", x - 5.08, y, -1)
    horizontal_stub(sheet, right_net, name, "G$1", "2", x + 5.08, y, 1)


def add_capacitor_bank(schematic, sheet, name, types, rail, first_number, row_y):
    number = first_number
    for deviceset, value, count in types:
        for _ in range(count):
            offset = number - first_number
            x = 25.4 + 30.48 * (offset % 12)
            y = row_y - 22.86 * (offset // 12)
            add_capacitor(schematic, sheet, f"C{number}", deviceset, value, rail, x, y)
            number += 1
    add_note(sheet, name, 12.7, row_y + 12.7, "1.524")


def add_power(schematic, power_sheet, emmc_sheet):
    # EVB PDF p. 24 R3809 and DshanPI sheet 18 R69 isolate the named CKE branch.
    pmic_sheet = schematic.findall("sheets/sheet")[1]
    buck_rail = pmic_sheet.find("nets/net[@name='VDDQ_DDR_CKE_S3']")
    buck_rail.set("name", DDR_POWER["VDD2"])
    add_resistor(schematic, power_sheet, "R3809", "0R", DDR_POWER["VDD2"],
                 "VDDQ_DDR_CKE_S3", 330.2, 121.92, deviceset="R_0603")
    add_note(power_sheet, "BUCK9 to DDRPHY_CKE_VDDQ", 298.45, 132.08, "1.524")

    add_capacitor_bank(schematic, power_sheet, "DDR VDD1 (1.8 V)", (
        ("C_0603", "10uF 10V X5R", 1), ("C_0402", "1uF 10V X5R", 1),
        ("C_0201", "100nF 10V X5R", 4),
    ), DDR_POWER["VDD1"], 3800, 121.92)
    add_capacitor_bank(schematic, power_sheet, "DDR VDD2 (1.1 V)", (
        ("C_0603", "22uF 10V X5R", 2), ("C_0603", "10uF 10V X5R", 2),
        ("C_0402", "1uF 10V X5R", 3), ("C_0201", "100nF 10V X5R", 10),
    ), DDR_POWER["VDD2"], 3806, 99.06)
    add_capacitor_bank(schematic, power_sheet, "DDR VDDQ (0.61 V nominal)", (
        ("C_0603", "10uF 10V X5R", 2), ("C_0402", "10uF 10V X5R", 1),
        ("C_0201", "100nF 10V X5R", 17),
    ), DDR_POWER["VDDQ"], 3823, 53.34)

    for name, deviceset, value, rail, position in (
        ("C4000", "C_0402", "2.2uF 10V X5R", EMMC_POWER["VCCQ"], 50.8),
        ("C4001", "C_0402", "2.2uF 10V X5R", EMMC_POWER["VCCQ"], 101.6),
        ("C4002", "C_0402", "4.7uF 10V X5R", EMMC_POWER["VCC"], 177.8),
        ("C4003", "C_0402", "4.7uF 10V X5R", EMMC_POWER["VCC"], 228.6),
        ("C4004", "C_0201", "100nF 10V X5R", EMMC_POWER["VDDI"], 304.8),
    ):
        add_capacitor(schematic, emmc_sheet, name, deviceset, value, rail, position, 50.8)
    add_note(emmc_sheet, "eMMC VCCQ (1.8 V), VCC (3.3 V) and VDDI bypass", 25.4, 67.31)


def ddr_signal_names():
    names = {}
    for channel in ("A", "B"):
        for prefix, memory_prefix, count in (
            ("A", "CA", 6), ("CKE", "CKE", 2), ("CSN", "CS", 2),
            ("DQ", "DQ", 16), ("DMI", "DMI", 2),
        ):
            for index in range(count):
                names[f"LP4X_{prefix}{index}_{channel}"] = f"{memory_prefix}{index}_{channel}"
        for polarity, memory_polarity in (("P", "t"), ("N", "c")):
            names[f"LP4X_CLK{polarity}_{channel}"] = f"CLK_{memory_polarity}_{channel}"
            for byte in range(2):
                names[f"LP4X_DQS{byte}{polarity}_{channel}"] = f"DQS{byte}_{memory_polarity}_{channel}"
    names["LP4X_RESET"] = "RST_n"
    return names


def add_signals(schematic, ddr_sheet, emmc_sheet, memory_library, balls):
    soc_library = schematic.find("libraries/library[@name='RK3576']")
    soc_device = soc_library.find("devicesets/deviceset[@name='RK3576']")
    memory_device = memory_library.find("devicesets/deviceset")
    soc_locations = pin_locations(schematic, "U1", soc_library, soc_device)
    memory_locations = pin_locations(schematic, EMCP_PART, memory_library, memory_device)

    soc_pins = {}
    for connection in soc_device.findall("devices/device/connects/connect"):
        pin_name, ball = connection.get("pin"), connection.get("pad")
        if "_LP4X_" in pin_name:
            logical_name = pin_name.split("_LP4X_", 1)[1].removesuffix("_" + ball).split("_LP5_", 1)[0]
            soc_pins["LP4X_" + logical_name] = connection
        elif pin_name.startswith("EMMC_"):
            soc_pins["_".join(pin_name.split("_")[:2])] = connection
        elif pin_name in ("ZQ_A_1R6", "ZQ_B_1J6", "USB3_OTG0_REXT_DP_TX_REXT_2T7"):
            soc_pins[pin_name] = connection

    memory_pins = memory_device.findall("devices/device/connects/connect")
    by_signal = {(pin.get("gate"), balls[pin.get("pad")]): pin for pin in memory_pins}
    expected_nets = {}
    pinmap = []
    ddr_names = ddr_signal_names()
    if {name for name in soc_pins if name.startswith("LP4X_")} != ddr_names.keys():
        raise ValueError("The RK3576 LPDDR4X pins differ from the expected HDG pin names")
    for soc_name, signal in ddr_names.items():
        gate_name = "LPDDR4X_CHB" if signal.endswith("_B") else "LPDDR4X_CHA"
        memory_pin = by_signal[gate_name, signal]
        soc_pin = soc_pins[soc_name]
        connect_pin(soc_locations, "U1", soc_pin, soc_name)
        connect_pin(memory_locations, EMCP_PART, memory_pin, soc_name)
        ball = memory_pin.get("pad")
        expected_nets[ball] = soc_name
        pinmap.append((soc_name, soc_pin.get("pad"), soc_name, ball, signal))

    emmc_names = {"EMMC_CLK": "CLKm", "EMMC_CMD": "CMD", "EMMC_STRB": "DS", "EMMC_RSTN": "RST_n"}
    emmc_names.update({f"EMMC_D{index}": f"DAT{index}" for index in range(8)})
    for soc_name, signal in emmc_names.items():
        memory_net = "EMMC_CLKOUT" if soc_name == "EMMC_CLK" else soc_name
        memory_pin = by_signal["EMMC", signal]
        connect_pin(soc_locations, "U1", soc_pins[soc_name], soc_name)
        connect_pin(memory_locations, EMCP_PART, memory_pin, memory_net)
        expected_nets[memory_pin.get("pad")] = memory_net

    for index, channel, memory_resistor, soc_resistor, x in (
        (0, "A", "R3802", "R1200", 73.66), (1, "B", "R3804", "R1201", 271.78),
    ):
        memory_pin = by_signal[f"LPDDR4X_CH{channel}", f"ZQ{index}"]
        memory_net = f"DRAM_ZQ{index}"
        soc_net = f"DDRPHY_ZQ_{channel}"
        soc_ball = "1R6" if channel == "A" else "1J6"
        connect_pin(soc_locations, "U1", soc_pins[f"ZQ_{channel}_{soc_ball}"], soc_net)
        connect_pin(memory_locations, EMCP_PART, memory_pin, memory_net)
        expected_nets[memory_pin.get("pad")] = memory_net
        add_resistor(schematic, ddr_sheet, memory_resistor, "240R 1%", memory_net, DDR_POWER["VDDQ"], x, 107.95)
        add_resistor(schematic, ddr_sheet, soc_resistor, "240R 1%", soc_net, DDR_POWER["VDDQ"], x, 92.71)

    rext = "USB3_OTG0_REXT_DP_TX_REXT"
    connect_pin(soc_locations, "U1", soc_pins[rext + "_2T7"], rext)
    add_resistor(schematic, ddr_sheet, "R1400", "8.2k 1%", rext, "GND", 73.66, 50.8)
    add_note(ddr_sheet, "Y1 USB3/DP REXT (2T7), EVB p. 14 R1400", 25.4, 63.5)

    add_resistor(schematic, emmc_sheet, "R4000", "27R", "EMMC_CLK", "EMMC_CLKOUT", 264.16, 205.74)
    add_note(emmc_sheet, "Place R4000 close to U1 (HDG p. 159).", 223.52, 218.44)
    pullups = [("EMMC_CMD", "10k")]
    pullups.extend((f"EMMC_D{index}", "50k") for index in range(8))
    pullups.append(("EMMC_RSTN", "50k"))
    for index, (net_name, value) in enumerate(pullups):
        add_resistor(schematic, emmc_sheet, f"R{4001 + index}", value, net_name, EMMC_POWER["VCCQ"],
                     50.8 + 76.2 * (index % 5), 121.92 - 27.94 * (index // 5),
                     populate=net_name != "EMMC_RSTN")
    add_note(emmc_sheet, "R4010 is DNP by default. DS connects directly to U1.", 25.4, 144.78)

    supply = {**DDR_POWER, **EMMC_POWER}
    for pin in memory_pins:
        ball = pin.get("pad")
        gate_name = pin.get("gate")
        if gate_name == "GND" or gate_name == "POWER":
            net_name = "GND" if gate_name == "GND" else supply[balls[ball]]
            connect_pin(memory_locations, EMCP_PART, pin, net_name)
            expected_nets[ball] = net_name
    return pinmap, expected_nets


def check_memory_connections(schematic, balls, expected_nets):
    library = schematic.find(f"libraries/library[@name='{EMCP_LIBRARY}']")
    device = library.find("devicesets/deviceset/devices/device")
    pad_by_pin = {(pin.get("gate"), pin.get("pin")): pin.get("pad")
                  for pin in device.findall("connects/connect")}
    actual_nets = defaultdict(list)
    for net in schematic.findall("sheets/sheet/nets/net"):
        for reference in net.findall(f"segment/pinref[@part='{EMCP_PART}']"):
            ball = pad_by_pin[reference.get("gate"), reference.get("pin")]
            actual_nets[ball].append(net.get("name"))

    no_connects = {ball for ball, signal in balls.items()
                   if signal in ("NC", "DNU") or re.fullmatch(r"VSF[1-9]", signal)}
    if set(actual_nets) != balls.keys() - no_connects:
        missing = sorted(balls.keys() - no_connects - actual_nets.keys())
        connected_nc = sorted(actual_nets.keys() & no_connects)
        raise ValueError(f"Missing eMCP balls {missing}; wired NC balls {connected_nc}")
    for ball in actual_nets:
        if actual_nets[ball] != [expected_nets[ball]]:
            raise ValueError(f"{ball} {balls[ball]}: {actual_nets[ball]}, expected {expected_nets[ball]}")
    power_ground_signals = set(DDR_POWER) | set(EMMC_POWER) | {"VSS", "VSSm"}
    power_ground_nets = set(DDR_POWER.values()) | set(EMMC_POWER.values()) | {"GND"}
    signal_count = 0
    for ball, nets in actual_nets.items():
        if balls[ball] not in power_ground_signals:
            signal_count += 1
            if nets[0] in power_ground_nets:
                raise ValueError(f"Signal ball {ball} {balls[ball]} is wired to {nets[0]}")
    print(f"{len(actual_nets)} eMCP balls wired once: {signal_count} signals and "
          f"{len(actual_nets) - signal_count} supply/ground. {len(no_connects)} NC balls open.")


def main():
    path = (BOARD_DIRECTORY / "FRIDAY_Compute_SCH1.sch").relative_to(REPOSITORY).as_posix()
    source = subprocess.check_output(["git", "show", f"{BASELINE}:{path}"], cwd=REPOSITORY)
    root = ElementTree.fromstring(source)
    schematic = root.find("drawing/schematic")
    with (BOARD_DIRECTORY / "emcp_ballmap_source.csv").open(newline="", encoding="utf-8") as ball_map:
        balls = {row["ball"]: row["signal"] for row in csv.DictReader(ball_map)}

    ddr_sheet = add_sheet(schematic, 6, "LPDDR4X SIGNALS", "Hynix pp. 6, 8; RK3576 HDG pp. 13-16; EVB pp. 12, 14, 24.")
    power_sheet = add_sheet(schematic, 7, "MEMORY POWER AND GROUND", "Hynix pp. 7-8, 19-20; HDG pp. 16-18, 44; Sige5 sheet 14; DshanPI sheet 18.")
    emmc_sheet = add_sheet(schematic, 8, "eMMC 5.1 x8", "Hynix pp. 6-7, 54 (Table 14); RK3576 HDG pp. 19-20, 159; VCCIO0 at 1.8 V.")
    library = add_memory(schematic, ddr_sheet, power_sheet, emmc_sheet)
    add_power(schematic, power_sheet, emmc_sheet)
    pinmap, expected_nets = add_signals(schematic, ddr_sheet, emmc_sheet, library, balls)
    check_memory_connections(schematic, balls, expected_nets)

    ElementTree.indent(root, space="  ")
    (BOARD_DIRECTORY / SCHEMATIC_NAME).write_bytes(
        b'<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE eagle SYSTEM "eagle.dtd">\n'
        + ElementTree.tostring(root, encoding="utf-8") + b"\n"
    )
    with (BOARD_DIRECTORY / "SCH-2_ddr_pinmap.csv").open("w", newline="", encoding="utf-8") as output:
        writer = csv.writer(output, lineterminator="\n")
        writer.writerow(("soc_pin", "soc_ball", "net", "emcp_ball", "emcp_signal"))
        writer.writerows(pinmap)
    print(f"{len(pinmap)} SoC-to-eMCP DDR pin-map rows. No swaps.")


if __name__ == "__main__":
    main()
