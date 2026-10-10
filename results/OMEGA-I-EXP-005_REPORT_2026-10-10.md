# Ω-I-EXP-005 — Exploratory lineage-feature benchmark
Date: 2026-10-10
Execution: local Python/NumPy/scikit-learn. **Exploratory run; protocol was not preregistered before execution.** No GitHub Actions/CI run.

## Design
Generated 500 independent trajectory families, each with an 8-dimensional stable linear process. Built 4,000 pair examples: 2,000 same-lineage pairs from a trajectory and 2,000 independent branch pairs cloned from a common state. Train/test split was grouped by trajectory family (70/30) to avoid the same family appearing on both sides. Compared current-state distance, organization summary, and history/transition features. Lineage labels came from simulator construction, not from a feature threshold.

## Held-out metrics
| Model | ROC-AUC | Balanced accuracy |
|---|---:|---:|
| PRESENT_ONLY | 0.58866 | 0.56417 |
| ORGANIZATION | 0.58866 | 0.56417 |
| HISTORY_AWARE | 0.76955 | 0.70583 |

Family-level bootstrap 95% CI:
- History-aware AUC: [0.73897, 0.79811]
- Present-only AUC: [0.55464, 0.62377]
- AUC improvement (history minus present): [0.14768, 0.21495]

A 100-repeat shuffled-training-label control had AUC median 0.46938 and mean 0.48272; its range was wide [0.24050, 0.74224], indicating this control/model setup is noisy and needs a stronger permutation protocol before confirmatory use.

## Interpretation
History/transition features classified the simulator's stipulated same-lineage versus independent-branch label better than current-state distance alone. The organization feature was constant in this particular construction and therefore added no information; this is a design limitation, not evidence that organization never matters.

## Validity limitations
This is exploratory, not preregistered, and not confirmatory. Positive and negative pairs were constructed by different sampling procedures, and same-lineage pairs are temporally separated points from one path while negative pairs are independent continuations after a clone point. The classifier may learn these construction-specific distribution differences. The lineage label is an operational simulator label. The result does **not** establish that history defines personal identity, organism identity, consciousness, or a law of nature.

## Decision
Signal is promising only as a benchmark-development result. Do not mark Ω-I as confirmed. Next step: preregister a balanced, matched intervention benchmark with multiple transition families, informative organization features, label-permutation tests, and matched-pair bootstrap.
