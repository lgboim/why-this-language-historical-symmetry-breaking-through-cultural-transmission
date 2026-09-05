"""model_v2.py — corrected T4 (frozen founder early partition) and a measured T2 move cost, per results_model/T4_correction_design.md.
Everything else (world, energy, reconstruct, seeds, random streams) is imported unchanged from model.py's definitions; model.py itself is
left untouched as the record of the original run. Writes results_model/toy_results_v2.md and results_model/t4_v2_per_seed.json.
python3 model_v2.py"""
import json, numpy as np
import model_core as M                # definitions only: does NOT re-run the original simulation or touch results_model/toy_results.md
from metrics import ari
N, NB, C, LAM, W = M.N, M.NB, M.C, M.LAM, M.W
SEEDS = range(20)
parents = {s: M.reconstruct({}, np.random.RandomState(1000 + s)) for s in SEEDS}          # founders (same as model.py)
early = {s: M.reconstruct({}, np.random.RandomState(1000 + s), sweeps=1) for s in SEEDS}  # the founder's frozen early partition (as in T3)
O = ["# Toy model — corrected T4 and measured T2 move cost (20 seeds; design fixed in T4_correction_design.md before running)", ""]
O.append(f"founder vs its own early partition: ARI {np.mean([ari(early[s], parents[s]) for s in SEEDS]):.3f}")
# ---- T4 corrected: accumulate = anchors resampled each generation from the FROZEN early partition of the founder
dec = {"rewrite": [], "accumulate": []}
for s in SEEDS:
    for mode in dec:
        P = parents[s]; founder = P; rng = np.random.RandomState(500 + s); traj = []
        for g in range(1, 6):
            src = P if mode == "rewrite" else early[s]                                   # the one corrected line
            A = M.anchors_from(src, rng.choice(N, 19, replace=False)); P = M.reconstruct(A, np.random.RandomState(300 + 10 * s + g)); traj.append(ari(P, founder))
        dec[mode].append(traj)
R = np.array(dec["rewrite"]); Acc = np.array(dec["accumulate"]); d5 = R[:, 4] - Acc[:, 4]
rng = np.random.default_rng(0); bt = [rng.choice(d5, len(d5)).mean() for _ in range(5000)]
O += ["", "## T4 (corrected): ARI to the founder by generation, mean over 20 seeds", "| record | g1 | g2 | g3 | g4 | g5 |", "|---|---|---|---|---|---|",
      "| rewrite (anchors from the current parent's final partition) | " + " | ".join(f"{v:.3f}" for v in R.mean(0)) + " |",
      "| accumulate (anchors from the founder's FROZEN early partition) | " + " | ".join(f"{v:.3f}" for v in Acc.mean(0)) + " |",
      "", f"g5 paired difference rewrite − accumulate: {d5.mean():+.3f} [{np.percentile(bt, 2.5):+.3f}, {np.percentile(bt, 97.5):+.3f}] (5,000 paired bootstrap resamples); "
      f"rewrite higher in {int((d5 > 0).sum())}/20, lower in {int((d5 < 0).sum())}/20, tied {int((d5 == 0).sum())}",
      "per-generation mean differences rewrite − accumulate: " + ", ".join(f"g{g+1} {v:+.3f}" for g, v in enumerate((R - Acc).mean(0))),
      "Descriptive; no threshold was registered for T4. A higher endpoint is not by itself a slower decay rate.",
      "", "Original (invalid for this claim) implementation drew a fresh unrelated shallow partition each generation: rewrite 0.466, 0.314, 0.327, 0.242, 0.198; accumulate 0.263, 0.196, 0.194, 0.158, 0.157 (results_model/toy_results.md)."]
# ---- T2 move cost, measured: for each untaught object o with an anchored Hamming-1 neighbour a, the greedy ΔE of moving o into a's class in the converged child
def delta_E(P, o, new):
    old = P[o]
    if new == old: return 0.0
    cnt = {}
    for lab in P: cnt[lab] = cnt.get(lab, 0) + 1
    m_dest = cnt.get(new, 0); m_src = cnt[old]
    d_within = C * (m_dest - (m_src - 1))
    d_classes = LAM * ((1 if m_dest == 0 else 0) - (1 if m_src == 1 else 0))
    d_cut = W * (sum(1 for j in NB[o] if P[j] != new) - sum(1 for j in NB[o] if P[j] != old))
    return d_within + d_classes + d_cut
dE = {"same-class anchor": [], "other-class anchor": []}; joined = {"same-class anchor": [], "other-class anchor": []}
for s in SEEDS:
    P = parents[s]; rng = np.random.RandomState(s); objs = rng.choice(N, 19, replace=False); A = M.anchors_from(P, objs); child = M.reconstruct(A, np.random.RandomState(77 + s))
    for o in range(N):
        if o in A: continue
        for a in NB[o]:
            if a not in A: continue
            k = "same-class anchor" if P[a] == P[o] else "other-class anchor"
            dE[k].append(delta_E(child, o, child[a])); joined[k].append(child[o] == child[a])
O += ["", "## T2 move cost, measured at the converged child (untaught object o, anchored Hamming-1 neighbour a)", "| anchor | n pairs | share of o already in a's class | mean ΔE of moving o into a's class (if not there) | share with ΔE ≤ 0 |", "|---|---|---|---|---|"]
for k in dE:
    e = np.array(dE[k]); j = np.array(joined[k]); e_not = e[~j]
    O.append(f"| {k} | {len(e)} | {j.mean():.2f} | {e_not.mean() if len(e_not) else float('nan'):+.2f} | {(e_not <= 0).mean() if len(e_not) else float('nan'):.2f} |")
O += ["", "ΔE = c·(m_dest − (m_src − 1)) + λ·Δ#classes + w·Δ#cut edges, with c = 1, λ = 6, w = 1. This replaces the published verbal claim that the marginal within-class cost is 'below w'."]
open("results_model/toy_results_v2.md", "w").write("\n".join(O) + "\n"); print("\n".join(O))
json.dump({"rewrite": R.tolist(), "accumulate": Acc.tolist(), "seeds": list(SEEDS)}, open("results_model/t4_v2_per_seed.json", "w"))
