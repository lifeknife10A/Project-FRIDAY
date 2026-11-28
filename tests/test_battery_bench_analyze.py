#!/usr/bin/env python3
"""Unit tests for scripts/battery_bench_analyze.py using small SYNTHETIC CSVs."""

from __future__ import annotations

import csv
import json
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import battery_bench_analyze as bba  # noqa: E402


def _write_csv(path: Path, rows: list[tuple[float, float, float, float | str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["time_s", "voltage_V", "current_A", "temp_C"])
        w.writerows(rows)


def _make_synthetic_cell(
    cell_dir: Path,
    *,
    nominal_mah: float = 220.0,
    ambient_c: float = 25.0,
    t2_current_a: float = 0.044,
    t2_duration_s: float = 17100.0,  # 209 mAh (~95% of 220 mAh)
    t3_peak_temp_c: float = 36.0,
    t3_drop_frac: float = 0.90,      # stays >= 3.30 V for 90% of T3
    t4_vmin_20_v: float = 3.12,
    t5_vrest: float = 3.80,
    t5_vload_1s: float = 3.71,       # (3.80 - 3.71)/1.5 = 60 mOhm
    t6_scale: float = 0.99,
    t_init_mm: float = 6.00,
    t_post_mm: float = 6.10,         # +1.67%
    synthetic: bool | None = True,
) -> None:
    cell_dir.mkdir(parents=True, exist_ok=True)
    meta: dict[str, object] = {
        "model": "SYNTHETIC_CELL",
        "cell_id": cell_dir.name,
        "date": "2026-11-28",
        "ambient_C": ambient_c,
        "nominal_mAh": nominal_mah,
        "incoming": {
            "T_init_mm": t_init_mm,
            "T_post_mm": t_post_mm,
        },
    }
    if synthetic is not None:
        meta["synthetic"] = synthetic
    (cell_dir / "meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")

    # T2: 0.2C constant-current discharge
    _write_csv(
        cell_dir / "T2.csv",
        [
            (0.0, 4.18, t2_current_a, ambient_c),
            (t2_duration_s / 2.0, 3.75, t2_current_a, ""),
            (t2_duration_s, 3.00, t2_current_a, ambient_c + 1.0),
        ],
    )

    # T3: 1.5 A CC discharge (~200 mAh = 480 s @ 1.5 A)
    t3_total_s = 480.0
    t_knee = t3_total_s * t3_drop_frac
    _write_csv(
        cell_dir / "T3.csv",
        [
            (0.0, 4.15, 1.50, ambient_c),
            (t_knee * 0.5, 3.55, 1.50, ""),
            (t_knee, 3.31, 1.50, t3_peak_temp_c - 1.0),
            (t_knee + 1.0, 3.25, 1.50, t3_peak_temp_c),
            (t3_total_s, 3.00, 1.50, t3_peak_temp_c - 0.5),
        ],
    )

    # T4: pulse checks at 50% and 20% SoC
    _write_csv(
        cell_dir / "T4_50.csv",
        [(0.0, 3.80, 0.0, ambient_c), (1.0, 3.45, 3.0, ""), (10.0, 3.38, 3.0, ambient_c + 2.0)],
    )
    _write_csv(
        cell_dir / "T4_20.csv",
        [(0.0, 3.65, 0.0, ambient_c), (1.0, 3.25, 3.0, ""), (10.0, t4_vmin_20_v, 3.0, ambient_c + 3.0)],
    )

    # T5: DCIR step at 1.5 A
    _write_csv(
        cell_dir / "T5.csv",
        [
            (0.0, t5_vrest, 0.0, ambient_c),
            (1.0, t5_vrest, 0.0, ""),
            (2.0, t5_vload_1s + 0.02, 1.50, ""),
            (3.0, t5_vload_1s, 1.50, ambient_c),
        ],
    )

    # T6: 2 additional cycles
    for name in ("T6_2.csv", "T6_3.csv"):
        _write_csv(
            cell_dir / name,
            [(0.0, 4.15, 1.50, ambient_c), (t3_total_s * t6_scale, 3.00, 1.50, ambient_c + 8.0)],
        )


class TestBatteryBenchAnalyze(unittest.TestCase):
    def test_passing_model_with_one_bad_cell(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            model_dir = Path(tmp) / "SYNTHETIC_MODEL"
            _make_synthetic_cell(model_dir / "C1", t5_vload_1s=3.71)  # 60 mOhm
            _make_synthetic_cell(model_dir / "C2", t5_vload_1s=3.70)  # 66.7 mOhm
            _make_synthetic_cell(model_dir / "C3", t5_vload_1s=3.69)  # 73.3 mOhm
            _make_synthetic_cell(model_dir / "C4", t5_vload_1s=3.55)  # 166.7 mOhm -> FAIL

            report = bba.analyze_model(model_dir, allow_synthetic=True)
            self.assertTrue(report["model_passed"])
            self.assertEqual(report["verdict"], "PASS")
            self.assertEqual(report["cells_passed"], 3)
            self.assertIsNotNone(report["best_pair"])
            self.assertTrue((model_dir / "report.json").is_file())
            self.assertTrue((model_dir / "report.md").is_file())
            c4 = next(c for c in report["cells"] if c["cell_id"] == "C4")
            self.assertIn("T5_DCIR", c4["failures"])

    def test_failure_modes_dcir_overheat_pulse_sag(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            model_dir = Path(tmp) / "SYNTHETIC_FAILS"
            _make_synthetic_cell(model_dir / "C1", t5_vload_1s=3.56)        # 160 mOhm -> T5_DCIR
            _make_synthetic_cell(model_dir / "C2", t3_peak_temp_c=52.0)     # +27 C & >50 C -> T3_TEMP_RISE/ABS
            _make_synthetic_cell(model_dir / "C3", t4_vmin_20_v=2.85)       # < 3.00 V -> T4_PULSE_SAG

            report = bba.analyze_model(model_dir, allow_synthetic=True)
            self.assertFalse(report["model_passed"])
            self.assertEqual(report["verdict"], "FAIL")
            by_id = {c["cell_id"]: c for c in report["cells"]}
            self.assertIn("T5_DCIR", by_id["C1"]["failures"])
            self.assertIn("T3_TEMP_RISE", by_id["C2"]["failures"])
            self.assertIn("T3_TEMP_ABS", by_id["C2"]["failures"])
            self.assertIn("T4_PULSE_SAG", by_id["C3"]["failures"])

    def test_refuses_missing_meta_and_synthetic_mismatch(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            model_dir = Path(tmp) / "SYNTHETIC_GUARDS"
            _make_synthetic_cell(model_dir / "C1", synthetic=True)
            with self.assertRaises(ValueError):
                bba.analyze_model(model_dir, allow_synthetic=False)

            _make_synthetic_cell(model_dir / "C2", synthetic=None)
            with self.assertRaises(ValueError):
                bba.analyze_cell(model_dir / "C2", allow_synthetic=True)

            (model_dir / "C3").mkdir(parents=True)
            with self.assertRaises(FileNotFoundError):
                bba.analyze_cell(model_dir / "C3", allow_synthetic=True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
