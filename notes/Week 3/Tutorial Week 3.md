---
tags: [tutorial, week-3]
week: 3
type: tutorial
---

# Tutorial Week 3

> [!abstract] Focus
> Discrete and continuous [[Multivariate Bayesian Models]], [[Jeffreys Prior]] for a Pareto model, [[Inverse Gamma Distribution|InvGamma]] conjugacy, and the [[Multivariate Normal Distribution|multivariate normal]].

## Q1 — Electrical component (discrete multivariate)
$\theta_1$ (factory), $\theta_2$ (machine); likelihood $\Pr(x=3\mid\theta_1,\theta_2)$ and prior $\Pr(\theta_1,\theta_2)$ given as tables.

**(a)** Form the joint posterior table: multiply likelihood × prior entrywise for $x=3$, then normalise by the total. Marginals are row/column sums:
$$\Pr(\theta_1\mid x=3)=\sum_{\theta_2}\Pr(\theta_1,\theta_2\mid x=3),\qquad \Pr(\theta_2\mid x=3)=\sum_{\theta_1}\Pr(\theta_1,\theta_2\mid x=3).$$
**(b)** Compare the highest-probability cell before vs after — the observation may shift which combination is most likely.
→ [[Multivariate Bayesian Models]] · [[Bayes Theorem]] · [[Posterior Inference]]

## Q2 — Pareto Jeffreys prior
$f(x\mid b)=b\,a_0^{\,b}\,x^{-b-1}$ for $x>a_0$, $a_0$ known, $b>0$ unknown.
$$\log f=\log b+b\log a_0-(b+1)\log x,\qquad \frac{d^2\log f}{db^2}=-\frac1{b^2}$$
$$\Longrightarrow\ I(b)=\frac1{b^2},\qquad \pi_J(b)\propto\frac1b\ (\text{improper}).$$
Posterior for $x_1,\dots,x_n$:
$$L=b^n a_0^{nb}\Big(\textstyle\prod x_i\Big)^{-b-1}\;\Longrightarrow\;\pi(b\mid x)\propto b^{n-1}e^{-b\sum_i\log(x_i/a_0)},$$
so
$$b\mid x\sim\text{Gamma}\!\left(n,\ \sum_{i=1}^n\log\frac{x_i}{a_0}\right).$$
→ [[Jeffreys Prior]] · [[Fisher Information]] · [[Gamma Distribution]]

## Q3 — Precision / variance conjugacy
$x_i\sim N(\mu_0,\tau^{-1})$, $\mu_0$ fixed.
**(a)** If $\tau=1/\sigma^2\sim\text{Gamma}(\alpha,\beta)$ then $\sigma^2\sim$ [[Inverse Gamma Distribution|InvGamma]]$(\alpha,\beta)$ (change of variables).
**(b)** Likelihood $\propto\tau^{n/2}\exp\{-\frac\tau2\sum(x_i-\mu_0)^2\}$, so with a Gamma prior
$$\tau\mid x\sim\text{Gamma}\!\left(\alpha+\frac n2,\ \beta+\frac12\sum_{i=1}^n(x_i-\mu_0)^2\right).$$
**(c)** Equivalently in the variance parameterisation, InvGamma is conjugate for $\sigma^2$.
→ [[Inverse Gamma Distribution]] · [[Normal Distribution]] · [[Conjugate Priors]]

## Q4 — Multivariate normal
$x_1,\dots,x_n\in\mathbb{R}^d$, $x_i\sim N_d(\mu,\Sigma)$.
**(a)** Conjugate prior $\mu\sim N_d(\mu_0,\Sigma_0)$ gives
$$\hat\mu=(\Sigma_0^{-1}+n\Sigma^{-1})^{-1}(\Sigma_0^{-1}\mu_0+n\Sigma^{-1}\bar x),\qquad \hat\Sigma=(\Sigma_0^{-1}+n\Sigma^{-1})^{-1}.$$
**(b)** With known $\mu$ and $\Lambda=\Sigma^{-1}\sim W_d(v,A)$,
$$\hat v=v+\frac n2,\qquad \hat A=A+\frac12\sum_{i=1}^n(x_i-\mu)(x_i-\mu)^\top,$$
so the posterior is again [[Wishart Distribution|Wishart]].
→ [[Multivariate Bayesian Models]] · [[Multivariate Normal Distribution]] · [[Wishart Distribution]]

## Connections
- **See also:** [[Week 3 Overview]] · [[Normal Model with Unknown Mean and Variance]]

## Source
- [[Tutorial Week 3.pdf]]
