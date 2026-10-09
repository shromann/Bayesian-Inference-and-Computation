---
tags: [bayesian, workflow, week-1]
week: 1
type: concept
---

# Bayesian Updating

> [!abstract] One-line summary
> The four-step recipe that turns a modelling problem into a posterior distribution: likelihood, prior, Bayes, inference.

## The 4 key steps
1. **Specify a [[Likelihood Function|likelihood model]]** $L(x\mid\theta)$.
2. **Determine/elicit a [[Prior Distribution]]** $\pi(\theta)$.
3. **Compute the [[Posterior Distribution]]** via [[Bayes Theorem]]:
$$\pi(\theta\mid x)=\frac{L(x\mid\theta)\pi(\theta)}{\int_\theta L(x\mid\theta)\pi(\theta)\,d\theta}.$$
4. **Draw inference** (and/or make decisions) from the posterior — see [[Posterior Inference]] and [[Posterior Decision Theory]].

## Prior → posterior, concretely
$$\pi(\theta\mid x)=\psi(x,\pi(\theta))=\frac{L(x\mid\theta)\pi(\theta)}{m(x)}.$$
"Going from $\pi(\theta)$ to $\pi(\theta\mid x)$ reflects how our beliefs about $\theta$ have changed by observing $x$."

## Illustration (regression)
$y=ax+b+\epsilon$, parameters $\theta=(a,b)'$. Prior beliefs about $(a,b)$ are specified as a distribution; after fitting, the result is a *posterior distribution* over $(a,b)$ — still a distribution, not a point. **Parameters are represented by distributions, not point estimates.**

## Connections
- **Builds on:** [[Bayes Theorem]] · [[Prior Distribution]] · [[Likelihood Function]]
- **Leads to:** [[Posterior Distribution]] · [[Posterior Inference]] · [[Water Consumption Example]]
- **See also:** [[Week 1 Overview]]

## Source
- [[Lecture Week 1.pdf]], slides 14–16, 25
- [[Lecture Week 2.pdf]], slide 4
