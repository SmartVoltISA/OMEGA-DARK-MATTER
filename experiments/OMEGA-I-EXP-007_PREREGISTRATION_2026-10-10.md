# Ω-I-EXP-007 — Factorial interventions on identity proxies
Date: 2026-10-10
Status: preregistered before execution.

## Question
Can models distinguish simulated lineage continuity when element identity, organization, function, and causal ancestry are independently manipulated, without directly leaking the label into features?

## Critical scope
"Same lineage" is an operational simulator label defined by parent pointers. It is not a universal definition of identity. This experiment tests recoverability of lineage from observed signals, not metaphysical identity.

## Design
- 4 dynamics: AR(1), IID, damped oscillator, and regime-switch.
- 4 interventions on a system trajectory: (A) uninterrupted continuation; (B) snapshot clone with new parent pointer but identical state at branch time; (C) element relabel/replacement while preserving the numeric state transition; (D) organization/function perturbation with matched initial state.
- 250 independent base trajectories per dynamic, each length 240.
- Split by base trajectory: 175 train, 75 test.
- Label is generated only from simulator's explicit parent-pointer ledger; it is never used to generate observations or features.
- Features: (1) current state distance, (2) trajectory-history distance, (3) transition residual distance, (4) structure/function distance where defined. Each is computed from observed values only.
- Models: present-only, present+history, present+history+transition. Logistic regression, fixed C=1, standardization fit only on training data.
- Metrics: held-out ROC-AUC, balanced accuracy, 95% bootstrap CI over base families (2,000 resamples).
- Negative controls: permuted labels, shuffled history, IID dynamics.
- Primary comparison: incremental ROC-AUC from adding history to present-only.

## Decision rules
History is incrementally useful only if test-set AUC improves and family-bootstrap 95% CI for paired AUC difference excludes zero. Label permutation must return AUC near 0.5. Any condition where the label is structurally unidentifiable from observed features should remain near chance.

## Limitation
Even a successful result only shows recoverability of the simulator's parent-pointer label under these intervention rules. It cannot establish a general theory of identity, consciousness, or physics.
