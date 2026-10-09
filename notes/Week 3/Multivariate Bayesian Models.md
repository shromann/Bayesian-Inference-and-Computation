---
tags: [multivariate, week-3]
week: 3
type: concept
---

# Multivariate Bayesian Models

> [!abstract] One-line summary
> Bayesian inference generalises to a parameter vector $\theta=(\theta_1,\dots,\theta_d)$ with no new theory — just specify a multivariate prior, compute the joint posterior, and integrate out nuisance parameters.

## The general recipe
$$\pi(\theta\mid x)\propto L(x\mid\theta)\,\pi(\theta),$$
identical in form to the univariate case. Virtually every practical problem has more than one unknown quantity, and this is where Bayesian methods become *easier* than their classical counterparts (no need for profiling, no asymptotic approximations).

## Marginal distributions
To infer $\theta_1$ when only 1 or a few parameters matter, integrate out the rest:
$$\pi(\theta_1\mid x)=\int_{\Theta_d}\cdots\int_{\Theta_2}\pi(\theta\mid x)\,d\theta_2\cdots d\theta_d.$$
Do this (a) algebraically or (b) via [[Monte Carlo Integration|Monte Carlo simulation]]. *Marginal* because you summarise the joint by integrating (marginalising) the others.

## The three challenges
1. **Prior specification** — multivariate priors involve complex dependencies and are harder to elicit.
2. **Computation** — integrals are harder; need algorithms beyond [[Inversion Sampling]].
3. **Interpretation** — posterior structure is more complex.

## Worked examples
- **Discrete (machine quality):** finite $\theta$, so the joint posterior is just a normalised table. Multiply likelihood by prior, normalise, then sum rows/columns for marginals. ([[Tutorial Week 3]] Q1.)
- **Poisson decomposition:** $Y_1\sim\text{Poisson}(\alpha\beta)$, $Y_2\sim\text{Poisson}((1-\alpha)\beta)$, independent given $(\alpha,\beta)$. With $\alpha\sim\text{Beta}(p,q)$, $\beta\sim\text{Gamma}(p+q,1)$ independent:
$$\alpha\mid y_1,y_2\sim\text{Beta}(y_1+p,\ y_2+q),\qquad \beta\mid y_1,y_2\sim\text{Gamma}(y_1+y_2+p+q,\ 2).$$
The joint posterior **factorises**, so sampling is easy: first $\alpha$, then $\beta$.
- **Normal with unknown mean and variance:** see [[Normal Model with Unknown Mean and Variance]].
- **Multivariate regression:** conjugate priors are [[Multivariate Normal Distribution|multivariate normal]] for $\mu$ and [[Wishart Distribution|inverse Wishart]] for $\Sigma$.

## Multivariate conjugate structure
| Univariate (scalar) | Multivariate |
|---|---|
| precision $\tau$, conjugate [[Gamma Distribution|Gamma]] | precision matrix $\Lambda$, conjugate [[Wishart Distribution|Wishart]] |
| variance $\sigma^2$, conjugate [[Inverse Gamma Distribution|InvGamma]] | covariance $\Sigma$, conjugate [[Wishart Distribution|InvWishart]] |

For known $\Sigma$, the conjugate prior for $\mu$ is $N_d(\mu_0,\Sigma_0)$ and the posterior is $N_d(\hat\mu,\hat\Sigma)$ with
$$\hat\mu=(\Sigma_0^{-1}+n\Sigma^{-1})^{-1}(\Sigma_0^{-1}\mu_0+n\Sigma^{-1}\bar x),\qquad \hat\Sigma=(\Sigma_0^{-1}+n\Sigma^{-1})^{-1}.$$
A clear analogy with the univariate normal update in [[Conjugate Priors]].

## Connections
- **Builds on:** [[Posterior Distribution]] · [[Conjugate Priors]] · [[Jeffreys Prior]]
- **Leads to:** [[Multivariate Normal Distribution]] · [[Normal Model with Unknown Mean and Variance]] · [[Wishart Distribution]] · [[Monte Carlo Integration]]
- **See also:** [[Inverse Gamma Distribution]] · [[Posterior Inference]]

## Source
- [[Lecture Week 3.pdf]], slides 10–27
- [[Tutorial Week 3.pdf]], Q1, Q4
