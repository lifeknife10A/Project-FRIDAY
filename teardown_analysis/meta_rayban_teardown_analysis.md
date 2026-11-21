# META RAY-BAN SMART GLASSES: HARDWARE TEARDOWN & ARCHITECTURAL INSPIRATION REPORT
## Reverse Engineering & Comparative Analysis for Project FRIDAY (v9.1.0)

**Document Source:** `/Users/krish/Downloads/Ray-Ban Meta Smart Glasses Teardown.mp4`  
**Full Video Transcription:** [transcription.md](file:///Users/krish/NMIMS/Friday/teardown_analysis/transcription.md)  
**Extracted Frame Directory:** [frames/](file:///Users/krish/NMIMS/Friday/teardown_analysis/frames/)  
**Analysis Date:** November 21, 2026

---

## 1. Executive Summary & Core Architectural Takeaways

The **Ray-Ban Meta Smart Glasses (Gen 2 Headliner/Wayfarer)** represent the current commercial benchmark for consumer smart eyewear. A detailed teardown of the physical hardware reveals how Meta and Luxottica solved the spatial, thermal, mechanical, and electrical routing challenges of putting computing onto a human face.

### The 5 Biggest Insider Discoveries:

1. **Strict Temple Arm Asymmetry:**  
   Meta completely separates compute from energy storage. The **Left Temple** houses the high-density mainboard PCB (Snapdragon AR1 Gen 1, 32GB memory, shielding cans, power switch), while the **Right Temple** houses the single **154 mAh Li-ion battery** and RF antenna flex.
2. **CNC Aluminum Hinge Bridges:**  
   The delicate flex PCB does **not** bend across a raw plastic friction hinge. Meta uses precision CNC aluminum hinge inserts that provide both mechanical screw anchoring and an internal shielded channel through which the flex PCB passes without pinching or shear fatigue.
3. **Dual-Compound Thermal Architecture:**  
   To manage chip thermals within tight plastic enclosures without scorching the wearer's skin, Meta employs **two distinct thermal interface materials (TIM)**:
   * A high-conductivity **green thermal paste** directly between the Snapdragon silicon / RAM and the inner shielding cans.
   * A bulk **black thermal gap filler** on top of the shielding cans to conduct heat to the outer chassis.
4. **Overmolded Nose-Bridge Bus & Embedded Mic:**  
   Rather than running loose wires across the brow, Meta insert-molds copper traces directly through the front frame plastic, connecting the right-temple battery to the left-temple mainboard. Crucially, a **MEMS microphone is embedded directly inside the right nose-pad bracket**, maximizing vocal pickup near the mouth while rejecting temple speaker spillover.
5. **Dedicated Speaker Acoustic Cavity & Membrane:**  
   The open-ear directional audio does not use bare speakers firing into ambient air. Each temple contains an enclosed acoustic back-volume cavity sealed with an acoustic membrane, tuning the resonant frequency and channeling audio downward toward the ear canal.

---

## 2. Head-to-Head Architectural Comparison

| Architectural Dimension | Ray-Ban Meta Smart Glasses (Gen 2) | Project FRIDAY (v9.1.0) | Engineering Rationale / FRIDAY Advantage |
| :--- | :--- | :--- | :--- |
| **Computing Model** | **Tethered Peripheral:** Audio/video streamed over Bluetooth/Wi-Fi to smartphone for cloud AI processing. | **Sovereign On-Device Edge AI:** 100% on-device vision, Whisper STT, 0.5B VLM, and Kokoro TTS on local NPU/CPU. | Absolute privacy, zero cellular latency, full functionality offline. |
| **SoC / Silicon** | Qualcomm Snapdragon AR1 Gen 1 (4nm, low-power vision/ISP coprocessor). | Rockchip RK3576 (8-core, 6.0 TOPS NPU @ INT8 / native INT4, LPDDR4x). | NPU-accelerated autoregressive neural token generation ($35\text{ tok/s}$). |
| **Battery Topology** | **Single 1S Cell (154 mAh, ~0.59 Wh)** in Right Temple only. | **Balanced Series 2S Dual Cells (2x 300mAh, 2.22 Wh, 7.4V)** across both temples. | **$3.76\times$ the energy capacity**; 2S cuts through-bridge current by $50\%$ and hinge $I^2R$ heat by $75\%$. |
| **Weight** | **48.6 – 50.8 grams** (lightweight daily sunglasses). | **115.0 grams** (audited, self-contained AI computer). | Trade-off: FRIDAY carries $4\times$ battery mass, NPU heatsinks, and phase-change materials to run untethered LLMs. |
| **Thermal Dissipation** | Dual-paste conduction to plastic shell (rated for short 60s video bursts). | Copper spreader + **PureTemp 40 Phase Change Material (PCM)** + aerogel skin barrier. | Absorbs $31.44\text{ J}$ active 3.0W neural burst into $600\text{ J}$ latent heat buffer; keeps skin $\le 37.5^\circ\text{C}$. |
| **Audio Synthesis** | Cloud TTS synthesized on smartphone, streamed over Bluetooth A2DP. | **Local Kokoro-82M Studio Voice (`bf_emma`)** running on quad Cortex-A72 at 24 kHz. | Zero internet reliance, ultra-low Time-to-First-Audio ($<200\text{ ms}$ chunking). |
| **Audio Transducers** | Micro dynamic drivers with acoustic ported cavities. | Dual local **MAX98357A I2S Mono Amps** + directional temple exciters. | Digital I2S across bridge avoids PWM EMI; hardware $<0.1\,\mu\text{A}$ sleep biasing. |
| **Nose-Bridge Routing** | Insert-molded copper traces in injection-molded nylon. | 18C Left / 34C Right **Rigid-Flex Harness** with $\ge 2.0\text{mm}$ $2\text{ oz}$ Cu power pours ($<0.03\,\Omega$). | Eliminates expensive multi-million dollar insert-molding tooling for student capstone. |

---

## 3. Detailed Subsystem Analysis & Keyframe Review

### 3.1 Left Temple: Compute Mainboard & Audio Cavity
- **Video Timestamp:** `[01:45 -> 02:05]`  
- **Extracted Frame:** `01_left_arm_opened_pcb_speaker_01_48.jpg`  
- **Hardware Observations:**
  * The left arm is split along a near-zero-gap adhesive joint.
  * The mainboard is a multi-layer rigid PCB with two primary RF/EMC shielding cans.
  * A micro slide switch is mounted on the inner rim for hardware power cut.
  * The speaker transducer sits in a dedicated acoustic recess directly behind the mainboard, with an acoustic tuning membrane.
  * Pogo pins on the inner face provide direct spring-loaded mating to the front-frame camera flex.

### 3.2 Hinge Channeling & CNC Aluminum Inserts
- **Video Timestamp:** `[02:15 -> 02:35]` and `[07:52 -> 08:05]`  
- **Extracted Frames:** `02_cnc_hinge_flex_channel_02_15.jpg`, `13_hinge_flex_routing_overview_07_52.jpg`  
- **Hardware Observations:**
  * Standard glasses hinges experience severe rotational shear. Meta solved this by anchoring a **CNC machined aluminum bracket** into the hinge block.
  * The flex PCB is channeled through the neutral bending axis of this metal insert, ensuring that folding the glasses does not pinch, crease, or fatigue the polyimide substrate.
  * **Direct Takeaway for FRIDAY:** In our 3D-printed PETG frame, we must design an internal filleted curved channel ($R \ge 2.5\text{ mm}$) at the hinge interface to prevent sharp $90^\circ$ bends on our 18-conductor and 34-conductor flexes.

### 3.3 Silicon Packaging & Dual Thermal Interface Materials (TIM)
- **Video Timestamp:** `[03:05 -> 03:45]`  
- **Extracted Frames:** `04_mainboard_cans_black_thermal_paste_03_05.jpg`, `05_cans_removed_green_thermal_paste_snapdragon_03_24.jpg`, `06_snapdragon_ar1_and_32gb_storage_03_40.jpg`  
- **Hardware Observations:**
  * Removing the top shielding can reveals the Snapdragon AR1 processor co-packaged with RAM.
  * A distinctive **green high-viscosity thermal paste** bridges the top of the Snapdragon die to the metal shielding can.
  * On the outside of the can, a layer of **black thermal gap-filler** conducts heat outward toward the temple shell.
  * The cans feature internal stamped recesses to prevent metal-to-silicon edge contact during drop impacts.
  * **Direct Takeaway for FRIDAY:** Validates our dual thermal strategy. FRIDAY uses thermal grease/copper shim from the RK3576 die to the heat-spreader, coupled to our PureTemp 40 PCM pad to buffer active inference bursts.

### 3.4 Right Temple: Battery & Antenna Subsystem
- **Video Timestamp:** `[04:05 -> 04:30]`  
- **Extracted Frames:** `07_right_arm_opened_battery_154mah_04_05.jpg`, `08_antenna_flex_under_battery_04_20.jpg`  
- **Hardware Observations:**
  * The entire volume of the right arm is dedicated to a **154 mAh (3.85V, 0.59 Wh)** custom-contoured Li-ion pouch cell.
  * A thin polyimide flex PCB runs underneath the battery cell, integrating the Bluetooth/Wi-Fi antenna elements on an adhesive carrier.
  * **Why FRIDAY Diverges:** Meta's 154 mAh battery only lasts 4 hours because the phone does the AI heavy lifting. For FRIDAY's sovereign edge AI, a single 154 mAh cell would die in 20 minutes under 3.0W load. FRIDAY's balanced **Series 2S (2x 300mAh = 600mAh total @ 7.4V = 2.22 Wh)** delivers over $3.7\times$ the energy and halves the current across the bridge.

### 3.5 Nose Bridge: Overmolded Charging & Embedded Nose Microphone
- **Video Timestamp:** `[05:20 -> 05:40]`  
- **Extracted Frames:** `10_nose_piece_overmolded_charge_pins_and_mic_05_20.jpg`, `11_dremel_cut_frame_charge_trace_cross_section_05_38.jpg`  
- **Hardware Observations:**
  * Meta placed the magnetic charging pogo contacts directly inside the nasal bridge saddle.
  * Under the Dremel cross-section, a micro MEMS microphone is embedded right inside the plastic nose-pad bracket.
  * **Acoustic Advantage:** Placing a microphone on the nose pad positions it significantly closer to the speaker's vocal tract while gaining natural acoustic shielding from temple-mounted open-ear speakers, drastically simplifying echo cancellation.

---

## 4. Implementation Guidance for Project FRIDAY

From this teardown, the following 4 engineering optimizations are adopted for Project FRIDAY:

1. **Acoustic Port Geometry for Temple Tips:**  
   Do not point bare speakers outward. Design a directional down-firing port ($1.5\text{ mm} \times 6.0\text{ mm}$ slot) directly above the ear canal in the PETG temple arm CAD with a felt acoustic damping mesh.
2. **Nose-Pad Microphone Placement Option:**  
   In addition to our front-right frame microphones, routing one of our INMP441 MEMS microphone channels down into the right nose-pad bracket (mimicking Meta's placement) will improve voice SNR during outdoor wind noise.
3. **Smooth Curved Hinge Flex Guide:**  
   Implement a curved cable relief pocket ($R \ge 3.0\text{ mm}$) in the Fusion 360 parametric frame CAD where the 18C and 34C FFC cables cross the hinge, preventing pinch damage when folding.
4. **Self-Molded Surface Strategy:**  
   Confirming the teardown's finding: printing our frame in solid-core Black PETG eliminates paint chipping, provides shore D80 structural stiffness, and withstands $75^\circ\text{C}$ glass transition temperature without post-finishing.
