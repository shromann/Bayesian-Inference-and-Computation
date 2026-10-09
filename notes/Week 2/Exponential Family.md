---
tags: [priors, theory, week-2]
week: 2
type: concept
---

# Exponential Family

> [!abstract] One-line summary
> Conjugate priors exist (essentially) only for models in the exponential family — a special algebraic form shared by most textbook distributions.

## Definition
A likelihood is in the exponential family if
$$f(x\mid\theta)=h(x)\,g(\theta)\exp\{t(x)\,c(\theta)\}$$
for functions $h,g,t,c$ such that $\int f(x\mid\theta)\,dx=1$.

Includes: Exponential, [[Poisson Distribution|Poisson]], one-parameter [[Gamma Distribution|Gamma]], [[Binomial Distribution|Binomial]], [[Normal Distribution|Normal]] (with known variance).

## Why conjugacy follows
With prior $\pi(\theta)$ and i.i.d. data,
$$\pi(\theta\mid x)\propto\pi(\theta)\,g(\theta)^n\exp\!\Big\{c(\theta)\sum_i t(x_i)\Big\}.$$
Choose a prior of the form
$$\pi(\theta)\propto g(\theta)^d\exp\{b\,c(\theta)\}$$
for some $d,b$. Then
$$\pi(\theta\mid x)\propto g(\theta)^{d+n}\exp\!\Big\{c(\theta)\big[\textstyle\sum_i t(x_i)+b\big]\Big\}
=g(\theta)^{\tilde d}\exp\{\tilde b\,c(\theta)\},$$
which is back in the same family with modified parameters $(\tilde d,\tilde b)$. This is exactly [[Conjugate Priors|conjugacy]].

## Worked construction (Binomial)
$$f(x\mid\theta)=\binom{n}{x}(1-\theta)^n\exp\!\left\{x\log\frac{\theta}{1-\theta}\right\},$$
so $h(x)=\binom nx$, $g(\theta)=(1-\theta)^n$, $t(x)=x$, $c(\theta)=\log\frac{\theta}{1-\theta}$. The conjugate prior must be
$$\pi(\theta)\propto[(1-\theta)^n]^d\exp\!\left\{b\log\frac{\theta}{1-\theta}\right\}=(1-\theta)^{nd-b}\theta^b,$$
which is the [[Beta Distribution|Beta]] family.

## Outside the family
A few non-exponential-family conjugacies exist (e.g. $U(0,\theta)$ likelihood with a Pareto prior), but these are out of scope.

## Connections
- **Builds on:** [[Likelihood Function]] · [[Conjugate Priors]]
- **Leads to:** [[Conjugate Prior Reference Table]]
- **See also:** [[Fisher Information]]

## Source
- [[Lecture Week 2.pdf]], slides 12–14
