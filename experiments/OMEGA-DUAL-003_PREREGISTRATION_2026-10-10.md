# Ω-DUAL-003 — preregistration
Date: 2026-10-10
Status: protocol committed before execution.

## Question
Does allocating two noisy sensors to complementary state components (specialization) outperform giving both sensors to a common aggregate signal, when total sensor count, noise, and scoring are matched?

## Hypotheses
H1: specialization + exchange improves binary prediction over shared-aggregate sensing when the two state components have different time-varying relevance.
H0: specialization does not improve prediction over shared-aggregate sensing.
No assumption that H1 must win; shared sensing may be superior.

## Generative process
300 independent trajectories, 240 steps each; first 40 steps burn-in; seed 20261010. Hidden state x1,x2 follows x_j(t)=0.82*x_j(t−1)+epsilon_j(t), epsilon~Normal(0,0.3²). Relevance weights change by regime: for steps 0–119, w=(0.8,0.2); for steps 120–239, w=(0.2,0.8). Target y(t)=sign(w1*x1+w2*x2), exact zero maps to +1.
Two sensor channels per time step. Observation noise sigma ∈ {0.2,0.6,1.0}; independent Gaussian noise.

## Conditions
A. SPECIALIZED: sensor 1 observes x1+noise, sensor 2 observes x2+noise; combined prediction sign(w1*obs1+w2*obs2), using the known current regime weights.
B. SHARED_AGGREGATE: both sensors observe (w1*x1+w2*x2)+noise; prediction sign(sensor1+sensor2).
C. MISALLOCATED_SPECIALISTS: sensors still observe x1 and x2 but the weights are swapped, representing stale specialization across the regime transition.
D. SINGLE_SENSOR_SHARED: one shared aggregate sensor plus a fair random second sensor, as a resource ablation.
All conditions have two scalar sensor channels per step; no model fitting.
Primary metric: trajectory-level accuracy, same scoring timestamps for all conditions. Compare SPECIALIZED minus SHARED_AGGREGATE with paired trajectory bootstrap 95% CI (2,000 resamples). Secondary: first versus second regime and performance around transition. Report all results.
Criterion for narrow support: specialized accuracy exceeds shared-aggregate accuracy and paired CI excludes zero at two or more sigma levels. Otherwise no support under this benchmark.
No post-hoc tuning or exclusions. If code differs from this protocol, label invalid.

## Scope
Synthetic benchmark only. This can test task-dependent sensor allocation, not universal duality, neuroscience, consciousness, or a physical theory. Local execution must not be described as CI.
