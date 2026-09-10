# Ω-DM — RELATION STATE MODEL v0.1

Date: 2026-09-11
Status: MODEL CANDIDATE / NOT PHYSICAL VALIDATION

## Purpose

Extract the smallest common quantitative representation from the existing relation, graph, field, interaction, motion, light, mass and gravity branches without declaring their concepts physically identical.

## 1. Candidate system state

```text
G(t) = (V, E(t), S_V(t), S_E(t))
```

- `V`: distinguishable entities / nodes.
- `E(t)`: relation topology at time `t`.
- `S_V(t)`: state variables attached to entities.
- `S_E(t)`: state variables attached to relations.

This is an abstract state representation. It is not yet a physical field theory.

## 2. Relation state

A relation is treated as an inspectable object rather than only a binary pointer.

Candidate components:

```text
r_ij(t) = [a_ij, w_ij, k_ij, g_ij, tau_ij, m_ij, c_ij, b_ij, ...]
```

Possible meanings, only after operational definition:

- `a`: existence / activity;
- `w`: strength or weight;
- `k`: stiffness / response coefficient;
- `g`: geometry / orientation descriptor;
- `tau`: propagation or response delay;
- `m`: retained relational memory;
- `c`: capacity;
- `b`: breaking threshold.

No variable receives a physical unit merely because a similarly named quantity exists in physics.

## 3. Minimal update law

The generic form is:

```text
S_E(t+dt) = F_E(S_E(t), S_V(t), topology, boundary, parameters)
S_V(t+dt) = F_V(S_V(t), S_E(t), external_inputs, parameters)
```

The first scientific requirement is to make `F_E` and `F_V` explicit and minimal.

## 4. Propagation / transition layer

A transition is represented as:

```text
S(t) → S(t+dt)
```

A propagating disturbance is a structured sequence of local state changes:

```text
local state change → neighboring relation response → next local state change → ...
```

The LIGHT branch provides a controlled computational example where a relation-based representation reproduces wave-like propagation, while the full electromagnetic interpretation remains external input.

## 5. Memory is not automatic

Existing ORISIK work contains a limiting result: propagation plus dissipation alone did not guarantee persistent relational memory in the tested damped model.

Therefore:

```text
propagation + dissipation ≠ memory
```

A memory mechanism must be explicitly specified and independently tested.

## 6. Topology is an observable model variable

Ω-LINK-1 provides controlled-model evidence that:

- identical node and edge counts can yield different behavior when edge placement differs;
- reversing direction can alter reachable-state structure;
- deleting one edge can have different global effects depending on alternative paths.

Thus a quantitative model cannot generally reduce a network to node count + edge count alone.

## 7. Field bridge — unresolved

A possible coarse-graining is:

```text
microscopic relation state S_E
        ↓ coarse-graining
relational density / order parameter ρ_R(x,t)
        ↓
dynamical field equation
        ↓
effective contribution A_eff(x,t)
        ↓
observable
```

This is a proposed modelling route, not an established physical mapping.

The coarse-graining operator and units of `ρ_R` remain undefined.

## 8. Ω-DM minimum bridge

```text
relation state
      ↓
explicit interaction law
      ↓
coarse-grained effective dynamics
      ↓
gravitational observable
      ↓
rotation curves / lensing / structure
```

To become a scientific test, the model must specify:

1. variables and units;
2. equations;
3. initial and boundary conditions;
4. fixed versus fitted parameters;
5. baseline models;
6. likelihood/error model;
7. complexity penalty;
8. held-out data;
9. null/permutation controls;
10. independent replication.

## 9. Hard derivation barriers

The current LIGHT run shows that relation-first representations can reproduce several known electromagnetic structures computationally, but it does not derive:

- U(1);
- spacetime dimension/signature;
- unique Maxwell kinetic term;
- alpha;
- quantum commutation relations;
- photon representation;
- matter charge spectrum.

Likewise, the current gravity branch does not derive a gravitational field equation from relation state.

## 10. Falsification-first Ω-DM-001

Before fitting observational galaxies, implement a synthetic test with a known injected relational contribution.

### Null

Set the relational contribution to zero while retaining the same numerical framework.

### Recovery

Inject a known relational contribution and test whether the inference procedure recovers it.

### Permutation

Destroy relational topology while preserving selected low-level statistics.

### Complexity control

Compare against the simplest conventional baseline and penalize additional degrees of freedom.

### Held-out test

Freeze parameters before evaluation on data not used for calibration.

## 11. Current conclusion

The repositories support a common abstract state language around:

```text
DISTINCTION → RELATION → STATE → INTERACTION → TRANSITION → PROPAGATION → STRUCTURE → OBSERVABLE
```

They do not yet establish that this abstract language is a fundamental physical ontology, nor that it produces gravity or dark-matter phenomenology.

The next decisive step is an explicit minimal update law plus synthetic recovery/falsification tests.
