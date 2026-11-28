#!/usr/bin/env python3
"""Generate the SK hynix eMCP EAGLE library from the verified ball map."""

import csv
import re
import xml.etree.ElementTree as ElementTree
from collections import Counter
from pathlib import Path


REPOSITORY = Path(__file__).resolve().parent.parent
BALL_MAP = REPOSITORY / "hardware/compute_board/emcp_ballmap_source.csv"
LIBRARY = REPOSITORY / "libraries/H9HP52ACPMADAR.lbr"
DEVICE = "H9HP52ACPMADAR-KMM"
PACKAGE = "FBGA254_11.5X13.0_P0.50"
ROWS = "A B C D E F G H J K L M N P R T U V W Y AA AB AC AD".split()
PITCH = 0.50
PAD_DIAMETER = 0.300
COURTYARD_MARGIN = 0.25
POWER_SIGNALS = ("VDD1", "VDD2", "VDDQ", "VCC", "VCCQ", "VDDI")
GATE_NAMES = ("LPDDR4X_CHA", "LPDDR4X_CHB", "EMMC", "POWER", "GND", "NC")
XML_HEADER = b'<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE eagle SYSTEM "eagle.dtd">\n'


def gate_for_ball(ball):
    signal = ball["signal"]
    if signal in ("DNU", "NC") or signal.startswith("VSF"):
        return "NC"
    if signal in ("VSS", "VSSm"):
        return "GND"
    if signal in POWER_SIGNALS:
        return "POWER"
    if signal.endswith("_A") or signal == "ZQ0":
        return "LPDDR4X_CHA"
    if signal.endswith("_B") or signal == "ZQ1":
        return "LPDDR4X_CHB"
    if signal == "RST_n" and ball["function"].startswith("LPDDR4X"):
        return "LPDDR4X_CHA"
    if signal in ("CLKm", "CMD", "DS", "RST_n") or re.fullmatch(r"DAT[0-7]", signal):
        return "EMMC"
    raise ValueError(f"Unexpected signal on {ball['ball']}: {signal}")


def pin_direction(gate_name, signal):
    if gate_name == "NC":
        return "nc"
    if gate_name == "GND" or signal == "VDDI" or signal.startswith("ZQ"):
        return "pas"
    if gate_name == "POWER":
        return "pwr"
    if signal == "DS":
        return "out"
    if signal.startswith(("DQ", "DMI", "DAT")) or signal == "CMD":
        return "io"
    return "in"


def rectangle(parent, half_width, half_height, layer, width):
    corners = [(-half_width, -half_height), (half_width, -half_height),
               (half_width, half_height), (-half_width, half_height)]
    for start, end in zip(corners, corners[1:] + corners[:1]):
        ElementTree.SubElement(parent, "wire", x1=str(start[0]), y1=str(start[1]),
                               x2=str(end[0]), y2=str(end[1]), layer=layer, width=width)


def add_package(library, balls):
    packages = ElementTree.SubElement(library, "packages")
    package = ElementTree.SubElement(packages, "package", name=PACKAGE)
    ElementTree.SubElement(package, "description").text = (
        "SK hynix H9HP52ACPMADAR Rev 1.0 p. 9: 254-ball FBGA, 11.5 x 13.0 mm body, "
        "0.50 mm pitch, ball diameter 0.300 +/- 0.050 mm before reflow. "
        "The round SMD copper pads use the 0.300 mm nominal ball diameter from that drawing. "
        "Page 9 specifies package dimensions rather than a separate PCB land pattern. "
        "The top-view A1 orientation follows the ball map on p. 6. "
        "The layer 39 courtyard extends 0.25 mm beyond the nominal body."
    )
    rectangle(package, 5.75, 6.50, "51", "0.10")
    rectangle(package, 5.75 + COURTYARD_MARGIN, 6.50 + COURTYARD_MARGIN, "39", "0.05")
    ElementTree.SubElement(package, "circle", x="-5.25", y="6.10", radius="0.20",
                           width="0.15", layer="21")
    ElementTree.SubElement(package, "text", x="0", y="7.0", size="0.8", layer="25",
                           align="bottom-center").text = ">NAME"
    ElementTree.SubElement(package, "text", x="0", y="-7.0", size="0.8", layer="27",
                           align="top-center").text = ">VALUE"
    for ball in balls:
        address = ball["ball"]
        row, column = re.fullmatch(r"([A-Z]+)([1-9][0-9]*)", address).groups()
        if row not in ROWS or not 1 <= int(column) <= 18:
            raise ValueError(f"Ball {address} is outside the 24 x 18 package grid")
        ElementTree.SubElement(package, "smd", name=address,
                               x=f"{(int(column) - 9.5) * PITCH:.2f}",
                               y=f"{(11.5 - ROWS.index(row)) * PITCH:.2f}",
                               dx=f"{PAD_DIAMETER:.3f}", dy=f"{PAD_DIAMETER:.3f}",
                               layer="1", roundness="100")


def add_symbol(symbols, connects, gate_name, balls):
    symbol = ElementTree.SubElement(symbols, "symbol", name=gate_name)
    signal_counts = Counter(ball["signal"] for ball in balls)
    if gate_name in ("LPDDR4X_CHA", "LPDDR4X_CHB", "EMMC"):
        data_signals = ("DQ", "DMI", "DAT")
        # Order numeric signal names by index so DQ10 follows DQ9.
        balls = sorted(balls, key=lambda ball: re.sub(r"\d+", lambda match: match[0].zfill(2),
                                                      ball["signal"]))
        left = [ball for ball in balls if not ball["signal"].startswith(data_signals)]
        right = [ball for ball in balls if ball["signal"].startswith(data_signals)]
    else:
        balls = sorted(balls, key=lambda ball: ball["signal"])
        middle = (len(balls) + 1) // 2
        left, right = balls[:middle], balls[middle:]

    half_height = (max(len(left), len(right)) + 1) * 1.27
    rectangle(symbol, 20.32, half_height, "94", "0.254")
    ElementTree.SubElement(symbol, "text", x="0", y=f"{half_height + 2.54:.2f}",
                           size="1.778", layer="95", align="bottom-center").text = ">NAME"
    ElementTree.SubElement(symbol, "text", x="0", y="0", size="1.27",
                           layer="94", align="center", rot="R90").text = gate_name
    for side, pins, rotation in ((-1, left, "R0"), (1, right, "R180")):
        for index, ball in enumerate(pins):
            signal = ball["signal"]
            pin_name = signal
            if signal_counts[signal] > 1:
                pin_name += "@" + ball["ball"]
            ElementTree.SubElement(symbol, "pin", name=pin_name, x=f"{side * 25.4:.2f}",
                                   y=f"{half_height - 2.54 * (index + 1):.2f}",
                                   length="middle", direction=pin_direction(gate_name, signal),
                                   visible="both", rot=rotation)
            ElementTree.SubElement(connects, "connect", gate=gate_name, pin=pin_name, pad=ball["ball"])


def build_library(balls):
    root = ElementTree.Element("eagle", version="9.6.2")
    drawing = ElementTree.SubElement(root, "drawing")
    layers = ElementTree.SubElement(drawing, "layers")
    for number, name, color in (
        (1, "Top", 4), (21, "tPlace", 7), (25, "tNames", 7), (27, "tValues", 7),
        (39, "tKeepout", 4), (51, "tDocu", 7), (93, "Pins", 2), (94, "Symbols", 4),
        (95, "Names", 7), (96, "Values", 7),
    ):
        ElementTree.SubElement(layers, "layer", number=str(number), name=name, color=str(color),
                               fill="1", visible="yes", active="yes")
    library = ElementTree.SubElement(drawing, "library")
    ElementTree.SubElement(library, "description").text = (
        "SK hynix 64 GB eMMC 5.1 and 32 Gbit LPDDR4X. Ball assignments from "
        "hardware/compute_board/emcp_ballmap_source.csv, datasheet p. 6. "
        "The optional NC gate contains all no-connect, do-not-use and vendor-specific balls."
    )
    add_package(library, balls)
    symbols = ElementTree.SubElement(library, "symbols")
    devicesets = ElementTree.SubElement(library, "devicesets")
    deviceset = ElementTree.SubElement(devicesets, "deviceset", name=DEVICE, prefix="U")
    gates = ElementTree.SubElement(deviceset, "gates")
    devices = ElementTree.SubElement(deviceset, "devices")
    device = ElementTree.SubElement(devices, "device", name="", package=PACKAGE)
    connects = ElementTree.SubElement(device, "connects")
    for index, gate_name in enumerate(GATE_NAMES):
        ElementTree.SubElement(gates, "gate", name=gate_name, symbol=gate_name,
                               x=str(index * 63.5), y="0",
                               addlevel="request" if gate_name == "NC" else "must")
        gate_balls = [ball for ball in balls if gate_for_ball(ball) == gate_name]
        add_symbol(symbols, connects, gate_name, gate_balls)
    ElementTree.SubElement(ElementTree.SubElement(device, "technologies"), "technology", name="")
    return root


def check_library(root, balls):
    library = root.find("drawing/library")
    pads = [pad.get("name") for pad in library.findall("packages/package/smd")]
    connects = library.findall("devicesets/deviceset/devices/device/connects/connect")
    expected_signals = {ball["ball"]: ball["signal"] for ball in balls}
    if len(balls) != 254 or len(set(pads)) != 254 or len(pads) != 254:
        raise ValueError("Expected 254 unique pads and 254 CSV rows")
    if set(pads) != expected_signals.keys():
        raise ValueError("Package pad names differ from the CSV ball names")
    if Counter(connect.get("pad") for connect in connects) != Counter(pads):
        raise ValueError("Every physical pad must have exactly one device connection")
    for connect in connects:
        gate_name = connect.get("gate")
        pin_name = connect.get("pin")
        symbol = library.find(f"symbols/symbol[@name='{gate_name}']")
        pin = symbol.find(f"pin[@name='{pin_name}']")
        if pin is None or pin.get("name").split("@", 1)[0] != expected_signals[connect.get("pad")]:
            raise ValueError(f"Pin name differs from the CSV signal at {connect.get('pad')}")
        if (pin.get("direction") == "nc") != (gate_name == "NC"):
            raise ValueError(f"Incorrect NC marking at {connect.get('pad')}")
    no_connect_count = sum(connect.get("gate") == "NC" for connect in connects)
    print(f"Verified {len(pads)} unique pads and {len(connects)} CSV signal matches. "
          f"{no_connect_count} balls are marked NC.")


def main():
    with BALL_MAP.open(newline="", encoding="utf-8") as source:
        balls = list(csv.DictReader(source))
    root = build_library(balls)
    check_library(root, balls)
    ElementTree.indent(root, space="  ")
    LIBRARY.write_bytes(XML_HEADER + ElementTree.tostring(root, encoding="utf-8") + b"\n")


if __name__ == "__main__":
    main()
