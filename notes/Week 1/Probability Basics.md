---
tags: [foundations, probability, week-1]
week: 1
type: concept
---

# Probability Basics

> [!abstract] One-line summary
> Three rules — conditional probability, total probability (marginalisation), and Bayes' theorem — are the entire algebraic foundation of Bayesian inference.

## Conditional probability
For events $A$ and $B$ with $\Pr(B)>0$,
$$\Pr(A\mid B)=\frac{\Pr(A,B)}{\Pr(B)}.$$

## Law of total probability (marginalisation)

**Discrete** random variable $B$:
$$\Pr(A)=\sum_i \Pr(A,B_i)=\sum_i \Pr(A\mid B_i)\Pr(B_i).$$

**Continuous** random variable $X$ with density $p(x)$:
$$\Pr(A)=\int \Pr(A\mid X=x)\,p(x)\,dx=\int \Pr(A,x)\,dx.$$

> [!note] Why it matters
> Marginalisation is the operation that removes nuisance parameters. Every time we "integrate out" a parameter to get a [[Posterior Distribution|marginal posterior]], we are applying the law of total probability. See [[Multivariate Bayesian Models]].

## Bayes' theorem
$$\Pr(A\mid B)=\frac{\Pr(B\mid A)\Pr(A)}{\Pr(B)}.$$

This is just conditional probability applied twice: $\Pr(A\cap B)=\Pr(A\mid B)\Pr(B)=\Pr(B\mid A)\Pr(A)$.

## From events to inference
Substituting $A=x$ (observed data) and $B=\theta$ (unknown parameter) turns an event identity into the machinery of [[Bayesian Statistics]]:
$$\pi(\theta\mid x)=\frac{L(x\mid\theta)\pi(\theta)}{m(x)}\;\propto\;L(x\mid\theta)\pi(\theta).$$

## Worked example (categorical Bayes)
Rock strata A and B give fossil probabilities $\Pr(\text{fossil}\mid A)=0.9$, $\Pr(\text{fossil}\mid B)=0.2$, with base rates $\Pr(A)=0.8$, $\Pr(B)=0.2$. If a fossil is present,
$$\Pr(A\mid\text{fossil})=\frac{0.9\times0.8}{0.9\times0.8+0.2\times0.2}=\frac{0.72}{0.76}\approx0.947.$$
This is [[Tutorial Week 1]] question 3.

## Connections
- **Leads to:** [[Bayes Theorem]] · [[Likelihood Function]] · [[Prior Distribution]]
- **See also:** [[Probability Distributions]]

## Source
- [[Lecture Week 1.pdf]], slides 9–14
- [[Tutorial Week 1.pdf]], Q3
