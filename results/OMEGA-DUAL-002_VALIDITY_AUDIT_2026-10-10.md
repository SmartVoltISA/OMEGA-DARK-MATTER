# Ω-DUAL-002 — validity audit and exploratory pilot
Date: 2026-10-10
Status: **INVALID AS CONFIRMATORY TEST; exploratory pilot only.**

## What was run
A local Python/NumPy simulation used 300 trajectories per observation-noise setting, 200 time steps each, 50 burn-in steps, and 2,000 trajectory-bootstrap resamples. Seed: 20261010. Machine-readable pilot output is archived in [OMEGA-DUAL-002_INVALID_PILOT_2026-10-10.json](OMEGA-DUAL-002_INVALID_PILOT_2026-10-10.json).

## Pilot numbers (not confirmatory)
| Observation noise σ | Coupled MSE | Uncoupled MSE | Paired improvement (uncoupled − coupled), 95% bootstrap CI | Shared-sensor MSE |
|---:|---:|---:|---:|---:|
| 0.1 | 0.2311 | 0.5406 | 0.3094 [0.3025, 0.3163] | 0.2298 |
| 0.5 | 0.8067 | 0.9313 | 0.1247 [0.1174, 0.1321] | 0.7749 |
| 1.0 | 1.0696 | 1.1809 | 0.1113 [0.1031, 0.1194] | 0.9785 |

The pilot appears to show lower MSE for the coupled condition than the uncoupled condition, but the shared-sensor control performs as well or better. Do not interpret these differences as evidence that specialization plus coupling is uniquely beneficial.

## Why the run is invalid against preregistration
1. The preregistered state equation included an input/control term u(t); the implementation omitted it.
2. Prediction transformations differ between conditions (tanh of a sum, average of local signs, and a separately scaled shared-sensor estimate). This makes MSE comparisons not fully capacity/output-scale matched.
3. The shuffled-message and shared-sensor controls were approximate rather than a faithful, fully matched implementation of the written protocol.
4. Although the random seed and run sizes were fixed, this mismatch means the preregistered decision rule cannot be applied as a confirmatory result.

## Decision
**No confirmatory conclusion.** Preserve this pilot as a failed validity check, not as evidence for or against a general duality principle. Next step: preregister a corrected protocol amendment before writing a corrected runner; use a common prediction range and scoring rule for every condition, explicitly implement the state update, and audit the runner against the protocol before executing.
