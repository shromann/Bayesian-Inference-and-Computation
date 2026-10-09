---
tags: [distributions, conjugate]
type: distribution
---

# Beta Distribution

> [!abstract] One-line summary
> A distribution on $[0,1]$ — the natural model for a probability — and the conjugate prior for the [[Binomial Distribution|Binomial]] and related likelihoods.

## Density
$$\pi(\theta)=\frac{\Gamma(a+b)}{\Gamma(a)\Gamma(b)}\theta^{a-1}(1-\theta)^{b-1}\propto\theta^{a-1}(1-\theta)^{b-1},\qquad 0\le\theta\le1.$$

## Moments
$$\mathbb{E}[\theta]=\frac{a}{a+b},\qquad \text{Var}(\theta)=\frac{ab}{(a+b)^2(a+b+1)}.$$

## Conjugate role
[[Binomial Distribution|Binomial]] likelihood + $\text{Beta}(a,b)$ prior → $\text{Beta}(a+x,\ b+n-x)$ posterior. Used in the drunk-friend / tea-drinker / music-expert example ([[Prior Distribution]]) and [[Prior Predictive Checking]].

Special case: the [[Jeffreys Prior]] for the binomial is the proper $\text{Beta}(\tfrac12,\tfrac12)$.

## Connections
- **Builds on:** [[Probability Distributions]]
- **Leads to:** [[Conjugate Priors]] · [[Mixture Priors]] · [[Prior Predictive Checking]]
- **See also:** [[Conjugate Prior Reference Table]] · [[Binomial Distribution]]

## Source
- [[Lecture Week 2.pdf]], slides 7–8
- [[Lecture Week 1.pdf]], slide 19
