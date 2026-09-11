# Ω-DM-006 — Scaling Law Protocol

Date: 2026-09-11
Status: PREREGISTERED BEFORE CERTIFICATION RUN

## Question

Does the predictive relational signal obey a reproducible scaling law when the system size changes?

Primary sizes:

N = 24, 48, 96, 192

The inference objective is held fixed in form. We measure predictive improvement, active-edge density, and a normalized relational strength statistic as functions of N.

## Generator

Use the same bounded nonlinear relation mechanism as Ω-DM-004:

v_i(t+1) = v_i(t) - K * sum_j W_ij * tanh(1.5*(x_i-x_j)) - gamma*v_i + eta_i

Parameters:

K=0.02
gamma=0.02
sigma_process=0.003
edge_p=0.12
edge weights uniform in [0.2,1.0]

Initial x_i uniform [-1,1], v_i uniform [-0.2,0.2].

## Observation and inference

Full observation is used for this scaling experiment. No observation noise is added, to isolate size scaling from the Ω-DM-005 observation attack.

The inference remains the symmetric non-negative relation reconstruction used in R3/Ω-DM-004. Lambda grid remains:

{0.1, 0.3, 1, 3, 10, 30, 100}

Training length and test length are fixed at 40 and 20 trajectories, each of length 80.

## Seeds

For each N use 10 independent main seeds:

20261001..20261010 for N=24
20261011..20261020 for N=48
20261021..20261030 for N=96
20261031..20261040 for N=192

Seed assignment is fixed before execution.

## Primary metrics

1. Relative held-out RMSE improvement at h=1,2,5,10 versus zero-relation baseline.
2. Active-edge density:
   active_edges / [N*(N-1)/2].
3. True-edge density.
4. Ratio active_edges / true_edges.
5. Median and mean inferred edge weight among active edges.
6. Held-out RMSE as an absolute metric.

## Scaling hypothesis

H1: The predictive relation signal remains positive as N increases, and active-edge density remains bounded rather than diverging with system size.

H0: The predictive signal disappears or the inferred structure becomes a size-dependent artifact, with no stable scaling relation.

No functional exponent or exact scaling form is fitted before the primary results. Any exponent fit is secondary/post-hoc.

## Controls

For every N, run 5 W=0 null seeds and 5 temporal-permutation controls using the same seed ranges offset by +100.

A control passes if the inference selects the empty graph or provides no systematic held-out advantage.

## Acceptance / falsification

This experiment is not a binary claim of physical validity.

PASS-SCALING requires:

- positive mean held-out improvement at all four N values for h=1;
- no systematic control advantage;
- the scaling of active-edge density is reported rather than assumed;
- results are reproducible across the independent seeds.

FAIL-SCALING if the predictive advantage collapses systematically with N or controls reproduce the effect.

INCONCLUSIVE if numerical conditioning, runtime, or finite-size effects prevent a clean comparison.

## Important limitation

This is a synthetic finite-network scaling test. A stable scaling law here is evidence about the mathematical model class, not evidence that the physical universe is a relational network.

No gravity, dark matter, spacetime, or cosmological interpretation is used as an input to this experiment.

## Certification rule

This protocol must remain unchanged during the certification rerun. Any implementation correction affecting the estimator, generator, seeds, metrics, or acceptance rule requires a new protocol commit before rerunning certification.
