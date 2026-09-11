# Ω-DM-026 — Nonlinear local exchange on irregular geometry

## Question
Does an inverse-square-like environmental response survive when the regular lattice is removed and local exchange is nonlinear, while retaining only locality and antisymmetric pair exchange?

## H1
A stable radial response exponent near p=2 in 3D remains across independent irregular realizations and moderate nonlinear response strength.

## H0
The p≈2 behavior is not robust under this generalization; geometry/nonlinearity changes the exponent or destroys a stable scaling regime.

## Model
- 3D random point cloud inside a unit ball.
- Local connectivity: Delaunay tetrahedralization; edges are local and irregular.
- Positive edge conductance: w_ij = 1/(|x_i-x_j|+0.03).
- Boundary nodes with |x|>0.90 are pinned to u=0.
- Central source is the point closest to the origin.
- Pair current is antisymmetric:
  J_ij = w_ij*tanh(alpha*(u_i-u_j))/alpha,
  J_ji = -J_ij.
- Equilibrium is obtained by minimizing the corresponding convex pair-energy minus source work.

No inverse-square term, Poisson equation, gravitational constant, or gravitational force is inserted.

## Measurements
1. Radial environmental response u(r).
2. Potential exponent q from u(r) ~ r^-q; reported gradient exponent p=q+1.
3. Direct current through spherical cuts; conservation is checked independently.
4. Independent random seeds.
5. Source-amplitude stress test to expose nonlinear regime changes.

## Acceptance
H1 requires p close to 2 with small seed-to-seed spread in the preregistered moderate-response regime and conservation error near numerical precision. Otherwise retain H0/inconclusive.

## Important scope
A positive result would establish only a model-level structural mechanism. It would not establish physical gravity or dark matter without a mapping to measured physical observables and independent empirical validation.
