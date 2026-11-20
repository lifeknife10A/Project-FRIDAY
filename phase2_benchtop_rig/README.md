# PHASE 2: EMBEDDED BRING-UP & BENCHTOP DEV RIG
## Project FRIDAY Systems Engineering & Electronics Bring-Up Guide

This directory houses the embedded bring-up documentation, harness pinouts, and test procedures for assembling the benchtop development rig before committing to wearable frame integration.

---

## 1. Directory Structure

```
phase2_benchtop_rig/
├── README.md                      # This bring-up guide
├── pinouts/
│   └── hinge_harness_pinout.csv   # Complete pinout map for 18C Left and 34C Right flexes
└── firmware/                      # (Staged for Milestone 2.3 Rust runtime & coprocessor C code)
```

---

## 2. Benchtop Development Topology

Rather than building directly inside the glasses frame, Phase 2 mounts all components flat on an acrylic breadboard base plate:
1. **Compute Brain:** Orange Pi 5 (Rockchip RK3588S) or Luckfox RK3576 development board.
2. **Vision Ingestion:** Sony IMX415 MIPI CSI-2 camera module connected via a 15-pin FFC ribbon.
3. **Audio Capture:** $2\times$ INMP441 I2S MEMS microphone breakout boards mounted $15\text{ mm}$ apart with isolated star-ground return.
4. **Audio Playback:** $2\times$ MAX98357A I2S Class-D amplifier breakout boards driving $8\,\Omega$ bone-conduction transducers.
   * Left Amp: $10\text{ k}\Omega$ pull-up to $1.8\text{V}$ $\implies$ Decodes **LEFT Channel**.
   * Right Amp: $82\text{ k}\Omega$ pull-up to $1.8\text{V}$ $\implies$ Decodes **RIGHT Channel**.
5. **Coprocessor Node:** Raspberry Pi Pico (RP2040) or ESP32-S3 emulating the Ambiq Apollo4 Lite:
   * Plays the $<80\text{ ms}$ earcon chime over I2S upon wake-word detection.
   * Buffers speech audio in circular SRAM while pulsing host wake GPIO.
   * Monitors BQ25887 charger telemetry over I2C and asserts the hardware `CD` interlock.

---

## 3. Harness Conductor Verification Check

Before connecting battery power:
* Refer to [hinge_harness_pinout.csv](file:///Users/krish/NMIMS/Friday/phase2_benchtop_rig/pinouts/hinge_harness_pinout.csv) for the full netlist.
* Verify that **`PACK+`** and **`PACK-`** maintain $> 100\text{ M}\Omega$ isolation from `DGND` and `MIC_STAR_GND` prior to powering up the system.
* Verify that `CELL_MID` reads $3.7\text{V}$ nominal relative to `PACK-` and that total pack voltage is $7.4\text{V}$ nominal.
