# Ω-DM-013 — Emergent inertia from internal relational dynamics

Status: PREREGISTERED
Date: 2026-09-11

## Question

Can a nonzero effective inertia for collective translation arise from internal relational degrees of freedom, without adding an absolute kinetic term or inserting mass by definition?

## Motivation

Ω-DM-012 showed a strict null mode for a purely difference-based kinetic action. The present test asks whether that null can be lifted by giving the relations their own internal dynamical state, while keeping the theory relational and avoiding an explicit absolute mass term.

## Model

Each node has position x_i and velocity v_i. Each edge e=(i,j) carries an internal scalar y_ij.

Use the relational Lagrangian

L = T_rel + T_edge - V_rel

with

T_rel = 0.5 * sum_(i,j) W_ij * (v_i - v_j)^2
T_edge = 0.5 * sum_(i,j) W_ij * (dy_ij/dt)^2
V_rel = 0.5 * k * sum_(i,j) W_ij * (x_i - x_j - y_ij)^2

where k=1 and W is symmetric, nonnegative, connected, and has zero diagonal.

There is NO term proportional to sum_i v_i^2 and NO parameter named mass.

The edge variable y_ij is an internal relational degree of freedom. Under a uniform translation x_i -> x_i + a, the differences x_i-x_j remain unchanged, so any collective inertia must arise only through dynamical response of the internal sector to the imposed translation protocol.

## Operational experiment

For each graph, prepare the internal variables in their ground state for the initial configuration. Impose a finite-duration collective translation of all node coordinates with prescribed velocity U, then release the external drive and measure the conserved total canonical momentum and total kinetic-plus-potential energy.

Define the effective collective inertial coefficient by

m_eff = P_collective / U

where P_collective is the conserved momentum associated with the collective translation after the drive is removed.

This is an operational response coefficient, not an assumed mass.

## Primary hypothesis

H1: internal relational dynamics generate a stable nonzero collective inertial coefficient that is proportional to the total relational coupling scale across graphs, while remaining absent in the static/no-dynamics control.

Primary acceptance:

1. m_eff > 1e-8 on at least 95% of 60 graphs;
2. coefficient of variation of m_eff / S_W <= 0.15, where S_W = sum_{i<j} W_ij;
3. the same coefficient is reproduced when U is changed between 0.5 and 2.0, within 5% relative error;
4. no explicit absolute kinetic term is present.

H0: collective inertia remains zero or is not a stable emergent response.

## Controls

1. Ω-DM-012-style static relational control: remove edge dynamics and verify the collective coefficient returns to numerical zero.
2. Weight-shuffle control: preserve the weight distribution but randomly reassign edge weights; this tests whether the effect depends on topology rather than only total weight.
3. Velocity-scale control: U in {0.5, 1.0, 2.0}; the inferred m_eff must remain invariant.
4. Energy conservation check after release.

## Dataset

60 independently generated connected weighted graphs.
N=12, 20, 32 nodes, 20 graphs per size.
Edge probability p=0.20.
Weights uniform on [0.2, 1.0].
Fixed seeds 20261301 through 20261360.

## Numerical method

Use deterministic symplectic integration with fixed timestep dt=0.002 for 5000 steps after release. Repeat with dt/2 as a numerical stability check on a fixed subset of 12 graphs.

## Falsification / interpretation

A PASS would show only that this concrete internal-relational model possesses an emergent collective response coefficient. It would NOT establish physical mass, gravity, or dark matter.

A FAIL would strengthen the Ω-DM-012 no-go result for this class of internal edge dynamics.

If the primary result is positive, the next test must determine whether the same coefficient can independently control source response, without identifying source and inertia by definition.

All equations are written in plain text to keep the protocol reproducible and display-safe.