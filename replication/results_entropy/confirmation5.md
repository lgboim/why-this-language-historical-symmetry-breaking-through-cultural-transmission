# E1–E4: entropy-bonus scan (seeds 0–9)

## coef 0.005: n runs = 170, seeds = 30
E1 rewrite − accumulate topsim_distinct: | 30 | 21/9 | +0.047 | [+0.026, +0.068] | 0.043 | INCONCLUSIVE |
E2 child entropy@250 < 0.5 × gen-0 entropy@250: 1.00 of seeds
E4 same − other anchors: | 30 | 30/0 | +0.389 | [+0.367, +0.409] | 0.000 | SUPPORTED |

## coef 0.02: n runs = 770, seeds = 10
E1 rewrite − accumulate topsim_distinct: | 10 | 9/1 | +0.085 | [+0.042, +0.131] | 0.021 | SUPPORTED |
E2 child entropy@250 < 0.5 × gen-0 entropy@250: 1.00 of seeds
E4 same − other anchors: | 10 | 10/0 | +0.385 | [+0.347, +0.422] | 0.002 | SUPPORTED |

## coef 0.08: n runs = 90, seeds = 10
E1 rewrite − accumulate topsim_distinct: | 10 | 10/0 | +0.041 | [+0.027, +0.058] | 0.002 | SUPPORTED |
E2 child entropy@250 < 0.5 × gen-0 entropy@250: 1.00 of seeds
E4 same − other anchors: | 10 | 10/0 | +0.218 | [+0.197, +0.236] | 0.002 | SUPPORTED |

## E3 within-generation form change per 250 steps (inheriting generations)

coef 0.005: 0.102 | coef 0.02: 0.129 | coef 0.08: 0.289
0.02 − 0.005: | 10 | 9/1 | +0.027 | [+0.017, +0.036] | 0.021 | SUPPORTED |
0.08 − 0.02: | 10 | 10/0 | +0.160 | [+0.153, +0.169] | 0.002 | SUPPORTED |
