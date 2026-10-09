---
tags: [bayesian, computation, week-2]
week: 2
type: concept
---

# Normalising Constant

> [!abstract] One-line summary
> The normalising constant $m(x)=\int L(x\mid\theta)\pi(\theta)\,d\theta$ turns an unnormalised posterior into a proper density — and computing it is often the hardest part of Bayesian inference.

## Definition
$$m(x)=\int_\Theta L(x\mid\theta)\pi(\theta)\,d\theta.$$
It appears in the denominator of [[Bayes Theorem]]:
$$\pi(\theta\mid x)=\frac{L(x\mid\theta)\pi(\theta)}{m(x)}.$$

## Why it is a problem
Even simple priors can make $m(x)$ intractable. Example: $x_1,\dots,x_n\sim\text{Poisson}(\theta)$ with the "truncated uniform" prior $\pi(\theta)=1$ for $0<\theta\le1$. Then
$$m(x)=\int_0^1 \exp(-n\theta)\,\theta^{\sum x_i}\,d\theta,$$
which can only be evaluated numerically. The issue is magnified as $\dim(\theta)$ grows.

## Why we can often ignore it
Many algorithms only need the posterior *up to proportionality*:
- [[Conjugate Priors]] — the constant cancels into a recognisable family.
- [[Rejection Sampling]] and [[Importance Sampling]] — ratios $f/g$ cancel constants.
- [[Monte Carlo Integration]] — expectations normalise automatically.

> [!note] Also called
> In model comparison the normalising constant $m(x)$ is the **marginal likelihood** or **evidence** — central to Bayes factors (later weeks).

## Connections
- **Builds on:** [[Bayes Theorem]] · [[Likelihood Function]]
- **Leads to:** [[Conjugate Priors]] · [[Monte Carlo Integration]] · [[Importance Sampling]]
- **See also:** [[Posterior Distribution]]

## Source
- [[Lecture Week 2.pdf]], slide 5
