# Ω-DUAL-004 — preregistration
Date: 2026-10-10
Status: registered before execution.

## Question
When the relevance of two signals changes over time and communication has a cost, does adaptive specialization outperform fixed specialization and shared aggregate sensing?

## Model
300 independent trajectories, 300 steps, first 50 burn-in; seed 20261010. State x_j(t)=0.85*x_j(t−1)+Normal(0,0.35²), j=1,2. Relevance regime alternates every 75 steps among weights (0.9,0.1) and (0.1,0.9). Target is sign(w1*x1+w2*x2). Sensor noise sigma=0.5.
Each time step offers two scalar measurements. Specialized sensors observe x1 and x2 with independent Gaussian noise. Shared-sensor control observes the weighted target aggregate twice with independent noise.
Adaptive policy estimates which coordinate currently matters from a short window of recent target errors and selects the weight ordering for the next window. Window size=15; adaptation lag is one full window. No parameter fitting on test trajectories.

## Conditions
1. ORACLE_SPECIALISTS: uses current registered weights, no lag; upper-bound diagnostic.
2. FIXED_SPECIALISTS: assumes (0.9,0.1) throughout, even after regime changes.
3. ADAPTIVE_SPECIALISTS: estimates current dominant coordinate from recent prediction errors and selects the corresponding weight ordering; decisions only affect the next 15-step window.
4. SHARED_AGGREGATE: two independent measurements of the current weighted aggregate.
5. NO_COMMUNICATION: each specialized node makes a local sign prediction; system combines the signs with majority vote, tie resolved by a seeded fair coin.
6. COMMUNICATION_COST: adaptive specialists pay a fixed cost c=0.02 accuracy-equivalent per message; report raw accuracy and net score = accuracy − c*message_count/scored_steps.

Primary metric: held-out-time accuracy, averaged per trajectory. Bootstrap 2,000 resamples by trajectory for paired differences. Primary comparison: adaptive specialists vs fixed specialists. Secondary comparison vs shared aggregate and oracle.
Decision rule: adaptive support only if adaptive beats fixed with paired 95% CI strictly above zero, and net score (with communication cost) also exceeds fixed accuracy in at least two regimes. No post-hoc changes.

## Validity
Synthetic process only. If the adaptive policy is not implemented exactly as described or uses future labels/state, mark invalid. Local run is not CI. No inference to brains, matter, consciousness, or universal duality.
