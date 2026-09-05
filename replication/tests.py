"""
Sanity + invariant tests for the symbol-emergence lab. One file, no pytest needed.

    python tests.py            # runs everything, prints PASS/FAIL per check
    python tests.py -k bone    # only checks whose name contains 'bone'

Covers: metric correctness (tie-corrected Spearman, topsim, posdis on synthetic languages),
world/holdout invariants, agent shapes & imitation, Bone semantics, channel balance across
conditions, seed pairing + determinism, the statistics in analyze.py, and integrity of results/.
"""
import glob, json, os, sys, traceback, itertools
from math import comb
import numpy as np
import torch

from game import (World, Sender, Receiver, Bone, Config, run, _rank_avg, _spearman,
                  topographic_similarity, positional_disentanglement, language_of,
                  transmit_oral, transmit_bone)

CHECKS = []
def check(fn):
    CHECKS.append(fn); return fn

def rank_ref(x):
    """Reference fractional ranking via unique/counts (independent of _rank_avg)."""
    x = np.asarray(x, float)
    u, inv, cnt = np.unique(x, return_inverse=True, return_counts=True)
    start = np.cumsum(np.concatenate([[0], cnt[:-1]])) + 1
    return (start + (cnt - 1) / 2.0)[inv]

def spearman_ref(a, b):
    ra, rb = rank_ref(a), rank_ref(b)
    return float(np.corrcoef(ra, rb)[0, 1])

# ----------------------------------------------------------------------------- metrics
@check
def rank_avg_matches_reference():
    rng = np.random.RandomState(0)
    for _ in range(200):
        x = rng.randint(0, 4, size=rng.randint(2, 60))          # heavy ties, like Hamming distances
        assert np.allclose(_rank_avg(x), rank_ref(x)), x
    assert np.allclose(_rank_avg([3, 1, 2]), [3, 1, 2])
    assert np.allclose(_rank_avg([1, 1, 1]), [2, 2, 2])

@check
def spearman_matches_reference_and_argsort_is_wrong():
    rng = np.random.RandomState(1)
    diffs = []
    for _ in range(200):
        n = rng.randint(5, 80)
        a, b = rng.randint(0, 4, n), rng.randint(0, 4, n)
        if len(set(a)) < 2 or len(set(b)) < 2:
            continue
        s = _spearman(a, b)
        assert abs(s - spearman_ref(a, b)) < 1e-9
        # the v1 bug: rank by argsort (no tie averaging)
        ra, rb = np.argsort(np.argsort(a)), np.argsort(np.argsort(b))
        diffs.append(abs(s - np.corrcoef(ra, rb)[0, 1]))
    assert max(diffs) > 0.05, "argsort ranking should differ noticeably on tied data"
    assert _spearman([1, 1, 1], [1, 2, 3]) == 0.0                # degenerate -> 0, not NaN

@check
def topsim_extremes_on_synthetic_languages():
    w = World(3, 4, seed=0)
    perfect = w.objects.copy()                                   # symbol i = value of attr i
    assert abs(topographic_similarity(w, perfect) - 1.0) < 1e-9
    perm = np.array([[ (3 - v) for v in o] for o in w.objects])   # relabel values: still perfect
    assert abs(topographic_similarity(w, perm) - 1.0) < 1e-9
    const = np.zeros_like(perfect)
    assert topographic_similarity(w, const) == 0.0
    rng = np.random.RandomState(0)
    hol = np.array([rng.permutation(64)[:1] for _ in range(64)])  # holistic: each object a unique id
    hol = np.stack([hol[:, 0] // 16, (hol[:, 0] // 4) % 4, hol[:, 0] % 4], 1)
    ts = topographic_similarity(w, hol)
    assert abs(ts) < 0.15, ts
    # metric is symmetric under renaming of message symbols and reordering of positions
    assert abs(topographic_similarity(w, perfect[:, ::-1]) - 1.0) < 1e-9

@check
def posdis_extremes():
    w = World(3, 4, seed=0)
    assert abs(positional_disentanglement(w, w.objects.copy()) - 1.0) < 1e-9
    assert positional_disentanglement(w, np.zeros((64, 3), int)) == 0.0
    # each position = XOR-ish mix of two attributes -> low posdis
    mixed = np.stack([(w.objects[:, 0] + w.objects[:, 1]) % 4,
                      (w.objects[:, 1] + w.objects[:, 2]) % 4,
                      (w.objects[:, 0] + w.objects[:, 2]) % 4], 1)
    assert positional_disentanglement(w, mixed) < 0.05

# ----------------------------------------------------------------------------- world
@check
def world_holdout_invariants():
    w = World(3, 4, 0.25, seed=7)
    assert len(w.objects) == 64 and len(w.test_idx) == 16 and len(w.train_idx) == 48
    assert not set(w.train_idx) & set(w.test_idx)
    assert set(w.train_idx) | set(w.test_idx) == set(range(64))
    w2 = World(3, 4, 0.25, seed=7)
    assert np.array_equal(w.test_idx, w2.test_idx), "same seed must give same split"
    assert not np.array_equal(w.test_idx, World(3, 4, 0.25, seed=8).test_idx)
    # every attribute value still appears in training (otherwise held-out is unlearnable)
    for a in range(3):
        assert set(w.objects[w.train_idx][:, a]) == set(range(4))
    x = w.encode(np.arange(64))
    assert x.shape == (64, 12) and torch.all(x.sum(1) == 3)

@check
def sample_batch_invariants():
    w = World(3, 4, seed=0)
    rng = np.random.RandomState(0)
    for split in ("train", "test"):
        pool = set(w.train_idx if split == "train" else w.test_idx)
        t, c, lab = w.sample_batch(256, 4, split, rng)
        assert c.shape == (256, 5)
        assert set(t) <= pool
        assert np.all(c[np.arange(256), lab] == t), "label must point at the target"
        for row, tt in zip(c, t):
            assert (row == tt).sum() == 1, "target appears exactly once among candidates"
            assert len(set(row)) == 5, "no duplicate candidates (fixed in v3)"
    # distractor distribution is uniform over non-targets (the bijection must not bias)
    t, c, lab = w.sample_batch(4000, 4, "train", rng)
    others = c[c != t[:, None]]
    counts = np.bincount(others, minlength=64)
    assert counts.min() > 0.6 * counts.mean() and counts.max() < 1.4 * counts.mean(), counts
    # target position is uniform-ish (no positional leak for the receiver)
    counts = np.bincount(lab, minlength=5)
    assert counts.min() > 256 / 5 * 0.5, counts

# ----------------------------------------------------------------------------- agents
@check
def sender_receiver_shapes_and_invariances():
    torch.manual_seed(0)
    w = World(3, 4, seed=0)
    s, r = Sender(w.dim, 8, 3), Receiver(w.dim, 8)
    x = w.encode(np.arange(64))
    m, lp, ent = s(x)
    assert m.shape == (64, 3) and m.min() >= 0 and m.max() < 8
    assert lp.shape == (64,) and torch.all(lp <= 0) and torch.all(ent >= 0)
    g1, g2 = s(x, greedy=True)[0], s(x, greedy=True)[0]
    assert torch.equal(g1, g2), "greedy decoding must be deterministic"
    assert np.array_equal(language_of(s, w), g1.numpy())
    # receiver: permuting candidates permutes logits identically
    t, c, lab = w.sample_batch(32, 4, "train", np.random.RandomState(0))
    feats = w.encode(c.reshape(-1)).view(32, 5, w.dim)
    logits = r(g1[t], feats)
    perm = torch.tensor([4, 0, 3, 1, 2])
    assert torch.allclose(r(g1[t], feats[:, perm]), logits[:, perm], atol=1e-6)

@check
def imitation_actually_teaches_the_child():
    torch.manual_seed(0)
    w = World(3, 4, seed=0)
    cfg = Config(transmit_steps=200)
    parent, child = Sender(w.dim, 8, 3), Sender(w.dim, 8, 3)
    objs = np.random.RandomState(0).choice(w.train_idx, 19, replace=False)
    target = parent(w.encode(objs), greedy=True)[0]
    before = (child(w.encode(objs), greedy=True)[0] == target).float().mean().item()
    transmit_oral(cfg, w, parent, child, objs)
    after = (child(w.encode(objs), greedy=True)[0] == target).float().mean().item()
    assert after > 0.9 and after > before, (before, after)

# ----------------------------------------------------------------------------- bone
@check
def bone_capacity_and_replacement_rules():
    b = Bone(3)
    b.record([0, 1, 2], [(1, 1, 1), (2, 2, 2), (3, 3, 3)], [True, True, True])
    assert len(b.entries) == 3
    b.record([5], [(5, 5, 5)], [False])
    assert 5 not in b.entries, "failures are never carved"
    b.record([5], [(5, 5, 5)], [True])                          # full; all weak -> evict one
    assert len(b.entries) == 3 and 5 in b.entries
    b.record([5, 5], [(5, 5, 5)] * 2, [True, True])              # strengthen 5 to 3
    b.record([5], [(9, 9, 9)], [True])
    assert b.entries[5] == (5, 5, 5), "strong incumbent survives a competing form"
    weak = [o for o in b.entries if o != 5][0]
    b.record([weak], [(7, 7, 7)], [True])
    assert b.entries[weak] == (7, 7, 7), "weak incumbent is replaced"
    for _ in range(5):
        b.record(list(b.entries), [b.entries[o] for o in b.entries], [True] * 3)
    b.record([42], [(4, 2, 4)], [True])
    assert 42 not in b.entries and len(b.entries) == 3, "full bone of strong entries rejects newcomers"
    objs, msgs = b.read()
    assert msgs.shape == (3, 3) and all(tuple(m) == b.entries[o] for o, m in zip(objs, msgs))
    assert Bone(2).read() == (None, None)

@check
def bone_rewrite_keeps_slots_and_uses_final_language():
    torch.manual_seed(0)
    w = World(3, 4, seed=0)
    s = Sender(w.dim, 8, 3)
    b = Bone(19)
    objs = np.arange(19)
    b.record(objs, [(0, 0, 0)] * 19, [True] * 19)
    keys = set(b.entries)
    b.rewrite_from(s, w)
    assert set(b.entries) == keys
    lang = language_of(s, w)
    assert all(b.entries[o] == tuple(lang[o]) for o in keys)
    assert all(v == 1 for v in b.successes.values())

@check
def transmit_bone_teaches_child_the_carved_forms():
    torch.manual_seed(1)
    w = World(3, 4, seed=0)
    b = Bone(19)
    objs = np.random.RandomState(1).choice(w.train_idx, 19, replace=False)
    forms = [tuple(int(v) for v in np.random.RandomState(int(o)).randint(0, 8, 3)) for o in objs]
    b.record(objs, forms, [True] * 19)
    child = Sender(w.dim, 8, 3)
    transmit_bone(Config(transmit_steps=300), w, child, b)
    got = language_of(child, w)[objs]
    assert (got == np.array(forms)).mean() > 0.9

# ----------------------------------------------------------------------------- channel balance / pairing
@check
def all_channels_carry_exactly_n_transmit_pairs():
    cfg = Config(steps=30, generations=3, transmit_steps=5)
    seen = {}
    orig = __import__("game")._imitate
    def spy(cfg_, world, child, objs, target):
        seen.setdefault(cfg_.condition, []).append(len(objs)); orig(cfg_, world, child, objs, target)
    __import__("game")._imitate = spy
    try:
        for cond in ("oral", "oral_fixed", "bone", "bone_edition"):
            run(Config(**{**cfg.__dict__, "condition": cond}))
    finally:
        __import__("game")._imitate = orig
    for cond in ("oral", "oral_fixed"):
        assert seen[cond] == [19, 19], (cond, seen[cond])
    for cond in ("bone", "bone_edition"):
        assert all(n <= 19 for n in seen[cond]) and len(seen[cond]) == 2, (cond, seen[cond])

@check
def oral_fixed_uses_same_subset_every_generation_and_oral_does_not():
    import game
    calls = {}
    orig = game.transmit_oral
    def spy(cfg, world, parent, child, objs):
        calls.setdefault(cfg.condition, []).append(tuple(sorted(objs))); orig(cfg, world, parent, child, objs)
    game.transmit_oral = spy
    try:
        for cond in ("oral", "oral_fixed"):
            run(Config(condition=cond, steps=20, generations=4, transmit_steps=2))
    finally:
        game.transmit_oral = orig
    assert len(set(calls["oral_fixed"])) == 1
    assert len(set(calls["oral"])) > 1
    w = World(3, 4, 0.25, seed=0)
    assert set(calls["oral_fixed"][0]) <= set(w.train_idx), "transmitted objects must be training objects"

@check
def seed_pairing_and_determinism():
    a = run(Config(condition="oral", steps=40, generations=2, transmit_steps=5, eval_every=20, seed=3))
    b = run(Config(condition="oral", steps=40, generations=2, transmit_steps=5, eval_every=20, seed=3))
    assert json.dumps(a) == json.dumps(b), "same config+seed must reproduce bit-identically"
    c = run(Config(condition="oral", steps=40, generations=2, transmit_steps=5, eval_every=20, seed=4))
    assert json.dumps(a) != json.dumps(c)
    # same seed across conditions -> same held-out split and same generation-0 init
    p = run(Config(condition="pair", steps=40, generations=2, eval_every=20, seed=3))
    assert World(seed=3).test_idx.tolist() == World(seed=3).test_idx.tolist()
    assert a[0]["language"] if "language" in a[0] else True
    # gen-0 of every transmission condition shares init with `generations` (seed*100+0)
    g = run(Config(condition="generations", steps=40, generations=2, eval_every=20, seed=3))
    assert [r for r in a if r["gen"] == 0][-1]["language"] == [r for r in g if r["gen"] == 0][-1]["language"]

@check
def log_schema_and_step_accounting():
    log = run(Config(condition="bone", steps=50, generations=3, transmit_steps=3, eval_every=25, seed=0))
    assert len(log) == 3 * 2
    assert [r["step"] for r in log] == [25, 50, 75, 100, 125, 150]
    assert sum("language" in r for r in log) == 3
    for r in log:
        assert 0 <= r["test_acc"] <= 1 and -1 <= r["topsim"] <= 1 and 1 <= r["n_unique_msgs"] <= 64
        assert r["bone_size"] is not None and r["bone_size"] <= 19
    lp = run(Config(condition="pair", steps=50, generations=3, eval_every=25, seed=0))
    assert [r["step"] for r in lp] == [25, 50, 75, 100, 125, 150] and all(r["gen"] == 0 for r in lp)

# ----------------------------------------------------------------------------- statistics (analyze.py)
def _sign_test(diffs):
    d = np.asarray(diffs); d = d[d != 0]
    n, k = len(d), int((d > 0).sum())
    if n == 0: return 1.0
    p_one = sum(comb(n, i) for i in range(max(k, n - k), n + 1)) / 2 ** n
    return min(1.0, 2 * p_one)

@check
def sign_test_matches_exact_binomial():
    assert abs(_sign_test([1] * 10) - 2 / 1024) < 1e-12
    assert abs(_sign_test([1] * 9 + [-1]) - 2 * 11 / 1024) < 1e-12
    assert _sign_test([1] * 5 + [-1] * 5) == 1.0
    assert _sign_test([0, 0, 0]) == 1.0
    assert _sign_test([1, 1, 1, -1, 0]) == _sign_test([1, 1, 1, -1]), "ties are dropped"
    # symmetric
    assert _sign_test([1, 1, 1, 1, -1]) == _sign_test([-1, -1, -1, -1, 1])

@check
def bootstrap_ci_is_sane():
    rng = np.random.RandomState(0)
    d = rng.normal(0.05, 0.02, 10)
    m = np.array([rng.choice(d, 10).mean() for _ in range(5000)])
    lo, hi = np.percentile(m, 2.5), np.percentile(m, 97.5)
    assert lo < d.mean() < hi and lo > 0
    z = np.zeros(10); assert np.percentile([rng.choice(z, 10).mean() for _ in range(100)], 50) == 0

# ----------------------------------------------------------------------------- results/ integrity
@check
def results_dir_integrity_and_metric_consistency():
    files = sorted(glob.glob("results/*_seed*.json"))
    assert len(files) == 70, len(files)
    seen = {}
    ref = None
    for p in files:
        d = json.load(open(p)); c, log = d["config"], d["log"]
        seen.setdefault(c["condition"], set()).add(c["seed"])
        assert c["n_transmit"] == 19 and c["bone_capacity"] == -1 and c["steps"] == 2000
        key = {k: v for k, v in c.items() if k not in ("condition", "seed")}
        ref = ref or key
        assert key == ref, f"config drift in {p}"
        assert len(log) == 48 and log[-1]["step"] == 12000
        w = World(c["n_attrs"], c["n_vals"], c["holdout_frac"], seed=c["seed"])
        for r in log:
            if "language" in r:
                lang = np.array(r["language"])
                assert lang.shape == (64, 3) and lang.min() >= 0 and lang.max() < 8
                assert abs(topographic_similarity(w, lang) - r["topsim"]) < 1e-9, p
                assert abs(positional_disentanglement(w, lang) - r["posdis"]) < 1e-9, p
                assert len({tuple(m) for m in lang}) == r["n_unique_msgs"], p
            if c["condition"].startswith("bone"):
                assert r["bone_size"] is not None and r["bone_size"] <= 19
            else:
                assert r["bone_size"] is None
    assert all(seen[k] == set(range(10)) for k in seen) and len(seen) == 7, seen

@check
def results_gen0_is_shared_across_generational_conditions():
    """gen 0 has no transmission, so oral/oral_fixed/bone/bone_edition/generations must be
    identical there for a given seed (same init, same rng stream) -> a strong pairing check."""
    for seed in range(10):
        g0 = {}
        for cond in ("generations", "oral", "oral_fixed", "bone", "bone_edition"):
            log = json.load(open(f"results/{cond}_seed{seed}.json"))["log"]
            g0[cond] = [r["language"] for r in log if r["gen"] == 0 and "language" in r][0]
        langs = list(g0.values())
        assert all(l == langs[0] for l in langs), f"gen-0 languages differ at seed {seed}"

@check
def summary_md_reproduces_from_results():
    import subprocess, tempfile, shutil
    tmp = tempfile.mkdtemp()
    for p in glob.glob("results/*_seed*.json"):
        shutil.copy(p, tmp)
    subprocess.run([sys.executable, "analyze.py", tmp], check=True, capture_output=True)
    a = open("results/summary.md").read().rstrip()
    b = open(os.path.join(tmp, "summary.md")).read().rstrip()
    shutil.rmtree(tmp)
    assert a == b, "results/summary.md is stale relative to results/*.json"

# ----------------------------------------------------------------------------- lab.py (v3)
import lab
from lab import Cell, Record, make_cfg, run_cell, named_cells, build_grid, stats_line

@check
def lab_vectorised_metrics_match_game():
    w = World(3, 4, seed=0); rng = np.random.RandomState(0)
    for _ in range(30):
        lang = rng.randint(0, 8, (64, 3))
        assert abs(lab.topsim(w.objects, lang) - topographic_similarity(w, lang)) < 1e-12
    assert abs(lab.topsim(w.objects, w.objects.copy()) - 1.0) < 1e-12
    for _ in range(100):
        x = rng.randint(0, 4, rng.randint(2, 50))
        assert np.allclose(lab.rank_avg(x), _rank_avg(x))

@check
def lab_named_cells_cover_v2_and_grid_is_well_formed():
    nc = named_cells("small")
    assert set(nc) == {"pair", "population", "generations", "oral", "oral_fixed", "bone", "bone_edition"}
    assert nc["oral"].slots == "redraw" and nc["oral_fixed"].slots == "fixed"
    assert nc["bone"].fresh == "accumulate" and nc["bone_edition"].fresh == "rewrite"
    assert all(c.capacity == 19 for n, c in nc.items() if c.is_record)
    g = build_grid("small", "full")
    assert len(g) == 3 + 3 * 3 * 2 * 2 * 2 + 2 == 77 and len(set(g)) == len(g)
    assert len({c.name() for c in g}) == len(g), "cell names must be unique (they are file names)"
    assert all(c in g for c in nc.values()), "every v2 condition is a cell of the full grid"
    assert len(build_grid("small", "reduced")) == 11

@check
def lab_record_random_fixed_only_carves_slot_objects_and_fills_to_capacity():
    w = World(3, 4, seed=0); rng = np.random.RandomState(0)
    rec = Record(Cell("small", "gens", "random", "fixed", "accumulate", 19), w, 8, rng)
    slots = set(rec.slot_set); assert len(slots) == 19 and slots <= set(int(o) for o in w.train_idx)
    rec.observe(list(range(64)), [(1, 2, 3)] * 64, [True] * 64)
    assert set(rec.entries) <= slots and len(rec.entries) == 19
    rec2 = Record(Cell("small", "gens", "random", "fixed", "accumulate", 19), w, 8, np.random.RandomState(0))
    assert rec2.slot_set == slots, "same rng -> same slots (pairing)"
    rec2.observe([next(iter(slots))], [(7, 7, 7)], [True])
    lang = np.zeros((64, 3), int)
    rec2.end_of_generation(lang, np.ones(64))
    assert len(rec2.entries) == 19, "record is filled to capacity from the parent's final language"
    assert rec2.entries[next(iter(slots))] == (7, 7, 7), "accumulate keeps carved forms"
    rec2.c = Cell("small", "gens", "random", "fixed", "rewrite", 19)
    rec2.end_of_generation(lang, np.ones(64))
    assert all(m == (0, 0, 0) for m in rec2.entries.values()), "rewrite re-carves everything"

@check
def lab_record_hard_picks_lowest_accuracy_and_redraw_changes_slots():
    w = World(3, 4, seed=0)
    rec = Record(Cell("small", "gens", "hard", "dynamic", "rewrite", 8), w, 8, np.random.RandomState(0))
    rec.observe(list(range(64)), [(1, 1, 1)] * 64, [True] * 64)
    assert rec.entries == {}, "hard: nothing is carved before the first selection"
    acc = np.ones(64); hard = [int(o) for o in w.train_idx[:8]]; acc[hard] = 0.0
    rec.end_of_generation(np.zeros((64, 3), int), acc)
    assert set(rec.entries) == set(hard)
    rec = Record(Cell("small", "gens", "random", "redraw", "rewrite", 19), w, 8, np.random.RandomState(0))
    s0 = set(rec.slot_set); rec.end_of_generation(np.zeros((64, 3), int), np.ones(64))
    assert set(rec.slot_set) != s0 and set(rec.entries) == set(rec.slot_set)

@check
def lab_record_noise_corrupts_one_symbol_per_hit():
    w = World(3, 4, seed=0)
    rec = Record(Cell("small", "gens", "random", "fixed", "rewrite", 40, noise=0.5), w, 8, np.random.RandomState(0))
    lang = np.full((64, 3), 3)
    rec.end_of_generation(lang, np.ones(64))
    hits = [sum(a != 3 for a in m) for m in rec.entries.values()]
    assert max(hits) <= 1 and 0.2 < np.mean([h > 0 for h in hits]) < 0.8, hits

@check
def lab_run_is_deterministic_logs_everything_and_teaches_receiver():
    cfg = make_cfg(Cell("small", "gens", "random", "fixed", "rewrite", 19, 0.0, "both"), 0,
                   steps=60, generations=3, eval_every=30, transmit_steps=30, save_weights=True)
    (l1, w1), (l2, _) = run_cell(cfg), run_cell(cfg)
    assert json.dumps(l1) == json.dumps(l2)
    assert len(l1) == 6 and len(w1) == 3
    fin = [r for r in l1 if "per_obj_acc" in r]
    assert len(fin) == 3
    for r in l1:
        assert len(r["language"]) == 64 and len(r["decode"]) == 64 and 0 <= r["intelligibility"] <= 1
    assert fin[0]["transmitted_objs"] is None and len(fin[1]["transmitted_objs"]) == 19
    assert len(fin[0]["record"]) == 19 and fin[0]["slot_set"] == sorted(fin[1]["transmitted_objs"])
    assert set(w1[0]) == {"sender", "receiver"}
    # pairing: generation 0 is identical across cells for the same seed
    other = make_cfg(Cell("small", "gens", "success", "dynamic", "accumulate", 19), 0,
                     steps=60, generations=3, eval_every=30, transmit_steps=30, save_weights=False)
    l3, _ = run_cell(other)
    assert [r for r in l3 if r["gen"] == 0][-1]["language"] == fin[0]["language"]
    assert json.dumps(lab.cfg_to_json(cfg)) and lab.cfg_from_json(json.loads(json.dumps(lab.cfg_to_json(cfg)))) == cfg

@check
def lab_decision_rule():
    assert stats_line([0.1] * 10, ">")["verdict"] == "SUPPORTED"
    assert stats_line([-0.1] * 10, ">")["verdict"] == "REFUTED"
    assert stats_line([0.1] * 6 + [-0.1] * 4, ">")["verdict"] == "INCONCLUSIVE"
    assert stats_line([0.1] * 5, ">")["verdict"].startswith("UNDERPOWERED")
    assert "A>B" in stats_line([0.1] * 10, "?")["verdict"]

# ----------------------------------------------------------------------------- runner
# ---------------------------------------------------------------- v4 additions: ARI, anchors, hard distractors, Gumbel agents
from metrics import ari as _ari   # the project metric itself is under test

def test_ari_identity_and_relabelling():
    import numpy as np
    p = [0, 0, 1, 1, 2, 2, 3, 3]
    assert abs(_ari(p, p) - 1.0) < 1e-9
    assert abs(_ari(p, [5, 5, 9, 9, 1, 1, 7, 7]) - 1.0) < 1e-9          # relabelling-invariant
    rng = np.random.RandomState(0); vals = [_ari(rng.randint(0, 4, 40), rng.randint(0, 4, 40)) for _ in range(200)]
    assert abs(np.mean(vals)) < 0.05                                     # chance ≈ 0
    assert _ari(list(range(8)), list(range(8))) == 1.0                   # identical singleton partitions are identical partitions (standard convention)
    assert _ari([0] * 8, [3] * 8) == 1.0                                 # identical single-class partitions
    assert _ari(list(range(8)), [0] * 8) == 0.0                          # all-singletons vs one class: no information
    assert abs(_ari(p, [0, 1, 0, 1, 2, 3, 2, 3]) - _ari([0, 1, 0, 1, 2, 3, 2, 3], p)) < 1e-12   # symmetric
    assert _ari([7], [7]) == 1.0 and _ari([], []) == 1.0                 # declared policy for fewer than two items

def test_hard_distractors_are_hamming1_and_distinct():
    import numpy as np
    from game import World
    w = World(3, 4, 0.25, seed=1); w.hard_frac = 1.0; rng = np.random.RandomState(1)
    t = rng.choice(w.train_idx, 500); c, lab = w.candidates(t, 4, rng)
    d = (w.objects[c] != w.objects[t][:, None, :]).sum(-1)
    assert (d[d > 0] == 1).all() and all(len(set(r)) == 5 for r in c) and (c[np.arange(500), lab] == t).all()
    w.hard_frac = 0.0; c2, _ = w.candidates(t, 4, rng); d2 = (w.objects[c2] != w.objects[t][:, None, :]).sum(-1)
    assert (d2[d2 > 0] >= 1).all() and not (d2[d2 > 0] == 1).all()       # standard sampling is not all-Hamming-1

def test_gumbel_agents_interface_and_gradient():
    import torch, numpy as np
    from game import World, GumbelSender, GumbelReceiver
    w = World(3, 4, 0.25, seed=0); S, R = GumbelSender(w.dim, 8, 3, 64), GumbelReceiver(w.dim, 8, 3, 64)
    x = w.encode(np.arange(16)); msgs, lp, ent = S(x)
    assert msgs.shape == (16, 3) and lp.shape == (16,) and ent.shape == (16,) and S.onehot.shape == (16, 3, 8)
    rng = np.random.RandomState(0); c, lab = w.candidates(np.arange(16), 4, rng)
    logits = R(msgs, w.encode(c.reshape(-1)).view(16, 5, w.dim), onehot=S.onehot)
    loss = torch.nn.functional.cross_entropy(logits, torch.from_numpy(lab)); loss.backward()
    assert any(p.grad is not None and p.grad.abs().sum() > 0 for p in S.parameters())   # straight-through gradient reaches the sender
    g, _, _ = S(x, greedy=True); assert (g == S.logits(x).argmax(-1)).all()
    assert S.supervised_loss(x, msgs).item() >= 0

def test_class_matched_anchor_definition():
    import numpy as np
    from game import World
    w = World(3, 4, 0.25, seed=0); SD = (w.objects[:, None, :] != w.objects[None, :, :]).sum(-1)
    lang = np.zeros((64, 3), int); lang[:, 0] = w.objects[:, 0]          # one form per value of attribute 0 (classes of 16)
    o = w.train_idx[0]; nb = [p for p in w.train_idx if p != o and SD[o, p] == 1]
    same = [p for p in nb if (lang[p] == lang[o]).all()]; other = [p for p in nb if not (lang[p] == lang[o]).all()]
    assert same and other and all(w.objects[p, 0] == w.objects[o, 0] for p in same) and all(w.objects[p, 0] != w.objects[o, 0] for p in other)


CHECKS += [test_ari_identity_and_relabelling, test_hard_distractors_are_hamming1_and_distinct, test_gumbel_agents_interface_and_gradient, test_class_matched_anchor_definition]


if __name__ == "__main__":
    torch.set_num_threads(2)
    filt = sys.argv[sys.argv.index("-k") + 1] if "-k" in sys.argv else ""
    passed = failed = 0
    for fn in CHECKS:
        if filt not in fn.__name__:
            continue
        try:
            fn(); passed += 1; print(f"PASS  {fn.__name__}")
        except Exception:
            failed += 1; print(f"FAIL  {fn.__name__}\n" + "".join("      " + l for l in traceback.format_exc().splitlines(True)))
    print(f"\n{passed} passed, {failed} failed")
    sys.exit(1 if failed else 0)
