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

## 2. Zero-Waste Benchtop Development Topology

To eliminate drawer waste and protect student capital:
1. **Zero-Rupee Audio & Peripheral Pre-Testing (Raspberry Pi 3B):**
   * Uses the student's on-hand **Raspberry Pi 3B (1 GB)** to validate peripheral circuitry before purchasing any new compute hardware:
   * **Audio Output:** Test I2S digital audio clocking (`GPIO 18 BCLK`, `GPIO 19 LRCLK`, `GPIO 21 DOUT`) driving dual MAX98357A amplifiers.
     * Left Amp: $\le 10\text{ k}\Omega$ pull-up to $1.8\text{V} \implies$ Decodes **LEFT Channel**.
     * Right Amp: Single $82\text{ k}\Omega$ pull-up to $1.8\text{V} \implies$ Decodes **RIGHT Channel**.
   * **Audio Input:** Connect $2\times$ INMP441 I2S MEMS microphones with an isolated star-ground return and test WebRTC AEC3 echo cancellation in software.
   * **Cost:** **₹0** out-of-pocket for compute.
2. **Single-Shot Target Hardware Bring-Up:**
   * After Phase 1 software and Phase 2 audio peripherals are validated, purchase only the target **Luckfox RK3576 / Core3576 module** (6.0 TOPS NPU) that mounts directly into the final Track 1 thick-temple wearable frame.
   * Intermediate evaluation boards (e.g. Orange Pi 5) are strictly bypassed.

---

## 3. Harness Conductor Verification Check

Before connecting battery power:
* Refer to [hinge_harness_pinout.csv](file:///Users/krish/NMIMS/Friday/phase2_benchtop_rig/pinouts/hinge_harness_pinout.csv) for the full netlist.
* Verify that **`PACK+`** and **`PACK-`** maintain $> 100\text{ M}\Omega$ isolation from `DGND` and `MIC_STAR_GND` prior to powering up the system.
* Verify that `CELL_MID` reads $3.7\text{V}$ nominal relative to `PACK-` and that total pack voltage is $7.4\text{V}$ nominal.
