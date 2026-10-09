---
tags: [tutorial, week-2]
week: 2
type: tutorial
---

# Tutorial Week 2

> [!abstract] Focus
> Deriving posteriors with [[Conjugate Priors]], prior recovery, and a first [[Jeffreys Prior]].

## Q1 — Posterior practice
**(a)** $p(x\mid\theta)=\theta^{x-1}(1-\theta)$ on $x=1,2,\dots$ with $\text{Beta}(p,q)$ prior.
Likelihood $L=\theta^{\sum(x_i-1)}(1-\theta)^n=\theta^{\sum x_i-n}(1-\theta)^n$. Hence
$$\theta\mid x\sim\text{Beta}\!\left(p+\sum_i x_i-n,\ q+n\right).$$
**(b)** $p(x\mid\theta)=e^{-\theta}\theta^x/x!$ (Poisson) with prior $p(\theta)=e^{-\theta}=\text{Gamma}(1,1)$:
$$\theta\mid x\sim\text{Gamma}\!\left(1+\sum_i x_i,\ 1+n\right).$$
→ [[Conjugate Priors]] · [[Poisson Distribution]] · [[Gamma Distribution]]

## Q2 — Defective items
**(a)** $\text{Beta}(2,200)$ prior, $n=100$, $x=3$: posterior $\text{Beta}(2+3,\ 200+100-3)=\text{Beta}(5,297)$.
**(b)** Posterior mean $=4/102$ and variance $=0.0003658$ ⇒ posterior is $\text{Beta}(4,98)$; matching $\text{Beta}(p+3,\ q+97)$ gives $p=q=1$, i.e. a uniform $\text{Beta}(1,1)$ prior.
→ [[Beta Distribution]] · [[Binomial Distribution]] · [[Conjugate Priors]]

## Q3 — Component variability
$x\sim N(\theta,1)$, prior $\theta\sim N(10,0.25)$, $n=12$, $\bar x=31/3$
$$c=1/0.25=4,\quad \tau=1,\quad \theta\mid x\sim N\!\left(\frac{4(10)+12(31/3)}{16},\ \frac1{16}\right)=N(10.25,\ 0.0625).$$
$$\Pr(\theta\ge10)=1-\Phi\!\left(\frac{10-10.25}{0.25}\right)=1-\Phi(-1)=\Phi(1)\approx0.841.$$
→ [[Conjugate Priors]] · [[Normal Distribution]]

## Q4 — Magnetic tape
$X_i\sim\text{Poisson}(\theta)$, prior $\text{Gamma}(3,1)$, $\sum x_i=13$, $n=5$:
$$\theta\mid x\sim\text{Gamma}(3+13,\ 1+5)=\text{Gamma}(16,6).$$
→ [[Conjugate Priors]] · [[Poisson Distribution]]

## Q5 — Remaining conjugate pairs
**(a) Geometric:** $p(x\mid\theta)\propto(1-\theta)^{x-1}\theta$ + $\text{Beta}(p,q)$ → $\text{Beta}(p+n,\ q+\sum x_i-n)$.
**(b) Negative Binomial:** $p(x\mid\theta)\propto\theta^r(1-\theta)^x$ + $\text{Beta}(p,q)$ → $\text{Beta}(p+r,\ q+x)$.
→ [[Conjugate Prior Reference Table]] · [[Exponential Family]]

## Q6 — Jeffreys prior for the geometric
For $p(x\mid\theta)=(1-\theta)^{x-1}\theta$,
$$\log L=(x-1)\log(1-\theta)+\log\theta,\qquad \frac{d^2\log L}{d\theta^2}=-\frac{x-1}{(1-\theta)^2}-\frac1{\theta^2}.$$
With $\mathbb{E}[X]=1/\theta$, the [[Fisher Information]] is
$$I(\theta)=\frac{1}{\theta(1-\theta)}+\frac1{\theta^2}=\frac{1}{\theta^2(1-\theta)}\;\Longrightarrow\;\pi_J(\theta)\propto\theta^{-1}(1-\theta)^{-1/2}.$$
→ [[Jeffreys Prior]] · [[Fisher Information]]

## Q7 — Coin tossing: MLE vs MAP vs posterior mean
$n$ tosses, $x$ heads, uniform prior.
- $\hat\theta_{\text{MLE}}=x/n$.
- Posterior $\text{Beta}(1+x,\ 1+n-x)$ ⇒ $\hat\theta_{\text{MAP}}=\text{mode}=x/n$.
- Posterior mean $=(1+x)/(2+n)$, shrunk slightly toward $1/2$.
→ [[Maximum A Posteriori]] · [[Maximum Likelihood Estimation]] · [[Beta Distribution]]

## Connections
- **See also:** [[Week 2 Overview]] · [[Conjugate Priors]] · [[Jeffreys Prior]]

## Source
- [[Tutorial Week 2.pdf]]
