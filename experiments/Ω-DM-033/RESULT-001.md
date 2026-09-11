# Ω-DM-033 — RESULT-001

**Status: FAIL-H1 / H0 RETAINED**

## Execution
The preregistered smaller stress test was executed locally with N=120, two initial ensembles, six seeds each, 30 rewiring rounds, and six measurement sources per realization.

The dynamics uses only graph-local Forman-type curvature and degree-preserving 2-switches. No coordinates or target dimension were supplied.

## Results

### Random 6-regular
Seed-level effective dimensions:

- 0: 1.19413
- 1: 1.17636
- 2: 1.28118
- 3: 1.17906
- 4: 1.19561
- 5: 1.18518

Mean d_eff = 1.20192; sample SD = 0.03959.

### Watts-Strogatz small-world
Seed-level effective dimensions:

- 0: 0.03162
- 1: 0.46708
- 2: 0.36450
- 3: 0.37805
- 4: 0.61812
- 5: 0.16631

Mean d_eff = 0.33761; sample SD = 0.21013.

## Decision
Neither ensemble approaches d_eff≈3. The regular ensemble is comparatively stable but near 1.2, while the small-world ensemble is lower and more dispersed.

**H1 is rejected for this curvature-regulation rule. H0 is retained.**

This does not prove that curvature regulation can never produce three-dimensional relational geometry. It falsifies the tested simple curvature-neutral rewiring mechanism as a robust selector of d_eff≈3.

## Important computational note
Ω-DM-032's exact N=500 runner was also attempted locally but exceeded the execution time budget before completion. Therefore Ω-DM-032 remains unchanged and is not retroactively marked executed. Ω-DM-033 is the separately preregistered smaller stress test that did complete.

## Scope
No physical spacetime, gravity, or dark matter claim is made.
