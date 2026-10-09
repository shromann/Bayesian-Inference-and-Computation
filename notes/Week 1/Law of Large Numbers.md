---
tags: [probability, theorem, week-1]
week: 1
type: concept
---

# Law of Large Numbers

> [!abstract] One-line summary
> The sample average of i.i.d. variables converges almost surely to their expectation. This is the theoretical justification for [[Monte Carlo Integration]].

## Statement (Strong Law)
Consider a sequence $X_1,X_2,\dots,X_N$ of independent and identically distributed random variables with $\mathbb{E}[X_1]=\mathbb{E}[X_2]=\cdots=\mu$. Then
$$\frac1N\sum_{i=1}^N X_i\to\mu\quad\text{as }N\to\infty,$$
with probability one. In words: the probability that the sample average converges to the expectation is 1.

## Role in Monte Carlo
Take $X_i=g(\theta^{(i)})$ with $\theta^{(i)}\sim\pi(\theta\mid x)$ i.i.d. Then
$$\frac1N\sum_{i=1}^N g(\theta^{(i)})\to\int g(\theta)\pi(\theta\mid x)\,d\theta\quad\text{as }N\to\infty.$$
This makes the Monte Carlo estimator consistent. For *precision* (how fast it converges) we need the [[Central Limit Theorem]], giving [[Monte Carlo Error]].

## Connections
- **Builds on:** [[Probability Basics]]
- **Leads to:** [[Monte Carlo Integration]] · [[Monte Carlo Error]]
- **See also:** [[Central Limit Theorem]]

## Source
- [[Lecture Week 1.pdf]], slide 46
- [[Lecture Week 3.pdf]], slides 29–30
