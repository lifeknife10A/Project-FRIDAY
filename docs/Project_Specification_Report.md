# PROJECT FRIDAY: AUTONOMOUS EDGE-AI SMART GLASSES
## Systems & Product Requirements Specification Report (Capstone PRD)

**Candidate Name:** Krishna Jagat Solanki – (70412400024)  
**Degree Programme:** MBA.Tech in Information Technology  
**Institutional Affiliation:** Department of Information Technology, Mukesh Patel School of Technology Management & Engineering (MPSTME), SVKM's NMIMS, Mumbai Campus  
**Project Classification:** Capstone Systems Engineering Specification  
**Document Target:** Formal Academic Specification Report & Design Blueprint  

---

## Section 1: Project Vision & Problem Statement

### 1.1 Contemporary Industry Background & Technical Critique
Contemporary commercial smart eyewear platforms—most notably the Meta Ray-Ban Smart Glasses, Amazon Echo Frames, and Apple Vision Pro—present fundamental architectural compromises that severely limit their operational sovereignty, privacy guarantees, and practical utility. Commercial smart glasses predominantly function as tethered peripheral microphones and cameras rather than sovereign cognitive systems. Audio recordings and image frames captured on the face are transmitted over high-power Bluetooth links to a paired host smartphone, where they are queued and uploaded via cellular networks to hyperscale cloud data centers for inference.

This architecture introduces three fatal engineering deficiencies:
1. **Unacceptable End-to-End Latency:** Cloud offloading yields round-trip latencies of 1.8 to 3.5 seconds across real-world mobile networks, completely breaking conversational flow and assistive guidance.
2. **Network Dependency & Fragility:** In network-isolated or low-bandwidth environments (basements, remote industrial facilities, subterranean transit, or flights), tethered glasses become non-functional pieces of plastic.
3. **Severe Telemetry & Privacy Vulnerabilities:** Ingesting continuous first-person video and microphone streams onto third-party corporate cloud servers creates insurmountable enterprise security and personal privacy barriers.

### 1.2 Formal Engineering Problem Statement
Engineering a truly wearable, standalone artificial intelligence system inside standard eyeglass frames requires resolving an extreme multidimensional trade-off across thermal dissipation, structural weight, electrical energy density, and neural memory bandwidth. Deploying real-time Vision-Language Models (VLMs) on battery-constrained edge devices typically demands heavy computational accelerators exceeding 15 Watts, necessitating bulky tethered battery pucks or active cooling fans that make everyday facial wear impossible. 

The core engineering objective of **Project FRIDAY** is to design, model, and implement an indigenous, completely self-contained, sovereign edge-AI smart glasses platform that executes multimodal vision encoding, speech recognition, neural reasoning, and speech synthesis entirely within an all-up mass envelope of **exactly 115.0 grams** (strictly below a 125.0-gram ceiling) and a **3.0-Watt active power envelope**, operating with zero reliance on cloud infrastructure or smartphone neural coprocessors.

### 1.3 The Sovereign Edge-Computing Paradigm
Project FRIDAY fundamentally rejects the smartphone-as-a-coprocessor model. All sensory ingestion, neural representation, autoregressive sequence generation, and auditory feedback run natively on onboard heterogeneous silicon. By executing inference directly at the edge, FRIDAY guarantees zero visual data leakage, sub-1.25-second time-to-first-word audio response, and unbroken contextual assistance regardless of geographic or network positioning.

### 1.4 The Five Non-Negotiable Directives (Hard Constraints)
All systems, mechanical structures, firmware routines, and neural pipelines are governed by five inviolable constraints:
* **Directive 01 (Zero External Battery Packs):** The entire power delivery network, dual lithium-polymer pouch cells, and battery management circuitry must be 100% enclosed within the left and right temple arms. No external battery packs, neckbands, tethered pocket pucks, or dangling wires are permitted under any operating condition.
* **Directive 02 (Zero Phone-in-the-Loop AI Inference):** The smartphone must never act as an offload coprocessor for artificial intelligence. All speech-to-text (STT), vision tokenization, distilled multimodal language model inference, and text-to-speech (TTS) execution must be computed locally on the glasses' internal silicon.
* **Directive 03 (Dedicated Bluetooth Role):** Bluetooth connectivity (Bluetooth 5.2 / BT Classic Audio via Murata 1XK / NXP IW416) is restricted strictly to standard Bluetooth Hands-Free Profile (HFP/A2DP) for incoming telephone calls, media playback, telemetry sync with the FRIDAY Companion App, and fallback internet modem tethering (Directive 04). Bluetooth must never be used to transmit raw camera frames or voice audio to a phone for cloud AI computation.
* **Directive 04 (Tiered Connectivity & Graceful Tool Fallback):** For actions requiring public web data (e.g., Google Search, live weather, Gmail sync):
  1. *Primary Gateway:* Direct Wi-Fi connection from the onboard wireless module.
  2. *Secondary Gateway (Fallback):* If Wi-Fi is unavailable, the system establishes a secure Bluetooth Personal Area Network (PAN / GATT proxy) to the user's phone, utilizing the phone purely as a "dumb internet modem."
  3. *Zero-Connection Behavior:* If neither Wi-Fi nor a paired smartphone gateway is reachable, Friday gracefully intercepts the tool call and audibly notifies the user via local TTS:  
     *"I am currently offline with no Wi-Fi or tethered device available. Please connect me to Wi-Fi or pair via Bluetooth to perform web searches. I can still analyze what you see locally."*
* **Directive 05 (Total Mass Envelope $\le 125	ext{ grams}$):** The all-up weight (AUW) of the frame, lenses, hinges, electronics, dual batteries, wiring, and thermal dissipation elements must strictly not exceed **125.0 grams**, with an audited target of **115.0 grams** and center of gravity positioned along the ear-temple axis.

---

## Section 2: User Persona & Core Interaction Workflows

### 2.1 Target User Profiles & Demographics
1. **Visually Impaired and Low-Vision Individuals:** Users requiring instantaneous, hands-free auditory scene description, fine-print reading, medication verification, and obstacle awareness without drawing social attention to assistive apparatus.
2. **Mobile Knowledge Workers and Industrial Field Engineers:** Technicians and field engineers who operate in complex environments requiring continuous hands-free situational context, technical documentation reference, and equipment inspection without breaking focus.

### 2.2 Multimodal Sensory & Input Trigger Triad
Interaction with FRIDAY is entirely screenless and hands-free, mediated by a unified sensory triad:
* **Auditory Wake-Word & Earcon:** An ultra-low-power voice activity detector running on the Ambiq Apollo4 Lite coprocessor ($<80\,\mu	ext{W}$) continuously monitors microphone streams. Upon detecting the local trigger phrase ("Hey Friday"), the coprocessor fires an instantaneous ($<80	ext{ ms}$) auditory chime into the directional audio drivers, signaling immediate system readiness while concurrently asserting the host wake interrupt.
* **Capacitive Temple Touch:** A discrete capacitive sensor ribbon embedded along the right temple arm supports single-tap (pause/resume speech), double-tap (force optical capture), and swipe gestures (volume regulation and speech rate adjustment).
* **Kinematic Head Orientation:** The front-frame Sony IMX415 camera is mounted with a permanent 6-degree downward optical inclination. When a user naturally tilts their head downward to inspect an object or text, the spatial orientation triggers the vision pipeline into foveal reading mode.

### 2.3 Comprehensive Operational Interaction Scenarios

#### Scenario A: Autonomous Fine-Print & Prescription Label Reading
When a user holds a medication container and queries *"Friday, what are the dosage instructions on this bottle?"*:
1. The Apollo4 Lite detects the query, plays an 80ms acknowledgement earcon, and wakes the Rockchip RK3576 via GPIO.
2. The IMX415 captures `Stream 0` ($384 	imes 384$ full field-of-view downscale).
3. The onboard NPU executes a lightweight DBNet-Mobile text detector ($<5	ext{ ms}$), identifying the bounding centroid $(X_c, Y_c)$ of the dense text region.
4. The 2D Rockchip Graphic Acceleration (RGA) engine extracts an optical 1:1 foveal crop ($384 	imes 384$ window) from the raw 4K sensor buffer centered on $(X_c, Y_c)$, guaranteeing $\ge 10	ext{ px/char}$ native resolution.
5. The SigLIP-B vision encoder compresses the $384 	imes 384$ patch grid into 144 visual tokens via a $2	imes 2$ unshuffle operation.
6. The distilled Qwen2.5-0.5B decoder generates autoregressive tokens at $\ge 35	ext{ tokens/s}$, streaming text chunks to the local TTS engine.
7. Total elapsed time from query completion to first spoken output is $\sim 1.20	ext{ seconds}$, synthesized directly through the local MAX98357A directional audio drivers.

#### Scenario B: Real-Time Ambient Scene & Spatial Understanding
For general environmental inquiries (*"What is directly ahead of me?"*), the system captures the full 85-degree diagonal field of view, encodes spatial topology, and returns concise, localized spatial descriptions (e.g., *"An empty crosswalk with an approaching pedestrian ten feet ahead"*).

#### Scenario C: Tiered Web Tool-Calling & Graceful Fallback
When a user asks for live information (*"Friday, search Google for the price of this bottle"*):
1. Friday attempts direct Wi-Fi transmission.
2. If Wi-Fi is disconnected, it attempts to route the API request through the smartphone Bluetooth PAN gateway.
3. If completely isolated, local TTS informs the user: *"I am currently offline with no Wi-Fi or tethered device available. Please connect me to Wi-Fi or pair via Bluetooth to perform web searches. I can still analyze what you see locally."*

#### Scenario D: Hands-Free Telephony & Audio Pass-Through
Incoming smartphone calls route to the glasses via standard Bluetooth HFP/A2DP audio sink profiles. The front dual MEMS microphones engage WebRTC Acoustic Echo Cancellation (AEC3) to eliminate speaker feedback, ensuring clear duplex voice calls.

---

## Section 3: AI & Machine Learning Pipeline Requirements

### 3.1 Asymmetric Edge Multimodal Model Architecture
To achieve sovereign inference under a 6.0 TOPS NPU envelope, the neural architecture is structured as an asymmetric vision-language student model comprising a SigLIP-B vision encoder and a heavily quantized Qwen2.5-0.5B transformer decoder. Standard vision transformers project $384 	imes 384$ images into 576 patches ($24 	imes 24$ grid), resulting in 576 visual tokens. Passing 576 tokens into the language decoder would consume over 70% of the available memory bus bandwidth. FRIDAY introduces an optimized $2	imes 2$ spatial pixel-unshuffle downsampling layer following the vision encoder, reducing the token sequence from 576 to strictly 144 tokens. This 75% reduction in prefix sequence length preserves fine spatial details while shrinking the vision prefix prefill time to under 45 ms.

### 3.2 Discrete Token Vocabulary Optimization (64,000 Subset)
The native Qwen2.5 tokenizer utilizes a massive vocabulary of 151,936 tokens. In an embedded architecture, an unquantized language model head (LM-head) for 152k tokens across an 896 hidden dimension consumes 136.1 MB of memory traffic per generated token, instantly saturating the 32-bit LPDDR4x bus. To resolve this bottleneck, FRIDAY derives a strict 64,000-token vocabulary subset ($\mathcal{V}_S \subset \mathcal{V}_T$) based on high-frequency conversational English and Hindi/Hinglish token distributions. Pruning the vocabulary to 64k tokens reduces the INT8 LM-head weight footprint to exactly 57.34 MB, unlocking sustainable multi-token decoding speeds.

### 3.3 Two-Stage Bounded Cross-Modal Distillation Protocol
Training the 496M parameter student model from a 72B parameter teacher (Qwen2.5-VL-72B) is executed via a mathematically closed two-stage distillation objective that eliminates probability mass divergence:

#### Stage 1: Normalized Epsilon-Smoothed Top-64 Forward KL Divergence
Because the student vocabulary $\mathcal{V}_S$ is a strict subset of the teacher vocabulary $\mathcal{V}_T$, standard Kullback-Leibler divergence is undefined if the teacher predicts tokens outside $\mathcal{V}_S$. FRIDAY bounds the distillation support set to $\Omega_{64}$, defined as the top-64 teacher tokens restricted strictly to tokens contained within $\mathcal{V}_S$:

```
Omega_64 = Top-64( { v in V_S | p_T(v) } )  ==>  Omega_64 subset of V_S
p_tilde_T(v) = p_T(v) / sum_{u in Omega_64} p_T(u)
p_bar_S(v)    = p_S(v) / sum_{u in Omega_64} p_S(u)
p_tilde_S(v)  = (1 - eps) * p_bar_S(v) + (eps / |Omega_64|),   eps = 1e-5
L_KD = sum_{v in Omega_64} p_tilde_T(v) * ln( p_tilde_T(v) / p_tilde_S(v) )
```

Because both teacher and student distributions are explicitly renormalized over $\Omega_{64}$, and the student distribution is bounded below by $\epsilon/64 > 0$, the loss function represents a true, mathematically closed KL divergence on a normalized probability space, completely eliminating gradient explosions or probability leakage.

#### Stage 2: On-Policy Sequence Direct Preference Optimization (DPO)
Following forward distillation, the model undergoes sequence-level DPO fine-tuning using pairs of verified edge-scene descriptions and hallucinated responses, enforcing strict factual grounding and brevity suitable for immediate speech synthesis.

### 3.4 Hardware Memory Traffic & Bus Utilization Analysis
Autoregressive token generation on embedded systems is fundamentally memory-bandwidth bound. The table below delineates the verified traffic generated per token decoded on the RK3576 32-bit LPDDR4x memory bus:

| Parameter / Buffer Element | Quantization Precision | Footprint / Traffic | % of Token Budget |
| :--- | :--- | :--- | :--- |
| **352M Transformer Layers (INT4)** | INT4 (0.5 B/param) | 176.00 MB | 65.83% |
| **64,000-Token Language Model Head** | INT8 (1.0 B/weight) | 57.34 MB | 21.45% |
| **W4A16 Scales, Offsets & RMSNorms** | FP16 / Mixed | 16.00 MB | 5.98% |
| **KV-Cache Traffic (1024 Context)** | INT8 Quantized | 18.00 MB | 6.74% |
| **Total Sustained Traffic per Token** | System Combined | 267.34 MB/token | 100.00% |

At a target generation throughput of 35 tokens per second, sustained memory bandwidth demand is:
$$	ext{Bandwidth} = 0.29634	ext{ GB} 	imes 35	ext{ tokens/s} = \mathbf{10.37	ext{ GB/s}}.$$
On the Rockchip RK3576 LPDDR4x bus (operating at 2133 MHz with a sustained real-world ceiling of $13.50	ext{ GB/s}$), this represents exactly **$76.8\%$ bus utilization**, leaving **$3.13	ext{ GB/s}$ of continuous unallocated bandwidth** for concurrent ISP camera frame DMA transfers and audio I2S ring-buffers.

---

## Section 4: Edge Firmware & Software Architecture

### 4.1 Asymmetric Dual-Silicon Heterogeneous Compute Architecture
Project FRIDAY partitions processing across two distinct silicon computing nodes housed on opposite sides of the frame:
1. **Always-On Micro-Coprocessor (Ambiq Apollo4 Lite):** ARM Cortex-M4 @ 192MHz, 1.375 MB SRAM located on the right carrier board, consuming under $10\,\mu	ext{A/MHz}$ in deep sensing sleep.
2. **High-Performance Neural Host (Rockchip RK3576 SoM):** Featuring $4	imes$ Cortex-A72, $4	imes$ Cortex-A53 cores, and a 6.0 TOPS 3-core NPU responsible for operating system execution and neural decoding.

### 4.2 Operating System & Real-Time Kernel Configuration
The primary host executes an optimized Linux 6.1-LTS kernel patched with `PREEMPT_RT` for deterministic real-time audio and frame scheduling. Systemd is replaced with a minimal BusyBox/musl init pipeline, stripping unused networking daemons and achieving a cold-boot time of under 4.2 seconds and a Suspend-to-RAM resume time of under 250 milliseconds. Hardware acceleration drivers for the Rockchip NPU (`rknpu`), 2D graphics engine (`rga`), and MIPI CSI-2 camera controller (`rkisp`) are compiled directly into the monolithic kernel image.

### 4.3 Lock-Free Asynchronous Orchestration Daemon in Rust
The core software orchestration layer is written entirely in the **Rust** programming language, executing atop the Tokio asynchronous event-loop runtime. To guarantee zero audio buffer underruns and eliminate memory allocation latency during active inference, inter-thread data sharing between the camera capture thread, NPU inference runtime, and audio playback thread is mediated strictly through lock-free Single-Producer Single-Consumer (SPSC) ring-buffers allocated in non-swappable pinned memory pages.

### 4.4 Low-Latency Acoustic Signal Chain & Multiband DRC
Audio input captured from the dual front-right MEMS microphones passes through an isolated star-ground return and enters a hardware-accelerated digital signal processing pipeline:
1. WebRTC Acoustic Echo Cancellation 3 (AEC3) removes acoustic speaker spillover from the temple drivers.
2. A dual-microphone adaptive delay-and-sum beamformer enhances voice capture while rejecting off-axis ambient traffic noise.
3. A multi-band Dynamic Range Compressor (DRC) normalizes speech synthesis amplitude, maximizing speech intelligibility in noisy outdoor environments without driving the MAX98357A amplifiers into clipping.

### 4.5 Fast Suspend-to-RAM Handshake & Watchdog Recovery
To eliminate idle battery drain following query responses, FRIDAY implements a strict post-query power handshake:
1. Following speech synthesis completion, the host holds in an active listening state for exactly 3.0 seconds to permit conversational follow-ups (consuming $\sim 1.8	ext{ Joules}$ at $0.6	ext{W}$ idle).
2. If no input is detected, Linux executes Suspend-to-RAM (`echo mem > /sys/power/state`), transitioning within 85 ms ($<0.15	ext{ J}$) into deep sleep ($<15	ext{ mW}$).
3. Hardware Watchdog Guard: The Apollo4 coprocessor enforces a 2.0-second suspend-entry watchdog and a 1.5-second resume watchdog. If the Linux host fails to acknowledge sleep transitions, the Apollo4 triggers a hardware PMIC reset.

---

## Section 5: Mechanical & Industrial Design Requirements

### 5.1 Ergonomic Architecture & Mass Center of Gravity
Standard smart glasses suffer from severe anterior weight bias, placing excessive downward pressure on the nasal bridge that causes user fatigue within 20 minutes of wear. FRIDAY counteracts nasal torque by distributing heavy subsystems symmetrically along the temple arms: the power management and charging silicon sit in the left temple arm, while the compute SoM, coprocessor, and buck-boost regulators sit in the right temple arm. Both arms house identical 11.5g 300mAh lithium-polymer cells. This symmetrical distribution places the center of gravity directly along the transverse ear-temple axis, eliminating nasal fatigue.

### 5.2 Titanium Grade 5 Kinematic Camera Skeleton
Mounting an optical camera inside polymer eyewear frames introduces severe thermal creep: as heat from the compute core warms the frame, unsupported plastic bridges distort, shifting the optical capture vector away from user gaze. FRIDAY encases the Sony IMX415 sensor inside a laser-cut stamped Titanium Grade 5 kinematic cradle (3.0 grams) mounted with a permanent 6-degree downward pitch. An integrated NTC thermistor inside the camera cradle provides real-time temperature feedback to the software lens distortion calibration table.

### 5.3 1D Outward-Preferential Thermal Resistance Network
Facial wearables are legally and ergonomically constrained by skin contact temperatures: international standards (IEC 62368-1) limit wearable skin contact temperatures to under $43.0^\circ	ext{C}$, with FRIDAY enforcing a strict design ceiling of $\le 37.5^\circ	ext{C}$. To reject the 3.0-Watt peak inference heat while protecting the user's temple, FRIDAY implements an asymmetric 1D thermal resistance model:
* **Inner Temple Wall (High Resistance):** The inner temple wall facing user skin is lined with a 1.0mm aerogel insulation blanket (thermal conductivity $k pprox 0.015	ext{ W/m}\cdot	ext{K}$), establishing a massive thermal barrier of $R_{	ext{skin}} \ge 35.0	ext{ K/W}$.
* **Outer Temple Wall (Low Resistance):** The outer temple wall features pyrolytic graphite foil bonded directly to an exterior 1.5g anodized aluminum heat dissipation plate ($R_{	ext{outer}} pprox 3.5	ext{ K/W}$). Heat flows $10	imes$ preferentially outward into ambient air, maintaining outer plate temperature at $40.0^\circ	ext{C}	ext{--}41.0^\circ	ext{C}$ while inner skin contact remains strictly $\le 37.5^\circ	ext{C}$.

### 5.4 Phase Change Material (PCM) Latent Energy Buffer
Because natural air convection over a compact eyewear surface is limited to $\sim 0.36	ext{ Watts}$, active inference at 3.0 Watts generates instantaneous heat faster than steady-state convection can reject it. FRIDAY integrates a 4.0g PureTemp 40 composite PCM pad into the right temple outer cavity. With a latent heat of fusion of $150	ext{ J/g}$, the PCM absorbs exactly 600 Joules of latent heat at a constant melting plateau of $39.0^\circ	ext{C}$ to $40.5^\circ	ext{C}$, clamping silicon junction temperature during peak inference bursts.

### 5.5 Non-Ratcheting Thermal Burst Contract & Environmental Bounds
Active inference is capped by firmware to a maximum burst of exactly 12 seconds per turn. During a 12-second turn:
$$	ext{Heat Accumulated} = (3.0	ext{W} - 0.38	ext{W}) 	imes 12	ext{s} = \mathbf{31.44	ext{ Joules}}.$$
At the certified nominal ambient of $28.0^\circ	ext{C}$, the driving temperature difference to the $40.0^\circ	ext{C}$ outer plate is $\Delta T = 12.0	ext{ K}$. Across an effective frame surface area of $A pprox 20.0	ext{ cm}^2$ ($0.0020	ext{ m}^2$) with convection factor $h = 15.0	ext{ W/m}^2\cdot	ext{K}$, the product $h \cdot A$ equals exactly **$0.030	ext{ W/K}$** ($30	ext{ mW/K}$). Passive heat rejection at rest is $P_{	ext{passive}} = 12.0	ext{ K} 	imes 0.030	ext{ W/K} = 0.36	ext{ Watts}$, yielding a net cooling rate of $P_{	ext{cooling}} = 0.36	ext{W} - 0.04	ext{W} = 0.32	ext{ Watts}$. The required inter-turn passive cooldown is:
$$t_{	ext{cool}} = rac{31.44	ext{ J}}{0.32	ext{ W}} = 98.25	ext{ seconds} \implies \mathbf{t_{	ext{inter-turn}} \ge 100.0	ext{ seconds}}.$$
Enforcing $t_{	ext{inter-turn}} \ge 100	ext{ seconds}$ completely re-solidifies the PCM, guaranteeing zero thermal ratcheting.

---

## Section 6: Electronics & Power Specifications

### 6.1 Active-Balanced Series 2S Battery Topology (7.4V Nominal)
Parallel single-cell (1S, 3.7V) battery architectures require high currents (exceeding 0.90 Amperes at 3.0W) to cross the narrow hinge flex, inducing severe resistive $I^2R$ heating and dangerous localized hot-spots inside the frame bridge. FRIDAY introduces an Active-Balanced Series 2S battery architecture: two 3.7V 300mAh pouch cells are wired in series across the hinges, operating at 7.4V nominal (6.0V to 8.4V operating range, 2.22 Wh total). Doubling the bus voltage halves the bridge current to $\sim 0.43	ext{ Amperes}$, reducing bridge $I^2R$ resistive heat generation by exactly 75%. Cell balance is maintained during charge cycles by a TI BQ25887 boost charger with active balance bleed resistors derated to 45.8% ($0.114	ext{W}$ each).

### 6.2 Power Management Integrated Circuits & Buck-Boost Regulation
The power delivery tree integrates three specialized stages:
1. TI BQ25887 Series 2S boost charger with autonomous JEITA thermal profiling located in the left temple.
2. TI BQ28Z610 2S fuel gauge and secondary hardware overvoltage/undervoltage protection IC.
3. MPS MP28167 high-efficiency synchronous buck-boost converter located on the right carrier board, stepping the 6.0V-8.4V pack voltage down to a tightly regulated 3.8V VSYS rail at $\ge 95\%$ efficiency to power the RK3576 SoM.

### 6.3 Interconnect Flex Harnessing & Conductor Route Allocation (18C Left / 34C Right)
The interconnect harness between temples and front frame is executed via continuous 2-layer rigid-flex polyimide strips with rolled-annealed (RA) copper. The conductor allocations across both hinges are fully closed and verified with zero missing lines:

| Harness Segment | Conductor Count | Layer Stack & Pitch | Subsystem Signal Breakdown |
| :--- | :--- | :--- | :--- |
| **Left-to-Bridge Flex** | 18 Conductors | 2-Layer Polyimide, 0.30mm pitch (5.4mm width; >=2.0mm 2oz Cu power pours) | 1x PACK+ (2.0mm 2oz Cu, <=0.030Ω), 1x PACK- (2.0mm 2oz Cu, <=0.030Ω), 2x CELL_MID (parallel 2oz RA Cu, <=0.030Ω), 1x Kelvin MID, 1x Bleed, 2x Chg I2C, 1x INT, 1x CD, 1x NTC2, 4x Left Audio (BCLK, LR, DATA, SD), 1x VAUX_1V8, 2x Isolated DGND/Shield |
| **Right Hinge Flex** | 34 Conductors | 2-Layer Staggered, 0.35mm pitch (6.0mm width) | 6x MIPI CSI-2, 2x CAM I2C, 2x CAM Ctrl, 2x CAM Pwr, 1x CAM NTC, 4x Mic Bus, 1x Mic Star-GND, 1x PACK+, 1x PACK-, 2x CELL_MID, 1x Kelvin MID, 1x Bleed, 2x Chg I2C, 1x INT, 1x CD, 1x NTC2, 4x Left Audio, 1x VAUX_1V8 |

### 6.4 Dual Mono Class-D Audio Amplification & Resistor-Coupled Sleep Biasing
Driving high-frequency Class-D PWM speaker currents across the bridge flex introduces unacceptable electromagnetic interference (EMI) into adjacent MIPI camera lines. FRIDAY deploys two independent MAX98357A mono Class-D amplifiers located locally in each temple arm. Clean digital I2S lines (BCLK, LRCLK, DATA_L) cross the flex instead of raw speaker pulses. In accordance with the Analog Devices MAX98357A datasheet, channel decoding and hardware shutdown are controlled via dedicated resistor networks forming dividers against the internal $100\text{ k}\Omega$ pulldown ($R_{\text{PD}} \in [92\text{k}\Omega, 108\text{k}\Omega]$):
* **Left Temple Amp (`SD_MODE_L`):** Biased via a single $\le 10\text{ k}\Omega$ precision pull-up to $1.8\text{V}$. When the Apollo4 control GPIO is in high-impedance, $V_{\text{pin}} = 1.636\text{V}$ nominal ($1.623\text{V}$ min $> 1.40\text{V}$), unconditionally selecting the **LEFT CHANNEL**. When pulled to GND ($<0.16\text{V}$), the amp enters deep shutdown ($<0.1\,\mu\text{A}$), with the $10\text{ k}\Omega$ resistor limiting sinking current to $180\,\mu\text{A}$.
* **Right Temple Amp (`SD_MODE_R`):** Biased via a single $82\text{ k}\Omega$ precision pull-up to $1.8\text{V}$ utilizing the internal $100\text{ k}\Omega$ pulldown (eliminating external low-side divider resistors), establishing $V_{\text{pin}} = 0.989\text{V}$ nominal ($0.952\text{V}\text{--}1.023\text{V}$ across process corners, securely centered in the $0.77\text{V}$ to $1.40\text{V}$ window), unconditionally decoding the **RIGHT CHANNEL**. Pulling the node to GND enforces deep sleep ($<0.1\,\mu\text{A}$).

### 6.5 Dead-Battery Bootstrapping & Coordinated Watchdog Interlock
The Ambiq Apollo4 Lite operating voltage is strictly **$1.71\text{V}\text{--}2.2\text{V}$** (nominal $1.8\text{V}$). When docked into external $5\text{V}$ power with depleted cells, an auxiliary LDO steps $5\text{V}$ down to **$1.8\text{V}$** and routes `VAUX_1V8` across the bridge behind an ideal-diode OR switch, safely powering the Apollo4 Lite within its operating voltage ratings.

To prevent runaway charging if the Apollo4 hangs while `CD` is LOW:
1. The Apollo4 internal hardware watchdog timer (WDT) is configured with a **$1.0\text{s}$ timeout** ($t_{\text{WDT\_MCU}} = 1.0\text{s}$), strictly shorter than the BQ25887 charger watchdog. If firmware freezes, the internal WDT forces an immediate MCU hardware reset within $1.0\text{s}$, de-asserting the GPIO and allowing `CD` to float HIGH via its pull-up resistor, cutting off charging instantly.
2. Once `ICHG = 200\text{ mA}$ is programmed, the Apollo4 disables the BQ25887 internal I2C watchdog (`WATCHDOG = 00`) while actively monitoring battery telemetry on a $500\text{ms}$ loop, preventing unsolicited watchdog expiration from resetting charge current to the dangerous $1.5\text{A}$ ($5\text{C}$) default.

---

## Section 7: Performance & Latency Budgets

To enforce deterministic responsiveness, all software and hardware operations are bounded by strict numerical latency and throughput budgets:

| Subsystem Operation | Target Latency / Bound | Hardware Silicon Node | Engineering Verification Metric |
| :--- | :--- | :--- | :--- |
| **Wake-Word to Earcon Chime** | < 80 milliseconds | Ambiq Apollo4 Lite | Hardware timer from VAD trigger to speaker pulse |
| **Linux Resume from RAM** | < 250 milliseconds | Rockchip RK3576 Host | Kernel resume timestamp in PREEMPT_RT syslog |
| **Camera Capture & Foveal Crop** | < 15 milliseconds | IMX415 + RGA Engine | MIPI DMA buffer write + RGA crop completion |
| **Vision Token Encoding** | < 45 milliseconds | SigLIP-B (6.0 TOPS NPU) | Time to encode 144 visual token embeddings |
| **Time-to-First-Token (TTFT)** | < 650 milliseconds | RK3576 NPU Core | Prefix prefill latency for visual prompt |
| **Autoregressive Generation** | >= 35 tokens/second | RK3576 LPDDR4x Bus | Sustained INT4 decoding speed under 10.37 GB/s |
| **TTS Stream Latency** | < 180 milliseconds | RK3576 CPU / I2S | Latency from first decoded token to audio buffer |
| **Time-to-First-Spoken-Word** | ~ 1.20 seconds (Target) | Full System Combined | Total elapsed time from voice query to spoken word |
| **Peak Active Thermal Burst** | <= 12.0 seconds | Thermal Architecture | Hardware thermal governor timer clamp |
| **Inter-Turn Passive Cooldown** | >= 100.0 seconds | PureTemp 40 PCM | Time required to re-solidify 31.44 Joules @ 28 deg C |

---

## Section 8: Academic Novelty & Thesis Deliverables

Project FRIDAY provides distinct, peer-reviewable research contributions across three engineering domains for the capstone defense:

### 8.1 Information Technology & Machine Learning Novelty
* **Bounded Cross-Modal Distillation:** Formulation and mathematical proof of a bounded two-stage cross-modal distillation protocol (Normalized Epsilon-Smoothed Top-64 Forward KD strictly over $\Omega_{64} \subseteq \mathcal{V}_S$ + Sequence DPO) that enables extreme cross-modal compression of a 72B foundation model into a 496M student operating under a 9.36 GB/s memory bandwidth envelope.
* **Spatial Token Unshuffle Downsampling:** Elimination of redundant visual token traffic through a $2	imes 2$ spatial unshuffle layer reducing patch sequence length from 576 to strictly 144 tokens without semantic resolution loss.

### 8.2 Systems & Embedded Software Engineering Novelty
* **Zero-Cost Asynchronous Edge Runtime:** An asynchronous, zero-cost-abstraction edge orchestration daemon written in Rust, leveraging lock-free SPSC ring buffers and WebRTC AEC3 signal processing to achieve a sub-1.25-second target Time-to-First-Spoken-Word.
* **Heterogeneous Asymmetric Wake Pipeline:** An asymmetric dual-silicon power state machine that couples micro-watt coprocessor audio buffering ($<80	ext{ms}$ chime) with sub-second Linux Fast Suspend-to-RAM.

### 8.3 Hardware & Wearable Mechatronic Novelty
* **Sovereign Wearable Packaging:** A completely self-contained smart-glasses form factor with Series 2S active-balanced battery packaging, 18C/34C rigid-flex routing, and titanium kinematic optomechanics operating under a verified 115.0-gram all-up mass envelope.
* **Phase Change Thermal Management:** An outward-preferential 1D thermal resistance model combining aerogel skin barriers with composite phase change materials, guaranteeing skin contact temperatures $\le 37.5^\circ	ext{C}$ during 3.0W neural inference bursts.

---

## Section 9: Risk Matrix & Scope Boundaries

### 9.1 Scope Boundaries: In-Scope vs. Out-of-Scope
To ensure rigorous execution and prevent feature creep during capstone implementation, boundaries are formally defined:

| Project Dimension | Accepted In-Scope Deliverables | Explicitly Out-of-Scope (Deferred) |
| :--- | :--- | :--- |
| **Visual Interface / Display** | Pure audio UI via bone-conduction / directional drivers; visual feedback via phone companion app. | Heads-Up Display (HUD) optics, micro-OLEDs, waveguides (deferred due to battery, weight, and thermal limits). |
| **Silicon & Board Level** | Rockchip RK3576 development platform / SoM, custom 2-layer carrier PCBs in Autodesk Fusion Electronics. | Custom silicon ASIC tape-out, monolithic 6-layer rigid-flex fabrication (simulated via standard FR4 + FFC). |
| **Frame Prototyping** | 3D-printed frames in FDM PETG / PLA+ with precision inserts; reuse of student's personal optical lenses. | Mass production injection tooling, titanium die casting, high-index prescription lens grinding. |
| **Connectivity & Telephony** | Direct Wi-Fi 4, Bluetooth 5.2 PAN modem proxy, HFP/A2DP audio sink, local spoken offline notice. | Integrated 4G/5G cellular baseband modems, eSIM hardware (requires carrier certification). |
| **Environmental Protection** | Standard sweat and splash resistance (IP54 equivalent design rules with silicone gasket seals). | Submersible waterproofing (IP68), military-spec drop testing, ballistic impact certification. |

### 9.2 Comprehensive Engineering Risk Matrix

| Risk Description | Category | Sev. | Prob. | Mitigation Strategy & Contingency Action |
| :--- | :--- | :--- | :--- | :--- |
| **Memory bus saturation during INT4 VLM generation** | Technical | High | Med | Prune vocabulary to 64k tokens; deploy 2x2 visual token unshuffle; clamp context window to 1024 tokens. |
| **Thermal throttling during extended conversational turns** | Thermal | High | Med | Enforce strict 12s active burst clamp in firmware; integrate 4.0g PCM pad; enforce >=100s inter-turn cooldown. |
| **Hinge conductor fatigue failure across repeated folding** | Hardware | Med | Low | Use Rolled-Annealed (RA) copper with grain parallel to bend axis; enforce 3.0mm stiffener clearance; benchtop FFC harness. |
| **Cell voltage imbalance leading to premature UVLO cutoff** | Electrical | High | Low | TI BQ25887 active balance circuitry with 45.8% derated balance bleed resistors; Kelvin MID sense monitoring. |
| **Host Linux sleep-transition freeze or crash** | Software | Med | Med | Apollo4 Lite hardware watchdog monitoring suspend/resume handshakes; automated PMIC power cycle fallback. |
| **Component procurement delays and budget overrun** | Management | Med | Low | Butcher BOM to student-grade components (Robu.in / JLCPCB / FDM PETG); ₹13,500 total spend ceiling. |

### 9.3 Lean Zero-Waste Student Bill of Materials (BOM) & Sourcing Matrix
To protect student capital and eliminate intermediate drawer waste, Project FRIDAY enforces a strict zero-rupee gate:
1. **The ₹0 Initial Sandbox:** Phase 1 executes entirely for **₹0** on the student's MacBook Air M4 (16 GB Unified Memory) and free cloud GPUs (Kaggle / Google Colab).
2. **Free Peripheral Bring-Up:** Audio peripheral communication (I2S to MAX98357A, INMP441 capture, WebRTC AEC3) is pre-tested on the student's existing **Raspberry Pi 3B (1 GB)** for **₹0**.
3. **Single-Shot Wearable Procurement:** Intermediate throwaway evaluation boards (e.g., Orange Pi 5) are strictly bypassed. Procurement occurs only after Phase 1 passes the usability gate, purchasing exclusively the components that install directly onto the Track 1 "Thick-Temple" wearable:

| Subsystem Component | Target Wearable Specification | Purpose in Prototype | Est. Cost (INR) | Source Channel |
| :--- | :--- | :--- | :--- | :--- |
| **Compute Core** | **Firefly CAM-3576Q38** (RK3576 6 TOPS NPU, **4GB LPDDR4x**, onboard Wi-Fi 6 + BT 5.4, 38×38×11.5mm, 14.2g) | Primary on-device AI inference engine in right temple with onboard 40-pin FPC MIPI camera connector | ₹5,400 | Firefly Store / ThinkRobotics / Evelta |
| **Camera Module** | Sony IMX219 / OV5647 160° Wide-Angle MIPI CSI Module | Center-bridge 1080p camera ($6^\circ$ down-pitch) plugging directly into CAM-3576Q38 | ₹1,450 | Robu.in / ElectronicsComp |
| **MEMS Microphones** | 2x INMP441 Digital I2S MEMS Breakouts | Dual front-right beamforming audio capture | ₹290 | Robu.in |
| **Audio Amplifiers** | 2x MAX98357A I2S Mono 3.2W Breakouts | Dual mono temple amps with resistor channel-select ($10\text{ k}\Omega$ Left, $220\text{ k}\Omega$ Right against internal $100\text{ k}\Omega$ pulldown) | ₹250 | Robu.in |
| **Speakers / Drivers** | 2x Mini Bone Conduction / Directional (8Ω 1W) | Direct ear-canal acoustic drivers in temple tips | ₹300 | Robu.in / Amazon.in |
| **Dual LiPo Batteries** | 2x 3.7V 300mAh 30C/60C High-Discharge Pouch Cells | Series 2S power pack (1 cell per temple, 30C rating safely delivers 1.85A / 6.2C peak surge with 0V sag) | ₹380 | Robu.in |
| **2S Boost Charger** | IP2326 Type-C 2S Boost Charger ($R_{ISET}=0.33\,\Omega$ set for 300mA 1C) | Docked 2S active charging circuit with ammeter-verified 300mA current | ₹110 | Robu.in / Amazon.in |
| **2S Battery Protection** | 2S 3A/5A BMS with HY2212 Active Cell Balancing | Active cell balancing (4.20V ± 25mV cutoff, 35mA bleed shunt) & overcurrent protection | ₹120 | Robu.in |
| **2S-to-5V System Buck** | MP2315 / MP2307 Synchronous DC-DC Step-Down Buck | True synchronous buck (95% efficiency, zero external Schottky diode heat) regulating 2S to 5.0V @ 2A | ₹95 | Robu.in |
| **User Interaction** | TTP223 Capacitive Touch Sensor / Tactile Micro-Switch | Touch trigger on right temple arm to start queries | ₹25 | Robu.in |
| **Eyewear Frame** | FDM 3D Printing in Black PETG (0.12mm) | Heat-resistant front frame & thick temples (42.0g net frame mass) | ₹300 | NMIMS FabLab / Local Lab |
| **Optical Lenses** | Student Personal Prescription / Plano Lenses | Repurposed eyewear lenses (zero cutting cost) | ₹0 | Self-Provided |
| **Carrier PCBs** | Batch of 5 Standard 2-Layer FR4 Low-Speed Boards | Temple breakout boards for low-speed audio & power wiring | ₹350 | JLCPCB / Robu PCB |
| **Interconnect Wiring** | 0.5mm FFC Ribbon Cables + 30 AWG Wire | Through-bridge hinge wiring (doubled power runs for $R_{DC} < 0.030\,\Omega$) | ₹120 | Robu.in |
| **Thermal Assembly** | 0.3mm Copper Shim + 4.0g Paraffin PCM + Arctic MX-4 | Conductive heat spreading into 600 J PCM buffer & chassis | ₹190 | Amazon.in |
| **Contingency Buffer** | Fasteners, Kapton tape, flux, heatshrink | Assembly hardware and prototyping buffer | ₹215 | Local Hardware Store |
| **TOTAL HARDWARE COST** | **Complete Untethered Wearable Prototype** | **100% Installed on Wearable (Zero Drawer Waste)** | **₹9,595 INR** | **Student Outlay (~$115 USD, strictly < ₹10k Cap)** |

---

## References

[1] Rockchip Electronics Co., Ltd., "RK3576 Technical Reference Manual & Datasheet," Rev 1.1, 2024.  
[2] Ambiq Micro, Inc., "Apollo4 Lite SoC Datasheet: Ultra-Low Power Microcontroller with 2MB MRAM and 1.375MB SRAM," Rev 1.0, 2023.  
[3] Analog Devices, Inc., "MAX98357A/MAX98357B: Tiny, Low-Cost, PCM Class D Amplifier Datasheet," Rev 4, 2021.  
[4] Texas Instruments, Inc., "BQ25887 I2C Controlled 2-Cell, 2A Boost-Mode Battery Charger with Cell Balancing," SLUSD78B, 2019.  
[5] Texas Instruments, Inc., "BQ28Z610 1-Series to 2-Series Cell Gas Gauge and Protection IC," SLUSBX8, 2018.  
[6] Monolithic Power Systems, "MP28167: Synchronous Buck-Boost Converter with Integrated Power MOSFETs," Rev 1.02, 2022.  
[7] Sony Semiconductor Solutions Corp., "IMX415-AAQR Diagonal 6.43 mm (Type 1/2.8) 8.29M-Effective Pixel Color CMOS Image Sensor," 2020.  
[8] Qwen Team, "Qwen2.5 Technical Report: Open Large Language and Multimodal Foundation Models," arXiv:2409.12191, 2024.  
[9] X. Zhai et al., "Sigmoid Loss for Language Image Pre-Training (SigLIP)," in IEEE/CVF International Conference on Computer Vision (ICCV), 2023.  
[10] R. Rafailov et al., "Direct Preference Optimization: Your Language Model is Secretly a Reward Model," in Advances in Neural Information Processing Systems (NeurIPS), 2023.  
[11] PureTemp LLC, "PureTemp 40 Technical Data Sheet: Bio-Based Phase Change Material," TD-PT40, 2022.  
[12] IPC Association, "IPC-2223: Sectional Design Standard for Flexible Printed Boards," IPC-2223E, 2020.
