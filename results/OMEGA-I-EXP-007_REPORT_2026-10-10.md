# Ω-I-EXP-007 — Factorial intervention benchmark
Date: 2026-10-10
Execution: local Python/NumPy/scikit-learn; GitHub Actions/CI not run.
Preregistration: [EXP-007 protocol](../experiments/OMEGA-I-EXP-007_PREREGISTRATION_2026-10-10.md)

## Execution
Four dynamics (AR1, IID, SWITCH, OSC), 250 base families each. Four paired interventions per family yielded 4,000 rows total; 2,800 rows from the first 175 families per dynamic were used for training, and 1,200 rows from the remaining 75 families per dynamic were held out. Models were standardized logistic regression, C=1.

## Pooled held-out metrics
| Features | ROC-AUC | Balanced accuracy |
|---|---:|---:|
| Present-state distance | 0.5559 | 0.5433 |
| Present + history distance | 0.5739 | 0.5425 |
| Present + history + transition distance | 0.5771 | 0.5433 |
| Present + history + transition + organization summaries | 0.7271 | 0.7008 |

Incremental AUC from adding history to present-only: 0.0180. Family-block bootstrap 95% CI: [-0.0154, 0.0505], which includes zero. Therefore the preregistered criterion for a reliable incremental history effect was **not met**.

Per-dynamics AUC for the full feature set:
- AR1: 0.7108
- IID: 0.7261
- OSC: 0.7373
- SWITCH: 0.7184

The similarity across dynamics, including IID, warns that this classifier is partly recovering intervention/feature construction signatures rather than a unique causal-history law.

## Negative control and audit
After training with permuted labels and independently permuting held-out labels, AUC was 0.4881, near chance. The more important limitation is conceptual: the simulator defines same-lineage labels by intervention bookkeeping (continuation and element replacement = same; snapshot clone and function perturbation = different). These labels are not an independently validated definition of identity. Also, organization summaries strongly separate some intervention types; their high AUC must not be interpreted as discovering identity.

## Decision
**EXP-007 does not confirm that causal history independently defines identity.** The incremental history effect is small and statistically inconclusive under the family-block bootstrap. Organization features raise pooled classification performance, but intervention-specific artifacts and the simulator's stipulated labels prevent a universal interpretation. Ω-I remains open. The correct next step is to redesign the experiment so each intervention is factorially crossed with lineage labels and matched controls, with label-generating parent pointers hidden from feature construction.
