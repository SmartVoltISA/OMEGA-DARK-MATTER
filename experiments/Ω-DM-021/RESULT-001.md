# Ω-DM-021 — RESULT-001

**Status: PASS-H1 (model-level) / physical interpretation NOT established**

## Execution
Local deterministic runner, cubic 3D lattice `N=31`, unit positive nearest-neighbour relations, zero boundary. Primary conservative case `mu=0`; matched leaky control `mu=0.02`.

## Conservative result
The shell-averaged radial response gradient fit over the preregistered interior range gives:

`p = 1.997456` in `G(r) ~ r^-p`.

Direct edge-current measurement gives shell flux equal to `1.000000` at every tested interior shell to numerical precision. Flux coefficient of variation (excluding the first/last measured shell) is approximately `1.3e-15`.

Thus the computation simultaneously shows:

`Q(r) ≈ constant`

and, in 3D,

`G(r) ∝ Q(r)/r^2`,

with the measured exponent essentially 2.

## Leaky control
With the matched local leakage term `mu=0.02`, the measured exponent becomes `p = 2.417746`. Shell flux decreases monotonically rather than remaining constant; values over the tested shells were approximately:

`0.9385, 0.8932, 0.8490, 0.7952, 0.7504, 0.6984, 0.6529, 0.6067, 0.5666`.

The flux coefficient of variation is about `0.129`, demonstrating loss of conservation and a steeper/screened response.

## Interpretation
**H1 supported for the specified mathematical model.** The inverse-square-like environmental response is recovered from conservation of a local relational flux combined with 3D geometric dilution. No inverse-square radial kernel or gravitational force was inserted.

This is a stronger statement than merely observing a fitted exponent: the conserved quantity is measured directly from the edge relations and remains constant through the interior shells.

The result does **not** derive physical gravity or dark matter. The operator is explicitly a local conservative Laplacian-like relational network, so the experiment establishes a structural mathematical mechanism, not a physical ontology. The next scientific step is to remove remaining operator-specific assumptions and test whether the same conservation→geometry mechanism survives broader classes of local relational dynamics.

## Reproducibility
Runner: `experiments/Ω-DM-021/run_r21.py`

Commits:
- Protocol: `d2076d71fd7642911fc2c729199cc43691cc1f23`
- Runner: `36637d7e737c25b49d9f1bf0c95a636415507248`
