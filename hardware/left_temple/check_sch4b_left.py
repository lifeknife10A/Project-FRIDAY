#!/usr/bin/env python3
"""Run the inherited left-side protection checks and the new audio checks."""

import xml.etree.ElementTree as ElementTree

from check_sch4a_exports import check_paths, expected_rows, require
from gen_sch4b_left import BOARD_DIRECTORY, PROTECTION_FET, SCHEMATIC_NAME, SHUNT
from sch4b_audio import sd_mode_screen


PROTECTION_PADS = {"1": "G1", "4": "G2", "S1_78": "S1A", "S2_56": "S2A", "2": "EP", "3": "EP"}


def check_left(pins, values):
    require(values["Q1"] == PROTECTION_FET and values["RS1"] == SHUNT, "S1 or S2 changed")
    checks = check_paths(pins, values, protection_pads=PROTECTION_PADS, shunt_ohms=0.020)
    require({pad for part, pad in pins if part == "Q1"} == set(PROTECTION_PADS), "Unexpected Q1 pad connection")
    for (reference, pad), expected in {
        ("J3", "9"): "SD_MODE_L",
        ("U5", "1"): "SAI1_SDO0_M0", ("U5", "2"): "AMP_L_GAIN", ("U5", "4"): "AMP_L_SD_MODE",
        ("U5", "7"): "VCC5V0_SYS_S5_AMP", ("U5", "8"): "VCC5V0_SYS_S5_AMP",
        ("U5", "9"): "SPK_L_P", ("U5", "10"): "SPK_L_N", ("U5", "14"): "SAI1_LRCK_M0",
        ("U5", "16"): "SAI1_BCLK_M0", ("U5", "17"): "PACK-_PROT",
        ("U6", "4"): "AMP_L_ENABLE_GATE", ("Q6", "3"): "AMP_L_SD_SOURCE",
        ("R29", "1"): "SD_MODE_L", ("R32", "2"): "AMP_L_SD_MODE",
        ("J4", "1"): "SPK_L_P", ("J4", "2"): "SPK_L_N",
    }.items():
        require(pins.get((reference, pad)) == expected, f"{reference}.{pad} must be on {expected}")

    require(values["R32"] == "1k 1%" and values["R33"] == "4.7k 1%" and values["R34"] == "100k 1%",
            "Left audio channel or gain strap changed")
    sd_low, sd_high, sd_off = sd_mode_screen(1000)
    require(sd_low > 1.500 and sd_off < 0.080, "Left channel or shutdown fails SD_MODE limits")
    pair_ohms = 0.006
    series_ohms = 0.020 + pair_ohms
    checks.extend((
        f"HY2120 discharge threshold at maximum stated FET pair resistance: "
        f"{0.170 / series_ohms:.2f}–{0.230 / series_ohms:.2f} A "
        f"at 170–230 mV and 20 + 6 mΩ, VGS 4.5 V / 25 °C.",
        "At 3 A the shunt and maximum specified FET pair drop sum to 78 mV. Bench-check hot trip and fuse coordination.",
        f"Left SD_MODE high: {sd_low:.3f}–{sd_high:.3f} V at 4.50–5.50 V amp supply. "
        f"Shutdown screen ≤{sd_off * 1000:.1f} mV at the rated 55 °C P-FET leakage point.",
        "MAX98357A gain +3 dB. Speaker outputs remain a local floating BTL pair.",
    ))
    return checks


def main():
    schematic = ElementTree.parse(BOARD_DIRECTORY / SCHEMATIC_NAME).find("drawing/schematic")
    pins = {(part, pad): net for net, part, pad, pin, sheet in expected_rows(schematic)}
    values = {part.get("name"): part.get("value") for part in schematic.findall("parts/part")}
    print("\n".join(check_left(pins, values)))


if __name__ == "__main__":
    main()
