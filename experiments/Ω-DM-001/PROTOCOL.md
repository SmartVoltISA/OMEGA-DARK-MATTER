# Ω-DM-001 — Synthetic Relational Contribution Recovery

**Status:** EXECUTED / CONTROL AUDIT COMPLETE
**Purpose:** test whether a deliberately hidden relational contribution can be recovered from synthetic observables under preregistered controls.

## Scope

This is a **synthetic identifiability test**, not a physical gravity derivation and not evidence for dark matter being relational.

The experiment asks a narrower question:

> If a known relational state contributes to an observable through an explicit model law, can the contribution be detected and recovered, while matched null and topology-destroyed controls reject false positives?

## Hypotheses

**H1:** Under the generating model, a hidden relational contribution produces a measurable improvement over the visible-only baseline on held-out synthetic data, with controlled complexity.

**H0:** The visible-only baseline is sufficient; apparent improvement from the relational term is attributable to noise, overfitting, or arbitrary topology.

## Generative model

Use a one-dimensional radial synthetic system with fixed sample radii `r_i`.

Visible baseline acceleration:

`a_B(r) = A / (r + eps)^2`

A hidden relation graph defines a relational density:

`rho_R(r_i) = sum_j W_ij K(r_i-r_j)`

where `W_ij` is the hidden relation state and `K` is a fixed normalized kernel.

The synthetic relational contribution is defined explicitly as:

`a_R(r_i) = lambda * rho_R(r_i) / (r_i + eps)^2`

and the generated observable is:

`v_i^2 = r_i * (a_B(r_i) + a_R(r_i)) + noise_i`

This inverse-square form is **part of the toy generator only**. It must not be presented as a derivation of gravity.

## Controls

1. **M0 visible-only:** fit only `A`.
2. **M1 relation-aware:** fit `A` and `lambda` with the generating relation basis fixed before fitting.
3. **Permutation control:** preserve the relation-weight distribution but randomly permute relation endpoints, destroying the original topology.
4. **Null injection:** set `lambda = 0` and repeat the full fitting pipeline.
5. **Held-out data:** generate train/test samples from the same preregistered generator but independent noise.

## Metrics

Primary:
- held-out RMSE;
- held-out log-likelihood under the fixed Gaussian noise model;
- improvement `Delta = score(M0) - score(M1)`.

Secondary:
- recovered `lambda` bias;
- recovery interval/uncertainty;
- permutation-control false-positive rate;
- null-control false-positive rate.

Complexity must be penalized; an extra parameter is not free evidence.

## Fixed parameters

The executable must record:
- random seed;
- number of radial samples;
- train/test split;
- `A_true`, `lambda_true`, `eps`;
- kernel width and normalization;
- graph topology and weight-generation rule;
- noise standard deviation;
- optimizer/search grid;
- software commit identifier.

No parameter may be changed after observing test performance without creating a new experiment version.

## Falsification logic

H1 is **not** supported if the relation-aware improvement disappears on held-out data, fails to recover injected `lambda`, or is reproduced by the topology-permutation/null controls at a comparable rate.

A successful synthetic recovery only establishes that the chosen hidden variable is identifiable under the chosen generator. It does **not** establish a physical relational origin of gravity.

## Required output

`RESULT-001.md` must contain the exact seed, generator parameters, model scores, recovery statistics, control results, code commit, and an explicit PASS/FAIL/INVALID classification.

Until the executable is actually run, no numerical result is claimed.

---

## Execution record — appended 2026-09-11

**Status:** EXECUTED LOCALLY / CONTROL AUDIT COMPLETE

The executable was run after a control flaw was identified in the first permutation implementation. The first implementation shuffled relation weights on the same edge-pair set and generated observations from the shuffled graph; this was rejected as an invalid control. A corrected permutation control generates observations from the original graph and uses an independently randomized topology preserving edge count and weight multiset only as the fitted relation basis.

Corrected executable commit: `64e062b701676cb38285b4fcc85e6c1f4768c6dd`.

Fixed execution parameters: seed `20260911`; `N=80`; train/test `56/24`; `A_true=2.0`; `lambda_true=0.65`; `eps=0.20`; kernel width `0.45`; noise sigma `0.015`; 20 null repetitions; 20 permutation repetitions.

Main fit:
- M0 `A=2.4783989771`
- M1 `A=2.0005088559`
- recovered `lambda=0.6536026375`
- held-out RMSE M0 `0.0183405481`
- held-out RMSE M1 `0.0167181599`
- improvement `0.0016223882`

Controls:
- 20 null seeds: mean held-out RMSE improvement approximately `-0.00004797`.
- 20 corrected topology-permutation seeds: mean held-out RMSE improvement approximately `-0.00050946`, population SD approximately `0.00106496`.

**Decision:** PASS — synthetic identifiability gate.

**Boundary:** this result demonstrates recovery under the explicitly chosen synthetic generator only. The inverse-square relational contribution is supplied by the generator; it is not derived by the experiment. No claim about physical dark matter or gravity follows.
