# Ω-I-EXP-006 — Symmetric lineage identifiability
Date: 2026-10-10
Execution: local Python/NumPy/scikit-learn. No GitHub Actions/CI run.
Preregistered protocol: [EXP-006 preregistration](../experiments/OMEGA-I-EXP-006_PREREGISTRATION_2026-10-10.md)

## Results
- Independent branch-pair trials: 10,000
- Samples: 20,000 branch observations
- Training: 14,000 samples; held-out test: 6,000 samples, split by pair
- Held-out ROC-AUC: **0.50219**
- Balanced accuracy: **0.49983**
- Accuracy choosing which branch is labelled original within held-out pairs: **0.50333**
- Approximate 95% interval for paired-choice accuracy: **[0.48544, 0.52123]**

## Interpretation
The classifier performs at chance. This is the expected result because the "original" label is assigned by a fair coin independently of the observations, while both branches share the same pre-branch state and transition rule and have identically distributed noise. There is no observational signal that can reveal the arbitrary lineage label.

This is an important boundary condition: **causal provenance cannot be inferred from observations when the label is deliberately independent of all observable data**. External lineage records or an asymmetric intervention would change the available information.

## Decision
EXP-006 passes its intended sanity check. It does not show that identity is always unknowable; it shows non-identifiability under this symmetric setup. Combined with EXP-004/005, the evidence says historical features can help predict dynamics or recover some simulator-defined distinctions, but they cannot recover a lineage label that has no observable correlate. Ω-I remains open.
