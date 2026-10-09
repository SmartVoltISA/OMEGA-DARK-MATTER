# Ω-DM / Ω — Relational Fabric: Experiment Log
Date: 2026-10-09
Status: exploratory; hypothesis not established physics

## Purpose
Preserve the discussion and toy-model checks concerning the hypothesis that matter may be modeled as a continuous relational fabric, with stable localized configurations appearing as derived structures. The idea that the underlying fabric can have dynamics faster than the speed at which causal information propagates is an open conjecture.

This record separates conceptual assumptions, illustrative calculations, and validated evidence. It does not claim to establish a physical theory.

## Hypothesis under investigation
**H-relational-fabric (provisional):** The primary object in the model is a dynamic relational fabric, not a set of pre-existing particles connected by separate edges. What are later described as nodes, boundaries, or objects may correspond to stable local configurations of the fabric.

**Additional conjecture:** The fabric's internal dynamics might differ from the maximum speed of causal information propagation (the vacuum speed of light, c).

This conjecture is not established. If the fabric can transmit a controllable signal faster than c, the model must confront causality and existing experimental constraints. Merely naming an internal process “not information” is insufficient; the distinction must be operationally defined.

## Conceptual distinctions
- Fabric: the complete relational structure, not a separate carrier plus separate threads.
- State: a mathematical description of the fabric at a given place/time or in a more general state space.
- Localized configuration: a candidate stable pattern; not assumed to be a particle until defined operationally.
- Disturbance propagation: movement of a detectable change through the model.
- Information transmission: a controllable change capable of influencing a receiver.
- c: the vacuum speed of light and the limiting speed for causal information in standard relativistic physics.

## Experiment log

### EXP-01 — Continuous-field toy model
**Model:** one-dimensional wave equation
\[
\partial_t^2 u = v^2\partial_x^2u
\]
**Question:** Can a continuous state propagate disturbances without predefining particles?
**Outcome:** The equation supports wave propagation at model speed v. This is a standard illustrative model, not a derivation of matter from relations.
**Limitations:** The field and its dynamics are prescribed in advance. No emergent matter or physical value of c is derived.
**Status:** Demonstration only; not a physical test of the hypothesis.

### EXP-02 — Two assigned propagation speeds
**Setup reported in discussion:** compare toy cases with v=1 and v=2 in arbitrary units.
**Outcome reported:** the faster case's disturbance reaches farther over the same interval.
**Interpretation:** expected from the chosen model parameters.
**Limitations:** The numerical values are arbitrary, and the front estimate depends on the threshold used. This does not demonstrate superluminal physical propagation.
**Reproducibility:** Original executable source, parameters, and raw arrays were not preserved with this entry. Treat the reported table as an illustrative result, not independently reproducible evidence.

### EXP-03 — Separating internal dynamics from information propagation
**Question:** Can a model have faster internal dynamics while retaining a slower causal information channel?
**Control logic:** compare (A) one dynamics with one propagation speed; (B) internal dynamics plus a separately defined observable channel; (C) a relational structure with causal propagation emerging from its rules.
**Outcome:** No validated model has yet established the separation. A simple direct local coupling can allow the faster dynamics to influence the observable channel.
**Conclusion:** A mathematical mechanism is needed that prevents faster internal processes from carrying controllable information faster than c, if that is the intended claim.
**Status:** Open design problem; no physical confirmation.

### EXP-04 — Discrete-chain coupling illustration
**Setup reported in discussion:** a fast chain advances two arbitrary cells per tick; a slower channel advances one cell per tick; a locally coupled channel follows the fast influence.
**Reported table:** at 5, 10, 20, 30, and 60 ticks, distances were respectively 10, 20, 40, 60, 120 for the fast chain; 5, 10, 20, 30, 60 for the slow channel; and 10, 20, 40, 60, 120 for the directly coupled channel.
**Interpretation:** these values follow the stipulated update rules; direct coupling transmits the fast influence.
**Limitations:** This is a constructed toy model with assigned speeds, not a measured physical phenomenon. The original source code and raw outputs were not preserved here.
**Status:** Illustrative control only; must be rerun from saved code before being treated as a reproducible experiment.

### EXP-05 — Speed from coupling parameters
**Candidate relation:** \(v_{model}=a\sqrt{K/M}\), for a conventional linear chain with spacing a, coupling coefficient K, and mass M.
**Outcome reported in discussion:** increasing K by a factor of four approximately doubles the model propagation speed.
**Interpretation:** expected for that standard chain model.
**Limitations:** The model explicitly contains discrete elements and parameters. It does not derive nodes, matter, or c from a node-free relational fabric.
**Status:** Analytic/illustrative baseline, not evidence for Ω's ontology.

### EXP-06 — Grid-resolution check
**Reported measured front speeds:** grid steps 1.00 → 1.133; 0.50 → 1.117; 0.25 → 1.121.
**Interpretation:** values are approximately stable across these resolutions, suggesting numerical convergence for the specific setup.
**Limitations:** the original solver, initial conditions, threshold definition, and raw output are not attached to this record. This result cannot currently be independently reproduced from repository contents.
**Status:** provisional reported result; rerun required.

## Evidence assessment
1. No experiment so far demonstrates that physical matter is a relational fabric.
2. No experiment so far derives the speed of light c from the fabric's own rules.
3. No experiment so far demonstrates physical superluminal propagation.
4. The toy calculations only illustrate expected behavior of prescribed wave/chain models.
5. The prior numerical claims are not promoted to verified results until executable scripts, fixed parameters, random seeds where relevant, raw outputs, and tests are committed and rerun.

## Next preregistered experiment
### EXP-07 — Can a node-free relational model generate a causal speed limit?
Before implementation, specify:
- State variable(s) for the fabric without predefining particle nodes.
- Locality/nonlocality assumptions and evolution rules.
- An operational definition of a controllable information signal.
- How a localized stable structure is detected and what counts as persistence.
- A control model with a speed limit imposed by hand.
- A test for whether the limit emerges from the dynamics rather than from a hidden hard-coded bound.
- A signal-transfer test to ensure faster internal modes do not enable faster-than-causal communication.
- Fixed parameters, numerical stability checks, grid-convergence checks, and raw data preservation.
- Clear failure criteria and independent replication.

**Success condition:** the model produces a robust, measurable causal limit from its own specified rules, while passing the information-transfer test and outperforming a suitable control in explanatory power.
**Failure condition:** the limit is hard-coded, unstable under refinement, or faster internal modes enable controllable superluminal signalling.
A successful toy model would still not establish that the real universe uses this ontology; it would only justify further comparison with known physics.

## Current decision
Keep the relational-fabric idea as an open research hypothesis. Do not state that it is confirmed, and do not merge it with the dark-matter claim as though they were the same result. Investigate any link between them only through an explicit mathematical model and separate tests.

## Reproducibility checklist for future runs
- [ ] Executable source committed
- [ ] Model equations and assumptions documented
- [ ] Parameters and initial conditions fixed
- [ ] Seed recorded where applicable
- [ ] Runtime/library environment recorded
- [ ] Raw numerical outputs saved
- [ ] Unit and stability tests passed
- [ ] Grid/time-step convergence tested
- [ ] Null/control comparison run
- [ ] Results reproduced independently
- [ ] Failures and deviations recorded
