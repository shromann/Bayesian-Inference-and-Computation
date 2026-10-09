---
tags: [monte-carlo, computation, week-1, week-4]
week: 4
type: concept
---

# Monte Carlo Error

> [!abstract] One-line summary
> Estimating a quantity with random samples gives a random estimate. The variability of that estimate is the Monte Carlo error — and the CLT lets us control it.

## The problem
We estimate $\mu_{\text{true}}=\int_0^1 h(u)\,du$ by
$$\bar h=\frac1N\sum_{i=1}^N h(u^{(i)}),\qquad u^{(i)}\sim U(0,1).$$
This is random. How variable is it, and how do we choose $N$?

## Two approaches
1. **Repeated simulation** (easy, poor): repeat the whole experiment $N_{\text{rep}}$ times and look at spread. Easy to obtain but far too much computation.
2. **Exploit the CLT** (easy, good): for large $N$,
$$\bar h\sim N\!\left(\mu_{\text{true}},\frac{s_h^2}{N}\right),$$
where $s_h$ is the sample standard deviation of the $h(u^{(i)})$.

## Choosing the sample size
Want to estimate $\mu_{\text{true}}$ to within $E$ with probability $1-\alpha$. Require
$$z_{1-\alpha/2}\frac{s_h}{\sqrt N}\le E\quad\Longrightarrow\quad N\ge\left(\frac{z_{1-\alpha/2}\,s_h}{E}\right)^2.$$
Example: $E=0.01$ gives $N\ge1356$. This is the Monte Carlo analogue of a classical sample-size calculation.

## Cautions
> [!warning] Not the same as a credible interval
> Monte Carlo error measures uncertainty in *our computation*, not uncertainty about $\theta$. Reporting posterior estimates is commonly accompanied by (estimates of) Monte Carlo error.
> The CLT result assumes **independent** samples. It is more complicated for dependent samples (e.g. MCMC, later).

## Connections
- **Builds on:** [[Monte Carlo Integration]] · [[Central Limit Theorem]] · [[Law of Large Numbers]]
- **Leads to:** [[Importance Sampling]] · [[Effective Sample Size]]
- **See also:** [[Credible Intervals]]

## Source
- [[Lecture Week 1.pdf]], slides 50–51
- [[Lecture Week 4.pdf]], slides 27–29
