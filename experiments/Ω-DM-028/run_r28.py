"""Ω-DM-028: isolate the geometric shell-measure condition."""
import numpy as np


def fit_p(r, G):
    return -np.polyfit(np.log(r), np.log(G), 1)[0]


def run():
    r = np.arange(2.0, 21.0)
    Q = 1.0
    rows = []
    for s in (-0.2, 0.0, 0.2):
        S = r ** (2.0 + s)
        G = Q / S
        p = fit_p(r, G)
        rows.append((s, p, p - (2.0 + s)))
    return rows


if __name__ == "__main__":
    for s, p, err in run():
        print(f"s={s:+.1f}  p={p:.12f}  error={err:.3e}")
