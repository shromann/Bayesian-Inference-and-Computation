---
tags: [foundations, frequentist, week-1]
week: 1
type: concept
---

# Frequentist Statistics

> [!abstract] One-line summary
> In the frequentist view the data $x$ is random but the parameter $\theta$ is a fixed unknown constant. Inference is a set of tools — MLE, confidence intervals, tests, predictions — built on that assumption.

## The running example
A forestry commission wants to estimate the proportion $\theta\in[0,1]$ of diseased trees. Model $X\mid\theta\sim\text{Binomial}(n,\theta)$ and maximise the likelihood in $\theta$.

Frequentist inference takes the form of:
- a **point estimate** ($\hat\theta=0.1$);
- a **confidence interval** (95% CI for $\theta$ is $(0.08,1.20)$);
- a **hypothesis test** (reject $H_0:\theta=0.07$ at 5%);
- a **prediction** (15% of trees infected next year);
- a **decision** (how many trees to remove).

## The core assumption
> [!important] Parameter is fixed
> $x\sim N(\theta,1)$: the data is random. But $\theta$ (though unknown) is a *constant*. Probability statements are only ever about the data, never about $\theta$.

This is exactly what [[Bayesian Statistics]] changes.

## Main tools
- [[Maximum Likelihood Estimation]] — the workhorse point estimator.
- [[Confidence Intervals]] — interval estimates with a long-run interpretation.
- [[Non-regular Likelihoods]] — where standard asymptotics fail.
- Prediction by plugging in $\hat\theta$: $y\sim\pi(y\mid\hat\theta)$ — which ignores parameter uncertainty (see [[Bayesian Predictive Distribution]] for the fix).

## Reframing
Frequentist statistics *maximises* the likelihood surface; Bayesian statistics *averages over* it. The [[Prior Distribution|prior]] is the weight used in that averaging — weighting is uncontroversial in frequentist statistics (think weighted regression). See [[Bayesian Statistics]].

## Connections
- **Leads to:** [[Maximum Likelihood Estimation]] · [[Confidence Intervals]] · [[Bayesian Statistics]]
- **See also:** [[Maximum A Posteriori]]

## Source
- [[Lecture Week 1.pdf]], slides 4–8, 20
