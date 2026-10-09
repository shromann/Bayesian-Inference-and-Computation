---
tags: [example, conjugate, week-1]
week: 1
type: example
---

# Water Consumption Example

> [!abstract] One-line summary
> The course's running worked example: Melbourne per-capita water use modelled as Poisson, analysed with a Gamma prior, giving a Gamma posterior and a Negative Binomial predictive — all in closed form.

## Setup
Data $x_1,\dots,x_n$ = Melbourne average daily per-capita water use (litres), 1940–2004, $n=65$, $\sum_i x_i=24890$. Model
$$x_i\sim\text{Poisson}(\theta),\quad i=1,\dots,n.$$
Independence and a constant rate $\theta$ are clearly wrong for time series, but they simplify things (returned to later).

## 1. Likelihood
$$L(x\mid\theta)=\prod_{i=1}^n\frac{\theta^{x_i}}{x_i!}e^{-\theta}=\frac{\theta^{\sum_i x_i}e^{-n\theta}}{\prod_i x_i!}\propto\theta^{\sum_i x_i}e^{-n\theta}.$$

## 2. Prior
$$\theta\sim\text{Gamma}(\alpha,\beta),\qquad \pi(\theta)=\frac{\beta^\alpha}{\Gamma(\alpha)}\theta^{\alpha-1}\exp(-\beta\theta)\propto\theta^{\alpha-1}e^{-\beta\theta}.$$

## 3. Posterior (conjugate update)
$$\pi(\theta\mid x)\propto\theta^{\sum_i x_i+\alpha-1}\exp\{-(\beta+n)\theta\}\;\Longrightarrow\;\boxed{\theta\mid x\sim\text{Gamma}\!\left(\alpha+\sum_{i=1}^n x_i,\ \beta+n\right).}$$
See [[Conjugate Priors]] and [[Gamma Distribution]].

## 4. Inference
- Posterior mean: $\dfrac{\alpha+\sum_i x_i}{\beta+n}$.
- Posterior variance: $\dfrac{\alpha+\sum_i x_i}{(\beta+n)^2}$.
- 95% credible interval from the Gamma quantiles.
- Predictive: $p(y\mid x)=\text{NegBin}\!\left(y\mid\alpha+\sum_i x_i,\ \frac{\beta+n}{\beta+n+1}\right)$.

## Prior sensitivity
| Prior | $\alpha$ | $\beta$ | Effect |
|---|---|---|---|
| Moderate | 1 | 0.01 | posterior close to the data |
| Strongly informative | 1 | 10 | posterior pulled toward the prior |

Key lesson: the posterior is directly influenced by the prior; enough data can overwhelm prior information. This is what motivates the different prior types in [[Week 2 Overview]].

## More realistic models
Constant $\theta$ is unrealistic. Alternatives with parameters $(\theta_0,\theta_1)$ (linear trend), $(\theta_0,\theta_1,\theta_2)$ (piecewise linear, known change-point $\kappa$), or $(\theta_0,\theta_1,\theta_2,\kappa)$ (unknown change-point) quickly make the algebra intractable → [[Monte Carlo Integration]].

## Connections
- **Builds on:** [[Bayesian Updating]] · [[Conjugate Priors]]
- **Leads to:** [[Posterior Inference]] · [[Bayesian Predictive Distribution]] · [[Monte Carlo Integration]] · [[Multivariate Bayesian Models]]
- **See also:** [[Gamma Distribution]] · [[Poisson Distribution]] · [[Tutorial Week 1]]

## Source
- [[Lecture Week 1.pdf]], slides 31–40
- [[Tutorial Week 1.pdf]], Q1
