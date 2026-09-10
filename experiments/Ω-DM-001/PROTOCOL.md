# Ω-DM-001 — Synthetic Relational Contribution Recovery

**Status:** PROTOCOL / NOT YET EXECUTED
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
