"""confirm8.py — A3'/A4' (form-level) on the Gumbel learner, pooled over all results_arch* raw files with seeds >= 120."""
import glob, json, numpy as np
from game import World
from lab import stats_line, fmt
P, sib = {}, {}
for f in sorted(glob.glob("results_arch*/k14_k17_power_raw.json")):
    Pp, res = json.load(open(f)); P.update({int(k): v for k, v in Pp.items() if int(k) >= 120}); sib.update({(s, arm, i): np.array(l) for s, arm, i, l in res if s >= 120})
seeds = sorted(P); ag = lambda s, a, b: np.mean([(a[o] == b[o]).all() for o in World(3, 4, 0.25, seed=s).train_idx])
same = {s: ag(s, sib[(s, "fresh", 1)], sib[(s, "fresh", 2)]) for s in seeds}; diff = {s: ag(s, sib[(s, "different", 1)], sib[(s, "different", 2)]) for s in seeds}; none = {s: ag(s, sib[(s, "none", 1)], sib[(s, "none", 2)]) for s in seeds}
stale = {s: ag(s, sib[(s, "stale", 1)], sib[(s, "stale", 2)]) for s in seeds}
t5s = {s: np.mean([ag(s, sib[(s, "stale", i)], np.array(P[s][3])) for i in (1, 2)]) for s in seeds}; t5f = {s: np.mean([ag(s, sib[(s, "fresh", i)], np.array(P[s][3])) for i in (1, 2)]) for s in seeds}
st = stats_line(np.array([stale[s] - same[s] for s in seeds]), "?")
O = [f"# A3'/A4' form-level, Gumbel, seeds {seeds[0]}–{seeds[-1]} (n={len(seeds)})", "", f"form agreement: same {np.mean(list(same.values())):.2f}, different {np.mean(list(diff.values())):.2f}, none {np.mean(list(none.values())):.2f}; stale siblings {np.mean(list(stale.values())):.2f}; to step-500 forms stale {np.mean(list(t5s.values())):.2f} / fresh {np.mean(list(t5f.values())):.2f}",
     "A3' primary same − different: " + fmt(stats_line(np.array([same[s] - diff[s] for s in seeds]), ">")), "A3' secondary different − none: " + fmt(stats_line(np.array([diff[s] - none[s] for s in seeds]), ">")),
     "A4' target stale − fresh (to step-500 forms): " + fmt(stats_line(np.array([t5s[s] - t5f[s] for s in seeds]), ">")), "A4' strength stale − fresh siblings: " + fmt(st) + (" → SUPPORTED" if st["mean"] >= -0.05 and st["lo"] >= -0.10 else " → FAILED")]
open("results_arch/confirmation8.md", "w").write("\n".join(O) + "\n"); print("\n".join(O))
