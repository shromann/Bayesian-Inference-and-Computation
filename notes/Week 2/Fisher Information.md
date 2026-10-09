---
tags: [theory, information, week-2]
week: 2
type: concept
---

# Fisher Information

> [!abstract] One-line summary
> The Fisher information measures how much the data tell us about a parameter. It is the curvature of the log-likelihood and the building block of [[Jeffreys Prior]].

## Definition (univariate)
$$I(\theta)=-E\!\left[\frac{d^2\log L(x\mid\theta)}{d\theta^2}\right].$$
It is the expected curvature of the log-likelihood at $\theta$: a sharp peak means lots of information.

## Role in asymptotics
- In [[Posterior Asymptotics]], the posterior converges to $N(\theta_0, I_n(\theta_0)^{-1})$ where $I_n(\theta)=nI(\theta)$.
- For the [[Maximum Likelihood Estimation|MLE]] this is the usual variance.

## Role in Jeffreys' prior
[[Jeffreys Prior]] is defined as $\pi_J(\theta)\propto|I(\theta)|^{1/2}$ — chosen precisely because it transforms correctly under reparameterisation.

## Examples
| Model | $I(\theta)$ | Jeffreys prior |
|---|---|---|
| $\text{Binomial}(n,\theta)$ | $n\theta^{-1}(1-\theta)^{-1}$ | $\propto\theta^{-1/2}(1-\theta)^{-1/2}$ |
| $N(\theta,\sigma^2)$, $\sigma^2$ known | $n/\sigma^2$ | $\propto1$ |
| $N(m,\theta)$ (variance) | $n/(2\theta^2)$ | $\propto\theta^{-1}$ |
| $N(\mu,\sigma^2)$ both unknown | $\mathrm{diag}(n/\sigma^2,\ n/(2\sigma^4))$ | $\propto\sigma^{-3}$ |

## Connections
- **Builds on:** [[Likelihood Function]]
- **Leads to:** [[Jeffreys Prior]] · [[Posterior Asymptotics]]
- **See also:** [[Maximum Likelihood Estimation]]

## Source
- [[Lecture Week 2.pdf]], slides 26–33
- [[Lecture Week 4.pdf]], slides 21–25
