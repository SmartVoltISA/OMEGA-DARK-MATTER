import numpy as np, networkx as nx

def k_node(G,u):
    Nu=set(G.neighbors(u)); vals=[]
    for v in Nu:
        vals.append(4-G.degree(u)-G.degree(v)+3*len(Nu & set(G.neighbors(v))))
    return np.mean(vals) if vals else 0.0

def energy(G): return float(np.var([k_node(G,u) for u in G]))

def relax(G,steps=30,tries=100,seed=0):
    G=G.copy(); rng=np.random.default_rng(seed); best=energy(G)
    for _ in range(steps):
        edges=list(G.edges()); accepted=False
        for _ in range(tries):
            e1=edges[rng.integers(len(edges))]; e2=edges[rng.integers(len(edges))]
            a,b=e1; c,d=e2
            if len({a,b,c,d})<4: continue
            new=((a,c),(b,d)) if rng.random()<.5 else ((a,d),(b,c))
            if any(x==y for x,y in new) or any(G.has_edge(*e) for e in new): continue
            G.remove_edges_from([e1,e2]); G.add_edges_from(new); s=energy(G)
            if s<best-1e-12: best=s; accepted=True; break
            G.remove_edges_from(new); G.add_edges_from([e1,e2])
        if not accepted: break
    return G,best

def dim(G,seed):
    vals=[]; rng=np.random.default_rng(seed)
    for s in rng.choice(list(G),6,replace=False):
        d=nx.single_source_shortest_path_length(G,int(s)); c=np.bincount(list(d.values())); r=np.arange(len(c)); m=(r>=1)&(r<=min(8,len(c)-1))&(c>0)
        if m.sum()>=4: vals.append(float(np.polyfit(np.log(r[m]),np.log(c[m]),1)[0]))
    return float(np.mean(vals)),float(np.std(vals,ddof=1)) if len(vals)>1 else 0.0

rows=[]
for kind in ['regular','smallworld']:
    for seed in range(6):
        G=nx.random_regular_graph(6,120,seed=seed) if kind=='regular' else nx.connected_watts_strogatz_graph(120,6,.15,seed=seed)
        G,E=relax(G,seed=seed); p,sd=dim(G,1000+seed); rows.append((kind,seed,p,sd,E,nx.diameter(G)))
        print(rows[-1])
