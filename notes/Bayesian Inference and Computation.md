---
tags: [moc, home]
type: map-of-content
---
# Bayesian Inference and Computation

> [!abstract] Start here
> This is the entry point to the course knowledge graph. Everything is connected: read a note, follow the **Builds on** / **Leads to** links, and the whole course unfolds as one story — *how do we optimally learn from data, and how do we compute the answer when the maths is intractable?*

## The one-paragraph version

We start from a parameter $\theta$ and a prior belief $\pi(\theta)$. We observe data $x$ through a likelihood $L(x\mid\theta)$. [[Bayes Theorem]] turns prior + likelihood into the [[Posterior Distribution]] $\pi(\theta\mid x)$. When the maths is tractable we get [[Conjugate Priors]]; when it is not we approximate the posterior with [[Monte Carlo Integration]] ([[Inversion Sampling]], [[Rejection Sampling]], [[Importance Sampling]]). We then summarise the posterior ([[Posterior Inference]], [[Credible Intervals]], [[Bayesian Predictive Distribution]]) and make decisions with it ([[Posterior Decision Theory]]).

## Course roadmap

| Week | Theme | Core question | Overview |
|---|---|---|---|
| 1 | Foundations & Monte Carlo | What is Bayesian inference, and why sample? | [[Week 1 Overview]] |
| 2 | Priors & inversion sampling | Which priors make the maths easy? How do we draw samples? | [[Week 2 Overview]] |
| 3 | Multivariate models & rejection sampling | What if there are many parameters? | [[Week 3 Overview]] |
| 4 | Decisions, asymptotics & importance sampling | What do we *do* with the posterior? | [[Week 4 Overview]] |

## Concept clusters

### 1. Foundations
- [[Probability Basics]] — conditional probability, total probability, [[Bayes Theorem]]
- [[Frequentist Statistics]] — [[Maximum Likelihood Estimation]], [[Confidence Intervals]], [[Non-regular Likelihoods]]
- [[Bayesian Statistics]] — the philosophical shift: parameters are random
- [[Likelihood Function]] · [[Prior Distribution]] · [[Posterior Distribution]] · [[Bayesian Updating]]

### 2. Inference from the posterior
- [[Posterior Inference]] · [[Credible Intervals]] · [[Bayesian Predictive Distribution]]
- [[Water Consumption Example]] — the running worked example
- [[Normalising Constant]]

### 3. Priors
- [[Conjugate Priors]] ([[Conjugate Prior Reference Table]]) · [[Exponential Family]]
- [[Improper Priors]] · [[Jeffreys Prior]] ([[Fisher Information]])
- [[Mixture Priors]] · [[Prior Predictive Checking]]
- [[Maximum A Posteriori]] — the bridge back to the MLE

### 4. Multivariate models
- [[Multivariate Bayesian Models]] · [[Multivariate Normal Distribution]]
- [[Normal Model with Unknown Mean and Variance]]
- [[Inverse Gamma Distribution]] · [[Wishart Distribution]]

### 5. Monte Carlo computation
- [[Monte Carlo Integration]] (basis: [[Law of Large Numbers]]) · [[Monte Carlo Error]] (basis: [[Central Limit Theorem]])
- [[Inversion Sampling]] (basis: [[Probability Integral Transform]])
- [[Rejection Sampling]]
- [[Importance Sampling]] (diagnostic: [[Effective Sample Size]])

### 6. Using the posterior
- [[Posterior Decision Theory]] · [[Loss Functions]] · [[Posterior Asymptotics]]

## Reference & support
- [[Conjugate Prior Reference Table]] — all conjugate pairs on one page
- [[Probability Distributions]] — index of the distributions used
- [[Glossary]] — every symbol and term in one place
- [[History of Bayesian Computation]] — why this field only took off in the 1990s

## Tutorials
- [[Tutorial Week 1]] · [[Tutorial Week 2]] · [[Tutorial Week 3]] · [[Tutorial Week 4]]

## Source material
- [[Lecture Week 1.pdf]] · [[Lecture Week 2.pdf]] · [[Lecture Week 3.pdf]] · [[Lecture Week 4.pdf]]
- Tutorials: [[Tutorial Week 1.pdf]] · [[Tutorial Week 2.pdf]] · [[Tutorial Week 3.pdf]] · [[Tutorial Week 4.pdf]]

## Suggested learning path

1. Read [[Week 1 Overview]] top to bottom (it is the conceptual spine).
2. Move to [[Week 2 Overview]] and master [[Conjugate Priors]] before touching samplers.
3. [[Week 3 Overview]] generalises everything to many parameters.
4. [[Week 4 Overview]] is about what you *do* with a posterior — decisions and theory.

> [!tip] How to use the links
> Each note has a **Connections** section: *Builds on* (prerequisites), *Leads to* (what comes next), and *See also* (related). Follow *Builds on* backwards if something feels hard.
