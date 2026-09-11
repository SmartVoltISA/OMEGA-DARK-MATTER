# Ω-DM-021 — Conservation of Relational Flux

**Status:** PREREGISTERED / EXECUTED LOCALLY

## Question
Can an inverse-square-like environmental response arise from conservation of a relational flux through expanding shells, rather than from inserting an inverse-square law or gravitational force?

## Relation-first formulation
A localized intervention changes the relational state of an environment. Measure

`ΔR(r) = R(environment at radius r | source) - R(environment at radius r | control)`.

The primary object is the environmental response and its transport through relations, not an assumed force.

## Hypotheses
**H1:** In a 3D local, symmetric, positive, conservative relational network, a localized source produces approximately conserved outward relational flux through shells. Geometric dilution then gives a radial response gradient approximately proportional to `1/r^2`.

**H0:** Shell flux is not conserved and/or the radial gradient does not follow the expected dimensional dilution.

## Controls
A matched leaky operator adds a local leakage term `μ u` to the conservative relational balance. This control tests whether loss of conservation changes the radial law toward a screened response.

## Generator
- 3D cubic nearest-neighbour lattice.
- Positive local relation weight on every edge; baseline certification uses unit weights to isolate conservation from disorder.
- Conservative operator: sum of outward edge differences equals the localized source at the source site and zero elsewhere in the interior.
- Boundary values fixed to zero.
- No gravitational force, Newton constant, inverse-square kernel, Poisson point-source law, mass, or potential is inserted as a radial law.
- Source amplitude is one in the primary run.

## Measurements
1. Shell-averaged environmental response `u(r)`.
2. Radial response gradient `G(r) = -d<u>/dr`.
3. Direct relational edge flux crossing a spherical shell, using `J_ij = w_ij (u_i-u_j)` and summing outward crossings.
4. Power-law exponent from `G(r) ~ r^-p` over an interior range away from source and boundary.
5. Flux coefficient of variation across interior shells.

## Falsification / success criteria
Primary H1 support requires both:
- `p` close to 2 in 3D; and
- shell flux approximately constant across the same interior range.

The leaky control should show decreasing shell flux with radius and a departure from a pure inverse-square law.

## Scope
A positive result establishes a mathematical/model-level consequence of local conservative relational transport plus 3D geometry. It does **not** establish physical gravity, dark matter, or a universal law of nature.

## Reproducibility
Runner: `experiments/Ω-DM-021/run_r21.py`
