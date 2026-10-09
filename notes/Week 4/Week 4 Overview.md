---
tags: [moc, week-4]
week: 4
type: map-of-content
---

# Week 4 Overview — Decisions, Asymptotics & Importance Sampling

> [!abstract] Theme
> The [[Posterior Distribution]] *is* the inference — but often we want a point estimate, a decision, or a large-sample shortcut. This week: [[Posterior Decision Theory]] (via [[Loss Functions]]), [[Posterior Asymptotics]], [[Monte Carlo Error]], and [[Importance Sampling]].

## Learning objectives
By the end you should be able to:
- Define a decision problem and pick the optimal decision under a given loss.
- Derive which posterior summary minimises quadratic, absolute, 0–1 and linear loss.
- State the consistency and asymptotic normality of the posterior.
- Quantify and control [[Monte Carlo Error]] using the [[Central Limit Theorem]].
- Implement [[Importance Sampling]] and assess it with [[Effective Sample Size]].

## Path through the material

### 1. From inference to decisions
- [[Posterior Decision Theory]] — a full Bayesian decision problem is (prior, model, loss).
- [[Loss Functions]] — quadratic → mean; absolute → median; 0–1 → mode; linear → quantile.
- Examples: sea walls, baking loaves of bread.

### 2. Large-sample behaviour
- [[Posterior Asymptotics]] — consistency (concentration at $\theta_0$) and asymptotic normality.
- Result: $\theta\mid x\to N(\theta_0, I_n(\theta_0)^{-1})$ regardless of the prior (provided $\pi(\theta_0)\ne0$).
- [[Central Limit Theorem]] — the engine behind Monte Carlo error.

### 3. Monte Carlo precision
- [[Monte Carlo Error]] — $\bar h\sim N(\mu_\text{true}, s_h^2/N)$; choose $N$ for a target precision.
- [[Effective Sample Size]] — the diagnostic for weighted samples.

### 4. Importance sampling
- [[Importance Sampling]] — keep every sample, weight by $f(x)/g(x)$.
- Unnormalised vs normalised estimators (bias for finite $N$).
- Connection back to [[Rejection Sampling]] and [[Monte Carlo Integration]].

## Key equations
$$d^*=\arg\min_d\int_\Theta L(\theta,d)\pi(\theta\mid x)\,d\theta$$
$$\theta\mid x\overset{\text{approx}}{\sim} N(\theta_0, I_n(\theta_0)^{-1})\quad\text{as }n\to\infty$$
$$E_f[h(x)]\approx\frac1N\sum_{i=1}^N w(x^{(i)})h(x^{(i)}),\qquad w(x)=\frac{f(x)}{g(x)},\ x^{(i)}\sim g$$
$$\text{ESS}=\left[\sum_{i=1}^N (W^{(i)})^2\right]^{-1},\qquad 1\le\text{ESS}\le N$$

## Connections
- **Builds on:** [[Week 3 Overview]]

## Source
- [[Lecture Week 4.pdf]] (45 slides)
- [[Tutorial Week 4.pdf]]
