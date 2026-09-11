# Ω-DM-023 — Directed Relational Conservation

## Question
Can an inverse-square-like environmental response survive when local relations are directed/nonreciprocal, and which conservation symmetry is actually sufficient?

## Relation-first framing
A localized intervention changes the relational state of an environment. We measure that change as ΔR(r), its radial gradient G(r), and the directed relational flux through shells.

## Hypotheses
H1: A directed local relational medium can retain approximately constant shell flux and an inverse-square-like radial gradient in 3D if it satisfies a generalized node-wise conservation law.

H0: Breaking reciprocity while retaining locality destroys the conservation→geometry mechanism and does not robustly yield p≈2.

## Model classes
A. Balanced directed medium: each directed edge has positive conductance, with outgoing weights normalized so node-wise total exported capacity equals node-wise total imported capacity. The steady state is defined by directed flux balance.

B. Unbalanced directed control: same local directed construction, but independently perturb the outgoing/imported balance while keeping locality and positive edge strengths.

No radial kernel, inverse-square term, gravitational force, G, mass, or dark-matter term is allowed.

## Measurements
1. Solve steady relational state for a localized source and zero outer boundary.
2. For every interior shell, compute directed outward flux Q(r) from directed edge currents crossing the shell.
3. Fit radial response gradient G(r) ~ r^-p.
4. Primary conservation diagnostic: coefficient of variation of Q(r).
5. Test source amplitudes 0.5, 1, 2 for linear flux scaling.
6. Repeat over seeds 0..5.

## Decision rule
H1 is supported only if the balanced directed class has near-constant interior flux and mean |p-2| <= 0.10, while the unbalanced control loses flux conservation and does not reproduce the same scaling robustly.

## Scientific boundary
Even a PASS establishes only a mathematical mechanism for the specified relational class. It does not establish physical gravity or dark matter.
