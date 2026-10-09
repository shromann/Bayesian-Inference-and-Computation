---
tags: [estimation, priors, week-2]
week: 2
type: concept
---

# Maximum A Posteriori

> [!abstract] One-line summary
> The MAP estimate is the posterior mode. It is the Bayesian point estimate that coincides with the MLE when the prior is flat.

## Definition
$$\hat\theta_{\text{MAP}}=\arg\max_\theta\log\pi(\theta\mid x)=\arg\max_\theta\big\{\log L(x\mid\theta)+\log\pi(\theta)\big\}.$$

Compare the [[Maximum Likelihood Estimation|MLE]]: $\hat\theta_{\text{MLE}}=\arg\max_\theta\log L(x\mid\theta)$.

## The bridge
$\hat\theta_{\text{MAP}}$ is the MLE plus a penalty $\log\pi(\theta)$ — a form of regularisation. With a flat/uninformative prior $\theta\sim U(0,1)$, $\log\pi(\theta)=0$, so
$$\hat\theta_{\text{MAP}}=\hat\theta_{\text{MLE}}.$$

## But Bayes gives more
Bayesian inference also provides the posterior mean, median, and mode. These need not coincide with the MLE. Which one to report depends on the [[Loss Functions|loss function]] — see [[Posterior Decision Theory]].

## Connections
- **Builds on:** [[Improper Priors]] · [[Posterior Distribution]] · [[Maximum Likelihood Estimation]]
- **Leads to:** [[Loss Functions]] · [[Posterior Decision Theory]]
- **See also:** [[Tutorial Week 2]] Q7 (compare MAP, MLE, posterior mean under a uniform prior)

## Source
- [[Lecture Week 2.pdf]], slide 23
