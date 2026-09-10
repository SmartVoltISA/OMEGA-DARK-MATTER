"""Ω-DM-002 reference implementation skeleton.

Purpose: reconstruct a sparse hidden symmetric relation matrix from synthetic
state-transition trajectories without exposing the generating topology.

Stdlib only. This file intentionally emits machine-readable JSON so an
independent runner can archive exact results and rerun the protocol.
"""
from __future__ import annotations
import json, math, random, hashlib


def matrix_hash(W):
    raw = json.dumps(W, separators=(",", ":"), sort_keys=True).encode()
    return hashlib.sha256(raw).hexdigest()


def generate_graph(n, p, seed):
    rng = random.Random(seed)
    W = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if rng.random() < p:
                w = 0.2 + 0.8 * rng.random()
                W[i][j] = W[j][i] = w
    return W


def step(x, v, W, k, gamma, sigma, rng):
    n = len(x)
    a = [0.0] * n
    for i in range(n):
        coupling = 0.0
        for j in range(n):
            coupling += W[i][j] * (x[i] - x[j])
        a[i] = -k * coupling - gamma * v[i]
    x2 = [x[i] + v[i] for i in range(n)]
    v2 = [v[i] + a[i] + rng.gauss(0.0, sigma) for i in range(n)]
    return x2, v2


def generate_trajectory(W, length, k, gamma, sigma, seed):
    rng = random.Random(seed)
    n = len(W)
    x = [rng.uniform(-1.0, 1.0) for _ in range(n)]
    v = [rng.uniform(-0.2, 0.2) for _ in range(n)]
    out = [x[:]]
    for _ in range(length - 1):
        x, v = step(x, v, W, k, gamma, sigma, rng)
        out.append(x[:])
    return out


def mse(a, b):
    s = 0.0; c = 0
    for xa, xb in zip(a, b):
        for va, vb in zip(xa, xb):
            d = va - vb
            s += d * d; c += 1
    return s / max(c, 1)


def edge_list(W):
    n = len(W)
    return [(i, j, W[i][j]) for i in range(n) for j in range(i + 1, n) if W[i][j] > 0]


def fit_lambda_on_basis(trajs, basis, k, gamma):
    """Fit only a scalar coupling multiplier for a supplied candidate basis.

    This helper is deliberately not the full Ω-DM-002 inference procedure.
    It is an auditable scoring primitive; topology reconstruction must be
    implemented separately and frozen before test evaluation.
    """
    # Baseline prediction has no coupling. Candidate prediction uses basis.
    num = 0.0; den = 0.0
    for tr in trajs:
        for t in range(len(tr) - 1):
            x = tr[t]
            target = tr[t + 1]
            for i in range(len(x)):
                base = x[i]  # deliberately simple reference baseline
                q = 0.0
                for j in range(len(x)):
                    q += basis[i][j] * (x[i] - x[j])
                z = target[i] - base
                num += q * (-z)
                den += q * q
    return num / den if den else 0.0


def main():
    # These are protocol defaults, not accepted results.
    cfg = dict(seed=20260911, n=24, edge_probability=0.12,
               trajectories_train=40, trajectories_test=20,
               length=80, k=0.05, gamma=0.02, noise_sigma=0.005)
    W = generate_graph(cfg["n"], cfg["edge_probability"], cfg["seed"])
    train = [generate_trajectory(W, cfg["length"], cfg["k"], cfg["gamma"],
                                 cfg["noise_sigma"], cfg["seed"] + 1000 + i)
             for i in range(cfg["trajectories_train"])]
    test = [generate_trajectory(W, cfg["length"], cfg["k"], cfg["gamma"],
                                cfg["noise_sigma"], cfg["seed"] + 2000 + i)
            for i in range(cfg["trajectories_test"])]
    result = {"status": "REFERENCE_RUN_ONLY", "config": cfg,
              "true_W_sha256": matrix_hash(W),
              "edge_count": len(edge_list(W)),
              "note": "Topology reconstruction and acceptance criteria are specified in PROTOCOL.md; numerical PASS/FAIL must not be inferred from this skeleton."}
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
