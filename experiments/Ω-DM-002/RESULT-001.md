# Ω-DM-002 — RESULT-001

**Status:** IMPLEMENTED / NOT EXECUTED
**Classification:** INVALID for scientific inference until the executable is actually run and independently checked.

## Implementation state

The hidden-topology reconstruction routine is now implemented in `run_reconstruct.py`.

The inference routine receives observed trajectories only. The generating `W` is used by the synthetic generator and is not passed to `reconstruct()`.

The candidate graph is frozen before held-out scoring. Null and topology-permutation controls are defined.

## Important audit note

The current estimator is intentionally simple: each candidate edge is scored independently from observed acceleration/state differences. Correlated contributions from neighboring edges can bias individual edge weights. Therefore this implementation is a **first reconstruction gate**, not yet a claim of optimal graph recovery.

## Required execution

Run the committed script and archive:

- exact commit SHA;
- Python/runtime version;
- full JSON output;
- baseline vs reconstructed held-out rollout RMSE;
- true/recovered edge counts;
- topology recovery metrics;
- 20-seed null distribution;
- 20-seed permutation distribution;
- sensitivity to the preregistered sparsity threshold;
- independent scoring check;
- PASS/FAIL/INVALID decision.

No numerical result is claimed in this file until execution evidence is available.

## Interpretation boundary

Even a PASS would mean only that hidden relations are reconstructable in the specified synthetic dynamical system. It would not constitute evidence that gravity or dark matter is caused by relational structure.
