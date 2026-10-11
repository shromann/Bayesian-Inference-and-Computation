---
tags: [lesson, week-3]
week: 3
type: lesson
---

# Week 3 Lesson Notes

> [!abstract] How to use this note
> A guided walk-through of the Week 3 material, topic by topic, with derivations, intuition, and checkpoint questions. Read alongside [[Week 3 Overview]] and the individual concept notes. Theme: scaling the Bayesian machinery to many parameters, flexible priors, and a second sampler.

## Teaching order

1. [[#Topic 1 Flexible Priors Mixture Priors and Prior Predictive Checking|Flexible Priors: Mixtures and Prior Predictive Checking]]
2. [[#Topic 2 Multivariate Bayesian Models|Multivariate Bayesian Models]]
3. [[#Topic 3 The Multivariate Conjugate Toolkit|The Multivariate Conjugate Toolkit]] (Multivariate Normal, Wishart, Inverse Gamma)
4. [[#Topic 4 The Normal Model with Unknown Mean and Variance|The Normal Model with Unknown Mean and Variance]]
5. [[#Topic 5 Rejection Sampling|Rejection Sampling]]

---

# Topic 1: Flexible Priors: Mixture Priors and Prior Predictive Checking

## 1.1 Why standard conjugate priors are too rigid

[[Conjugate Priors]] are convenient but may not capture prior beliefs. **Example: spinning a coin** on a table. Tossing suggests $p\approx0.5$, but spinning can favour $0.4$ or $0.6$ because of edge imperfections. The belief is **bimodal or trimodal** — a single [[Beta Distribution|Beta]] cannot represent it.

## 1.2 Mixture priors ([[Mixture Priors]])

If $\pi_1(\theta),\dots,\pi_k(\theta)$ are all conjugate priors giving posteriors $\pi_i(\theta\mid x)$, take

$$\pi(\theta)=\sum_{i=1}^k w_i\,\pi_i(\theta),\qquad \sum_{i=1}^k w_i=1.$$

Then

$$\pi(\theta\mid x)=\frac{\sum_i w_i\pi_i(\theta)L(x\mid\theta)}{m(x)}=\sum_{i=1}^k w_i^*\,\pi_i(\theta\mid x),$$

where the updated weights are

$$w_i^*=\frac{w_i\,m_i(x)}{m(x)},\qquad m(x)=\sum_{i=1}^k w_i\,m_i(x),\qquad \sum_i w_i^*=1.$$

> [!important] Closure
> The posterior is a **mixture of the same conjugate family**. The data update the **weights**: component $i$ gains weight in proportion to its marginal likelihood $m_i(x)$. This is the same machinery as **model comparison / Bayes factors**.

## 1.3 Prior predictive checking ([[Prior Predictive Checking]])

The **prior predictive** is

$$\pi(y)=\int\pi(y\mid\theta)\,\pi(\theta)\,d\theta,$$

the distribution of data implied by the prior alone. Procedure:

1. Sample from $\pi(y)$ for your chosen $\pi(\theta)$.
2. Check whether $\pi(y)$ represents plausible data.
3. If not, modify $\pi(\theta)$ and repeat.

> [!warning] Use it before the real data
> Do not use the upcoming analysis data to inform this decision — otherwise it is no longer a *prior* check.

**Worked example (rare genetic disorder).** $\theta\sim\text{Beta}(\alpha,\beta)$ = probability an individual has the disorder; $X\mid\theta\sim\text{Binomial}(n,\theta)$. For a single future individual $y\in\{0,1\}$:

$$\Pr(y=1)\propto\int\theta\,\theta^{\alpha-1}(1-\theta)^{\beta-1}\,d\theta=B(\alpha+1,\beta),\qquad B(a,b)=\frac{\Gamma(a)\Gamma(b)}{\Gamma(a+b)}.$$

| Prior | Analytic $\Pr(y=0)$ | MC $\Pr(y=0)$ |
|---|---|---|
| $\text{Beta}(1,1)$ | 0.5 | 0.496 |
| $\text{Beta}(1,25)$ | 0.038 | 0.039 |

$\text{Beta}(1,1)$ implies a 50–50 chance of a *rare* disorder — implausible. $\text{Beta}(1,25)$ is more realistic.

## Check your understanding

1. Why might a conjugate prior be too restrictive, and how do mixtures fix this?
2. Write the mixture posterior and identify the updated weights.
3. What is the prior predictive and how is it used?

### Answers

1. It cannot express multimodal beliefs; a mixture of conjugates can while remaining conjugate.
2. $\pi(\theta\mid x)=\sum_i w_i^*\pi_i(\theta\mid x)$ with $w_i^*=w_i m_i(x)/m(x)$, $m(x)=\sum_i w_i m_i(x)$.
3. $\pi(y)=\int\pi(y\mid\theta)\pi(\theta)\,d\theta$; simulate from it and check whether the implied data are plausible, adjusting the prior if not.

---

# Topic 2: Multivariate Bayesian Models

## 2.1 The general recipe

For a parameter vector $\theta=(\theta_1,\dots,\theta_d)$,

$$\pi(\theta\mid x)\propto L(x\mid\theta)\,\pi(\theta),$$

identical in form to the univariate case. This is where Bayesian methods often become *easier* than classical ones (no profiling, no asymptotic approximation needed).

## 2.2 Marginal distributions

To infer $\theta_1$ when the rest are nuisance,

$$\pi(\theta_1\mid x)=\int_{\Theta_d}\cdots\int_{\Theta_2}\pi(\theta\mid x)\,d\theta_2\cdots d\theta_d.$$

Do this (a) algebraically or (b) by [[Monte Carlo Integration|Monte Carlo simulation]] (sample from the joint, discard the rest).

## 2.3 The three challenges

1. **Prior specification** — multivariate priors involve dependencies and are hard to elicit.
2. **Computation** — integrals are harder; need samplers beyond [[Inversion Sampling]].
3. **Interpretation** — posterior structure is more complex.

## 2.4 Worked examples

- **Discrete (machine quality, Tutorial Q1).** Finite $\theta$, so the joint posterior is just a normalised table: multiply likelihood × prior entrywise, normalise, and sum rows/columns for marginals.
- **Poisson decomposition.** $Y_1\sim\text{Poisson}(\alpha\beta)$, $Y_2\sim\text{Poisson}((1-\alpha)\beta)$ independent given $(\alpha,\beta)$; prior $\alpha\sim\text{Beta}(p,q)$, $\beta\sim\text{Gamma}(p+q,1)$ independent:
  $$\alpha\mid y_1,y_2\sim\text{Beta}(y_1+p,\ y_2+q),\qquad \beta\mid y_1,y_2\sim\text{Gamma}(y_1+y_2+p+q,\ 2).$$
  The joint posterior **factorises**, so sampling is easy: first $\alpha$, then $\beta$.

## Check your understanding

1. Write the multivariate posterior and the marginal for $\theta_1$.
2. Name the three new challenges of multivariate inference.
3. In the Poisson decomposition, why is sampling easy?

### Answers

1. $\pi(\theta\mid x)\propto L(x\mid\theta)\pi(\theta)$; $\pi(\theta_1\mid x)=\int\cdots\int\pi(\theta\mid x)\,d\theta_2\cdots d\theta_d$.
2. Prior specification, computation, interpretation.
3. Because the joint posterior factorises into independent $\alpha$ and $\beta$ posteriors, so we can draw them sequentially.

---

# Topic 3: The Multivariate Conjugate Toolkit

## 3.1 The analogy table

| Univariate (scalar)                                         | Multivariate |                                                              |              |     |
| ----------------------------------------------------------- | ------------ | ------------------------------------------------------------ | ------------ | --- |
| precision $\tau$, conjugate [[Gamma Distribution            | Gamma]]      | precision matrix $\Lambda$, conjugate [[Wishart Distribution | Wishart]]    |     |
| variance $\sigma^2$, conjugate [[Inverse Gamma Distribution | InvGamma]]   | covariance $\Sigma$, conjugate [[Wishart Distribution        | InvWishart]] |     |

## 3.2 Multivariate normal ([[Multivariate Normal Distribution]])

$$f(x\mid\mu,\Sigma)=\frac{1}{(2\pi)^{d/2}|\Sigma|^{1/2}}\exp\!\left(-\tfrac12(x-\mu)^T\Sigma^{-1}(x-\mu)\right),$$

with precision matrix $\Lambda=\Sigma^{-1}$ (analogous to $\tau=1/\sigma^2$). When $\Sigma$ is **known**, the conjugate prior for $\mu$ is $N_d(\mu_0,\Sigma_0)$ and the posterior is $N_d(\hat\mu,\hat\Sigma)$ with

$$\hat\mu=(\Sigma_0^{-1}+n\Sigma^{-1})^{-1}(\Sigma_0^{-1}\mu_0+n\Sigma^{-1}\bar x),\qquad \hat\Sigma=(\Sigma_0^{-1}+n\Sigma^{-1})^{-1}.$$

This is the direct analogue of the univariate Normal–Normal update (precision-weighted average, precisions add).

## 3.3 Inverse Gamma ([[Inverse Gamma Distribution]])

$$\pi(x\mid a,b)=\frac{b^a}{\Gamma(a)}\left(\frac1x\right)^{a+1}\exp\!\left(-\frac bx\right),\qquad x>0.$$

If $X\sim\text{Gamma}$ then $1/X\sim\text{InvGamma}$. It is conjugate for a variance (known mean) and is the marginal posterior for $\sigma^2$ in the [[Normal Model with Unknown Mean and Variance]].

## 3.4 Wishart and Inverse Wishart ([[Wishart Distribution]])

$$\pi(\Lambda\mid v,A)=\frac{|A|^v}{\Gamma_d(v)}|\Lambda|^{v-(d+1)/2}\exp[-\operatorname{tr}(A\Lambda)],\qquad \pi(\Sigma\mid v,A)\ \text{(Inverse Wishart)}.$$

When $d=1$ these reduce to Gamma and Inverse Gamma. With known $\mu$ and prior $\Sigma\sim IW_d(v,A)$:

$$\hat v=v+\frac n2,\qquad \hat A=A+\frac12\sum_{i=1}^n(x_i-\mu)(x_i-\mu)^\top.$$

## Check your understanding

1. Give the multivariate analogues of Gamma and Inverse Gamma.
2. State the posterior for $\mu$ when $\Sigma$ is known.
3. What are the posterior parameters when $\Sigma\sim IW_d(v,A)$ and $\mu$ is known?

### Answers

1. Wishart (for precision) and Inverse Wishart (for covariance).
2. $N_d(\hat\mu,\hat\Sigma)$ with the precision-weighted $\hat\mu$ and $\hat\Sigma=(\Sigma_0^{-1}+n\Sigma^{-1})^{-1}$.
3. $\hat v=v+\frac n2$ and $\hat A=A+\frac12\sum_i(x_i-\mu)(x_i-\mu)^\top$.

---

# Topic 4: The Normal Model with Unknown Mean and Variance

## 4.1 Setup

$Y_1,\dots,Y_n\stackrel{iid}{\sim}N(\mu,\sigma^2)$, both unknown. Use independent [[Jeffreys Prior]]s:

$$\pi(\mu,\sigma^2)=\pi_J(\mu)\pi_J(\sigma^2)\propto1\cdot\frac{1}{\sigma^2}.$$

(The product form $1/\sigma^2$ is the conventional improper prior — recall the factorisation objection to $N3$ in [[Jeffreys Prior]].)

## 4.2 Joint posterior

$$\pi(\mu,\sigma^2\mid y)\propto\sigma^{-(n+2)}\exp\!\left(-\frac{1}{2\sigma^2}\sum_{i=1}^n(y_i-\mu)^2\right)=\sigma^{-(n+2)}\exp\!\left(-\frac{1}{2\sigma^2}\big[(n-1)s^2+n(\bar y-\mu)^2\big]\right),$$

using $\sum(y_i-\mu)^2=(n-1)s^2+n(\bar y-\mu)^2$ with $s^2=\frac{1}{n-1}\sum(y_i-\bar y)^2$.

## 4.3 Conditional posterior for $\mu$

$$\pi(\mu\mid\sigma^2,y)\propto\exp\!\left(-\frac{n}{2\sigma^2}(\bar y-\mu)^2\right)\ \Longrightarrow\ \mu\mid\sigma^2,y\sim N(\bar y,\ \sigma^2/n).$$

## 4.4 Marginal posteriors

**For $\sigma^2$** (integrate out $\mu$):

$$\pi(\sigma^2\mid y)\propto(\sigma^2)^{-(n+1)/2}\exp\!\left(-\frac{(n-1)s^2}{2\sigma^2}\right)\ \Longrightarrow\ \sigma^2\mid y\sim\text{Inv-}\chi^2(n-1,\ s^2).$$

Equivalently $\sigma^2\mid y\sim\text{InvGamma}\big(\frac{n-1}{2},\ \frac{(n-1)s^2}{2}\big)$.

**For $\mu$** (integrate out $\sigma^2$; substitute $z=A/(2\sigma^2)$, $A=(n-1)s^2+n(\bar y-\mu)^2$):

$$\pi(\mu\mid y)\propto\left(1+\frac{n(\bar y-\mu)^2}{(n-1)s^2}\right)^{-n/2}\ \Longrightarrow\ \frac{\mu-\bar y}{s/\sqrt n}\,\Big|\,y\ \sim t_{n-1}.$$

> [!important] The marginal for $\mu$ is Student-$t$, not normal
> The heavier tails come from the extra uncertainty in $\sigma^2$. This is exactly why HDR intervals widen when we stop pretending $\sigma^2$ is known (see [[Tutorial Week 4]] Q2).

## 4.5 Easy joint sampling

Because $\pi(\mu,\sigma^2\mid y)=\pi(\mu\mid\sigma^2,y)\,\pi(\sigma^2\mid y)$, draw $\sigma^2\mid y$ first, then $\mu\mid\sigma^2,y$ (a Normal × Inverse-$\chi^2$ pair).

A full conjugate analysis replaces the improper priors with

$$\mu\mid\sigma^2\sim N(\mu_0,\sigma^2/\kappa_0),\qquad\sigma^2\sim\text{Inv-}\chi^2(\nu_0,\sigma_0^2),$$

a **Normal–Inv-$\chi^2$** (or Normal–InvGamma) prior/posterior.

## Check your understanding

1. Which improper prior is conventional here and why that form?
2. Derive the conditional posterior $\pi(\mu\mid\sigma^2,y)$.
3. Why is the marginal for $\mu$ a $t$ rather than a normal?
4. How do you sample from the joint posterior in two easy steps?

### Answers

1. $\pi(\mu,\sigma^2)\propto1/\sigma^2$ (independent Jeffreys priors); it is invariant and improper but yields a proper posterior.
2. Collect the $\mu$-terms: $\propto\exp(-\frac{n}{2\sigma^2}(\bar y-\mu)^2)$, giving $N(\bar y,\sigma^2/n)$.
3. Because integrating out the unknown $\sigma^2$ adds variability, giving a $t_{n-1}$ with heavier tails.
4. Draw $\sigma^2\mid y$, then $\mu\mid\sigma^2,y$.

---

# Topic 5: Rejection Sampling

## 5.1 Idea

We want samples from $f(x)$, which is hard. Instead, sample from an easy proposal $g(x)$ and accept with the right probability so accepted points follow $f$.

**Bounding requirement.** Choose $g$ and $K>0$ with

$$f(x)\le K\,g(x)\quad\forall x.$$

## 5.2 Algorithm (two equivalent forms)

**Version 1**
1. Generate $x^*\sim g(x)$.
2. Generate $y^*\sim U(0,Kg(x^*))$.
3. Accept $x^*$ if $y^*\le f(x^*)$.

**Version 2**
1. Generate $x^*\sim g(x)$.
2. Accept $x^*$ with probability $\dfrac{f(x^*)}{Kg(x^*)}$.

> [!note] Why they are the same
> Under Version 1, $\Pr(\text{accept }x^*)=\Pr(y^*\le f(x^*))=\int_0^{f(x^*)}\frac{1}{Kg(x^*)}\,dz=\frac{f(x^*)}{Kg(x^*)}$.

## 5.3 Why it works

With acceptance probability $h(x)=f(x)/(Kg(x))$,

$$\Pr(X\le x\mid X\text{ accepted})=\frac{\int_{-\infty}^x h(y)g(y)\,dy}{\int_{-\infty}^\infty h(y)g(y)\,dy}=\frac{\int_{-\infty}^x f(y)\,dy}{\int_{-\infty}^\infty f(y)\,dy},$$

which is the CDF of $f$. The constants ($K$ and any normalising constant of $f$) cancel, so $f$ need only be known up to proportionality.

## 5.4 Efficiency and choosing $K$

$$\Pr(X\text{ accepted})=\int h(y)g(y)\,dy=\frac1K\int f(y)\,dy\propto\frac1K.$$

- Want $K$ **as small as possible** subject to $f\le Kg$.
- Optimal choice: $K=\max_x f(x)/g(x)$, giving maximum acceptance probability 1.
- Accuracy improves as $g$ gets closer to $f$ (smaller $K$).

## 5.5 Worked example

Target $f(x)\propto x(1-x)^3$ on $[0,1]$, proposal $g(x)=U(0,1)$ (so $g=1$). Then $K=\max_x f(x)$; $f'(x)=(1-x)^2(1-4x)=0\Rightarrow x=\tfrac14$, so

$$K=f(1/4)=\tfrac14(3/4)^3=\tfrac{27}{256}.$$

```r
L <- 5000; K <- 27/256
xstar <- runif(L)
ind <- (runif(L) < (xstar*(1-xstar)^3/K))
hist(xstar[ind], probability = TRUE)
```

Efficiency example (target $\text{Beta}(2,2)$): proposal $\text{Beta}(1,1)$ gives efficiency 0.681; proposal $\text{Beta}(1.5,1.5)$ gives 0.848.

## Check your understanding

1. State the bounding requirement and why $K$ is needed.
2. Prove the two algorithm versions have the same acceptance probability.
3. Show accepted samples have distribution $f$.
4. What is the optimal $K$, and what does the acceptance rate tell you?

### Answers

1. $f(x)\le Kg(x)$ for all $x$; $K$ is needed because $g\ge f$ directly is generally impossible, so we scale up $g$ by $K$.
2. Both give acceptance probability $f(x^*)/(Kg(x^*))$.
3. The ratio of $\int_{-\infty}^x hg$ to $\int_{-\infty}^\infty hg$ is $\int_{-\infty}^x f/\int_{-\infty}^\infty f$, the CDF of $f$.
4. $K=\max_x f(x)/g(x)$; acceptance rate $=1/K$ (up to the constant of $f$), so smaller $K$ (better proposal) means higher efficiency.

---

## Connections

- **Builds on:** [[Conjugate Priors]] · [[Jeffreys Prior]] · [[Monte Carlo Integration]] · [[Inversion Sampling]]
- **Leads to:** [[Importance Sampling]] · [[Effective Sample Size]] · MCMC (later)
- **See also:** [[Week 3 Overview]] · [[Tutorial Week 3]] · [[Normal Model with Unknown Mean and Variance]] · [[Rejection Sampling]]
