---
tags: [reference, distributions]
type: map-of-content
---

# Probability Distributions

> [!abstract] Index
> Every distribution used in the course, with the conjugate role it plays. Follow a link for the density, moments, and where it appears.

## Discrete
- [[Binomial Distribution]] — counts of successes; conjugate prior [[Beta Distribution|Beta]].
- [[Poisson Distribution]] — counts/rates; conjugate prior [[Gamma Distribution|Gamma]].
- [[Negative Binomial Distribution]] — appears as the Poisson–Gamma predictive.

## Continuous
- [[Normal Distribution]] — Gaussian; conjugate prior Normal (known variance).
- [[Beta Distribution]] — on $[0,1]$; conjugate prior for a probability.
- [[Gamma Distribution]] — positive reals; conjugate prior for a rate/precision.
- [[Inverse Gamma Distribution]] — conjugate prior for a variance.
- [[Multivariate Normal Distribution]] — vector Gaussian.
- [[Wishart Distribution]] — matrix-valued; conjugate prior for a precision/covariance matrix.

## Quick conjugate map
| Likelihood | Prior | Posterior |
|---|---|---|
| [[Binomial Distribution]] | [[Beta Distribution]] | Beta |
| [[Poisson Distribution]] | [[Gamma Distribution]] | Gamma |
| [[Normal Distribution]] (known var.) | [[Normal Distribution]] | Normal |
| [[Gamma Distribution]] | [[Gamma Distribution]] | Gamma |
| [[Normal Distribution]] (known mean) | [[Inverse Gamma Distribution]] | InvGamma |
| [[Multivariate Normal Distribution]] | [[Wishart Distribution]] | InvWishart |

See [[Conjugate Prior Reference Table]] for the full parameter updates.

## Connections
- **See also:** [[Likelihood Function]] · [[Conjugate Priors]] · [[Glossary]]

## Source
- [[Lecture Week 2.pdf]], slide 19
- [[Lecture Week 3.pdf]], slides 19–27
