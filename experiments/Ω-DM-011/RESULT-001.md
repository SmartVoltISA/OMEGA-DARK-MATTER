# Ω-DM-011 — RESULT-001

Status: FAIL
Certification date: 2026-09-11
Protocol commit: d8d29f33e95031195350d2aabe47127520bbb575
Runner commit: 08ef2b7d3e9c72cf05c0a56538669f9c239d2f2e

## Primary result

40 independent connected weighted graphs were tested.

- log-correlation between inertial response m_eff and source strength q_eff: 0.7455297
- mean q_eff / m_eff: 0.0982349
- median q_eff / m_eff: 0.0994295
- coefficient of variation of q_eff / m_eff: 0.1450575

Preregistered H1 required log-correlation >= 0.95 AND CV <= 0.10.

Therefore H1 is NOT supported.

## Controls

Shuffled graph/probe pairing:

- log-correlation: 0.0713979
- control successfully destroys the primary correspondence.

Weight rescaling:

- W -> 0.5 W: median ratio changes by +63.72%; CV = 0.1184
- W -> 2.0 W: median ratio changes by -43.78%; CV = 0.1639

The apparent source/inertia ratio is therefore not invariant under simple relation-strength rescaling.

## Interpretation

This is a clean FAIL, not an inconclusive run. The numerical procedure and controls executed successfully.

The result says that, in this specified relational action construction, symmetric coupling and conservation structure do NOT by themselves force a universal source/inertia equivalence.

This is consistent with the lesson from Ω-DM-010: a source-like observable and an inertia-like observable do not automatically collapse onto one physical scalar merely because both originate from the same graph.

The weight-rescaling result is especially important. The ratio changes strongly when relation strength is multiplied by a constant, showing that the observed quantities retain construction-dependent scaling.

## What this does NOT show

This does not falsify gravity, dark matter, equivalence principle physics, or relational approaches in general. It only rejects the preregistered H1 for this concrete synthetic construction.

No inverse-square interaction was inserted. No claim about physical mass was tested.

## Next scientific step

Do not keep inventing graph statistics until one matches. The next useful test should introduce a genuine variational/conservation constraint in which the candidate source and inertial quantities arise as distinct Noether/response derivatives of the same action, with no direct identification between them. The key question is whether equivalence can then be derived rather than fitted.
