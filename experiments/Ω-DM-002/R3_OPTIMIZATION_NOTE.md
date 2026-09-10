# Ω-DM-002 R3 — Optimization Note

**Status:** ENGINEERING / NOT SCIENTIFIC RESULT
**Date:** 2026-09-11

## Purpose

The preregistered R3 executor is mathematically aligned with the protocol, but its reference implementation stores the full design matrix and repeatedly scans every row during coordinate descent. This makes the stdlib-only execution unnecessarily expensive.

## Required optimization

A future optimized executor may replace repeated row scans with sufficient statistics:

- `G = XᵀX`
- `b = Xᵀy`
- `yTy = yᵀy`

For the same fixed design, the coordinate-descent update can then use

`rho_j = b_j - Σ_{k≠j} G_jk w_k`

and

`w_j = max(0, (rho_j - λ) / G_jj)`.

RSS can be recovered as

`RSS = yTy - 2 wᵀb + wᵀG w`.

The optimization must preserve the objective, non-negativity constraint, lambda grid, training-only BIC-like selection, and frozen test evaluation exactly. It must not silently change scaling or introduce standardization.

## Certification rule

The optimized implementation must be treated as a new executable implementation and checked against the reference implementation on a small deterministic fixture before being used for the official R3 run.

No numerical R3 conclusion is promoted by this note.

`CODE OPTIMIZED ≠ EXECUTED ≠ VALIDATED`
