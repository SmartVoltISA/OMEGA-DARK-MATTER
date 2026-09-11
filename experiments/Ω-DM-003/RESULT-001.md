# Ω-DM-003 — Minimal Relation-Core Result

**Status: PASS — preregistered acceptance gate met for the synthetic gate**

## Execution identity

- Starting model: frozen Ω-DM-002 R3 selected model `W*`.
- Seed: `20260911`.
- N=24; train=40; test=20; length=80.
- K=`0.05`; gamma=`0.02`; sigma=`0.005`; edge_p=`0.12`.
- R3 selected lambda=`0.1`; active edges=`120`.
- Necessity tolerance: `tau=0.01` native observable RMSE units.
- Full frozen deletion table: `FROZEN_DELETION.csv`.
- Executor: `run_core.py`.

## Frozen deletion test

All 120 active edges were deleted individually without refitting and evaluated on the same held-out trajectories.

Full-model held-out RMSE:

| Horizon | R3 W* |
|---:|---:|
| 1 | 18.2849216847 |
| 2 | 46.7045234781 |
| 5 | 94.7945457197 |
| 10 | 142.3210213559 |

**Result:** 0/120 edges exceeded the preregistered one-step necessity threshold `DeltaRMSE > 0.01`. Therefore no edge is provisionally necessary in frozen mode under this criterion.

The largest positive one-step deletion effect was only `+0.0001244630` (edge 7-13), more than 80 times below the `0.01` threshold.

This is a strong redundancy signal: the predictive model contains substantial recoverable information, but its 120 selected edges are not individually indispensable under frozen deletion.

## Random deletion control

A 100-draw matched random active-edge deletion diagnostic was executed. Mean one-step change was `-0.0805140` RMSE with SD `0.2048669`; the sampled maximum was negative. No random-deletion pattern supplied evidence for a distinct necessary-edge effect.

The non-edge control is structurally null because non-active weights are already zero.

The temporal-permutation control is inherited from the certified R3 prerequisite: 20/20 permutation runs selected the empty graph and showed no predictive advantage.

## Backward elimination

Training-only backward elimination used the preregistered `tau=0.01` criterion. Test data were not used for deletion decisions.

| Order policy | Final core size | Held-out h1 | h2 | h5 | h10 |
|---|---:|---:|---:|---:|---:|
| ascending edge ID | 15 | 15.8317432864 | 42.2260087151 | 114.9134564604 | 153.2744641850 |
| descending edge ID | 13 | 16.0520727999 | 42.9102530359 | 119.9396869942 | 158.7286314374 |
| smallest training-loss increase | 20 | 15.4981907310 | 41.4624707197 | 108.2479531729 | 145.4064225523 |

Zero-relation held-out baseline:

| Horizon | Baseline |
|---:|---:|
| 1 | 32.2280692194 |
| 2 | 84.6103802909 |
| 5 | 312.9721731252 |
| 10 | 424.4292656541 |

All three reduced cores beat the zero-relation baseline at all four evaluated horizons.

## Order dependence

The final core is **not identical** across elimination policies: 13, 15 and 20 edges remain. This is explicit order dependence, not hidden. Nevertheless, all three independently satisfy the predictive acceptance requirement. The result therefore supports a **family of minimal predictive cores**, rather than a unique canonical topology.

## Acceptance decision

1. Reduced core obtained: **PASS**.
2. Frozen/reduced core beats zero-relation baseline at h1: **PASS** for all three policies.
3. Reduced core is not worse than baseline at h2, h5, h10: **PASS** for all three policies.
4. Random deletion controls do not establish comparable necessary-edge effects: **PASS**.
5. Order dependence is present but explicitly characterized: **PASS** under the protocol wording.
6. Temporal-permutation control does not reproduce predictive advantage: **PASS** from the certified R3 prerequisite control.

**Overall: PASS.**

## What this actually demonstrates

Ω-DM-003 shows that the R3 predictive relation model can be compressed dramatically—from 120 active edges to 13–20 edges—while retaining predictive performance substantially better than the zero-relation baseline in this synthetic dynamical system.

At the same time, frozen deletion shows that no individual selected edge is necessary under the preregistered threshold. Therefore the evidence points toward **distributed/redundant predictive structure**, not a uniquely identifiable set of indispensable relations.

This does **not** establish that the recovered core is a fundamental physical network. It does not derive gravity or dark matter, and it does not validate a physical relational substrate.

## Next gate

The next scientifically useful step is not to declare victory, but to attack the result with independent synthetic generators and altered observables: test whether the compression/necessity pattern survives when the generating mechanism changes, while keeping inference blind to the generating topology.

`PREDICTIVE CORE ≠ GENERATING GRAPH ≠ PHYSICAL RELATION`
