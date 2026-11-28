#!/usr/bin/env python3
"""Generate the standalone D16/D17 left-temple power schematic for Fusion Electronics."""

import csv
import sys
import xml.etree.ElementTree as ElementTree
from pathlib import Path

BOARD_DIRECTORY = Path(__file__).resolve().parent
REPOSITORY = BOARD_DIRECTORY.parent.parent
LIBRARIES = REPOSITORY / "libraries"
SCHEMATIC_NAME = "FRIDAY_Left_SCH4a.sch"
SUPPORT = "FRIDAY_SCH1_Support"
LEFT = "FRIDAY_SCH4a_Power"
AUXILIARY = "FH12-24S-0.5SH_55_"
RETURN = "PACK-_PROT"
PACK = "PACK+_PROT"
CELL_POSITIVE = "CELL_POS"
CELL_NEGATIVE = "CELL_NEG"
MIDPOINT = "CELL_MID"

sys.path.insert(0, str(BOARD_DIRECTORY.parent / "compute_board"))
from gen_sch1 import add_segment


def element(parent, tag, **attributes):
    return ElementTree.SubElement(parent, tag, {key: str(value) for key, value in attributes.items()})


def wire(parent, start_x, start_y, end_x, end_y, layer):
    element(parent, "wire", x1=start_x, y1=start_y, x2=end_x, y2=end_y, width=0.1524, layer=layer)


def outline(parent, width, height, layer):
    left, right = -width / 2, width / 2
    bottom, top = -height / 2, height / 2
    wire(parent, left, bottom, right, bottom, layer)
    wire(parent, right, bottom, right, top, layer)
    wire(parent, right, top, left, top, layer)
    wire(parent, left, top, left, bottom, layer)


def text(parent, message, position_x, position_y, size, layer):
    element(parent, "text", x=position_x, y=position_y, size=size, layer=layer).text = message


def land_pattern(library, name, width, height, pads):
    package = element(library.find("packages"), "package", name=name)
    outline(package, width, height, 51)
    outline(package, width + 0.5, height + 0.5, 39)
    text(package, ">NAME", -width / 2, height / 2 + 0.35, 0.8, 25)
    for name, position_x, position_y, pad_width, pad_height in pads:
        element(package, "smd", name=name, x=position_x, y=position_y,
                dx=pad_width, dy=pad_height, layer=1, cream="no" if name == "EP" else "yes")
    return package


def horizontal_pair(half_span, width, height):
    return (("1", -half_span, 0, width, height), ("2", half_span, 0, width, height))


def inline_device(library, name, package, left_pins, right_pins):
    """Declare symbol pins in display order and explicitly map them to land names."""
    symbol = element(library.find("symbols"), "symbol", name=name)
    half_height = max(5.08, max(len(left_pins), len(right_pins)) * 1.27 + 2.54)
    outline(symbol, 35.56, 2 * half_height, 94)
    text(symbol, ">NAME", -17.78, half_height + 1.27, 1.27, 95)
    text(symbol, ">VALUE", -17.78, -half_height - 2.54, 1.27, 96)
    for pins, position_x, rotation in ((left_pins, -22.86, "R0"), (right_pins, 22.86, "R180")):
        for index, (pin, pad) in enumerate(pins):
            position_y = (len(pins) - 1) * 1.27 - index * 2.54
            element(symbol, "pin", name=pin, x=position_x, y=position_y, length="middle",
                    direction="pas", visible="pin", rot=rotation)
    deviceset = element(library.find("devicesets"), "deviceset", name=name, uservalue="yes")
    element(element(deviceset, "gates"), "gate", name="G$1", symbol=name, x=0, y=0)
    device = element(element(deviceset, "devices"), "device", name="", package=package)
    connects = element(device, "connects")
    for pin, pad in (*left_pins, *right_pins):
        element(connects, "connect", gate="G$1", pin=pin, pad=pad)
    element(element(device, "technologies"), "technology", name="")


def two_terminal_device(library, name, package, first="1", second="2"):
    """Use the compact horizontal passive symbol for two-terminal lands."""
    inline_device(library, name, package, ((first, "1"),), ((second, "2"),))
    symbol = library.find(f"symbols/symbol[@name='{name}']")
    for item in list(symbol):
        if item.tag != "pin":
            symbol.remove(item)
    wire(symbol, -2.54, 1.27, 2.54, 1.27, 94)
    wire(symbol, 2.54, 1.27, 2.54, -1.27, 94)
    wire(symbol, 2.54, -1.27, -2.54, -1.27, 94)
    wire(symbol, -2.54, -1.27, -2.54, 1.27, 94)
    text(symbol, ">NAME", -2.54, 2.54, 1.27, 95)
    text(symbol, ">VALUE", -2.54, -3.81, 1.27, 96)
    for pin, position_x in zip(symbol.findall("pin"), (-5.08, 5.08)):
        pin.set("x", str(position_x))
        pin.set("length", "short")
        pin.set("visible", "off")


def power_library(libraries):
    library = element(libraries, "library", name=LEFT)
    for name in ("packages", "symbols", "devicesets"):
        element(library, name)

    # Injoinic pp. 2, 17, nominal top view. Exposed-pad stencil is a PCB release item.
    charger_pads = []
    for index in range(6):
        offset = 1.25 - index * 0.5
        charger_pads.extend(((str(1 + index), -1.92, offset, 0.70, 0.27),
                             (str(7 + index), -offset, -1.92, 0.27, 0.70),
                             (str(13 + index), 1.92, -offset, 0.70, 0.27),
                             (str(19 + index), offset, 1.92, 0.27, 0.70)))
    charger_pads.append(("EP", 0, 0, 2.5, 2.5))
    charger_package = land_pattern(library, "QFN24_4X4_EP", 4, 4, charger_pads)
    element(charger_package, "circle", x=-2.18, y=1.9, radius=0.12, width=0.15, layer=21)
    inline_device(library, "IP2326_NPD", "QFN24_4X4_EP",
                  (("VIN", "13"), ("EN", "12"), ("ISET", "11"), ("VSET", "3"),
                   ("CON_SEL", "10"), ("TIME_SET", "7"), ("VIN_UVSET", "8"), ("VIN_OVSET", "9"),
                   ("NTC", "4"), ("DM", "1"), ("DP", "2"), ("LED", "6")),
                  (("BST", "14"), ("LX", "15 16 17"), ("VSYS", "19 20"), ("VOUT", "21 22"),
                   ("VBATM", "23"), ("VBAT_GND", "24"), ("PGND", "18"), ("EP", "EP"),
                   ("BAT_STAT", "5")))

    sot23_6_pads = []
    for index in range(3):
        position_x = (index - 1) * 0.95
        sot23_6_pads.extend(((str(index + 1), position_x, -1.12, 0.58, 0.95),
                             (str(6 - index), position_x, 1.12, 0.58, 0.95)))
    land_pattern(library, "SOT23_6", 2.9, 1.6, sot23_6_pads)
    inline_device(library, "HY2120_CB", "SOT23_6",
                  (("VDD", "5"), ("VC", "4"), ("VSS", "6")),
                  (("OD", "1"), ("OC", "2"), ("CS", "3")))

    # AOS PO-00255 and AON5816 p.1. Land names follow the manufacturer's terminal aliases.
    mosfet_pads = [("EP", 0, 0, 1.80, 2.77)]
    for source, position_y, ordering in (("1", -2.25, ("G", "B", "A")),
                                        ("2", 2.25, ("A", "B", "G"))):
        for index, terminal in enumerate(ordering):
            pad_name = f"G{source}" if terminal == "G" else f"S{source}{terminal}"
            mosfet_pads.append((pad_name, (index - 1) * 0.5, position_y, 0.25, 0.60))
    protection_package = land_pattern(library, "AOS_DFN2X5A", 2, 5, mosfet_pads)
    element(protection_package, "circle", x=-1.15, y=-2.45, radius=0.12, width=0.15, layer=21)
    inline_device(library, "AON5816", "AOS_DFN2X5A",
                  (("G1", "G1"), ("S1", "S1A S1B"), ("D1_D2", "EP")),
                  (("G2", "G2"), ("S2", "S2A S2B")))

    # TI RPW0010A example board layout.
    efuse_pads = [("5", -0.25, 0, 0.30, 2.40), ("6", 0.25, 0, 0.30, 2.40)]
    for index, (height, pad_height) in enumerate(((0.70, 0.30), (0.225, 0.25),
                                                   (-0.225, 0.25), (-0.70, 0.30))):
        efuse_pads.extend(((str(1 + index), -0.90, height, 0.60, pad_height),
                           (str(10 - index), 0.90, height, 0.60, pad_height)))
    efuse_package = land_pattern(library, "TI_RPW0010A", 2, 2, efuse_pads)
    element(efuse_package, "circle", x=-1.14, y=0.72, radius=0.11, width=0.15, layer=21)
    inline_device(library, "TPS259470", "TI_RPW0010A",
                  (("IN", "5"), ("EN_UVLO", "1"), ("OVLO", "2"), ("GND", "8"),
                   ("AUXOFF", "3")),
                  (("OUT", "6"), ("ILM", "9"), ("DVDT", "7"), ("ITIMER", "10"), ("FLT", "4")))

    land_pattern(library, "SOT23_3", 2.9, 1.35,
                 (("1", -0.95, -1.00, 0.68, 0.90), ("2", 0.95, -1.00, 0.68, 0.90),
                  ("3", 0, 1.00, 0.68, 0.90)))
    inline_device(library, "AO3401A", "SOT23_3", (("D", "3"), ("G", "1")), (("S", "2"),))
    land_pattern(library, "DIODES_SOT23", 2.9, 1.3,
                 (("1", -0.95, -1.00, 0.80, 0.90), ("2", 0.95, -1.00, 0.80, 0.90),
                  ("3", 0, 1.00, 1.35, 0.90)))
    inline_device(library, "DMN2058U", "DIODES_SOT23", (("G", "1"),), (("D", "3"), ("S", "2")))

    land_pattern(library, "NANO2_2410", 6.10, 2.69, horizontal_pair(2.445, 2.16, 3.15))
    land_pattern(library, "XAL5030", 5.48, 5.28, horizontal_pair(1.94, 1.52, 4.7))
    land_pattern(library, "SOD123FL", 2.85, 1.8, horizontal_pair(1.39, 1.0, 1.6))
    land_pattern(library, "C_1206", 3.2, 1.6, horizontal_pair(1.40, 1.4, 1.8))
    for name, package in (("NANO2_FUSE", "NANO2_2410"), ("INDUCTOR", "XAL5030"), ("C_1206", "C_1206"),
                          ("R_1206", "C_1206")):
        two_terminal_device(library, name, package)
    element(library.find("packages/package[@name='SOD123FL']"), "circle",
            x=-2.10, y=0.82, radius=0.10, width=0.15, layer=21)
    two_terminal_device(library, "SMF_TVS", "SOD123FL", "K", "A")

    # Vishay p.2, 0.005–0.2 ohm land figures. The inner pads are Kelvin terminals.
    land_pattern(library, "VISHAY_WSK2512", 6.35, 3.18,
                 (("P1", -3.0, 0, 2.29, 3.30), ("P2", 3.0, 0, 2.29, 3.30),
                  ("K1", -1.08, 1.27, 0.76, 0.76), ("K2", 1.08, 1.27, 0.76, 0.76)))
    inline_device(library, "WSK2512", "VISHAY_WSK2512",
                  (("I_MINUS", "P1"), ("S_MINUS", "K1")), (("I_PLUS", "P2"), ("S_PLUS", "K2")))

    # Generic solder lands. The cell part has two strain-relief provisions per cell.
    for name, span, pad_width, pad_height in (("CELL_TABS", 2.30, 2.50, 3.00),
                                              ("HARNESS_PADS", 2.30, 2.50, 3.00),
                                              ("NTC_PADS", 1.27, 1.55, 2.0)):
        package = land_pattern(library, name, 2 * span + pad_width, pad_height,
                               horizontal_pair(span, pad_width, pad_height))
        for pad in package.findall("smd"):
            pad.set("cream", "no")
        if name == "CELL_TABS":
            for hole_x in (-2.30, 2.30):
                element(package, "hole", x=hole_x, y=-3.3, drill=1.1)
    inline_device(library, "CELL_TABS", "CELL_TABS", (("POS", "1"),), (("NEG", "2"),))
    inline_device(library, "HARNESS_PADS", "HARNESS_PADS", (("POS", "1"),), (("NEG", "2"),))
    two_terminal_device(library, "PACK_NTC", "NTC_PADS")

    package = land_pattern(library, "EDAC_MAGNETIC_3POS", 21.3, 4.6, ())
    for index in range(3):
        element(package, "pad", name=index + 1, x=(index - 1) * 2.7, y=0,
                drill=0.85, diameter=1.65)
    element(package, "circle", x=-3.85, y=0, radius=0.20, width=0.15, layer=21)
    inline_device(library, "MAGNETIC_POGO", "EDAC_MAGNETIC_3POS",
                  (("VBUS", "1"), ("GND", "2"), ("DET", "3")), ())
    return library


class Schematic:
    def __init__(self):
        support = ElementTree.parse(LIBRARIES / f"{SUPPORT}.lbr")
        self.root = ElementTree.Element("eagle", version="9.6.2")
        drawing = element(self.root, "drawing")
        for name in ("settings", "grid", "layers"):
            drawing.append(support.find(f"drawing/{name}"))
        self.schematic = element(drawing, "schematic", xreflabel="%F%N/%S.%C%R", xrefpart="/%S.%C%R")
        libraries = element(self.schematic, "libraries")
        for name in (SUPPORT, AUXILIARY):
            library = ElementTree.parse(LIBRARIES / f"{name}.lbr").find("drawing/library")
            library.set("name", name)
            libraries.append(library)
        power_library(libraries)
        element(self.schematic, "attributes")
        element(self.schematic, "variantdefs")
        element(element(self.schematic, "classes"), "class", number=0, name="default", width=0, drill=0)
        self.parts = element(self.schematic, "parts")
        self.sheets = element(self.schematic, "sheets")

    def sheet(self, number, title, description):
        sheet = element(self.sheets, "sheet")
        for name in ("plain", "instances", "busses", "nets"):
            element(sheet, name)
        self.part(sheet, f"FRAME{number}", "A3_FRAME", "", 0, 0, {}, SUPPORT)
        self.note(sheet, title, 15.24, 281.94, 2.54)
        self.note(sheet, description, 15.24, 274.32)
        return sheet

    def note(self, sheet, message, position_x, position_y, size=1.78):
        text(sheet.find("plain"), message, position_x, position_y, size, 94)

    def part(self, sheet, reference, device_name, value, position_x, position_y, connections, library=LEFT):
        if self.parts.find(f"part[@name='{reference}']") is not None:
            raise ValueError(f"Duplicate part {reference}")
        element(self.parts, "part", name=reference, library=library, deviceset=device_name, device="", value=value)
        definition = self.schematic.find(f"libraries/library[@name='{library}']")
        gate = definition.find(f"devicesets/deviceset[@name='{device_name}']/gates/gate")
        symbol = definition.find(f"symbols/symbol[@name='{gate.get('symbol')}']")
        gate_name = gate.get("name")
        instance = element(sheet.find("instances"), "instance", part=reference, gate=gate_name,
                           x=position_x, y=position_y, smashed="yes")
        for marker, layer in (("NAME", "95"), ("VALUE", "96")):
            marker_text = symbol.find(f"text[@layer='{layer}']")
            if marker_text is not None and (marker != "VALUE" or value):
                element(instance, "attribute", name=marker,
                        x=position_x + float(marker_text.get("x")), y=position_y + float(marker_text.get("y")),
                        size=1.27, layer=layer, align="bottom-left")
        pins = {pin.get("name"): pin for pin in symbol.findall("pin")}
        for pin_name, net_name in connections.items():
            pin = pins[pin_name]
            start_x = position_x + float(pin.get("x"))
            start_y = position_y + float(pin.get("y"))
            extension = -17.78 if float(pin.get("x")) < 0 else 5.08
            add_segment(sheet, net_name, reference, gate_name, pin_name,
                                  (start_x, start_y), (start_x + extension, start_y))

    def passive(self, sheet, reference, device_name, value, position_x, position_y, first, second):
        library = LEFT if device_name in ("C_1206", "R_1206", "NANO2_FUSE", "INDUCTOR", "PACK_NTC") else SUPPORT
        self.part(sheet, reference, device_name, value, position_x, position_y,
                  {"1": first, "2": second}, library)

    def test_point(self, sheet, reference, value, position_x, position_y, net_name):
        self.part(sheet, reference, "TP_1MM", value, position_x, position_y, {"1": net_name}, SUPPORT)

    def save(self):
        ElementTree.indent(self.root, space="  ")
        body = ElementTree.tostring(self.root, encoding="unicode")
        (BOARD_DIRECTORY / SCHEMATIC_NAME).write_text(
            '<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE eagle SYSTEM "eagle.dtd">\n' + body + "\n",
            encoding="utf-8",
        )


def pack_sheet(design):
    sheet = design.sheet(1, "FRIDAY / SCH-4a / LEFT TEMPLE PACK AND PROTECTION",
                         "D16/D17 | Both cells local | Generic tab pads | Bench qualification pending")
    design.part(sheet, "BT1", "CELL_TABS", "UPPER 1S POUCH TABS", 76.20, 220.98,
                {"POS": CELL_POSITIVE, "NEG": MIDPOINT})
    design.part(sheet, "BT2", "CELL_TABS", "LOWER 1S POUCH TABS", 76.20, 193.04,
                {"POS": MIDPOINT, "NEG": CELL_NEGATIVE})
    design.passive(sheet, "F1", "NANO2_FUSE", "0451002.MRL 2A", 198.12, 220.98, CELL_POSITIVE, PACK)
    design.part(sheet, "J2", "HARNESS_PADS", "D16 KEYED HARNESS PADS", 319.05, 220.98,
                {"POS": PACK, "NEG": RETURN})

    design.part(sheet, "U2", "HY2120_CB", "HY2120-CB", 76.20, 137.16,
                {"VDD": "PROTECT_VDD", "VC": "PROTECT_VC", "VSS": CELL_NEGATIVE,
                 "OD": "DISCHARGE_GATE", "OC": "CHARGE_GATE", "CS": "PROTECT_CS"})
    design.part(sheet, "Q1", "AON5816", "AON5816", 198.12, 137.16,
                {"G1": "DISCHARGE_GATE", "S1": CELL_NEGATIVE, "D1_D2": "FET_COMMON_DRAIN",
                 "G2": "CHARGE_GATE", "S2": "SHUNT_FET_SIDE"})
    design.part(sheet, "RS1", "WSK2512", "WSK2512R0500FEA 50mR 1W", 319.05, 137.16,
                {"I_MINUS": "SHUNT_FET_SIDE", "S_MINUS": "SHUNT_K-",
                 "I_PLUS": RETURN, "S_PLUS": "SHUNT_K+"})

    for reference, value, position_x, first, second in (
        ("R1", "330R", 50.80, CELL_POSITIVE, "PROTECT_VDD"),
        ("R2", "330R", 129.54, MIDPOINT, "PROTECT_VC"),
        ("R3", "2k", 210.82, RETURN, "PROTECT_CS"),
    ):
        design.passive(sheet, reference, "R_0603", value, position_x, 98.24, first, second)
    design.passive(sheet, "C1", "C_0603", "100nF 25V", 50.80, 72.39, "PROTECT_VDD", CELL_NEGATIVE)
    design.passive(sheet, "C2", "C_0603", "100nF 25V", 129.54, 72.39, "PROTECT_VC", CELL_NEGATIVE)
    for reference, value, position_x, net_name in (
        ("TP1", "PACK+ (PROTECTED)", 48.26, PACK),
        ("TP2", "PACK- (PROTECTED)", 121.92, RETURN),
        ("TP3", "CELL_MID", 195.58, MIDPOINT),
        ("TP4", "SHUNT K-", 269.24, "SHUNT_K-"),
        ("TP5", "SHUNT K+", 342.90, "SHUNT_K+"),
    ):
        design.test_point(sheet, reference, value, position_x, 46.99, net_name)
    design.note(sheet, "BT1 / BT2 tabs solder locally. Fit strain relief to the final cell and frame before assembly.",
                15.24, 255.27)
    design.note(sheet, "J2 pad 1 positive, pad 2 protected return. Use a keyed two-lead harness. No cell-midpoint crossing.",
                15.24, 247.65)
    design.note(sheet, "U2 CS observes the drop across both protection FETs and RS1. Do not bond any raw cell return to enclosure or flex.",
                15.24, 176.53)


def charger_sheet(design):
    sheet = design.sheet(2, "FRIDAY / SCH-4a / 2S BOOST CHARGER AND INTEGRATED BALANCE",
                         "Injoinic IP2326 V1.6 pp. 2, 9-15 | Fixed 5 V source | 8.4 V and 0.20 A nominal")
    design.part(sheet, "U1", "IP2326_NPD", "IP2326_NPD", 146.05, 179.07,
                {"VIN": "CHARGER_VIN", "EN": "CHARGER_RUN", "ISET": "CHARGER_ISET",
                 "TIME_SET": "CHARGER_TIME", "VIN_UVSET": "CHARGER_UVSET", "NTC": "CHARGER_NTC",
                 "BST": "CHARGER_BST", "LX": "CHARGER_SW", "VSYS": "CHARGER_VSYS", "VOUT": PACK,
                 "VBATM": "CHARGER_VBATM", "VBAT_GND": RETURN, "PGND": RETURN, "EP": RETURN,
                 "BAT_STAT": "CHARGER_BAT_STAT"})
    design.part(sheet, "Q2", "AO3401A", "AO3401A", 270.51, 126.43,
                {"D": MIDPOINT, "S": "MIDPOINT_SWITCHED", "G": "BALANCE_GATE"})
    for reference, value, position_x, position_y, first, second in (
        ("R4", "0.5R 5%", 55.88, 226.06, "VBUS_OR", "CHARGER_VIN"),
        ("R5", "450k 1%", 55.88, 165.10, "CHARGER_ISET", RETURN),
        ("R6", "120k 1%", 55.88, 139.70, "CHARGER_TIME", RETURN),
        ("R7", "68k 1%", 55.88, 114.30, "CHARGER_UVSET", RETURN),
        ("R8", "82k 1%", 55.88, 76.20, "CHARGER_NTC", RETURN),
        ("R9", "5.1k 5%", 228.60, 86.36, "BALANCE_GATE", RETURN),
        ("R10", "3.1M 5%", 302.26, 86.36, "BALANCE_GATE", "MIDPOINT_SWITCHED"),
    ):
        design.passive(sheet, reference, "R_0603", value, position_x, position_y, first, second)
    design.passive(sheet, "R11", "R_1206", "120R 1% 0.25W", 363.22, 126.43,
                   "MIDPOINT_SWITCHED", "CHARGER_VBATM")
    design.passive(sheet, "TH1", "PACK_NTC", "HNT-GR1 100k B4100", 139.70, 76.20,
                   "CHARGER_NTC", RETURN)
    design.passive(sheet, "L1", "INDUCTOR", "XAL5030-222MEC 2.2uH", 157.48, 226.06,
                   "VBUS_OR", "CHARGER_SW")
    for reference, device_name, value, position_x, position_y, first, second in (
        ("C3", "C_1206", "10uF 25V X7R", 53.34, 251.46, "VBUS_OR", RETURN),
        ("C4", "C_1206", "10uF 25V X7R", 153.67, 251.46, "CHARGER_VIN", RETURN),
        ("C5", "C_0603", "100nF 25V X7R", 245.11, 251.46, "CHARGER_BST", "CHARGER_SW"),
        ("C6", "C_1206", "22uF 25V X7R", 238.76, 226.06, "CHARGER_VSYS", RETURN),
        ("C7", "C_1206", "22uF 25V X7R", 331.47, 226.06, "CHARGER_VSYS", RETURN),
        ("C8", "C_1206", "10uF 25V X7R", 238.76, 199.39, PACK, RETURN),
        ("C9", "C_1206", "10uF 25V X7R", 331.47, 199.39, PACK, RETURN),
        ("C10", "C_0603", "100nF 25V X7R", 238.76, 171.45, PACK, RETURN),
        ("C11", "C_0603", "100nF 25V X7R", 331.47, 171.45, "CHARGER_VBATM", RETURN),
    ):
        design.passive(sheet, reference, device_name, value, position_x, position_y, first, second)
    design.test_point(sheet, "TP7", "CHARGER SW", 157.48, 45.72, "CHARGER_SW")
    design.test_point(sheet, "TP8", "PACK NTC", 80.01, 45.72, "CHARGER_NTC")
    design.note(sheet, "U1 VSET / CON_SEL open: 8.4 V nominal / 2S. OVSET open: 8.75 V internal backup.",
                15.24, 58.42)
    design.note(sheet, "U1 DM / DP open for fixed 5 V. Right USB data stays on the compute board.",
                15.24, 33.02)


def input_sheet(design):
    sheet = design.sheet(3, "FRIDAY / SCH-4a / POGO AND USB INPUT OR",
                         "D16 | Two independent reverse-blocking eFuses | Each branch has TVS, UVLO, OVLO and current limit")
    design.part(sheet, "J1", "MAGNETIC_POGO", "EDAC 686E0321250110E", 76.20, 237.49,
                {"VBUS": "POGO_VBUS_IN", "GND": RETURN, "DET": "POGO_DET_RAW"})
    design.note(sheet, "J1 top view pin 1 VBUS, pin 2 protected GND, pin 3 DET. Dock is the source for VBUS and DET.",
                16.51, 259.08)
    design.note(sheet, "U3 and U4 outputs join at VBUS_OR. Their always-on reverse blockers oppose flow toward either input.",
                16.51, 208.28)
    for index, (reference, source, row) in enumerate((
        ("U3", "POGO_VBUS_IN", 164.08), ("U4", "VBUS_5V_CHG", 77.47),
    )):
        prefix = "POGO" if index == 0 else "USB"
        connections = {"IN": source, "OUT": "VBUS_OR", "GND": RETURN,
                       "EN_UVLO": f"{prefix}_UVLO", "OVLO": f"{prefix}_OVLO",
                       "DVDT": f"{prefix}_DVDT", "ILM": f"{prefix}_ILM"}
        design.part(sheet, reference, "TPS259470", "TPS259470ARPW", 180.34, row, connections)
        first_resistor = 12 + 5 * index
        for offset, value, position_x, position_y, first, second in (
            (0, "374k 1%", 55.88, row + 12.70, source, f"{prefix}_UVLO"),
            (1, "150k 1%", 55.88, row - 10.16, f"{prefix}_UVLO", RETURN),
            (2, "365k 1%", 298.45, row + 24.13, source, f"{prefix}_OVLO"),
            (3, "100k 1%", 298.45, row + 2.54, f"{prefix}_OVLO", RETURN),
            (4, "6.04k 1%", 298.45, row - 20.32, f"{prefix}_ILM", RETURN),
        ):
            design.passive(sheet, f"R{first_resistor + offset}", "R_0603", value,
                           position_x, position_y, first, second)
        design.part(sheet, f"D{index + 1}", "SMF_TVS", "SMF6.0A", 55.88, row - 33.02,
                    {"K": source, "A": RETURN})
        design.passive(sheet, f"C{12 + 2 * index}", "C_0603", "1uF 25V X7R", 182.88, row - 33.02,
                       source, RETURN)
        design.passive(sheet, f"C{13 + 2 * index}", "C_0603", "1nF 25V C0G", 298.45, row - 38.10,
                       f"{prefix}_DVDT", RETURN)
    design.test_point(sheet, "TP6", "VBUS OR", 298.45, 237.49, "VBUS_OR")


def interface_sheet(design):
    sheet = design.sheet(4, "FRIDAY / SCH-4a / AUXILIARY FLEX AND 1.8 V CONTROL",
                         "Existing audio assignments pass through the interface. Audio circuitry is in SCH-4b.")
    with (REPOSITORY / "hardware/interconnect/pinout_right_left_aux.csv").open(newline="") as source:
        aux_connections = {
            row["pin"]: RETURN if row["net"] == "GND" else row["net"]
            for row in csv.DictReader(source) if row["type"] != "NC"
        }
    aux_connections["SHIELD"] = RETURN
    design.part(sheet, "J3", "FH12-24S-0.5SH(55)", "FH12-24S-0.5SH(55)", 95.25, 161.29,
                aux_connections, AUXILIARY)

    for reference, raw_signal, gate_signal, output_signal, row, series, pulldown, first_resistor in (
        ("Q3", "POGO_DET_RAW", "DETECT_GATE", "DOCK_DET", 200.66, "47k 1%", "100k 1%", 22),
        ("Q4", "CHARGER_BAT_STAT", "STATUS_GATE", "CHG_STAT", 139.70, "4.7k 1%", "1M 1%", 24),
        ("Q5", "CHG_EN", "ENABLE_GATE", "CHARGER_RUN", 78.74, "4.7k 1%", "1M 1%", 26),
    ):
        design.part(sheet, reference, "DMN2058U", "DMN2058U-7", 269.24, row,
                    {"G": gate_signal, "D": output_signal, "S": RETURN})
        design.passive(sheet, f"R{first_resistor}", "R_0603", series, 185.42, row + 11.43,
                       raw_signal, gate_signal)
        design.passive(sheet, f"R{first_resistor + 1}", "R_0603", pulldown, 185.42, row - 11.43,
                       gate_signal, RETURN)

    design.passive(sheet, "R28", "R_0603", "5.1k 1%", 342.90, 78.74, "VBUS_OR", "CHARGER_RUN")
    design.note(sheet, "J3 pin 1 as marked at the contact row. Fit pin 1 to pin 1 with the contact side per the interconnect drawing.",
                15.24, 254.00)
    design.note(sheet, "Right pulls DOCK_DET and CHG_STAT to VCCIO7 1.8 V. Both left outputs are open drain.",
                15.24, 246.38)
    design.note(sheet, "CHG_EN low requests charge. An unpowered or unplugged right side defaults to local charging.",
                15.24, 45.72)
    design.note(sheet, "AUX and pogo ground join only PACK-_PROT. PACK- harness stays the main load-current return.",
                15.24, 38.10)


def main():
    design = Schematic()
    pack_sheet(design)
    charger_sheet(design)
    input_sheet(design)
    interface_sheet(design)
    design.save()
    print(f"Generated {SCHEMATIC_NAME} with {len(design.sheets)} sheets and {len(design.parts) - 4} physical parts.")


if __name__ == "__main__":
    main()
