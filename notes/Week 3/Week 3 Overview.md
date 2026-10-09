---
tags: [moc, week-3]
week: 3
type: map-of-content
---

# Week 3 Overview — Multivariate Models & Rejection Sampling

> [!abstract] Theme
> Real problems have many parameters. We scale the Bayesian machinery to multivariate $\theta$ ([[Multivariate Bayesian Models]]), learn how to choose flexible priors ([[Mixture Priors]], [[Prior Predictive Checking]]), and add a second sampler ([[Rejection Sampling]]).

## Learning objectives
By the end you should be able to:
- Build and normalise a joint posterior and derive marginals by integration.
- Handle the [[Normal Model with Unknown Mean and Variance]] and recognise [[Inverse Gamma Distribution|Inverse Gamma]] and [[Wishart Distribution|Wishart]] conjugacy.
- Construct flexible [[Mixture Priors]] and validate them with [[Prior Predictive Checking]].
- Implement [[Rejection Sampling]] and choose the bounding constant $K$.

## Path through the material

### 1. More flexible priors
- [[Mixture Priors]] — combine conjugates; the posterior is a mixture with updated weights.
- [[Prior Predictive Checking]] — does $\pi(\theta)$ imply sensible data? Check via the prior predictive $\pi(y)=\int\pi(y\mid\theta)\pi(\theta)\,d\theta$.

### 2. Multivariate models
- [[Multivariate Bayesian Models]] — the general recipe; marginals by integrating out nuisance parameters.
- [[Multivariate Normal Distribution]] — the building block.
- [[Normal Model with Unknown Mean and Variance]] — full Bayesian analysis with independent [[Jeffreys Prior]]s and with conjugate priors.
- [[Inverse Gamma Distribution]] — conjugate for a variance; relation to [[Gamma Distribution|Gamma]].
- [[Wishart Distribution]] — conjugate for a precision matrix (the multivariate analogue of Gamma).

### 3. Monte Carlo, continued
- [[Monte Carlo Integration]] — recap, finite/infinite ranges, multidimensional integrals.
- [[Rejection Sampling]] — sample from an easy $g$ and accept with the right probability.
  - Bounding constant $K=\max_x f(x)/g(x)$.
  - Acceptance probability $f(x)/(Kg(x))$; efficiency $\propto 1/K$.

## Key equations
$$\pi(\theta_1\mid x)=\int_{\Theta_d}\cdots\int_{\Theta_2}\pi(\theta\mid x)\,d\theta_2\cdots d\theta_d$$
$$\sigma^2\mid y\sim\text{InvGamma}\!\left(\frac{n-1}{2},\frac{(n-1)s^2}{2}\right)\qquad (\text{with independent Jeffreys priors})$$
$$\Pr(x^*\text{ accepted})=\frac{f(x^*)}{Kg(x^*)},\qquad K=\max_x\frac{f(x)}{g(x)}$$

## Connections
- **Builds on:** [[Week 2 Overview]]
- **Leads to:** [[Week 4 Overview]]

## Source
- [[Lecture Week 3.pdf]] (48 slides)
- [[Tutorial Week 3.pdf]]
