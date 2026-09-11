# Ω-DM-022 — Protocol

## Question
Does the conservation -> geometry -> inverse-square mechanism survive when the local relational operator is no longer a uniform Laplacian, but is generated from heterogeneous, nonlinear local relation rules?

## H1
For a localized intervention in a 3D local relational system, if the resulting edge flux is conserved and the operator remains local and symmetric, the far/interior radial environmental response should remain approximately inverse-square: G(r) ~ r^-2, despite heterogeneous relation strengths.

## H0
The inverse-square response requires the uniform Laplacian-like operator used in Ω-DM-019/021; replacing it with a broader heterogeneous local relational rule destroys the exponent near 2.

## Construction
- 3D cubic lattice N=31.
- Zero Dirichlet boundary.
- One localized unit intervention at the center.
- Only nearest-neighbour relations.
- Each lattice site receives an independent positive latent relational trait.
- Each edge conductance is generated locally from the two endpoint traits by a nonlinear symmetric rule:
  w_ij = sqrt(s_i*s_j) * (1 + 0.35*sin(s_i-s_j)), clipped to remain positive.
- The operator is assembled solely from these local edge relations, with balanced diagonal terms so that pairwise internal flux is conserved.
- No radial kernel, inverse-square term, gravitational force, gravitational constant, or Poisson radial solution is inserted.

## Measurement
1. Solve the static relational response to the localized intervention.
2. Compute shell-averaged radial response.
3. Estimate radial gradient G(r).
4. Fit log(G) against log(r) over the interior range r=3..11.
5. Repeat for six independent random relational media (seeds 0..5).

## Primary criterion
H1 is supported at model level if the six-seed mean exponent is close to 2 and the individual realizations remain reasonably close without tuning a radial law.

## Important limitation
The balanced diagonal construction still enforces conservation. This experiment therefore tests robustness of the conservation mechanism under heterogeneous/nonlinear local relation weights; it does not yet remove conservation itself as an assumption.

## Reproducibility
Runner: `experiments/Ω-DM-022/run_r22.py`
