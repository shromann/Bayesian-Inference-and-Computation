---
tags: [distributions, discrete, prediction]
type: distribution
---

# Negative Binomial Distribution

> [!abstract] One-line summary
> The predictive distribution that arises from a Poisson likelihood with a Gamma prior. Conjugate prior for its probability parameter is [[Beta Distribution|Beta]].

## Probability mass function
$$\pi(y\mid a,p)=\binom{y+a-1}{y}(1-p)^y p^a,\qquad a>0,\ 0\le p\le1.$$

## Predictive role
For $x_1,\dots,x_n\sim\text{Poisson}(\theta)$ with $\theta\sim\text{Gamma}(\alpha,\beta)$, the posterior predictive of a future count $y$ is
$$p(y\mid x)=\int\pi(y\mid\theta)\pi(\theta\mid x)\,d\theta=\text{NegBin}\!\left(y\ \Big|\ \alpha+\sum_i x_i,\ \frac{\beta+n}{\beta+n+1}\right).$$
See [[Water Consumption Example]] and [[Bayesian Predictive Distribution]].

## Conjugate role
$\text{NegBin}(r,\theta)$ likelihood + $\text{Beta}(p,q)$ prior → $\text{Beta}(p+r,\ q+x)$ posterior (see [[Conjugate Prior Reference Table]]).

## Connections
- **Builds on:** [[Poisson Distribution]] · [[Gamma Distribution]] · [[Bayesian Predictive Distribution]]
- **Leads to:** [[Conjugate Priors]]
- **See also:** [[Conjugate Prior Reference Table]] · [[Tutorial Week 1]] Q1(c)

## Source
- [[Lecture Week 1.pdf]], slide 37
- [[Tutorial Week 1.pdf]], Q1(c)
