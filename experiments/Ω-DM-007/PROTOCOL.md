# Ω-DM-007 — Mass and Attraction Identifiability

Date: 2026-09-11
Status: PREREGISTERED BEFORE CERTIFICATION RUN

## Question

Can the relation language distinguish and quantify two different quantities that are often conflated:

1. attractive interaction strength (force law);
2. inertial response (effective mass).

The primary goal is to identify what is observable from relational dynamics alone and what requires an external calibration.

## Generator

Use a two-body one-dimensional controlled relation model. No inverse-square law is used.

F_12 = w * tanh(k * (x_2 - x_1))
F_21 = -F_12

a_1 = F_12 / m_1
a_2 = F_21 / m_2

Fixed generator parameters:

m_1 = 2.0
m_2 = 3.5
w = 1.7
k = 1.0
dt = 0.01

Initial state:

x_1 = -2.0
x_2 = 2.0
v_1 = 0.6
v_2 = -0.2

The force is attractive because its sign is toward the other body.

## Observables

The primary observation is x_i(t) and v_i(t). The hidden quantities are m_1, m_2 and w.

## Primary tests

### A. Attraction sign

Determine whether acceleration points toward the other body over the tested trajectory.

### B. Mass ratio

Estimate:

m_2 / m_1 = -a_1 / a_2

when both accelerations are non-zero.

### C. Absolute mass identifiability

Test whether x(t) alone can uniquely determine m_i and w.

Expected symmetry:

(m_1, m_2, w) -> (c*m_1, c*m_2, c*w)

leaves acceleration unchanged for any c > 0.

Therefore absolute mass scale and absolute interaction strength are expected to be non-identifiable from closed two-body motion alone.

### D. Force-law shape

After an independent inertial calibration, reconstruct F(x_2-x_1) and compare the observed shape with candidate laws without assuming inverse-square behaviour.

## Falsification

The expected mass-ratio identity is falsified if the recovered acceleration ratio is systematically inconsistent with m_2/m_1.

The scale-degeneracy claim is falsified if two parameter triples related by the transformation above produce distinguishable trajectories under the same initial conditions and numerical precision.

## Important distinction

This experiment does NOT discover physical mass or gravity. It tests the identifiability structure of a relational dynamical language.

A positive result means:

- attraction can be operationally identified from directed response;
- mass ratios can be recovered from relative inertial response;
- absolute mass requires a calibration or additional physical law;
- the interaction law is a separate object from mass.

## Certification rule

No inverse-square term, gravitational constant, or physical units may be introduced into the generator after protocol registration.
