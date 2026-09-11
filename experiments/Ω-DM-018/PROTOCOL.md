# Ω-DM-018 — Blind Relational Environmental Response

## Objective

Test whether an inverse-square environmental response can be recovered from a general relational operator without explicitly inserting a Laplacian, Poisson equation, inverse-square force, gravitational potential, or gravitational constant.

## Core question

Given a localized intervention in one element of a relational medium, can the change in the surrounding relational state be reconstructed as an empirical response kernel?

We measure:

`ΔR = R(environment | intervention) - R(environment | control)`

The object of inference is the environmental response, not a presumed force or entity.

## Model family

Use a 3D lattice solely as an observation index. Construct a random symmetric positive local relational operator from nearest-neighbour and next-nearest-neighbour couplings, with independently sampled positive weights. Do not construct the operator as a discrete Laplacian and do not tune weights to reproduce a known radial law.

For each realization:

`A_ij = A_ji >= 0`

for permitted local relations. The response field is obtained from the linear relational equilibrium

`A x = b`

with one pinned reference degree of freedom to remove the global gauge mode. The intervention is a localized source vector `b`; the control uses `b=0`.

The analysis must not use the expected exponent when fitting.

## Blind analysis

Before looking at radial results, generate and save the response fields and the analysis metadata. Candidate response laws are:

1. power law `r^-p`
2. exponential `exp(-r/L)`
3. screened power law `r^-p exp(-r/L)`
4. finite-size polynomial alternatives

Fit all candidates over predeclared interior ranges. Report residuals and information criteria. Do not select inverse-square in advance.

## Primary observable

The primary observable is the magnitude of the radial gradient of the environmental response:

`G(r) = |d <ΔR>/dr|`

where `<...>` is a shell average after centering on the intervention location.

Secondary observable: shell-averaged response `<ΔR>(r)`.

## Controls

- zero-intervention control
- randomized source-location control
- relation-weight permutation control preserving the weight distribution
- isotropic versus anisotropic coupling realization
- resolution/finite-size check

## Success criterion

A model-level H1 requires:

- power-law family preferred over exponential/screened alternatives by a predeclared information criterion;
- fitted exponent stable across at least three independent random realizations and interior ranges;
- exponent confidence intervals overlap 2 within the preregistered tolerance;
- randomized controls fail to reproduce the same radial law.

This does NOT constitute a gravity or dark-matter claim. It only establishes an emergent environmental response law in the specified relation system.

## Falsification

H0 is retained if the exponent is unstable, screened/exponential models are preferred, permutation controls reproduce the effect, or the apparent power law disappears under resolution or realization changes.

## Reproducibility

Record random seeds, lattice size, relation-generation rule, coupling ranges, boundary condition, pinned degree, source amplitude, solver tolerance, fit ranges, candidate models, metrics, and all raw radial summaries.
