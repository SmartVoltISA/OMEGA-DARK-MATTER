"""Ω-23 continuous signed-relation margin experiment. Requires NumPy.
Preregistered in EXPERIMENTS/2026-10-09-relational-fabric-omega23-preregistration.md.
"""
import json
import numpy as np

N, J = 160, 0.85
SEEDS = range(20262300, 20262340)
MODES = ("adaptive_live", "frozen_learned", "permuted_learned", "fixed_original", "no_coupling")

def make_graph(seed):
    rng = np.random.default_rng(seed)
    edges = set()
    for i in range(N):
        for d in (1, 2):
            edges.add(tuple(sorted((i, (i+d) % N))))
    for i in range(N):
        for d in (1, 2):
            old = tuple(sorted((i, (i+d) % N)))
            if old in edges and rng.random() < .03:
                edges.remove(old)
                candidates = [j for j in range(N) if j != i and tuple(sorted((i, j))) not in edges]
                if candidates:
                    edges.add(tuple(sorted((i, int(rng.choice(candidates))))))
    return np.asarray(sorted(edges), dtype=int)

def field(x, edges, weights, signs):
    a, b = edges[:, 0], edges[:, 1]
    sums, den = np.zeros(N), np.zeros(N)
    np.add.at(sums, a, weights*signs*x[b]); np.add.at(sums, b, weights*signs*x[a])
    np.add.at(den, a, weights); np.add.at(den, b, weights)
    return np.divide(sums, den, out=np.zeros_like(sums), where=den > 0)

def evolve(x, edges, weights, signs, steps, adapt=False, target=None):
    x, weights = x.copy(), weights.copy()
    a, b = edges[:, 0], edges[:, 1]
    for _ in range(steps):
        xn = np.tanh(.35*x + J*field(x, edges, weights, signs))
        if adapt:
            compat = x[a]*x[b]*signs
            weights = np.clip(weights + .025*(compat-.15*weights) - .008*(weights-1), .1, 1.3)
            if target is not None:
                weights = np.clip(weights*(target/weights.mean()), .1, 1.3)
        x = xn
    return x, weights

def metrics(x, edges, signs):
    a, b = edges[:, 0], edges[:, 1]
    p = signs*x[a]*x[b]
    margin = float(np.mean(p))
    activity = float(np.mean(np.abs(x[a]*x[b])))
    return {"M": margin, "A": activity, "Q": float(margin/(activity+1e-12)),
            "rms": float(np.sqrt(np.mean(x*x)))}

def state_recovery(x0, x1):
    denom = np.sqrt(np.mean(x0*x0))
    return None if denom < 1e-10 else float(1-np.sqrt(np.mean((x1-x0)**2))/(2*denom))

def main():
    runs = []
    for seed in SEEDS:
        rng = np.random.default_rng(seed); edges = make_graph(seed)
        x0 = rng.normal(0, .15, N); w0 = rng.uniform(.7, 1.3, len(edges))
        signs = np.where(rng.random(len(edges)) < .5, 1., -1.)
        xcommon, wlearn = evolve(x0, edges, w0, signs, 100, True, float(w0.mean()))
        wlearn = np.clip(wlearn*(w0.mean()/wlearn.mean()), .1, 1.3)
        xpert = xcommon.copy(); xpert[:int(.1*N)] *= -1
        wperm = np.random.default_rng(seed+700000).permutation(wlearn)
        for mode in MODES:
            if mode == "adaptive_live":
                xpost, _ = evolve(xpert, edges, wlearn, signs, 100, True, float(w0.mean()))
            elif mode == "frozen_learned":
                xpost, _ = evolve(xpert, edges, wlearn, signs, 100)
            elif mode == "permuted_learned":
                xpost, _ = evolve(xpert, edges, wperm, signs, 100)
            elif mode == "fixed_original":
                xpost, _ = evolve(xpert, edges, w0, signs, 100)
            else:
                xpost = xpert.copy()
                for _ in range(100): xpost = np.tanh(.35*xpost)
            pre, post = metrics(xcommon, edges, signs), metrics(xpost, edges, signs)
            runs.append({"seed": int(seed), "mode": mode, "pre_M": pre["M"], "post_M": post["M"],
                "delta_M": post["M"]-pre["M"], "pre_A": pre["A"], "post_A": post["A"],
                "pre_Q": pre["Q"], "post_Q": post["Q"], "pre_rms": pre["rms"], "post_rms": post["rms"],
                "state_recovery": state_recovery(xcommon, xpost)})
    summary = {}
    for mode in MODES:
        rr = [r for r in runs if r["mode"] == mode]; summary[mode] = {}
        for key in ("pre_M","post_M","delta_M","pre_A","post_A","pre_Q","post_Q","pre_rms","post_rms","state_recovery"):
            vals = np.array([r[key] for r in rr if r[key] is not None], float)
            summary[mode][key] = {"n": int(len(vals)), "mean": float(vals.mean()) if len(vals) else None,
                                  "sd": float(vals.std(ddof=1)) if len(vals)>1 else None}
    rng = np.random.default_rng(20262399); paired = {}
    for control in ("permuted_learned", "fixed_original"):
        paired[control] = {}
        for key in ("post_M","delta_M","post_A","post_Q","state_recovery"):
            d = np.array([next(r[key] for r in runs if r["seed"]==s and r["mode"]=="frozen_learned") -
                          next(r[key] for r in runs if r["seed"]==s and r["mode"]==control) for s in SEEDS])
            boot = d[rng.integers(0, len(d), size=(10000, len(d)))].mean(axis=1)
            paired[control][key] = {"n": len(d), "mean_difference": float(d.mean()),
                "positive": int((d>0).sum()), "negative": int((d<0).sum()),
                "ci95": [float(np.quantile(boot,.025)), float(np.quantile(boot,.975))]}
    print(json.dumps({"experiment":"Ω-23 continuous signed-relation margin",
        "execution":"Run locally with python experiments/relational_fabric_omega23_continuous_margin.py > results/2026-10-09-relational-fabric-omega23.json",
        "protocol":{"n_seeds":40,"nodes":N,"J":J,"train_steps":100,"post_perturbation_steps":100,
            "primary_metric":"M=mean(s_e*x_i*x_j) over all edges","activity":"A=mean(abs(x_i*x_j))",
            "normalized":"Q=M/(A+1e-12)","signs_fixed_across_modes":True,
            "common_snapshot":True,"bootstrap_resamples":10000,"bootstrap_seed":20262399},
        "summary":summary,"paired":paired,"runs":runs}, indent=2))

if __name__ == "__main__":
    main()
