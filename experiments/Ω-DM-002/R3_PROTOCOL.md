# Ω-DM-002 R3 — Minimum-Structure Reconstruction

**Status:** PREREGISTERED / NOT EXECUTED

## Question

Can the hidden relation structure be reconstructed from observed state transitions while selecting the **minimum sufficient relation structure** using training data only?

## Motivation

R1 recovered nearly all true edges but massively over-reconstructed. R2 improved prediction but used an exploratory fixed complexity choice. R3 therefore makes complexity selection explicit and forbids test-set tuning.

## Data

Synthetic dynamics:

`x_i(t+1) = x_i(t) + v_i(t)`

`v_i(t+1) = v_i(t) - k Σ_j W_ij (x_i(t)-x_j(t)) - γv_i(t) + η_i(t)`

`W` is hidden, symmetric, non-negative, sparse. It is never supplied to the inference procedure.

## Candidate complexity grid

Use only the training trajectories to select among fixed sparsity penalties:

`λ ∈ {0.1, 0.3, 1, 3, 10, 30, 100}`

For each λ, fit a symmetric non-negative graph jointly. The selected model minimizes:

`BIC_like = N_train * log(RSS/N_train) + 2 * k_active`

where `k_active` is the number of active undirected edges. No test observation may enter model selection.

## Acceptance

Primary:

1. Selected model must beat the zero-relation baseline on held-out one-step RMSE.
2. Selected model must not be worse than baseline on held-out multi-step rollout RMSE at horizons 2, 5 and 10.
3. Null data (`W=0`) must not systematically select a non-empty graph with predictive advantage.
4. Temporal-permutation control must not systematically produce predictive advantage.

Secondary:

- edge precision/recall;
- active-edge count;
- stability of selected complexity across training seeds;
- coefficient recovery error;
- sensitivity to the λ grid.

## Falsification

R3 is FAIL if the minimum-complexity model does not improve held-out prediction, if controls show comparable improvement, or if the selected complexity is unstable without predictive benefit.

## Interpretation boundary

PASS means only that a minimum-sufficient hidden relation structure is recoverable in this synthetic dynamical system. It is not evidence for gravity, dark matter, or a physical relational substrate.

## Provenance

- Predecessor: Ω-DM-002 RESULT-001 / R1 failure.
- R2 exploratory result is not used as a test-set tuning source.
- Execution must archive the full candidate-grid table, selection metric, held-out metrics, null controls, permutation controls and exact code commit.
