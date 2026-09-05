"""probe44.py — where the basin comes from.   python probe44.py -> results_v3/probe44.md
 A stale anchors still break symmetry? siblings taught the parent's STEP-500 snapshot (same 19 objects) vs its FINAL language (runs: 30 seeds × 2 inits × 2 arms)
 B founder-specific or world-generic attractor? ARI between final languages: different cells same seed / same cell different seeds / gen0 vs gen5 across seeds
 C basin depth vs anchor density: sibling agreement on untaught objects by number of same-class anchors and by distance to nearest anchor"""
import glob, itertools, json, os
import numpy as np, torch
from multiprocessing import Pool
from collections import Counter, defaultdict
from game import World, Sender, Receiver
from lab import Cell, make_cfg, teach_sender, train_generation, stats_line, fmt, SELECTS, FRESHES
GENS = Cell("small", "gens"); N = 64
from metrics import ari as _ari_std   # shared standard ARI (corrected 2026-09-05)
def ari(a, b): return np.nan if len(a) < 4 else _ari_std(a, b)
def gen0(s):
    f = glob.glob(f"results_v3/*_seed{s}.json") + glob.glob(f"results_v3_confirm/*_seed{s}.json"); j = json.load(open(f[0])); L = {r["gen_step"]: np.array(r["language"]) for r in j["log"] if r["gen"] == 0}; return L[500], L[2000]
def job(args):
    s, arm, init = args; torch.set_num_threads(1); cfg = make_cfg(GENS, s, steps=2000, eval_every=2000, generations=1, save_weights=False)
    world = World(3, 4, 0.25, seed=s); l500, lfin = gen0(s); lang = l500 if arm == "stale" else lfin; objs = np.sort(np.random.RandomState(3000 + s).choice(np.array(world.train_idx), 19, replace=False))
    torch.manual_seed(s * 100 + 50 + init); S_, R_ = Sender(world.dim, 8, 3, 64), Receiver(world.dim, 8, 64); teach_sender(cfg, world, S_, objs, lang[objs])
    log = []; train_generation(cfg, world, [S_], [R_], np.random.RandomState(s + 7 * init), None, log, 1, 0, 2000); return s, arm, init, log[-1]["language"]
if __name__ == "__main__":
    raw = "results_v3/probe44_raw.json"
    if os.path.exists(raw): res = [tuple(x) for x in json.load(open(raw))]
    else:
        with Pool(8) as p: res = p.map(job, [(s, arm, i) for s in range(30) for arm in ("stale", "fresh") for i in (1, 2)])
        json.dump(res, open(raw, "w"))
    worlds = {s: World(3, 4, 0.25, seed=s) for s in range(30)}; TR = {s: np.isin(np.arange(N), worlds[s].train_idx) for s in range(30)}
    SD = {s: (worlds[s].objects[:, None, :] != worlds[s].objects[None, :, :]).sum(-1) for s in range(30)}
    R = {(s, arm, i): np.array(l) for s, arm, i, l in res}
    O = ["# probe44 — where the basin comes from", ""]
    # A
    O += ["## A. Stale vs fresh anchors (same 19 objects; 30 seeds; two independent siblings per arm): sibling–sibling ARI, child–parent(final) ARI, child–snapshot(500) ARI; staleness of the taught forms", "", "| arm | taught forms ≠ parent final | ARI sib–sib | ARI child–parent final | ARI child–step-500 | sib−parent: seeds > 0 |", "|---|---|---|---|---|---|"]
    V = {}
    for arm in ("fresh", "stale"):
        ss, cp, c5, st, w = [], [], [], [], 0
        for s in range(30):
            l500, lfin = gen0(s); tr = worlds[s].train_idx; a, b = R[(s, arm, 1)], R[(s, arm, 2)]; objs = np.sort(np.random.RandomState(3000 + s).choice(np.array(tr), 19, replace=False))
            st.append(np.mean([(l500[o] != lfin[o]).any() for o in objs]) if arm == "stale" else 0.0)
            P = lambda l: [tuple(l[o]) for o in tr]; x = ari(P(a), P(b)); y = (ari(P(a), P(lfin)) + ari(P(b), P(lfin))) / 2; ss.append(x); cp.append(y); c5.append((ari(P(a), P(l500)) + ari(P(b), P(l500))) / 2); w += x > y
        V[arm] = (np.array(ss), np.array(cp)); O.append(f"| {arm} | {np.mean(st):.2f} | {np.mean(ss):.3f} | {np.mean(cp):.3f} | {np.mean(c5):.3f} | {w}/30 |")
    O += ["", "sibling ARI, stale − fresh: " + fmt(stats_line(V["stale"][0] - V["fresh"][0], "?")), "child–parent ARI, stale − fresh: " + fmt(stats_line(V["stale"][1] - V["fresh"][1], "<")), ""]
    # B
    LOGS = {}
    for d in ("results_v3", "results_v3_confirm"):
        for p in glob.glob(os.path.join(d, "*_seed*.json")):
            j = json.load(open(p)); LOGS[(Cell(**j["config"]["cell"]), j["config"]["seed"])] = j["log"]
    def cell(sel, fr): return Cell("small", "gens", sel, "fixed" if sel == "random" else "dynamic", fr, 19, 0.0, "sender")
    FC = [cell(a, b) for a, b in itertools.product(SELECTS, FRESHES)]
    def fin(c, s): tr = worlds[s].train_idx; return [tuple(np.array(LOGS[(c, s)][-1]["language"])[o]) for o in tr]
    def g0(c, s): tr = worlds[s].train_idx; r = [x for x in LOGS[(c, s)] if x["gen"] == 0][-1]; return [tuple(np.array(r["language"])[o]) for o in tr]
    same_seed, diff_seed, g05_same, g05_diff = [], [], [], []
    for s in range(30):
        for c1, c2 in itertools.combinations(FC, 2):
            if (c1, s) in LOGS and (c2, s) in LOGS: same_seed.append(ari(fin(c1, s), fin(c2, s)))
        for c in FC:
            if (c, s) in LOGS: g05_same.append(ari(g0(c, s), fin(c, s)))
    # different seeds: train sets differ, so compare on the intersection of train objects
    rng = np.random.RandomState(0)
    for _ in range(600):
        s1, s2 = rng.choice(30, 2, replace=False); c = FC[rng.randint(len(FC))]
        if (c, s1) not in LOGS or (c, s2) not in LOGS: continue
        common = sorted(set(worlds[s1].train_idx) & set(worlds[s2].train_idx)); l1, l2 = np.array(LOGS[(c, s1)][-1]["language"]), np.array(LOGS[(c, s2)][-1]["language"])
        diff_seed.append(ari([tuple(l1[o]) for o in common], [tuple(l2[o]) for o in common]))
        r0 = [x for x in LOGS[(c, s1)] if x["gen"] == 0][-1]; l0 = np.array(r0["language"]); g05_diff.append(ari([tuple(l0[o]) for o in common], [tuple(l2[o]) for o in common]))
    O += ["## B. Founder-specific or world-generic? ARI between FINAL languages (train objects)", "", "| comparison | n | ARI |", "|---|---|---|",
          f"| different channels, same founder (same seed) | {len(same_seed)} | {np.mean(same_seed):.3f} |", f"| same channel, different founders (different seeds; common train objects) | {len(diff_seed)} | {np.mean(diff_seed):.3f} |",
          f"| gen 0 → gen 5, same lineage | {len(g05_same)} | {np.mean(g05_same):.3f} |", f"| gen 0 of seed A → gen 5 of seed B | {len(g05_diff)} | {np.mean(g05_diff):.3f} |", ""]
    # C
    Rs = {}
    for f in ("results_v3/probe41_raw.json", "results_v3_confirm2/k16_raw.json"):
        for s, arm, i, l in json.load(open(f)):
            if arm == "same": Rs[(s, i)] = np.array(l)
    _P = json.load(open("results_v3_confirm2/k14_raw.json"))[0]
    def parent_lang(s): return np.array(_P[str(s)][0]) if s >= 30 else gen0(s)[1]
    W = {s: World(3, 4, 0.25, seed=s) for s in range(45)}; SDa = {s: (W[s].objects[:, None, :] != W[s].objects[None, :, :]).sum(-1) for s in range(45)}
    by_k, by_d = defaultdict(list), defaultdict(list)
    for s in sorted({s for s, _ in Rs}):
        lp = parent_lang(s); a, b = Rs[(s, 1)], Rs[(s, 2)]; tr = np.array(W[s].train_idx); T = set(np.random.RandomState(3000 + s).choice(tr, 19, replace=False).tolist())
        for o in tr:
            if o in T: continue
            k = sum(p in T and (lp[p] == lp[o]).all() for p in tr if p != o and SDa[s][o, p] == 1); d = min((SDa[s][o, p] for p in T), default=3)
            agree = (a[o] == b[o]).all(); by_k[min(k, 2)].append(agree); by_d[d].append(agree)
    O += ["## C. Basin depth: sibling exact-form agreement on untaught objects (same-record arm, 45 seeds) by number of same-class anchors, and by distance to the nearest taught object", "",
          "| same-class anchors 0 | 1 | 2+ | nearest taught at d=1 | d=2 | d=3 |", "|---|---|---|---|---|---|",
          " | ".join(f"{np.mean(by_k[k]):.2f} (n={len(by_k[k])})" for k in range(3)) + " | " + " | ".join(f"{np.mean(by_d[d]) if by_d[d] else float('nan'):.2f} (n={len(by_d[d])})" for d in (1, 2, 3)) + " |"]
    path = "results_v3/probe44.md"; open(path, "w").write("\n".join(O) + "\n"); print("\n".join(O)); print("wrote", path)
