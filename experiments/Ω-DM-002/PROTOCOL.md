# Ω-DM-002 — Hidden Relation Reconstruction

**Status:** PREREGISTERED PROTOCOL / NOT YET EXECUTED
**Scope:** synthetic inference only

## Question

Can the structure of a hidden relational network be reconstructed from observed state transitions **without supplying the generating topology to the inference model**?

Ω-DM-001 supplied the correct relation basis and therefore tested identifiability conditional on privileged structural knowledge. Ω-DM-002 removes that privilege.

## H1 / H0

**H1:** observed trajectories contain enough information to recover a compact hidden relational structure that improves prediction on held-out trajectories beyond a no-relation baseline and topology-matched nulls.

**H0:** any apparent relation recovery is explained by noise, ordinary state dynamics, over-parameterization, or topology-independent statistics.

## Generative system

For N nodes with scalar state x_i(t), define a hidden weighted undirected graph W with W_ii=0 and W_ij≥0.

The synthetic transition law is:

`x_i(t+1) = x_i(t) + v_i(t)`

`v_i(t+1) = v_i(t) - k * sum_j W_ij * (x_i(t)-x_j(t)) - gamma*v_i(t) + eta_i(t)`

Here W is the hidden relational state. The coupling term is deliberately a **toy network interaction law**, not gravity and not a physical claim.

The inference model observes trajectories x(t), not W.

## Candidate models

**M0 — local baseline:** each node evolves from its own previous state only.

**M1 — reconstructed relation:** infer a sparse nonnegative W from training trajectories, then freeze W and evaluate prediction on held-out trajectories.

**M2 — topology null:** infer W after destroying cross-node temporal alignment while preserving per-node marginal statistics.

**M3 — degree/weight null:** randomized topology preserving node count, edge count and weight distribution.

The final test must not use test trajectories to select W or hyperparameters.

## Reconstruction constraints

To prevent trivial memorization:

- W is symmetric;
- W_ii = 0;
- W_ij ≥ 0;
- sparsity is penalized;
- parameter search grid is fixed before execution;
- training trajectories and held-out trajectories are independent;
- recovered W is frozen before held-out scoring.

## Primary metrics

1. held-out one-step RMSE;
2. multi-step rollout RMSE;
3. held-out improvement M0 → M1;
4. relation recovery precision/recall against the hidden generator, reported only as a secondary synthetic metric;
5. sparsity/complexity penalty.

## Falsification

The relation hypothesis fails this gate if:

- M1 does not improve held-out prediction;
- improvement disappears under independent trajectories;
- M2/M3 produce comparable gains;
- recovered topology is no better than the null after complexity control;
- results are unstable under preregistered seed changes.

## Required controls

At minimum:

- ≥20 independent random seeds;
- null generator with W=0;
- topology permutation preserving edge count and weight multiset;
- train/test separation;
- fixed noise level;
- sensitivity to sparsity penalty;
- at least one independent implementation/check of the scoring equations.

## Provenance

The run must record:

```text
seed(s)
N
trajectory count
trajectory length
k
gamma
noise sigma
edge-generation rule
true W hash
training/test split
candidate model grid
sparsity penalty
code commit
runtime/environment
all scores
failures/INVALID runs
```

No post-hoc topology selection is permitted.

## Interpretation boundary

Even a successful reconstruction proves only that hidden relations are recoverable in the specified synthetic dynamical system. It does **not** establish a physical relational field, gravity modification, dark matter explanation, or cosmological validity.

## Gate dependency

`Ω-DM-001 PASS` → conditional identifiability established.

`Ω-DM-002` → structural recovery without privileged topology.

Only if Ω-DM-002 survives controls should the programme consider a physically motivated inference model or astronomical data.