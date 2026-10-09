---
tags: [reference, conjugate, week-2]
week: 2
type: reference
---

# Conjugate Prior Reference Table

> [!abstract] One page, all standard conjugate pairs
> The likelihood, the conjugate prior, and the resulting posterior. Notation: $\bar x=\frac1n\sum x_i$; $\tau=1/\sigma^2$ is the likelihood precision and $c=1/d^2$ the prior precision.

## Standard pairs

| Likelihood | Prior | Posterior |
|---|---|---|
| $x\sim\text{Bin}(n,\theta)$ | $\text{Beta}(p,q)$ | $\text{Beta}(p+x,\ q+n-x)$ |
| $x_1,\dots,x_n\sim\text{Poisson}(\theta)$ | $\text{Gamma}(p,q)$ | $\text{Gamma}\!\left(p+\sum_{i=1}^n x_i,\ q+n\right)$ |
| $x_1,\dots,x_n\sim N(\theta,\tau^{-1})$ ($\tau$ known) | $N(b,c^{-1})$ | $N\!\left(\frac{cb+n\tau\bar x}{c+n\tau},\ \frac{1}{c+n\tau}\right)$ |
| $x_1,\dots,x_n\sim\text{Gamma}(k,\theta)$ ($k$ known) | $\text{Gamma}(p,q)$ | $\text{Gamma}\!\left(p+nk,\ q+\sum_{i=1}^n x_i\right)$ |
| $x_1,\dots,x_n\sim\text{Geometric}(\theta)$ | $\text{Beta}(p,q)$ | $\text{Beta}\!\left(p+n,\ q+\sum_{i=1}^n x_i-n\right)$ |
| $x\sim\text{NegBin}(r,\theta)$ | $\text{Beta}(p,q)$ | $\text{Beta}(p+r,\ q+x)$ |

## Multivariate extension

| Likelihood | Prior | Posterior |
|---|---|---|
| $x_i\sim N_d(\mu,\Sigma)$, $\Sigma$ known | $N_d(\mu_0,\Sigma_0)$ | $N_d(\hat\mu,\hat\Sigma)$ (see [[Multivariate Bayesian Models]]) |
| $x_i\sim N_d(\mu,\Sigma)$, $\mu$ known | $IW_d(\Sigma\mid v,A)$ | $IW_d(\Sigma\mid\hat v,\hat A)$, $\hat v=v+\frac n2$, $\hat A=A+\frac12\sum_i(x_i-\mu)(x_i-\mu)^\top$ |

## Key facts
- Conjugacy holds (essentially) only for the [[Exponential Family]].
- Posterior precision = prior precision + $n\times$ data precision (Normal case).
- The [[Exponential Family]] construction explains *why* the prior has the form $\pi(\theta)\propto g(\theta)^d\exp\{b\,c(\theta)\}$.
- Full derivations of the first four pairs: [[Lecture Week 2.pdf]]; last two: [[Tutorial Week 2]] Q5.

## Connections
- **Builds on:** [[Conjugate Priors]] · [[Exponential Family]]
- **See also:** [[Probability Distributions]] · [[Normal Model with Unknown Mean and Variance]] · [[Wishart Distribution]]

## Source
- [[Lecture Week 2.pdf]], slide 19
- [[Tutorial Week 2.pdf]], Q5
