# Ω-DM-023 — RESULT-001

**Status: HOLD — runner/protocol saved, numerical certification pending**

## Purpose
Test whether the conservation→geometry mechanism survives directed/nonreciprocal local relations, and determine whether generalized balance rather than reciprocity is the relevant condition.

## What is established
The protocol and deterministic runner are now committed. The experiment compares a positive local directed medium with a deliberately unbalanced directed control. It measures shell flux directly from directed edge currents, radial response scaling, and source-amplitude scaling.

## Important methodological note
The first implementation is retained as a reproducible runner but has not been accepted as a scientific result yet. The proposed global balancing procedure is only an approximation to exact node-wise flow balance, and therefore a PASS based on it would be premature. Certification requires running the saved script and checking the actual balance residuals before interpreting p≈2.

## Decision
No H1/H0 conclusion is issued in this result file until the numerical run is independently inspected. This preserves the Ω research rule:

UNKNOWN != TRUE
HYPOTHESIS != EXPERIMENT
PROPOSED != EXECUTED
RESULT != CONCLUSION
CONCLUSION != PROOF

## Reproducibility
Protocol commit: `8160f1bae06f46f2147738990f5c9aee5b3b999b`
Runner commit: `adfe604c231815bbc90aade13d2b51345cb1edac`
