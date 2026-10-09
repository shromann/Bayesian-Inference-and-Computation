---
tags: [distributions, multivariate, week-3]
week: 3
type: distribution
---

# Multivariate Normal Distribution

> [!abstract] One-line summary
> The $d$-dimensional Gaussian — the building block for multivariate regression and the conjugate prior for a mean vector when the covariance is known.

## Density
For $x\in\mathbb{R}^d$,
$$\pi(x\mid\mu,\Sigma)=\frac{1}{(2\pi)^{d/2}|\Sigma|^{1/2}}\exp\!\left(-\tfrac12(x-\mu)^T\Sigma^{-1}(x-\mu)\right),$$
where $\mu\in\mathbb{R}^d$ is the mean vector and $\Sigma$ is a $d\times d$ positive semi-definite covariance matrix. The **precision matrix** $\Lambda=\Sigma^{-1}$ (analogous to $\tau=1/\sigma^2$) is also positive semi-definite.

## Conjugate use
When the covariance $\Sigma$ is known, the conjugate prior for the mean is
$$\mu\sim N_d(\mu_0,\Sigma_0),$$
and the posterior is $N_d(\hat\mu,\hat\Sigma)$ with the precision-weighted forms given in [[Multivariate Bayesian Models]]. This is the direct analogue of the univariate Normal–Normal update.

## Connections
- **Builds on:** [[Normal Distribution]]
- **Leads to:** [[Multivariate Bayesian Models]] · [[Wishart Distribution]]
- **See also:** [[Conjugate Priors]]

## Source
- [[Lecture Week 3.pdf]], slides 24, 26–27
- [[Tutorial Week 3.pdf]], Q4
