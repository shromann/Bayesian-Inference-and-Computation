---
tags: [multivariate, normal, week-3]
week: 3
type: example
---

# Normal Model with Unknown Mean and Variance

> [!abstract] One-line summary
> When both $\mu$ and $\sigma^2$ are unknown, the posterior factorises as Normal × Inverse-Gamma (or Normal × Inverse-$\chi^2$), and the marginal for $\mu$ is a $t$ distribution.

## Setup
$Y_1,\dots,Y_n\stackrel{iid}{\sim}N(\mu,\sigma^2)$, both unknown. Use independent [[Jeffreys Prior]]s:
$$\pi(\mu,\sigma^2)=\pi_J(\mu)\pi_J(\sigma^2)\propto1\cdot\frac{1}{\sigma^2}.$$
This product form ($\propto1/\sigma^2$) is the conventional improper prior for this model — see the objection to $N3$ in [[Jeffreys Prior]].

## Joint posterior
$$\pi(\mu,\sigma^2\mid y)\propto\sigma^{-(n+2)}\exp\!\left(-\frac{1}{2\sigma^2}\sum_{i=1}^n(y_i-\mu)^2\right)
=\sigma^{-(n+2)}\exp\!\left(-\frac{1}{2\sigma^2}\big[(n-1)s^2+n(\bar y-\mu)^2\big]\right),$$
using $\sum(y_i-\mu)^2=(n-1)s^2+n(\bar y-\mu)^2$ where $s^2=\frac{1}{n-1}\sum(y_i-\bar y)^2$.

## Conditional posterior for $\mu$
$$\pi(\mu\mid\sigma^2,y)\propto\exp\!\left(-\frac{n}{2\sigma^2}(\bar y-\mu)^2\right)\;\Longrightarrow\;\mu\mid\sigma^2,y\sim N(\bar y,\ \sigma^2/n).$$

## Marginal posterior for $\sigma^2$
Integrating out $\mu$:
$$\pi(\sigma^2\mid y)\propto(\sigma^2)^{-(n+1)/2}\exp\!\left(-\frac{(n-1)s^2}{2\sigma^2}\right)
\;\Longrightarrow\;\sigma^2\mid y\sim\text{Inv-}\chi^2(n-1,\ s^2).$$
Equivalently, an [[Inverse Gamma Distribution|Inverse Gamma]]:
$$\sigma^2\mid y\sim\text{InvGamma}\!\left(\frac{n-1}{2},\ \frac{(n-1)s^2}{2}\right).$$

## Marginal posterior for $\mu$
Integrating out $\sigma^2$ (substitute $z=A/(2\sigma^2)$, $A=(n-1)s^2+n(\bar y-\mu)^2$):
$$\pi(\mu\mid y)\propto\left(1+\frac{n(\bar y-\mu)^2}{(n-1)s^2}\right)^{-n/2}\;\Longrightarrow\;\frac{\mu-\bar y}{s/\sqrt n}\;\Big|\;y\ \sim t_{n-1}.$$
So the marginal for $\mu$ is a Student-$t$, not a normal — the extra tails come from uncertainty in $\sigma^2$.

## Sampling and the fully conjugate version
> [!tip] Easy joint sampling
> Because $\pi(\mu,\sigma^2\mid y)=\pi(\mu\mid\sigma^2,y)\,\pi(\sigma^2\mid y)$, draw $\sigma^2\mid y$ first, then $\mu\mid\sigma^2,y$. Normal × Inv-$\chi^2$.

A full conjugate analysis replaces the improper priors with
$$\mu\mid\sigma^2\sim N(\mu_0,\sigma^2/\kappa_0),\qquad\sigma^2\sim\text{Inv-}\chi^2(\nu_0,\sigma_0^2),$$
giving a **Normal–Inv-$\chi^2$** (or **Normal–InvGamma**) joint prior and posterior.

## Connections
- **Builds on:** [[Jeffreys Prior]] · [[Conjugate Priors]] · [[Posterior Inference]]
- **Leads to:** [[Inverse Gamma Distribution]] · [[Multivariate Bayesian Models]]
- **See also:** [[Normal Distribution]] · [[Credible Intervals]] · [[Tutorial Week 4]] Q2

## Source
- [[Lecture Week 3.pdf]], slides 17–23
