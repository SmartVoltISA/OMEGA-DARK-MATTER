# Ω-DM-002 R3 — Execution Status

**Status: CERTIFIED PASS**

## Implementation

A convergent optimized executor is committed as:

`experiments/Ω-DM-002/run_r3_convergent.py`

The implementation preserves the preregistered R3 objective, fixed lambda grid, training-only BIC-like selection, non-negativity constraint, and frozen held-out evaluation. It uses sufficient statistics plus an exact quadratic factorization and NNLS to solve the equivalent non-negative quadratic program.

## Validation of implementation

The optimized executor was cross-checked against the reference cyclic coordinate-descent solver on a deterministic fixture:

- maximum coefficient difference: `4.10e-11`;
- RSS difference: `5.87e-11`.

No standardization or intercept was introduced.

## Certified execution

Main configuration: seed `20260911`, N=24, train=40, test=20, length=80, K=.05, gamma=.02, sigma=.005, edge probability=.12, lambda grid `{0.1, 0.3, 1, 3, 10, 30, 100}`.

Main result:

- selected λ = `0.1`;
- baseline h1 RMSE = `32.2280692194`;
- selected h1 RMSE = `18.2849216847`;
- baseline/selected h2 RMSE = `84.6103802909 / 46.7045234781`;
- baseline/selected h5 RMSE = `312.9721731252 / 94.7945457197`;
- baseline/selected h10 RMSE = `424.4292656541 / 142.3210213559`.

Relative improvements: h1 `43.26%`, h2 `44.80%`, h5 `69.71%`, h10 `66.47%`.

Controls:

- W=0 null: 20 runs; mean h1 improvement `-3.14e-08`; one non-empty selection, with negative improvement; no systematic predictive advantage.
- temporal permutation: 20 runs; mean h1 improvement `0`; zero non-empty selections; no predictive advantage.

## Decision

**PASS.** All four preregistered acceptance conditions are satisfied.

Secondary topology result remains limited: the selected model has 120 active edges versus 33 hidden edges, with edge recall `1.0` and precision `0.275`. Therefore R3 demonstrates predictive recoverability of a minimum-sufficient relation structure in the synthetic system, not unique topology recovery.

The full result is archived in:

- `experiments/Ω-DM-002/R3_RESULT.md`
- `experiments/Ω-DM-002/R3_FULL_OUTPUT.json`

## Gate transition

Ω-DM-002 R3 is now certified. The next research gate may proceed to **Ω-DM-003**, subject to its own preregistration and independent falsification criteria.

`EXECUTED = CONVERGED = VALIDATED FOR THIS SYNTHETIC GATE`
