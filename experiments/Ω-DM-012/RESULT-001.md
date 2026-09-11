# Ω-DM-012 — RESULT-001

Status: PASS-H0
Certification date: 2026-09-11
Protocol commit: 97e628181bab844da799ddd8a266f892756b51a9
Runner commit: f67bd2bcd540657da1ad5212128155f1c80a45f0

## Primary result

100 independent connected weighted graphs were tested across N=10, 20 and 40.

The purely relational kinetic action was

T_rel = 0.5 * sum_(i,j) W_ij * (v_i - v_j)^2

For the uniform translation mode v_i=1 for every node, the measured quantities were:

- maximum absolute relational kinetic energy: 1.5765e-14
- maximum absolute total canonical momentum: 1.5765e-14
- maximum absolute Hessian quadratic form: 1.5765e-14
- required numerical tolerance: 1e-12

Therefore every primary graph satisfied the zero-translation-inertia prediction within tolerance.

## Controls

Nonuniform zero-mean velocity control:

- minimum relational kinetic energy across all 100 graphs: 3.6192655
- therefore the relational kinetic metric is nonzero away from the global translation null mode.

Positive control with an explicit absolute kinetic term m0=1:

- minimum uniform-mode kinetic energy: 5.0
- minimum uniform-mode total momentum: 10.0
- minimum uniform-mode Hessian quadratic form: 10.0

The positive control confirms that the measurement procedure detects translational inertia when an absolute kinetic term is actually supplied.

## Interpretation

PASS-H0: the null prediction is confirmed.

A kinetic action built only from pairwise velocity differences has a null global translation mode. Symmetric relational coupling and connectivity do not by themselves generate a nonzero inertial coefficient for uniform translation.

This is stronger than another graph-statistic failure: it identifies a structural degree of freedom that the purely relational action cannot represent. Ordinary translational inertia therefore requires additional structure if this action is used as the starting point.

Possible next targets are an internal field carrying the missing collective mode, boundary/embedding structure, or an additional absolute kinetic sector. Any such addition must be introduced explicitly and then tested rather than identified with mass by definition.

## What this does NOT show

This does not falsify gravity, dark matter, the equivalence principle, or relational approaches in general. It is a no-go result for this specific purely difference-based kinetic action.

It also does not imply that all relational theories lack inertia: a richer relational theory could contain additional dynamical degrees of freedom that carry the collective mode.
