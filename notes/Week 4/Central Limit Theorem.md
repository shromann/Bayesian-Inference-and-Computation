---
tags: [probability, theorem, week-4]
week: 4
type: concept
---

# Central Limit Theorem

> [!abstract] One-line summary
> The sample mean of i.i.d. variables is approximately normal for large $N$. This gives the sampling distribution of a [[Monte Carlo Integration]] estimator and underpins [[Monte Carlo Error]].

## Statement (informal)
For i.i.d. $X_1,\dots,X_N$ with mean $\mu$ and finite variance $\sigma^2$,
$$\bar X=\frac1N\sum_{i=1}^N X_i\;\approx\;N\!\left(\mu,\frac{\sigma^2}{N}\right)\quad\text{for large }N.$$

## Role in Monte Carlo
Apply it to $h(u^{(i)})$ in [[Monte Carlo Integration]]:
$$\bar h\approx N\!\left(\mu_{\text{true}},\frac{s_h^2}{N}\right).$$
This is the practical tool for choosing $N$ to hit a target precision — see [[Monte Carlo Error]].

## Contrast with the LLN
- [[Law of Large Numbers]]: $\bar X\to\mu$ (consistency of the estimator).
- CLT: *how* it fluctuates around $\mu$ (the $\sim1/\sqrt N$ rate and normality).

## Connections
- **Builds on:** [[Law of Large Numbers]]
- **Leads to:** [[Monte Carlo Error]] · [[Posterior Asymptotics]]
- **See also:** [[Monte Carlo Integration]]

## Source
- [[Lecture Week 4.pdf]], slides 28–29
