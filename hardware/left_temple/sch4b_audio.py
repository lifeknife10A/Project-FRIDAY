"""Shared EAGLE capture for the two MAX98357A amplifier stages."""

import subprocess
import xml.etree.ElementTree as ElementTree

from gen_sch4a import (
    LIBRARIES, REPOSITORY, SUPPORT, Schematic, element, horizontal_pair,
    inline_device, land_pattern, power_library,
)


AUDIO_LIBRARY = "FRIDAY_SCH4b_Audio"
AMPLIFIER_LIBRARY = "MAX98357AETE_T"
AMPLIFIER_DEVICE = "MAX98357AETE+T"
FLEX_LIBRARY = "FH12-24S-0.5SH_55_"


class Extension(Schematic):
    def __init__(self, baseline, path):
        contents = subprocess.check_output(["git", "show", f"{baseline}:{path}"], cwd=REPOSITORY)
        self.root = ElementTree.fromstring(contents)
        self.schematic = self.root.find("drawing/schematic")
        self.parts = self.schematic.find("parts")
        self.sheets = self.schematic.find("sheets")
        self.libraries = self.schematic.find("libraries")

    def import_library(self, name):
        if self.libraries.find(f"library[@name='{name}']") is None:
            library = ElementTree.parse(LIBRARIES / f"{name}.lbr").find("drawing/library")
            library.set("name", name)
            self.libraries.append(library)

    def capacitor(self, sheet, reference, package, value, x, y, positive, ground):
        self.part(sheet, reference, package, value, x, y, {"1": positive, "2": ground}, SUPPORT)

    def resistor(self, sheet, reference, value, x, y, first, second, package="R_0603", populate=True):
        self.part(sheet, reference, package, value, x, y, {"1": first, "2": second}, SUPPORT)
        if not populate:
            element(self.parts.find(f"part[@name='{reference}']"), "variant", name="default", populate="no")

    def save_to(self, path):
        ElementTree.indent(self.root, space="  ")
        schematic = ElementTree.tostring(self.root, encoding="unicode")
        path.write_text(
            '<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE eagle SYSTEM "eagle.dtd">\n' + schematic + "\n",
            encoding="utf-8",
        )


def copy_support_device(destination, original, name):
    deviceset = original.find(f"devicesets/deviceset[@name='{name}']")
    package_name = deviceset.find("devices/device").get("package")
    symbol_name = deviceset.find("gates/gate").get("symbol")
    for section, tag, key in (("packages", "package", package_name), ("symbols", "symbol", symbol_name),
                               ("devicesets", "deviceset", name)):
        target = destination.find(section)
        if target.find(f"{tag}[@name='{key}']") is None:
            target.append(original.find(f"{section}/{tag}[@name='{key}']"))


def add_audio_library(design, efuse=False):
    design.import_library(AMPLIFIER_LIBRARY)
    audio = element(design.libraries, "library", name=AUDIO_LIBRARY)
    for section in ("packages", "symbols", "devicesets"):
        element(audio, section)
    original = power_library(ElementTree.Element("libraries"))
    for name in ("AO3401A", "C_1206"):
        copy_support_device(audio, original, name)
    if efuse:
        for name in ("TPS259470", "SMF_TVS"):
            copy_support_device(audio, original, name)
    comparator_pads = (("1", -0.95, -1.05, 0.65, 0.85), ("2", 0, -1.05, 0.65, 0.85),
                       ("3", 0.95, -1.05, 0.65, 0.85), ("4", 0.95, 1.05, 0.65, 0.85),
                       ("5", -0.95, 1.05, 0.65, 0.85))
    land_pattern(audio, "TI_DBV_SOT23_5", 2.9, 1.6, comparator_pads)
    inline_device(audio, "TLV7041", "TI_DBV_SOT23_5",
                  (("IN+", "3"), ("IN-", "4"), ("VCC", "5"), ("GND", "2")), (("OUT", "1"),))
    speaker = land_pattern(audio, "FRIDAY_SPEAKER_SOLDER_LANDS", 6.2, 2.8,
                           horizontal_pair(1.9, 2.4, 2.8))
    for pad in speaker.findall("smd"):
        pad.set("cream", "no")
    inline_device(audio, "BTL_SPEAKER", "FRIDAY_SPEAKER_SOLDER_LANDS",
                  (("SPK_P", "1"),), (("SPK_N", "2"),))
    return audio


def add_amplifier(design, sheet, side, supply, ground, mode, references):
    amplifier, speaker, comparator, high_fet, first_resistor, first_capacitor = references
    enable_gate = f"AMP_{side}_ENABLE_GATE"
    reference_voltage = f"AMP_{side}_SELECT_REF"
    select_gate = f"AMP_{side}_SELECT_GATE"
    enable_supply = f"AMP_{side}_SD_SOURCE"
    select = f"AMP_{side}_SD_MODE"
    gain = f"AMP_{side}_GAIN"
    positive = f"SPK_{side}_P"
    negative = f"SPK_{side}_N"

    design.part(sheet, amplifier, AMPLIFIER_DEVICE, "MAX98357AETE+T", 183, 200.66,
                {"VDD": supply, "GND": ground, "EP": ground, "SD_MODE": select, "GAIN_SLOT": gain,
                 "BCLK": "SAI1_BCLK_M0", "LRCLK": "SAI1_LRCK_M0", "DIN": "SAI1_SDO0_M0",
                 "OUTP": positive, "OUTN": negative}, AMPLIFIER_LIBRARY)
    design.part(sheet, speaker, "BTL_SPEAKER", "1510 / 8 ohm assumed", 332, 200.66,
                {"SPK_P": positive, "SPK_N": negative}, AUDIO_LIBRARY)
    design.part(sheet, comparator, "TLV7041", "TLV7041DBVR", 120, 117,
                {"IN+": reference_voltage, "IN-": enable_gate, "VCC": supply,
                 "GND": ground, "OUT": select_gate}, AUDIO_LIBRARY)
    design.part(sheet, high_fet, "AO3401A", "AO3401A", 252, 117,
                {"G": select_gate, "S": supply, "D": enable_supply}, AUDIO_LIBRARY)
    for offset, value, x, y, first, second in (
        (0, "1k 1%", 51, 139, mode, enable_gate),
        (1, "100k 1%", 51, 94, enable_gate, ground),
        (2, "100k 1%", 191, 144, supply, select_gate),
        (3, "1k 1%" if side == "L" else "16.2k 1%", 330, 112, enable_supply, select),
        (4, "4.7k 1%", 330, 81, select, ground),
        (5, "100k 1%", 62, 183, supply, gain),
        (6, "56k 1%", 114, 83, supply, reference_voltage),
        (7, "10k 1%", 184, 83, reference_voltage, ground),
    ):
        design.resistor(sheet, f"R{first_resistor + offset}", value, x, y, first, second)
    for offset, package, value, x in (
        (0, "C_0603", "100nF 16V X7R", 187),
        (1, "C_0805", "10uF 16V X7R", 259),
        (2, "C_0603", "100nF 16V X7R", 65),
    ):
        design.capacitor(sheet, f"C{first_capacitor + offset}", package, value, x, 246, supply, ground)
    if side == "L":
        design.part(sheet, f"C{first_capacitor + 3}", "C_1206", "22uF 16V X7R", 335, 246,
                    {"1": supply, "2": ground}, AUDIO_LIBRARY)
    design.note(sheet, "0.8 W into assumed 8 ohms is a software and bench limit. GAIN_SLOT is set to +3 dB.",
                15.24, 63)
    design.note(sheet, "Local BTL speaker pair. Verify >10 uH voice-coil inductance and emissions.",
                15.24, 53)
    design.note(sheet, "Host low or high-Z shuts down. Host high selects the fitted channel through the local rail.",
                15.24, 43)


def sd_mode_screen(series_ohms, supply_low=4.50, supply_high=5.50):
    """Worst corners from the SD_MODE table, resistor tolerances and selector losses."""
    def parallel(first, second):
        return 1 / (1 / first + 1 / second)

    parallel_low = parallel(4700 * 0.99, 92000)
    parallel_high = parallel(4700 * 1.01, 108000)
    low = (supply_low - 0.01) * parallel_low / (series_ohms * 1.01 + parallel_low)
    high = supply_high * parallel_high / (series_ohms * 0.99 + parallel_high)
    off = 5e-6 * parallel_high
    return low, high, off


def gpio_channel_screen():
    """Check nominal divider tolerances against the full Rockchip 1.8 V GPIO range."""
    reference_low = 4.50 * 9900 / (56560 + 9900) - 0.030
    reference_high = 5.50 * 10100 / (55440 + 10100) + 0.030
    host_low_max = 0.25 * 1.95
    host_high_min = 0.75 * 1.65 * 99000 / (99000 + 1010)
    if not host_low_max < reference_low < reference_high < host_high_min:
        raise ValueError("Comparator references fail the 1.8 V GPIO limits")
    return (f"SD selector input trip screen {reference_low:.3f}–{reference_high:.3f} V "
            f"between host low ≤{host_low_max:.3f} V and high ≥{host_high_min:.3f} V.")
