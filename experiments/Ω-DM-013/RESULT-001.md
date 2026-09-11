# Ω-DM-013 — RESULT-001

Status: FAIL-H1
Certification date: 2026-09-11
Protocol commit: d8fe3358e602251168b17ca117094b026d8cf083
Runner commit: 782c84c5899d6d3f9949f6247b6b39d3af9f041b

## Primary result

60 independent connected weighted graphs were tested across N=12, 20 and 32.

The proposed internal edge state y_ij does NOT lift the global translation null mode.

For every graph and every tested velocity scale U in {0.5, 1.0, 2.0}:

- m_eff = 0 exactly for the prescribed ground-state translation protocol;
- fraction with nonzero m_eff = 0/60;
- m_eff / S_W = 0 for all graphs.

The minimum total relational weight S_W across the 60 graphs was 6.9510731863, so the null result is not caused by empty graphs.

## Why

The complete preregistered action depends on x only through pair differences x_i-x_j. A uniform translation x_i -> x_i+a leaves every pair difference unchanged. The edge variables y_ij are internal relative variables and, when initialized in their ground state with zero velocity, are unchanged by this collective translation.

Therefore the global translation remains an exact symmetry/null mode. The internal edge dynamics proposed here do not couple to the collective coordinate.

## Interpretation

H1 is NOT supported.

This is a stronger structural negative result than Ω-DM-012: merely giving the relations their own internal scalar dynamics is insufficient if those dynamics remain functions only of internal pair differences.

The result identifies the missing ingredient more sharply. To obtain emergent translational inertia without inserting an absolute mass term, the relational theory needs an internal degree of freedom that actually transforms or responds under collective translation, or an additional relational structure that defines translation relative to something dynamical.

## Scientific scope

This does not falsify gravity, dark matter, inertia, the equivalence principle, or relational theories generally. It is a no-go result for this specific difference-only internal-edge construction.

No physical mass was inserted and no inverse-square interaction was used.

## Next target

Do not add an absolute kinetic term. The next principled test should introduce a genuinely dynamical reference/medium relation, such that collective motion is relational to an internal field or frame rather than only to pairwise node differences. The test must determine whether a nonzero effective inertia emerges while preserving translational symmetry in an enlarged state space.