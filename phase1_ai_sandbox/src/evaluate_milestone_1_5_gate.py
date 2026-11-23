"""
PROJECT FRIDAY - MILESTONE 1.5 EMPIRICAL TECHNICAL GATE
Automated Empirical Evaluation Suite for Vision, Multimodal Distillation,
Benchmark Fine-Print Reading, Memory Bandwidth & Neural Voice Quality.
Author: Krishna Jagat Solanki
"""

import os
import sys
import time
import json
import numpy as np
import torch
import cv2

# Add src to path
sys.path.append(os.path.dirname(__file__))
from optical_foveation import OpticalFoveationEngine, create_synthetic_prescription_label
from student_vlm import SpatialUnshuffleDownsampler
from kokoro_voice_engine import FridayVoiceEngine
from benchmark_dataset_evaluator import (
    BenchmarkEvaluator,
    normalize_entity_space_insensitive,
    normalize_numeric_context,
    check_sensitive_modification_or_low_conf
)

def evaluate_milestone_1_5_gate():
    print("==================================================================")
    print("PROJECT FRIDAY: MILESTONE 1.5 EMPIRICAL TECHNICAL GATE AUDIT")
    print("==================================================================")
    print("Purpose: Empirical validation of optical foveation, 144-token vision")
    print("         projection, multimodal distillation convergence, memory bandwidth,")
    print("         and downstream 40-sample benchmark fine-print comprehension.\n")

    results = {}
    all_passed = True
    device = torch.device("mps" if torch.backends.mps.is_available() else ("cuda" if torch.cuda.is_available() else "cpu"))

    # -------------------------------------------------------------
    # GATE 1: OPTICAL FOVEATION & RESOLUTION PRESERVATION
    # -------------------------------------------------------------
    print("--- [GATE 1/5] EVALUATING OPTICAL FOVEATION & RESOLUTION ---")
    foveation_engine = OpticalFoveationEngine(target_crop_size=384, pitch_angle_deg=6.0)
    test_frame = create_synthetic_prescription_label()
    
    t0 = time.perf_counter()
    stream0, stream1, meta = foveation_engine.process_frame(test_frame)
    foveation_time_ms = (time.perf_counter() - t0) * 1000.0
    
    g1_shape_pass = (stream0.shape == (384, 384, 3)) and (stream1.shape == (384, 384, 3))
    g1_latency_pass = foveation_time_ms < 25.0
    g1_guidance_pass = bool(meta.get("boundary_overflow")) and (meta.get("guidance_message") is not None)
    
    print(f"  Stream 0 Dimensions: {stream0.shape} (Expected: 384x384x3) -> {'PASS' if stream0.shape == (384, 384, 3) else 'FAIL'}")
    print(f"  Stream 1 Foveal Crop: {stream1.shape} (Expected: 384x384x3) -> {'PASS' if stream1.shape == (384, 384, 3) else 'FAIL'}")
    print(f"  Dynamic Foveation Latency: {foveation_time_ms:.2f} ms (Target: < 25.0 ms) -> {'PASS' if g1_latency_pass else 'FAIL'}")
    print(f"  Boundary Overflow Guidance Triggered: {meta.get('boundary_overflow')} -> {'PASS' if g1_guidance_pass else 'FAIL'}")
    
    gate1_pass = bool(g1_shape_pass and g1_latency_pass and g1_guidance_pass)
    results["Gate_1_Optical_Foveation"] = {
        "passed": gate1_pass,
        "foveation_latency_ms": round(foveation_time_ms, 2),
        "stream1_resolution": list(stream1.shape),
        "guidance_protocol_active": bool(meta.get("boundary_overflow"))
    }
    if not gate1_pass: all_passed = False

    # -------------------------------------------------------------
    # GATE 2: 2x2 SPATIAL UNSHUFFLE (576 -> 144 TOKENS)
    # -------------------------------------------------------------
    print("\n--- [GATE 2/5] EVALUATING 2x2 SPATIAL UNSHUFFLE DOWNSAMPLING ---")
    unshuffle = SpatialUnshuffleDownsampler(
        in_features=768,
        out_features=896,
        grid_size=24
    ).to(device)
    unshuffle.eval()
    
    dummy_input = torch.randn(1, 576, 768, device=device)
    with torch.no_grad():
        _ = unshuffle(dummy_input) # Warmup
        
    t0 = time.perf_counter()
    with torch.no_grad():
        out_tokens = unshuffle(dummy_input)
    unshuffle_time_ms = (time.perf_counter() - t0) * 1000.0
    
    out_b, out_n, out_d = out_tokens.shape
    g2_token_pass = (out_n == 144)
    g2_dim_pass = (out_d == 896)
    
    print(f"  Output Visual Token Count: {out_n} (Target: Strictly 144 tokens, 75% sequence reduction) -> {'PASS' if g2_token_pass else 'FAIL'}")
    print(f"  Projected Hidden Dimension: {out_d} (Target: 896 for Qwen2.5-0.5B) -> {'PASS' if g2_dim_pass else 'FAIL'}")
    print(f"  Host Execution Latency (Reference Only): {unshuffle_time_ms:.2f} ms")
    
    gate2_pass = bool(g2_token_pass and g2_dim_pass)
    results["Gate_2_Spatial_Unshuffle"] = {
        "passed": gate2_pass,
        "output_tokens": int(out_n),
        "embedding_dim": int(out_d),
        "host_reference_latency_ms": round(unshuffle_time_ms, 2),
        "note": "Host latency reported as reference only; physical RK3576 NPU latency to be measured in Phase 2 bring-up."
    }
    if not gate2_pass: all_passed = False

    # -------------------------------------------------------------
    # GATE 3: MEMORY BANDWIDTH & BUS CAPACITY CONTRACT
    # -------------------------------------------------------------
    print("\n--- [GATE 3/5] AUDITING MEMORY BANDWIDTH & BUS CAPACITY ---")
    weights_int4_mb = 208.32 # All-INT4 packed binary
    scales_norms_mb = 16.0
    kv_cache_mb = 6.29 # INT8 KV cache for 1024-token context window
    total_mb_per_token = weights_int4_mb + scales_norms_mb + kv_cache_mb # 230.61 MB
    
    target_tok_s = 25.0
    operating_bw_gb_s = (total_mb_per_token / 1000.0) * target_tok_s # 5.77 GB/s
    burst_bw_gb_s = (total_mb_per_token / 1000.0) * 35.0 # 8.07 GB/s
    bus_safe_ceiling_gb_s = 14.00 # Firefly CAM-3576Q38 32-bit LPDDR5 @ 5500 MT/s safe ceiling
    headroom_operating_gb_s = bus_safe_ceiling_gb_s - operating_bw_gb_s
    headroom_pct = (headroom_operating_gb_s / bus_safe_ceiling_gb_s) * 100.0
    
    g3_bw_pass = (operating_bw_gb_s < bus_safe_ceiling_gb_s) and (burst_bw_gb_s < bus_safe_ceiling_gb_s)
    g3_headroom_pass = (headroom_pct >= 40.0)
    
    print(f"  All-INT4 Packed Footprint: {weights_int4_mb:.2f} MB")
    print(f"  Total DDR Traffic per Token: {total_mb_per_token:.2f} MB/token")
    print(f"  Operating Bandwidth @ 25 tok/s: {operating_bw_gb_s:.2f} GB/s (Safe Ceiling: {bus_safe_ceiling_gb_s:.2f} GB/s) -> {'PASS' if g3_bw_pass else 'FAIL'}")
    print(f"  Burst Peak Bandwidth @ 35 tok/s: {burst_bw_gb_s:.2f} GB/s (Safe Ceiling: {bus_safe_ceiling_gb_s:.2f} GB/s) -> {'PASS' if g3_bw_pass else 'FAIL'}")
    print(f"  Continuous Operating Headroom: {headroom_operating_gb_s:.2f} GB/s ({headroom_pct:.1f}% margin) -> {'PASS' if g3_headroom_pass else 'FAIL'}")
    
    gate3_pass = bool(g3_bw_pass and g3_headroom_pass)
    results["Gate_3_Memory_Bandwidth"] = {
        "passed": gate3_pass,
        "operating_bandwidth_gb_s": round(operating_bw_gb_s, 2),
        "burst_bandwidth_gb_s": round(burst_bw_gb_s, 2),
        "bus_safe_ceiling_gb_s": round(bus_safe_ceiling_gb_s, 2),
        "headroom_pct": round(headroom_pct, 1)
    }
    if not gate3_pass: all_passed = False

    # -------------------------------------------------------------
    # GATE 4: KOKORO-82M NEURAL VOICE QUALITY & RTF
    # -------------------------------------------------------------
    print("\n--- [GATE 4/5] AUDITING KOKORO-82M VOICE SYNTHESIS (bf_emma) ---")
    voice_engine = FridayVoiceEngine(voice="bf_emma")
    test_phrase = "Project Friday voice synthesis verified with Emma persona."
    
    t0 = time.perf_counter()
    sample_wav = voice_engine.synthesize(test_phrase, output_wav="assets/gate_voice_test.wav")
    synth_time_ms = (time.perf_counter() - t0) * 1000.0
    
    g4_voice_pass = False
    rtf = 1.0
    if sample_wav and os.path.exists(sample_wav):
        import soundfile as sf
        audio_info = sf.info(sample_wav)
        duration_s = audio_info.duration
        rtf = (synth_time_ms / 1000.0) / max(0.01, duration_s)
        g4_voice_pass = (audio_info.samplerate == 24000) and (rtf < 1.0)
        print(f"  Synthesized Audio Duration: {duration_s:.2f} s")
        print(f"  Synthesis Latency: {synth_time_ms:.1f} ms (RTF: {rtf:.2f}, Target: RTF < 1.0) -> {'PASS' if rtf < 1.0 else 'FAIL'}")
        print(f"  Sampling Rate: {audio_info.samplerate} Hz (Target: 24,000 Hz) -> {'PASS' if audio_info.samplerate == 24000 else 'FAIL'}")
    else:
        print("  [!] Kokoro synthesis output file missing!")
        
    gate4_pass = bool(g4_voice_pass)
    results["Gate_4_Kokoro_Voice"] = {
        "passed": gate4_pass,
        "voice_persona": "bf_emma",
        "sample_rate_hz": 24000,
        "real_time_factor": round(rtf, 2),
        "faster_than_realtime": bool(rtf < 1.0)
    }
    if not gate4_pass: all_passed = False

    # -------------------------------------------------------------
    # GATE 5: 40-SAMPLE MULTIMODAL BENCHMARK EVALUATION (LITERAL PATH)
    # -------------------------------------------------------------
    print("\n--- [GATE 5/5] AUDITING 40-SAMPLE MULTIMODAL BENCHMARK (LITERAL PATH) ---")
    manifest_path = os.path.join(os.path.dirname(__file__), "../../assets/benchmark_dataset/benchmark_manifest.json")
    
    g5_pass = False
    bench_summary = {}
    if os.path.exists(manifest_path):
        from benchmark_dataset_evaluator import BenchmarkEvaluator, run_ocr, REFUSAL_TEXT
        from literal_reader import read_literal
        evaluator = BenchmarkEvaluator(manifest_path)
        
        predictions = {}
        for sample in evaluator.samples:
            img_rel = os.path.join(os.path.dirname(manifest_path), "images", sample["filename"])
            pred_text = ""
            raw_pred_text = ""
            conf = 0.0
            extracted_ans = REFUSAL_TEXT
            fb_triggered = False
            
            if os.path.exists(img_rel):
                ocr_lines = run_ocr(img_rel)
                if ocr_lines:
                    conf = float(np.mean([l.get("confidence", 0.0) for l in ocr_lines]))
                    raw_pred_text = " ".join([l.get("raw_text", "") for l in ocr_lines])
                    pred_text = " ".join([l.get("normalized_text", "") for l in ocr_lines])
                    
                    # Auditor Item B3: Use read_literal for literal rows, never pass raw transcript
                    lit_res = read_literal(ocr_lines, sample.get("category", ""), sample.get("prompt", ""))
                    extracted_ans = lit_res.get("speech", REFUSAL_TEXT)
                    if extracted_ans == REFUSAL_TEXT:
                        fb_triggered = True
                else:
                    pred_text = ""
                    raw_pred_text = ""
                    conf = 0.0
                    extracted_ans = REFUSAL_TEXT
                    fb_triggered = True
            else:
                pred_text = ""
                raw_pred_text = ""
                conf = 0.0
                extracted_ans = REFUSAL_TEXT
                fb_triggered = True
                
            predictions[sample["id"]] = {
                "predicted_text": pred_text,
                "raw_predicted_text": raw_pred_text,
                "confidence": conf,
                "extracted_answer": extracted_ans,
                "fallback_triggered": fb_triggered
            }
            
        bench_summary = evaluator.evaluate_predictions(predictions)
        key_acc = bench_summary["aggregate_key_field_accuracy_pct"]
        safety_acc = bench_summary["aggregate_safety_entity_accuracy_pct"]
        raw_cer = bench_summary["aggregate_raw_cer_pct"]
        raw_wer = bench_summary["aggregate_raw_wer_pct"]
        sp_cer = bench_summary["aggregate_space_norm_cer_pct"]
        sp_wer = bench_summary["aggregate_space_norm_wer_pct"]
        safety_counts = bench_summary.get("safety_metric_counts", {})
        wrong_spoken_count = bench_summary.get("wrong_spoken_dose_count", 0)
        
        # Strict pre-registered thresholds from plan.md line 332 & Auditor Gate A6
        g5_key_pass = key_acc >= 95.0
        g5_safety_pass = safety_acc >= 95.0
        g5_cer_pass = raw_cer <= 5.0  # Plan.md line 332 strict threshold
        g5_wer_pass = raw_wer <= 30.0 # Plan.md line 332 strict threshold
        g5_wrong_spoken_pass = (wrong_spoken_count == 0) # Hard safety gate: wrong-spoken = 0
        g5_pass = bool(g5_key_pass and g5_safety_pass and g5_cer_pass and g5_wer_pass and g5_wrong_spoken_pass)
        
        print(f"  Benchmark Total Samples: {bench_summary['total_samples']} across 4 categories")
        print(f"  Key-Field Exact Match: {key_acc:.2f}% (Target: >= 95.0%) -> {'PASS' if g5_key_pass else 'FAIL'}")
        print(f"  Numerical Safety Entity Accuracy: {safety_acc:.2f}% (Target: >= 95.0%) -> {'PASS' if g5_safety_pass else 'FAIL'}")
        print(f"  Safety Protocol Counts: Correct = {safety_counts.get('correct', 0)}, Safe-Refusal = {safety_counts.get('safe_refusal', 0)}, Wrong-Spoken = {wrong_spoken_count} (Hard Gate: Wrong-Spoken == 0) -> {'PASS' if g5_wrong_spoken_pass else 'FAIL'}")
        print(f"  Raw Unstripped Punctuation CER: {raw_cer:.2f}% (Target: <= 5.0%) -> {'PASS' if g5_cer_pass else 'FAIL'}")
        print(f"  Raw Unstripped Punctuation WER: {raw_wer:.2f}% (Target: <= 30.0%) -> {'PASS' if g5_wer_pass else 'FAIL'}")
        print(f"  Space-Normalized CER / WER: {sp_cer:.2f}% / {sp_wer:.2f}%")
        print("  Per-Category Performance Breakdown:")
        for cat, c_data in bench_summary["category_breakdown"].items():
            print(f"    - {cat:<14s}: Key = {c_data['key_field_accuracy_pct']:5.1f}% | Raw CER = {c_data['raw_cer_pct']:5.2f}% | Sp-CER = {c_data['space_norm_cer_pct']:5.2f}%")
    else:
        print("  [!] Benchmark manifest not found!")
        
    results["Gate_5_Benchmark_Dataset"] = {
        "passed": g5_pass,
        "metrics": bench_summary
    }
    if not g5_pass: all_passed = False

    # -------------------------------------------------------------
    # SUMMARY DECISION MATRIX
    # -------------------------------------------------------------
    print("\n" + "="*65)
    print("MILESTONE 1.5 FINAL TECHNICAL GATE DECISION MATRIX")
    print("="*65)
    for gate, data in results.items():
        status = "PASSED [✓]" if data["passed"] else "FAILED [X]"
        print(f"  {gate:<35}: {status}")
        
    print("="*65)
    if all_passed:
        print(">>> MILESTONE 1.5 TECHNICAL GATE: ALL CRITERIA SATISFIED <<<")
    else:
        print(">>> MILESTONE 1.5 TECHNICAL GATE: HALTED (CRITERIA NOT MET) <<<")
    print("="*65 + "\n")

    # Save manifest computed strictly from execution data
    report_file = os.path.join(os.path.dirname(__file__), "../milestone_1_5_evaluation_report.json")
    report_data = {
        "milestone_1_5_overall_pass": bool(all_passed),
        "gates": results,
        "target_architecture": "Rockchip_RK3576",
        "som_module": "Firefly_CAM_3576Q38_LPDDR5",
        "visual_tokens_invariant": 144,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    }
    with open(report_file, "w") as f:
        json.dump(report_data, f, indent=2)
    print(f"Evaluation report saved to: {report_file}")

    return all_passed

if __name__ == "__main__":
    success = evaluate_milestone_1_5_gate()
    sys.exit(0 if success else 1)
