# Ω-DM-003 — Minimal Relation-Core / Necessity Gate

**Status: EXECUTED / PASS — synthetic gate**

This gate follows Ω-DM-002 R3. Its purpose is to test whether an inferred relation structure contains relations that are individually necessary for predictive behavior, and to identify a minimal predictive core.

## Result

The frozen R3 model contained 120 active edges. None of the 120 individual frozen deletions exceeded the preregistered one-step necessity threshold `tau=0.01`. Training-only backward elimination nevertheless produced compact predictive cores of 13, 15 and 20 edges under three deterministic order policies.

All three cores beat the zero-relation baseline at held-out horizons 1, 2, 5 and 10. The result therefore supports a **distributed, redundant predictive core**, not a unique indispensable topology.

The final core is order-dependent; this is explicitly characterized in `RESULT-001.md` rather than hidden.

## Core distinction

`PREDICTIVE CORE ≠ GENERATING GRAPH ≠ PHYSICAL RELATION`

A relation can be predictive, redundant, compensable, or necessary under a specified model without establishing that it is a fundamental physical interaction.

## Archived execution

- `run_core.py` — deterministic executor.
- `FROZEN_DELETION.csv` — complete 120-edge frozen deletion table.
- `RESULT-001.md` — certified interpretation and acceptance decision.

## Acceptance

**PASS for this synthetic gate.** This means only that a substantially smaller predictive relation structure can be recovered from the R3 model in the specified synthetic dynamical system. It does not establish gravity, dark matter, or a physical relational substrate.

## Next pressure test

The next gate should use independent synthetic generators and altered observables so that the predictive-core phenomenon must survive a change in the generating mechanism. Inference must remain blind to the generating topology.
