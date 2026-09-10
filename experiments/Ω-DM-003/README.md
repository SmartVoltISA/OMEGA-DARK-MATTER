# Ω-DM-003 — Minimal Relation-Core / Necessity Gate

**Status:** PROTOCOL / NOT EXECUTED

This gate follows Ω-DM-002 R3. Its purpose is to test whether an inferred relation structure contains relations that are individually necessary for predictive behavior, and to identify a minimal predictive core.

## Core distinction

`PREDICTIVE CORE ≠ GENERATING GRAPH ≠ PHYSICAL RELATION`

A relation can be predictive, redundant, compensable, or necessary under a specified model without establishing that it is a fundamental physical interaction.

## Question

Given a frozen inferred relation model `W*`, which relations are necessary for held-out predictive behavior, and can a smaller relation set preserve the required predictive performance?

## Protocol

1. Fit/select `W*` using training data only, using the fixed R3 procedure once that implementation is frozen.
2. Freeze `W*` before testing relation necessity.
3. For each active edge `e`, construct `W* - e` without refitting.
4. Measure the held-out change:

`ΔRMSE_e = RMSE(W* - e) - RMSE(W*)`

5. Repeat for multi-step rollout horizons 2, 5 and 10.
6. Compare active-edge deletions with matched control deletions of non-essential/random relations.
7. Run a second deletion mode with refitting of the remaining allowed edges. This distinguishes direct necessity from redundancy that can be compensated by neighboring relations.
8. Perform backward elimination using only training data for decisions, then freeze the resulting core and evaluate it once on held-out data.
9. Repeat across independent seeds and test order dependence.

## Necessity criterion

An edge is provisionally **necessary** under this model if its frozen deletion produces a pre-registered deterioration exceeding the tolerance defined in the protocol and the effect is distinguishable from matched deletion controls.

Necessity is model- and threshold-dependent; it is not a universal statement about nature.

## Controls

- zero-relation baseline;
- random active-edge deletion;
- non-edge deletion control;
- temporal-permutation control;
- independent trajectory seeds;
- order-dependence check for backward elimination.

## Falsification pressure

The gate is weakened or fails if:

- deleting most relations has negligible effect;
- apparent necessity disappears after compensatory refitting;
- results depend strongly on deletion order;
- random controls produce comparable effects;
- the reduced core loses held-out predictive performance;
- conclusions change materially under small threshold/grid changes.

## Interpretation boundary

A successful result demonstrates only a reproducible minimal predictive structure in the specified synthetic dynamical system. It does not derive gravity, dark matter, or a physical relational substrate.

## Provenance

- Predecessor: `Ω-DM-002/R3_PROTOCOL.md`.
- Ground-truth `W` may be used only after inference decisions for secondary topology metrics.
- Test observations are never used to choose the core.
- Every execution must archive code commit, candidate deletion table, thresholds, seed list, and held-out results.
