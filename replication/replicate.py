"""replicate.py — end-to-end re-run of the pre-registered K1–K17 on a fresh seed range, with thresholds read from manifest_k.json.
   python replicate.py --seeds 100..119 --out results_replicate --workers 8
   Steps: (1) sweep the four confirmation families (cap 8, cap 40, noise 0.2, reader both) + cap-19 partner cells + generations on the seeds;
          (2) run the child/sibling/snapshot experiments (K14, K16, K17a-c); (3) evaluate with the existing evaluators, seed range injected via env.
   No statistical decision lives here: every threshold is in manifest_k.json and in results_v3_confirm2/PREREG.md."""
import argparse, json, os, subprocess, sys
p = argparse.ArgumentParser(); p.add_argument("--seeds", required=True); p.add_argument("--out", default="results_replicate"); p.add_argument("--workers", type=int, default=8); p.add_argument("--quick", action="store_true", help="smoke test: short generations"); p.add_argument("--arch", default="gru", choices=["gru", "gumbel"]); a = p.parse_args()
lo, hi = map(int, a.seeds.split("..")); seeds = list(range(lo, hi + 1)); M = json.load(open("manifest_k.json"))
env = dict(os.environ, K_SEEDS=f"{lo}..{hi}", K_OUT=a.out, K_ARCH=a.arch)
cells = ["cap-8_noise-0.0_rd-sender", "cap-40_noise-0.0_rd-sender", "cap-19_noise-0.2_rd-sender", "cap-19_noise-0.0_rd-both", "cap-19_noise-0.0_rd-sender", "generations"]
print(f"[1/3] sweep {len(cells)} families x {len(seeds)} seeds -> {a.out}"); subprocess.run([sys.executable, "lab.py", "run", "--out", a.out, "--workers", str(a.workers), "--seeds", *map(str, seeds), "--cells", *cells, "--arch", a.arch] + (["--quick"] if a.quick else []), check=True)
print("[2/3] child/sibling experiments (K14, K16, K17)"); subprocess.run([sys.executable, "probe46.py"], env=env, check=True)
print("[3/3] evaluate"); 
for ev in ("confirm2.py", "confirm2b.py", "confirm3.py", "confirm4.py"): subprocess.run([sys.executable, ev], env=env, check=True)
print("done; thresholds used:"); print(json.dumps(M["rule"], indent=1))
