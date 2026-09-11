# Ω-DM-004 — Independent-Generator Cross-Mechanism Test

**Status: PREREGISTERED / NOT EXECUTED**

## Objective

Attack the Ω-DM-002/003 result with a generating mechanism that is structurally related but not identical to the linear hidden-relation generator used previously.

The inference procedure remains the R3 symmetric non-negative relation reconstruction. The generator changes its coupling law from linear difference coupling to bounded nonlinear coupling:

`v_i(t+1) = v_i(t) - K Σ_j W_ij tanh(1.5(x_i(t)-x_j(t))) - γv_i(t) + η_i(t)`

The hidden graph is never supplied to inference.

## Fixed configuration

- seed block: `20260911 ... 20260930` (20 independent main seeds)
- N=24
- training trajectories=40
- test trajectories=20
- length=80
- K=0.02
- gamma=0.02
- sigma=0.003
- edge probability=0.12
- hidden edge weights uniform on [0.2, 1.0]
- R3 lambda grid `{0.1, 0.3, 1, 3, 10, 30, 100}`
- no standardization, intercept, or topology supplied to inference

## Primary test

For each seed, fit/select the R3 model on training data only using the BIC-like rule. Freeze the selected model and evaluate held-out one-step and rollout RMSE at horizons 2, 5 and 10 against the zero-relation baseline.

Report per-seed selected lambda, active-edge count and relative RMSE improvement.

## Controls

- 10 W=0 null seeds: no coupling in the generator.
- 10 temporal-permutation seeds: training trajectories are independently time-permuted before inference; test data remain unpermuted.

Controls must not systematically reproduce predictive advantage.

## Acceptance

The independent-generator result is a **robust cross-mechanism replication** if:

1. at least 90% of main seeds beat the zero-relation baseline at h=1;
2. at least 80% beat baseline at each of h=2,5,10;
3. mean improvement is positive at all four horizons;
4. null and temporal-permutation controls show no systematic predictive advantage;
5. inference never receives the generating topology.

If these criteria fail, report FAIL or INCONCLUSIVE rather than altering the protocol after seeing results.

## Interpretation boundary

PASS means only that predictive hidden-relation recovery survives a changed nonlinear synthetic generating mechanism. It does not establish a physical relational substrate and is not evidence for gravity or dark matter.

## Provenance

Predecessors: Ω-DM-002 R3 and Ω-DM-003. The purpose is explicit falsification pressure, not confirmation by repeating the same generator.
