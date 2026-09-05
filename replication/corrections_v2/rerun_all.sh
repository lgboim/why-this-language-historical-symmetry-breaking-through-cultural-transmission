#!/bin/sh
# Re-score every ARI-dependent evaluator from cached data with the corrected metric; writes go to corrections_v2/recomputed/ (rerun.py redirects them).
cd "$(dirname "$0")/.."
run() { echo "=== $*"; env "$@" 2>&1 | tail -3; }
run python3 corrections_v2/rerun.py confirm3.py
run K_OUT=results_replicate K_SEEDS=100..119 python3 corrections_v2/rerun.py confirm3.py
run python3 corrections_v2/rerun.py probe46.py
run K_OUT=results_replicate K_SEEDS=100..119 python3 corrections_v2/rerun.py probe46.py
for a in results_arch results_arch2 results_arch3; do [ -d $a ] && run K_ARCH=gumbel K_OUT=$a K_SEEDS=100..119 python3 corrections_v2/rerun.py probe46.py; done
run python3 corrections_v2/rerun.py probe42.py
run python3 corrections_v2/rerun.py probe45.py
run python3 corrections_v2/rerun.py confirm4.py
run K_OUT=results_v3_confirm2 python3 corrections_v2/rerun.py confirm4.py
run python3 corrections_v2/rerun.py confirm7.py
run python3 corrections_v2/rerun.py confirm8.py
run python3 corrections_v2/rerun.py probe47.py
run python3 corrections_v2/rerun.py probe49.py
run python3 corrections_v2/rerun.py probe39.py
run python3 corrections_v2/rerun.py probe41.py
run python3 corrections_v2/rerun.py probe43.py
run python3 corrections_v2/rerun.py probe44.py
echo "=== done"
