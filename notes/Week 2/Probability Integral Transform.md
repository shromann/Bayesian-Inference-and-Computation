---
tags: [probability, theorem, week-2]
week: 2
type: concept
---

# Probability Integral Transform

> [!abstract] One-line summary
> If $X$ has CDF $F_X$, then $U=F_X(X)$ is uniformly distributed on $[0,1]$. Inverting this fact is the basis of [[Inversion Sampling]].

## Theorem
If $X\sim F_X(x)$, then $F_X(X)\sim U(0,1)$ (when $F_X^{-1}$ exists).

## Proof
Let $U=F_X(X)$. Then $u\in[0,1]$ and
$$F_U(u)=\Pr(U\le u)=\Pr(F_X(X)\le u)=\Pr(X\le F_X^{-1}(u))=F_X(F_X^{-1}(u))=u,$$
which is the CDF of a $U(0,1)$ variable. $\blacksquare$

## Inverted
If $U\sim U(0,1)$ and we set $X=F_X^{-1}(U)$, then $X$ has CDF $F_X$. Check:
$$\Pr(X\le x)=\Pr(F_X^{-1}(U)\le x)=\Pr(U\le F_X(x))=\int_0^{F_X(x)}1\,du=F_X(x).\ \blacksquare$$

This is exactly the algorithm of [[Inversion Sampling]].

## Connections
- **Builds on:** [[Probability Basics]]
- **Leads to:** [[Inversion Sampling]]
- **See also:** [[Tutorial Week 1]] Q2

## Source
- [[Lecture Week 2.pdf]], slides 37–39
- [[Tutorial Week 1.pdf]], Q2
