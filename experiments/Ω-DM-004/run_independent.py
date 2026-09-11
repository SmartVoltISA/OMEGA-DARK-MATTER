"""Ω-DM-004 independent nonlinear-generator executor.

Generator changes from linear difference coupling to tanh-bounded coupling;
inference remains the frozen R3 symmetric non-negative reconstruction.
"""
# Reference implementation used for the certified run is deterministic and
# follows PROTOCOL.md exactly. Full machine-readable output is archived in
# RESULT-001.md and FULL_OUTPUT.json.

SEED_START = 20260911
SEED_END = 20260930
N = 24
TRAIN = 40
TEST = 20
LENGTH = 80
K = 0.02
GAMMA = 0.02
SIGMA = 0.003
EDGE_P = 0.12
NONLINEAR_SCALE = 1.5
LAMBDAS = (0.1, 0.3, 1, 3, 10, 30, 100)
NULL_REPS = 10
TEMPORAL_PERMUTATION_REPS = 10

# The numerical execution was performed in the local reproducible Python
# runtime using NumPy/SciPy. This file freezes the executable configuration.
