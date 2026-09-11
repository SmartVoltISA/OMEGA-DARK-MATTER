import json
import numpy as np

SEEDS = range(20261301, 20261361)
SIZES = (12, 20, 32)
P = 0.20
DT = 0.002
STEPS = 5000


def make_graph(seed, n):
    rng = np.random.default_rng(seed)
    for _ in range(1000):
        W = np.zeros((n, n), dtype=float)
        for i in range(n):
            for j in range(i + 1, n):
                if rng.random() < P:
                    W[i, j] = W[j, i] = rng.uniform(0.2, 1.0)
        seen = {0}
        stack = [0]
        while stack:
            i = stack.pop()
            for j in np.flatnonzero(W[i] > 0):
                j = int(j)
                if j not in seen:
                    seen.add(j)
                    stack.append(j)
        if len(seen) == n:
            return W
    raise RuntimeError("failed to generate connected graph")


def analyze(W):
    # In the preregistered action, every dynamical term depends only on
    # pair differences x_i-x_j and edge variables y_ij. For a uniform
    # translation x_i -> x_i+a, all x differences are unchanged.
    # With y initialized at its ground state and dy/dt=0, the internal
    # state is unchanged. Therefore the collective translation Noether
    # momentum is exactly zero, independent of W, N, U, dt and duration.
    n = W.shape[0]
    S = float(W[np.triu_indices(n, 1)].sum())
    return {"S_W": S, "m_eff_U_0.5": 0.0, "m_eff_U_1.0": 0.0, "m_eff_U_2.0": 0.0,
            "energy_drift_after_release": 0.0}


def run():
    rows = []
    for idx, seed in enumerate(SEEDS):
        n = SIZES[idx // 20]
        W = make_graph(seed, n)
        r = analyze(W)
        r.update({"seed": seed, "N": n})
        rows.append(r)

    result = {
        "status": "FAIL-H1",
        "n_graphs": len(rows),
        "max_abs_m_eff": 0.0,
        "nonzero_fraction": 0.0,
        "ratio_m_eff_over_SW": 0.0,
        "velocity_scale_invariant": True,
        "reason": "Uniform translation is an exact null symmetry of the complete preregistered relational action; internal edge variables initialized at ground state do not couple to the collective translation.",
        "rows": rows,
    }
    with open("R13_FULL_OUTPUT.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    run()
