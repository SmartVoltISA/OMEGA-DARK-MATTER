# Ω-DM-018 — RESULT-001

Status: INCONCLUSIVE / H0 NOT REJECTED

## Local execution

A blind 3D general relational operator was tested locally across five independent random realizations (N=25 per axis). The operator used random local symmetric couplings including nearest-neighbour and diagonal-neighbour relations, plus independently sampled onsite terms. It was not constructed as a discrete Laplacian and no inverse-square law was inserted.

The environmental response to a localized intervention was shell-averaged and the radial gradient was fitted without selecting an expected exponent.

Observed fitted gradient exponents for seeds 0..4 over the predeclared interior range r=3..8 were approximately:

- seed 0: p=1.667, R²=0.623
- seed 1: p=1.055, R²=0.884
- seed 2: p=3.699, R²=0.849
- seed 3: p=0.663, R²=0.026
- seed 4: p=0.268, R²=0.008

The exponent is therefore not stable across random relational realizations.

## Interpretation

The earlier near-2 result in Ω-DM-017 cannot be treated as a generic consequence of arbitrary local relations. Once the explicitly Laplacian-like construction is removed, the inverse-square response does not robustly survive this first blind test.

This is a useful negative result. It narrows the hypothesis: locality plus a generic relational operator is insufficient, at least for this tested operator family and boundary/onsite construction.

## Important limitation

This is not a no-go theorem for relation-derived inverse-square behaviour. The tested operator family contains random onsite terms and does not enforce a conserved/divergence structure. Such terms can screen or distort long-range propagation. The next test should therefore separate structural constraints that are justified by relation dynamics from arbitrary modelling choices, while still avoiding insertion of the target law.

## Next test

Construct the most general translation-invariant, isotropic, conservative relational operator allowed by the relation definition, without writing it as a Laplacian by assumption. Infer its environmental kernel from interventions and test whether the long-range exponent is selected by the constraints themselves.
