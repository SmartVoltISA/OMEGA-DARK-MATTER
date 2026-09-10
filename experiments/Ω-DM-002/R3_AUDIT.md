# Ω-DM-002 R3 — Local Audit

**Status:** AUDIT / PRE-EXECUTION

A local independent numerical check of the R3 equations was performed before treating the R3 protocol as executed.

## Finding

A straightforward joint ridge reconstruction improves held-out prediction relative to the zero-relation baseline, but the selected graph remains substantially denser than the hidden graph. With a representative run, active edges were ~72 versus 33 true edges. Therefore ridge regularization is not an adequate implementation of the preregistered minimum-structure criterion.

## Consequence

Do **not** mark R3 PASS. The implementation must use the specified L1/complexity-selection procedure rather than substitute ridge regression.

The current observation is retained as an engineering audit: predictive recovery can occur before sparse structural recovery, so prediction and topology recovery must remain separate gates.

## Next implementation

Implement non-negative L1 coordinate descent over the joint symmetric edge design, evaluate the complete preregistered λ grid using training-only BIC-like selection, freeze the selected graph, then evaluate untouched held-out data plus null and temporal-permutation controls.
