---
tags: [bayesian, inference, week-1]
week: 1
type: concept
---

# Credible Intervals

> [!abstract] One-line summary
> A credible interval is a Bayesian interval estimate with the interpretation people intuitively want: "there is a 95% probability $\theta$ lies in this interval."

## The interpretation
> [!success] Bayesian (θ is random)
> "There is a 95% probability that $\theta$ is in your (single) credible interval." Very intuitive and simple.

Compare with [[Confidence Intervals]], where the same numbers must be interpreted as long-run coverage.

## How to find a 95% interval
Solve for $[a,b]$ such that
$$\int_0^a\pi(\theta\mid x)\,d\theta=0.025,\qquad \int_0^b\pi(\theta\mid x)\,d\theta=0.975.$$
For the [[Water Consumption Example]] (a Gamma posterior), $E_\pi[\theta]$, $\text{Var}(\theta)$ and $[a,b]$ all come from the posterior directly.

## Credible intervals are not unique
There are infinitely many intervals with 95% coverage, all with the same interpretation. The choice is yours. Two common choices:
- **Equal-tailed interval** — chop 2.5% off each tail.
- **High Density Region (HDR)** — the interval with the *shortest width* (smallest area).

## High Density Regions (HDR)
- Shortest-width credible interval.
- Not always the central interval: if the posterior is skewed, the HDR shifts.
- Can comprise **disjoint regions** for multimodal posteriors (see [[Mixture Priors]]).

For a symmetric posterior (e.g. the normal) the equal-tailed and HDR intervals coincide, and the mean/median/mode all agree.

## Connections
- **Builds on:** [[Posterior Distribution]] · [[Posterior Inference]]
- **Leads to:** [[Posterior Decision Theory]] (intervals as decisions) · [[Monte Carlo Integration]] (computing quantiles from samples)
- **See also:** [[Confidence Intervals]] · [[Loss Functions]]

## Source
- [[Lecture Week 1.pdf]], slides 26–27
- [[Tutorial Week 4.pdf]], Q2 (HDR calculation)
