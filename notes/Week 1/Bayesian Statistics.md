---
tags: [foundations, bayesian, philosophy, week-1]
week: 1
type: concept
---

# Bayesian Statistics

> [!abstract] One-line summary
> Bayesian statistics treats the unknown parameter as a random variable with a distribution, updating that distribution with data. It is a general answer to the question: *how do we optimally learn?*

## The general question
- $\theta$ — an object (parameter) we wish to learn about.
- $\pi(\theta)$ — current knowledge about $\theta$, in distributional form.
- $x$ — information (data) we observe.
- We want a function $\psi$ such that $\pi(\theta\mid x)=\psi(x,\pi(\theta))$.

Two answers:
1. **Simple option:** [[Bayes Theorem]] (this course).
2. **Modern lens:** optimisation-centric updating (post-Bayesian; see [[Maximum Likelihood Estimation]] and [[Tutorial Week 1]] Q5).

## The conceptual difference
| | Data $x$ | Parameter $\theta$ |
|---|---|---|
| **Frequentist** | random | fixed constant |
| **Bayesian** | random | **random**, $\theta\sim\pi(\theta)$ |

Making $\theta$ random is what allows direct probability statements about it — descriptive inference becomes easy.

## The argument for priors
It is sensible to include prior information, since we invariably have *some* knowledge. Prior knowledge is already used to construct the likelihood model, to set test significance levels, and to weight regressions. Bayesian statistics simply makes the weighting explicit by averaging over the likelihood surface rather than maximising it.

## The argument against
Different priors give different inferences. Whether you see this as a feature or a bug determines your acceptance of the Bayesian approach.

## The 4-step Bayesian recipe
See [[Bayesian Updating]]:
1. Specify a [[Likelihood Function|likelihood model]] $L(x\mid\theta)$.
2. Elicit a [[Prior Distribution]] $\pi(\theta)$.
3. Compute the [[Posterior Distribution]] via [[Bayes Theorem]].
4. Draw inference from the posterior.

## Prior knowledge is unavoidable
Even a "prior-free" analysis assumes things:
- The model (e.g. normal) is a prior choice.
- The significance level is a prior choice.

The honest question is not *whether* to use prior information but *how* — see the coloured-balls and drunk-friend examples in [[Prior Distribution]].

## Connections
- **Builds on:** [[Probability Basics]] · [[Frequentist Statistics]]
- **Leads to:** [[Bayesian Updating]] · [[Prior Distribution]] · [[Posterior Distribution]] · [[Credible Intervals]]
- **See also:** [[History of Bayesian Computation]]

## Source
- [[Lecture Week 1.pdf]], slides 11–20
