---
tags: [bayesian, prior, week-1, week-2]
week: 1
type: concept
---

# Prior Distribution

> [!abstract] One-line summary
> The prior $\pi(\theta)$ encodes everything we believe about the parameter *before* seeing the data, in distributional form. It is the most debated and most important modelling choice in Bayesian inference.

## Definition
$\pi(\theta)$ describes our knowledge about the model parameters:
- in distributional form,
- before we have seen the data.

It may be "uninformative" (flat) or based on expert elicitation. Its role in [[Bayes Theorem]] is to weight the [[Likelihood Function]].

## Prior → posterior
Parameters are represented by *distributions*, not point estimates. Fitting a linear regression $y=ax+b+\epsilon$ with $\theta=(a,b)'$:
$$\pi\begin{pmatrix}a\\b\end{pmatrix}=N\!\left(\begin{pmatrix}0\\0\end{pmatrix},\begin{pmatrix}100&0\\0&100\end{pmatrix}\right)\quad\longrightarrow\quad \pi\begin{pmatrix}a\\b\end{pmatrix}\mid x=N(\hat\mu,\hat\Sigma).$$
See [[Bayesian Updating]].

## Do we really have prior knowledge?
Often sensible priors come straight from the model itself:
- **Normal, zero mean, equal variances, zero covariance** for $(a,b)$ — some of these are defensible, some are not. E.g. we *expect* a negative covariance between intercept and slope, so zero covariance is questionable.
- **Same data, different priors:** $X\mid\theta\sim\text{Binomial}(10,\theta)$, observe $x=10$. A drunk friend, a tea-drinker, and a music expert all get 10/10. The data alone forces the same conclusion, but priors $\text{Beta}(10,10)$, $\text{Beta}(10,4)$, $\text{Beta}(10,1)$ encode how surprising each claim is.

## Types of priors
- [[Conjugate Priors]] — posterior stays in the same family.
- [[Improper Priors]] — integrate to $\infty$ but may still give a proper posterior.
- [[Jeffreys Prior]] — invariant to reparameterisation.
- [[Mixture Priors]] — flexible, multimodal beliefs.
- Validate any prior with [[Prior Predictive Checking]].

## The coloured-balls lesson
The posterior answer depends on the prior. With the uniform prior $\Pr(C_i)=1/7$ we got $1/35$; if the manufacturer uses 5 equally likely colours, the prior changes. *We often have to think hard about prior beliefs, and the answer depends on what we believe.* ([[Tutorial Week 1]] Q4.)

## Connections
- **Builds on:** [[Bayesian Statistics]] · [[Bayes Theorem]]
- **Leads to:** [[Posterior Distribution]] · [[Conjugate Priors]] · [[Improper Priors]] · [[Jeffreys Prior]] · [[Mixture Priors]] · [[Prior Predictive Checking]]
- **See also:** [[Maximum A Posteriori]]

## Source
- [[Lecture Week 1.pdf]], slides 14–24
- [[Lecture Week 2.pdf]], slides 4–34
