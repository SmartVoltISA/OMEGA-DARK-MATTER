# Ω-DUAL-002B — corrected preregistration
Date: 2026-10-10
Status: registered before corrected run. This is a new confirmatory attempt; Ω-DUAL-002 pilot remains invalid and unchanged.

## Question
In a two-component noisy dynamical process, does access to both specialized sensor streams improve binary prediction compared with a no-message local-decision baseline?

## Data-generating process
For each of 300 independent trajectories and 200 time steps:
x_j(t) = 0.75*x_j(t-1) + ε_j(t), where ε_j ~ Normal(0, 0.25²), j ∈ {1,2}; x_j(0)=0.
Each node sees only its own coordinate plus independent Gaussian observation noise with σ ∈ {0.1, 0.5, 1.0}.
Target y(t) = sign(x1(t)+x2(t)); if exactly zero, y=+1. First 50 steps are burn-in; remaining 150 steps are scored.
Fixed seed: 20261010.

## Conditions (all scored with identical binary accuracy)
- COUPLED_SPECIALISTS: each node sends its observation to the other; joint prediction is sign(obs1+obs2).
- UNCOUPLED_SPECIALISTS: each node outputs sign(its own observation); system-level prediction is majority vote. A tie is broken by a pre-generated fair coin, identical across paired conditions.
- SHUFFLED_PARTNER: node A's observation is combined with node B's observation permuted within the same trajectory across scored times; prediction is sign(obs1+shuffled_obs2).
- SHARED_TARGET_SENSOR: two independent sensors each observe (x1+x2)/2 with Gaussian noise σ; prediction is sign(sensor1+sensor2).
- RELIABILITY SWEEP: at σ=0.5, in COUPLED_SPECIALISTS, each B message is delivered correctly with probability q ∈ {0.25, 0.5, 0.75, 1.0}; otherwise replace it with independent Normal(0,1) noise. Report accuracy.

## Statistics and decision rule
Primary endpoint: paired trajectory-level difference in accuracy between COUPLED_SPECIALISTS and UNCOUPLED_SPECIALISTS. Report mean accuracy and 95% trajectory-bootstrap CI (2,000 resamples) for the paired difference. Also report condition accuracies and 95% trajectory-bootstrap intervals.
Criterion for narrow support: coupled accuracy exceeds uncoupled accuracy and paired 95% CI for the difference excludes zero in at least two of three σ settings. All other outcomes must be reported.
No fitted parameters, no post-hoc tuning, no exclusions.

## Scope
Synthetic benchmark only. Even a positive result supports only this specific information-routing task; it does not establish universal duality, neuroscience claims, or a physical theory. The prior Ω-DUAL-002 pilot was invalid as confirmatory and remains archived as such.
