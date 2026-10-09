---
tags: [monte-carlo, diagnostics, week-4]
week: 4
type: concept
---

# Effective Sample Size

> [!abstract] One-line summary
> ESS measures how many "equally weighted" samples an importance-sampling run is worth. It is the standard diagnostic for weight degeneracy.

## Definition
$$\text{ESS}=\left[\sum_{i=1}^N (W^{(i)})^2\right]^{-1},$$
where $W^{(i)}=W(x^{(i)})$ are the normalised [[Importance Sampling|importance weights]].

## Range and interpretation
$$1\le\text{ESS}\le N.$$
- $\text{ESS}=1$ when one weight is 1 and the rest are 0 — total **sample depletion**.
- $\text{ESS}=N$ when $W^{(i)}=1/N$ for all $i$ — perfect.
- Loose interpretation: the equivalent number of equally weighted independent samples.

## Using it
> [!tip] Design goal
> To maximise ESS, choose the proposal $g(x)$ to closely match the target $f(x)$. The same idea improves the efficiency of [[Rejection Sampling]] (choose $g$ close to $f$ so $K$ is small).

Example (target $\text{Beta}(2,2)$): proposal $\text{Beta}(1,1)$ gives rejection efficiency 0.681 and ESS 4172.82 (84%); proposal $\text{Beta}(1.5,1.5)$ gives efficiency 0.848 and ESS 4634.02 (93%).

## Connections
- **Builds on:** [[Importance Sampling]]
- **Leads to:** [[Monte Carlo Error]] (precision of weighted estimators) · MCMC diagnostics (later)
- **See also:** [[Rejection Sampling]]

## Source
- [[Lecture Week 4.pdf]], slides 43–44
