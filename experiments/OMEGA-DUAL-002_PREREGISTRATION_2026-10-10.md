# Ω-DUAL-002 — preregistration
Date: 2026-10-10
Status: PREREGISTERED before execution.

## Research question
Does functional specialization plus communication improve performance in a noisy dynamical coordination task when compared with a capacity-matched non-specialized system, and can communication also hurt?

## Hypotheses
- H1 (conditional): specialization plus reliable coupling improves held-out task reward when each node has a distinct useful sensor.
- H0: the specialized coupled system does not outperform the capacity-matched shared-information baseline.
- Adverse outcome allowed: coupling may transmit noise or stale information and reduce reward under low communication reliability.

## Model
A two-dimensional hidden state x(t) = [x1(t), x2(t)] evolves as a noisy stable linear process:
x(t+1) = 0.75*x(t) + 0.25*u(t) + process_noise.
At each time step, a target action is the sign of x1(t)+x2(t). Each agent chooses an estimate/action from its available sensor values. Sensor noise is Gaussian and independent.

Conditions:
1. SPECIALIZED_COUPLED: node A senses x1, node B senses x2; each sends its local observation to the other; both form an estimate of the shared target.
2. SPECIALIZED_UNCOUPLED: same specialized sensors and local computation budget, but no messages; the system's action is the mean of each node's local sign estimate.
3. SHARED_SENSOR_CONTROL: both nodes receive the same noisy observation of (x1+x2)/2, with the same total number of scalar observations as the specialized condition; their actions are averaged.
4. SHUFFLED_MESSAGE_CONTROL: specialized sensors, but received messages are permuted across time within each trajectory, breaking temporal alignment.
5. SPECIALIZED_COUPLING_ABLATION: specialized coupled condition with communication reliability q in {0, 0.25, 0.5, 0.75, 1.0}; a message is replaced with fresh Gaussian noise with probability 1-q.

Primary outcome: mean squared error (MSE) predicting the sign target via continuous estimate x1+x2; a correct sign is secondary. This is a controlled toy model, not a brain model.
Observation noise sigma ∈ {0.1, 0.5, 1.0}; communication reliability q ∈ {0.25, 0.5, 0.75, 1.0}.
Use 300 independent trajectories per sigma, 200 time steps each; first 50 steps burn-in, remaining 150 scored. Fixed seed 20261010. Report mean and trajectory-bootstrap 95% interval (2,000 resamples) for paired MSE differences. No parameter fitting, no post-hoc tuning.

## Decision rule
Primary comparison: SPECIALIZED_COUPLED versus SPECIALIZED_UNCOUPLED at q=1. A positive benefit requires lower MSE and a paired 95% bootstrap interval for (MSE_uncoupled − MSE_coupled) strictly above zero in at least two of three noise settings. Report all conditions, including negative outcomes. This rule is a local benchmark criterion only.

## Validity constraints
- The dynamics and target are synthetic.
- Because target depends on both state dimensions, a specialization benefit is task-dependent; no inference about all wholes, hemispheres, matter, or consciousness.
- If any implementation condition differs from this protocol, flag it and do not call the run confirmatory.
- Save code, machine-readable results, and report. Local execution is not CI execution.
