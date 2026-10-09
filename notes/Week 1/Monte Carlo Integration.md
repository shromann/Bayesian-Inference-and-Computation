---
tags: [monte-carlo, computation, week-1, week-3]
week: 1
type: concept
---

# Monte Carlo Integration

> [!abstract] One-line summary
> "Monte Carlo" = integration using random numbers: approximate an integral by an average over samples. It turns intractable posterior integrals into a routine computation.

## The idea
Posterior quantities are expectations (integrals). If we can sample $\theta^{(1)},\dots,\theta^{(N)}\sim\pi(\theta\mid x)$, then
$$E_\pi[g(\theta)]=\int_\Theta g(\theta)\pi(\theta\mid x)\,d\theta\;\approx\;\frac1N\sum_{i=1}^N g(\theta^{(i)}).$$

Examples:
- Posterior mean $\approx\frac1N\sum_i\theta^{(i)}$.
- Probabilities: $\Pr(\theta<-1)\approx\frac1N\sum_i\mathbb{I}(\theta^{(i)}<-1)$ (indicator is just a function $g$).

## Why it works
Approximate the posterior by the discrete measure
$$\pi(\theta\mid x)\approx\frac1N\sum_{i=1}^N\delta_{\theta^{(i)}}(\theta),$$
where $\delta_b(A)=1$ if $b\in A$ and $0$ otherwise. Then
$$E_\pi[g(\theta)]\approx\int g(\theta)\frac1N\sum_i\delta_{\theta^{(i)}}(\theta)\,d\theta=\frac1N\sum_i g(\theta^{(i)}).$$
Rigorous justification is the [[Law of Large Numbers]].

## Multivariate Monte Carlo
- **Marginal distributions:** if $(\theta_1^{(i)},\theta_2^{(i)})\sim\pi(\theta_1,\theta_2\mid x)$, then discarding the $\theta_2$ values gives samples from $p(\theta_1\mid x)$.
- **Functions of parameters:** compute $\theta_1^{(i)}-\theta_2^{(i)}$ and histogram — no Jacobian needed.
- **Predictive distributions:** sample $\theta^{(i)}$, then $y^{(i)}\sim\pi(y\mid\theta^{(i)})$, discard $\theta^{(i)}$. See [[Bayesian Predictive Distribution]].

## Integration over arbitrary ranges
| Range | Trick |
|---|---|
| $\int_0^1 g$ | $U\sim U(0,1)$, average $g(u)$ |
| $\int_a^b g$ | transform $u=(x-a)/(b-a)$ or simulate $U(a,b)$, multiply by $(b-a)$ |
| $\int_0^\infty g$ | substitute $u=1/(x+1)$ |
| multivariate | straightforward; the same average works |

## Cost and benefit
> [!tip] Why Monte Carlo is so useful
> The approach is remarkably easy to use even in high dimensions (no curse of dimensionality for the *method* itself). The price is high variance. Techniques to improve precision include [[Importance Sampling]].

## Connections
- **Builds on:** [[Posterior Distribution]] · [[Law of Large Numbers]]
- **Leads to:** [[Monte Carlo Error]] · [[Inversion Sampling]] · [[Rejection Sampling]] · [[Importance Sampling]] · [[Bayesian Predictive Distribution]]
- **See also:** [[Posterior Inference]] · [[Multivariate Bayesian Models]]

## Source
- [[Lecture Week 1.pdf]], slides 42–51
- [[Lecture Week 3.pdf]], slides 29–37
- [[Lecture Week 4.pdf]], slides 27–29, 45
