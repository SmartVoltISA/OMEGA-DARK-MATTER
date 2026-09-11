"""Ω-DM-032 runner: coordinate-free curvature-neutral rewiring."""
import numpy as np
import networkx as nx


def make_graph(n, seed, kind):
    rng=np.random.default_rng(seed)
    if kind=='er':
        while True:
            G=nx.gnp_random_graph(n,0.045,seed=int(rng.integers(1<<30)))
            if nx.is_connected(G): return G
    if kind=='regular':
        return nx.random_regular_graph(6,n,seed=int(rng.integers(1<<30)))
    G=nx.watts_strogatz_graph(n,6,0.15,seed=int(rng.integers(1<<30)))
    return G if nx.is_connected(G) else nx.connected_watts_strogatz_graph(n,6,0.15,seed=int(rng.integers(1<<30)))


def curvature_data(G):
    deg=dict(G.degree()); K={}; total=0.0
    for u,v in G.edges():
        t=len(set(G.neighbors(u)) & set(G.neighbors(v)))
        k=4-deg[u]-deg[v]+3*t
        K[(u,v)]=k; total+=k*k
    return K,total/max(1,G.number_of_edges())


def energy(G): return curvature_data(G)[1]


def relax(G, steps=60):
    G=G.copy(); n=len(G)
    for _ in range(steps):
        base=energy(G); best=None; bestE=base
        nodes=list(G.nodes()); candidates=[]
        for u in nodes:
            d=nx.single_source_shortest_path_length(G,u,cutoff=2)
            for v in d:
                if u<v and u!=v and not G.has_edge(u,v): candidates.append((u,v))
        candidates=sorted(candidates); edges=list(G.edges())
        for u,v in candidates[::max(1,len(candidates)//180)][:180]:
            if G.degree(u)>=10 or G.degree(v)>=10: continue
            for a,b in edges[::max(1,len(edges)//120)][:120]:
                if len({u,v,a,b})<4: continue
                if G.degree(a)<=3 or G.degree(b)<=3: continue
                if G.degree(a)-1<3 or G.degree(b)-1<3: continue
                H=G.copy(); H.remove_edge(a,b); H.add_edge(u,v)
                if nx.is_connected(H) and max(dict(H.degree()).values())<=10 and min(dict(H.degree()).values())>=3:
                    e=energy(H)
                    if e < bestE-1e-12: bestE=e; best=H
        if best is None: break
        G=best
    return G


def shell_dimension(G,sources):
    vals=[]; rss=[]
    for s in sources:
        d=nx.single_source_shortest_path_length(G,s); c=np.bincount(list(d.values())); r=np.arange(len(c))
        mask=(r>=2)&(r<=len(c)-2)&(c>0)
        if mask.sum()<4: continue
        x=np.log(r[mask]); y=np.log(c[mask]); coef=np.polyfit(x,y,1); pred=np.polyval(coef,x)
        vals.append(float(coef[0])); rss.append(float(np.mean((y-pred)**2)))
    if not vals: return float('nan'),float('nan'),float('nan')
    return float(np.mean(vals)),float(np.std(vals,ddof=1) if len(vals)>1 else 0.0),float(np.mean(rss))


def run():
    rows=[]
    for kind in ['er','regular','smallworld']:
        for seed in range(6):
            G=relax(make_graph(500,seed,kind))
            rng=np.random.default_rng(10000+seed); src=rng.choice(list(G.nodes()),8,replace=False)
            p,sd,rss=shell_dimension(G,src); K,Ek=curvature_data(G)
            rows.append((kind,seed,p,sd,rss,G.number_of_edges(),float(np.mean([d for _,d in G.degree()])),float(np.std([d for _,d in G.degree()])),Ek,nx.diameter(G)))
            print(rows[-1])
    return rows

if __name__=='__main__': run()
