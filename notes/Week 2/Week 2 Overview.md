---
tags: [moc, week-2]
week: 2
type: map-of-content
---

# Week 2 Overview — Priors & Inversion Sampling

> [!abstract] Theme
> The [[Posterior Distribution]] is usually only known up to its [[Normalising Constant]]. This week we choose priors that make the algebra easy ([[Conjugate Priors]], [[Improper Priors]], [[Jeffreys Prior]]) and learn the first sampling algorithm ([[Inversion Sampling]]).

## Learning objectives
By the end you should be able to:
- Derive a posterior in closed form using a conjugate prior.
- Recognise the [[Exponential Family]] and construct a conjugate prior for it.
- Use and critique [[Improper Priors]] and derive a [[Jeffreys Prior]].
- Relate the [[Maximum A Posteriori|MAP]] to the [[Maximum Likelihood Estimation|MLE]].
- Draw samples from a univariate distribution by [[Inversion Sampling]].

## Path through the material

### 1. Why the normalising constant matters
- [[Normalising Constant]] — $m(x)=\int L(x\mid\theta)\pi(\theta)\,d\theta$; even simple priors create hard integrals.
- [[Posterior Distribution]] — recall the target.

### 2. Priors that keep the maths easy
- [[Conjugate Priors]] — posterior stays in the prior's family.
  - [[Binomial Distribution|Binomial]] + [[Beta Distribution|Beta]] → Beta
  - [[Poisson Distribution|Poisson]] + [[Gamma Distribution|Gamma]] → Gamma
  - [[Gamma Distribution|Gamma]] + Gamma → Gamma
  - [[Normal Distribution|Normal]] (known variance) + Normal → Normal
- [[Conjugate Prior Reference Table]] — the full list.
- [[Exponential Family]] — *why* conjugate priors exist.

### 3. Priors that add nothing (and their problems)
- [[Improper Priors]] — $\int\pi(\theta)\,d\theta=\infty$, yet the posterior can be proper.
- [[Maximum A Posteriori]] — with a flat prior, MAP = MLE.
- Transformation non-invariance of improper priors → motivates Jeffreys.
- [[Jeffreys Prior]] — $\pi_J(\theta)\propto|I(\theta)|^{1/2}$, with [[Fisher Information]].
- Worked cases: Binomial ($\text{Beta}(\tfrac12,\tfrac12)$), Normal mean ($\pi\propto1$), Normal variance ($\pi\propto\theta^{-1}$), Normal mean+variance ($\pi\propto\sigma^{-3}$).

### 4. Monte Carlo methods start
- [[Inversion Sampling]] — invert the CDF.
- [[Probability Integral Transform]] — the theorem that makes it work.

## Key equations
$$\pi(\theta)\propto g(\theta)^d\exp\{b\,c(\theta)\}\quad\text{(conjugate prior for an exponential family)}$$
$$\pi_J(\theta)\propto|I(\theta)|^{1/2},\qquad I(\theta)=-E\!\left[\frac{d^2\log L(x\mid\theta)}{d\theta^2}\right]$$
$$x=F^{-1}(u),\qquad u\sim U(0,1)$$

## Connections
- **Builds on:** [[Week 1 Overview]]
- **Leads to:** [[Week 3 Overview]]

## Source
- [[Lecture Week 2.pdf]] (45 slides)
- [[Tutorial Week 2.pdf]]
