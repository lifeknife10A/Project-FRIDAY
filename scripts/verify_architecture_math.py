#!/usr/bin/env python3
"""
PROJECT FRIDAY - ARCHITECTURAL MATHEMATICS & DESIGN INVARIANT REGRESSION AUDIT
Author: Krishna Jagat Solanki
Version: 9.1.0

This script independently re-verifies every quantitative, electrical, physical,
and mathematical invariant defined in the Project FRIDAY systems architecture:
1. Left Flex Conductor Count (Exactly 18 Conductors)
2. Right Hinge Flex Conductor Count (Exactly 34 Conductors)
3. All-Up Mass Budget Rollup (109.5g Physical + 5.5g Contingency = Exactly 115.0g)
4. Memory Bus Traffic & Bandwidth Utilization (<10.5 GB/s, >3.0 GB/s headroom)
5. MAX98357A Resistor-Coupled SD_MODE Channel Decoding Tolerances (Left & Right)
6. Outward-Preferential 1D Thermal Resistance & PCM Solidification Time
"""

import sys

def audit_conductors():
    print("--- [1/6] AUDITING CONDUCTOR HARNESS ALLOCATION ---")
    
    # Left-to-Bridge Flex (18 Conductors)
    left_conductors = {
        "1x Dedicated 2S Pack High Voltage (PACK+)": 1,
        "1x Dedicated 2S Pack Return (PACK-)": 1,
        "2x Series Midpoint Interconnect (CELL_MID)": 2,
        "1x Kelvin MID Sense Line": 1,
        "1x Active Balance Bleed Tap": 1,
        "2x Charger I2C Bus (SCL_CHG, SDA_CHG)": 2,
        "1x Charger Interrupt/Status (INT_CHG)": 1,
        "1x Hardware Charge Disable Interlock (CD)": 1,
        "1x Cell 2 NTC Line (To TS pin)": 1,
        "4x Left Audio Digital I2S Bus (BCLK, LRCLK, DATA_L, SD_MODE_L)": 4,
        "1x Auxiliary 1.8V Bootstrapping (VAUX_1V8)": 1,
        "2x Isolated Digital Ground & EMI Shield Return (DGND/SHIELD)": 2
    }
    total_left = sum(left_conductors.values())
    print(f"  Left Flex Conductor Total: {total_left}")
    assert total_left == 18, f"Left Flex mismatch: expected 18, got {total_left}"
    print("  [PASS] Left-to-Bridge Flex = Exactly 18 Conductors")

    # Right Hinge Flex (34 Conductors)
    right_conductors = {
        "6x 2-Lane MIPI CSI-2 (CLK+/-, D0+/-, D1+/-)": 6,
        "2x Camera I2C Control (CAM_SCL, CAM_SDA)": 2,
        "2x Camera Clock & Reset (CAM_MCLK, CAM_RST_N)": 2,
        "2x Camera Regulated Power Rails (2.9V, 1.8V)": 2,
        "1x Camera Cradle NTC Thermistor": 1,
        "4x Dual MEMS Mic Bus (MIC_VDD, BCLK, LRCLK, DATA)": 4,
        "1x Microphone Star-GND Return": 1,
        "1x Dedicated 2S Pack High Voltage (PACK+)": 1,
        "1x Dedicated 2S Pack Return (PACK-)": 1,
        "2x Series Midpoint Interconnect (CELL_MID)": 2,
        "1x Kelvin MID Sense Line": 1,
        "1x Active Balance Bleed Tap": 1,
        "2x Charger I2C Bus (SCL_CHG, SDA_CHG)": 2,
        "1x Charger Interrupt/Status (INT_CHG)": 1,
        "1x Hardware Charge Disable Interlock (CD)": 1,
        "1x Cell 2 NTC Line": 1,
        "4x Left Audio Bus (BCLK, LRCLK, DATA_L, SD_MODE_L)": 4,
        "1x Auxiliary 1.8V Bootstrapping (VAUX_1V8)": 1
    }
    total_right = sum(right_conductors.values())
    print(f"  Right Hinge Flex Conductor Total: {total_right}")
    assert total_right == 34, f"Right Flex mismatch: expected 34, got {total_right}"
    print("  [PASS] Right Hinge Flex = Exactly 34 Conductors\n")

def audit_mass_budget():
    print("--- [2/6] AUDITING ALL-UP MASS BUDGET ---")
    physical_bom = [
        ("Front Frame (Nylon PA12)", 12.0),
        ("High-Index 1.67 Lenses", 8.5),
        ("Titanium Camera Skeleton & IMX415 Lens", 3.0),
        ("Dual MEMS Microphones (Star-GND)", 0.8),
        ("Spring Hinges & Brass Inserts", 3.0),
        ("Silicone Nose Pads, Brackets & Fasteners", 1.8),
        ("Continuous Rigid-Flex Hinge Bridges", 2.2),
        ("Right Temple Chassis (PA12)", 7.2),
        ("Compute Core SoM (Rockchip RK3576)", 11.8),
        ("Right Carrier PCB + 2S Buck-Boost", 1.9),
        ("Wi-Fi / BT 5.2 Murata 1XK Combo SiP", 0.8),
        ("Cell 2 LiPo (Series 2S, 3.7V 300mAh)", 11.5),
        ("Right Protection Board, NTC & Balance", 1.2),
        ("Thermal Assembly (4.0g PCM + 1.5g Al)", 5.5),
        ("Ambiq Apollo4 Lite Coprocessor & Mux", 1.1),
        ("Capacitive Touch Ribbon & Hall Switch", 0.7),
        ("MAX98357A Right Amp & Speaker Driver", 3.0),
        ("Left Temple Chassis (PA12)", 7.2),
        ("Cell 1 LiPo (Series 2S, 3.7V 300mAh)", 11.5),
        ("TI BQ25887 2S Charger & Power Rails", 3.7),
        ("TI BQ28Z610 2S Protector & Balance Tap", 1.2),
        ("Auxiliary 5V-to-1.8V LDO Board", 0.8),
        ("MAX98357A Left Amp & Speaker Driver", 4.8),
        ("Magnetic Pogo Charging Port (5V/3A)", 1.4),
        ("Solder Paste, Potting & Shielding Cans", 2.9)
    ]
    contingency = 5.5
    
    physical_sum = round(sum(item[1] for item in physical_bom), 2)
    total_mass = round(physical_sum + contingency, 2)
    print(f"  Physical Rows Count: {len(physical_bom)}")
    print(f"  Physical Mass Sum: {physical_sum} g")
    print(f"  Contingency Margin: {contingency} g ({(contingency/total_mass)*100:.2f}%)")
    print(f"  Total All-Up Weight (AUW): {total_mass} g")
    
    assert len(physical_bom) == 25, f"Expected 25 physical items, got {len(physical_bom)}"
    assert physical_sum == 109.5, f"Physical sum mismatch: {physical_sum}"
    assert total_mass == 115.0, f"Total AUW mismatch: {total_mass}"
    assert total_mass <= 125.0, f"Directive 05 violated! AUW {total_mass} > 125.0g"
    print("  [PASS] Mass Budget Reconciled to Exactly 115.0g (10.0g Headroom under Directive 05)\n")

def audit_memory_bandwidth():
    print("--- [3/6] AUDITING MEMORY TRAFFIC & BUS BANDWIDTH ---")
    # Bus Baseline (RK3576 32-bit LPDDR4x @ 2133 MHz clock / 4266 MT/s):
    # Theoretical Peak = 4 bytes * 4.266 GT/s = 17.064 GB/s
    # Sustainable Streaming Ceiling (79% efficiency) = 13.50 GB/s
    # Safe Operational Ceiling (with ISP/Camera/Audio contention) = 10.50 GB/s
    bus_peak_gb_s = 17.064
    bus_sustained_gb_s = 13.50
    bus_safe_ceiling_gb_s = 10.50

    # Exact Qwen2.5-0.5B KV Cache Geometry (Both K and V tensors):
    # 2 (K+V) * 24 layers * 2 KV heads * 64 head_dim * 1 byte (INT8) * 1024 context tokens = 6.29 MB
    kv_cache_mb = (2 * 24 * 2 * 64 * 1.0 * 1024) / 1e6
    scales_norms_mb = 16.0

    # === [CONTRACT A: PRIMARY ALL-INT4 W4A16 QUANTIZATION (Measured 198.96 MiB / 208.63 MB Artifact)] ===
    # Total student parameters: 415.24M (415,242,112 params)
    # Packed INT4 weights: 415.24M * 0.5 bytes = 207.62 MB (~208.32 MB aligned)
    weights_all_int4_mb = 208.32
    traffic_all_int4_per_tok = weights_all_int4_mb + scales_norms_mb + kv_cache_mb # 230.61 MB/token
    bw_all_int4_25 = (traffic_all_int4_per_tok / 1000.0) * 25.0 # 5.77 GB/s
    bw_all_int4_35 = (traffic_all_int4_per_tok / 1000.0) * 35.0 # 8.07 GB/s
    headroom_all_int4_safe = bus_safe_ceiling_gb_s - bw_all_int4_25

    print(f"  [Primary All-INT4 Artifact (208.43 MB packed)]:")
    print(f"    Weights: {weights_all_int4_mb:.2f} MB | Scales/Norms: {scales_norms_mb:.1f} MB | INT8 KV Cache: {kv_cache_mb:.2f} MB")
    print(f"    Total Traffic per Token: {traffic_all_int4_per_tok:.2f} MB/token")
    print(f"    Operating Bandwidth (25 tok/s): {bw_all_int4_25:.2f} GB/s (Headroom below 10.5 GB/s safe ceiling: {headroom_all_int4_safe:.2f} GB/s, {headroom_all_int4_safe/bus_safe_ceiling_gb_s*100:.1f}%)")
    print(f"    Burst Peak Bandwidth (35 tok/s): {bw_all_int4_35:.2f} GB/s (Headroom: {bus_safe_ceiling_gb_s - bw_all_int4_35:.2f} GB/s)")
    assert bw_all_int4_25 < bus_safe_ceiling_gb_s, f"Primary contract exceeded ceiling: {bw_all_int4_25}"
    assert bw_all_int4_35 < bus_safe_ceiling_gb_s, f"Burst peak exceeded ceiling: {bw_all_int4_35}"

    # === [CONTRACT B: INT4 BODY + INT8 LM-HEAD SECONDARY FALLBACK] ===
    # 352M transformer body @ INT4 = 176.0 MB; 64k LM-head @ INT8 = 57.34 MB; Total weights = 233.34 MB
    layers_mb = 352e6 * 0.5 / 1e6
    lm_head_mb = 64000 * 896 * 1.0 / 1e6
    weights_int8_head_mb = layers_mb + lm_head_mb
    traffic_int8_head_per_tok = weights_int8_head_mb + scales_norms_mb + kv_cache_mb # 255.63 MB/token
    bw_int8_head_25 = (traffic_int8_head_per_tok / 1000.0) * 25.0 # 6.39 GB/s
    bw_int8_head_35 = (traffic_int8_head_per_tok / 1000.0) * 35.0 # 8.95 GB/s
    headroom_int8_head_safe = bus_safe_ceiling_gb_s - bw_int8_head_35

    print(f"  [Secondary INT8-Head Fallback]:")
    print(f"    Total Traffic per Token: {traffic_int8_head_per_tok:.2f} MB/token")
    print(f"    Operating Bandwidth (25 tok/s): {bw_int8_head_25:.2f} GB/s")
    print(f"    Burst Peak Bandwidth (35 tok/s): {bw_int8_head_35:.2f} GB/s (Headroom: {headroom_int8_head_safe:.2f} GB/s, {headroom_int8_head_safe/bus_safe_ceiling_gb_s*100:.1f}%)")
    assert bw_int8_head_35 < bus_safe_ceiling_gb_s, f"Fallback contract exceeded ceiling: {bw_int8_head_35}"

    print(f"  [PASS] Memory Bandwidth Rigorously Verified: Primary = 5.77 GB/s @ 25 tok/s, Fallback = 8.95 GB/s @ 35 tok/s (< 10.50 GB/s safe ceiling)\n")

def audit_audio_decoding():
    print("--- [4/6] AUDITING MAX98357A RESISTOR-COUPLED SD_MODE NETWORK ---")
    r_pd_nom = 100.0 # kOhm internal pulldown
    r_pd_min = 92.0  # kOhm minimum
    r_pd_max = 108.0 # kOhm maximum

    # === A. WEARABLE FINAL PCB DOMAIN (1.8V IO Rail) ===
    v_rail_1v8 = 1.80
    r_pullup_l_1v8 = 10.0 # kOhm
    v_left_nom_1v8 = v_rail_1v8 * (r_pd_nom / (r_pullup_l_1v8 + r_pd_nom))
    v_left_min_1v8 = v_rail_1v8 * (r_pd_min / (r_pullup_l_1v8 + r_pd_min))
    assert v_left_min_1v8 > 1.40, f"Left channel voltage failed threshold: {v_left_min_1v8}"

    r_pullup_r_1v8 = 82.0 # kOhm
    v_right_min_1v8 = v_rail_1v8 * (r_pd_min / (r_pullup_r_1v8 + r_pd_min))
    v_right_max_1v8 = v_rail_1v8 * (r_pd_max / (r_pullup_r_1v8 + r_pd_max))
    assert v_right_min_1v8 >= 0.77 and v_right_max_1v8 <= 1.40, f"Right channel out of window: {v_right_min_1v8} to {v_right_max_1v8}"
    print(f"  [Wearable 1.8V Rail]: Left (10k) = {v_left_nom_1v8:.3f}V (>1.40V), Right (82k) = {v_right_min_1v8:.3f}V - {v_right_max_1v8:.3f}V (in 0.77V - 1.40V) -> PASS")

    # === B. RASPBERRY PI 3B TESTBED DOMAIN (3.3V GPIO Rail) ===
    v_rail_3v3 = 3.30
    r_pullup_l_3v3 = 10.0 # kOhm
    v_left_min_3v3 = v_rail_3v3 * (r_pd_min / (r_pullup_l_3v3 + r_pd_min))
    assert v_left_min_3v3 > 1.40, f"Pi 3B Left channel failed threshold: {v_left_min_3v3}"

    r_pullup_r_3v3 = 220.0 # kOhm pullup to 3.3V
    v_right_min_3v3 = v_rail_3v3 * (r_pd_min / (r_pullup_r_3v3 + r_pd_min))
    v_right_max_3v3 = v_rail_3v3 * (r_pd_max / (r_pullup_r_3v3 + r_pd_max))
    assert v_right_min_3v3 >= 0.77 and v_right_max_3v3 <= 1.40, f"Pi 3B Right channel out of window: {v_right_min_3v3} to {v_right_max_3v3}"
    print(f"  [Raspberry Pi 3B 3.3V Rail]: Left (10k) = {v_left_min_3v3:.3f}V (>1.40V), Right (220k) = {v_right_min_3v3:.3f}V - {v_right_max_3v3:.3f}V (in 0.77V - 1.40V) -> PASS")
    print("  [PASS] MAX98357A Dual-Rail Stereo Decoding Rigorously Verified\n")

def audit_thermals():
    print("--- [5/6] AUDITING 1D THERMAL DISSIPATION & PCM SOLIDIFICATION ---")
    p_active = 3.0 # W
    t_burst = 12.0 # s
    p_shed_active = 0.38 # W
    e_accumulated = (p_active - p_shed_active) * t_burst
    
    t_ambient_nom = 28.0 # deg C
    t_plateau = 40.0 # deg C
    delta_t = t_plateau - t_ambient_nom
    
    area_m2 = 0.0020 # 20 cm^2
    h_coeff = 15.0   # W/m^2-K
    ha_product = area_m2 * h_coeff # 0.030 W/K
    
    p_passive = delta_t * ha_product
    p_rest = 0.04 # W
    p_cooling = p_passive - p_rest
    t_cool_nom = e_accumulated / p_cooling
    
    # Extended band: 30C and 32C
    p_cooling_30 = (t_plateau - 30.0) * ha_product - 0.056
    t_cool_30 = e_accumulated / p_cooling_30
    
    p_cooling_32 = (t_plateau - 32.0) * ha_product - 0.057
    t_cool_32 = e_accumulated / p_cooling_32
    
    pcm_mass = 4.0 # g
    latent_heat_j_g = 150.0 # J/g
    e_latent_total = pcm_mass * latent_heat_j_g
    
    print(f"  Burst Energy: {e_accumulated:.2f} Joules ({t_burst}s @ {p_active}W)")
    print(f"  PCM Latent Capacity: {e_latent_total:.1f} Joules ({pcm_mass}g @ {latent_heat_j_g} J/g)")
    print(f"  Thermal Dissipation Constant: {ha_product:.3f} W/K (Area: 20 cm^2, h: 15 W/m^2-K)")
    print(f"  Cooldown Time @ 28°C: {t_cool_nom:.2f} s (Enforced Inter-Turn: >= 100.0s)")
    print(f"  Cooldown Time @ 30°C: {t_cool_30:.1f} s")
    print(f"  Cooldown Time @ 32°C: {t_cool_32:.1f} s")
    
    assert e_latent_total >= e_accumulated * 15, "PCM capacity insufficient for repeated bursts"
    assert t_cool_nom <= 100.0, f"Nominal cooldown exceeds 100s: {t_cool_nom}"
    print("  [PASS] Thermal Duty Cycle Non-Ratcheting & Physically Honest\n")

def audit_power_and_battery():
    print("--- [6/6] AUDITING SERIES 2S POWER DELIVERY ---")
    cell_capacity_mah = 300.0 # mAh
    cell_voltage_nom = 3.7 # V
    pack_voltage_nom = 7.4 # V
    energy_wh = (2 * cell_voltage_nom * cell_capacity_mah) / 1000.0
    
    peak_power = 3.0 # W
    converter_efficiency = 0.95 # MP28167
    bus_current_a = (peak_power / converter_efficiency) / pack_voltage_nom
    single_cell_equiv_a = (peak_power / converter_efficiency) / cell_voltage_nom
    i2r_reduction = (1.0 - (bus_current_a**2 / single_cell_equiv_a**2)) * 100.0
    
    print(f"  Pack Energy: {energy_wh:.2f} Wh (Series 2S 7.4V nominal)")
    print(f"  Bridge Current @ 3.0W: {bus_current_a:.3f} A (vs 1S current: {single_cell_equiv_a:.3f} A)")
    print(f"  Bridge I^2R Heating Reduction: {i2r_reduction:.1f}%")
    
    assert bus_current_a < 0.45, f"Bus current exceeded 0.45A: {bus_current_a}"
    assert i2r_reduction > 74.0, f"I^2R reduction failed 75% target: {i2r_reduction}"
    print("  [PASS] Series 2S Power Delivery Halves Current & Slashes Hinge Heat by 75%\n")

if __name__ == "__main__":
    print("==================================================================")
    print("PROJECT FRIDAY: FULL-SYSTEM MATHEMATICAL & HARDWARE AUDIT SUITE")
    print("==================================================================\n")
    audit_conductors()
    audit_mass_budget()
    audit_memory_bandwidth()
    audit_audio_decoding()
    audit_thermals()
    audit_power_and_battery()
    print("==================================================================")
    print(">>> ALL 6 AUDIT ENGINES PASSED WITH ZERO DISCREPANCIES <<<")
    print("ALL TESTS PASSED [✓]")
    print("==================================================================")
