# Ω-DM-006 — Scaling Law Result

Date: 2026-09-11
Status: INCONCLUSIVE / GENERATOR FINITE-SIZE FAILURE

## Certification status

The preregistered scaling experiment could not reach its inference gate because the frozen generator is not dynamically comparable across system sizes.

The protocol held the coupling constant K=0.02 and edge probability p=0.12 fixed while increasing N. Because expected degree grows approximately as pN, the total interaction term grows with N. The trajectories therefore become rapidly larger and increasingly ill-conditioned.

This is a valid negative methodological finding. The protocol was not modified to rescue the result.

## Diagnostic execution

Ten independent seeds were checked at each N using the frozen generator.

| N | Mean max(abs(x)) | Max max(abs(x)) | Mean trajectory SD |
|---:|---:|---:|---:|
| 24 | 14.28 | 43.97 | 1.90 |
| 48 | 160.41 | 320.07 | 10.30 |
| 96 | 6078.64 | 22138.47 | 188.50 |
| 192 | 5,361,164.54 | 37,200,415.57 | 81,410.70 |

The growth is several orders of magnitude across the tested sizes. This prevents a clean interpretation of held-out prediction as a scaling property of the relation language.

## Interpretation

The failed scaling gate does NOT show that relational prediction fails at larger N.

It shows something more basic:

`fixed local coupling + fixed edge density + unnormalized sum over neighbors`

does not define a size-stable family of dynamical systems.

The interaction term scales with the increasing number of neighbors. Therefore N cannot be changed while treating all other generator parameters as physically equivalent.

This is an important constraint on the Ω relation language: before searching for universal scaling, the generator family itself must possess a controlled thermodynamic/large-N limit.

## Scientific consequence

The earlier Ω-DM results remain valid for their preregistered finite systems. Ω-DM-006 does not add evidence for or against a physical relational substrate.

Instead it identifies a required normalization question:

`How should relational influence scale when the number of possible relations increases?`

That question is now a first-class experimental target.

## Next experiment

Ω-DM-007 should compare explicit interaction normalizations, for example:

1. raw sum: sum_j W_ij f_ij;
2. degree-normalized: (1/d_i) sum_j W_ij f_ij;
3. global-N normalized: (1/N) sum_j W_ij f_ij;
4. RMS/variance-preserving normalization.

The normalization must be preregistered and tested across N=24,48,96,192 before any claim about a scaling law is made.

## Rule extracted

A scaling law cannot be inferred from changing system size unless the underlying generator family is itself size-controlled.

`SIZE SCALING REQUIRES DYNAMIC NORMALIZATION`
