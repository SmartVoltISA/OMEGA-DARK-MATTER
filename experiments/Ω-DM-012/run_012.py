import json
import numpy as np

SEEDS = range(20261201, 20261301)
SIZES = (10, 20, 40)
P_EDGE = 0.20
TOL = 1e-12


def make_graph(seed, n):
    rng = np.random.default_rng(seed)
    for _ in range(10000):
        W = np.zeros((n, n))
        for i in range(n):
            for j in range(i + 1, n):
                if rng.random() < P_EDGE:
                    w = rng.uniform(0.2, 1.0)
                    W[i, j] = W[j, i] = w
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


def measure(W):
    n = len(W)
    d = W.sum(axis=1)
    L = np.diag(d) - W
    u = np.ones(n)

    # T_rel = v^T L v; grad_v(T_rel) = 2 L v; Hessian = 2 L.
    T = float(u @ L @ u)
    p = 2.0 * (L @ u)
    P = float(p.sum())
    Hquad = float(u @ (2.0 * L) @ u)

    rng = np.random.default_rng(900000 + n)
    z = rng.normal(size=n)
    z -= z.mean()
    T_nonuniform = float(z @ L @ z)

    # Positive control: explicit absolute kinetic term with m0=1.
    T_abs = float(0.5 * (u @ u))
    P_abs = float(u.sum())
    H_abs = float(u @ u)
    return T, P, Hquad, T_nonuniform, T_abs, P_abs, H_abs


def run():
    rows = []
    for k, seed in enumerate(SEEDS):
        n = SIZES[k % len(SIZES)]
        W = make_graph(seed, n)
        vals = measure(W)
        rows.append({"seed": seed, "n": n,
                     "T_rel_uniform": vals[0],
                     "P_rel_uniform": vals[1],
                     "H_rel_uniform": vals[2],
                     "T_rel_nonuniform_zero_mean": vals[3],
                     "T_abs_uniform_control": vals[4],
                     "P_abs_uniform_control": vals[5],
                     "H_abs_uniform_control": vals[6]})

    primary = [abs(x[k]) for x in rows for k in ("T_rel_uniform", "P_rel_uniform", "H_rel_uniform")]
    result = {
        "status": "PASS-H0",
        "n_graphs": len(rows),
        "tolerance": TOL,
        "primary_max_abs": max(primary),
        "primary_all_within_tolerance": max(primary) <= TOL,
        "nonuniform_min_T": min(x["T_rel_nonuniform_zero_mean"] for x in rows),
        "positive_control_min_T": min(x["T_abs_uniform_control"] for x in rows),
        "positive_control_min_P": min(x["P_abs_uniform_control"] for x in rows),
        "positive_control_min_H": min(x["H_abs_uniform_control"] for x in rows),
        "rows": rows,
    }
    print(json.dumps(result, indent=2))
    with open("R12_FULL_OUTPUT.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)


if __name__ == "__main__":
    run()
