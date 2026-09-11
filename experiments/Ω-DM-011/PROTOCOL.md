# Ω-DM-011 — Conservation/action test of source–inertia equivalence

Status: PREREGISTERED
Date: 2026-09-11

## Question

Can a common mass-like scalar emerge from a relational action and conservation law when source strength and inertial response are measured by different observables?

## Motivation

Ω-DM-010 failed because two independently constructed graph observables produced an almost perfectly inverse source/inertia relation. Ω-DM-011 therefore removes the arbitrary graph-statistic definitions and asks a sharper question: does a symmetric relational action plus conservation itself force source strength and inertial response to track one another?

## Model

For each random connected weighted graph, W is symmetric, W_ij >= 0, with zero diagonal.

Node coordinates x_i and velocities v_i are used only to measure response. The relational kinetic metric is

M = I + alpha * D

where D is the diagonal weighted degree matrix and alpha is fixed at 1.0.

The pair potential is

V = 0.5 * sum_ij W_ij * (x_i - x_j)^2

and therefore the pair force is symmetric and internal. No inverse-square term and no physical mass law are inserted.

The corresponding free kinetic momentum is p = M v.

## Independently measured observables

1. Inertial response m_eff:
   Apply a uniform velocity increment delta_v to a localized two-node probe cluster while all other nodes remain fixed. Measure the resulting cluster momentum increment. Define m_eff = delta_p / delta_v.

2. Source strength q_eff:
   Use the same graph as a scalar source network. Apply a unit localized source on the probe cluster and solve
   (L + eps*I) phi = s
   with eps=1e-3. Measure outward flux through a one-edge-thick graph cut surrounding the probe. q_eff is the absolute net cut flux.

The two measurements use different response channels: kinetic momentum versus field flux.

## Primary hypothesis

H1: conservation/action structure alone produces a stable proportionality q_eff = C * m_eff across independently generated graphs, with normalized scatter CV(q_eff/m_eff) <= 0.10 and log-correlation >= 0.95.

H0: the proportionality is not stable: either CV > 0.10 or log-correlation < 0.95.

No fitted transformation other than one global proportionality constant C is allowed for the primary test.

## Controls

A shuffled graph/probe pairing control is required. It should destroy any graph-local source/inertia correspondence while preserving marginal distributions.

A weight-rescaling control is required: W -> cW for c in {0.5, 2.0}. Because M depends on D and the field equation depends on L, this tests whether the apparent proportionality is merely a shared scaling artifact.

## Dataset

40 independent random connected weighted graphs.
N=20 nodes.
Edge probability p=0.15, resampled until connected.
Edge weights uniform on [0.2, 1.0].
Probe cluster: the two nodes with largest weighted degree, fixed by deterministic rule.
Seeds: 20260911 through 20260950.

## Acceptance criteria

PASS only if H1 passes on the 40-graph primary set AND the shuffled control fails AND the weight-rescaling control preserves proportionality within 10% relative change in the median ratio.

FAIL if the primary H1 criterion fails while the controls execute successfully.

INCONCLUSIVE if numerical stability, graph connectivity, or control execution fails.

## Reproducibility

Python standard library + NumPy only. Fixed seeds. All raw per-graph measurements and aggregate statistics must be saved.

## Scientific scope

A PASS would show only that this specified relational action construction generates a robust source/inertia correspondence. It would not establish physical gravity, dark matter, or a physical mass law.
A FAIL would be evidence that conservation and symmetric relational coupling alone do not force source–inertia equivalence in this construction.
