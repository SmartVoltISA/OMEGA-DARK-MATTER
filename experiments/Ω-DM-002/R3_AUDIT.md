# Ω-DM-002 R3 — Local Audit

**Status:** EXECUTION AUDIT / NOT CERTIFIED

A local independent numerical check was performed before promoting the R3 implementation to an official scientific result.

## Earlier finding

A straightforward joint ridge reconstruction improved held-out prediction relative to the zero-relation baseline, but the selected graph was substantially denser than the hidden graph. Ridge is therefore not an adequate substitute for the preregistered minimum-structure procedure.

## Optimized execution audit — 2026-09-11

An algebraically equivalent NumPy implementation was built locally using sufficient statistics `G = XᵀX`, `b = Xᵀy`, and `yᵀy` to remove repeated full-matrix scans. The purpose was execution diagnostics, not protocol replacement.

Main deterministic configuration was kept identical to R3: seed `20260911`, `N=24`, 40 training trajectories, 20 test trajectories, length 80, `K=.05`, `gamma=.02`, `sigma=.005`, `edge_p=.12`, and lambda grid `{0.1, 0.3, 1, 3, 10, 30, 100}`.

### Main diagnostic run

The coordinate-descent solver reached its iteration cap rather than the requested tolerance, so this run is **not certified as converged**.

At 5000 iterations:

- selected λ = `100`
- active edges = `103`
- hidden true edges = `33`
- baseline h1 RMSE = `32.2280692194`
- selected h1 RMSE = `18.2845877859`
- selected h2 RMSE = `46.7038223718`
- selected h5 RMSE = `94.7946326634`
- selected h10 RMSE = `142.3212770489`

The one-step prediction improves, but multi-step rollout degrades strongly and the optimizer has not converged. This is a strong diagnostic warning, not an R3 PASS/FAIL classification.

### Control diagnostic

Two null seeds and two temporal-permutation seeds were also executed with the optimized diagnostic implementation. The null cases selected zero edges at λ=`0.3` and showed no predictive improvement. Temporal-permutation cases also selected zero edges and showed no predictive improvement. These are only preliminary control samples, not the full preregistered control set.

## Certification boundary

The official R3 result remains **NOT CERTIFIED**. Before certification:

1. implement a demonstrably convergent solver or otherwise certify convergence of the exact preregistered objective;
2. cross-check the optimized solver against the reference implementation on a small deterministic fixture;
3. run the complete control set and archive exact output, runtime, code identity and final decision.

Do not promote the diagnostic numbers to a scientific R3 result.

`CODE READY ≠ EXECUTED ≠ CONVERGED ≠ VALIDATED`

## Next implementation

Build the convergent optimized solver while preserving the exact R3 objective and lambda grid. Only after fixture agreement should the full R3 certification run be attempted.
