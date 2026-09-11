# Ω-DM-015 — Relational attraction from stiffness and density

Status: PREREGISTERED
Date: 2026-09-11

## Question

Can attraction between two localized relational structures arise from the same relation-first dynamics used in Ω-DM-014, without inserting an attractive force law such as 1/r^2?

## Model

Use the one-dimensional relational field

T = 0.5 * sum_i qdot_i^2
V = 0.5 * k * sum_i (q_(i+1)-q_i)^2 + sum_i lambda/4 * (q_i^2 - 1)^2

with k=1 and lambda=1.

No pairwise attraction term is added. The only interactions are local state differences and the internal double-well state dynamics.

## Two-body excitation

Prepare a kink and antikink separated by distance R. Define the interaction energy

V_int(R) = E_pair(R) - E_kink - E_antikink.

The radial force proxy is

F(R) = -dV_int/dR.

Attraction requires F(R) < 0 over a resolved interval of R, meaning the energy decreases when the two structures approach.

## Primary hypothesis H1

A genuine attractive interaction emerges from overlap/reorganization of the relational structures, with:

1. F(R) < 0 for at least 4 consecutive separations;
2. V_int(R) < 0 over the same interval;
3. the sign survives grid refinement;
4. the interaction is not produced by an explicitly inserted force law.

## Secondary question

Determine the range law of the emergent attraction. Test exponential, power-law and other simple decays. Do not assume inverse-square behavior.

A power-law candidate is only considered supported if the fitted exponent is stable under system-size and fitting-window changes and clearly outperforms exponential decay.

## Density/stiffness sweep

Repeat for k in {0.5,1,2} and bond-density d in {0.50,0.75,1.00}. Disconnected realizations are excluded from the primary connected sample.

## Controls

1. Single-defect control: no second excitation, so no two-body interaction should be inferred.
2. Large-separation control: interaction must approach numerical zero.
3. Grid refinement.
4. Symmetric exchange control: swapping kink and antikink must preserve the interaction curve.
5. No explicit 1/R, 1/R^2, or pairwise force term is allowed.

## Interpretation

PASS would establish emergent attraction in this concrete relational field model. It would NOT establish gravitational attraction or dark matter physics.

A particularly important result would be a positive attraction combined with Ω-DM-014's emergent inertial coefficient, because that would give the pair

internal structure -> effective inertia
internal structure -> attraction

without manually adding mass or an attractive force law.

The next stage would then test whether the same construction can produce a long-range law and whether source strength and inertial response are independently related.

All equations use plain text for display-safe reproducibility.