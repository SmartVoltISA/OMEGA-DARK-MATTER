# Ω-I-EXP-004 — Trajectory-first results
Date: 2026-10-10
Execution: local Python / NumPy / scikit-learn. No GitHub Actions/CI run.
Preregistration: [protocol](../experiments/OMEGA-I-EXP-004_PREREGISTRATION_2026-10-10.md)

## Results
| Condition | Current-only RMSE | History-5 RMSE | Shuffled-target RMSE | Paired improvement | 95% bootstrap CI |
|---|---:|---:|---:|---:|---:|
| AR1 | 1.57259 | 1.53780 | 1.93760 | 0.03475 | [0.03169, 0.03780] |
| IID | 1.41055 | 1.41058 | 1.41057 | -0.00002 | [-0.00013, 0.00010] |
| Regime switch | 1.95858 | 1.71344 | 1.95832 | 0.24372 | [0.22758, 0.26008] |
| Damped oscillator | 1.38021 | 1.35704 | 1.65277 | 0.02311 | [0.02009, 0.02623] |

## Validity checks
Trajectories were generated from explicit transition equations independently of model fitting and outcome labels. Data split by trajectory index: 140 training and 60 held-out trajectories per condition, each length 600. All reported values were computed locally from fixed seeds. The IID control's paired interval includes zero; history has no measurable benefit there. Shuffled-target is a deliberately corrupted training control.

## Interpretation
This valid trajectory-first run supports a narrow predictive claim: five past observations improve next-observation prediction in these AR1, regime-switch, and damped-oscillator synthetic processes, while they do not improve IID prediction. The largest effect occurs in the regime-switch process, where lagged observations help a fixed linear model adapt to the changed dynamics. This is not a test of identity itself and does not prove that history defines a person, organism, system, consciousness, time, or physical law.

## Relationship to EXP-003
The preceding EXP-003 classification pilot was audited and marked INVALID due to target leakage; its high AUC values must not be treated as evidence. EXP-004 is the corrected trajectory-first predictive experiment. No prior artifacts were overwritten.
