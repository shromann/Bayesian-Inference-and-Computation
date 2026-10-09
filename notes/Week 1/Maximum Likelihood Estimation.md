---
tags: [foundations, estimation, week-1, week-2]
week: 1
type: concept
---

# Maximum Likelihood Estimation

> [!abstract] One-line summary
> The MLE $\hat\theta$ is the parameter value that makes the observed data most likely. It is the central frequentist estimator, and its large-sample normality underpins confidence intervals.

## Definition
$$\hat\theta_{\text{MLE}}=\arg\max_\theta L(x\mid\theta)=\arg\max_\theta \log L(x\mid\theta).$$

> [!warning] The likelihood is not a probability of $\theta$
> In $L(x\mid\theta)$, $x$ is the random variable, not $\theta$. $\theta$ is fixed; the "likelihood function" is really a function of $\theta$ for fixed data, even though we write it as if it were a density.

## Properties
- **Consistency:** $\hat\theta_{\text{MLE}}\to\theta_0$.
- **Asymptotic normality:** in many circumstances $\hat\theta\sim N(\theta, H)$ where $H$ comes from the curvature of the log-likelihood. This enables confidence intervals and tests.
- **Invariance:** the MLE of $g(\theta)$ is $g(\hat\theta)$.

## Connection to the posterior
The MLE is the limit of the [[Maximum A Posteriori|MAP]] under a flat prior:
$$\hat\theta_{\text{MAP}}=\arg\max_\theta\{\log L(x\mid\theta)+\log\pi(\theta)\}.$$
With $\pi(\theta)\propto1$, the two coincide. But the Bayesian [[Posterior Distribution|posterior mean]] is generally different from the MLE — see [[Tutorial Week 2]] Q7.

## Information-theoretic view
For large $n$, the MLE is the value of $\theta$ minimising the Kullback–Leibler (KL) divergence between the true distribution and the model. This is the "optimisation-centric" view of learning hinted at in [[Bayesian Statistics]] — see [[Tutorial Week 1]] Q5.

## Non-regular case
When the likelihood is not regular (e.g. $r=0$ successes in $n=47$ trials), $\hat\theta=0$ is still defined but $\hat\theta\sim N(\theta,H)$ fails. See [[Non-regular Likelihoods]].

## Connections
- **Builds on:** [[Likelihood Function]] · [[Frequentist Statistics]]
- **Leads to:** [[Confidence Intervals]] · [[Maximum A Posteriori]] · [[Posterior Asymptotics]]
- **See also:** [[Fisher Information]]

## Source
- [[Lecture Week 1.pdf]], slides 5, 7
- [[Lecture Week 2.pdf]], slide 23
- [[Tutorial Week 1.pdf]], Q5
