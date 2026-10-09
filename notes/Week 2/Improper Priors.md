---
tags: [priors, week-2]
week: 2
type: concept
---

# Improper Priors

> [!abstract] One-line summary
> An improper prior does not integrate to 1 (it integrates to $\infty$), yet it can still yield a perfectly valid proper posterior. It represents "no information".

## Definition
A prior $\pi(\theta)$ is improper if
$$\int\pi(\theta)\,d\theta=\infty\qquad\left(\text{or }\sum_i\pi(\theta_i)\to\infty\text{ for discrete }\theta\right).$$

## How it arises
In the normal model, as the prior variance $d^2\to\infty$ (equivalently $c=1/d^2\to0$),
$$\theta\mid x\sim N\!\left(\bar x,\frac{\sigma^2}{n}\right).$$
The limit prior is $\theta\sim N(b,\infty)$, i.e. $\pi(\theta)\propto1$ — uniform on $\mathbb{R}$. This is improper, since $\int_{\mathbb{R}}\pi(\theta)\,d\theta=\infty$.

## Rules of use
> [!important] Conditions
> - OK to use **as long as the posterior is proper**: $\int\pi(\theta\mid x)\,d\theta<\infty$.
> - If $\int\pi(\theta\mid x)\,d\theta=\infty$, the type of prior **cannot** be used.
> - Small $c$ means weak prior information (very large variance); $c\to0$ is complete uninformativeness.

## Uninformative prior ≠ frequentist inference
It is tempting to think a flat prior returns frequentist inference. Not so:
- Bayesian inference gives a **distribution on $\theta$**; frequentist inference (generally) gives point estimators.
- With $\theta\sim U(0,1)$, $\log\pi(\theta)=0$, so [[Maximum A Posteriori|MAP]] = [[Maximum Likelihood Estimation|MLE]]. But other Bayes estimators (e.g. posterior mean) need not coincide with the MLE.

## The invariance problem
Representing "ignorance" by uniformity of belief does **not** translate across scales. If $\pi(\theta)\propto1$ and $\phi=\theta^2$, then
$$\pi(\phi)=\pi(\theta)\left|\frac{d\theta}{d\phi}\right|\propto\frac{1}{\sqrt\phi},$$
yet ignorance about $\theta$ should mean ignorance about $\phi$ too. This motivates [[Jeffreys Prior]].

## Connections
- **Builds on:** [[Conjugate Priors]] · [[Prior Distribution]]
- **Leads to:** [[Maximum A Posteriori]] · [[Jeffreys Prior]]
- **See also:** [[Normalising Constant]]

## Source
- [[Lecture Week 2.pdf]], slides 21–25
