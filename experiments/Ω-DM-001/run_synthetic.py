"""Ω-DM-001 synthetic relational-contribution recovery.

Stdlib-only reference implementation. This generates a controlled toy system,
fits visible-only and relation-aware models, and runs null/permutation controls.
It is not a physical gravity model.
"""
import math
import random

SEED = 20260911
N = 80
TRAIN_N = 56
A_TRUE = 2.0
LAMBDA_TRUE = 0.65
EPS = 0.20
KERNEL_WIDTH = 0.45
NOISE_SIGMA = 0.015


def kernel(dx):
    z = dx / KERNEL_WIDTH
    return math.exp(-0.5 * z * z)


def make_graph(n, rng):
    w = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if abs(i - j) <= 3:
                value = 0.25 + 0.75 * rng.random()
                w[i][j] = value
                w[j][i] = value
    return w


def permute_graph(w, rng):
    """Destroy endpoint topology while preserving edge count and weight multiset."""
    n = len(w)
    weights = [w[i][j] for i in range(n) for j in range(i + 1, n) if w[i][j] > 0]
    all_pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    pairs = rng.sample(all_pairs, len(weights))
    rng.shuffle(weights)
    out = [[0.0] * n for _ in range(n)]
    for (i, j), value in zip(pairs, weights):
        out[i][j] = value
        out[j][i] = value
    return out


def rho_relation(radii, w):
    n = len(radii)
    rho = [0.0] * n
    for i in range(n):
        for j in range(n):
            if i != j and w[i][j] > 0:
                rho[i] += w[i][j] * kernel(radii[i] - radii[j])
    scale = max(rho) or 1.0
    return [x / scale for x in rho]


def basis(r, rho):
    return rho / (r + EPS) ** 2


def generate(radii, rho, rng, lam):
    y = []
    for r, rr in zip(radii, rho):
        value = r * (A_TRUE / (r + EPS) ** 2 + lam * basis(r, rr))
        y.append(value + rng.gauss(0.0, NOISE_SIGMA))
    return y


def fit_a(radii, y, relation=None):
    x0 = [r / (r + EPS) ** 2 for r in radii]
    if relation is None:
        num = sum(a * b for a, b in zip(x0, y))
        den = sum(a * a for a in x0)
        return num / den, None
    x1 = [r * basis(r, rr) for r, rr in zip(radii, relation)]
    s00 = sum(x * x for x in x0)
    s01 = sum(a * b for a, b in zip(x0, x1))
    s11 = sum(x * x for x in x1)
    t0 = sum(a * b for a, b in zip(x0, y))
    t1 = sum(a * b for a, b in zip(x1, y))
    det = s00 * s11 - s01 * s01
    if abs(det) < 1e-14:
        raise ValueError("singular design matrix")
    A = (t0 * s11 - t1 * s01) / det
    lam = (t1 * s00 - t0 * s01) / det
    return A, lam


def rmse(radii, y, relation, A, lam):
    errs = []
    for r, obs, rr in zip(radii, y, relation):
        pred = r * (A / (r + EPS) ** 2 + (0.0 if lam is None else lam * basis(r, rr)))
        errs.append((obs - pred) ** 2)
    return math.sqrt(sum(errs) / len(errs))


def run_once(seed=SEED, lam=LAMBDA_TRUE, use_permuted=False):
    rng = random.Random(seed)
    radii = [0.5 + 0.10 * i for i in range(N)]
    generating_graph = make_graph(N, rng)
    true_rho = rho_relation(radii, generating_graph)
    y = generate(radii, true_rho, rng, lam)

    # The permutation is used only by the fitted model. The observations are
    # always generated from the original topology; otherwise the control is invalid.
    model_rho = true_rho
    if use_permuted:
        model_rho = rho_relation(radii, permute_graph(generating_graph, rng))

    train_r, test_r = radii[:TRAIN_N], radii[TRAIN_N:]
    train_y, test_y = y[:TRAIN_N], y[TRAIN_N:]
    train_rho, test_rho = model_rho[:TRAIN_N], model_rho[TRAIN_N:]
    A0, _ = fit_a(train_r, train_y)
    A1, l1 = fit_a(train_r, train_y, train_rho)
    e0 = rmse(test_r, test_y, test_rho, A0, None)
    e1 = rmse(test_r, test_y, test_rho, A1, l1)
    return A0, A1, l1, e0, e1


def main():
    main_run = run_once()
    null_runs = [run_once(SEED + k, lam=0.0) for k in range(20)]
    perm_runs = [run_once(SEED + 100 + k, lam=LAMBDA_TRUE, use_permuted=True) for k in range(20)]

    print("Ω-DM-001")
    print(f"seed={SEED} N={N} train={TRAIN_N} test={N-TRAIN_N}")
    print(f"truth A={A_TRUE} lambda={LAMBDA_TRUE}")
    print("main A0,A1,lambda1,RMSE0,RMSE1 =", main_run)
    print("null mean RMSE improvement =", sum(x[3] - x[4] for x in null_runs) / len(null_runs))
    print("permutation mean RMSE improvement =", sum(x[3] - x[4] for x in perm_runs) / len(perm_runs))


if __name__ == "__main__":
    main()
