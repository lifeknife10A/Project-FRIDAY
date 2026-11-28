#!/usr/bin/env python3
"""Extend accepted SCH-2 with FRIDAY's bridge, left-aux and right audio interfaces."""

import csv
import sys
from pathlib import Path

from gen_sch2 import connect_pin, pin_locations

BOARD_DIRECTORY = Path(__file__).resolve().parent
REPOSITORY = BOARD_DIRECTORY.parent.parent
sys.path.insert(0, str(BOARD_DIRECTORY.parent / "left_temple"))
from sch4b_audio import (
    AUDIO_LIBRARY, FLEX_LIBRARY, Extension, add_amplifier, add_audio_library, copy_support_device,
    element, inline_device, land_pattern,
)

BASELINE = "08e94c847ed6b1c0665002e86ff34b9d0e210bb2"
SCHEMATIC_NAME = "FRIDAY_Compute_SCH4b.sch"
APPROVALS_PATH = BOARD_DIRECTORY / "SCH-4b_emcp_erc_approvals.txt"
APPROVAL_REASON = "power pin tied to named rail — auditor reviewed (SCH-2 accepted 08e94c8)"
VCCIO_S0 = "VCC_1V8_S0"
VCCIO_S3 = "VCC_1V8_S3"
SYSTEM_5V = "VCC5V0_SYS_S5"
USB_INPUT = "VBUS_5V"
USB_BRANCH = "VBUS_5V_CHG"
PACK_INPUT = "VBAT_2S_IN"
ADC_REFERENCE_SOURCE = "VCCA1V8_PLDO2_S0"

SOC_BALLS = {
    "AK20": "CSI0_D0_P", "AL20": "CSI0_D0_N", "AK21": "CSI0_D1_P", "AL21": "CSI0_D1_N",
    "AK22": "CSI0_CLK_P", "AL22": "CSI0_CLK_N",
    "1E9": "I2C_CAM_SCL", "1D12": "I2C_CAM_SDA", "1D7": "CAM_ENABLE_SOC",
    "1C6": "SAI1_BCLK_SOC", "1B6": "SAI1_LRCK_SOC", "A7": "SAI1_SDO0_M0",
    "1A6": "SAI1_SDI0_M0", "1D6": "SD_MODE_L", "1C5": "SD_MODE_R",
    "1AD2": "DOCK_DET", "AK4": "CHG_STAT", "1U21": "CHG_EN_SINK_CTRL",
    "1D9": "USB_CHG_ALLOW_SOC", "1B19": "PACK_SARADC_IN2",
}


def connector_pins(filename):
    with (REPOSITORY / "hardware/interconnect" / filename).open(newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream))
    if [row["pin"] for row in rows] != [str(index) for index in range(1, 25)]:
        raise ValueError(f"Expected every numbered contact in {filename}")
    return {row["pin"]: row["net"] for row in rows if row["type"] != "NC"}


def connect_soc(design):
    from collections import Counter

    library = design.libraries.find("library[@name='RK3576']")
    deviceset = library.find("devicesets/deviceset[@name='RK3576']")
    connections = {item.get("pad"): item for item in deviceset.findall("devices/device/connects/connect")}
    pads_for_pin = {(item.get("gate"), item.get("pin")): pad for pad, item in connections.items()}
    occupied = Counter(pads_for_pin[item.get("gate"), item.get("pin")]
                       for item in design.schematic.findall("sheets/sheet/nets/net/segment/pinref[@part='U1']"))
    locations = pin_locations(design.schematic, "U1", library, deviceset)
    for ball, net in SOC_BALLS.items():
        if occupied[ball]:
            raise ValueError(f"Expected unused ball U1.{ball} for {net}")
        connect_pin(locations, "U1", connections[ball], net)


def add_compute_devices(design, library):
    design.import_library(FLEX_LIBRARY)
    bridge = Extension("6ae5713d08860d3c5aa9ff0ccfd014daa86729c1",
                       "hardware/bridge_board/FRIDAY_Bridge_SCH3.sch")
    copy_support_device(library, bridge.libraries.find("library[@name='FRIDAY_SCH3_Camera']"), "SN74LV1T34")
    pads = []
    for index in range(7):
        position_y = 1.95 - 0.65 * index
        pads.extend(((str(index + 1), -2.84, position_y, 1.45, 0.40),
                     (str(14 - index), 2.84, position_y, 1.45, 0.40)))
    package = land_pattern(library, "TI_PW14_TSSOP", 4.4, 5.0, pads)
    element(package, "circle", x=-2.38, y=2.4, radius=0.11, width=0.15, layer=21)
    inline_device(library, "TMUX1511", "TI_PW14_TSSOP",
                  (("VDD", "14"), ("SEL1", "1"), ("S1", "2"), ("GND", "7"), ("SEL2", "4"),
                   ("SEL3", "10"), ("SEL4", "13")),
                  (("D1", "3"), ("S2", "5"), ("D2", "6"), ("S3", "9"), ("D3", "8"),
                   ("S4", "12"), ("D4", "11")))


def flex_sheet(design):
    sheet = design.sheet(9, "FRIDAY / SCH-4b / BRIDGE AND LEFT AUXILIARY FLEX",
                         "D16/D17 and interconnect CSVs | Both cables connect pin 1 to pin 1")
    for reference, filename, x in (("J5", "pinout_right_bridge.csv", 96),
                                    ("J6", "pinout_right_left_aux.csv", 276)):
        design.part(sheet, reference, "FH12-24S-0.5SH(55)", "FH12-24S-0.5SH(55)",
                    x, 211, connector_pins(filename), FLEX_LIBRARY)
    design.note(sheet, "J5/J6 bottom contacts. Pin 1 is at negative X in each unrotated footprint.",
                15.24, 249)
    for number, net, position_x in (
        (801, "CAM_RST_L_RESERVED", 60), (802, "CAM_MCLK_RESERVED", 161),
        (803, "CAM_CRADLE_NTC_RESERVED", 265),
    ):
        reference = f"TP{number}"
        design.test_point(sheet, reference, "RESERVED DNP", position_x, 155, net)
        element(design.parts.find(f"part[@name='{reference}']"), "variant", name="default", populate="no")

    design.resistor(sheet, "R801", "22R 1%", 67, 123, "SAI1_BCLK_SOC", "SAI1_BCLK_M0")
    design.resistor(sheet, "R802", "22R 1%", 190, 123, "SAI1_LRCK_SOC", "SAI1_LRCK_M0")
    design.resistor(sheet, "R803", "0R jumper >= 1A", 309, 123, SYSTEM_5V, "VCC5V0_SYS_S5_AMP")
    design.part(sheet, "U12", "SN74LV1T34", "SN74LV1T34DBVR", 169, 74,
                {"A": "CAM_ENABLE_SOC", "Y": "CAM_ENABLE", "VCC": VCCIO_S0, "GND": "GND"}, AUDIO_LIBRARY)
    design.resistor(sheet, "R804", "100k 1%", 66, 73, "CAM_ENABLE_SOC", "GND")
    design.capacitor(sheet, "C801", "C_0603", "100nF 16V X7R", 258, 79, VCCIO_S0, "GND")
    design.note(sheet, "Place clock resistors at U1. Keep CSI polarity and grounds. Camera I2C pulls up on the bridge only.",
                15.24, 37)


def charger_and_adc_sheet(design):
    sheet = design.sheet(10, "FRIDAY / SCH-4b / CHARGER USB BRANCH AND PACK MONITOR",
                         "Raw USB input ahead of the system mux | Powered-off isolation at the SARADC input")
    design.part(sheet, "U13", "TPS259470", "TPS259470ARPW", 156, 208,
                {"IN": USB_INPUT, "OUT": USB_BRANCH, "GND": "GND",
                 "EN_UVLO": "USB_CHG_ALLOW", "OVLO": "USB_CHG_OVLO",
                 "DVDT": "USB_CHG_DVDT", "ILM": "USB_CHG_ILM"}, AUDIO_LIBRARY)
    design.part(sheet, "U14", "SN74LV1T34", "SN74LV1T34DBVR", 79, 146,
                {"A": "USB_CHG_ALLOW_SOC", "Y": "USB_CHG_ALLOW", "VCC": VCCIO_S0, "GND": "GND"}, AUDIO_LIBRARY)
    design.part(sheet, "Q12", "DMN2058U", "DMN2058U-7", 315, 146,
                {"G": "CHG_EN_SINK_CTRL", "D": "CHG_EN", "S": "GND"}, AUDIO_LIBRARY)
    design.part(sheet, "U15", "TMUX1511", "TMUX1511PWR", 215, 65,
                {"VDD": ADC_REFERENCE_SOURCE, "SEL1": ADC_REFERENCE_SOURCE, "S1": "PACK_DIV_FILTER",
                 "D1": "PACK_SARADC_IN2", "GND": "GND", "SEL2": "GND", "SEL3": "GND", "SEL4": "GND"}, AUDIO_LIBRARY)
    for number, value, x, y, first, second in (
        (805, "365k 1%", 250, 245, USB_INPUT, "USB_CHG_OVLO"),
        (806, "100k 1%", 250, 223, "USB_CHG_OVLO", "GND"),
        (807, "6.65k 1%", 360, 227, "USB_CHG_ILM", "GND"),
        (808, "100k 1%", 48, 172, "USB_CHG_ALLOW_SOC", "GND"),
        (809, "100k 1%", 49, 210, "USB_CHG_ALLOW", "GND"),
        (810, "10k 1%", 204, 172, VCCIO_S0, "DOCK_DET"),
        (811, "10k 1%", 204, 149, VCCIO_S0, "CHG_STAT"),
        (812, "4.7k 1%", 343, 174, VCCIO_S3, "CHG_EN"),
        (813, "100k 1%", 278, 116, "CHG_EN_SINK_CTRL", "GND"),
        (814, "1M 1%", 78, 97, PACK_INPUT, "PACK_DIV_FILTER"),
        (815, "220k 1%", 78, 65, "PACK_DIV_FILTER", "GND"),
        (816, "100k 1%", 328, 65, "PACK_SARADC_IN2", "GND"),
    ):
        design.resistor(sheet, f"R{number}", value, x, y, first, second)
    for number, value, x, y, net in (
        (802, "1uF 25V X7R", 70, 245, USB_INPUT),
        (803, "1nF 25V C0G", 360, 205, "USB_CHG_DVDT"),
        (804, "100nF 16V X7R", 143, 122, VCCIO_S0),
        (805, "100nF 16V X7R", 78, 42, "PACK_DIV_FILTER"),
        (806, "100nF 16V X7R", 328, 91, ADC_REFERENCE_SOURCE),
    ):
        design.capacitor(sheet, f"C{number}", "C_0603", value, x, y, net, "GND")
    design.note(sheet, "Firmware authorizes USB charge only after USB source-current policy allows it.",
                14, 259)
    design.note(sheet, "J4 pad 1 is PACK+_PROT (VBAT_2S_IN). Pad 2 is PACK-_PROT (GND). Existing mux and buck retained.",
                14, 32)


def right_amplifier_sheet(design):
    sheet = design.sheet(11, "FRIDAY / SCH-4b / RIGHT TEMPLE AUDIO",
                         "Dedicated right channel enable. SAI1 clock and data shared with the left amplifier.")
    add_amplifier(design, sheet, "R", SYSTEM_5V, "GND", "SD_MODE_R", ("U16", "J7", "U17", "Q13", 820, 810))


def add_emcp_approvals(design):
    if not APPROVALS_PATH.exists():
        return
    records = APPROVALS_PATH.read_text(encoding="utf-8").splitlines()
    header, signatures = records[0], records[1:]
    if header != APPROVAL_REASON or len(signatures) != 65 or len(set(signatures)) != 65:
        raise ValueError("Expected exactly 65 unique inherited eMCP warning approvals")
    errors = design.schematic.find("errors")
    for signature in signatures:
        code, sheet, x, y, part, pin, net, *unused = signature.split("\t")
        if code != "104" or part != "U11" or not pin or not net:
            raise ValueError(f"Unexpected approval {signature}")
        element(errors, "approved", hash=signature)


def main():
    design = Extension(BASELINE, "hardware/compute_board/FRIDAY_Compute_SCH2.sch")
    library = add_audio_library(design, efuse=True)
    add_compute_devices(design, library)
    connect_soc(design)
    flex_sheet(design)
    charger_and_adc_sheet(design)
    right_amplifier_sheet(design)
    add_emcp_approvals(design)
    design.save_to(BOARD_DIRECTORY / SCHEMATIC_NAME)
    print(f"Generated {SCHEMATIC_NAME} with {len(design.sheets)} sheets and {len(SOC_BALLS)} new SoC connections.")


if __name__ == "__main__":
    main()
