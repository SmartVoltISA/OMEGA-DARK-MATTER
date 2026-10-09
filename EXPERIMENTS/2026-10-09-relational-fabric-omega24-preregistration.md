# Ω-24 — Activity-matched continuous relational alignment

**Status:** preregistered before execution.

## Question
Does learned edge-magnitude placement improve signed relational alignment when post-evolution state amplitude is matched across conditions?

## Motivation
Ω-23 showed a larger raw continuous margin M for frozen learned magnitudes, but activity A also increased and normalized alignment Q decreased. This follow-up fixes the amplitude confound in the evaluation rather than treating raw margin as sufficient.

## Primary metric
For each post-perturbation state x, calculate its RMS r = sqrt(mean(x_i^2)). Rescale only for evaluation, by the positive factor c = r_target/r, where r_target is the RMS of that seed's shared pre-perturbation trained state. Compute the activity-matched margin:
M_matched = mean_e(s_e (c x_i)(c x_j))
over all graph edges. All edge signs s_e are fixed to the original edge-sign labels. Positive scaling leaves each state's sign pattern unchanged, while placing all branches at the same RMS target per seed. Report the unscaled M, A, Q, RMS, and state recovery as secondary diagnostics. If a branch RMS is below 1e-12, mark its matched score undefined rather than amplifying numerical zero.

## Protocol
- 40 paired seeds: 20262400–20262439; N=160; ring-derived graph k=4, rewiring probability 0.03.
- Initial state N(0, 0.15), edge magnitudes Uniform(0.7, 1.3), edge signs independently ±1.
- Train one common network for 100 steps. All conditions branch from the same trained state and receive the same sign-flip perturbation to the first 10% of nodes.
- Conditions: adaptive-live learned magnitudes; frozen learned magnitudes; learned magnitudes permuted across edges; original fixed magnitudes; no coupling.
- Edge signs remain fixed in every mode; adaptation changes magnitudes only. Train 100 steps; evaluate 100 post-perturbation steps.
- Primary: M_matched after rescaling every branch to the common pre-perturbation RMS for that seed. The rescaling is for scoring only and does not feed back into dynamics.
- Paired comparisons: frozen learned minus permuted learned and frozen learned minus fixed original. Use 10,000 paired bootstrap resamples, seed 20262499, 95% percentile CIs.
- The no-coupling mode is expected to decay near zero; if its RMS is below 1e-12, its matched score is undefined and is not evidence for or against organization.

## Decision rule
A learned-magnitude advantage is supported only if the 95% paired bootstrap CIs for M_matched are strictly above zero versus both controls. Otherwise report no demonstrated advantage. Also report adaptive-live comparisons; do not overinterpret secondary metrics. This is a toy-network test, not a physical test of dark matter or superluminal propagation.

## Integrity
This protocol must be committed before executing Ω-24. Retain all per-seed records and state clearly which environment actually ran the numerical computation.
