---
tags: [decision, loss, week-4]
week: 4
type: concept
---

# Loss Functions

> [!abstract] One-line summary
> Each loss function singles out a different posterior summary as "best": quadratic → mean, absolute → median, 0–1 → mode, linear → quantile.

## The four standard losses for estimating $\theta$
Here $d\in\mathcal{D}=\Theta$ is the estimate $\hat\theta$.

### 1. Quadratic loss — $L(\theta,d)=(\theta-d)^2$
$$\mathbb{E}[L]=\int(\theta-d)^2\pi(\theta\mid x)\,d\theta=\text{Var}(\theta\mid x)+\big(\mathbb{E}(\theta\mid x)-d\big)^2.$$
Minimised at $d=\mathbb{E}(\theta\mid x)$.
> **Posterior mean minimises quadratic loss.** Minimum expected loss = posterior variance.

### 2. Absolute error loss — $L(\theta,d)=|\theta-d|$
This is linear loss with $g=h=1$.
> **Posterior median minimises absolute error loss.**

### 3. 0–1 loss
$$L(\theta,d)=\begin{cases}0&|d-\theta|\le\epsilon\\1&|d-\theta|>\epsilon,\end{cases}\qquad\epsilon\to0.$$
$\mathbb{E}[L]=1-\Pr(|d-\theta|\le\epsilon)$: we choose the highest-probability interval $[d-\epsilon,d+\epsilon]$. Letting $\epsilon\to0$ selects the highest density point.
> **Posterior mode minimises 0–1 loss.**

### 4. Linear loss
$$L(\theta,d)=\begin{cases}g(d-\theta)&d>\theta\\ h(\theta-d)&d<\theta,\end{cases}\qquad g,h>0.$$
The optimum is the $\frac{h}{g+h}$ posterior quantile $q$, i.e. $\frac{h}{g+h}=\int_{-\infty}^q\pi(\theta\mid x)\,d\theta$.
> **Linear loss is minimised at the $\frac{h}{g+h}$ posterior quantile.**

## Worked application (baking bread)
Cost $c$ per loaf, sale price $s>c$, posterior demand $\pi(d\mid x)$, decision $b$ loaves. Relative loss is
$$L(b,d)=\begin{cases}c(b-d)&b>d\quad(\text{surplus})\\ (s-c)(d-b)&b\le d\quad(\text{lost profit}),\end{cases}$$
which is linear loss with $g=c$, $h=s-c$. The optimal stock is
$$b^*=\frac{s-c}{s}\text{ quantile of }\pi(d\mid x).$$

## Connections
- **Builds on:** [[Posterior Decision Theory]] · [[Posterior Inference]]
- **Leads to:** [[Credible Intervals]] (HDR as a 0–1-type decision)
- **See also:** [[Maximum A Posteriori]] · [[Tutorial Week 4]] Q1

## Source
- [[Lecture Week 4.pdf]], slides 5–15
- [[Tutorial Week 4.pdf]], Q1
