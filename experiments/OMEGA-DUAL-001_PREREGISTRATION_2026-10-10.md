# Ω-DUAL-001 — preregistration
Date: 2026-10-10
Status at registration: PREREGISTERED; not yet executed.

## Question
In a deliberately minimal synthetic coordination task, does bidirectional information exchange between two functionally specialized nodes improve prediction over uncoupled, duplicated/identical, and shuffled-message controls? This tests only this model and task, not a universal law about all wholes.

## Hypotheses
- H1: Under noisy observations, specialized nodes that exchange information outperform uncoupled specialized nodes on held-out XOR prediction.
- H0: Coupling does not improve held-out performance over the uncoupled baseline.
- Secondary: performance should decline as observation noise rises; shuffled messages should remove most of any genuine coupling advantage.

## Frozen design
- Task: independent equiprobable bits A and B; target Y = A XOR B.
- Node A receives only a noisy version of A; node B receives only a noisy version of B. Each observation bit is independently flipped with probability p.
- Specialized local decoder estimates its own source bit by using its observation (ties do not occur).
- Uncoupled condition: each node retains only its local evidence; prediction of XOR is based on local estimates but without exchanging the other node's estimate. Because the nodes cannot jointly observe both bits, its preregistered prediction is a fair coin.
- Coupled condition: nodes exchange their local estimates; combined prediction is XOR of the two estimates.
- Shuffled-message control: partner estimates are permuted independently across examples, breaking pair alignment while preserving marginal message frequencies.
- Identical-node control: both nodes are given the same noisy observation of A and use the same decoder; their XOR output cannot access B.
- Noise p ∈ {0.00, 0.05, 0.10, 0.20, 0.30}.
- 100,000 examples per noise level; deterministic seed 20261010; generated examples split in order into 50% train / 50% test, with no learned parameters. Primary endpoint: held-out accuracy. Report all conditions and the binomial 95% Wilson interval.
- A separate coupling-strength sweep uses probability q ∈ {0, .25, .50, .75, 1.0} that each partner estimate is delivered correctly; when not delivered correctly, the received bit is flipped. Same seed and examples for paired comparisons.
- No exclusions or post-hoc changes. If implementation deviates, mark invalid and retain artifacts.

## Validity limits
This is a constructed information-routing demonstration. The task itself makes XOR require information about both bits; a successful result cannot establish that every whole needs two parts, that the brain follows this mechanism, or that it describes matter, consciousness, or physical reality. A trivial/prior-matched baseline and shuffled-message control are required to interpret results.

## Execution checklist
1. Commit this protocol before running the experiment.
2. Run the exact implementation locally.
3. Save code, machine-readable results, report, and execution status.
4. Record negative results and validity limitations.
