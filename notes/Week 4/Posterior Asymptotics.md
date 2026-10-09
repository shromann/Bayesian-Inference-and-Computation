---
tags: [theory, asymptotics, week-4]
week: 4
type: concept
---

# Posterior Asymptotics

> [!abstract] One-line summary
> As $n\to\infty$ the posterior concentrates at the true value $\theta_0$ (consistency) and becomes normal with variance $I_n(\theta_0)^{-1}$ — regardless of the prior.

## Two results
1. **Consistency (concentration):** if the true value is $\theta_0$ and $\pi(\theta_0)\ne0$ (or non-zero in a neighbourhood), then the posterior probability that $\theta$ is in a neighbourhood of $\theta_0$ tends to 1 as $n\to\infty$.
2. **Asymptotic normality:** as $n\to\infty$,
$$\pi(\theta\mid x)\to N\!\left(\theta_0,\ I_n(\theta_0)^{-1}\right).$$

Both are heuristic/outline arguments assuming a well-specified model ($f(x\mid\theta)$ is the true data-generating process for some $\theta_0$).

## Consistency (sketch)
Write the posterior from i.i.d. data $x_1,\dots,x_n\sim f(x\mid\theta_0)$:
$$\pi(\theta\mid x_1,\dots,x_n)\propto\pi(\theta)\exp\!\big(n\,\ell_n(\theta)\big),\qquad \ell_n(\theta)=\frac1n\sum_{i=1}^n\log f(x_i\mid\theta).$$
By the [[Law of Large Numbers]], $\ell_n(\theta)\to\mathbb{E}[\log f(x\mid\theta)]$ for fixed $\theta$, and
$$\arg\max_\theta \mathbb{E}[\ell_n(\theta)]=\theta_0.$$
Hence for $\theta\ne\theta_0$,
$$\frac{\pi(\theta_0\mid x)}{\pi(\theta\mid x)}\approx\exp\{n(\mathbb{E}[\ell_n(\theta_0)]-\mathbb{E}[\ell_n(\theta)])\}\to\infty,$$
so the posterior mass concentrates on $\theta_0$ (provided $\pi(\theta_0)\ne0$).

## Asymptotic normality (sketch)
Taylor-expand $\mathbb{E}[\ell_n(\theta)]$ about $\theta_0$. The first-order term vanishes (the score is zero at the true value), giving
$$\mathbb{E}[\ell_n(\theta)]\approx\mathbb{E}[\ell_n(\theta_0)]-\frac{1}{2v}(\theta-\theta_0)^2,\qquad v=-1/\mathbb{E}''[\ell_n(\theta_0)]=I(\theta)^{-1}.$$
So
$$\pi(\theta\mid x)\approx\exp\!\left(-\frac{n}{2v}(\theta-\theta_0)^2\right)\;\Longrightarrow\;\theta\mid x\sim N(\theta_0,I_n(\theta_0)^{-1}),$$
where $I_n(\theta)=nI(\theta)$ and $I(\theta)$ is the [[Fisher Information]].

> [!important] Independence of the prior
> The limit holds for **any** prior, as long as $\pi(\theta_0)\ne0$ (or non-zero in a neighbourhood of $\theta_0$). Since $\theta_0$ is unknown in practice, we often substitute the [[Maximum Likelihood Estimation|MLE]] $\hat\theta$.

## Examples
- **Normal, known variance:** $x_i\sim N(\theta,\sigma^2)$ → $I_n(\theta)=n/\sigma^2$ → $\theta\mid x\sim N(\bar X,\sigma^2/n)$.
- **Binomial:** $x\sim\text{Bin}(n,\theta)$ → $I_n(\theta)=n/[\theta(1-\theta)]$ → $\theta\mid x\sim N\!\left(\frac xn,\ \frac{\frac xn(1-\frac xn)}{n}\right)$.

## Connections
- **Builds on:** [[Fisher Information]] · [[Normalising Constant]] · [[Law of Large Numbers]] · [[Bayesian Statistics]]
- **Leads to:** [[Monte Carlo Error]] (CLT parallel) · [[Loss Functions]] (large-sample simplification)
- **See also:** [[Maximum Likelihood Estimation]] · [[Tutorial Week 4]] Q5, Q6

## Source
- [[Lecture Week 4.pdf]], slides 17–25
- [[Tutorial Week 4.pdf]], Q5, Q6
