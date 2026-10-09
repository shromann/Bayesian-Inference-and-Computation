---
tags: [distributions, continuous]
type: distribution
---

# Normal Distribution

> [!abstract] One-line summary
> The Gaussian. With known variance its conjugate prior for the mean is Normal; with unknown mean and variance the analysis yields a $t$ marginal.

## Density
$$f(x\mid\theta,\sigma^2)=\frac{1}{\sqrt{2\pi\sigma^2}}\exp\!\left(-\frac{(x-\theta)^2}{2\sigma^2}\right).$$

## Conjugate role (known variance)
$x_1,\dots,x_n\sim N(\theta,\sigma^2)$, $\theta\sim N(b,d^2)$. With precisions $c=1/d^2$, $\tau=1/\sigma^2$:
$$\theta\mid x\sim N\!\left(\frac{cb+n\tau\bar x}{c+n\tau},\ \frac{1}{c+n\tau}\right).$$
Posterior mean is a weighted average of prior mean and $\bar x$; posterior precision = prior precision + $n\times$ data precision; $\bar x$ is sufficient. See [[Conjugate Priors]].

## Unknown mean and variance
See [[Normal Model with Unknown Mean and Variance]]: posterior factorises as Normal × [[Inverse Gamma Distribution|InvGamma]]; marginal for $\mu$ is Student-$t_{n-1}$.

## Asymptotics
[[Posterior Asymptotics]]: $\theta\mid x\to N(\theta_0,\sigma^2/n)$ for any prior with mass near $\theta_0$.

## Connections
- **Builds on:** [[Probability Distributions]]
- **Leads to:** [[Conjugate Priors]] · [[Normal Model with Unknown Mean and Variance]] · [[Multivariate Normal Distribution]]
- **See also:** [[Conjugate Prior Reference Table]] · [[Posterior Asymptotics]]

## Source
- [[Lecture Week 2.pdf]], slides 15–18
- [[Lecture Week 3.pdf]], slides 17–23
- [[Lecture Week 4.pdf]], slide 24
