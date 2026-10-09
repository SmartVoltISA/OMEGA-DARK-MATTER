# Ω-20 — Competing links and perturbation recovery

**Status:** preregistered before numerical execution.

## Question
Can adaptive signed relations produce a robust multi-domain organization that survives perturbations better than fixed, shuffled, and unsigned-consensus controls?

## Hypothesis and null
H1: a signed adaptive network (with both reinforcing and competing edges) has higher post-perturbation domain retention and recovery than matched fixed and shuffled controls.
H0: the adaptive signed mode does not outperform controls on paired seeds.

## Protocol
- 40 paired seeds: 20262000–20262039; N=160; ring-derived graph with k=4, rewiring probability 0.03.
- Random initial state Normal(0,0.15), no seeded domains.
- Edge weights Uniform(0.7,1.3), mean-normalized across conditions.
- Modes: (A) adaptive signed links; (B) frozen learned signed weights; (C) learned weights permuted across edges; (D) fixed unsigned weights; (E) adaptive unsigned weights; (F) no coupling.
- Signed dynamics use the weighted neighbour field divided by sum of absolute incident weights; edge signs are positive or negative. Update x' = tanh(0.35x + J × signed-neighbour-field), J=0.85.
- Adaptation strengthens edges when endpoint states align and weakens/reverses them when they oppose; clip magnitude to [0.1,1.3], with an explicit penalty toward the initial magnitude. Weight means and absolute means are matched after training.
- Train for 100 steps, evaluate for 100 steps. Then invert the sign of a fixed 10% node patch and evolve for 100 recovery steps.
- Primary metrics: sign agreement weighted by edge sign (same-sign nodes on positive edges and opposite-sign nodes on negative edges); post-perturbation retention relative to pre-perturbation edge relations; recovery toward pre-perturbation state.
- Secondary: number of connected components under the edge-preferred relation, state RMS, edge sign fraction.
- Same graph and initial state paired across modes; 40 seeds. Report mean ± sample SD and paired bootstrap 95% CIs with 10,000 resamples, fixed bootstrap seed 20262099.
- No parameter tuning after results are inspected.

## Decision rule
H1 is supported only if adaptive signed links outperform both frozen learned signed weights and shuffled learned weights on the primary post-perturbation retention metric, with both paired 95% CIs excluding zero. Otherwise record H1 as unsupported.

## Limits
Toy network only. This does not model real particles or establish a physical substrate, dark matter, or superluminal information transfer.
