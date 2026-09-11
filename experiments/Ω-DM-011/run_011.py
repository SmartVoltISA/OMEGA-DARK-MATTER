import json
import numpy as np

START = 20260911
SEEDS = range(START, START + 40)
N = 20
P = 0.15
EPS = 1e-3
ALPHA = 1.0


def make_graph(seed, scale=1.0):
    rng = np.random.default_rng(seed)
    for _ in range(1000):
        W = np.zeros((N, N), dtype=float)
        for i in range(N):
            for j in range(i + 1, N):
                if rng.random() < P:
                    w = rng.uniform(0.2, 1.0)
                    W[i, j] = W[j, i] = w * scale
        # deterministic connectivity check
        seen = {0}
        stack = [0]
        while stack:
            i = stack.pop()
            for j in np.flatnonzero(W[i] > 0):
                j = int(j)
                if j not in seen:
                    seen.add(j)
                    stack.append(j)
        if len(seen) == N:
            return W
    raise RuntimeError("failed to generate connected graph")


def measure(W):
    d = W.sum(axis=1)
    Mdiag = 1.0 + ALPHA * d
    probe = np.argsort(-d, kind="stable")[:2]
    L = np.diag(d) - W

    # Independent source-channel measurement.
    s = np.zeros(N)
    s[probe] = 0.5
    phi = np.linalg.solve(L + EPS * np.eye(N), s)

    rest = np.ones(N, dtype=bool)
    rest[probe] = False
    flux = 0.0
    for i in probe:
        for j in np.flatnonzero(rest):
            flux += W[i, j] * (phi[i] - phi[j])

    m_eff = float(Mdiag[probe].sum())
    q_eff = float(abs(flux))
    return m_eff, q_eff, [int(x) for x in probe]


def corr(a, b):
    return float(np.corrcoef(np.log(a), np.log(b))[0, 1])


def run():
    rows = []
    for seed in SEEDS:
        W = make_graph(seed)
        m, q, probe = measure(W)
        rows.append({"seed": seed, "m_eff": m, "q_eff": q, "ratio": q / m, "probe": probe})

    m = np.array([r["m_eff"] for r in rows])
    q = np.array([r["q_eff"] for r in rows])
    ratio = q / m
    primary_corr = corr(m, q)
    primary_cv = float(ratio.std(ddof=1) / ratio.mean())

    rng = np.random.default_rng(11011)
    perm = rng.permutation(len(rows))
    shuffled_corr = corr(m, q[perm])

    rescale = {}
    for c in (0.5, 2.0):
        rr = []
        for seed in SEEDS:
            W = make_graph(seed, scale=c)
            mm, qq, _ = measure(W)
            rr.append(qq / mm)
        rr = np.array(rr)
        rescale[str(c)] = {
            "mean_ratio": float(rr.mean()),
            "median_ratio": float(np.median(rr)),
            "median_relative_change_vs_primary": float(np.median(rr) / np.median(ratio) - 1.0),
            "cv": float(rr.std(ddof=1) / rr.mean()),
        }

    result = {
        "status": "FAIL",
        "n": len(rows),
        "primary": {
            "log_correlation": primary_corr,
            "ratio_mean": float(ratio.mean()),
            "ratio_median": float(np.median(ratio)),
            "ratio_cv": primary_cv,
            "h1_pass": bool(primary_corr >= 0.95 and primary_cv <= 0.10),
        },
        "shuffled_control": {
            "log_correlation": shuffled_corr,
            "fails_h1": bool(shuffled_corr < 0.95),
        },
        "weight_rescaling": rescale,
        "rows": rows,
    }
    print(json.dumps(result, indent=2))
    with open("R11_FULL_OUTPUT.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)


if __name__ == "__main__":
    run()
