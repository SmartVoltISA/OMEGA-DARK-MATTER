# Ω-DM-009 — Relational Source vs Inertial Scale

Date: 2026-09-11
Status: PREREGISTERED BEFORE CERTIFICATION RERUN

Question: can one relational property generate two independently measured quantities: source strength of a 3D field and resistance to a standardized internal deformation?

For each of 24 random internal weighted graphs (5–12 nodes), construct Laplacian L from symmetric edge weights in [0.2,1].

Source measurement: C = trace(L). Measure far-field flux using phi(r)=-C/(4*pi*r), with r={3,4,5,6,8,10}; infer q from flux/(4*pi*r^2). No mass parameter is supplied.

Inertial measurement: use standardized differential forcing f=(1,-1,0,...) and compute compliance c=f^T pinv(L+1e-9 I)f. Define m_rel=n/c. This is an operational relational inertia proxy, not physical mass.

Primary tests:
1. correlation log(q) vs log(m_rel);
2. power-law exponent p in q=a*m_rel^p;
3. coefficient of variation of q/m_rel.

Controls:
- shuffled q/m_rel pairings, preserving marginals;
- report graph size and spectral gap as possible confounders;
- node relabeling must leave results invariant.

Acceptance requires strong positive cross-object correlation, exponent near 1, low ratio dispersion, and destruction of correlation under shuffled pairing. This does NOT establish equivalence of gravitational and inertial mass.

Critical limitation: C is explicitly defined as trace(L), so source strength is not emergent from an unknown physical law. The test asks whether two different operational measurements of relational structure track one another.

Certification rule: protocol must remain unchanged during certification rerun. Any correction affecting estimator, generator, seeds, metrics, or acceptance requires a new protocol commit.
