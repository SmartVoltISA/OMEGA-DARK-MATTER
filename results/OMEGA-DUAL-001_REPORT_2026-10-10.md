# Ω-DUAL-001 — execution report
Date: 2026-10-10
Status: **EXECUTED LOCALLY; synthetic benchmark only**.

## Result
Across 100,000 generated examples per observation-noise setting (50,000 held-out test examples), the coupled specialized pair predicted XOR correctly at:
- p=0.00: 100.00% (95% Wilson CI 99.992–100.000%)
- p=0.05: 90.53% (90.270–90.784%)
- p=0.10: 82.004% (81.665–82.338%)
- p=0.20: 67.972% (67.562–68.380%)
- p=0.30: 58.092% (57.659–58.524%)

At every noise setting, shuffled-message, identical-node, and uncoupled chance controls were near 50%. At observation noise p=0.10, changing message-delivery reliability q yielded accuracy 18.154%, 34.078%, 50.030%, 66.070%, and 81.846% for q=0, .25, .5, .75, and 1.0 respectively. At q=0 messages are systematically inverted, so performance falls below chance; this is expected for XOR, not evidence of a general anti-coupling effect.

## Interpretation
**The benchmark supports the narrow claim that correctly aligned exchange of complementary information can enable a two-node system to solve this particular XOR task.** Performance degrades with observation noise, and destroying pair alignment removes the advantage.

## Validity audit / limitations
- The task is constructed so that XOR requires information about both independent input bits. The result is therefore partly guaranteed by task design and is not an independent discovery that every whole requires two parts.
- The identical-node control is deliberately deprived of B's information and returns XOR of the same observation with itself. It is a diagnostic for missing complementary input, not a capacity-matched alternative architecture.
- The uncoupled condition uses a fair-coin predictor, which is the appropriate no-information baseline for independent equiprobable XOR, but does not model every possible uncoupled system.
- This is a deterministic synthetic simulation with independent bit flips; it says nothing directly about cerebral hemispheres, physical matter, consciousness, or universal ontology.
- The preregistration's wording that the first half is "train" and the second half "test" is nominal: no model is fitted, so there is no training phase. The report treats the second half as held-out evaluation only.
- The registered primary comparison is coupled versus uncoupled chance; shuffled-message and identical-node controls are secondary diagnostic comparisons. No post-hoc parameter tuning was used.
- Execution status is local Python/NumPy execution. No GitHub Actions/CI run was performed. The committed runner should be re-run in the target environment to verify byte-for-byte reproducibility before calling the artifact independently reproduced.

## Decision
**PARTIAL SUPPORT for the narrow synthetic mechanism; NOT CONFIRMED as a general duality principle.** Next experiment should use a less tautological, capacity-matched dynamical coordination task where the value of specialization and coupling is not guaranteed by the target definition.
