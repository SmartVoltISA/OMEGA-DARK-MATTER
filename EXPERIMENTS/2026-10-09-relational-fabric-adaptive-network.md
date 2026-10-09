# Ω-12 — Adaptive relational network without a double-well potential

**Date:** 2026-10-09  
**Status:** Six runs executed: three seeds × adaptive/fixed-weight control.

## Question
Can relation weights differentiate under co-activity alone, without a double-well potential or prescribed preferred node states?

## Model
64 nodes on a fixed sparse connected undirected graph. Node states follow damped noisy graph diffusion. Adaptive weights update by a bounded co-activity rule, \(W_{ij}\leftarrow\mathrm{clip}(W_{ij}+dt[\eta\tanh(x_ix_j/\sigma^2)-\gamma(W_{ij}-0.05)],0,0.5)\). Controls keep weights fixed at 0.05. There is no double-well potential and no preferred ±1 state.

Parameters: 5000 steps, dt=0.01, eta=0.3, gamma=0.3, damping mu=0.1, noise 0.03, sigma=0.01. Initial states are Gaussian noise with SD 0.01.

## Final results at step 5000

| Seed | Condition | State RMS | Weight SD | Zero-weight fraction | Mean abs. edge-state difference |
|---|---|---:|---:|---:|---:|
| 20261014 | Adaptive | 0.00557 | 0.12248 | 20.8% | 0.00637 |
| 20261015 | Adaptive | 0.00528 | 0.09471 | 17.1% | 0.00584 |
| 20261016 | Adaptive | 0.00493 | 0.10192 | 17.0% | 0.00563 |
| 20261014 | Fixed | 0.00568 | 0.00000 | 0.0% | 0.00648 |
| 20261015 | Fixed | 0.00522 | ~0.00000 | 0.0% | 0.00586 |
| 20261016 | Fixed | 0.00490 | 0.00000 | 0.0% | 0.00574 |

## Interpretation

1. Adaptive relation weights differentiated: SD reached 0.095–0.122 and around 17–21% of edge weights reached zero.
2. Node states did not amplify into stable domains; their RMS remained around 0.005–0.006.
3. Adaptive and fixed controls had similar state RMS. The clearest effect was heterogeneous edge weights, not a new state pattern.
4. This does not prove that relations create matter. The model still prescribes nodes, topology, state variables, a weight-update law, damping and noise.
5. An initial metrics implementation had an indexing bug and failed; it was corrected before the six reported runs.

## Reproducibility
Code: `experiments/relational_fabric_adaptive_network.py`  
Data: `results/2026-10-09-relational-fabric-adaptive-network.json`

Numerical functions were executed in the current Python session. The saved script and JSON were fetched back from GitHub for verification, but the repository script itself was not executed directly during this run.

## Next test
Compare adaptive, shuffled-weight, fixed-weight and no-coupling controls under identical graph topology and random forcing. Preregister a persistent-cluster metric and require it to beat controls across more seeds.
