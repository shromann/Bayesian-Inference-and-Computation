---
tags: [priors, checking, week-3]
week: 3
type: concept
---

# Prior Predictive Checking

> [!abstract] One-line summary
> Simulate data implied by your prior *before* seeing the real data. If the implied data look implausible, fix the prior.

## Prior predictive distribution
$$\pi(y)=\int\pi(y\mid\theta)\,\pi(\theta)\,d\theta,$$
the distribution of data $y$ implied by the prior alone. Compare with the [[Bayesian Predictive Distribution|posterior predictive]] $\pi(y\mid x)=\int\pi(y\mid\theta)\pi(\theta\mid x)\,d\theta$.

## Procedure
1. Generate samples from $\pi(y)$ given your choice of $\pi(\theta)$.
2. Check whether $\pi(y)$ represents your beliefs about the data you might observe.
3. If not, modify $\pi(\theta)$ and repeat.

> [!warning] Do not use the upcoming data to inform this decision
> Prior predictive checking must happen before/independently of the analysis data, otherwise it is no longer a prior check.

## Worked example (rare genetic disorder)
$\theta\sim\text{Beta}(\alpha,\beta)$ = probability an individual has a rare disorder; $X\mid\theta\sim\text{Binomial}(n,\theta)$. For a single future individual $y\in\{0,1\}$,
$$\Pr(y=0)\propto\int\theta\,\theta^{\alpha-1}(1-\theta)^{\beta-1}d\theta=B(\alpha+1,\beta),$$
$$\Pr(y=1)\propto\int(1-\theta)\theta^{\alpha-1}(1-\theta)^{\beta-1}d\theta=B(\alpha,\beta+1),$$
with $B(a,b)=\Gamma(a)\Gamma(b)/\Gamma(a+b)$ and $\Pr(y=0)=1-\Pr(y=1)$.

| Prior | Analytic $\Pr(y=0)$ | MC $\Pr(y=0)$ |
|---|---|---|
| $\text{Beta}(1,1)$ | 0.5 | 0.496 |
| $\text{Beta}(1,25)$ | 0.038 | 0.039 |

$\text{Beta}(1,1)$ says a priori a 50–50 chance of a *rare* disorder — implausible. $\text{Beta}(1,25)$ is more realistic.

## Connections
- **Builds on:** [[Prior Distribution]] · [[Bayesian Predictive Distribution]] · [[Monte Carlo Integration]]
- **Leads to:** [[Mixture Priors]] (flexible priors)
- **See also:** [[Beta Distribution]] · [[Binomial Distribution]]

## Source
- [[Lecture Week 3.pdf]], slides 6–8
