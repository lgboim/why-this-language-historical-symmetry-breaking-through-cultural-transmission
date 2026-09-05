"""probe46.py — power extension for K14 and K17b on seeds 45-74 (fresh parents), pooled with seeds 30-44.
   python probe46.py -> results_v3_confirm2/k14_k17_power.md"""
import json, os, itertools
import numpy as np, torch
from multiprocessing import Pool
from collections import Counter, defaultdict
from scipy.optimize import linear_sum_assignment
from game import World, Sender, Receiver
from lab import Cell, make_cfg, teach_sender, train_generation, stats_line, fmt, spearman, make_agents
from probe40 import choose, ARMS
GENS = Cell("small", "gens"); N = 64; IU = np.triu_indices(N, 1); import os as _os
_KS = _os.environ.get("K_SEEDS"); _KO = _os.environ.get("K_OUT", "results_v3_confirm2"); _KA = _os.environ.get("K_ARCH", "gru")
def _seeds(default):
    return list(range(int(_KS.split("..")[0]), int(_KS.split("..")[1]) + 1)) if _KS else default
NEW = _seeds(list(range(45, 75))); ALL = NEW if _KS else list(range(30, 75))
from metrics import ari   # shared standard ARI (corrected 2026-09-05; the old local copy returned 0 for identical singleton partitions)
def parent_job(s):
    torch.set_num_threads(1); cfg = make_cfg(GENS, s, steps=2000, eval_every=250, generations=1, save_weights=False, arch=_KA); world = World(3, 4, 0.25, seed=s)
    S_, R_ = make_agents(cfg, world, s * 100); log = []
    train_generation(cfg, world, [S_], [R_], np.random.RandomState(s), None, log, 0, 0, 2000)
    from lab import receiver_decode, sender_language
    msgs, _ = sender_language(S_, world); dec = receiver_decode(R_, world, msgs); L = {r["gen_step"]: r["language"] for r in log}
    return s, L[2000], list(map(int, dec)), [L[k] for k in (1000, 1250, 1500, 1750, 2000)], L[500]
def child_job(args):
    s, arm, init, lang, dec, hist, l500 = args; torch.set_num_threads(1); lang, dec = np.array(lang), np.array(dec); hist = [np.array(h) for h in hist]
    cfg = make_cfg(GENS, s, steps=2000, eval_every=2000, generations=1, save_weights=False, arch=_KA); world = World(3, 4, 0.25, seed=s)
    if arm in ARMS:
        objs = np.array(sorted(choose(arm, world, lang, dec, hist, np.random.RandomState(2000 + s)))); init_seed = s * 100 + 1; L = lang
    else:
        tr = np.array(world.train_idx); init_seed = s * 100 + 50 + init; L = lang
        if arm == "stale": objs = np.sort(np.random.RandomState(3000 + s).choice(tr, 19, replace=False)); L = np.array(l500)
        elif arm in ("fresh", "same"): objs = np.sort(np.random.RandomState(3000 + s).choice(tr, 19, replace=False))
        elif arm == "different": objs = np.sort(np.random.RandomState(3000 + s + 100 * init).choice(tr, 19, replace=False))
        else: objs = np.array([], dtype=int)
    S_, R_ = make_agents(cfg, world, init_seed)
    if len(objs): teach_sender(cfg, world, S_, objs, L[objs])
    log = []
    train_generation(cfg, world, [S_], [R_], np.random.RandomState(s if arm in ARMS else s + 7 * init), None, log, 1, 0, 2000); return s, arm, init, log[-1]["language"]
if __name__ == "__main__":
    raw = f"{_KO}/k14_k17_power_raw.json"
    if os.path.exists(raw): P, res = json.load(open(raw)); P = {int(k): v for k, v in P.items()}
    else:
        with Pool(8) as p: P = {s: (lf, d, h, l5) for s, lf, d, h, l5 in p.map(parent_job, NEW)}
        jobs = [(s, arm, 0, *P[s]) for s in NEW for arm in ARMS] + [(s, arm, i, *P[s]) for s in NEW for arm in ("stale", "fresh", "different", "none") for i in (1, 2)]
        with Pool(8) as p: res = p.map(child_job, jobs)
        json.dump([{str(k): v for k, v in P.items()}, res], open(raw, "w"))
    # pool with seeds 30-44
    K14P, K14R = json.load(open("results_v3_confirm2/k14_raw.json")); K17P, K17R = json.load(open("results_v3_confirm2/k17_raw.json"))
    lang14 = {(s, arm): np.array(l) for s, arm, objs, l, d, ta in K14R}; lang14.update({(s, arm): np.array(l) for s, arm, i, l in res if arm in ARMS})
    sib = {(s, arm, i): np.array(l) for s, arm, i, l in K17R}; sib.update({(s, arm, i): np.array(l) for s, arm, i, l in res if arm in ("stale", "fresh", "different", "none")})
    par = {int(s): (np.array(v[0]), None) for s, v in K14P.items()}; par.update({s: (np.array(P[s][0]), np.array(P[s][3])) for s in NEW})
    for s, v in K17P.items(): par[int(s)] = (par[int(s)][0], np.array(v[0]))
    worlds = {s: World(3, 4, 0.25, seed=s) for s in ALL}; OD = {s: (worlds[s].objects[:, None, :] != worlds[s].objects[None, :, :]).sum(-1)[IU] for s in ALL}
    def tsd(s, lang): md = (lang[:, None, :] != lang[None, :, :]).sum(-1)[IU]; k = md > 0; return spearman(OD[s][k], md[k]) if k.sum() > 2 else np.nan
    def cbm(lang, w):
        M = np.zeros((24, 12))
        for o in range(N):
            for p in range(3):
                for a in range(3): M[p * 8 + lang[o, p], a * 4 + w.objects[o, a]] += 1
        r, c = linear_sum_assignment(-M); return M[r, c].sum() / (N * 3)
    O = [f"# K14 + K17b power extension: seeds 30–74 pooled (n = {len(ALL)})", "", "## K14 (thresholds unchanged: |Δtopsim_distinct| < 0.03 AND |ΔCBM| < 0.02; ≥3/4)", "", "| rule | Δ topsim_distinct | | | | | | Δ CBM | | | | | | verdict |", "|---|" + "---|" * 13]
    ok = 0
    for arm in ARMS[1:]:
        dt = np.array([tsd(s, lang14[(s, arm)]) - tsd(s, lang14[(s, "random19")]) for s in ALL]); dc = np.array([cbm(lang14[(s, arm)], worlds[s]) - cbm(lang14[(s, "random19")], worlds[s]) for s in ALL])
        v = abs(dt.mean()) < 0.03 and abs(dc.mean()) < 0.02; ok += v; O.append(f"| {arm} " + fmt(stats_line(dt, "?")) + " " + fmt(stats_line(dc, "?")) + f" {'not different' if v else 'DIFFERENT'} |")
    O.append(f"\nK14: {ok}/4 → {'SUPPORTED' if ok >= 3 else 'FAILED'}")
    cp = []
    for s in ALL:
        tr = worlds[s].train_idx; lf = par[s][0]; Pt = lambda l: [tuple(l[o]) for o in tr]
        f = (ari(Pt(sib[(s, "fresh", 1)]), Pt(lf)) + ari(Pt(sib[(s, "fresh", 2)]), Pt(lf))) / 2; st = (ari(Pt(sib[(s, "stale", 1)]), Pt(lf)) + ari(Pt(sib[(s, "stale", 2)]), Pt(lf))) / 2; cp.append(f - st)
    O += ["", "## K17b (fresh − stale child–parent ARI > 0, ≥80% seeds, CI > 0)", "", fmt(stats_line(np.array(cp), ">"))]
    ssd, c5d, k16p, k16s = [], [], [], []
    for s in ALL:
        tr = worlds[s].train_idx; lf = par[s][0]; l5 = par[s][1]; Pt = lambda l: [tuple(l[o]) for o in tr]
        if l5 is None or (s, "different", 1) not in sib: continue
        sib_ari = lambda arm: ari(Pt(sib[(s, arm, 1)]), Pt(sib[(s, arm, 2)]))
        ssd.append(sib_ari("stale") - sib_ari("fresh")); c5d.append(np.mean([ari(Pt(sib[(s, "stale", i)]), Pt(l5)) - ari(Pt(sib[(s, "fresh", i)]), Pt(l5)) for i in (1, 2)]))
        k16p.append(sib_ari("fresh") - sib_ari("different")); k16s.append(sib_ari("different") - sib_ari("none"))
    if ssd:
        st = stats_line(np.array(ssd), "?")
        O += ["", "## K17a (sibling ARI stale − fresh; equivalence: mean ≥ −0.05 and CI lower ≥ −0.10)", "", fmt(st) + (" → SUPPORTED" if st["mean"] >= -0.05 and st["lo"] >= -0.10 else " → FAILED"),
              "", "## K17c (child–step-500 ARI stale − fresh > 0)", "", fmt(stats_line(np.array(c5d), ">")),
              "", "## K16 (sibling ARI: same − different (primary); different − none (secondary))", "", "primary: " + fmt(stats_line(np.array(k16p), ">")), "secondary: " + fmt(stats_line(np.array(k16s), ">"))]
    open(f"{_KO}/k14_k17_power.md", "w").write("\n".join(O) + "\n"); print("\n".join(O))
