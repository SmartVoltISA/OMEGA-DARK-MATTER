# Ω-DM-003 — Preregistered Minimal Relation-Core Protocol

**Status:** PREREGISTERED / NOT EXECUTED

## 1. Objective

Test whether an inferred hidden relation model contains a smaller set of relations that preserves predictive behavior, and measure relation necessity by controlled deletion.

## 2. Data separation

Inference, complexity selection and core selection use training trajectories only. The held-out trajectories are touched once for final evaluation after the core is frozen.

Ground-truth `W_true` is hidden from inference and may be opened only after all inference decisions for secondary precision/recall analysis.

## 3. Starting model

The starting model is the R3 selected symmetric non-negative relation matrix `W*`. The exact R3 fitting implementation and λ-selection table must be committed before Ω-DM-003 execution.

If R3 is not executable from the committed implementation, Ω-DM-003 must remain NOT EXECUTED.

## 4. Frozen deletion test

For every active undirected edge `e` in `W*`, create `W*[-e]` by setting only that edge weight to zero. Do not refit.

Primary quantity:

`ΔRMSE_e(h) = RMSE(W*[-e], h) - RMSE(W*, h)`

for one-step prediction and rollout horizons `h ∈ {2,5,10}`.

The same held-out trajectories and initial states are used for every deletion, so comparisons are paired.

## 5. Tolerance

Before execution, use an absolute one-step RMSE tolerance of `τ = 0.01` in the native observable units. An edge is provisionally necessary in frozen mode only when:

`ΔRMSE_e(1) > τ`

and the effect is not smaller than the corresponding matched random-deletion control distribution at the preregistered control criterion.

Because the observable scale is synthetic, this threshold is a methodological parameter, not a universal constant.

## 6. Compensatory refit test

For each candidate deletion, a secondary model may refit only the remaining allowed edges using training data. This answers a different question:

- frozen deletion = direct predictive necessity;
- deletion + refit = necessity after compensation by the remaining relation structure.

No held-out data may be used for refitting or selection.

## 7. Minimal-core search

Use backward elimination on the training set:

1. start from `W*`;
2. evaluate removal candidates using training-only loss plus the preregistered complexity rule;
3. remove an edge only when the resulting training model remains within the specified predictive tolerance and is preferred by the complexity rule;
4. repeat until no eligible deletion remains;
5. freeze the final core;
6. evaluate once on held-out data.

Because greedy elimination can be order-dependent, execute at least three deterministic edge-order policies: ascending edge identifier, descending edge identifier, and smallest-training-loss-increase first. Report whether the final core is identical or materially different.

## 8. Controls

A. Random active-edge deletion controls matched to the number of tested active edges.

B. Non-edge deletion controls, which should have no direct effect because their weight is already zero.

C. Temporal-permutation control preserving marginal observations while destroying temporal relation.

D. Independent trajectory seeds for replication.

## 9. Primary outputs

- full frozen deletion table;
- `ΔRMSE` at horizons 1, 2, 5, 10;
- matched control distributions;
- final core size;
- final held-out RMSE versus full model and zero-relation baseline;
- order-dependence across the three elimination policies.

## 10. Secondary outputs

After inference is locked:

- true-edge precision/recall;
- coefficient error versus `W_true`;
- overlap of recovered core with the generating graph;
- sensitivity to tolerance `τ` in a post-hoc robustness analysis clearly separated from the preregistered decision.

## 11. Acceptance

The gate is **PASS** only if all are satisfied:

1. a reduced core is obtained;
2. the frozen core beats the zero-relation baseline on held-out one-step prediction;
3. it is not worse than the baseline at horizons 2, 5 and 10 under the same acceptance margin used for R3;
4. random deletion controls do not systematically mimic the identified necessary-edge effects;
5. the core-selection procedure shows reproducible or explicitly characterized order dependence;
6. temporal-permutation controls do not reproduce the predictive advantage.

Otherwise report FAIL or INCONCLUSIVE according to the specific failure mode; never convert an implementation failure into a scientific failure.

## 12. Interpretation boundary

PASS means only that a minimal predictive relation core is recoverable in the specified synthetic dynamical system. It does not establish that the recovered edges are fundamental physical relations and provides no direct evidence for dark matter or gravity.

## 13. Provenance

Predecessor: `Ω-DM-002/R3_PROTOCOL.md`.

Required execution record: exact code commit, Python/runtime version, seed list, protocol hash/commit, deletion table, control table, final core, held-out metrics, and interpretation.
