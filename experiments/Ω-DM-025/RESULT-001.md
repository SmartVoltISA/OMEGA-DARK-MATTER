# Ω-DM-025 — RESULT-001

**Status: PASS-H1 (structural mathematical mechanism) / physical interpretation NOT established**

## Execution
Local deterministic Python execution, 3D lattice N=21, six independent heterogeneous media (seeds 0..5).

The primitive conservation rule is an elementary antisymmetric pair exchange: one unit of relational quantity removed from one endpoint is added to the other. Conservation therefore exists at the event/update rule level; it is not introduced as a Laplacian equation.

## Conserved runs
Measured radial-gradient exponents:

- seed 0: p = 1.912084
- seed 1: p = 1.909703
- seed 2: p = 1.903668
- seed 3: p = 1.915834
- seed 4: p = 1.921947
- seed 5: p = 1.942756

Mean p = 1.917665.

Shell flux was numerically constant in every tested realization to machine precision; the measured mean flux was 1 for unit source. The finite-size/heterogeneous lattice shifts the fitted radial exponent below 2, but remains within the preregistered tolerance |p-2| <= 0.15.

## Source scaling
For seed 0, source amplitudes 0.5, 1, 2 produced mean shell fluxes:

0.5, 1.0, 2.0

within numerical precision. This confirms linear scaling of the conserved flux with source amplitude in this model.

## Leakage control
Adding local loss mu=0.01 changed the fitted exponents to approximately 2.049, 2.047, 2.040 for seeds 0..2 and reduced the conserved quantity away from the source. The control is directionally consistent with screened/modified response, but the exponent alone is not used as evidence of a particular screening law.

## Interpretation
H1 is supported for the tested construction: an elementary local exchange rule can generate conservation before any Laplacian representation is written, and the resulting 3D environmental response is approximately inverse-square-like.

This is an important upstream result relative to Ω-DM-021..024: conservation need not be postulated as a matrix/operator axiom if it follows from antisymmetric local exchange.

## Scientific boundary
This does not establish physical gravity or dark matter. The model still assumes locality, pairwise exchange, a 3D lattice, and a linear difference-dependent exchange law. The next robustness target is to remove linearity and fixed lattice geometry while preserving only antisymmetric local exchange, then test whether the same dimensional scaling survives.

## Reproducibility
Protocol commit: `acfae4d359d83e7a52697c0317a70a07a322d093`
Runner commit: `0bdaa510d506a64971c3ae3401e65407dbf50392`
