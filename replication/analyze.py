"""
Aggregate results/ into a summary table, paired-by-seed comparisons, and a figure.

    python analyze.py [results_dir]   # -> <dir>/summary.md, <dir>/curves.png

Seeds are shared across conditions (same held-out split, same init), so every
comparison between two conditions is PAIRED by seed: we report wins/losses,
mean paired difference with a bootstrap 95% CI, and an exact sign-test p-value.
"""
import glob, json, os, sys
from collections import defaultdict
from itertools import combinations
from math import comb
import numpy as np

out = sys.argv[1] if len(sys.argv) > 1 else "results"
runs = defaultdict(dict)          # condition -> seed -> log
configs = []
for p in sorted(glob.glob(os.path.join(out, "*_seed*.json"))):
    d = json.load(open(p))
    runs[d["config"]["condition"]][d["config"]["seed"]] = d["log"]
    configs.append(d["config"])
if not runs:
    sys.exit("no results found")

# Guard against mixing incompatible runs in one folder (this bit us once: v1 JSONs
# have `transmit_frac`, v2 have `n_transmit`). Refuse to produce a blended summary.
def sig(c):
    return (c.get("n_attrs"), c.get("n_vals"), c.get("vocab"), c.get("msg_len"),
            c.get("steps"), c.get("generations"),
            "v1" if "transmit_frac" in c else "v2")
sigs = {sig(c) for c in configs}
if len(sigs) > 1:
    sys.exit("REFUSING: results dir mixes incompatible runs (different world/steps/schema):\n  "
             + "\n  ".join(map(str, sorted(sigs)))
             + f"\nSeparate them into different --out folders before analyzing '{out}'.")

ORDER = ["pair", "population", "generations", "oral", "oral_fixed", "bone", "bone_edition"]
conds = [c for c in ORDER if c in runs] + [c for c in runs if c not in ORDER]
METRICS = ["train_acc", "test_acc", "topsim", "posdis", "n_unique_msgs"]

def final(cond, key):
    return {s: l[-1][key] for s, l in runs[cond].items()}

def ms(v):
    v = np.asarray(v, float)
    return f"{v.mean():.3f} ± {v.std(ddof=1) if len(v) > 1 else 0:.3f}"

def sign_test(diffs):
    d = np.asarray(diffs); d = d[d != 0]
    n, k = len(d), int((d > 0).sum())
    if n == 0:
        return 1.0
    p_one = sum(comb(n, i) for i in range(max(k, n - k), n + 1)) / 2 ** n
    return min(1.0, 2 * p_one)

def boot_ci(diffs, B=5000, rng=np.random.RandomState(0)):
    d = np.asarray(diffs, float)
    m = np.array([rng.choice(d, len(d)).mean() for _ in range(B)])
    return np.percentile(m, 2.5), np.percentile(m, 97.5)

L = ["# Symbol emergence — summary", "",
     f"Seeds per condition: " + ", ".join(f"{c}={len(runs[c])}" for c in conds), "",
     "Final values (mean ± sd over seeds). test_acc = held-out attribute combinations "
     "(chance = 0.2). topsim = topographic similarity (tie-corrected Spearman). "
     "posdis = positional disentanglement. n_unique_msgs = distinct messages over the 64 objects.", "",
     "| condition | " + " | ".join(METRICS) + " |", "|---|" + "---|" * len(METRICS)]
for c in conds:
    L.append(f"| {c} | " + " | ".join(ms(list(final(c, m).values())) for m in METRICS) + " |")

# ---- paired comparisons ----------------------------------------------------
L += ["", "## Paired-by-seed comparisons (A − B)", "",
      "wins = seeds where A > B. p = two-sided exact sign test. CI = bootstrap 95% of mean difference.", ""]
for m in ["test_acc", "topsim", "n_unique_msgs"]:
    L += [f"### {m}", "", "| A | B | n | wins/ties/losses | mean diff | 95% CI | p |", "|---|---|---|---|---|---|---|"]
    for a, b in combinations(conds, 2):
        fa, fb = final(a, m), final(b, m)
        seeds = sorted(set(fa) & set(fb))
        if len(seeds) < 2:
            continue
        d = np.array([fa[s] - fb[s] for s in seeds])
        lo, hi = boot_ci(d)
        L.append(f"| {a} | {b} | {len(d)} | {(d>0).sum()}/{(d==0).sum()}/{(d<0).sum()} | "
                 f"{d.mean():+.3f} | [{lo:+.3f}, {hi:+.3f}] | {sign_test(d):.3f} |")
    L.append("")

# ---- per-generation trajectories ------------------------------------------
L += ["## Per-generation (end of each generation; mean ± sd over seeds)", ""]
for c in conds:
    gens = sorted({r["gen"] for l in runs[c].values() for r in l})
    if len(gens) < 2:
        continue
    L += [f"### {c}", "| gen | test_acc | topsim | posdis | n_unique_msgs |", "|---|---|---|---|---|"]
    for g in gens:
        vals = defaultdict(list)
        for l in runs[c].values():
            recs = [r for r in l if r["gen"] == g]
            if recs:
                for m in ["test_acc", "topsim", "posdis", "n_unique_msgs"]:
                    vals[m].append(recs[-1][m])
        L.append(f"| {g} | " + " | ".join(ms(vals[m]) for m in ["test_acc", "topsim", "posdis", "n_unique_msgs"]) + " |")
    # slope of topsim across generations (per seed), is it > 0?
    slopes = []
    for l in runs[c].values():
        pts = [(r["gen"], r["topsim"]) for r in l if "language" in r]
        if len(pts) >= 3:
            x, y = zip(*pts); slopes.append(np.polyfit(x, y, 1)[0])
    if slopes:
        s = np.array(slopes)
        L.append(f"\ntopsim slope per generation: {s.mean():+.4f} (positive in {(s>0).sum()}/{len(s)} seeds, sign-test p={sign_test(s):.3f})")
    L.append("")

# ---- speed of re-acquisition ------------------------------------------------
L += ["## Steps to train_acc ≥ 0.9 in the last generation", ""]
for c in conds:
    ts = []
    for l in runs[c].values():
        lg = max(r["gen"] for r in l)
        hit = [r["gen_step"] for r in l if r["gen"] == lg and r["train_acc"] >= 0.9]
        ts.append(hit[0] if hit else np.nan)
    ts = np.array(ts, float)
    L.append(f"- {c}: median {np.nanmedian(ts):.0f} steps (reached in {np.isfinite(ts).sum()}/{len(ts)} seeds)")

open(os.path.join(out, "summary.md"), "w").write("\n".join(L))
print("\n".join(L))

try:
    import matplotlib; matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1, 3, figsize=(16, 4.2))
    for ax, m in zip(axes, ["test_acc", "topsim", "n_unique_msgs"]):
        for c in conds:
            logs = list(runs[c].values())
            steps = [r["step"] for r in logs[0]]
            ys = np.array([[r[m] for r in l] for l in logs if len(l) == len(steps)])
            ax.plot(steps, ys.mean(0), label=c)
            se = ys.std(0, ddof=1) / np.sqrt(len(ys)) if len(ys) > 1 else 0
            ax.fill_between(steps, ys.mean(0) - se, ys.mean(0) + se, alpha=0.15)
        ax.set_title(m + " (mean ± s.e.)"); ax.set_xlabel("training step")
    axes[0].legend(fontsize=8)
    plt.tight_layout(); plt.savefig(os.path.join(out, "curves.png"), dpi=120)
    print("saved", os.path.join(out, "curves.png"))
except ImportError:
    print("matplotlib not installed; skipped figure")
