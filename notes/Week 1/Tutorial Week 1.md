---
tags: [tutorial, week-1]
week: 1
type: tutorial
---

# Tutorial Week 1

> [!abstract] Focus
> Revision of expectations, the [[Probability Integral Transform]], [[Bayes Theorem]], prior choice, and the information-theoretic view of the [[Maximum Likelihood Estimation|MLE]].

## Q1 — Water consumption ([[Water Consumption Example]])
$X_i\sim\text{Poisson}(\theta)$, prior $\theta\sim\text{Gamma}(\alpha,\beta)$, posterior $\text{Gamma}(\alpha+\sum x_i,\ \beta+n)$. Recall $\Gamma(a+1)=a\Gamma(a)$.

**(a) Posterior mean.** For $\theta\sim\text{Gamma}(a,b)$, $\mathbb{E}[\theta]=a/b$:
$$\mathbb{E}[\theta]=\frac{\alpha+\sum_i x_i}{\beta+n}.$$

**(b) Posterior variance.** $\text{Var}(\theta)=a/b^2$:
$$\text{Var}(\theta)=\frac{\alpha+\sum_i x_i}{(\beta+n)^2}.$$

**(c) Predictive.** With $y\mid\theta\sim\text{Poisson}(\theta)$ and $\theta\mid x\sim\text{Gamma}(a,b)$,
$$p(y\mid x)=\int\text{Poisson}(y\mid\theta)\text{Gamma}(\theta\mid a,b)\,d\theta=\text{NegBin}\!\left(y\ \Big|\ a=\alpha+\sum_i x_i,\ p=\frac{\beta+n}{\beta+n+1}\right).$$
→ [[Gamma Distribution]] · [[Poisson Distribution]] · [[Negative Binomial Distribution]] · [[Bayesian Predictive Distribution]]

## Q2 — Probability integral transform
Show $U=F_X(X)\sim U(0,1)$ by computing its CDF. → [[Probability Integral Transform]]

## Q3 — Rock strata ([[Bayes Theorem]])
$\Pr(\text{fossil}\mid A)=0.9$, $\Pr(\text{fossil}\mid B)=0.2$, $\Pr(A)=0.8$, $\Pr(B)=0.2$.
**(a)** $\Pr(A\mid\text{fossil})=\frac{0.9\cdot0.8}{0.9\cdot0.8+0.2\cdot0.2}=\frac{0.72}{0.76}\approx0.947$, $\Pr(B\mid\text{fossil})\approx0.053$.
**(b)** $\Pr(\text{correct})=\Pr(A,\text{fossil})+\Pr(B,\text{no fossil})=0.72+0.16=0.88$.
→ [[Probability Basics]]

## Q4 — Coloured balls ([[Prior Distribution]])
**(a)** With 5 equally likely colours, each ball is black with probability $1/5$, so $C_i\sim\text{Binomial}(6,\tfrac15)$:
$$\Pr(C_i)=\binom6i\left(\tfrac15\right)^i\left(\tfrac45\right)^{6-i}.$$
**(b)** Posterior of no black balls left = $\Pr(C_3\mid A)$ using this prior and the likelihood of drawing 3 black from $i$ black balls.
**(c)** The change of prior changes the posterior — demonstrating prior sensitivity. → [[Bayes Theorem]]

## Q5 — MLE as KL minimisation
**(a)** For large $n$, $\hat\theta$ minimises $D_{KL}(p_{\text{true}}\,\|\,p(x\mid\theta))$; the MLE maximises $\mathbb{E}[\log p(x\mid\theta)]$ which (since $\mathbb{E}[\log p_{\text{true}}]$ is constant in $\theta$) equals minimising KL.
**(b)** For finite $n$, use the empirical measure $\hat p^n_{\text{true}}=\frac1n\sum_i\delta_{x_i}$, so minimising KL over the empirical distribution recovers the MLE.
→ [[Maximum Likelihood Estimation]] · [[Bayesian Statistics]]

## Connections
- **See also:** [[Week 1 Overview]] · [[Probability Basics]] · [[Water Consumption Example]]

## Source
- [[Tutorial Week 1.pdf]]
