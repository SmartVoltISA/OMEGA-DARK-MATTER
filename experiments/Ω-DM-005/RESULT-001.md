# Ω-DM-005 — Partial + Noisy Observation Result

Date: 2026-09-11
Status: PASS — robustness gate met

## Execution identity

- Protocol: `PROTOCOL.md`, committed before certification rerun (`7cea1ca7747e1a8b52fbf2c0325a2f0d79d39445`)
- Runner: `run_partial_noisy.py`
- Generator: Ω-DM-004 nonlinear bounded coupling `tanh(1.5*(x_i-x_j))`
- Inference: same R3 symmetric non-negative reconstruction, applied only to observed nodes
- Main seeds: 20260911..20260930 (20)
- Observation: 18 of 24 nodes observed; 6 permanently hidden
- Measurement noise: Gaussian sigma_obs = 0.01
- Process noise sigma = 0.003
- K = 0.02; gamma = 0.02; edge probability = 0.12
- Lambda grid: `{0.1, 0.3, 1, 3, 10, 30, 100}`

## Main result

All 20/20 main seeds beat the zero-relation baseline at every tested horizon.

| Horizon | Mean baseline RMSE | Mean selected RMSE | Mean relative improvement | SD of improvement | Win rate |
|---:|---:|---:|---:|---:|---:|
| 1 | 0.13336 | 0.04731 | 64.14% | 4.03% | 20/20 |
| 2 | 0.38531 | 0.13319 | 64.97% | 4.13% | 20/20 |
| 5 | 1.68007 | 0.49340 | 69.78% | 4.82% | 20/20 |
| 10 | 4.39423 | 0.89496 | 78.53% | 5.70% | 20/20 |

Mean selected lambda: `0.1`.
Mean active-edge count: `77.4`.

## Controls

### W=0 null

10 independent null runs with the same partial/noisy observation model selected the empty graph in all 10 runs. Mean h1 improvement: `0.0`.

### Temporal permutation

10 independent temporal-permutation controls selected the empty graph in all 10 runs. Mean h1 improvement: `0.0`.

No systematic control advantage was observed.

## Acceptance decision

1. h1 win rate >=80%: **PASS — 100%**.
2. Positive mean h1 improvement: **PASS — 64.14%**.
3. h2/h5/h10 win rate >=70%: **PASS — 100% at every horizon**.
4. W=0 and temporal-permutation controls clean: **PASS**.
5. Protocol frozen before certification: **PASS**.
6. Seed-level execution archived in the runner output: **PASS**.

**Overall: PASS.**

## Interpretation

The predictive relational signal survives a substantially harder observation regime: 25% of variables are permanently hidden from inference and the observed trajectories contain measurement noise. The same R3 relation-reconstruction objective still produces held-out predictive improvement on all 20 main seeds.

This strengthens the computational claim that the effect is not dependent on complete noiseless observation.

It does NOT show that the inferred relations are fundamental physical relations, and it does not establish gravity or dark matter.

`ROBUST SYNTHETIC IDENTIFIABILITY ≠ PHYSICAL VALIDATION`

## Next law-discovery gate

The next experiment should stop changing the observation regime and instead attack invariants of the relational dynamics: scaling with system size, permutation/symmetry invariance, conservation quantities, propagation speed, and coarse-graining. Each should be a separate preregistered test with explicit failure criteria.
