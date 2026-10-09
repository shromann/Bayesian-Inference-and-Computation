---
tags: [priors, jeffreys, week-2]
week: 2
type: concept
---

# Jeffreys Prior

> [!abstract] One-line summary
> The Jeffreys prior $\pi_J(\theta)\propto|I(\theta)|^{1/2}$ is the "default" ignorance prior that is invariant under one-to-one reparameterisation.

## Definition
$$\pi_J(\theta)\propto|I(\theta)|^{1/2},\qquad I(\theta)=-E\!\left[\frac{d^2\log L(x\mid\theta)}{d\theta^2}\right]$$
where $I(\theta)$ is the [[Fisher Information]] matrix. Harold Jeffreys (1891–1989) argued that a specification of prior ignorance should be *consistent across 1–1 transformations* — something a flat prior fails to do (see [[Improper Priors]]).

## Why it is invariant
If $\phi=g(\theta)$ is monotone, then
$$\pi_J(\phi)=\pi_J(\theta)\left|\frac{d\theta}{d\phi}\right|\propto|I(\theta)|^{1/2}\left|\frac{d\theta}{d\phi}\right|
=\left|I(\theta)\left(\frac{d\theta}{d\phi}\right)^2\right|^{1/2}
=|I(\phi)|^{1/2}.$$
So the same rule gives the correct prior in *any* parameterisation.

## Worked examples

### Binomial
$x\mid\theta\sim\text{Bin}(n,\theta)$:
$$I(\theta)=\frac{n}{\theta}+\frac{n}{1-\theta}=n\theta^{-1}(1-\theta)^{-1}\;\Longrightarrow\;\pi_J(\theta)\propto\theta^{-1/2}(1-\theta)^{-1/2},$$
which is the **proper** distribution $\text{Beta}(\tfrac12,\tfrac12)$.

### Normal mean (N1)
$X_i\sim N(\theta,\sigma^2)$, $\sigma^2$ known: $I(\theta)=n/\sigma^2$, so $\pi_J(\theta)\propto1$ — the improper uniform prior on $\mathbb{R}$.

### Normal variance (N2)
$X_i\sim N(m,\theta)$, $m$ known: $I(\theta)=n/(2\theta^2)$, so $\pi_J(\theta)\propto\theta^{-1}$ (improper) on $\mathbb{R}^+$.

### Normal mean and variance (N3)
$\theta=(\mu,\sigma^2)$: the information matrix is block diagonal,
$$I(\theta)=\begin{pmatrix}n/\sigma^2&0\\0&n/(2\sigma^4)\end{pmatrix}\;\Longrightarrow\;\pi_J(\mu,\sigma^2)\propto\left[\frac{n}{\sigma^2}\cdot\frac{n}{2\sigma^4}\right]^{1/2}\propto\sigma^{-3}.$$

## Objections
> [!warning] Two standard criticisms
> 1. **Data-dependence:** Jeffreys' prior depends on the likelihood $L(x\mid\theta)$ (i.e. on what data you intend to collect). A prior "should not" depend on the data to be collected.
> 2. **Inconsistency:** the priors don't factor. Here $N3\ne N2\times N1$. Jeffreys argues ignorance about $\mu$ and $\sigma^2$ should be represented by independent ignorance priors for each parameter separately — motivating the product form $\pi(\mu,\sigma^2)=1/\sigma^2$ used in [[Normal Model with Unknown Mean and Variance]] and [[Multivariate Bayesian Models]].

## Connections
- **Builds on:** [[Fisher Information]] · [[Improper Priors]]
- **Leads to:** [[Normal Model with Unknown Mean and Variance]] · [[Multivariate Bayesian Models]]
- **See also:** [[Conjugate Priors]] · [[Prior Distribution]]

## Source
- [[Lecture Week 2.pdf]], slides 25–34
- [[Tutorial Week 2.pdf]], Q6
- [[Tutorial Week 3.pdf]], Q2
