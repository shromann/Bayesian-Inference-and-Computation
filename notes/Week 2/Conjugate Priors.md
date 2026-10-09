---
tags: [priors, conjugate, week-2]
week: 2
type: concept
---

# Conjugate Priors

> [!abstract] One-line summary
> A conjugate prior is chosen so that the posterior stays in the same distributional family as the prior — turning [[Bayes Theorem]] into simple parameter arithmetic.

## Definition
If $\mathcal{F}$ is a class of sampling distributions (likelihoods) $L(x\mid\theta)$ and $\mathcal{P}$ is a class of priors, then $\mathcal{P}$ is **conjugate** for $\mathcal{F}$ if
$$\pi(\theta\mid x)\in\mathcal{P}\quad\text{for all } L(\cdot\mid\theta)\in\mathcal{F}\ \text{and}\ \pi(\cdot)\in\mathcal{P}.$$
In words: conjugate priors let the posterior stay in the same family as the prior. Viable when that family is flexible enough to describe prior beliefs.

## Why they matter
Conjugacy means the [[Normalising Constant]] integrates into a recognisable kernel — no numerical integration needed. This is the "algebraic" route to the [[Posterior Distribution]].

## Core examples (derivations)

### Binomial + Beta
$x\sim\text{Binomial}(n,\theta)$, prior $\theta\sim\text{Beta}(a,b)\propto\theta^{a-1}(1-\theta)^{b-1}$:
$$\pi(\theta\mid x)\propto\theta^{x}(1-\theta)^{n-x}\cdot\theta^{a-1}(1-\theta)^{b-1}=\theta^{a+x-1}(1-\theta)^{b+n-x-1}$$
$$\Longrightarrow\quad \theta\mid x\sim\text{Beta}(a+x,\ b+n-x).$$

### Poisson + Gamma
$x_1,\dots,x_n\stackrel{iid}{\sim}\text{Poisson}(\theta)$, prior $\theta\sim\text{Gamma}(a,b)\propto\theta^{a-1}e^{-b\theta}$:
$$\pi(\theta\mid x)\propto e^{-n\theta}\theta^{\sum x_i}\theta^{a-1}e^{-b\theta}\Longrightarrow \theta\mid x\sim\text{Gamma}\!\left(a+\textstyle\sum x_i,\ b+n\right).$$

### Gamma + Gamma
$x_1,\dots,x_n\stackrel{iid}{\sim}\text{Gamma}(k,\theta)$ with $k$ known, prior $\theta\sim\text{Gamma}(a,b)$:
$$\pi(\theta\mid x)\propto\theta^{kn}e^{-\theta\sum x_i}\theta^{a-1}e^{-b\theta}\Longrightarrow \theta\mid x\sim\text{Gamma}\!\left(a+kn,\ b+\textstyle\sum x_i\right).$$

### Normal + Normal (known variance)
$x_1,\dots,x_n\sim N(\theta,\sigma^2)$, $\sigma^2$ known, prior $\theta\sim N(b,d^2)$. With precisions $c=1/d^2$ and $\tau=1/\sigma^2$:
$$\theta\mid x\sim N\!\left(\frac{cb+n\tau\bar x}{c+n\tau},\ \frac{1}{c+n\tau}\right).$$

## Interpreting the normal update
- $E(\theta\mid x)=\gamma_n b+(1-\gamma_n)\bar x$ with $\gamma_n=\frac{c}{c+n\tau}$ — a **weighted average** of prior mean and sample mean.
- **Posterior precision = prior precision + $n\times$ data precision.**
- $\bar x$ is **sufficient** for $\theta$: the posterior depends on the data only through $\bar x$.
- As $n\to\infty$, $\theta\mid x\approx N(\bar x,\sigma^2/n)$: the prior washes out.
- As $d\to\infty$ ($c\to0$), the same limit: a diffuse prior gives the same answer. See [[Improper Priors]].

## Full reference
- [[Conjugate Prior Reference Table]] — all standard pairs.
- [[Exponential Family]] — the general reason conjugate priors exist.

## Connections
- **Builds on:** [[Prior Distribution]] · [[Likelihood Function]] · [[Normalising Constant]]
- **Leads to:** [[Exponential Family]] · [[Improper Priors]] · [[Mixture Priors]] · [[Normal Model with Unknown Mean and Variance]] · [[Multivariate Bayesian Models]]
- **See also:** [[Bayesian Updating]] · [[Water Consumption Example]] · [[Maximum A Posteriori]]

## Source
- [[Lecture Week 2.pdf]], slides 6–19
- [[Tutorial Week 2.pdf]], Q1, Q2, Q5
