---
tags: [monte-carlo, sampling, week-2]
week: 2
type: concept
---

# Inversion Sampling

> [!abstract] One-line summary
> The simplest Monte Carlo algorithm: draw $u\sim U(0,1)$ and return $x=F^{-1}(u)$. It needs the inverse CDF in closed form.

## Algorithm
To draw $n$ samples from $F(x)$:
1. Draw $u_1,\dots,u_n\sim U(0,1)$.
2. Set $x_i=F^{-1}(u_i)$.
3. Return $x_1,\dots,x_n$ as i.i.d. samples from $F(x)$.

This is the inverse of the [[Probability Integral Transform]]. It is the natural way to sample from a [[Posterior Distribution|posterior]] you can write down in closed form.

## Worked example 1
$f(x)=3x^2$ on $(0,1)$. Then $F(x)=x^3$. Solve $u=x^3$:
$$x=u^{1/3}\sim f(x).$$
R: `x = runif(5000)^(1/3)`.

## Worked example 2 (piecewise)
$$f(x)=\begin{cases}(x-2)/2&2\le x\le3\\ (2-x/3)/2&3<x\le6\\ 0&\text{otherwise.}\end{cases}$$
The CDF is
$$F(x)=\begin{cases}0&x<2\\ (x-2)^2/4&2\le x\le3\\ 1-\tfrac34(2-x/3)^2&3<x\le6\\ 1&x>6.\end{cases}$$
Inverting on each piece:
$$F^{-1}(u)=\begin{cases}2+2\sqrt u & u\in(0,\tfrac14]\\[2pt] 3\left(2-\sqrt{\tfrac43(1-u)}\right)&u\in(\tfrac14,1).\end{cases}$$
```r
Finv = function(u){
  out = rep(0, length(u))
  ind = (u <= 0.25)
  out[ind]  = 2 + 2*sqrt(u[ind])
  out[!ind] = 6*(1 - sqrt((1-u[!ind])/3))
  out
}
x = Finv(runif(5000))
```

## Limitations
- Needs a closed-form, invertible CDF. For distributions like $\text{Beta}(2,2)$ numerical inversion is inefficient → use [[Rejection Sampling]].
- Does not generalise well to [[Multivariate Bayesian Models|multivariate]] / non-standard posteriors.

## Connections
- **Builds on:** [[Probability Integral Transform]] · [[Monte Carlo Integration]]
- **Leads to:** [[Rejection Sampling]] · [[Importance Sampling]]
- **See also:** [[History of Bayesian Computation]]

## Source
- [[Lecture Week 2.pdf]], slides 36–45
