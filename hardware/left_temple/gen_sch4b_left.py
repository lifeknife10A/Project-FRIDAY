#!/usr/bin/env python3
"""Extend the reviewed SCH-4a left schematic with S1, S2 and its speaker stage."""

from pathlib import Path

from gen_sch4a import RETURN, element, inline_device, land_pattern
from sch4b_audio import AUDIO_LIBRARY, Extension, add_amplifier, add_audio_library


BOARD_DIRECTORY = Path(__file__).resolve().parent
BASELINE = "e0005989c094caf399fa8bd38fa73b7501675df8"
SCHEMATIC_NAME = "FRIDAY_Left_SCH4b.sch"
PROTECTION_FET = "SiSF04DN-T1-GE3"
SHUNT = "WSK2512R0200FEA 20mR 1W"


def add_protection_fet(library):
    pads = [(str(number), -1.305, (2.5 - number) * 0.65, 1.29, 0.40)
            for number in range(1, 5)]
    pads.extend((("S1_78", 0.60, 0.82, 1.64, 1.35), ("S2_56", 0.60, -0.82, 1.64, 1.35)))
    package = land_pattern(library, "POWERPAK_1212_8SCD", 3.30, 3.30, pads)
    element(package, "circle", x=-1.95, y=1.44, radius=0.10, width=0.15, layer=21)

    # Vishay 63021 p.1. Pin pairs 7/8 and 5/6 each share one shaped source land.
    source_outline = ((1.95, 0.532), (1.50, 0.532), (1.50, 0.763), (1.95, 0.763),
                      (1.95, 1.184), (1.50, 1.184), (1.50, 1.499), (0.040, 1.499),
                      (0.040, 1.698), (-0.260, 1.698), (-0.260, 0.116), (1.95, 0.116))
    for pad_name, direction in (("S1_78", 1), ("S2_56", -1)):
        pad = package.find(f"smd[@name='{pad_name}']")
        pad.set("stop", "no")
        pad.set("cream", "no")
        for layer in (1, 29):
            outline = element(package, "polygon", width="0.05", layer=layer)
            for x, y in source_outline:
                element(outline, "vertex", x=x, y=round(direction * y, 3))
        # Split the paste into a central window and the two external toe windows.
        element(package, "rectangle", x1="-0.19", y1=min(direction * 0.24, direction * 1.39),
                x2="1.37", y2=max(direction * 0.24, direction * 1.39), layer=31)
        for low, high in ((0.18, 0.47), (0.84, 1.10)):
            element(package, "rectangle", x1="1.49", y1=min(direction * low, direction * high),
                    x2="1.88", y2=max(direction * low, direction * high), layer=31)
    inline_device(library, "SISF04DN", "POWERPAK_1212_8SCD",
                  (("G1", "1"), ("S1", "S1_78"), ("D1_D2", "2 3")),
                  (("G2", "4"), ("S2", "S2_56")))


def replace_protection(design, library):
    add_protection_fet(library)
    old_part = design.parts.find("part[@name='Q1']")
    old_part.set("library", AUDIO_LIBRARY)
    old_part.set("deviceset", "SISF04DN")
    old_part.set("value", PROTECTION_FET)
    design.parts.find("part[@name='RS1']").set("value", SHUNT)


def main():
    design = Extension(BASELINE, "hardware/left_temple/FRIDAY_Left_SCH4a.sch")
    audio_library = add_audio_library(design)
    replace_protection(design, audio_library)
    sheet = design.sheet(5, "FRIDAY / SCH-4b / LEFT TEMPLE AUDIO",
                         "J3 pins 2–3 switched 5 V, 5/7/8 SAI1, 9 channel enable")
    add_amplifier(design, sheet, "L", "VCC5V0_SYS_S5_AMP", RETURN, "SD_MODE_L",
                  ("U5", "J4", "U6", "Q6", 29, 16))
    design.save_to(BOARD_DIRECTORY / SCHEMATIC_NAME)
    print(f"Generated {SCHEMATIC_NAME} from {BASELINE[:7]} with five sheets.")


if __name__ == "__main__":
    main()
