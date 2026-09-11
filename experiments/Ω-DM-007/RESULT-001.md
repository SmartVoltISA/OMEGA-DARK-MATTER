# Ω-DM-007 — Mass and Attraction Identifiability Result

Date: 2026-09-11
Status: PASS — identifiability structure confirmed

## Certification

Protocol `PROTOCOL.md` was committed before the certification run. The generator contains no inverse-square term and no gravitational constant.

## A. Attraction sign

The relational force was defined as:

F_12 = w * tanh(k*(x_2-x_1)), F_21 = -F_12.

Across the trajectory, the measured accelerations pointed toward the other body in 99.9% of sampled steps. The small remainder is a numerical differentiation boundary effect.

Result: PASS.

## B. Mass ratio

The hidden masses were:

m_1 = 2.0
m_2 = 3.5

The acceleration-ratio estimator gave:

median(-a_1/a_2) = 1.75

True ratio:

m_2/m_1 = 3.5/2.0 = 1.75

Numerical deviation was below floating-point resolution in the interior samples.

Result: PASS.

## C. Absolute mass versus interaction strength

Three parameter triples were tested:

(2.0, 3.5, 1.7)
(4.0, 7.0, 3.4)
(20.0, 35.0, 17.0)

All are related by a common scale factor. Their simulated trajectories were identical to numerical precision.

Maximum trajectory difference:

- scale 2: 0.0
- scale 10: approximately 5.33e-15

Therefore closed two-body motion alone cannot distinguish the absolute mass scale from the absolute interaction-strength scale in this model.

Result: PASS.

## D. Force-law recovery after inertial calibration

With the true inertial mass used only as an external calibration, the recovered force was:

F_est = m_1 * a_1.

It matched the injected bounded relation law:

F = 1.7 * tanh(x_2-x_1)

with RMSE approximately 0.00762 over the numerical trajectory. The residual is consistent with finite-difference acceleration estimation and integration discretization.

Result: PASS.

## Main scientific result

The experiment separates three concepts that must not be conflated:

1. direction of attraction;
2. relative inertial response (mass ratio);
3. absolute force/mass scale.

The first two are identifiable in this controlled model. The third is not identifiable from closed two-body motion alone because of the exact scale symmetry:

(m_1,m_2,w) -> (c*m_1,c*m_2,c*w).

## Interpretation for Ω

This is a mathematical identifiability result, not a discovery of physical mass or gravity.

It gives Ω a useful rule:

RELATIONAL DYNAMICS CAN REVEAL RELATIVE INERTIA AND ATTRACTION, BUT AN ABSOLUTE MASS SCALE REQUIRES AN EXTERNAL CALIBRATION OR AN ADDITIONAL LAW.

The next physical bridge should therefore not assume mass as an unexplained parameter. It should ask whether a relational invariant can supply the missing scale and whether the resulting force law approaches an observed gravitational law without inserting inverse-square behaviour by hand.

`IDENTIFIABILITY ≠ PHYSICAL GRAVITY`
