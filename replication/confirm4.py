"""confirm4.py — K18 lineage persistence on a fresh sweep (default results_replicate).   K_OUT / K_SEEDS env as in the other evaluators."""
import glob, json, os, numpy as np
from collections import Counter
from game import World
from lab import Cell, stats_line, fmt
_KO = os.environ.get("K_OUT", "results_replicate"); _KS = os.environ.get("K_SEEDS"); N = 64
LOGS = {}
for p in glob.glob(f"{_KO}/*_seed*.json"):
    j = json.load(open(p)); LOGS[(Cell(**j["config"]["cell"]), j["config"]["seed"])] = j["log"]
seeds = sorted({s for _, s in LOGS}); worlds = {s: World(3, 4, 0.25, seed=s) for s in seeds}
from metrics import ari   # shared standard ARI (corrected 2026-09-05; the old local copy returned 0 for identical singleton partitions)
def cell(sel, fr): return Cell("small", "gens", sel, "fixed" if sel == "random" else "dynamic", fr, 19, 0.0, "sender")
def a05(c, s):
    E = [r for r in LOGS[(c, s)] if "per_obj_acc" in r]; tr = worlds[s].train_idx; return ari([tuple(np.array(E[0]["language"])[o]) for o in tr], [tuple(np.array(E[-1]["language"])[o]) for o in tr])
rw = {s: np.mean([a05(cell(sel, "rewrite"), s) for sel in ("random", "success") if (cell(sel, "rewrite"), s) in LOGS]) for s in seeds if any((cell(sel, "rewrite"), s) in LOGS for sel in ("random", "success"))}
ac = {s: np.mean([a05(cell(sel, "accumulate"), s) for sel in ("random", "success") if (cell(sel, "accumulate"), s) in LOGS]) for s in seeds if any((cell(sel, "accumulate"), s) in LOGS for sel in ("random", "success"))}
ks = sorted(set(rw) & set(ac)); d = np.array([rw[s] - ac[s] for s in ks])
if len(ks) == 0: raise SystemExit(f"confirm4.py: no gen0/gen5 lineage data for K18 in {_KO} (seeds {_KS or 'default'}); K18 is evaluated on results_replicate only")
O = [f"# K18 on {_KO} (seeds {ks[0]}–{ks[-1]}, n={len(ks)})", "", "K18a rewrite − accumulate ARI(gen0, gen5), cap 19: " + fmt(stats_line(d, ">")),
     f"K18b persistence without permanence: rewrite mean {np.mean([rw[s] for s in ks]):.3f} (> 0.10: {np.mean([rw[s] for s in ks]) > 0.10}); accumulate mean {np.mean([ac[s] for s in ks]):.3f} (< 0.10: {np.mean([ac[s] for s in ks]) < 0.10})"]
open(f"{_KO}/confirmation4.md", "w").write("\n".join(O) + "\n"); print("\n".join(O))
