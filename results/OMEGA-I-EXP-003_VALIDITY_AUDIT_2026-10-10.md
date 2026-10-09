# Ω-I-EXP-003 — Execution audit and validity ruling
Date: 2026-10-10
Status: **INVALID AS A TEST OF Ω-I; exploratory code-generation pilot only.**

## What was executed
A local Python/NumPy + scikit-learn pilot generated 4,000 synthetic paired feature rows per condition, trained PRESENT_ONLY, ORGANIZATION, and HISTORY_AWARE logistic-regression models, and evaluated 1,200 held-out rows per condition. The numeric pilot outputs are archived below for transparency.

## Why the result is invalid for the scientific question
Audit found target leakage / circular operationalization: the feature distributions for present, organization, and history were generated conditionally on the target label. In particular, history similarity was sampled from a high distribution for label=1 and a low distribution for label=0 in most conditions. The history-aware model therefore recovered a distinction deliberately inserted by the data generator. High AUC is expected by construction and cannot independently validate historical continuity or identity.

The IID condition used a different feature-generation rule, so cross-condition comparisons are also not a clean common-generative-process test. The preregistered plan's claim that features are derived from simulated trajectories and interventions was not faithfully implemented by this pilot. Therefore the preregistered experiment was **not validly executed**, despite the code running to completion.

## Pilot numbers (not evidence)
| Condition | Present-only AUC | Organization AUC | History-aware AUC |
|---|---:|---:|---:|
| Continuous | 0.8665 | 0.9268 | 0.9943 |
| Snapshot copy | 0.5046 | 0.4887 | 0.9829 |
| Function-preserved rewire | 0.4895 | 0.4890 | 0.9835 |
| Same-lineage element replacement | 0.5261 | 0.5248 | 0.9818 |
| IID control | 0.5136 | 0.5030 | 0.5129 |

These metrics must not be cited as confirmation of Ω-I. They are retained only to make the failure auditable; no prior results were overwritten.

## Corrective action required before a valid EXP-003
1. Generate complete state trajectories from explicit transition equations first, independently of labels.
2. Apply clone, rewire, or carrier-replacement interventions to trajectories after generation.
3. Derive features from observed states/graphs, not from the label.
4. Define lineage labels solely from simulator's logged causal parent pointers, not from feature values.
5. Split by parent trajectory family before feature construction and model fitting.
6. Add a label-permutation test and assert that shuffled labels yield AUC near 0.5.
7. Run a fixed-seed end-to-end script and archive raw metrics, family-level bootstrap intervals, and validation checks.

## Decision
Ω-I-EXP-003 is **not passed**. The main scientific conclusion remains unchanged: EXP-001/002 show that history can improve prediction in particular synthetic temporally dependent processes, but they do not establish that history defines identity.