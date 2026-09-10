# Ω-DM-002 R3 — Execution Status

**Status:** IMPLEMENTATION COMMITTED / EXECUTION NOT YET CERTIFIED

## Implementation

A dedicated joint symmetric non-negative L1 executor is now committed as:

`experiments/Ω-DM-002/run_r3.py`

Commit containing the executor: `4dfc703dae6d338b8e5a03b28bfaccd7a253d037`.

The implementation follows the preregistered R3 structure: joint edge design, non-negative L1 coordinate descent, fixed lambda grid `{0.1, 0.3, 1, 3, 10, 30, 100}`, training-only BIC-like selection, frozen held-out evaluation at horizons 1/2/5/10, null controls, and temporal-permutation controls.

## Certification boundary

The official R3 numerical result is **not** recorded yet. The current execution environment cannot retrieve the newly committed GitHub source into the isolated local runtime, so no fabricated numerical output is accepted.

This is deliberately distinct from both PASS and FAIL:

`CODE READY ≠ EXECUTED ≠ VALIDATED`

The previously recorded local exploratory R3 calculation remains an engineering audit only and is not promoted to an official result.

## Next gate

Once the committed executor is actually run in a reproducible runtime, archive:

- exact output;
- runtime/Python version;
- code commit;
- full lambda-grid table;
- main/null/permutation results;
- final decision.

Only then may Ω-DM-003 minimal-core execution proceed.
