---
tags: [priors, mixture, week-3]
week: 3
type: concept
---

# Mixture Priors

> [!abstract] One-line summary
> A mixture of conjugate priors is still conjugate — the posterior is a mixture of the component posteriors with updated weights. This buys flexibility (e.g. bimodal beliefs) while keeping the maths easy.

## Motivation
[[Conjugate Priors]] are convenient but may be too rigid to capture prior beliefs. Example: the probability of heads when *spinning* a coin on a table. Tossing suggests $\approx0.5$, but spinning can favour $0.4$ or $0.6$ because of edge imperfections. The prior belief is **bimodal or trimodal** — a single [[Beta Distribution|Beta]] cannot represent this.

## Construction
Suppose $\pi_1(\theta),\dots,\pi_k(\theta)$ are all conjugate priors for $\theta$, giving posteriors $\pi_1(\theta\mid x),\dots,\pi_k(\theta\mid x)$. Take
$$\pi(\theta)=\sum_{i=1}^k w_i\,\pi_i(\theta),\qquad \sum_{i=1}^k w_i=1.$$
Then
$$\pi(\theta\mid x)=\frac{\pi(\theta)L(x\mid\theta)}{m(x)}
=\frac{\sum_i w_i\pi_i(\theta)L(x\mid\theta)}{m(x)}
=\sum_{i=1}^k w_i^*\,\pi_i(\theta\mid x),$$
where
$$w_i^*=\frac{w_i\,m_i(x)}{m(x)},\qquad m(x)=\sum_{i=1}^k w_i\,m_i(x),\qquad \sum_i w_i^*=1.$$

## Key result
> [!important] Closure
> The posterior is in the same conjugate-mixture family. The data update the **weights**: component $i$ gains weight in proportion to its marginal likelihood $m_i(x)$.

## Why it matters
- Handles multimodal/skewed priors.
- The weights $w_i^*$ are exactly the ingredient used later for **model comparison / Bayes factors** (link back to [[Normalising Constant|marginal likelihood]]).

## Connections
- **Builds on:** [[Conjugate Priors]] · [[Normalising Constant]]
- **Leads to:** model comparison (later weeks) · [[Prior Predictive Checking]]
- **See also:** [[Prior Distribution]]

## Source
- [[Lecture Week 3.pdf]], slides 4–5
