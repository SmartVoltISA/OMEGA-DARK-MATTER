"""Ω-DM-030 coordinate-free relational growth audit."""
import numpy as np
import networkx as nx


def shell_exponent(G, source=0, rmin=2, rmax=8):
    d = nx.single_source_shortest_path_length(G, source)
    c = np.bincount(list(d.values()))
    r = np.arange(len(c))
    mask = (r >= rmin) & (r <= min(rmax, len(c)-1)) & (c > 0)
    p = np.polyfit(np.log(r[mask]), np.log(c[mask]), 1)[0]
    return float(p), c


def triadic(seed, n=1500):
    rng = np.random.default_rng(seed)
    G = nx.Graph(); G.add_node(0)
    for i in range(1, n):
        if i < 3:
            targets = list(range(i))
        else:
            deg = np.array([G.degree(j)+1 for j in range(i)], float)
            targets = rng.choice(i, 3, replace=False, p=deg/deg.sum())
        G.add_edges_from((i, int(j)) for j in targets)
        if len(targets) >= 2 and rng.random() < 0.7:
            G.add_edge(int(targets[0]), int(targets[1]))
    return G


def run():
    rows=[]
    for kind in ("triadic", "regular", "ba"):
        vals=[]
        for seed in range(6):
            if kind == "triadic": G=triadic(seed)
            elif kind == "regular": G=nx.random_regular_graph(6, 1500, seed=seed)
            else: G=nx.barabasi_albert_graph(1500, 3, seed=seed)
            p,_=shell_exponent(G)
            vals.append(p); rows.append((kind,seed,p))
        print(kind, vals, float(np.mean(vals)), float(np.std(vals,ddof=1)))
    return rows

if __name__ == "__main__": run()
