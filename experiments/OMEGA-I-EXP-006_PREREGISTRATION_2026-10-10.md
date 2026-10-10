# Ω-I-EXP-006 — Observational identifiability of lineage under symmetric branching
Date: 2026-10-10
Status: preregistered before execution.

## Question
Can observations alone identify which of two symmetric post-clone branches is the "original" lineage when both branches share the same pre-branch history, dynamics, and observation model?

## Generative design
- 10,000 independent branch-pair trials.
- Each trial generates a common 8-dimensional pre-branch history from a stable linear dynamical system.
- At the branch point, duplicate the exact state and transition matrix into branches A and B.
- Generate both future branches with independent, identically distributed process noise and observation noise.
- Assign the simulator lineage label "original" to A or B by an independent fair coin after generating observations. This label is metadata and is independent of observed data by design.
- Features: current-state distance, five-step history distance, transition-residual distance, and organization-matrix distance.
- Evaluate a fixed logistic regression with 70/30 split, plus a direct label-permutation / symmetry sanity check.
- Fixed seed 20261010. Report held-out ROC-AUC, balanced accuracy, and binomial confidence interval for any deterministic tie-break baseline.

## Decision rule
If label assignment is independent of all observable features, observational prediction should be at chance (AUC approximately 0.5, balanced accuracy approximately 0.5). Any material deviation triggers an implementation audit. This is not a failure of the model; it demonstrates non-identifiability under the specified observational equivalence.

## Limits
This tests identifiability in a synthetic symmetric setup, not a universal claim that identity can never be inferred. Additional external records or asymmetric causal interventions could change the problem. It does not settle personal identity or physics.