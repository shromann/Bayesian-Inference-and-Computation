---
tags: [monte-carlo, sampling, week-4]
week: 4
type: concept
---

# Importance Sampling

> [!abstract] One-line summary
> Keep every sample from an easy proposal $g$, but *weight* each by $w=f/g$. Weighted averages under $g$ equal expectations under $f$ — without rejecting anything.

## The idea
A variation on [[Rejection Sampling]] Version 2: instead of accepting/rejecting, keep all $x^{(i)}\sim g(x)$ and weight them so they behave like samples from $f(x)$.

## Algorithm
For $i=1,\dots,N$:
1. Generate $x^{(i)}\sim g(x)$.
2. Give $x^{(i)}$ weight $w^{(i)}\propto\dfrac{f(x^{(i)})}{g(x^{(i)})}$.

The pairs $(x^{(1)},w^{(1)}),\dots,(x^{(N)},w^{(N)})$ are weighted samples from $f$. The weight is $\propto f/g$ (not $f/(Kg)$ as in rejection sampling — $K$ is lost in proportionality).

## Why the weights work
Assuming $\int f=1$ and $w(x)=f(x)/g(x)$,
$$\mathbb{E}_g[w(x)h(x)]=\int \frac{f(x)}{g(x)}h(x)g(x)\,dx=\int h(x)f(x)\,dx=\mathbb{E}_f[h(x)].$$
So a weighted average under $g$ estimates an expectation under $f$.

## Unnormalised target (the common case)
If $f=\tilde f/Z$ with unknown $Z=\int\tilde f$, use weights $\tilde w=\tilde f/g$ and normalise:
$$\mathbb{E}_f[h(x)]\approx\sum_{i=1}^N W(x^{(i)})h(x^{(i)}),\qquad W(x^{(i)})=\frac{\tilde w(x^{(i)})}{\sum_{j=1}^N\tilde w(x^{(j)})}.$$

| Estimator | Formula | Finite-$N$ bias |
|---|---|---|
| Unnormalised | $\frac1N\sum_i w(x^{(i)})h(x^{(i)})$ | unbiased |
| Normalised | $\sum_i W(x^{(i)})h(x^{(i)})$ | biased, asymptotically unbiased |

> [!warning] Why the normalised estimator is biased
> $E(X)/E(Y)\ne E(X/Y)$. The ratio is biased for finite $N$, but converges as $N\to\infty$.

## Efficiency: variability of the weights
- If weights are highly variable, $\text{Var}(w^{(i)})$ is high (bad).
- If weights are similar, $\text{Var}(w^{(i)})$ is small (good).
- To maximise efficiency, choose $g$ to closely match $f$ (equivalently, minimise $\text{Var}(f/g)$).

Measured by the [[Effective Sample Size]]:
$$\text{ESS}=\left[\sum_{i=1}^N (W^{(i)})^2\right]^{-1},\qquad 1\le\text{ESS}\le N.$$

## Worked example
Target $f(x)=20x(1-x)^3$ on $[0,1]$, proposal $g=U(0,1)$:
```r
y <- runif(L); w <- 20*y*(1-y)^3
wTilde <- y*(1-y)^3          # tilde(f)/g
W <- wTilde/sum(wTilde)
# weighted density estimate of f
```
Compare with [[Rejection Sampling]]: same target, but importance sampling uses every sample.

## Estimating the normalising constant
$$\int_\mathcal{X} f(x)\,dx=\int_\mathcal{X}\frac{f(x)}{g(x)}g(x)\,dx\approx\frac1N\sum_i\frac{f(x^{(i)})}{g(x^{(i)})},\qquad x^{(i)}\sim g.$$

## Connections
- **Builds on:** [[Monte Carlo Integration]] · [[Rejection Sampling]] · [[Normalising Constant]]
- **Leads to:** [[Effective Sample Size]] · [[Monte Carlo Error]]
- **See also:** [[Posterior Inference]]

## Source
- [[Lecture Week 4.pdf]], slides 33–45
