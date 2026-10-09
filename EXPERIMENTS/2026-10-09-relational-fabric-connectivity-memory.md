# Ω-16 — Connectivity memory vs ongoing adaptation

**Date:** 2026-10-09  
**Status:** Results from 80 runs recorded; protocol correction included in the committed script.

## Question
Does a learned edge-weight pattern itself store useful memory, or does recovery require continued adaptation?

## Protocol
N=160, ring-like graph with sparse rewiring, 80 preconditioning steps, then an eight-node local sign inversion and 80 recovery steps. Four modes: adaptive live; frozen learned weights; fixed original weights; learned weight values shuffled across edges during recovery. Same seed set (20261040–20261059) across modes.

## Recorded results from the preceding run

| Mode | Patch recovery | Global agreement with unperturbed copy | Original-domain retention | Weight SD |
|---|---:|---:|---:|---:|
| Adaptive live | 8.75% | 95.38% | 93.56% | 0.4167 |
| Frozen learned | 16.88% | 93.69% | 88.97% | 0.1736 |
| Fixed original | 16.88% | 93.69% | 88.97% | 0.1736 |
| Shuffled learned | 15.00% | 91.94% | 88.38% | 0.1736 |

Paired adaptive-live vs frozen domain-retention difference was +4.59 percentage points; 19/20 seeds favored adaptive live; bootstrap 95% interval [+3.34, +5.88] points. Adaptive live vs shuffled: +5.19 points, 19/20 seeds favored adaptive live; interval [+3.81, +6.53] points. Local patch recovery was lower for adaptive live by 8.13 points on average; bootstrap interval [-18.75, 0] points.

## Critical protocol note

The previously executed run did **not** train weights in the frozen-learned condition: only adaptive-live updated weights during preconditioning. Therefore the old frozen-learned values are effectively the fixed-original control and cannot answer whether learned weights alone store memory.

The committed script corrects this flaw by training weights during preconditioning for both adaptive-live and frozen-learned modes. **The corrected script has not yet been executed in this turn**, so its results must not be confused with the recorded table above. The next action is to run this corrected version and replace the summary with its actual output.

## Interpretation
Current data provisionally suggest continued adaptation preserves the imposed global domain pattern better, but patch repair is poor. There is no valid conclusion yet about learned weights alone storing memory because of the control flaw. The four-domain pattern is imposed, not spontaneously generated. Toy model only; not evidence for physical matter being relational fabric.
