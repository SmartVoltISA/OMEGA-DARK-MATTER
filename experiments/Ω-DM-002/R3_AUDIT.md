# Ω-DM-002 R3 — Local Audit

**Status:** CODE READY / NOT EXECUTED

A local independent numerical check of the R3 equations was performed before treating the R3 protocol as executed.

## Finding

A straightforward joint ridge reconstruction improves held-out prediction relative to the zero-relation baseline, but the selected graph remains substantially denser than the hidden graph. With a representative run, active edges were ~72 versus 33 true edges. Therefore ridge regularization is not an adequate implementation of the preregistered minimum-structure criterion.

## Consequence

Do **not** mark R3 PASS. The implementation must use the specified L1/complexity-selection procedure rather than substitute ridge regression.

The observation is retained as an engineering audit: predictive recovery can occur before sparse structural recovery, so prediction and topology recovery must remain separate gates.

## Implementation status — 2026-09-11

A dedicated stdlib-only executor has now been committed as `run_r3.py`. It implements:

- joint symmetric non-negative edge reconstruction;
- coordinate-descent L1 fitting;
- the complete preregistered lambda grid `{0.1, 0.3, 1, 3, 10, 30, 100}`;
- training-only BIC-like complexity selection;
- frozen selected graph;
- held-out rollout evaluation at horizons 1, 2, 5 and 10;
- null and temporal-permutation control scaffolding.

Executor blob SHA: `5a93522025c18842e28aa1e285e69e89681dd45b`.

**Important:** code existence is not an execution result. The official R3 result remains **NOT EXECUTED** until the committed executor is actually run and the exact output is archived.

## Next gate

After an auditable R3 execution, run Ω-DM-003: controlled deletion of inferred relations to identify a minimal predictive relation core and test necessity versus redundancy.
