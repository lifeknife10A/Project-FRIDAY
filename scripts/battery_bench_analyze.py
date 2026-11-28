#!/usr/bin/env python3
"""Analyze bench-qualification CSV logs for Project FRIDAY candidate 1S cells.

Reads ``tests/battery/<model>/<cell_id>/`` folders, computes T2–T6 metrics,
evaluates pass/fail thresholds from ``docs/battery_bench_test.md`` §d, checks
2S pair matching, and writes ``report.json`` and ``report.md``.

Refuses to run on folders missing ``meta.json`` or with mismatched/missing
``synthetic`` flags, and never fabricates or fills missing measurements.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path
from typing import Any

import numpy as np

# All pass/fail thresholds cited to docs/battery_bench_test.md §d (D17 / HY2120-CB)
THRESHOLDS: dict[str, float | int] = {
    "t2_min_cap_ratio": 0.85,            # §d: T2 capacity >= 85% of nominal mAh
    "t3_min_voltage_V": 3.30,            # §d: T3 V >= 3.30 V cutoff for usable delivery
    "t3_min_t2_cap_fraction": 0.80,      # §d: >= 80% of T2 capacity delivered above 3.30 V
    "t3_max_temp_rise_C": 15.0,          # §d: cell temp rise <= 15 C over ambient
    "t3_max_temp_abs_C": 50.0,           # §d: absolute peak cell temp <= 50 C
    "t4_min_pulse_voltage_V": 3.00,      # §d: V_min >= 3.00 V at 3.0 A (above HY2120 2.90 V UV)
    "t4_pulse_current_min_A": 2.50,      # pulse detection threshold around 3.0 A step
    "t5_max_dcir_mOhm": 100.0,           # §d: DCIR <= 100 mOhm (2S sag <= 0.30 V @ 1.5 A)
    "t5_rest_current_max_A": 0.10,       # max current considered "at rest" before T5 step
    "t5_load_current_min_A": 1.00,       # min step current for T5 1.5 A load step
    "t6_max_thickness_growth_pct": 5.0,  # §d: thickness growth <= 5% after 3rd cycle
    "t6_max_capacity_change_pct": 3.0,   # §d: capacity change <= 3% across T3/T6 cycles
    "pair_max_cap_diff_pct": 2.0,        # §d: best pair within 2% capacity
    "pair_max_dcir_diff_mOhm": 10.0,     # §d: best pair within 10 mOhm DCIR
    "model_min_passing_cells": 3,        # §d: >= 3 of 4 cells must pass all criteria
}

REQUIRED_CSVS = ("T2.csv", "T3.csv", "T4_50.csv", "T4_20.csv", "T5.csv", "T6_2.csv", "T6_3.csv")


def load_csv(path: Path) -> tuple[np.ndarray, np.ndarray, np.ndarray, list[float | None]]:
    """Load a canonical bench CSV (time_s,voltage_V,current_A,temp_C) without filling blanks."""
    if not path.is_file():
        raise FileNotFoundError(f"Missing required CSV: {path}")

    times: list[float] = []
    volts: list[float] = []
    amps: list[float] = []
    temps: list[float | None] = []

    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        expected = {"time_s", "voltage_V", "current_A", "temp_C"}
        if reader.fieldnames is None or not expected.issubset(set(reader.fieldnames)):
            raise ValueError(f"{path}: CSV header must contain {sorted(expected)}, got {reader.fieldnames}")
        for idx, row in enumerate(reader, start=2):
            try:
                t_val = float(row["time_s"])
                v_val = float(row["voltage_V"])
                i_val = float(row["current_A"])
            except (TypeError, ValueError) as exc:
                raise ValueError(f"{path}:{idx}: invalid numeric value in time_s/voltage_V/current_A") from exc
            raw_temp = (row.get("temp_C") or "").strip()
            if raw_temp == "":
                temp_val: float | None = None
            else:
                try:
                    temp_val = float(raw_temp)
                except ValueError as exc:
                    raise ValueError(f"{path}:{idx}: invalid temp_C value {raw_temp!r}") from exc
            times.append(t_val)
            volts.append(v_val)
            amps.append(i_val)
            temps.append(temp_val)

    if len(times) < 2:
        raise ValueError(f"{path}: need at least 2 rows, got {len(times)}")
    t_arr = np.asarray(times, dtype=float)
    if np.any(np.diff(t_arr) < 0):
        raise ValueError(f"{path}: time_s must be non-decreasing")
    return t_arr, np.asarray(volts, dtype=float), np.asarray(amps, dtype=float), temps


def integrate_mah(time_s: np.ndarray, current_a: np.ndarray) -> float:
    """Trapezoidal integration of current (A) over time (s) converted to mAh."""
    return float(np.trapezoid(current_a, time_s) / 3.6)


def compute_t3_delivery_mah(time_s: np.ndarray, voltage_v: np.ndarray, current_a: np.ndarray, min_v: float) -> float:
    """Compute cumulative mAh delivered before voltage first drops below ``min_v``."""
    below = np.where(voltage_v < min_v)[0]
    if below.size == 0:
        return integrate_mah(time_s, current_a)
    first_bad = int(below[0])
    if first_bad == 0:
        return 0.0
    return integrate_mah(time_s[: first_bad + 1], current_a[: first_bad + 1])


def compute_t4_pulse_vmin(path: Path) -> tuple[float, int]:
    """Return (min voltage during >= threshold pulse samples, pulse sample count)."""
    _, voltage_v, current_a, _ = load_csv(path)
    mask = current_a >= float(THRESHOLDS["t4_pulse_current_min_A"])
    if not np.any(mask):
        raise ValueError(f"{path}: no pulse samples found with current_A >= {THRESHOLDS['t4_pulse_current_min_A']}")
    return float(np.min(voltage_v[mask])), int(np.sum(mask))


def compute_t5_dcir_mohm(path: Path) -> float:
    """Compute DCIR in mOhm from (V_rest - V_load_at_1s) / I at the 1.5 A load step."""
    time_s, voltage_v, current_a, _ = load_csv(path)
    rest_max = float(THRESHOLDS["t5_rest_current_max_A"])
    load_min = float(THRESHOLDS["t5_load_current_min_A"])

    load_idxs = np.where(current_a >= load_min)[0]
    if load_idxs.size == 0:
        raise ValueError(f"{path}: no load step found with current_A >= {load_min}")
    step_start = int(load_idxs[0])
    rest_mask = current_a[:step_start] <= rest_max
    if not np.any(rest_mask):
        raise ValueError(f"{path}: no rest voltage samples (<= {rest_max} A) before load step")

    v_rest = float(voltage_v[:step_start][rest_mask][-1])
    target_t = float(time_s[step_start]) + 1.0
    after_1s = np.where((time_s >= target_t) & (current_a >= load_min))[0]
    if after_1s.size == 0:
        raise ValueError(f"{path}: no load sample at or after t_step + 1.0 s ({target_t} s)")
    idx_1s = int(after_1s[0])
    v_load_1s = float(voltage_v[idx_1s])
    i_load = float(current_a[idx_1s])
    return 1000.0 * (v_rest - v_load_1s) / i_load


def load_and_validate_meta(cell_dir: Path, allow_synthetic: bool) -> dict[str, Any]:
    """Load and strictly validate ``meta.json`` including the ``synthetic`` guard."""
    meta_path = cell_dir / "meta.json"
    if not meta_path.is_file():
        raise FileNotFoundError(f"{cell_dir}: missing required meta.json")

    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    if "synthetic" not in meta or not isinstance(meta["synthetic"], bool):
        raise ValueError(f"{meta_path}: 'synthetic' boolean field is required")
    if meta["synthetic"] and not allow_synthetic:
        raise ValueError(f"{meta_path}: synthetic=true requires --synthetic flag")
    if not meta["synthetic"] and allow_synthetic:
        raise ValueError(f"{meta_path}: synthetic=false cannot be analyzed with --synthetic flag")

    for req_key in ("ambient_C", "nominal_mAh", "incoming"):
        if req_key not in meta or meta[req_key] is None:
            raise ValueError(f"{meta_path}: missing required field '{req_key}'")
    incoming = meta["incoming"]
    for inc_key in ("T_init_mm", "T_post_mm"):
        if inc_key not in incoming or incoming[inc_key] is None:
            raise ValueError(f"{meta_path}: missing required incoming field '{inc_key}'")
    return meta


def analyze_cell(cell_dir: Path, allow_synthetic: bool) -> dict[str, Any]:
    """Compute all T2–T6 metrics and pass/fail flags for a single cell directory."""
    meta = load_and_validate_meta(cell_dir, allow_synthetic=allow_synthetic)
    for fname in REQUIRED_CSVS:
        if not (cell_dir / fname).is_file():
            raise FileNotFoundError(f"{cell_dir}: missing required CSV '{fname}'")

    nominal_mah = float(meta["nominal_mAh"])
    ambient_c = float(meta["ambient_C"])
    t_init_mm = float(meta["incoming"]["T_init_mm"])
    t_post_mm = float(meta["incoming"]["T_post_mm"])

    # T2 capacity
    t2_t, _, t2_i, _ = load_csv(cell_dir / "T2.csv")
    cap_t2 = integrate_mah(t2_t, t2_i)
    t2_pct_nom = 100.0 * cap_t2 / nominal_mah

    # T3 continuous 1.5 A
    t3_t, t3_v, t3_i, t3_temps = load_csv(cell_dir / "T3.csv")
    cap_t3 = integrate_mah(t3_t, t3_i)
    cap_t3_v330 = compute_t3_delivery_mah(t3_t, t3_v, t3_i, float(THRESHOLDS["t3_min_voltage_V"]))
    t3_v330_pct_t2 = 100.0 * cap_t3_v330 / cap_t2 if cap_t2 > 0 else 0.0
    valid_temps = [x for x in t3_temps if x is not None]
    if not valid_temps:
        raise ValueError(f"{cell_dir / 'T3.csv'}: no valid temp_C measurements present")
    t3_peak_temp_c = max(valid_temps)
    t3_temp_rise_c = t3_peak_temp_c - ambient_c

    # T4 pulses at 50% and 20% SoC
    vmin_50, n_50 = compute_t4_pulse_vmin(cell_dir / "T4_50.csv")
    vmin_20, n_20 = compute_t4_pulse_vmin(cell_dir / "T4_20.csv")
    t4_vmin = min(vmin_50, vmin_20)

    # T5 DCIR
    dcir_mohm = compute_t5_dcir_mohm(cell_dir / "T5.csv")

    # T6 cycling + thickness swelling
    t6_2_t, _, t6_2_i, _ = load_csv(cell_dir / "T6_2.csv")
    t6_3_t, _, t6_3_i, _ = load_csv(cell_dir / "T6_3.csv")
    cap_t6_2 = integrate_mah(t6_2_t, t6_2_i)
    cap_t6_3 = integrate_mah(t6_3_t, t6_3_i)
    cap_change_pct = 100.0 * max(abs(cap_t6_2 - cap_t3), abs(cap_t6_3 - cap_t3)) / cap_t3 if cap_t3 > 0 else 100.0
    thickness_growth_pct = 100.0 * (t_post_mm - t_init_mm) / t_init_mm

    failures: list[str] = []
    if cap_t2 < float(THRESHOLDS["t2_min_cap_ratio"]) * nominal_mah:
        failures.append("T2_CAPACITY")
    if cap_t3_v330 < float(THRESHOLDS["t3_min_t2_cap_fraction"]) * cap_t2:
        failures.append("T3_VOLTAGE_DELIVERY")
    if t3_temp_rise_c > float(THRESHOLDS["t3_max_temp_rise_C"]):
        failures.append("T3_TEMP_RISE")
    if t3_peak_temp_c > float(THRESHOLDS["t3_max_temp_abs_C"]):
        failures.append("T3_TEMP_ABS")
    if t4_vmin < float(THRESHOLDS["t4_min_pulse_voltage_V"]):
        failures.append("T4_PULSE_SAG")
    if dcir_mohm > float(THRESHOLDS["t5_max_dcir_mOhm"]):
        failures.append("T5_DCIR")
    if thickness_growth_pct > float(THRESHOLDS["t6_max_thickness_growth_pct"]):
        failures.append("T6_SWELLING")
    if cap_change_pct > float(THRESHOLDS["t6_max_capacity_change_pct"]):
        failures.append("T6_CAP_FADE")

    return {
        "cell_id": cell_dir.name,
        "synthetic": bool(meta["synthetic"]),
        "ambient_C": ambient_c,
        "nominal_mAh": nominal_mah,
        "t2_cap_mAh": round(cap_t2, 3),
        "t2_pct_of_nominal": round(t2_pct_nom, 2),
        "t3_cap_mAh": round(cap_t3, 3),
        "t3_v330_mAh": round(cap_t3_v330, 3),
        "t3_v330_pct_of_t2": round(t3_v330_pct_t2, 2),
        "t3_peak_temp_C": round(t3_peak_temp_c, 2),
        "t3_temp_rise_C": round(t3_temp_rise_c, 2),
        "t4_vmin_50_V": round(vmin_50, 4),
        "t4_vmin_20_V": round(vmin_20, 4),
        "t4_vmin_V": round(t4_vmin, 4),
        "t4_pulse_samples": n_50 + n_20,
        "t5_dcir_mOhm": round(dcir_mohm, 2),
        "t6_cap_cycle2_mAh": round(cap_t6_2, 3),
        "t6_cap_cycle3_mAh": round(cap_t6_3, 3),
        "t6_cap_change_pct": round(cap_change_pct, 2),
        "t6_thickness_growth_pct": round(thickness_growth_pct, 2),
        "passed": len(failures) == 0,
        "failures": failures,
    }


def select_best_pair(cells: list[dict[str, Any]]) -> dict[str, Any] | None:
    """Find best-matched passing pair within 2% capacity and 10 mOhm DCIR."""
    passing = [c for c in cells if c["passed"]]
    best: dict[str, Any] | None = None
    for i in range(len(passing)):
        for j in range(i + 1, len(passing)):
            a, b = passing[i], passing[j]
            cap_diff_pct = 100.0 * abs(a["t2_cap_mAh"] - b["t2_cap_mAh"]) / max(a["t2_cap_mAh"], b["t2_cap_mAh"])
            dcir_diff_mohm = abs(a["t5_dcir_mOhm"] - b["t5_dcir_mOhm"])
            if (
                cap_diff_pct <= float(THRESHOLDS["pair_max_cap_diff_pct"])
                and dcir_diff_mohm <= float(THRESHOLDS["pair_max_dcir_diff_mOhm"])
            ):
                cand = {
                    "pair": [a["cell_id"], b["cell_id"]],
                    "cap_diff_pct": round(cap_diff_pct, 3),
                    "dcir_diff_mOhm": round(dcir_diff_mohm, 2),
                }
                if best is None or (cand["dcir_diff_mOhm"], cand["cap_diff_pct"]) < (
                    best["dcir_diff_mOhm"],
                    best["cap_diff_pct"],
                ):
                    best = cand
    return best


def analyze_model(model_dir: Path, allow_synthetic: bool = False) -> dict[str, Any]:
    """Analyze all cell subdirectories under ``model_dir`` and write report.json + report.md."""
    if not model_dir.is_dir():
        raise FileNotFoundError(f"Model directory not found: {model_dir}")

    cell_dirs = sorted([p for p in model_dir.iterdir() if p.is_dir()])
    if not cell_dirs:
        raise ValueError(f"No cell subdirectories found in {model_dir}")

    cells = [analyze_cell(cdir, allow_synthetic=allow_synthetic) for cdir in cell_dirs]
    passing_count = sum(1 for c in cells if c["passed"])
    best_pair = select_best_pair(cells)
    model_passed = (passing_count >= int(THRESHOLDS["model_min_passing_cells"])) and (best_pair is not None)

    report = {
        "model": model_dir.name,
        "synthetic": allow_synthetic,
        "thresholds": THRESHOLDS,
        "cells_tested": len(cells),
        "cells_passed": passing_count,
        "best_pair": best_pair,
        "model_passed": model_passed,
        "verdict": "PASS" if model_passed else "FAIL",
        "cells": cells,
    }

    (model_dir / "report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    lines = [
        f"# Battery Bench-Qualification Report — `{model_dir.name}`",
        "",
        f"- **Verdict:** **{report['verdict']}** (`{passing_count}/{len(cells)}` cells passed; threshold `>= {THRESHOLDS['model_min_passing_cells']}`)",
        f"- **Data Mode:** `{'SYNTHETIC' if allow_synthetic else 'REAL BENCH'}`",
        f"- **Best Matched Pair:** `{best_pair['pair']}` (`ΔCap = {best_pair['cap_diff_pct']}%`, `ΔDCIR = {best_pair['dcir_diff_mOhm']} mΩ`)"
        if best_pair
        else "- **Best Matched Pair:** `NONE` (no passing pair within `2%` capacity and `10 mΩ` DCIR)",
        "",
        "| Cell | T2 Cap (mAh / %Nom) | T3 ≥3.30V (%T2) | T3 Peak / ΔT (°C) | T4 Vmin (V) | T5 DCIR (mΩ) | T6 ΔCap / Swell (%) | Result | Failed Rules |",
        "|---|---:|---:|---:|---:|---:|---:|:---:|---|",
    ]
    for c in cells:
        res = "PASS" if c["passed"] else "FAIL"
        fails = ", ".join(c["failures"]) if c["failures"] else "—"
        lines.append(
            f"| `{c['cell_id']}` | {c['t2_cap_mAh']} ({c['t2_pct_of_nominal']}%) | {c['t3_v330_pct_of_t2']}% | "
            f"{c['t3_peak_temp_C']} / +{c['t3_temp_rise_C']} | {c['t4_vmin_V']} | {c['t5_dcir_mOhm']} | "
            f"{c['t6_cap_change_pct']}% / {c['t6_thickness_growth_pct']}% | **{res}** | {fails} |"
        )
    (model_dir / "report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Analyze FRIDAY battery bench-qualification logs.")
    parser.add_argument("model_dir", type=Path, help="Path to tests/battery/<model>")
    parser.add_argument("--synthetic", action="store_true", help="Allow analyzing meta.json with synthetic=true")
    args = parser.parse_args(argv)
    try:
        report = analyze_model(args.model_dir, allow_synthetic=args.synthetic)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(f"{report['model']}: {report['verdict']} ({report['cells_passed']}/{report['cells_tested']} passed)")
    return 0 if report["model_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
