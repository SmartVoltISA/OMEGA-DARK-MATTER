# Ω-DM-016 — RESULT-001

Status: INCONCLUSIVE / DYNAMICAL-RESPONSE MISMATCH
Date: 2026-09-11

## Execution

The Ω-DM-016 runner was executed locally, outside GitHub Actions.

The test applies a uniform weak bias to a relaxed kink and infers a dynamical mass from measured center acceleration. Both bias signs were tested, with two amplitudes and two box sizes.

## Primary observation

The acceleration response is reproducible between N=201 and N=401, and reverses sign when the external bias sign is reversed.

For k=1.0:

- h=2e-4: |a| approximately 1.92166e-3, giving M_D approximately 0.20815 under the preregistered force calibration.
- h=4e-4: |a| approximately 3.25832e-3, giving M_D approximately 0.24553.

The corresponding values are essentially identical for N=201 and N=401.

For k=2.0 the inferred M_D is approximately 0.6263 and 0.6609 for the two biases.

For k=0.5 the response is not sufficiently clean for certification; the inferred values are strongly dependent on the bias amplitude.

## Comparison with Ω-DM-014

The independently measured energy metric from the corrected Ω-DM-014 runner is approximately:

- k=0.5: M_E about 1.2753 in the central translation window;
- k=1.0: M_E about 0.9467;
- k=2.0: M_E about 0.6698.

The dynamical-response estimate does not agree with M_E for k=1.0, and k=0.5 is particularly unstable.

Therefore Ω-DM-016 does NOT certify physical/dynamical inertia.

## Important methodological finding

The discrepancy is itself reproducible and points to a flaw in the current dynamical protocol: the uniform bias does not produce a sufficiently rigid collective translation of the finite kink. Internal deformation and the way the center coordinate is extracted contaminate the acceleration measurement.

This means the current M_D calculation cannot be used as an independent confirmation of M_E.

## Decision

H1 for independent dynamical inertia: NOT SUPPORTED by this run.

Status: INCONCLUSIVE rather than FAIL because the localized defect remains dynamically responsive and the response has the correct sign symmetry, but the collective-coordinate acceleration is not demonstrably the acceleration of a rigid translated defect.

## Next correction

The next protocol must use a translation-neutral perturbation with an independently measured generalized force and a projection onto the translational tangent mode, while separately monitoring deformation/radiation. The force-to-acceleration ratio must converge as h -> 0 and remain stable under N refinement.

No gravitational force law, inverse-square term, Newton constant, or fitted exponent was introduced.
