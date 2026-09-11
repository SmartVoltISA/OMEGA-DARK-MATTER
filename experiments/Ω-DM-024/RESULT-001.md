# Ω-DM-024 — RESULT-001

**Status: PASS-H1 (structural mathematical mechanism)**

## Execution
Deterministic local Python execution over dimensions d=1,2,3, six independent perturbations per dimension. The conserved case uses shell flux Q(r) divided by shell measure S_d(r), with no inverse-power response law inserted.

## Conserved case
Measured mean exponents:

- d=1: p = -0.001105, target d-1 = 0
- d=2: p = 0.998895, target d-1 = 1
- d=3: p = 1.998895, target d-1 = 2

Sample standard deviation in each dimension: 0.003505.

The deviations from d-1 are below 0.0012 in absolute mean value.

## Leakage control
A radius-dependent flux loss Q(r) was introduced. The response then contains an additional exponential factor, so the pure d-1 power law is no longer recovered. This confirms that the geometric exponent depends on conservation of flux rather than geometry alone.

## Interpretation
H1 supported. For the tested structural construction, conservation plus shell geometry is sufficient to produce the exponent p=d-1. In 3D this gives p=2, i.e. an inverse-square environmental gradient.

This result is deliberately narrower than a physical derivation: the experiment does not derive conservation from a deeper relational law, nor does it establish physical gravity or dark matter. It isolates the mathematical step responsible for the exponent once a conserved relational flux exists.

## Chain now supported by Ω-DM-021..024
local relations → conserved relational flux → shell geometry → p=d-1 → p=2 in 3D.

The decisive remaining problem is therefore upstream: determine whether conservation itself can emerge from a more primitive relation-first dynamics without being imposed as a Laplacian/balance axiom.

## Reproducibility
Protocol commit: `5cbce1c56552edecbea748607cea2fc45812097d`
Runner commit: `79689b1a55a4ff14414580eed0092b3a1cc21731`
