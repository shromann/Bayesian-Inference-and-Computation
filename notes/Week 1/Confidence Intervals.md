---
tags: [foundations, frequentist, week-1]
week: 1
type: concept
---

# Confidence Intervals

> [!abstract] One-line summary
> A frequentist confidence interval has a long-run coverage interpretation — not the intuitive "95% chance $\theta$ is inside" — which is awkward and motivates [[Credible Intervals]].

## The interval
A $100(1-\alpha)\%$ confidence interval for a population mean, when the normal model applies:
$$\bar x\pm t_{\alpha/2}\,\frac{s}{\sqrt n}.$$

## The interpretation problem
> [!warning] You cannot say "there is a 95% probability that $\theta$ is in this interval"
> Because $\theta$ is fixed in the frequentist view, any *single* interval either contains $\theta$ (probability 1) or does not (probability 0). The correct statement is: *in the long run, over all experiments, 95% of such intervals contain $\theta$.*

This is the "very awkward" interpretation from the lecture. It is why [[Bayesian Statistics]] is appealing: [[Credible Intervals]] allow the direct probability statement people actually want.

## Coverage picture
Simulate many datasets, form an interval for each — about 95% of them cover the true $\theta$.

## Connections
- **Builds on:** [[Maximum Likelihood Estimation]] · [[Frequentist Statistics]]
- **Leads to:** [[Credible Intervals]]
- **See also:** [[Non-regular Likelihoods]]

## Source
- [[Lecture Week 1.pdf]], slides 6, 26
