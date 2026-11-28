#!/usr/bin/env python3
"""Generate the four-sheet FRIDAY camera bridge schematic for Fusion Electronics."""

import csv
import sys
import xml.etree.ElementTree as ElementTree
from pathlib import Path

BOARD_DIRECTORY = Path(__file__).resolve().parent
REPOSITORY = BOARD_DIRECTORY.parent.parent
SCHEMATIC_NAME = "FRIDAY_Bridge_SCH3.sch"
SUPPORT = "FRIDAY_SCH1_Support"
CUSTOM = "FRIDAY_SCH3_Camera"
FLEX = "FH12-24S-0.5SH_55_"
SENSOR = "DF37NC-30DS-0.4V_51_"
MICROPHONE = "INMP441"
INPUT = "VCC_3V3_S3"
MIC_POWER = "VCC_1V8_S0"
ENABLE = "CAM_ENABLE"
ENABLE_LOCAL = "CAM_ENABLE_3V3"
DVDD = "CAM_DVDD_1V1"
AVDD = "CAM_AVDD_AFVDD_2V8"
DOVDD = "CAM_DOVDD_1V8"

# Share the existing FRIDAY EAGLE XML primitives and instance placement.
sys.path.insert(0, str(BOARD_DIRECTORY.parent / "left_temple"))
from gen_sch4a import Schematic, element, horizontal_pair, inline_device, land_pattern, two_terminal_device


def custom_library(libraries):
    library = element(libraries, "library", name=CUSTOM)
    for section in ("packages", "symbols", "devicesets"):
        element(library, section)

    five_pin_lands = (("1", -0.95, -1.05, 0.65, 0.85), ("2", 0, -1.05, 0.65, 0.85),
                      ("3", 0.95, -1.05, 0.65, 0.85), ("4", 0.95, 1.05, 0.65, 0.85),
                      ("5", -0.95, 1.05, 0.65, 0.85))
    for package in ("TSOT25_AP3429", "SOT25_AP7331", "SOT23_DBV"):
        outline = land_pattern(library, package, 2.9, 1.6, five_pin_lands)
        element(outline, "circle", x=-1.4, y=-1.45, radius=0.10, width=0.15, layer=21)

    inline_device(library, "AP3429", "TSOT25_AP3429",
                  (("VIN", "4"), ("EN", "1"), ("GND", "2")),
                  (("LX", "3"), ("FB", "5")))
    inline_device(library, "AP7331", "SOT25_AP7331",
                  (("IN", "1"), ("EN", "3"), ("GND", "2")), (("OUT", "5"), ("NC", "4")))
    inline_device(library, "SN74LV1T34", "SOT23_DBV",
                  (("A", "2"), ("VCC", "5"), ("GND", "3")), (("Y", "4"), ("NC", "1")))
    land_pattern(library, "XFL4020", 4.0, 4.0, horizontal_pair(1.45, 1.60, 3.70))
    two_terminal_device(library, "XFL4020", "XFL4020")
    land_pattern(library, "MLCC_1206", 3.2, 1.6, horizontal_pair(1.4, 1.4, 1.8))
    two_terminal_device(library, "C_1206", "MLCC_1206")

    oscillator_lands = (("1", -0.70, -0.53, 0.72, 0.65), ("2", 0.70, -0.53, 0.72, 0.65),
                        ("3", 0.70, 0.53, 0.72, 0.65), ("4", -0.70, 0.53, 0.72, 0.65))
    oscillator = land_pattern(library, "SIT_2016_4", 2.0, 1.6, oscillator_lands)
    element(oscillator, "circle", x=-1.21, y=-0.65, radius=0.10, width=0.15, layer=21)
    inline_device(library, "SIT1602B", "SIT_2016_4",
                  (("VDD", "4"), ("OE", "1"), ("GND", "2")), (("CLK", "3"),))

    supervisor_lands = [("EP", 0, 0, 2.5, 2.5)]
    for index in range(5):
        offset = 1.0 - index * 0.5
        supervisor_lands.extend((
            (str(index + 1), -1.95, offset, 0.65, 0.27),
            (str(index + 6), -offset, -1.95, 0.27, 0.65),
            (str(index + 11), 1.95, -offset, 0.65, 0.27),
            (str(index + 16), offset, 1.95, 0.27, 0.65),
        ))
    supervisor = land_pattern(library, "TI_RGP20", 4, 4, supervisor_lands)
    element(supervisor, "circle", x=-2.25, y=1.3, radius=0.10, width=0.15, layer=21)
    inline_device(library, "TPS386000", "TI_RGP20",
                  (("VDD", "14"), ("MR", "1"), ("SENSE1", "10"), ("SENSE2", "9"), ("SENSE3", "8"),
                   ("SENSE4L", "7"), ("SENSE4H", "6"), ("GND", "12"), ("NC11", "11"), ("EP", "EP")),
                  (("RESET1", "15"), ("RESET2", "16"), ("RESET3", "17"), ("RESET4", "18"),
                   ("CT1", "5"), ("CT2", "4"), ("CT3", "3"), ("CT4", "2"),
                   ("WDI", "20"), ("WDO", "19"), ("VREF", "13")))

    choke_lands = (("1", -0.51, 0.28, 0.39, 0.36), ("2", 0.51, 0.28, 0.39, 0.36),
                   ("3", 0.51, -0.28, 0.39, 0.36), ("4", -0.51, -0.28, 0.39, 0.36))
    land_pattern(library, "DLP11SN_0504", 1.25, 1.0, choke_lands)
    inline_device(library, "DLP11SN900HL2L", "DLP11SN_0504",
                  (("FLEX_N", "1"), ("FLEX_P", "4")), (("SENSOR_N", "2"), ("SENSOR_P", "3")))


class BridgeSchematic(Schematic):
    def __init__(self):
        support = ElementTree.parse(REPOSITORY / "libraries" / f"{SUPPORT}.lbr")
        self.root = ElementTree.Element("eagle", version="9.6.2")
        drawing = element(self.root, "drawing")
        for section in ("settings", "grid", "layers"):
            drawing.append(support.find(f"drawing/{section}"))
        self.schematic = element(drawing, "schematic", xreflabel="%F%N/%S.%C%R", xrefpart="/%S.%C%R")
        libraries = element(self.schematic, "libraries")
        for name in (SUPPORT, FLEX, SENSOR, MICROPHONE):
            library = ElementTree.parse(REPOSITORY / "libraries" / f"{name}.lbr").find("drawing/library")
            library.set("name", name)
            libraries.append(library)
        custom_library(libraries)
        element(self.schematic, "attributes")
        element(element(self.schematic, "variantdefs"), "variantdef", name="default")
        element(element(self.schematic, "classes"), "class", number=0, name="default", width=0, drill=0)
        self.parts = element(self.schematic, "parts")
        self.sheets = element(self.schematic, "sheets")

    def part(self, sheet, reference, device_name, value, position_x, position_y,
             connections, library=CUSTOM, populate=True):
        super().part(sheet, reference, device_name, value, position_x, position_y, connections, library)
        if not populate:
            part = self.parts.find(f"part[@name='{reference}']")
            element(part, "variant", name="default", populate="no")

    def passive(self, sheet, reference, device_name, value, position_x, position_y, first, second, populate=True):
        library = CUSTOM if device_name in ("C_1206", "XFL4020") else SUPPORT
        self.part(sheet, reference, device_name, value, position_x, position_y,
                  {"1": first, "2": second}, library, populate)

    def save(self):
        ElementTree.indent(self.root, space="  ")
        body = ElementTree.tostring(self.root, encoding="unicode")
        (BOARD_DIRECTORY / SCHEMATIC_NAME).write_text(
            '<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE eagle SYSTEM "eagle.dtd">\n' + body + "\n",
            encoding="utf-8",
        )


def interface_sheet(design):
    sheet = design.sheet(1, "FRIDAY / SCH-3 / CAMERA CONNECTORS AND CSI",
                         "RP-008969-SD p.2 and FRIDAY interconnect | 2-lane D-PHY | DF37 hold")
    with (REPOSITORY / "hardware/interconnect/pinout_right_bridge.csv").open(newline="") as stream:
        flex_pins = {row["pin"]: row["net"] for row in csv.DictReader(stream)}
    with (BOARD_DIRECTORY / "df37_crosswalk.csv").open(newline="") as stream:
        crosswalk = list(csv.DictReader(stream))
    if len(crosswalk) != 30 or any(row["footprint_pad"] != "UNPROVEN" for row in crosswalk):
        raise ValueError("SCH-3 J1 hold requires the reviewed, unproven 30-row crosswalk")

    design.part(sheet, "J2", "FH12-24S-0.5SH(55)", "FH12-24S-0.5SH(55)",
                84.0, 171.45, flex_pins, FLEX)
    design.part(sheet, "J1", "DF37NC-30DS-0.4V(51)", "DF37NC-30DS-0.4V(51)",
                323.85, 174.0, {}, SENSOR)
    design.note(sheet, "J2 PCB view: pin 1 at negative X. Bottom contact; pin 1 mates to pin 1 at right board.",
                13.97, 251.46)
    design.note(sheet, "J1 awaiting crosswalk. All 30 electrical contacts open.", 261.62, 232.41)
    design.note(sheet, "Place EMI filters near flex launch. Keep pair polarity and continuous return.",
                14, 109.22)

    for index, (lane, position_x) in enumerate((("D0", 69.85), ("D1", 205.74), ("CLK", 336.55)), start=2):
        negative = f"CSI0_{lane}_N"
        positive = f"CSI0_{lane}_P"
        design.part(sheet, f"L{index}", "DLP11SN900HL2L", "DLP11SN900HL2L", position_x, 78.74,
                    {"FLEX_N": negative, "FLEX_P": positive,
                     "SENSOR_N": f"{negative}_SENSOR", "SENSOR_P": f"{positive}_SENSOR"})
    design.note(sheet, "Sensor-side choke nets end at L2-L4 until the tail orientation is proven.", 14, 48.26)


def power_sheet(design):
    sheet = design.sheet(2, "FRIDAY / SCH-3 / CAMERA POWER",
                         "Common CAM_ENABLE sequencing per RP-008969-SD p.2 | Local camera DOVDD")
    design.part(sheet, "U1", "AP3429", "AP3429KTTR-G1", 76.20, 209.55,
                {"VIN": INPUT, "EN": ENABLE_LOCAL, "GND": "GND", "LX": "CAM_DVDD_SW", "FB": "CAM_DVDD_FB"})
    design.passive(sheet, "L1", "XFL4020", "XFL4020-222MEC 2.2uH", 172.72, 218.44, "CAM_DVDD_SW", DVDD)
    design.part(sheet, "U2", "AP7331", "AP7331-28WG-7", 245.11, 120.65,
                {"IN": INPUT, "EN": ENABLE_LOCAL, "GND": "GND", "OUT": AVDD})
    design.part(sheet, "U3", "AP7331", "AP7331-18WG-7", 245.11, 70.00,
                {"IN": INPUT, "EN": ENABLE_LOCAL, "GND": "GND", "OUT": DOVDD})
    design.part(sheet, "U4", "SN74LV1T34", "SN74LV1T34DBVR", 75.00, 78.74,
                {"A": ENABLE, "VCC": INPUT, "GND": "GND", "Y": ENABLE_LOCAL})
    design.passive(sheet, "R1", "R_0402", "20k 0.1%", 171.45, 188.00, DVDD, "CAM_DVDD_FB")
    design.passive(sheet, "R2", "R_0402", "24k 0.1%", 171.45, 162.56, "CAM_DVDD_FB", "GND")
    design.passive(sheet, "R3", "R_0402", "100k 1%", 55.88, 53.34, ENABLE, "GND")
    design.passive(sheet, "R4", "R_0402", "100k 1%", 129.54, 53.34, ENABLE_LOCAL, "GND")
    for reference, package, value, position_x, position_y, first, second in (
        ("C1", "C_1206", "22uF 10V X7R", 57.15, 246.38, INPUT, "GND"),
        ("C2", "C_1206", "22uF 10V X7R", 259.08, 220.98, DVDD, "GND"),
        ("C3", "C_1206", "22uF 10V X7R", 345.44, 220.98, DVDD, "GND"),
        ("C4", "C_0402", "330pF 25V C0G", 258.00, 187.96, DVDD, "CAM_DVDD_FB"),
        ("C5", "C_0402", "1uF 16V X5R", 152.40, 131.00, INPUT, "GND"),
        ("C6", "C_0402", "1uF 16V X5R", 335.28, 126.00, AVDD, "GND"),
        ("C7", "C_0402", "1uF 16V X5R", 152.40, 84.00, INPUT, "GND"),
        ("C8", "C_0402", "1uF 16V X5R", 335.28, 76.20, DOVDD, "GND"),
        ("C9", "C_0402", "100nF 16V X7R", 53.34, 118.11, INPUT, "GND"),
        ("C10", "C_0402", "1uF 16V X5R", 345.44, 171.45, DVDD, "GND"),
        ("C11", "C_0402", "1uF 16V X5R", 345.44, 104.00, AVDD, "GND"),
        ("C12", "C_0402", "100nF 25V X7R", 345.44, 95.25, AVDD, "GND"),
        ("C13", "C_0402", "1uF 16V X5R", 345.44, 55.88, DOVDD, "GND"),
    ):
        design.passive(sheet, reference, package, value, position_x, position_y, first, second)
    for index, (net_name, position_x) in enumerate(((DVDD, 207.01), (AVDD, 260.35), (DOVDD, 325.12)), start=1):
        design.test_point(sheet, f"TP{index}", net_name, position_x, 35.56, net_name)
    design.note(sheet, "U2 2.8 V supplies AVDD and AFVDD, as on the Pi carrier. J1 is electrically parked.",
                15.24, 151.13)
    design.note(sheet, "Input budget and load transient screen are in SCH-3_crossref.md.",
                15.24, 33.02)


def clock_sheet(design):
    sheet = design.sheet(3, "FRIDAY / SCH-3 / MCLK, RESET AND CAMERA CONTROL",
                         "Local 24 MHz MCLK | Supervisor holds XCLR until all camera rails qualify")
    design.part(sheet, "X1", "SIT1602B", "SIT1602BI-71-18E-24.000000D", 68.0, 220.98,
                {"VDD": DOVDD, "OE": DOVDD, "GND": "GND", "CLK": "CAM_MCLK_XO"})
    design.passive(sheet, "R5", "R_0402", "22R 1%", 172.72, 220.98, "CAM_MCLK_XO", "MCLK")
    design.passive(sheet, "C14", "C_0402", "1uF 16V X5R", 68, 248.92, DOVDD, "GND")
    design.part(sheet, "U5", "TPS386000", "TPS386000RGPR", 210.82, 133.35,
                {"VDD": INPUT, "MR": ENABLE_LOCAL, "SENSE1": "POR_SENSE_DVDD",
                 "SENSE2": "POR_SENSE_DOVDD", "SENSE3": "POR_SENSE_AVDD", "SENSE4L": "GND",
                 "SENSE4H": "GND", "WDI": "GND", "NC11": "GND", "GND": "GND", "EP": "GND",
                 "RESET1": "XCLR", "RESET2": "XCLR", "RESET3": "XCLR"})
    design.passive(sheet, "C15", "C_0402", "100nF 16V X7R", 277.00, 174.00, INPUT, "GND")
    for index, (supply, sense, resistance, row) in enumerate((
        (DVDD, "POR_SENSE_DVDD", "15.4k 0.1%", 154.94),
        (DOVDD, "POR_SENSE_DOVDD", "32.4k 0.1%", 125.73),
        (AVDD, "POR_SENSE_AVDD", "54.9k 0.1%", 96.52),
    )):
        design.passive(sheet, f"R{6 + index * 2}", "R_0402", resistance, 51.00, row, supply, sense)
        design.passive(sheet, f"R{7 + index * 2}", "R_0402", "10k 0.1%", 117.00, row, sense, "GND")
    design.passive(sheet, "R12", "R_0402", "10k 1%", 320, 135.89, DOVDD, "XCLR")
    design.passive(sheet, "R13", "R_0402", "0R DNP", 320, 218.44, "CAM_MCLK_RESERVED", "MCLK",
                   populate=False)
    design.passive(sheet, "R14", "R_0402", "0R DNP", 320, 110.49, "CAM_RST_L_RESERVED", "XCLR",
                   populate=False)
    design.passive(sheet, "R15", "R_0402", "2.2k 1%", 94, 56.00, DOVDD, "I2C_CAM_SCL")
    design.passive(sheet, "R16", "R_0402", "2.2k 1%", 175, 56.00, DOVDD, "I2C_CAM_SDA")
    for reference, label, position_x, position_y, net_name in (
        ("TP4", "MCLK", 227, 246.38, "MCLK"),
        ("TP5", "XCLR", 291, 76.20, "XCLR"),
        ("TP6", "CAM_ENABLE", 365.76, 76.20, ENABLE),
        ("TP7", "HOST CLK RESERVED", 336.55, 246.38, "CAM_MCLK_RESERVED"),
        ("TP8", "HOST RESET RESERVED", 265, 49.5, "CAM_RST_L_RESERVED"),
        ("TP9", "CRADLE NTC RESERVED", 349, 49.5, "CAM_CRADLE_NTC_RESERVED"),
    ):
        design.test_point(sheet, reference, label, position_x, position_y, net_name)
    design.note(sheet, "U5 CT1-CT3 open select 14 ms minimum. Clock startup is 5 ms maximum at rated VDD.",
                15.24, 189.23)
    design.note(sheet, "Host clock option requires removing R5 and revalidating reset timing. Host reset must be open drain.",
                15.24, 32.0)


def microphone_sheet(design):
    sheet = design.sheet(4, "FRIDAY / SCH-3 / STEREO DIGITAL MICROPHONES",
                         "Y3 | 1.8 V host I/O and microphone supplies | Common I2S data")
    for reference, selection, position_x, bypass in (
        ("MK1", "GND", 101.60, "C16"), ("MK2", MIC_POWER, 280.67, "C17"),
    ):
        design.part(sheet, reference, MICROPHONE, MICROPHONE, position_x, 192.0,
                    {"SCK": "SAI1_BCLK_M0", "WS": "SAI1_LRCK_M0", "SD": "SAI1_SDI0_M0",
                     "VDD": MIC_POWER, "CHIPEN": MIC_POWER, "GND": "GND", "L/R": selection}, MICROPHONE)
        design.passive(sheet, bypass, "C_0402", "100nF 16V X7R", position_x, 152.4, MIC_POWER, "GND")
    design.passive(sheet, "R17", "R_0402", "100k 1%", 101.60, 112.0, "SAI1_SDI0_M0", "GND")
    design.test_point(sheet, "TP10", "MIC SD", 224.79, 112.0, "SAI1_SDI0_M0")
    design.note(sheet, "MK1 strap low = left. MK2 strap high = right. Host uses 64 BCLK periods per stereo frame.",
                15.24, 246.38)
    design.note(sheet, "Bottom acoustic ports: align board and enclosure holes. Keep solder paste, adhesive and debris clear.",
                15.24, 82.55)
    design.note(sheet, "Host BCLK and LRCK must remain idle while the common 1.8 V S0 domain is off.",
                15.24, 74.93)


def main():
    design = BridgeSchematic()
    interface_sheet(design)
    power_sheet(design)
    clock_sheet(design)
    microphone_sheet(design)
    design.save()
    print(f"Generated {SCHEMATIC_NAME}: {len(design.sheets)} sheets, {len(design.parts) - 4} physical parts, J1 held open.")


if __name__ == "__main__":
    main()
