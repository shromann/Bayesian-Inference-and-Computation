---
tags: [foundations, likelihood, week-1]
week: 1
type: concept
---

# Likelihood Function

> [!abstract] One-line summary
> The likelihood $L(x\mid\theta)$ is the probability (density) of the observed data as a function of the parameter. It is the data's contribution to the posterior.

## Definition
For independent observations $x_1,\dots,x_n$ from a model with density $f$,
$$L(x\mid\theta)=\prod_{i=1}^n f(x_i\mid\theta).$$

It enters [[Bayes Theorem]] as the factor that re-weights the [[Prior Distribution]]. The model itself encodes prior assumptions about how data are generated.

## The running example
$X_i\sim\text{Poisson}(\theta)$:
$$L(x\mid\theta)=\prod_{i=1}^n\frac{\theta^{x_i}}{x_i!}e^{-\theta}=\frac{\theta^{\sum_i x_i}e^{-n\theta}}{\prod_i x_i!}.$$
This is used in the [[Water Consumption Example]].

## Exponential family form
Many likelihoods can be written as
$$f(x\mid\theta)=h(x)\,g(\theta)\exp\{t(x)\,c(\theta)\}.$$
This special structure is exactly what makes [[Conjugate Priors]] possible — see [[Exponential Family]].

## Key point
$L$ need only be known up to a constant multiple of $\theta$ to run [[Inversion Sampling|Monte Carlo]] algorithms such as [[Rejection Sampling]] and [[Importance Sampling]], because constants cancel in ratios. That is why an unnormalised posterior $\pi(\theta\mid x)\propto L(x\mid\theta)\pi(\theta)$ is enough.

## Connections
- **Builds on:** [[Probability Basics]]
- **Leads to:** [[Posterior Distribution]] · [[Maximum Likelihood Estimation]] · [[Exponential Family]] · [[Fisher Information]]
- **See also:** [[Normalising Constant]]

## Source
- [[Lecture Week 1.pdf]], slides 5, 14
- [[Lecture Week 2.pdf]], slides 7–15
