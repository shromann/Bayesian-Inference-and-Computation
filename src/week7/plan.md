# Week 7 — Bayesian Inference and Computation (animated explainer)

## Overview
- **Topic**: MCMC beyond Gibbs (Metropolis–Hastings), DAGs / conditional independence, rJAGS, and the Week 7 tutorial problems.
- **Hook**: Gibbs needs exact full conditionals — what if those are impossible to sample from?
- **Aha moment**: MH corrects an arbitrary proposal with a min(1, ratio) acceptance rule so the chain balances to π; a DAG turns the same balance idea into a local update recipe.
- **Sources**: `lectures/Lecture Week 7.pdf` (46 slides), `tutorial/Tutorial Week 7.pdf` (3 pages, 5 problems).
- **Target audience**: Students who have seen Weeks 1–4 (Gibbs, Monte Carlo, conjugate models, regression).
- **Length**: ~18 scenes, 20–50 s each (~10 min total) at 854×480 / 15 fps draft.
- **Style**: 3B1B-inspired; geometry before algebra; subtitled; paced with explicit waits.

## Palette & type
- Background `#1C1C1C`, primary `#58C4DD`, secondary `#83C167`, accent `#FFFF00`, muted `#888888`, danger `#FF6B6B`.
- Monospace Menlo; title 48, heading 36, body 30, label 24, caption 20.
- Opacity layers: primary 1.0, context 0.4, structure 0.15.

## Arc
Problem–Solution for MH (Scenes 1–11), Build-Up for DAGs/JAGS (12–16), then worked tutorial walkthroughs (17–21).

## Scene list

| # | Class | Topic | Key visual |
|---|-------|-------|------------|
| 1 | S01_Roadmap | Week 7 map | Three chapters appear in sequence |
| 2 | S02_GibbsRecap | Gibbs sweep on bivariate normal | Axes, zig-zag conditional moves, trace plots |
| 3 | S03_WhyMH | When conditionals fail | Inversion/rejection/importance checklist |
| 4 | S04_MHLoop | MH algorithm | Proposal arrow, accept/reject split |
| 5 | S05_RandomWalkDemo | Random walk chain from θ₀=(10,0) | 2D target ellipses + walk + trace |
| 6 | S06_DetailedBalance | Reversibility | Two-state flow arrows equalised |
| 7 | S07_DeriveAlpha | Deriving min(1,ratio) | Asymmetric flows, boost back-move |
| 8 | S08_VerifyBalance | Reversibility proof | min(a,b) = min(b,a) |
| 9 | S09_GibbsIsMH | Gibbs as special case | q = full conditional ⇒ α = 1 |
| 10 | S10_Proposals | RW / independence / single-site | Three proposal diagrams |
| 11 | S11_Tuning | Acceptance-rate sweet spot | Three trace plots: 4%, 46%, 92% |
| 12 | S12_DAGBasics | DAG → joint factorisation | Three 3-node DAGs with π(V) products |
| 13 | S13_CI | Independence vs conditional independence | Genotype family example |
| 14 | S14_Moralise | Marrying parents, global Markov | DAG → CI graph, D ⫫ (A,E,F) | (B,C) |
| 15 | S15_Dugongs | Dugong growth model | Full DAG + posterior factorisation |
| 16 | S16_JAGS | rJAGS workflow & diagnostics | data/model/inits → samples → 4 diagnostic panels |
| 17 | S17_Tut1 | Bivariate normal Gibbs recursion | θ₂ trace + ρ^t convergence envelope |
| 18 | S18_Tut2 | Mixture Beta prior | Two Beta components + posterior update |
| 19 | S19_Tut3 | Poisson–Gamma sales | Prior/posterior curves + 95% HPD |
| 20 | S20_Tut4 | Rice packets P(μ<495) | Normal–Gamma hierarchy + t tail |
| 21 | S21_Tut5 | Regression full conditionals | Blocked β vs single-coordinate splits |

## Numerical facts verified for the tutorial scenes
- Q1: θ₂⁽ᵗ⁾ = ρ^{2t}θ₂⁽⁰⁾ + Σ_{i=0}^{2t−1} ρ^i ε_i, E = ρ^{2t}θ₂⁰, Var = 1 − ρ^{4t}.
- Q2: π(θ) = ½Beta(2,4) + ½Beta(1,1); prior mean 5/12 ≈ 0.4167, sd ≈ 0.2539; posterior weights 20B(6,10) : B(5,7) = 20/33 : 13/33; posterior mean ≈ 0.3914.
- Q3: a=4, b=0.25 (mean 16, sd 8); Σy=400; posterior Gamma(404, 20.25); mean 19.95; 95% HPD ≈ [18.03, 21.90].
- Q4: ȳ=492.85, Σ(y−ȳ)²=444.55; posterior μ|τ ~ N(492.852, [22.005τ]⁻¹); τ|y ~ Gamma(12, 9 + 222.275 + 0.128) ≈ Gamma(12, 231.40); P(μ<495) ≈ 0.981.
- Q5: β|φ ~ N₂(β̂, φ⁻¹(XᵀX)⁻¹), φ|β ~ Gamma(n₁/2, Sβ/2), plus the two scalar full conditionals.

## Render plan
1. `manim -ql script.py S01_... S02_... ...` (draft).
2. Preview stills with `-ql --format=png -s <Scene>`.
3. Stitch with ffmpeg concat into `final.mp4`.
4. Upgrade to `-qm`/`-qh` only after draft review passes.
