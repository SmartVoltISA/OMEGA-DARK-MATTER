# Ω-DM-005 — Partial + Noisy Observation

Date: 2026-09-11
Status: PREREGISTERED PROTOCOL — certification pending

## Question

Does predictive relational structure remain identifiable when the nonlinear Ω-DM-004 system is only partially observed and observations contain measurement noise?

## Generator

Reuse the Ω-DM-004 nonlinear bounded coupling generator exactly:

v_i(t+1) = v_i(t) - K * sum_j W_ij * tanh(1.5*(x_i(t)-x_j(t))) - gamma*v_i(t) + eta_i(t)
x_i(t+1) = x_i(t) + v_i(t+1)

Parameters:
- N = 24
- train length = 40
- test length = 20
- total length = 80
- K = 0.02
- gamma = 0.02
- process noise sigma = 0.003
- edge probability = 0.12
- edge weights uniform in [0.2, 1.0]
- seeds = 20260911..20260930 (20 main runs)

## Observation model

For each main seed, choose 18 of 24 nodes as observed using a deterministic seed-derived permutation. The remaining 6 nodes are permanently unobserved by the inference procedure.

Observed values are:

y_obs(t) = x_obs(t) + epsilon_obs(t)

where epsilon_obs is independent Gaussian measurement noise with sigma_obs = 0.01.

The same observed-node mask is used for train and test. Hidden-node values are never supplied to inference or evaluation of the observed prediction target.

## Inference

Apply the same R3 symmetric non-negative relation reconstruction to the 18 observed variables only. Do not change the inference objective, lambda grid, or selection rule.

Lambda grid:
{0.1, 0.3, 1, 3, 10, 30, 100}

Select lambda using training data only.

## Baseline

Zero-relation baseline on the observed variables, using the same initial observed state and the same one-step/horizon rollout convention.

## Primary metric

Relative held-out RMSE improvement:

improvement(h) = 1 - RMSE_selected(h) / RMSE_zero(h)

for h = 1, 2, 5, 10.

Primary endpoint: mean improvement at h=1 across 20 seeds and win rate versus zero baseline.

Secondary endpoints: h=2, 5, 10; active-edge count; edge precision/recall only for observed-observed true edges; stability across masks/seeds.

## Controls

1. W=0 null: 10 independent seeds with the same observation model. Expected selected graph should collapse to empty or show no systematic held-out advantage.
2. Temporal permutation: 10 runs where training temporal order is independently permuted before reconstruction while preserving marginal observations. Expected no systematic predictive advantage.

## Acceptance gate

PASS requires all of:

1. h=1 win rate >= 80% across main runs;
2. positive mean h=1 improvement;
3. h=2/h=5/h=10 win rate >= 70% each;
4. no systematic advantage in W=0 null or temporal-permutation controls;
5. protocol parameters are frozen before certification rerun;
6. result is archived with seed-level outputs.

A failure is scientifically valid and must be reported as FAIL, not tuned away.

## Interpretation boundary

PASS would establish robustness of the synthetic predictive-relational effect under partial/noisy observation. It would not establish a physical relational substrate, gravity, or dark matter.

## Next law questions

If this gate passes, use the same frozen generator/inference pair to test scaling, symmetry, conservation, propagation speed and coarse-graining as separate preregistered experiments. Do not combine them into one adaptive optimization.
