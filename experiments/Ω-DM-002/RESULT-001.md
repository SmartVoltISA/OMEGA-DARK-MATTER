# Ω-DM-002 — RESULT-001

**Status:** EXECUTED LOCALLY / FAILED RECONSTRUCTION GATE
**Classification:** FAIL for the current reconstruction algorithm; no physical inference.

## Execution

The committed `run_reconstruct.py` was reproduced and executed locally in the analysis environment without GitHub Actions. GitHub Actions was not used.

Configuration:

- seed: `20260911`
- N: `24`
- train trajectories: `40`
- test trajectories: `20`
- trajectory length: `80`
- K: `0.05`
- gamma: `0.02`
- noise sigma: `0.005`
- edge probability: `0.12`
- sparsity threshold: `0.002`
- null controls: `20`
- permutation controls: `20`

## Main result

The hidden graph contained **33 true edges**.

The reconstruction returned **222 edges**.

- true positives: `32`
- precision: `0.1441`
- recall: `0.9697`
- baseline held-out rollout RMSE: `32.2280692194`
- reconstructed held-out rollout RMSE: `537.6809114935`

Thus the estimator almost recovered the true edge set in recall, but massively over-selected false edges and produced a dramatically worse held-out prediction.

**Decision: FAIL.**

This is a useful failure: the observed signal contains information about the hidden relations, but the present independent edge-scoring rule cannot distinguish direct relation from correlated network effects well enough for predictive reconstruction.

## Null control

Across 20 null runs, the mean held-out improvement `(baseline RMSE − relation RMSE)` was:

`-0.0062215162`

Population SD:

`0.0002415478`

The null did not show a positive systematic improvement.

## Permutation control

Across 20 topology/weight permutation runs, the mean held-out improvement was:

`-398.7010777537`

Population SD:

`401.7907977245`

The permutation control strongly failed to produce a false positive improvement; however, its extreme instability also shows that the current reconstructed graph is numerically ill-conditioned and unsuitable as a final inference method.

## Audit conclusion

The failure is methodological, not evidence against relational dynamics.

The current estimator scores each candidate edge independently. In a coupled network, neighboring edges generate correlated regressors. Consequently, the same observed acceleration can be attributed to many candidate edges. The result demonstrates why independent pairwise scoring is insufficient here.

## Required next gate

Do **not** tune the test result by hand.

Replace the estimator with a joint constrained reconstruction of `W` using the full coupled equations, with:

1. one coefficient per unordered edge;
2. symmetry enforced during fitting;
3. non-negativity enforced;
4. explicit L1/complexity penalty fixed before test scoring;
5. train-only model selection;
6. held-out prediction;
7. edge precision/recall;
8. null and permutation controls;
9. independent scoring implementation;
10. sensitivity analysis over a preregistered penalty grid.

Only then should Ω-DM-002 receive a second execution gate.

## Interpretation boundary

Even a future PASS would mean only that hidden relations are reconstructable in the specified synthetic dynamical system. It would not constitute evidence that gravity or dark matter is caused by relational structure.
