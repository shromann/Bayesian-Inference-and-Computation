---
tags: [reference, glossary]
type: reference
---

# Glossary

> [!abstract] Every symbol and key term, with a pointer to the note that develops it.

## Symbols

| Symbol | Meaning | See |
|---|---|---|
| $\theta$ | unknown parameter (vector $\theta=(\theta_1,\dots,\theta_d)$) | [[Prior Distribution]] |
| $\theta_0$ | true data-generating value | [[Posterior Asymptotics]] |
| $x$ | observed data ($x_1,\dots,x_n$) | [[Likelihood Function]] |
| $y$ | future / predictive data | [[Bayesian Predictive Distribution]] |
| $\pi(\theta)$ | prior distribution | [[Prior Distribution]] |
| $L(x\mid\theta)$ | likelihood | [[Likelihood Function]] |
| $\pi(\theta\mid x)$ | posterior distribution | [[Posterior Distribution]] |
| $m(x)$ | normalising constant / marginal likelihood | [[Normalising Constant]] |
| $I(\theta)$ | Fisher information | [[Fisher Information]] |
| $\pi_J(\theta)$ | Jeffreys prior | [[Jeffreys Prior]] |
| $\hat\theta_{\text{MLE}}$ | maximum likelihood estimate | [[Maximum Likelihood Estimation]] |
| $\hat\theta_{\text{MAP}}$ | maximum a posteriori estimate | [[Maximum A Posteriori]] |
| $d$ / $d^*$ | a decision / the optimal decision | [[Posterior Decision Theory]] |
| $L(\theta,d)$ | loss function | [[Loss Functions]] |
| $g(x)$ | proposal / importance density | [[Importance Sampling]] |
| $K$ | rejection-sampling bounding constant | [[Rejection Sampling]] |
| $w$, $W$ | importance weights (unnormalised, normalised) | [[Importance Sampling]] |
| $\tau=1/\sigma^2$ | precision (scalar) | [[Conjugate Priors]] |
| $\Lambda=\Sigma^{-1}$ | precision matrix | [[Multivariate Normal Distribution]] |
| $\bar x$ | sample mean (sufficient statistic for normal mean) | [[Conjugate Priors]] |
| $s^2$ | sample variance | [[Normal Model with Unknown Mean and Variance]] |
| $N$, $N_{\text{rep}}$ | Monte Carlo sample size / replicates | [[Monte Carlo Error]] |
| ESS | effective sample size | [[Effective Sample Size]] |
| HDR | high density region (shortest credible interval) | [[Credible Intervals]] |

## Key terms

- **Prior** — beliefs about $\theta$ before data. [[Prior Distribution]]
- **Conjugate prior** — keeps the posterior in the prior's family. [[Conjugate Priors]]
- **Improper prior** — integrates to $\infty$ but may still give a proper posterior. [[Improper Priors]]
- **Jeffreys prior** — invariant ignorance prior $\propto|I(\theta)|^{1/2}$. [[Jeffreys Prior]]
- **Mixture prior** — weighted combination of conjugates; stays conjugate. [[Mixture Priors]]
- **Posterior** — beliefs about $\theta$ after data; the full inference. [[Posterior Distribution]]
- **Credible interval** — direct-probability interval for $\theta$. [[Credible Intervals]]
- **HDR** — shortest-width credible interval. [[Credible Intervals]]
- **Posterior predictive** — distribution of future data given observed data. [[Bayesian Predictive Distribution]]
- **Prior predictive** — distribution of data implied by the prior alone. [[Prior Predictive Checking]]
- **Loss function** — penalty for a decision at a given $\theta$. [[Loss Functions]]
- **Consistency** — posterior concentrates at $\theta_0$. [[Posterior Asymptotics]]
- **Asymptotic normality** — posterior → $N(\theta_0,I_n(\theta_0)^{-1})$. [[Posterior Asymptotics]]
- **Monte Carlo integration** — integrate by averaging samples. [[Monte Carlo Integration]]
- **Monte Carlo error** — variability of a random estimate. [[Monte Carlo Error]]
- **Inversion sampling** — $x=F^{-1}(u)$. [[Inversion Sampling]]
- **Rejection sampling** — accept from a proposal with probability $f/(Kg)$. [[Rejection Sampling]]
- **Importance sampling** — keep all samples, weight by $f/g$. [[Importance Sampling]]
- **Sample depletion / degeneracy** — a few weights dominate; ESS $\to1$. [[Effective Sample Size]]

## Connections
- **See also:** [[Bayesian Inference and Computation]] · [[Probability Distributions]] · [[Conjugate Prior Reference Table]]
