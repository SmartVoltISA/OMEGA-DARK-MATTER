#!/usr/bin/env python3
"""Ω-DUAL-001: minimal two-node information-routing benchmark.
Run: python3 experiments/omega_dual_exp001.py
Standard library + NumPy required. Writes JSON beside this script's results folder.
"""
import json
import math
from pathlib import Path
import numpy as np

SEED = 20261010
N = 100_000
SPLIT = N // 2
NOISE_LEVELS = [0.00, 0.05, 0.10, 0.20, 0.30]
DELIVERY_RELIABILITY = [0.00, 0.25, 0.50, 0.75, 1.00]


def wilson(k, n, z=1.959963984540054):
    ph = k / n
    den = 1 + z*z/n
    center = (ph + z*z/(2*n)) / den
    half = z * math.sqrt(ph*(1-ph)/n + z*z/(4*n*n)) / den
    return [center-half, center+half]


def score(pred, target):
    correct = int(np.sum(pred[SPLIT:] == target[SPLIT:]))
    n = N - SPLIT
    return {"accuracy": correct/n, "correct": correct, "n_test": n,
            "wilson95": wilson(correct, n)}


def main():
    rng = np.random.default_rng(SEED)
    a = rng.integers(0, 2, N, dtype=np.int8)
    b = rng.integers(0, 2, N, dtype=np.int8)
    y = np.bitwise_xor(a, b)
    noise_rows = []

    for p in NOISE_LEVELS:
        flip_a = rng.random(N) < p
        flip_b = rng.random(N) < p
        obs_a = np.bitwise_xor(a, flip_a.astype(np.int8))
        obs_b = np.bitwise_xor(b, flip_b.astype(np.int8))
        coupled = np.bitwise_xor(obs_a, obs_b)
        shuffled_partner = rng.permutation(obs_b)
        shuffled = np.bitwise_xor(obs_a, shuffled_partner)
        # Identical nodes receive the same A-side observation; XOR duplicates to 0.
        identical = np.bitwise_xor(obs_a, obs_a)
        uncoupled_coin = rng.integers(0, 2, N, dtype=np.int8)
        noise_rows.append({
            "observation_noise_p": p,
            "conditions": {
                "coupled": score(coupled, y),
                "shuffled_message": score(shuffled, y),
                "identical_nodes": score(identical, y),
                "uncoupled_chance": score(uncoupled_coin, y),
            },
        })

    # Paired reliability sweep at observation noise p=0.10.
    p = 0.10
    flip_a = rng.random(N) < p
    flip_b = rng.random(N) < p
    obs_a = np.bitwise_xor(a, flip_a.astype(np.int8))
    obs_b = np.bitwise_xor(b, flip_b.astype(np.int8))
    reliability_rows = []
    for q in DELIVERY_RELIABILITY:
        transmission_flip = rng.random(N) > q
        received_b = np.bitwise_xor(obs_b, transmission_flip.astype(np.int8))
        pred = np.bitwise_xor(obs_a, received_b)
        reliability_rows.append({
            "delivery_reliability_q": q,
            **score(pred, y),
        })

    result = {
        "experiment": "OMEGA-DUAL-001",
        "status": "EXECUTED_LOCALLY",
        "date": "2026-10-10",
        "seed": SEED,
        "n_examples_per_noise": N,
        "train_test_split": "first 50% train, last 50% test; no fitted parameters",
        "primary_metric": "held-out accuracy",
        "noise_sweep": noise_rows,
        "coupling_reliability_sweep_at_p_0_1": reliability_rows,
        "note": "Constructed synthetic XOR information-routing task; not evidence for universal duality or physical ontology.",
    }
    out = Path(__file__).resolve().parents[1] / "results" / "OMEGA-DUAL-001_RESULTS_2026-10-10.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
