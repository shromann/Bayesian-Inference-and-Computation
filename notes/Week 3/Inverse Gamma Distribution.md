---
tags: [distributions, conjugate, week-3]
week: 3
type: distribution
---

# Inverse Gamma Distribution

> [!abstract] One-line summary
> If $\sigma^2\sim\text{InvGamma}(a,b)$ then $1/\sigma^2$ is Gamma. It is the conjugate prior for a variance (when the mean is known), and the marginal posterior for $\sigma^2$ in the normal model.

## Density
$$\pi(x\mid a,b)=\frac{b^a}{\Gamma(a)}\left(\frac1x\right)^{a+1}\exp\!\left(-\frac{b}{x}\right),\qquad x>0,\ a>0,\ b>0.$$

## Relation to Gamma
If $X\sim\text{Gamma}$ then $Z=1/X\sim\text{InvGamma}$ (a [[Tutorial Week 3]] question). This mirrors: if precision $\tau\sim\text{Gamma}$, then variance $\sigma^2=1/\tau\sim\text{InvGamma}$.

## Where it appears
- Conjugate prior/posterior for $\sigma^2$ in a [[Normal Distribution|normal]] model with known mean.
- Marginal posterior in [[Normal Model with Unknown Mean and Variance]]:
$$\sigma^2\mid y\sim\text{InvGamma}\!\left(\frac{n-1}{2},\frac{(n-1)s^2}{2}\right).$$
- Multivariate analogue: the [[Wishart Distribution|Inverse Wishart]] for a covariance matrix.

## Connections
- **Builds on:** [[Gamma Distribution]]
- **Leads to:** [[Normal Model with Unknown Mean and Variance]] · [[Wishart Distribution]]
- **See also:** [[Conjugate Prior Reference Table]] · [[Tutorial Week 3]] Q3

## Source
- [[Lecture Week 3.pdf]], slides 19–20
- [[Tutorial Week 3.pdf]], Q3
