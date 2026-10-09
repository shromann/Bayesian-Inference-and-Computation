---
tags: [bayesian, prediction, week-1]
week: 1
type: concept
---

# Bayesian Predictive Distribution

> [!abstract] One-line summary
> The posterior predictive $p(y\mid x)=\int\pi(y\mid\theta)\pi(\theta\mid x)\,d\theta$ propagates parameter *uncertainty* into predictions, unlike plugging in a point estimate.

## Definition
For future data $y$,
$$p(y\mid x)=\int_\Theta \pi(y\mid\theta)\,\pi(\theta\mid x)\,d\theta.$$
This is the prior [[Prior Predictive Checking|predictive distribution]] with the prior replaced by the posterior.

## Why not just use $\hat\theta$?
Plugging in a fixed estimate gives $y\sim\pi(y\mid\hat\theta)$ and **ignores uncertainty about $\theta$**. In the [[Non-regular Likelihoods|hospital example]] with $\hat\theta=0$ this predicts 100% survival and 0% death — completely unrealistic. The Bayesian predictive accounts for parameter uncertainty and retains some possibility of future deaths.

## Monte Carlo shortcut
Instead of the (often laborious) algebra:
1. Draw $\theta^{(i)}\sim\pi(\theta\mid x)$.
2. For each, draw $y^{(i)}\sim\pi(y\mid\theta^{(i)})$.
3. Discard the $\theta^{(i)}$ — the remaining $y^{(i)}$ are a sample from $p(y\mid x)$.

This is "hugely simpler than calculating the exact algebraic expression". See [[Monte Carlo Integration]].

## Closed-form example
For the [[Water Consumption Example]] (Poisson–Gamma), the predictive is
$$p(y\mid x)=\text{NegBin}\!\left(y\mid \alpha+\textstyle\sum_i x_i,\ \frac{\beta+n}{\beta+n+1}\right).$$

## Connections
- **Builds on:** [[Posterior Distribution]] · [[Non-regular Likelihoods]] · [[Monte Carlo Integration]]
- **Leads to:** [[Prior Predictive Checking]] · [[Posterior Decision Theory]]
- **See also:** [[Negative Binomial Distribution]] · [[Water Consumption Example]]

## Source
- [[Lecture Week 1.pdf]], slides 8, 29, 37, 40, 49
- [[Tutorial Week 1.pdf]], Q1(c)
