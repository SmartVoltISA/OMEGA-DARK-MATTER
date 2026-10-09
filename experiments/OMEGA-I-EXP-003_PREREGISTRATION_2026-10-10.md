# Ω-I-EXP-003 — Separating present state, organization, and causal history
Date: 2026-10-10
Status: preregistered before execution. Synthetic benchmark only.

## Research question
When two system snapshots look similar, do present-state features, organizational features, and causal-history features provide different information about (a) next-state prediction and (b) lineage continuity in a controlled synthetic system?

## Scope and caution
This experiment operationalizes lineage continuity by simulation bookkeeping. That makes the label objective within the toy world but does not establish a universal definition of identity, human personal identity, consciousness, or physics.

## Generative conditions
Generate 4,000 paired comparisons per condition, split by independent trajectory family into 70% train and 30% held-out test:
A. CONTINUOUS: same trajectory, adjacent time points; lineage label = same.
B. SNAPSHOT_COPY: clone current state into a new independent future trajectory; current snapshot matches exactly at copy time, lineage label = different.
C. FUNCTION_PRESERVED_REWIRE: replace graph wiring while preserving node count, degree sequence, and a designated input-output function; lineage label = different.
D. SAME_LINEAGE_ELEMENT_REPLACEMENT: replace individual carrier nodes while preserving the lineage's transition rule and state mapping; lineage label = same by simulation lineage bookkeeping.
E. IID_CONTROL: independent states, no temporal dependence.

Each simulated system has a 12-dimensional state and a 12-node directed weighted graph. Dynamics use a stable linear transition matrix plus Gaussian noise. Conditions B–D explicitly intervene on clone/graph/carrier while retaining or breaking the parent lineage according to the condition definition.

## Features and models
For pair classification, compare:
1. PRESENT_ONLY: distance between current state vectors.
2. ORGANIZATION: present-state distance plus graph degree/weight summaries and input-output response summary.
3. HISTORY_AWARE: organization features plus five-step state-history similarity and transition-residual signature.
Use standardized logistic regression with fixed C=1.0; no tuning on test set. Report held-out ROC-AUC and balanced accuracy. Also report a simple future-state RMSE task for current-only vs five-lag linear regression.

## Controls and uncertainty
- Split by trajectory family, not individual rows, to reduce leakage.
- Fixed seed 20261010.
- 2,000 bootstrap resamples over held-out families for 95% percentile intervals.
- Negative controls: shuffle history features within training families; IID condition.
- Record all conditions, model metrics, and confusion matrices.

## Decision rules
A feature family is incrementally useful only if held-out performance improves against the simpler model and the bootstrap interval for paired family-level improvement excludes zero. A positive result in these synthetic settings supports only that the engineered features recover the simulation's stipulated lineage convention. It is not evidence that the convention is the correct definition of identity in real systems.

## Reproducibility
Store executable code, raw aggregate JSON, report, and this preregistration. Local execution is not equivalent to GitHub Actions/CI; state execution venue honestly.
