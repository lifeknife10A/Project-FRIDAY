# Project FRIDAY — Battery Bench-Qualification Procedure (D17)

This procedure qualifies candidate 1S LiPo / LiHV cells (e.g. `Tattu 220 mAh 1S`, `Gens Ace 200 mAh 1S`, `GNB 300 mAh 1S`, `Grepow C200-5811047`) for Project FRIDAY's **2S left-temple pack** under **D16** and **D17** (`docs/plan1.md`, `docs/battery_cell_selection.md` §5):
- **Charger design point:** `IP2326_NPD` at `0.20 A` (`RISET = 450 kΩ`) to `4.20 V/cell` (`8.40 V` pack).
- **Protector design point:** `HY2120-CB` (`OVP 4.28 ± 0.025 V`, `UVP 2.90 ± 0.08 V`).
- **Load envelope (D17):** `8 W` burst (`≤ 1.50 A` pack at `6.0 V` empty / `90%` buck), `~3 W` sustained, `3.0 A` pulse headroom.

---

## a. Safety Rules (Mandatory — Read Before Handling Any Cell)

1. **Fire-safe workspace:** Conduct every charge, discharge, and pulse test inside a **LiPo-safe fireproof bag** or on a **ceramic/steel tile** cleared of all flammable materials.
2. **Never leave unattended:** Never leave a charging or high-rate discharging cell unattended, even for one minute.
3. **Fire suppression within arm's reach:** Keep a **bucket of dry sand** or an **ABC / Class-D dry-chemical fire extinguisher** directly beside the bench. **Never** pour water on a lithium-polymer fire.
4. **Immediate abort conditions:** Stop the test immediately, disconnect leads if safe, and move the cell into dry sand / outdoors if any of the following occur:
   - Cell body temperature **`> 60 °C`**
   - Any visible **swelling / puffing** of the pouch
   - Any sweet, fruity, or chemical **electrolyte odor** or hissing
   - Cell voltage drops **`< 2.90 V`** (under load or at rest)
5. **One cell at a time:** Test only **one single 1S cell** at a time. Never parallel-connect or series-connect uncharacterized cells on the bench.
6. **Insulate tabs & verify polarity:** Cover exposed cell tabs/solder pads with **Kapton tape** leaving only the test clip area exposed. Always verify `+` / `-` polarity with a multimeter before connecting the charger or electronic load.

---

## b. Equipment List (with Indian Sources)

| Item | Minimum Spec | Example Class | Indian Sources |
|---|---|---|---|
| **Balance / Smart Charger** | 1S LiPo/LiHV CC/CV (`0.1–1.0 A`, `4.20 V` cutoff) + **per-cell IR readout (`mΩ`)** | ISDT Q6 Nano / ToolkitRC M6DAC / SkyRC B6neo class | [Robu.in](https://robu.in/), [RC Mumbai](https://rcmumbai.com/), [Quadkart](https://www.quadkart.in/) |
| **Constant-Current Electronic Load** | `0–5 A+` CC mode, `0.01 A` step, **PC / Bluetooth CSV logging** (4-wire Kelvin sense preferred) | Atorch DL24 / DL24P class | [Robu.in](https://robu.in/), [ElectronicsComp](https://www.electronicscomp.com/), Amazon.in |
| **Digital Multimeter (DMM)** | `0.001 V` DC resolution | Mastech / Fluke / UNI-T | [Robu.in](https://robu.in/), Amazon.in |
| **Temperature Probe** | K-type thermocouple or `10 kΩ` NTC taped to cell center with Kapton tape (logged or read every `30 s`) | DMM thermocouple / USB logger | [Robu.in](https://robu.in/), Amazon.in |
| **Precision Scale** | `0.01 g` resolution (`0–100 g+`) | Pocket digital jewellery scale | Amazon.in, [Robu.in](https://robu.in/) |
| **Vernier Caliper** | `0.01 mm` resolution (**insulate jaws with Kapton tape** before touching bare tabs) | Digital vernier caliper | [Robu.in](https://robu.in/), Amazon.in |
| **Timer / Stopwatch** | `1 s` resolution (for manual `30 s` temp logs & pulse timing if not scripted) | Phone / bench timer | — |
| **Safety Consumables** | LiPo-safe bag, ceramic tile, dry sand bucket / extinguisher, Kapton tape | — | Local hardware / Amazon.in |

---

## c. Test Protocol (`4` Cells per Model: `C1`, `C2`, `C3`, `C4`)

Record **ambient room temperature (`°C`)** before starting each cell. Tape the temperature probe firmly to the flat center of the pouch cell using Kapton tape.

1. **T0 — Incoming Inspection (per cell `C1`–`C4`):**
   - Take front/back photos showing printed markings.
   - Transcribe exact label text.
   - Measure **mass (`g`)**, **length `L` / width `W` / thickness `T_init` (`mm`)**, **open-circuit voltage `V_ocv` (`V`)**, and **charger AC/DC IR (`mΩ`)**. Record in `meta.json`.
2. **T1 — Standard Charge (`4.20 V`):**
   - Charge CC **`0.20 A`** -> CV **`4.20 V`**, termination cutoff **`0.02 A`** (matches `IP2326_NPD` with `RISET = 450 kΩ`).
   - Log `T1.csv`: `mAh` in, total charge time, and peak body temperature (`°C`). Rest `10 min`.
3. **T2 — `0.2C` Reference Capacity (`capacity @4.20 V`):**
   - Discharge at **`0.2C` CC** (`C` = seller nominal `mAh`, e.g. `44 mA` for `220 mAh`, `54 mA` for `270 mAh`, `60 mA` for `300 mAh`) down to **`3.00 V`**.
   - Log `T2.csv`. Integrated `mAh` out = **`capacity @4.20 V`**. Recharge via **T1** and rest `10 min`.
4. **T3 — Continuous `1.5 A` Discharge (D17 Worst-Case):**
   - From full (`4.20 V`), discharge at **`1.50 A` CC** down to **`3.00 V`**.
   - Log `T3.csv` every **`1 s`** (`temp_C` every `1 s` if automated, or every `30 s` manually leaving intermediate rows blank). Recharge via **T1** before T4/T5.
5. **T4 — `3.0 A` Pulse Headroom (at `~50%` and `~20%` SoC):**
   - Discharge at `0.5C` (or `1.5 A` timed) to remove `~50%` of `T2` capacity (`T4_50.csv`), rest `60 s`, then run **`10 × (3.0 A for 10 s, rest 20 s)`**.
   - Continue discharging to `~20%` SoC remaining (`T4_20.csv`), rest `60 s`, and repeat **`10 × (3.0 A for 10 s, rest 20 s)`**.
   - Log at `≤ 1 s` interval; abort immediately if `V < 2.90 V` or `T > 60 °C`.
6. **T5 — DC Internal Resistance (`DCIR` at `50%` SoC):**
   - Starting from a fresh charge, discharge to **`50%` SoC** (`0.5 × T2` capacity), rest **`60 s`**, record `V_rest`, then apply **`1.50 A` CC** for at least `2 s` while logging `T5.csv` at `≤ 1 s`.
   - Compute:
     $$R_{\text{DC}} = \frac{V_{\text{rest}} - V_{\text{load\_at\_1s}}}{I}$$
7. **T6 — Cycle Repeat & Swelling Check:**
   - Repeat **T1 + T3** twice more (`T6_2.csv` = cycle 2, `T6_3.csv` = cycle 3 at `1.50 A` CC to `3.00 V`).
   - After cycle 3 cools to ambient, re-measure thickness **`T_post` (`mm`)** and record in `meta.json`.

---

## d. Pass / Fail Criteria (Tied to D17 & `HY2120-CB`)

| Test | Criterion | Threshold | Rationale |
|---|---|---|---|
| **T2 Capacity** | `capacity @4.20 V` | **`≥ 85%`** of nominal `mAh` | Confirms usable capacity when LiPo or `4.35 V` LiHV cells are charged only to `4.20 V`. |
| **T3 Voltage** | `V ≥ 3.30 V` delivery | **`≥ 80%`** of `T2` capacity before `V` drops `< 3.30 V` | Keeps 2S pack `≥ 6.60 V` under `1.5 A` load (clean margin above `6.0 V` empty / `SY8205FCC` dropout). |
| **T3 Thermal** | Temp rise & peak | **`ΔT ≤ 15 °C`** over ambient **AND** **`T_peak ≤ 50 °C`** | Temple thermal comfort and `10 °C` safety margin below `60 °C` abort limit. |
| **T4 Pulse** | `3.0 A / 10 s` sag | **`V_min ≥ 3.00 V`** at both `50%` and `20%` SoC | Stays above `HY2120-CB` UVP (`2.90 ± 0.08 V`) during `3 A` burst headroom. |
| **T5 DCIR** | DC internal resistance | **`DCIR ≤ 100 mΩ`** per cell | Limits 2S resistive sag at `1.5 A` to `2 × 0.10 Ω × 1.5 A = 0.30 V ≤ 0.3 V`. |
| **T6 Stability** | Swelling & fade | Thickness growth **`≤ 5%`**, capacity change **`≤ 3%`** across 3 cycles | Rejects cells that puff or fade rapidly at `1.5 A` (`5C–7.5C`). |
| **Pair Match** | Best 2S pair delta | **`≤ 2%`** capacity difference **AND** **`≤ 10 mΩ`** DCIR difference | Prevents cell imbalance under `IP2326_NPD` 2S charging and `HY2120-CB` cutoffs. |

- **Model Verdict:** A cell model **PASSES** only if **`≥ 3` of `4` cells pass all per-cell rules** AND at least one passing pair satisfies **Pair Match**. Select the passing pair with the smallest DCIR delta (tie-break: smallest capacity delta).

---

## e. Data Directory Layout & Atorch DL24 Export Guide

### Folder & File Layout
```text
tests/battery/<model>/
  C1/
    meta.json
    T1.csv
    T2.csv
    T3.csv
    T4_50.csv
    T4_20.csv
    T5.csv
    T6_2.csv
    T6_3.csv
  C2/ ...
  C3/ ...
  C4/ ...
```

- **CSV Header (exact):** `time_s,voltage_V,current_A,temp_C`
  - `time_s`: elapsed seconds (numeric, e.g. `0, 1, 2, ...`).
  - `voltage_V`: cell terminal voltage in Volts (`float`).
  - `current_A`: positive magnitude in Amps (`float`, e.g. `1.50` during `1.5 A` discharge).
  - `temp_C`: body temperature in `°C` (`float`), or **blank** between `30 s` manual readings (`12,3.84,1.50,`).
- **`meta.json` Schema (required in every cell folder):**
```json
{
  "model": "Tattu_220mAh_1S_45C",
  "cell_id": "C1",
  "date": "2026-11-29",
  "ambient_C": 25.0,
  "nominal_mAh": 220.0,
  "synthetic": false,
  "equipment": {
    "charger": "ISDT Q6 Nano",
    "load": "Atorch DL24P",
    "thermocouple": "K-type probe",
    "scale": "0.01g scale",
    "caliper": "0.01mm digital"
  },
  "incoming": {
    "photo": "C1_incoming.jpg",
    "label_text": "TATTU 220mAh 3.7V 45C",
    "mass_g": 5.52,
    "L_mm": 51.2,
    "W_mm": 12.0,
    "T_init_mm": 6.02,
    "T_post_mm": 6.10,
    "v_ocv_V": 3.84,
    "charger_ir_mOhm": 42.0
  }
}
```
> **Important:** `synthetic` MUST be `false` for all physical bench tests (`true` is reserved strictly for unit tests). `scripts/battery_bench_analyze.py` refuses to run if `meta.json` is missing or if `synthetic` does not match the CLI mode.

### Exporting from an Atorch DL24 / E-Test PC App
1. Connect the DL24/DL24P via USB-UART or Bluetooth to the **E-Test PC app** (or Bluetooth CSV logger).
2. Set logging interval to **`1 s`** and click **Record / Export CSV** after each test (`T2`, `T3`, `T4_50`, `T4_20`, `T5`, `T6_2`, `T6_3`).
3. Convert the exported table to the canonical 4-column CSV:
   - Keep/rename columns to `time_s,voltage_V,current_A,temp_C`.
   - Convert timestamp (`HH:MM:SS` or `ms`) to elapsed seconds starting at `0`.
   - If the DL24 app logs its heatsink NTC instead of your cell-body probe, clear `temp_C` and fill in your `30 s` cell-body thermocouple readings at matching `time_s` rows (leaving other rows blank).
4. Run the analyzer:
   ```bash
   python3 scripts/battery_bench_analyze.py tests/battery/<model>
   ```
   This generates `tests/battery/<model>/report.json` and `tests/battery/<model>/report.md`.
