# Ω-I-EXP-002 — Results report
Date: 2026-10-10
Execution: local Python/NumPy; GitHub Actions was not run.
Preregistration: [OMEGA-I-EXP-002 preregistration](../experiments/OMEGA-I-EXP-002_PREREGISTRATION_2026-10-10.md)

## Results
| Condition | Current-only RMSE | History-5 RMSE | Shuffled-history RMSE | Improvement current − history | 95% bootstrap CI |
|---|---:|---:|---:|---:|---:|
| AR1 continuity | 1.57233 | 1.54314 | 1.93120 | 0.02917 | [0.02564, 0.03248] |
| IID negative control | 1.42080 | 1.42078 | 1.42077 | 0.000016 | [-0.000140, 0.000168] |
| Regime switch | 1.94180 | 1.70845 | 1.94445 | 0.23149 | [0.21367, 0.25017] |
| Carrier replacement, rule preserved | 1.57743 | 1.54497 | 1.96031 | 0.03236 | [0.02803, 0.03663] |

## Interpretation
1. The IID control behaves as expected: the history advantage is essentially zero and its confidence interval includes zero.
2. In the stationary AR(1) process, five lags improve held-out RMSE modestly (about 1.86% relative to current-only).
3. In the regime-switch condition, history improves RMSE more strongly. This result is exploratory: the training data span both regimes and the model has no explicit regime indicator.
4. When the carrier is notionally replaced but the scalar process and rule are preserved, history remains predictive. This shows that predictive continuity can persist despite carrier labels being irrelevant in this synthetic construction; it does not establish that the system is the same individual.
5. The shuffled-history control is a deliberately corrupted training alignment, not a fair competitor. In some conditions it yields RMSE near current-only; in others it degrades strongly.

## Decision
The experiment supports the narrow statement that history can improve prediction when the data-generating process contains temporal structure, and not when observations are IID. It does **not** establish the broad Ω-I claim that historical continuity defines identity. Ω-I remains an open hypothesis.

## Reproducibility and limitations
The preregistered split, seeds, sample sizes, models, RMSE metric, and bootstrap count were used. Results are synthetic and depend on this data-generating setup. No real-world identity, memory, biological system, or physical process was tested. No GitHub Actions/CI run was initiated.
