# Ω-23 — Continuous signed-relation margin

**Status:** preregistered before execution.

## Question
Does learned edge-magnitude structure improve post-perturbation relational alignment when every edge contributes continuously, avoiding the low-coverage gate used in Ω-22?

## Primary metric
For each state vector x and fixed signed edge labels s_e ∈ {-1,+1}, define the continuous signed edge product p_e = s_e x_i x_j. The primary outcome is the raw mean margin M = mean(p_e) over **all** edges. Positive values mean the states tend to align with the edge signs; values near zero can reflect weak activity, so RMS state amplitude and mean absolute edge product A = mean(|x_i x_j|) are mandatory companion metrics. Secondary normalized alignment Q = M/(A + 1e-12) is reported only alongside A and is not the primary decision metric. No amplitude threshold or edge exclusion is used.

## Protocol
- 40 paired seeds: 20262300–20262339; N=160; ring-derived graph with k=4 and rewiring probability 0.03.
- Random Gaussian initial states N(0, 0.15); edge magnitudes Uniform(0.7, 1.3); edge signs independently ±1.
- Train one common network for 100 steps. All conditions branch from the same trained state and receive the same sign-flip perturbation to the first 10% of nodes.
- Conditions: adaptive-live learned magnitudes; frozen learned magnitudes; learned magnitudes permuted across edges; original fixed magnitudes; no coupling.
- To isolate magnitude assignment, **edge signs remain fixed to the original sign labels in every coupled condition**. The adaptive mode updates magnitudes only; it does not flip edge signs.
- Dynamics: x' = tanh(0.35x + 0.85 × signed weighted-neighbour field), normalized by total incident absolute weight. Train 100 steps; evaluate 100 post-perturbation steps.
- Primary: post-perturbation M over all edges. Secondary: pre/post M, M change from common pre-perturbation state, A, Q, state recovery, and RMS amplitude.
- Paired comparisons: frozen-learned minus permuted-learned and frozen-learned minus fixed-original, with 10,000 paired bootstrap resamples (seed 20262399), 95% percentile CIs.
- No-coupling is a degenerate dynamical control; if its state decays to near zero, its alignment score must not be interpreted as evidence of organization.

## Decision rule
Evidence for a learned-magnitude benefit requires the frozen-learned minus both controls primary-M differences to have positive 95% paired-bootstrap CIs, without the result being explained by lower/higher state activity alone. Otherwise report no demonstrated benefit or an inconclusive outcome. This is a toy-network test, not a physical test of dark matter or superluminal propagation.

## Integrity
Commit this preregistration before running the experiment. Record the actual execution environment and retain per-seed rows in the result JSON.
