---
tags: [lesson, week-4]
week: 4
type: lesson
---

# Week 4 Lesson Notes

> [!abstract] How to use this note
> A guided walk-through of the Week 4 material, topic by topic, with derivations, intuition, and checkpoint questions. Read alongside [[Week 4 Overview]] and the individual concept notes. Theme: turning the posterior into decisions, large-sample shortcuts, and a sampling method that keeps every draw.

## Teaching order

1. [[#Topic 1 Posterior Decision Theory|Posterior Decision Theory]]
2. [[#Topic 2 Loss Functions|Loss Functions]]
3. [[#Topic 3 Posterior Asymptotics|Posterior Asymptotics]]
4. [[#Topic 4 The Central Limit Theorem and Monte Carlo Error|The CLT and Monte Carlo Error]]
5. [[#Topic 5 Importance Sampling|Importance Sampling]]
6. [[#Topic 6 Effective Sample Size|Effective Sample Size]]

---

# Topic 1: Posterior Decision Theory

## 1.1 Inference vs decision

The posterior $\pi(\theta\mid x)$ is the complete inference about $\theta$. But applications often want:

1. The "best" point estimate $\hat\theta$ — see [[Loss Functions]].
2. The optimal decision $d^*\in\mathcal{D}$.

Examples: how many loaves to bake; how high to build sea walls; how much rail to build.

## 1.2 Loss and expected posterior loss

A loss function $L(\theta,d)$ defines the penalty of decision $d$ when the parameter is $\theta$ (negative loss = gain; utility $U=-L$). If $\theta$ were known, $d^*=\arg\min_d L(\theta,d)$. But $\theta\sim\pi(\theta\mid x)$, so we minimise the **expected posterior loss**:

$$\boxed{d^*=\arg\min_d\mathbb{E}_\pi[L(\theta,d)]=\arg\min_d\int_\Theta L(\theta,d)\,\pi(\theta\mid x)\,d\theta.}$$

## 1.3 A full Bayesian decision problem

> [!important] Three ingredients
> 1. Prior distribution $\pi(\theta)$
> 2. Model $f(x\mid\theta)$ (likelihood $L(x\mid\theta)$)
> 3. Loss function $L(\theta,d)$
>
> Most people stop at the first two; decisions require the third.

## 1.4 Examples

- **Sea walls:** $L(\theta,d_h)=C(h)+K\Pr(\text{wall exceeded in 50y}\mid\theta,h)$ — balance construction cost against failure impact.
- **Baking loaves:** the profit model reduces to **linear loss**, so the optimal stock is a posterior quantile (see next topic).

## Check your understanding

1. What extra ingredient does a decision require beyond the posterior?
2. Write the optimal decision under posterior expected loss.
3. List the three ingredients of a full Bayesian decision problem.

### Answers

1. A loss function $L(\theta,d)$.
2. $d^*=\arg\min_d\int L(\theta,d)\pi(\theta\mid x)\,d\theta$.
3. Prior, model (likelihood), loss.

---

# Topic 2: Loss Functions

## 2.1 The four standard losses

Here $d$ is an estimate $\hat\theta$ of $\theta$.

### 1. Quadratic loss, $L(\theta,d)=(\theta-d)^2$

$$\mathbb{E}[L]=\int(\theta-d)^2\pi(\theta\mid x)\,d\theta=\text{Var}(\theta\mid x)+\big(\mathbb{E}(\theta\mid x)-d\big)^2.$$

Minimised at $d=\mathbb{E}(\theta\mid x)$.

> **Posterior mean minimises quadratic loss.** Minimum expected loss $=$ posterior variance.

### 2. Absolute error loss, $L(\theta,d)=|\theta-d|$

> **Posterior median minimises absolute error loss.**

### 3. 0–1 loss

$$L(\theta,d)=\begin{cases}0&|d-\theta|\le\epsilon\\1&|d-\theta|>\epsilon,\end{cases}\qquad\epsilon\to0.$$

$\mathbb{E}[L]=1-\Pr(|d-\theta|\le\epsilon)$: choose the highest-probability interval $[d-\epsilon,d+\epsilon]$. Letting $\epsilon\to0$ selects the highest-density point.

> **Posterior mode minimises 0–1 loss.**

### 4. Linear loss

$$L(\theta,d)=\begin{cases}g(d-\theta)&d>\theta\\ h(\theta-d)&d<\theta,\end{cases}\qquad g,h>0.$$

The optimum is the $\frac{h}{g+h}$ posterior quantile $q$:

$$\frac{h}{g+h}=\int_{-\infty}^q\pi(\theta\mid x)\,d\theta.$$

> **Linear loss is minimised at the $\frac{h}{g+h}$ posterior quantile.**

## 2.2 Worked application (baking bread)

Cost $c$ per loaf, sale price $s>c$, posterior demand $\pi(d\mid x)$, decision $b$ loaves. Relative loss:

$$L(b,d)=\begin{cases}c(b-d)&b>d\quad(\text{surplus})\\ (s-c)(d-b)&b\le d\quad(\text{lost profit}),\end{cases}$$

linear loss with $g=c$, $h=s-c$. Optimal stock:

$$b^*=\frac{s-c}{s}\ \text{quantile of }\pi(d\mid x).$$

## Check your understanding

1. Show that quadratic loss is minimised at the posterior mean.
2. Which posterior summary minimises each of absolute, 0–1, and linear loss?
3. For the bread problem, at which quantile is the optimal stock?

### Answers

1. $\mathbb{E}[L]=\text{Var}(\theta\mid x)+(\mathbb{E}(\theta\mid x)-d)^2$, which is a non-negative square plus a constant, minimised at $d=\mathbb{E}(\theta\mid x)$.
2. Absolute → median; 0–1 → mode; linear → the $\frac{h}{g+h}$ quantile.
3. The $\frac{s-c}{s}$ quantile.

---

# Topic 3: Posterior Asymptotics

## 3.1 Two results

1. **Consistency (concentration):** if the true value is $\theta_0$ and $\pi(\theta_0)\ne0$, the posterior probability of a neighbourhood of $\theta_0$ tends to 1.
2. **Asymptotic normality:** as $n\to\infty$,

$$\pi(\theta\mid x)\to N\!\left(\theta_0,\ I_n(\theta_0)^{-1}\right),$$

where $I_n(\theta)=nI(\theta)$ and $I(\theta)$ is the [[Fisher Information]].

## 3.2 Consistency (sketch)

Write the posterior from i.i.d. data:

$$\pi(\theta\mid x)\propto\pi(\theta)\exp\!\big(n\,\ell_n(\theta)\big),\qquad \ell_n(\theta)=\frac1n\sum_{i=1}^n\log f(x_i\mid\theta).$$

By the [[Law of Large Numbers]], $\ell_n(\theta)\to\mathbb{E}[\log f(x\mid\theta)]$ for fixed $\theta$, and $\arg\max_\theta\mathbb{E}[\ell_n(\theta)]=\theta_0$. Hence for $\theta\ne\theta_0$,

$$\frac{\pi(\theta_0\mid x)}{\pi(\theta\mid x)}\approx\exp\{n(\mathbb{E}[\ell_n(\theta_0)]-\mathbb{E}[\ell_n(\theta)])\}\to\infty,$$

so the posterior mass concentrates on $\theta_0$.

## 3.3 Asymptotic normality (sketch)

Taylor-expand $\mathbb{E}[\ell_n(\theta)]$ about $\theta_0$. The first-order (score) term vanishes at the true value, leaving

$$\mathbb{E}[\ell_n(\theta)]\approx\mathbb{E}[\ell_n(\theta_0)]-\frac{1}{2v}(\theta-\theta_0)^2,\qquad v=-1/\mathbb{E}''[\ell_n(\theta_0)]=I(\theta)^{-1}.$$

So

$$\pi(\theta\mid x)\approx\exp\!\left(-\frac{n}{2v}(\theta-\theta_0)^2\right)\ \Longrightarrow\ \theta\mid x\sim N\!\left(\theta_0,\ I_n(\theta_0)^{-1}\right).$$

> [!important] Independence of the prior
> The limit holds for **any** prior, as long as $\pi(\theta_0)\ne0$. Since $\theta_0$ is unknown in practice, we often substitute the [[Maximum Likelihood Estimation|MLE]] $\hat\theta$.

## 3.4 Examples

- **Normal, known variance:** $I_n(\theta)=n/\sigma^2\Rightarrow\theta\mid x\sim N(\bar X,\sigma^2/n)$.
- **Binomial:** $I_n(\theta)=n/[\theta(1-\theta)]\Rightarrow\theta\mid x\sim N\!\big(\frac xn,\ \frac{\frac xn(1-\frac xn)}{n}\big)$.
- **Pareto (exam-style):** $\hat b=1/\big[\frac1n\sum\log(x_i/a)\big]$, $I_n(b)=n/b^2\Rightarrow b\mid x\approx N(\hat b,\ \hat b^2/n)$.

## Check your understanding

1. State the two asymptotic results and the key condition on the prior.
2. Why does the prior not matter asymptotically?
3. Write the asymptotic posterior for the Binomial.

### Answers

1. Consistency (posterior concentrates at $\theta_0$) and asymptotic normality $\theta\mid x\to N(\theta_0,I_n(\theta_0)^{-1})$, provided $\pi(\theta_0)\ne0$.
2. The data information $nI(\theta)$ grows with $n$, so it dominates the fixed prior information.
3. $\theta\mid x\approx N\big(\frac xn,\ \frac{\frac xn(1-\frac xn)}{n}\big)$.

---

# Topic 4: The Central Limit Theorem and Monte Carlo Error

## 4.1 The Central Limit Theorem

For i.i.d. $X_1,\dots,X_N$ with mean $\mu$ and finite variance $\sigma^2$,

$$\bar X=\frac1N\sum_{i=1}^N X_i\approx N\!\left(\mu,\frac{\sigma^2}{N}\right)\quad\text{for large }N.$$

> [!note] CLT vs LLN
> The [[Law of Large Numbers]] says $\bar X\to\mu$ (consistency). The [[Central Limit Theorem]] says *how* it fluctuates — normality at rate $1/\sqrt N$.

## 4.2 Monte Carlo error

We estimate $\mu_{\text{true}}=\int_0^1 h(u)\,du$ by $\bar h=\frac1N\sum_i h(u^{(i)})$, $u^{(i)}\sim U(0,1)$. This is random. Two ways to assess it:

1. **Repeated simulation** (easy, poor): repeat and look at spread — too much computation.
2. **Exploit the CLT** (easy, good): for large $N$,

$$\bar h\sim N\!\left(\mu_{\text{true}},\frac{s_h^2}{N}\right),$$

where $s_h$ is the sample standard deviation of the $h(u^{(i)})$.

## 4.3 Choosing the sample size

To estimate $\mu_{\text{true}}$ within $E$ with probability $1-\alpha$, require

$$z_{1-\alpha/2}\frac{s_h}{\sqrt N}\le E\ \Longrightarrow\ N\ge\left(\frac{z_{1-\alpha/2}\,s_h}{E}\right)^2.$$

Example: $E=0.01$ gives $N\ge1356$.

> [!warning] Not the same as a credible interval
> Monte Carlo error measures uncertainty in *our computation*, not uncertainty about $\theta$. The CLT result assumes **independent** samples — it is more complicated for dependent samples (e.g. MCMC, later).

## Check your understanding

1. State the CLT and how it gives the Monte Carlo error.
2. Derive the sample size needed for a target precision.
3. Why is Monte Carlo error conceptually different from a credible interval?

### Answers

1. $\bar X\approx N(\mu,\sigma^2/N)$; applied to $h(u^{(i)})$ gives $\bar h\sim N(\mu_{\text{true}},s_h^2/N)$.
2. Require $z_{1-\alpha/2}s_h/\sqrt N\le E$, so $N\ge(z_{1-\alpha/2}s_h/E)^2$.
3. It measures variability of the *computation*, not uncertainty about the parameter $\theta$.

---

# Topic 5: Importance Sampling

## 5.1 The idea

A variation on [[Rejection Sampling]] Version 2: instead of accepting/rejecting, keep **all** $x^{(i)}\sim g(x)$ and weight them so they behave like samples from $f(x)$.

## 5.2 Algorithm

For $i=1,\dots,N$:

1. Generate $x^{(i)}\sim g(x)$.
2. Give $x^{(i)}$ weight $w^{(i)}\propto\dfrac{f(x^{(i)})}{g(x^{(i)})}$.

The pairs $(x^{(i)},w^{(i)})$ are weighted samples from $f$. (Note the weight is $\propto f/g$, not $f/(Kg)$ — $K$ is lost in proportionality.)

## 5.3 Why the weights work

Assuming $\int f=1$ and $w(x)=f(x)/g(x)$,

$$\mathbb{E}_g[w(x)h(x)]=\int\frac{f(x)}{g(x)}h(x)g(x)\,dx=\int h(x)f(x)\,dx=\mathbb{E}_f[h(x)].$$

A weighted average under $g$ estimates an expectation under $f$.

## 5.4 The unnormalised target (common case)

If $f=\tilde f/Z$ with unknown $Z=\int\tilde f$, use $\tilde w=\tilde f/g$ and normalise:

$$\mathbb{E}_f[h(x)]\approx\sum_{i=1}^N W(x^{(i)})h(x^{(i)}),\qquad W(x^{(i)})=\frac{\tilde w(x^{(i)})}{\sum_{j=1}^N\tilde w(x^{(j)})}.$$

| Estimator | Formula | Finite-$N$ bias |
|---|---|---|
| Unnormalised | $\frac1N\sum_i w(x^{(i)})h(x^{(i)})$ | unbiased |
| Normalised | $\sum_i W(x^{(i)})h(x^{(i)})$ | biased, asymptotically unbiased |

> [!warning] Why the normalised estimator is biased
> $\mathbb{E}(X)/\mathbb{E}(Y)\ne\mathbb{E}(X/Y)$. The ratio is biased for finite $N$, but converges as $N\to\infty$.

## 5.5 Efficiency and estimating the normaliser

- Highly variable weights are bad; similar weights are good. Choose $g$ to closely match $f$ (minimise $\text{Var}(f/g)$).
- The normalising constant can be estimated: $\int_\mathcal{X}f(x)\,dx\approx\frac1N\sum_i\frac{f(x^{(i)})}{g(x^{(i)})}$, $x^{(i)}\sim g$.

Measured by the [[Effective Sample Size]] (next topic).

## Check your understanding

1. What is the importance weight and why are samples kept rather than accepted/rejected?
2. Prove that a weighted average under $g$ estimates an expectation under $f$.
3. When must you use the normalised (self-normalised) estimator, and what is its cost?

### Answers

1. $w=f/g$; keeping all samples and reweighting avoids throwing away draws and works even when the normalising constant of $f$ is unknown.
2. $\mathbb{E}_g[wh]=\int(f/g)hg\,dx=\int hf\,dx=\mathbb{E}_f[h]$.
3. When $f$ is known only up to an unknown constant $Z$; the normalised estimator is biased for finite $N$ (but asymptotically unbiased).

---

# Topic 6: Effective Sample Size

## 6.1 Definition

$$\text{ESS}=\left[\sum_{i=1}^N(W^{(i)})^2\right]^{-1},$$

where $W^{(i)}$ are the normalised [[Importance Sampling|importance weights]].

## 6.2 Range and interpretation

$$1\le\text{ESS}\le N.$$

- $\text{ESS}=1$ when one weight is 1 and the rest 0 — total **sample depletion / weight degeneracy**.
- $\text{ESS}=N$ when $W^{(i)}=1/N$ for all $i$ — perfect.
- Loose interpretation: the equivalent number of equally weighted independent samples.

> [!tip] Design goal
> To maximise ESS, choose the proposal $g$ to closely match the target $f$. The same idea improves [[Rejection Sampling]] efficiency (smaller $K$).

Example (target $\text{Beta}(2,2)$): proposal $\text{Beta}(1,1)$ gives rejection efficiency 0.681 and ESS 4172.82 (84%); proposal $\text{Beta}(1.5,1.5)$ gives efficiency 0.848 and ESS 4634.02 (93%).

## Check your understanding

1. Write the ESS and state its range.
2. What does ESS $=1$ indicate, and what causes it?
3. How do you improve ESS?

### Answers

1. $\text{ESS}=[\sum_i(W^{(i)})^2]^{-1}$, with $1\le\text{ESS}\le N$.
2. Total degeneracy — one sample dominates; caused by a proposal $g$ that poorly matches $f$, so weights are highly variable.
3. Choose $g$ to closely match $f$ (reduces weight variability).

---

## Connections

- **Builds on:** [[Posterior Distribution]] · [[Fisher Information]] · [[Monte Carlo Integration]] · [[Rejection Sampling]]
- **Leads to:** [[Effective Sample Size]] · MCMC (later)
- **See also:** [[Week 4 Overview]] · [[Tutorial Week 4]] · [[Loss Functions]] · [[Posterior Asymptotics]]
