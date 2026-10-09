---
tags: [moc, week-1]
week: 1
type: map-of-content
---

# Week 1 Overview — Foundations & Monte Carlo

> [!abstract] Theme
> Set up the contrast between [[Frequentist Statistics]] and [[Bayesian Statistics]], derive [[Bayes Theorem]], define the [[Prior Distribution]] and [[Posterior Distribution]], and motivate [[Monte Carlo Integration]].

## Learning objectives
By the end you should be able to:
- Interpret a likelihood, a confidence interval, and a prediction from a frequentist viewpoint.
- State [[Bayes Theorem]] and apply it to the [[Prior Distribution|prior]] → [[Posterior Distribution|posterior]] update.
- Explain why parameters are random in the Bayesian view.
- Explain why posterior quantities are integrals, and how samples approximate them.

## Path through the material

### 1. Probability foundations
- [[Probability Basics]] — conditional probability, law of total probability (marginalisation), and [[Bayes Theorem]].
- [[Likelihood Function]] — $L(x\mid\theta)$; the data is random, $\theta$ is fixed in the classical view.

### 2. The frequentist starting point
- [[Frequentist Statistics]] — the umbrella note.
- [[Maximum Likelihood Estimation]] — $\hat\theta=\arg\max_\theta L(x\mid\theta)$.
- [[Confidence Intervals]] — the awkward "long-run" interpretation.
- [[Non-regular Likelihoods]] — when $\hat\theta\sim N(\theta,H)$ breaks (hospital example).
- [[Bayesian Predictive Distribution]] — why plugging in $\hat\theta$ fails.

### 3. The Bayesian turn
- [[Bayesian Statistics]] — the general "how do we optimally learn?" framing.
- [[Bayes Theorem]] applied with $A=x$, $B=\theta$ gives the posterior.
- [[Bayesian Updating]] — the 4-step recipe.
- [[Prior Distribution]] — beliefs before data; [[Posterior Distribution]] — beliefs after.
- [[Credible Intervals]] — the intuitive replacement for confidence intervals (and HDRs).

### 4. Worked examples
- [[Water Consumption Example]] — Poisson–Gamma conjugate analysis, from likelihood to predictive distribution.
- Coloured balls (see [[Prior Distribution]]) — how the prior changes the answer.

### 5. Monte Carlo
- [[Monte Carlo Integration]] — sample to integrate.
- [[Law of Large Numbers]] — why it works.
- [[Monte Carlo Error]] — how precise is the estimate?
- [[History of Bayesian Computation]] — why this mattered so much.

## Key equations
$$\pi(\theta\mid x)=\frac{L(x\mid\theta)\pi(\theta)}{\int_\Theta L(x\mid\theta)\pi(\theta)\,d\theta}\;\propto\;L(x\mid\theta)\pi(\theta)$$
$$E_\pi[g(\theta)]=\int_\Theta g(\theta)\pi(\theta\mid x)\,d\theta\;\approx\;\frac1N\sum_{i=1}^N g(\theta^{(i)}), \qquad \theta^{(i)}\sim\pi(\theta\mid x)$$

## Connections
- **Leads to:** [[Week 2 Overview]]

## Source
- [[Lecture Week 1.pdf]] (52 slides)
- [[Tutorial Week 1.pdf]]
