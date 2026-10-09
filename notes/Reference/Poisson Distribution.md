---
tags: [distributions, discrete]
type: distribution
---

# Poisson Distribution

> [!abstract] One-line summary
> Counts of events in a fixed interval, parameterised by a rate. Its conjugate prior is the [[Gamma Distribution|Gamma]].

## Probability mass function
$$\pi(x\mid\theta)=\frac{\theta^x}{x!}\exp(-\theta),\qquad x=0,1,2,\dots,\ \theta>0.$$

## Likelihood for i.i.d. data
$$L(x\mid\theta)=\prod_{i=1}^n\frac{\theta^{x_i}}{x_i!}e^{-\theta}=\frac{\theta^{\sum_i x_i}e^{-n\theta}}{\prod_i x_i!}.$$

## Conjugate role
$\text{Gamma}(a,b)$ prior → $\text{Gamma}(a+\sum x_i,\ b+n)$ posterior. See [[Conjugate Priors]] and the [[Water Consumption Example]], where daily water use is modelled as $x_i\sim\text{Poisson}(\theta)$.

## Connection to the Negative Binomial
The posterior predictive of the Poisson–Gamma model is a [[Negative Binomial Distribution|Negative Binomial]].

## Connections
- **Builds on:** [[Probability Distributions]] · [[Likelihood Function]]
- **Leads to:** [[Gamma Distribution]] · [[Conjugate Priors]] · [[Water Consumption Example]] · [[Negative Binomial Distribution]]
- **See also:** [[Conjugate Prior Reference Table]]

## Source
- [[Lecture Week 1.pdf]], slides 31–37
- [[Lecture Week 2.pdf]], slides 9–10
