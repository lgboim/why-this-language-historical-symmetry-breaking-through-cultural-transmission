"""
Run the symbol-emergence experiment across conditions and seeds.

    python run.py                                  # all conditions x 10 seeds
    python run.py --conditions bone oral --seeds 0 1 2 3 4
    python run.py --quick                          # tiny smoke test
    python run.py --workers 4                      # parallel over (condition, seed) pairs

Each run writes results/<condition>_seed<k>.json (one dict per eval point; the
final eval of each generation also carries the full language).
"""
import argparse, json, os, time
from dataclasses import asdict
from multiprocessing import Pool

CONDITIONS = ["pair", "population", "generations", "oral", "oral_fixed", "bone", "bone_edition"]


def one(job):
    cond, seed, a = job
    import torch; torch.set_num_threads(1)
    from game import Config, run
    path = os.path.join(a["out"], f"{cond}_seed{seed}.json")
    if os.path.exists(path) and not a["quick"]:
        return f"skip {path} (exists)"
    cfg = Config(condition=cond, seed=seed, steps=a["steps"], generations=a["generations"],
                 n_transmit=a["n_transmit"], bone_capacity=a["bone_capacity"],
                 n_attrs=a["n_attrs"], n_vals=a["n_vals"], vocab=a["vocab"], msg_len=a["msg_len"])
    t0 = time.time()
    log = run(cfg)
    with open(path, "w") as f:
        json.dump({"config": asdict(cfg), "log": log}, f)
    last = log[-1]
    return (f"{cond:13s} seed={seed:<2d} train={last['train_acc']:.2f} test={last['test_acc']:.2f} "
            f"topsim={last['topsim']:.3f} posdis={last['posdis']:.2f} uniq={last['n_unique_msgs']:2d} "
            f"({time.time()-t0:.0f}s)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--conditions", nargs="+", default=CONDITIONS)
    ap.add_argument("--seeds", nargs="+", type=int, default=list(range(10)))
    ap.add_argument("--steps", type=int, default=2000)
    ap.add_argument("--generations", type=int, default=6)
    ap.add_argument("--n_transmit", type=int, default=19)
    ap.add_argument("--bone_capacity", type=int, default=-1)
    ap.add_argument("--n_attrs", type=int, default=3)
    ap.add_argument("--n_vals", type=int, default=4)
    ap.add_argument("--vocab", type=int, default=8)
    ap.add_argument("--msg_len", type=int, default=3)
    ap.add_argument("--workers", type=int, default=max(1, os.cpu_count() or 1))
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--out", default="results")
    args = ap.parse_args()
    os.makedirs(args.out, exist_ok=True)
    if args.quick:
        args.steps, args.generations = 300, 2
    a = vars(args)
    jobs = [(c, s, a) for s in args.seeds for c in args.conditions]
    with Pool(args.workers) as pool:
        for msg in pool.imap_unordered(one, jobs):
            print(msg, flush=True)
