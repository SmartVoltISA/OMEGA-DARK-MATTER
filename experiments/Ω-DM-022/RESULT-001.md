# Ω-DM-022 — RESULT-001

**Status: PASS-H1 (model-level robustness) / physical interpretation NOT established**

## Execution
Local deterministic Python runner. Six independent heterogeneous relational media, seeds 0..5, on a 31^3 3D lattice. The local relation strengths were generated from independent positive site traits using a symmetric nonlinear endpoint rule, rather than a uniform Laplacian coefficient.

## Results
Measured radial-gradient exponents:

- seed 0: `p = 2.028347277`
- seed 1: `p = 2.037217504`
- seed 2: `p = 1.925290430`
- seed 3: `p = 1.994436384`
- seed 4: `p = 1.993695122`
- seed 5: `p = 2.035562928`

Mean: `p = 2.002424941`

Sample standard deviation: `0.0425919606`

RMS deviation from 2: `0.0389565093`

## Interpretation
H1 is supported for this specified model class. The inverse-square-like environmental response survives substantial local heterogeneity and a nonlinear symmetric rule for generating relation strengths. The result is therefore not tied to a single uniform coefficient or radial kernel.

The experiment still explicitly enforces local conservation through balanced pairwise flux terms. Consequently, this is a robustness result for the mechanism identified in Ω-DM-021, not a derivation of conservation itself.

No inverse-square radial kernel, gravitational force, gravitational constant, or dark-matter term was inserted.

## Scientific boundary
This result does **not** establish physical gravity or dark matter. It shows that a conserved local relational network in 3D can robustly produce an approximately inverse-square environmental gradient even when relation strengths are heterogeneous and generated nonlinearly from local traits.

The next decisive test is to broaden the operator further: allow directed/nonreciprocal local relations and separately test which conservation symmetry, if any, is sufficient to retain the inverse-square scaling.

## Reproducibility
Runner: `experiments/Ω-DM-022/run_r22.py`

Commits:
- Protocol: `9c161bbee30ec3a58be272a2ebffa7356e20a7c7`
- Runner: `3a7e51a1d847c4eb5e6e2db0bcbe3462ea810ece`
