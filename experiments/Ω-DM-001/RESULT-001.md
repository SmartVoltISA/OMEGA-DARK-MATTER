# Ω-DM-001 — RESULT-001

**Status:** EXECUTED LOCALLY / CONTROL AUDIT COMPLETE
**Classification:** PASS for the narrow synthetic recovery test; NOT evidence for physical dark matter or gravity.

## Execution

The reference implementation was independently reproduced from the committed algorithm using Python stdlib-only arithmetic. GitHub commit containing the corrected executable: `64e062b701676cb38285b4fcc85e6c1f4768c6dd`.

Fixed parameters:
- seed: `20260911`
- N: `80`
- train/test: `56/24`
- `A_true = 2.0`
- `lambda_true = 0.65`
- `eps = 0.20`
- kernel width: `0.45`
- noise sigma: `0.015`
- null repetitions: `20`
- permutation repetitions: `20`

## Main recovery

For the original generating relation topology:

- visible-only M0: `A = 2.4783989771`
- relation-aware M1: `A = 2.0005088559`
- recovered `lambda = 0.6536026375`
- held-out RMSE M0: `0.0183405481`
- held-out RMSE M1: `0.0167181599`
- held-out RMSE improvement: `0.0016223882`

The injected relational coefficient `0.65` was recovered as `0.6536` in this fixed-seed run.

## Control audit

### Null injection

With `lambda = 0` over 20 seeds, mean held-out RMSE improvement from adding the relation term was approximately:

`-0.00004797`

So the extra relation parameter did not produce a systematic held-out gain in the null condition.

### Topology permutation

The first implementation contained a control flaw: it shuffled weights on the same edge-pair set and also generated the observations from the shuffled graph. That was invalid as a topology-destroying control.

This was **caught and corrected before accepting the result**. The corrected implementation:

1. generates observations from the original graph;
2. creates a separate random topology preserving edge count and weight multiset;
3. uses that randomized topology only as the fitted relation basis.

Across 20 permutation seeds, mean held-out RMSE improvement was approximately:

`-0.00050946`

with population SD approximately `0.00106496`.

The permutation control therefore does not reproduce the main positive improvement.

## Decision

**PASS — synthetic identifiability gate.**

The test supports only this narrow statement:

> In this explicitly constructed toy generator, a hidden relational contribution can be recovered from held-out synthetic observations when the correct relational basis is supplied, while the tested null and topology-destroyed controls do not show the same systematic improvement.

## Critical limitation

The generator itself explicitly defines the relational contribution with an inverse-square kernel. Therefore this experiment does **not** derive gravity, explain dark matter, establish a physical relational field, or distinguish Ω-DM from established gravitational theory.

The result is a methodological gate: **the relation-state → observable pipeline can be identifiable in a controlled synthetic setting.**

## Next required gate

Ω-DM-002 should remove the privileged knowledge of the generating relational basis and test whether a relation model can be selected/reconstructed from observables under preregistered complexity control. Only after that should the programme move toward real astronomical data.
