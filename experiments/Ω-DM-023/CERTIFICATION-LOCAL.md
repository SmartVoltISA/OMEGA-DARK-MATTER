# Ω-DM-023 — Local certification note

The repository runner was independently recreated and executed locally at reduced lattice size `N=17` because the full GitHub-hosted environment was not available for local network access and the initial N=25 sparse run exceeded the local execution budget.

Balanced directed model, seeds 0..5:
`p = 1.911600006, 1.995784542, 1.950486505, 1.958633352, 2.115145144, 2.060334376`
Mean `p = 1.9986640`.

Leaky control `mu=0.03`:
`p = 3.220753503, 3.349549048, 3.242650775, 3.302428337, 3.393072447, 3.362420879`
Mean `p = 3.3118121`.

Source scaling (balanced, seed 0): amplitudes `0.5, 1, 2` produced mean shell flux `0.432820855, 0.865641709, 1.731283418`, i.e. linear scaling.

This is an execution record, not a substitute for a future full-size certification run. The reduced-size run supports the model-level H1 but finite-size effects remain a stated limitation.
