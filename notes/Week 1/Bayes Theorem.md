---
tags: [foundations, bayes, week-1]
week: 1
type: concept
---

# Bayes' Theorem

> [!abstract] One-line summary
> Bayes' theorem re-weights a prior belief by the likelihood of the observed data to produce a posterior belief. It is the single equation that defines Bayesian inference.

## Statement
For a parameter $\theta$ and data $x$,
$$\pi(\theta\mid x)=\frac{\Pr(x\mid\theta)\,\pi(\theta)}{\Pr(x)}=\frac{L(x\mid\theta)\,\pi(\theta)}{\displaystyle\int_\Theta L(x\mid\theta)\pi(\theta)\,d\theta}.$$

## The three ingredients
| Symbol | Name | Meaning |
|---|---|---|
| $\pi(\theta)$ | [[Prior Distribution]] | belief about $\theta$ before seeing $x$ |
| $L(x\mid\theta)$ | [[Likelihood Function]] | how well each $\theta$ explains the data |
| $\pi(\theta\mid x)$ | [[Posterior Distribution]] | belief about $\theta$ after seeing $x$ |
| $m(x)=\int L(x\mid\theta)\pi(\theta)\,d\theta$ | [[Normalising Constant]] | makes the posterior integrate to 1 |

Because $m(x)$ does not depend on $\theta$, the working form is
$$\boxed{\pi(\theta\mid x)\propto L(x\mid\theta)\,\pi(\theta)}.$$

## Historical note
Thomas Bayes (1701–1761), in *An Essay towards solving a Problem in the Doctrine of Chances* (1763), gave a special case. It is essentially a conditional-probability statement. See [[History of Bayesian Computation]].

## Where it comes from
Equate the two factorisations of the joint probability:
$$\Pr(A\cap B)=\Pr(A\mid B)\Pr(B)=\Pr(B\mid A)\Pr(A)\;\Longrightarrow\;\Pr(B\mid A)=\frac{\Pr(A\mid B)\Pr(B)}{\Pr(A)}.$$

## Worked example (coloured balls)
Six balls of unknown colour; three drawn without replacement are all black. Let $C_i$ = "$i$ black balls in the bag". With prior $\Pr(C_i)=1/7$,
$$\Pr(C_3\mid A)=\frac{\Pr(A\mid C_3)\Pr(C_3)}{\sum_{i=0}^6\Pr(A\mid C_i)\Pr(C_i)}=\frac{(3/6)(2/5)(1/4)\cdot\frac17}{\frac17[(3/6)(2/5)(1/4)+(4/6)(3/5)(2/4)+(5/6)(4/5)(3/4)+1]}=\frac1{35}.$$
The prior $1/7$ has been updated to $1/35$. Changing the prior changes the answer — see [[Prior Distribution]] and [[Tutorial Week 1]] Q4.

## Connections
- **Builds on:** [[Probability Basics]]
- **Leads to:** [[Bayesian Updating]] · [[Posterior Distribution]] · [[Conjugate Priors]] · [[Normalising Constant]]
- **See also:** [[Bayesian Statistics]] · [[Likelihood Function]]

## Source
- [[Lecture Week 1.pdf]], slides 9–14, 21–24
