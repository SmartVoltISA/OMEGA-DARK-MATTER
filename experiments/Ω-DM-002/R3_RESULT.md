# Ω-DM-002 R3 — Certification Result

**Status: PASS — preregistered acceptance gate met**

## Execution identity

- Executor: `run_r3_convergent.py` — convergent optimized implementation preserving the preregistered objective.
- Numerical method: sufficient statistics, spectral factorization, then non-negative least squares after incorporating the L1 term as a linear shift. No standardization or intercept.
- Fixture cross-check against the reference cyclic coordinate-descent solver: max coefficient difference `4.10e-11`; RSS difference `5.87e-11`.
- Main seed: `20260911`; N=24; train=40; test=20; length=80; K=0.05; gamma=0.02; sigma=0.005; edge_p=0.12.
- Lambda grid: `{0.1, 0.3, 1, 3, 10, 30, 100}`.
- Controls: 20 W=0 null seeds + 20 temporal-permutation seeds.

## Main result

| Metric | Result |
|---|---:|
| Selected λ | 0.1 |
| Active edges | 120 |
| Hidden true edges | 33 |
| Edge precision | 0.275000 |
| Edge recall | 1.000000 |
| Baseline h1 RMSE | 32.2280692194 |
| Selected h1 RMSE | 18.2849216847 |
| Baseline h2 RMSE | 84.6103802909 |
| Selected h2 RMSE | 46.7045234781 |
| Baseline h5 RMSE | 312.9721731252 |
| Selected h5 RMSE | 94.7945457197 |
| Baseline h10 RMSE | 424.4292656541 |
| Selected h10 RMSE | 142.3210213559 |

Relative RMSE improvement: h1 **43.26%**, h2 **44.80%**, h5 **69.71%**, h10 **66.47%**.

## Candidate grid

| λ | RSS | active | BIC_like | KKT residual | converged |
|---:|---:|---:|---:|---:|:---:|
| 0.1 | 1.87913888693 | 120 | -792950.996441 | 1.155e-08 | True |
| 0.3 | 1.88149736822 | 91 | -792915.074514 | 6.706e-09 | True |
| 1 | 1.89729350805 | 71 | -792329.042601 | 6.985e-09 | True |
| 3 | 2.02985484898 | 70 | -787273.955433 | 9.313e-09 | True |
| 10 | 3.53763988614 | 67 | -745684.451012 | 5.588e-09 | True |
| 30 | 7.65640899539 | 65 | -687874.855881 | 9.313e-09 | True |
| 100 | 31.8569014817 | 65 | -581117.618351 | 1.118e-08 | True |

## Acceptance decision

1. **Held-out one-step:** PASS — selected model improves RMSE by 43.26%.
2. **Held-out multi-step:** PASS — selected model is better than the zero-relation baseline at horizons 2, 5 and 10, with improvements of 44.80%, 69.71% and 66.47%.
3. **W=0 null:** PASS — mean h1 improvement = `-3.1376e-08`; 19/20 runs selected the empty graph, and the single non-empty run had a negative predictive improvement. No systematic predictive advantage.
4. **Temporal permutation:** PASS — mean h1 improvement = `0`; 20/20 runs selected the empty graph and showed no predictive advantage.

## Secondary structure result

The model recovers all 33 hidden edges in the main synthetic graph (recall 1.0), but selects 120 active edges (precision 0.275). Thus R3 demonstrates predictive minimum-sufficient structure under the preregistered BIC-like criterion, while **not** demonstrating unique recovery of the true graph topology.

## Interpretation boundary

This PASS means only that a minimum-sufficient hidden relation structure is recoverable and predictive in this synthetic dynamical system. It is **not evidence for gravity, dark matter, or a physical relational substrate**.

Full machine-readable output is archived separately in `R3_FULL_OUTPUT.json`.

`EXECUTED = CONVERGED = VALIDATED FOR THIS SYNTHETIC GATE`; physical interpretation remains explicitly out of scope.
