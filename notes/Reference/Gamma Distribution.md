---
tags: [distributions, conjugate]
type: distribution
---

# Gamma Distribution

> [!abstract] One-line summary
> A distribution on the positive reals, the conjugate prior for rates (Poisson) and precisions (Normal). Its inverse is the [[Inverse Gamma Distribution|Inverse Gamma]].

## Density
$$\pi(\theta)=\frac{\beta^\alpha}{\Gamma(\alpha)}\theta^{\alpha-1}\exp(-\beta\theta)\propto\theta^{\alpha-1}e^{-\beta\theta},\qquad \alpha,\beta,\theta>0.$$

## Moments
$$\mathbb{E}[\theta]=\frac{\alpha}{\beta},\qquad \text{Var}(\theta)=\frac{\alpha}{\beta^2}.$$

## Conjugate roles
- [[Poisson Distribution|Poisson]] likelihood + $\text{Gamma}(a,b)$ → $\text{Gamma}(a+\sum x_i,\ b+n)$. See [[Water Consumption Example]].
- [[Gamma Distribution|Gamma]] likelihood (known shape) + $\text{Gamma}(a,b)$ → $\text{Gamma}(a+kn,\ b+\sum x_i)$.

## Related
- If $X\sim\text{Gamma}$ then $1/X\sim$ [[Inverse Gamma Distribution|InvGamma]].
- The [[Wishart Distribution]] is the multivariate generalisation.
- The distribution of the **precision** $\tau=1/\sigma^2$ is often taken Gamma, making $\sigma^2$ InvGamma.

## Connections
- **Builds on:** [[Probability Distributions]]
- **Leads to:** [[Conjugate Priors]] · [[Inverse Gamma Distribution]] · [[Wishart Distribution]] · [[Water Consumption Example]]
- **See also:** [[Conjugate Prior Reference Table]] · [[Poisson Distribution]]

## Source
- [[Lecture Week 2.pdf]], slides 9–11
- [[Lecture Week 3.pdf]], slides 19–20
