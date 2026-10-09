# Ω-21 — Common-snapshot perturbation recovery

**Status:** exploratory numerical run, 40 seeds × 6 branches = 240 evaluations, executed in a Python analysis session. The final protocol/report was committed after the run, so this is **not a preregistered result**.

## What changed
For each seed, one training trajectory creates a common continuous-state snapshot. Every branch begins from that exact snapshot, and the same 10% node patch is sign-inverted before 100 recovery steps. This removes the main state-history mismatch from Ω-20 for the signed conditions.

## Results

| Mode | Relation retention | State recovery |
|---|---:|---:|
| Adaptive live | 0.9230 ± 0.0386 | 0.7155 ± 0.1887 |
| Frozen learned | **0.9377 ± 0.0395** | **0.7692 ± 0.2018** |
| Permuted learned | 0.8974 ± 0.0387 | 0.7461 ± 0.1829 |
| Fixed original | 0.9150 ± 0.0339 | 0.7537 ± 0.1909 |
| Adaptive unsigned | 0.5000 ± 0.0272* | −0.3233 ± 0.7167* |
| No coupling | 0.9770 ± 0.0040* | 0.5000 ± 0.0000* |

Mean ± sample SD over 40 seeds.  
* These metrics are not directly comparable to the signed modes: the unsigned branch changes the scoring convention, and no-coupling states decay to approximately zero, making sign-based retention degenerate. Do not interpret these values as robust organization.

## Paired comparisons: adaptive live minus control

| Control | Relation-retention difference (95% CI) | State-recovery difference (95% CI) |
|---|---:|---:|
| Frozen learned | −0.01469 [−0.01953, −0.01000] | −0.05369 [−0.06076, −0.04666] |
| Permuted learned | +0.02555 [+0.01680, +0.03445] | −0.03058 [−0.04275, −0.01562] |
| Fixed original | +0.00797 [+0.00172, +0.01445] | −0.03827 [−0.04922, −0.02666] |

10,000 paired bootstrap resamples.

## Interpretation
The live adaptive mode retained more relations than the permuted and fixed signed controls, but less than frozen learned weights. On the continuous-state recovery metric, live adaptation was worse than all three signed controls, with paired confidence intervals excluding zero. Therefore, ongoing adaptation did not improve recovery in this implementation.

This is mixed evidence about retention and negative evidence for improved recovery. It is not support for the broad claim that adaptive competing links create a more resilient substrate.

## Limitations and next correction
- This run was exploratory, not preregistered before execution.
- The no-coupling sign-retention statistic is degenerate when state magnitude tends to zero.
- Unsigned and signed relation scores use different conventions and should not be ranked against each other.
- Next run should preregister a single relation score that explicitly includes signed edge preference and a minimum state-amplitude threshold; all modes must share the same initial snapshot, and comparisons should focus on signed controls.
