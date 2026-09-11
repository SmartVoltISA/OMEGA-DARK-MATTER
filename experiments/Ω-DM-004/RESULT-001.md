# Ω-DM-004 — Independent-Generator Result

**Status: PASS — cross-mechanism synthetic gate met**

## Execution identity

- Protocol: `PROTOCOL.md`, committed before certification rerun.
- Generator: nonlinear bounded coupling `tanh(1.5(x_i-x_j))`.
- Inference: unchanged R3 symmetric non-negative reconstruction.
- Main seeds: `20260911..20260930` (20).
- Null controls: 10 W=0 seeds.
- Temporal-permutation controls: 10 seeds.
- N=24; train=40; test=20; length=80; K=0.02; gamma=0.02; sigma=0.003; edge_p=0.12.
- Lambda grid: `{0.1, 0.3, 1, 3, 10, 30, 100}`.

## Main result

All 20/20 main seeds beat the zero-relation baseline at every tested horizon.

| Horizon | Mean relative improvement | SD | Win rate |
|---:|---:|---:|---:|
| 1 | 59.24% | 1.12% | 20/20 |
| 2 | 22.73% | 0.73% | 20/20 |
| 5 | 9.58% | 0.40% | 20/20 |
| 10 | 14.42% | 0.62% | 20/20 |

Mean selected lambda: `0.1`.
Mean active-edge count: `68.1`.

## Controls

The 10 W=0 null runs selected the empty graph and had mean h1 improvement `0.0`.

The 10 temporal-permutation controls likewise selected the empty graph and had mean h1 improvement `0.0`.

No systematic control advantage was observed.

## Acceptance decision

1. h1 success rate >=90%: **PASS — 100%**.
2. h2/h5/h10 success rate >=80%: **PASS — 100% at every horizon**.
3. Mean improvement positive at all horizons: **PASS**.
4. Controls show no systematic predictive advantage: **PASS**.
5. Generating topology hidden from inference: **PASS**.

**Overall: PASS.**

## Interpretation

This is stronger than repeating Ω-DM-002's original linear generator: the relation generator is now nonlinear and bounded, while the inference model is kept unchanged. The predictive advantage therefore survives a change in the data-generating mechanism.

However, this remains a synthetic result. It does not establish a physical relational substrate, gravity, or dark matter. It also does not show that the inferred topology equals the generating topology.

`CROSS-MECHANISM REPLICATION ≠ PHYSICAL VALIDATION`

## Next gate

The next useful attack is to alter the observable itself and test whether the relation signal remains identifiable under partial/noisy observation, rather than continuing to optimize the same synthetic setting.
