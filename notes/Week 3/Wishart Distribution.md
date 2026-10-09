---
tags: [distributions, multivariate, conjugate, week-3]
week: 3
type: distribution
---

# Wishart Distribution

> [!abstract] One-line summary
> The Wishart is the multivariate generalisation of the Gamma and serves as the conjugate prior for a precision matrix $\Lambda=\Sigma^{-1}$. Its inverse, the Inverse Wishart, is conjugate for a covariance matrix $\Sigma$.

## Wishart density
For $\Lambda\sim W_d(\Lambda\mid v,A)$:
$$\pi(\Lambda\mid v,A)=\frac{|A|^v}{\Gamma_d(v)}|\Lambda|^{v-(d+1)/2}\exp[-\operatorname{tr}(A\Lambda)],$$
with degrees of freedom $v\in(\frac{d-1}{2},\infty)$ (real) and scale $A\in\mathbb{R}^{d\times d}$ positive semi-definite. When $d=1$ this reduces to the [[Gamma Distribution]].

## Inverse Wishart density
For $\Sigma\sim IW_d(\Sigma\mid v,A)$:
$$\pi(\Sigma\mid v,A)=\frac{|A|^v}{\Gamma_d(v)}|\Sigma|^{-v-(d+1)/2}\exp(-\operatorname{tr}(A\Sigma^{-1})).$$
When $d=1$ this reduces to the [[Inverse Gamma Distribution]].

## Conjugate use
- With known $\mu$, conjugate prior $\Sigma\sim IW_d(v,A)$ gives posterior $IW_d(\hat v,\hat A)$ with
$$\hat v=v+\frac n2,\qquad \hat A=A+\frac12\sum_{i=1}^n(x_i-\mu)(x_i-\mu)^\top.$$
- Equivalently, $\Lambda=\Sigma^{-1}$ with a Wishart prior gives a Wishart posterior.

A clear analogy with the univariate result in [[Conjugate Priors]].

## Connections
- **Builds on:** [[Gamma Distribution]] · [[Inverse Gamma Distribution]] · [[Multivariate Normal Distribution]]
- **Leads to:** [[Multivariate Bayesian Models]]
- **See also:** [[Conjugate Prior Reference Table]] · [[Tutorial Week 3]] Q4

## Source
- [[Lecture Week 3.pdf]], slides 24–27
