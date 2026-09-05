# Reproducibility guide

## Scope

This repository supports three levels of reproduction:

1. **Public verification** checks the manuscript, figures, registrations, verdict reports, code and hashes, and runs the unit tests.
2. **Re-scoring from saved evaluator inputs** regenerates the pre-registered lineage and second-architecture verdicts, and the whole reconstruction model, from files shipped here.
3. **Full regeneration** re-runs the neural simulations with `lab.py` and `replicate.py`. The per-seed run files behind Version 2.0 total about 3 GB and are not in this repository or in the Zenodo archive; they can be provided on request.

Nothing here needs licensed data or network access. Everything runs on a CPU.

## Tested environment

Version 2.0 was built on macOS with Python 3.14.6, PyTorch 2.12 to 2.14, NumPy 2.4, SciPy 1.18 and Matplotlib 3.11. The scripts use standard-library features available in Python 3.11 or later.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Level 1: public verification

```bash
python verify_manifest.py --check           # every file against public_manifest.json (SHA-256)
python -m compileall -q replication          # syntax of every script
cd replication && python tests.py            # 31 checks; needs torch; under a minute
```

`tests.py` covers the world sampler (no duplicate distractors), the tie-corrected Spearman used for topographic similarity, the record mechanics, the v2 result files in `replication/results/`, and the corrected adjusted Rand index in `metrics.py` (identical singleton partitions score 1, as in the standard definition; Version 1.0 scored them 0).

## Level 2: re-scoring from shipped inputs

All commands run from `replication/`. `corrections_v2/rerun.py` executes an evaluator with every write redirected into `corrections_v2/recomputed/`, so shipped reports are never overwritten. After each command, compare the regenerated file with the shipped one; in our checks they are byte-identical.

| Command | Regenerates | Reads |
| --- | --- | --- |
| `python model_v2.py` | `results_model/toy_results_v2.md`, `results_model/t4_v2_per_seed.json` (corrected T4, measured T2 move cost) | nothing saved; the model is rebuilt from its seeds |
| `python corrections_v2/rerun.py probe46.py` | K14, K16, K17a to K17c on the confirmation cohort | `results_v3_confirm2/k14_raw.json`, `k16_raw.json`, `k17_raw.json` |
| `K_OUT=results_replicate K_SEEDS=100..119 python corrections_v2/rerun.py probe46.py` | the same tests on the replication cohort | `results_replicate/k14_k17_power_raw.json` |
| `K_ARCH=gumbel K_OUT=results_arch K_SEEDS=100..119 python corrections_v2/rerun.py probe46.py` | A1 to A4 (second architecture); also `results_arch2`, `results_arch3` | `results_arch*/k14_k17_power_raw.json` |
| `python corrections_v2/rerun.py confirm8.py` | D1 to D2 (distractor geometry) | `results_degeneracy/d_raw.json` |
| `python corrections_v2/rerun.py probe47.py` | S1 to S3 (one-shot) | `results_oneshot/s_raw.json` |
| `python corrections_v2/rerun.py probe49.py`, `probe42.py`, `probe45.py` | exploratory descriptives cited in the supplement | `results_medium/m2_raw.json`, `results_v3/probe41_raw.json`, `results_v3/probe44_raw.json` |

The `*_raw.json` files are the per-seed, per-cell aggregates that the evaluators consume. Their SHA-256 values as used for Version 2.0 are in `replication/corrections_v2/input_sha256.json`.

## Level 3: full regeneration

The following need the per-seed run files (`results_*/<cell>_seed<N>.json`, hundreds of megabytes per cohort), which are not shipped:

- `confirm2.py`, `confirm2b.py` (K8 to K13), `confirm3.py` (K13a, K13b), `confirm4.py` (K18), `confirm5.py`, `confirm6.py`, `confirm7.py` (M1 to M4), `probe39.py`, `probe41.py`, `probe43.py`, `probe44.py`;
- `figures.py`, which builds Figures 1 to 4 from the run files and writes `figure_stats.json`.

**Warning.** Several of these evaluators do not stop when the run files are absent: they write a table with n = 0 and "UNDERPOWERED" labels. Do not read such a table as a result. `confirm4.py` exits with an explicit message in that case.

To regenerate the runs:

```bash
cd replication
python lab.py run --help                       # the factorial channel lab (select, slots, fresh, capacity, noise, reader)
python replicate.py --seeds 100..119 --out results_replicate --workers 8
```

`replicate.py` sweeps the four confirmation families and the cap-19 partner cells, runs the child, sibling and snapshot experiments (K14, K16, K17), and evaluates them with the thresholds in `manifest_k.json`. Known limits, stated in the supplement (S5): the driver was tested on seeds 100 to 119 only, some evaluators keep hardcoded seed ranges and file names from the original cohorts, and reproducing K8 to K13 on a fresh cohort requires running `lab.py` for the confirmation cells and then pointing `confirm2.py` and `confirm2b.py` at the output directory with `K_OUT`. A full cohort takes several hours on an 8-core CPU.

Figures regenerate with `FIG_OUT=../figures python figures.py` once the discovery and confirmation run files are present. The shipped `figures/figure_stats.json` records every plotted statistic so that a regenerated figure can be compared number by number.

## What Version 2.0 changed and how it was checked

`replication/CHANGELOG_v2.md` lists every change with its reason. `replication/corrections_v2/` holds the original Version 1.0 reports (`originals/`), the re-scored reports (`recomputed/`), the hashes of every input (`input_sha256.json`) and the working notes. `verification/` holds the independent verification that triggered the corrections, including its own independent implementation of the metric and its recomputed values (`independent_results.json`). The metric correction was cross-checked against that implementation on 500 random partition pairs (maximum difference 1e-16).

## Reporting a reproduction problem

Open a reproduction issue using the repository template. Include the operating system, Python and PyTorch versions, the exact command, the traceback, and the SHA-256 of any shipped input involved.
