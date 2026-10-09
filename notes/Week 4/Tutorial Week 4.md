---
tags: [tutorial, week-4]
week: 4
type: tutorial
---

# Tutorial Week 4

> [!abstract] Focus
> [[Loss Functions|Loss-based point estimation]], [[Credible Intervals|HDR intervals]], predictives, [[Posterior Asymptotics]], and the Beta–Binomial predictive.

## Q1 — Loss functions for the conjugate normal
Posterior $\theta\mid x\sim N\!\left(\frac{cb+n\tau\bar x}{c+n\tau},\ \frac{1}{c+n\tau}\right)$ (symmetric).
- **Quadratic** → posterior mean $=\frac{cb+n\tau\bar x}{c+n\tau}$.
- **Absolute error** → posterior median = the same value (symmetry).
- **0–1** → posterior mode = the same value (symmetry).
- **Linear** ($g,h$) → the $\frac{h}{g+h}$ quantile $=\text{mean}+\text{sd}\cdot\Phi^{-1}\!\left(\frac{h}{g+h}\right)$.
→ [[Loss Functions]] · [[Conjugate Priors]]

## Q2 — Crop heights, 90% HDR
$n=6$, $\bar x=5.933$, $s\approx0.43$, diffuse prior ($d^2\to\infty$, $c\to0$) ⇒ $\theta\mid x\sim N(\bar x,\ \sigma^2/n)$.
**(a)** $\sigma^2=1$: sd $=\sqrt{1/6}=0.408$; 90% HDR $=\bar x\pm1.645(0.408)=(5.26,\ 6.60)$.
**(b)** Unknown $\sigma^2$, Jeffreys prior: $\frac{\theta-\bar x}{s/\sqrt n}\mid y\sim t_{n-1}$. With $s/\sqrt6=0.176$ and $t_{5,0.95}=2.015$,
$$90\%\text{ HDR}=\bar x\pm2.015(0.176)=(5.58,\ 6.29).$$
→ [[Normal Model with Unknown Mean and Variance]] · [[Credible Intervals]] · [[Jeffreys Prior]]

## Q3 — Weights of items
$N(\theta,4)$, prior $\theta\sim N(110,0.4)$, $n=5$, $\bar x=109.2$. Precisons $c=2.5$, $\tau=0.25$; $c+n\tau=3.75$.
**(a)** $\theta\mid x\sim N(109.73,\ 0.267)$.
**(b)** Predictive for one item: $N(109.73,\ 4+0.267)=N(109.73,\ 4.267)$.
**(c)** For the mean of $m$ further items: $N(109.73,\ 0.267+4/m)$.
**(d)** As $m\to\infty$ the predictive variance $\to0.267$ — the posterior variance of $\theta$.
→ [[Bayesian Predictive Distribution]] · [[Normal Distribution]]

## Q4 — Flaws in artificial fibre
Number of flaws in length $\ell$ is $\text{Poisson}(\ell\theta)$; conjugate prior $\text{Gamma}(p,q)$. With $\ell=(10,15,25,30,40)$ and $x=(3,2,7,6,10)$:
$$\sum x_i=28,\qquad \sum\ell_i=120,\qquad \theta\mid x\sim\text{Gamma}(p+28,\ q+120).$$
Predictive for a fibre of length 60:
$$p(y\mid x)=\text{NegBin}\!\left(y\ \Big|\ a=p+28,\ p=\frac{q+120}{q+180}\right).$$
→ [[Poisson Distribution]] · [[Gamma Distribution]] · [[Bayesian Predictive Distribution]]

## Q5 — Asymptotic posteriors
**(a)** $f(x\mid\theta)=\theta^{x-1}(1-\theta)$ (geometric, $\mathbb{E}[X]=1/(1-\theta)$): $\hat\theta=1-1/\bar x$, $I_n(\theta)=\dfrac{n}{\theta(1-\theta)^2}$, so $\theta\mid x\approx N(\hat\theta,\ I_n(\hat\theta)^{-1})$.
**(b)** $f(x\mid\theta)=e^{-\theta}\theta^x/x!$: $\hat\theta=\bar x$, $I_n(\theta)=n/\theta$ ⇒ $\theta\mid x\approx N(\bar x,\ \bar x/n)$.
→ [[Posterior Asymptotics]] · [[Fisher Information]]

## Q6 — Pareto asymptotic
$f(x\mid b)=b a^b x^{-b-1}$: $\hat b=1/\left[\frac1n\sum\log(x_i/a)\right]$, $I_n(b)=n/b^2$ ⇒ $b\mid x\approx N(\hat b,\ \hat b^2/n)$.
→ [[Posterior Asymptotics]]

## Q7 — Binomial predictive
$x\sim\text{Bin}(n,\theta)$, prior $\text{Beta}(a,b)$, so $\theta\mid x\sim\text{Beta}(a+x,\ b+n-x)$. For $y\mid\theta\sim\text{Bin}(N,\theta)$:
$$f(y\mid x)=\binom Ny\frac{B(y+a+x,\ N-y+b+n-x)}{B(a+x,\ b+n-x)}$$
(the Beta–Binomial distribution).
→ [[Bayesian Predictive Distribution]] · [[Binomial Distribution]] · [[Beta Distribution]]

## Connections
- **See also:** [[Week 4 Overview]] · [[Posterior Decision Theory]] · [[Importance Sampling]]

## Source
- [[Tutorial Week 4.pdf]]
