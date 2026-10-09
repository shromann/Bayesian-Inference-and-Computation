---
tags: [bayesian, inference, week-1]
week: 1
type: concept
---

# Posterior Inference

> [!abstract] One-line summary
> All inference is integration over the posterior: means, variances, credible intervals, and predictive distributions.

## Point estimates
For the [[Water Consumption Example]] with posterior $\theta\mid x\sim\text{Gamma}(\alpha+\sum_i x_i,\ \beta+n)$:
$$E_\pi[\theta]=\int_\Theta\theta\,\pi(\theta\mid x)\,d\theta=\frac{\alpha+\sum_i x_i}{\beta+n},$$
$$\text{Var}(\theta)=E_\pi[\theta^2]-E_\pi[\theta]^2=\frac{\alpha+\sum_i x_i}{(\beta+n)^2}.$$

## Credible intervals
A 95% [[Credible Intervals|credible interval]] $[a,b]$ solves
$$\int_0^a\pi(\theta\mid x)\,d\theta=0.025,\qquad\int_0^b\pi(\theta\mid x)\,d\theta=0.975.$$

## Predictive distributions
$$p(y\mid x)=\int_\Theta\pi(y\mid\theta)\pi(\theta\mid x)\,d\theta.$$
See [[Bayesian Predictive Distribution]].

## Multivariate case
For $\theta=(\theta_0,\theta_1,\theta_2,\kappa)$ (e.g. a change-point model), nuisance parameters are integrated out. The marginal of $\kappa$ is
$$\pi(\kappa\mid x)=\int_{\Theta_2}\int_{\Theta_1}\int_{\Theta_0}\pi(\theta_0,\theta_1,\theta_2,\kappa\mid x)\,d\theta_0\,d\theta_1\,d\theta_2.$$
Procedure is conceptually simple — but the algebra becomes hard fast, which is exactly why [[Monte Carlo Integration]] exists.

## Summary
> [!important] Integration is the theme
> Every posterior summary is an integral. Closed solutions are typically impossible, so we approximate the posterior by sampling from it.

## Connections
- **Builds on:** [[Posterior Distribution]]
- **Leads to:** [[Credible Intervals]] · [[Bayesian Predictive Distribution]] · [[Monte Carlo Integration]] · [[Posterior Decision Theory]]
- **See also:** [[Water Consumption Example]] · [[Multivariate Bayesian Models]]

## Source
- [[Lecture Week 1.pdf]], slides 36–40
