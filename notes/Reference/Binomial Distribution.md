---
tags: [distributions, discrete]
type: distribution
---

# Binomial Distribution

> [!abstract] One-line summary
> The number of successes in $n$ independent trials. Its conjugate prior is the [[Beta Distribution|Beta]].

## Probability mass function
$$L(x\mid\theta)=\binom{n}{x}\theta^x(1-\theta)^{n-x},\qquad x=0,\dots,n.$$

## Moments
$$\mathbb{E}[X]=n\theta,\qquad \text{Var}(X)=n\theta(1-\theta).$$

## Conjugate role
$\text{Beta}(a,b)$ prior → $\text{Beta}(a+x,\ b+n-x)$ posterior. This is the first example of [[Conjugate Priors]] and the model behind the drunk-friend example, [[Tutorial Week 2]] Q2, Q7, and [[Tutorial Week 4]] Q7.

## Exponential family
$$\binom{n}{x}(1-\theta)^n\exp\!\left\{x\log\frac{\theta}{1-\theta}\right\},$$
which is why a conjugate prior exists — see [[Exponential Family]].

## Jeffreys prior
$\pi_J(\theta)\propto\theta^{-1/2}(1-\theta)^{-1/2}=\text{Beta}(\tfrac12,\tfrac12)$ — see [[Jeffreys Prior]].

## Connections
- **Builds on:** [[Probability Distributions]] · [[Likelihood Function]]
- **Leads to:** [[Beta Distribution]] · [[Conjugate Priors]] · [[Exponential Family]]
- **See also:** [[Conjugate Prior Reference Table]]

## Source
- [[Lecture Week 2.pdf]], slides 7–8, 14
