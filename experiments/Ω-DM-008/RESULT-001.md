# Ω-DM-008 — Emergent Mass / Attraction Result

Date: 2026-09-11
Status: PASS-CANDIDATE (mathematical emergence only)

## Protocol identity

Protocol was committed before the certification run: `experiments/Ω-DM-008/PROTOCOL.md`.

## Primary result

The model used only a local discrete Poisson relation:

`sum_neighbours(phi_j - phi_i) = -q_i`

with zero boundary potential, and defined the observable field as `F = -grad(phi)`.

No `1/r^2` term was present in the generator.

For 3-D cubic lattices, fitting the radial field magnitude over the preregistered interior range gave:

| L | q | exponent p in |F| ~ r^(-p) | R^2 |
|---:|---:|---:|---:|
| 41 | 1 | 2.2133 | 0.99925 |
| 61 | 1 | 2.0725 | 0.99985 |
| 81 | 1 | 2.0549 | 0.99986 |

The exponent approaches 2 as finite-size effects decrease.

## Source-strength / mass-like scaling

At L=81:

| q | fitted amplitude A |
|---:|---:|
| 1 | 0.0927149 |
| 2 | 0.1854298 |
| 4 | 0.3708596 |

Amplitude ratios are exactly 2 and 4 to numerical precision.

The q=2 field was exactly 2 times the q=1 field in the numerical solution; maximum relative residual was 0.0 at floating-point precision for the stored comparison.

Therefore q behaves as a linear relational source strength in this model.

## Dimensional controls

Using the same local Poisson construction:

- 2-D: fitted field exponent p = 1.0101, R^2 = 0.99993.
- 1-D: field magnitude is constant away from the source, p approximately 0.

Thus the inverse-square field is not a generic consequence of the fitting procedure: it changes with spatial dimension.

## What was actually established

1. A local balance equation on a 3-D lattice generates a field whose gradient has approximately inverse-square radial scaling.
2. The scaling converges toward p=2 with increasing lattice size.
3. Source strength q scales linearly with far-field amplitude.
4. Dimensional controls give different exponents.
5. The inverse-square law was not inserted into the force generator.

## What was NOT established

This does not derive physical Newtonian gravity.

The local Poisson equation was itself an input. Therefore the experiment demonstrates a known mathematical emergence route, not a derivation from the primitive Ω relation language.

It does not determine physical mass units, the gravitational constant G, relativistic gravity, lensing, cosmology, or dark matter.

Most importantly:

`inverse-square emergence != derivation of gravity`

and

`q != physical mass unless an independent inertial definition is obtained`.

## Scientific significance for Ω

The result identifies a concrete bridge worth attacking:

`local relational balance -> potential -> gradient -> inverse-square field`

The unresolved question is whether the local balance equation itself can be derived from more primitive Ω rules such as distinction, relation, conservation and boundary/feedback, rather than being imported as Poisson's equation.

## Next test

Construct an independent inertial-response experiment in which the same relational source q is measured through resistance to acceleration. Test whether the q inferred from field amplitude agrees with the q inferred from inertia, without identifying either quantity with physical mass in advance.
