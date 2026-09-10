# Ω-DM-002 — Exploratory R2 Result

**Status:** EXECUTED LOCALLY / EXPLORATORY
**Date:** 2026-09-11
**Purpose:** test whether joint estimation of the relation matrix removes the false-edge explosion seen in the first estimator.

## Change from R1

R1 estimated every edge independently. That produced 222 candidate edges for 33 true edges and degraded held-out prediction.

R2 instead estimates all unordered edges jointly as one non-negative sparse regression problem. The candidate relation matrix is symmetric and frozen before test scoring.

The local numerical exploration used the same synthetic generator and train/test split family as Ω-DM-002, with a joint positive L1 regression implementation for the computational check.

## Main run

Configuration:

- seed: `20260911`
- nodes: `24`
- training trajectories: `40`
- test trajectories: `20`
- trajectory length: `80`
- coupling `K = 0.05`
- damping `gamma = 0.02`
- noise sigma `0.005`
- hidden true edges: `33`
- exploratory regularization: `alpha = 100`

Observed:

- recovered edges (>0): `38`
- true positives: `22`
- precision: `57.9%`
- recall: `66.7%`
- baseline one-step RMSE: `32.2281`
- reconstructed one-step RMSE: `18.2286`
- 10-step rollout RMSE: `64.4956` vs baseline `220.3233`

Thus joint estimation removes the catastrophic predictive failure of R1 and produces a substantial held-out predictive improvement.

## Controls

Twenty W=0 null runs produced zero recovered edges under the exploratory regularization and therefore zero apparent improvement.

Twenty temporal-permutation controls (node labels independently permuted within each training time slice) also produced zero recovered edges under the same setting.

These controls are supportive but do not by themselves establish a physical effect.

## Sensitivity observation

Increasing regularization reduced the number of inferred edges. At `alpha=100`, the main run gave 38 edges. Thresholding the same fitted coefficients more aggressively could increase precision, but such post-hoc threshold selection is **not** counted as confirmatory evidence.

## Decision

**Exploratory R2: PROMISING / NOT YET CONFIRMATORY.**

The failure mode identified in R1 is substantially reduced when relations are estimated jointly. The reconstruction problem remains non-identifiable enough that topology recovery is incomplete.

## Required next gate

Create a preregistered R3 in which model complexity is selected using training-only validation, with the final sparsity/regularization rule frozen before held-out evaluation. Add explicit topology metrics, coefficient error, stability across independent trajectories, and an independent implementation/scoring check.

## Interpretation boundary

This result concerns only reconstruction of hidden relations in a synthetic dynamical system whose relation law is explicitly supplied. It is not evidence for dark matter, gravity, or a physical relational substrate.
