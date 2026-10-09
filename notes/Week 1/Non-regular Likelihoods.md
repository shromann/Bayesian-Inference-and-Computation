---
tags: [foundations, frequentist, week-1]
week: 1
type: concept
---

# Non-regular Likelihoods

> [!abstract] One-line summary
> Sometimes standard likelihood asymptotics ($\hat\theta\sim N(\theta,H)$) fail even in simple models — and the Bayesian posterior gives a clean answer where the frequentist approach becomes tricky.

## The hospital example
Let $\theta=\Pr(\text{death of a baby from an operation})$, $r=$ number of previous deaths, $n=$ number of previous operations. Observed $r=0$, $n=47$, with $r\sim\text{Binomial}(n,\theta)$.

- The MLE $\hat\theta=0$ is well defined.
- But $\hat\theta\sim N(\theta,H)$ **fails** — the estimator sits on the boundary of the parameter space.
- So how do we get a CI or a hypothesis test? Non-standard asymptotics are needed, and they can be tricky.

## The Bayesian fix
Take $\theta\sim U(0,1)$ (an [[Improper Priors|uninformative]] prior). No "standard" asymptotics are required: the [[Posterior Distribution]] $\pi(\theta\mid x)$ contains all required information. Here it is concentrated near 0 but with a proper right tail, giving a sensible interval.

## The prediction problem too
Plugging in $\hat\theta=0$ gives a predictive distribution with a 100% prediction of survival and 0% for death — completely unrealistic. The Bayesian predictive instead draws $\theta\sim\pi(\theta\mid x)$ then $y\sim\text{Bernoulli}(\theta)$, which retains some chance of future deaths. See [[Bayesian Predictive Distribution]].

## Connections
- **Builds on:** [[Maximum Likelihood Estimation]] · [[Frequentist Statistics]]
- **Leads to:** [[Bayesian Statistics]] · [[Bayesian Predictive Distribution]]
- **See also:** [[Credible Intervals]]

## Source
- [[Lecture Week 1.pdf]], slides 7, 8, 28, 29
