---
tags: [bayesian, posterior, week-1]
week: 1
type: concept
---

# Posterior Distribution

> [!abstract] One-line summary
> The posterior $\pi(\theta\mid x)$ is the complete description of our knowledge about $\theta$ *after* seeing the data. It is, in a real sense, the inference.

## Definition
$$\pi(\theta\mid x)=\frac{L(x\mid\theta)\,\pi(\theta)}{m(x)}\;\propto\;L(x\mid\theta)\,\pi(\theta),\qquad m(x)=\int_\Theta L(x\mid\theta)\pi(\theta)\,d\theta.$$

It describes our knowledge about the model parameters in distributional form, after observing $x$. Going from $\pi(\theta)$ to $\pi(\theta\mid x)$ reflects how our beliefs changed.

## Why it is the whole answer
> [!important] Everything is in the posterior
> All information needed for further inference is contained in $\pi(\theta\mid x)$: point estimates, intervals, predictions, decisions. Every quantity is an integral over the posterior — which is why [[Monte Carlo Integration]] matters.

## Computing it
There are two practical routes ([[Lecture Week 1.pdf]] slide 30):
1. **Algebraically** (least common): exact but often difficult/impossible; only in restricted cases. → [[Conjugate Priors]]
2. **Computationally** (most common): approximate but always possible; simpler. → [[Monte Carlo Integration]]

Exact solutions save compute; knowing the maths behind the methods you implement is essential.

## Multivariate posterior
For $\theta=(\theta_1,\dots,\theta_d)$, marginals come from the [[Multivariate Bayesian Models|joint posterior]] by integrating out the rest. All inference proceeds via integration; nuisance parameters are integrated away.

## Connections
- **Builds on:** [[Bayes Theorem]] · [[Prior Distribution]] · [[Likelihood Function]]
- **Leads to:** [[Posterior Inference]] · [[Credible Intervals]] · [[Bayesian Predictive Distribution]] · [[Conjugate Priors]] · [[Monte Carlo Integration]] · [[Normalising Constant]]
- **See also:** [[Bayesian Updating]] · [[Water Consumption Example]]

## Source
- [[Lecture Week 1.pdf]], slides 14–15, 25–40
