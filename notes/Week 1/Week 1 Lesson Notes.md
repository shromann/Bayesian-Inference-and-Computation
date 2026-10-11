---
tags: [lesson, week-1]
week: 1
type: lesson
---

# Week 1 Lesson Notes

> [!abstract] How to use this note
> A guided walk-through of the Week 1 material, topic by topic, with derivations, intuition, and checkpoint questions. Read alongside [[Week 1 Overview]] and the individual concept notes. Covers the foundations of Bayesian inference and the motivation for Monte Carlo.

## Teaching order

1. [[#Topic 1 Probability Basics and Bayes Theorem|Probability Basics and Bayes' Theorem]] — the algebra
2. [[#Topic 2 The Likelihood Function|The Likelihood Function]] — the data's contribution
3. [[#Topic 3 Frequentist Statistics and the MLE|Frequentist Statistics and the MLE]] — the starting point
4. [[#Topic 4 The Bayesian Turn|The Bayesian Turn]] — making $\theta$ random
5. [[#Topic 5 The Prior Distribution|The Prior Distribution]] — beliefs before data
6. [[#Topic 6 The Posterior Distribution and Posterior Inference|The Posterior Distribution and Posterior Inference]] — the whole answer
7. [[#Topic 7 Credible Intervals|Credible Intervals]] — the intuitive interval
8. [[#Topic 8 The Bayesian Predictive Distribution|The Bayesian Predictive Distribution]] — uncertainty into predictions
9. [[#Topic 9 Monte Carlo Integration and the Law of Large Numbers|Monte Carlo Integration and the LLN]] — sampling to integrate
10. [[#Topic 10 The Water Consumption Example|The Water Consumption Example]] — the capstone

---

# Topic 1: Probability Basics and Bayes' Theorem

## 1.1 Conditional probability

For events $A,B$ with $\Pr(B)>0$,

$$\Pr(A\mid B)=\frac{\Pr(A,B)}{\Pr(B)}.$$

Rearranged, this gives the multiplication rule $\Pr(A,B)=\Pr(A\mid B)\Pr(B)$.

## 1.2 Law of total probability (marginalisation)

For a discrete variable $B$:

$$\Pr(A)=\sum_i\Pr(A,B_i)=\sum_i\Pr(A\mid B_i)\Pr(B_i).$$

For a continuous variable $X$ with density $p(x)$:

$$\Pr(A)=\int \Pr(A\mid X=x)\,p(x)\,dx.$$

> [!note] Why it matters
> Marginalisation is the operation that *removes nuisance parameters*. Every time we "integrate out" a parameter to get a marginal posterior, we are applying the law of total probability. See [[Multivariate Bayesian Models]].

## 1.3 Bayes' theorem

$$\Pr(A\mid B)=\frac{\Pr(B\mid A)\Pr(A)}{\Pr(B)}.$$

It is just conditional probability applied twice: $\Pr(A\cap B)=\Pr(A\mid B)\Pr(B)=\Pr(B\mid A)\Pr(A)$.

## 1.4 From events to inference

Substitute $A=x$ (observed data) and $B=\theta$ (unknown parameter). The event identity becomes the machinery of [[Bayesian Statistics]]:

$$\pi(\theta\mid x)=\frac{L(x\mid\theta)\pi(\theta)}{m(x)}\propto L(x\mid\theta)\pi(\theta),\qquad m(x)=\int_\Theta L(x\mid\theta)\pi(\theta)\,d\theta.$$

This is the same equation as [[Bayes Theorem]] — only the interpretation changes.

## 1.5 Worked example (rock strata)

Strata A and B give fossil probabilities $\Pr(\text{fossil}\mid A)=0.9$, $\Pr(\text{fossil}\mid B)=0.2$, with base rates $\Pr(A)=0.8$, $\Pr(B)=0.2$. Given a fossil is present,

$$\Pr(A\mid\text{fossil})=\frac{0.9\times0.8}{0.9\times0.8+0.2\times0.2}=\frac{0.72}{0.76}\approx0.947.$$

Notice the denominator is the law of total probability in action.

## Check your understanding

1. State the law of total probability for a continuous variable and say what it is used for in Bayesian inference.
2. Derive Bayes' theorem from conditional probability.
3. If $\Pr(A)=0.8$, $\Pr(B)=0.2$, $\Pr(\text{fossil}\mid A)=0.9$, $\Pr(\text{fossil}\mid B)=0.2$, find $\Pr(B\mid\text{fossil})$.

### Answers

1. $\Pr(A)=\int\Pr(A\mid X=x)p(x)\,dx$; it is used to marginalise (integrate out) nuisance parameters.
2. From $\Pr(A\cap B)=\Pr(A\mid B)\Pr(B)=\Pr(B\mid A)\Pr(A)$, so $\Pr(A\mid B)=\Pr(B\mid A)\Pr(A)/\Pr(B)$.
3. $1-0.947=0.053$.

---

# Topic 2: The Likelihood Function

## 2.1 Definition

For independent observations $x_1,\dots,x_n$ from a model with density $f$,

$$L(x\mid\theta)=\prod_{i=1}^n f(x_i\mid\theta).$$

It is the probability (density) of the observed data *as a function of the parameter*. It is the data's contribution to the posterior, re-weighting the [[Prior Distribution]] in [[Bayes Theorem]].

> [!warning] The likelihood is not a probability of $\theta$
> In $L(x\mid\theta)$, $x$ is the random variable, not $\theta$. $\theta$ is fixed; the "likelihood" is a function of $\theta$ for fixed data, even though we write it with a density-like symbol.

## 2.2 The running example

$X_i\sim\text{Poisson}(\theta)$ (the [[Water Consumption Example]]):

$$L(x\mid\theta)=\prod_{i=1}^n\frac{\theta^{x_i}}{x_i!}e^{-\theta}=\frac{\theta^{\sum_i x_i}e^{-n\theta}}{\prod_i x_i!}\propto\theta^{\sum_i x_i}e^{-n\theta}.$$

Everything that does not depend on $\theta$ has been dropped into the proportionality.

## 2.3 Exponential-family preview

Many likelihoods can be written as

$$f(x\mid\theta)=h(x)\,g(\theta)\exp\{t(x)\,c(\theta)\},$$

the [[Exponential Family]] form. This structure is exactly what makes [[Conjugate Priors]] possible.

## 2.4 Key point

$L$ need only be known up to a constant multiple of $\theta$ to run sampling algorithms ([[Rejection Sampling]], [[Importance Sampling]]), because constants cancel in ratios. That is why an unnormalised posterior is enough.

## Check your understanding

1. Write the likelihood for $n$ i.i.d. observations.
2. For $X_i\sim\text{Poisson}(\theta)$, write $L(x\mid\theta)$ up to proportionality in $\theta$.
3. Why is it valid to drop constants that do not involve $\theta$?

### Answers

1. $L(x\mid\theta)=\prod_{i=1}^n f(x_i\mid\theta)$.
2. $L(x\mid\theta)\propto\theta^{\sum_i x_i}e^{-n\theta}$.
3. Because the posterior is only needed up to proportionality; constants cancel in Bayes' rule (and in sampling ratios), so they never affect inference.

---

# Topic 3: Frequentist Statistics and the MLE

## 3.1 The frequentist stance

> [!important] Parameter is fixed
> In the frequentist view the data $x$ is **random** but the parameter $\theta$ is a **fixed unknown constant**. Probability statements are only ever about the data, never about $\theta$.

Inference then takes the form of a point estimate, a confidence interval, a hypothesis test, a prediction, or a decision. See [[Frequentist Statistics]].

## 3.2 Maximum likelihood estimation

$$\hat\theta_{\text{MLE}}=\arg\max_\theta L(x\mid\theta)=\arg\max_\theta\log L(x\mid\theta).$$

Properties:

- **Consistency:** $\hat\theta_{\text{MLE}}\to\theta_0$.
- **Asymptotic normality:** $\hat\theta\sim N(\theta,H)$ in the regular case, where $H$ comes from the curvature of the log-likelihood — this is what gives confidence intervals.
- **Invariance:** the MLE of $g(\theta)$ is $g(\hat\theta)$.

**Information-theoretic view (Tutorial Q5).** For large $n$, the MLE is the value of $\theta$ minimising the KL divergence $D_{KL}(p_{\text{true}}\,\|\,p(x\mid\theta))$. Equivalently it maximises $\mathbb{E}[\log p(x\mid\theta)]$.

## 3.3 Confidence intervals — and their awkwardness

A $100(1-\alpha)\%$ confidence interval for a mean is

$$\bar x\pm t_{\alpha/2}\frac{s}{\sqrt n}.$$

> [!warning] You cannot say "there is a 95% probability $\theta$ is in this interval"
> Because $\theta$ is fixed, any *single* interval either contains $\theta$ (probability 1) or does not (probability 0). The correct statement is long-run coverage: *over all experiments, 95% of such intervals contain $\theta$*.

This awkwardness is a key motivation for [[Credible Intervals]].

## 3.4 Non-regular likelihoods (the hospital example)

Let $\theta=\Pr(\text{death of a baby from an operation})$, with $r=0$ deaths in $n=47$ previous operations, $r\sim\text{Binomial}(n,\theta)$.

- The MLE $\hat\theta=0$ is well defined (it sits on the boundary).
- But $\hat\theta\sim N(\theta,H)$ **fails**.
- So even a simple CI becomes non-standard.

The Bayesian fix: with $\theta\sim U(0,1)$, the posterior contains all the information — it concentrates near 0 but with a proper right tail. Prediction is also fixed: plugging in $\hat\theta=0$ gives 100% survival, while the [[Bayesian Predictive Distribution]] retains some chance of future deaths.

## Check your understanding

1. State the MLE and two of its properties.
2. Why is the interpretation of a confidence interval so awkward?
3. In the hospital example, why does standard likelihood asymptotics fail?

### Answers

1. $\hat\theta=\arg\max_\theta\log L(x\mid\theta)$; consistent ($\to\theta_0$) and asymptotically normal ($\hat\theta\sim N(\theta,H)$).
2. Because $\theta$ is fixed, a single interval either contains it or not; only long-run coverage can be stated.
3. Because the MLE $\hat\theta=0$ lies on the boundary of the parameter space, violating the regularity needed for $\hat\theta\sim N(\theta,H)$.

---

# Topic 4: The Bayesian Turn

## 4.1 What changes

| | Data $x$ | Parameter $\theta$ |
|---|---|---|
| **Frequentist** | random | fixed constant |
| **Bayesian** | random | **random**, $\theta\sim\pi(\theta)$ |

Making $\theta$ random is what allows direct probability statements about it — descriptive inference becomes easy. Bayesian statistics treats learning as: given current knowledge (a distributional $\theta$), how do we optimally update with data $x$? See [[Bayesian Statistics]].

## 4.2 Arguments for and against priors

- **For:** we invariably have *some* prior knowledge, and it is already used implicitly (to choose the model, set significance levels, weight regressions). Bayesian statistics simply makes the weighting explicit — it *averages over* the likelihood surface rather than *maximising* it.
- **Against:** different priors give different inferences. Whether this is a feature or a bug is the philosophical divide.

The honest question is not *whether* to use prior information, but *how*.

## 4.3 The four-step Bayesian recipe ([[Bayesian Updating]])

1. Specify a [[Likelihood Function|likelihood model]] $L(x\mid\theta)$.
2. Elicit a [[Prior Distribution]] $\pi(\theta)$.
3. Compute the [[Posterior Distribution]] via [[Bayes Theorem]].
4. Draw inference (and/or make decisions) from the posterior.

$$\pi(\theta\mid x)=\frac{L(x\mid\theta)\pi(\theta)}{\int_\theta L(x\mid\theta)\pi(\theta)\,d\theta}.$$

**Illustration (regression).** For $y=ax+b+\epsilon$, parameters $\theta=(a,b)'$ get a prior distribution, and after observing data the result is a *posterior distribution* over $(a,b)$ — still a distribution, not a point.

## Check your understanding

1. What conceptual change from frequentist to Bayesian inference makes credible intervals possible?
2. Give one argument for using a prior and one against.
3. List the four steps of the Bayesian recipe.

### Answers

1. Treating $\theta$ as a random variable with a distribution, so probability statements about $\theta$ are legitimate.
2. For: prior knowledge is always present and the prior makes it explicit. Against: different priors give different answers (subjectivity).
3. Likelihood → prior → posterior (Bayes) → inference/decision.

---

# Topic 5: The Prior Distribution

## 5.1 Definition

$\pi(\theta)$ encodes everything we believe about the parameter **before** seeing the data, in distributional form. It may be uninformative (flat) or based on expert elicitation. Its role in [[Bayes Theorem]] is to weight the [[Likelihood Function]].

> [!important] Parameters are distributions, not points
> For regression $y=ax+b+\epsilon$ with $\theta=(a,b)'$:
> $$\pi\binom{a}{b}=N\!\left(\binom{0}{0},\begin{pmatrix}100&0\\0&100\end{pmatrix}\right)\quad\longrightarrow\quad \pi\binom{a}{b}\,\Big|\,x=N(\hat\mu,\hat\Sigma).$$

## 5.2 Do we really have prior knowledge?

Often sensible priors come from the model itself — and some assumptions are more defensible than others. For the regression example, assuming *zero covariance* between intercept and slope is questionable (we often expect a negative covariance).

**Same data, different priors (drunk friend).** $X\mid\theta\sim\text{Binomial}(10,\theta)$, observe $x=10$ (all successes). A drunk friend, a tea-drinker, and a music expert all produce 10/10. The data alone force the same conclusion; the priors $\text{Beta}(10,10)$, $\text{Beta}(10,4)$, $\text{Beta}(10,1)$ encode how surprising each claim is.

## 5.3 Types of priors

- [[Conjugate Priors]] — posterior stays in the same family.
- [[Improper Priors]] — integrate to $\infty$ but may give a proper posterior.
- [[Jeffreys Prior]] — invariant to reparameterisation.
- [[Mixture Priors]] — flexible, multimodal beliefs.
- Validate any prior with [[Prior Predictive Checking]].

## 5.4 The coloured-balls lesson

With the uniform prior $\Pr(C_i)=1/7$ the posterior for the drawn configuration is $1/35$; changing the prior changes the answer. *We often have to think hard about prior beliefs, and the answer depends on what we believe.* (Tutorial Q4.)

## Check your understanding

1. What is a prior distribution and what is its role in Bayes' theorem?
2. Give two examples of prior assumptions that are "hidden" inside a frequentist analysis.
3. Why can two analysts with the same data reach different posteriors?

### Answers

1. A distribution over $\theta$ before seeing data; it weights the likelihood in Bayes' rule.
2. The choice of model (e.g. normal) and the choice of significance level.
3. Because they use different priors — the posterior depends on both data and prior.

---

# Topic 6: The Posterior Distribution and Posterior Inference

## 6.1 The posterior

$$\pi(\theta\mid x)=\frac{L(x\mid\theta)\pi(\theta)}{m(x)}\propto L(x\mid\theta)\pi(\theta),\qquad m(x)=\int_\Theta L(x\mid\theta)\pi(\theta)\,d\theta.$$

It is the complete description of our knowledge about $\theta$ *after* seeing the data.

> [!important] Everything is in the posterior
> All information needed for further inference is contained in $\pi(\theta\mid x)$: point estimates, intervals, predictions, decisions. Every quantity is an integral over the posterior — which is why [[Monte Carlo Integration]] matters.

## 6.2 Two routes to compute it

1. **Algebraically** (least common): exact but often impossible; only in restricted cases → [[Conjugate Priors]].
2. **Computationally** (most common): approximate but always possible → [[Monte Carlo Integration]].

## 6.3 Posterior inference is integration

For the [[Water Consumption Example]] with $\theta\mid x\sim\text{Gamma}(\alpha+\sum_i x_i,\ \beta+n)$:

$$E_\pi[\theta]=\int_\Theta\theta\,\pi(\theta\mid x)\,d\theta=\frac{\alpha+\sum_i x_i}{\beta+n},\qquad \text{Var}(\theta)=\frac{\alpha+\sum_i x_i}{(\beta+n)^2}.$$

A 95% [[Credible Intervals|credible interval]] $[a,b]$ solves $\int_0^a\pi(\theta\mid x)\,d\theta=0.025$ and $\int_0^b\pi(\theta\mid x)\,d\theta=0.975$.

For a parameter vector $\theta=(\theta_0,\theta_1,\theta_2,\kappa)$, nuisance parameters are integrated out. The marginal of $\kappa$ is

$$\pi(\kappa\mid x)=\int_{\Theta_2}\int_{\Theta_1}\int_{\Theta_0}\pi(\theta_0,\theta_1,\theta_2,\kappa\mid x)\,d\theta_0\,d\theta_1\,d\theta_2.$$

Conceptually simple — but the algebra becomes hard fast, which is exactly why [[Monte Carlo Integration]] exists.

> [!important] Integration is the theme
> Every posterior summary is an integral. Closed solutions are typically impossible, so we approximate the posterior by sampling from it.

## Check your understanding

1. Why is the posterior described as "the whole answer"?
2. Name the two routes to computing a posterior and when each applies.
3. Write the posterior mean and variance for a $\text{Gamma}(a,b)$ posterior.

### Answers

1. All inference (estimates, intervals, predictions, decisions) is a functional/integral of the posterior, so it contains everything needed.
2. Algebraically (exact, only for special/conjugate cases) and computationally via Monte Carlo (approximate, always possible).
3. Mean $a/b$, variance $a/b^2$.

---

# Topic 7: Credible Intervals

## 7.1 The interpretation

> [!success] Bayesian ($\theta$ is random)
> "There is a 95% probability that $\theta$ is in this (single) credible interval."

Very intuitive — and exactly what confidence intervals cannot say. To find a 95% interval, solve

$$\int_0^a\pi(\theta\mid x)\,d\theta=0.025,\qquad \int_0^b\pi(\theta\mid x)\,d\theta=0.975.$$

## 7.2 They are not unique

Infinitely many intervals have 95% coverage. Two common choices:

- **Equal-tailed interval** — chop 2.5% off each tail.
- **High Density Region (HDR)** — the interval with the *shortest width*.

## 7.3 High Density Regions

- Shortest-width credible interval.
- Not always central: for a skewed posterior the HDR shifts.
- Can be **disjoint** for multimodal posteriors (see [[Mixture Priors]]).

For a symmetric posterior (e.g. normal) the equal-tailed and HDR intervals coincide, and the mean/median/mode all agree.

## Check your understanding

1. How does the interpretation of a credible interval differ from a confidence interval?
2. What is an HDR, and when does it differ from the equal-tailed interval?
3. For a normal posterior, how do the two intervals relate?

### Answers

1. A credible interval supports a direct probability statement about $\theta$; a confidence interval only supports long-run coverage.
2. The shortest-width credible interval; it differs from the equal-tailed interval when the posterior is skewed or multimodal.
3. They coincide (and mean = median = mode).

---

# Topic 8: The Bayesian Predictive Distribution

## 8.1 Definition

For future data $y$,

$$p(y\mid x)=\int_\Theta\pi(y\mid\theta)\,\pi(\theta\mid x)\,d\theta.$$

It is the prior predictive with the prior replaced by the posterior — it propagates parameter *uncertainty* into predictions.

## 8.2 Why not just plug in $\hat\theta$?

Plugging in a fixed estimate gives $y\sim\pi(y\mid\hat\theta)$ and **ignores uncertainty about $\theta$**. In the [[Non-regular Likelihoods|hospital example]] with $\hat\theta=0$ this predicts 100% survival — unrealistic. The Bayesian predictive accounts for parameter uncertainty and retains some possibility of future deaths.

## 8.3 Monte Carlo shortcut

Instead of the often-laborious algebra:

1. Draw $\theta^{(i)}\sim\pi(\theta\mid x)$.
2. For each, draw $y^{(i)}\sim\pi(y\mid\theta^{(i)})$.
3. Discard the $\theta^{(i)}$; the remaining $y^{(i)}$ are a sample from $p(y\mid x)$.

This is "hugely simpler than calculating the exact algebraic expression".

## 8.4 Closed-form example

For the [[Water Consumption Example]] (Poisson–Gamma),

$$p(y\mid x)=\text{NegBin}\!\left(y\ \Big|\ \alpha+\textstyle\sum_i x_i,\ \frac{\beta+n}{\beta+n+1}\right).$$

## Check your understanding

1. Write the posterior predictive and explain in words what it does.
2. Why is it better than plugging in a point estimate?
3. Describe the two-stage Monte Carlo algorithm for predicting.

### Answers

1. $p(y\mid x)=\int\pi(y\mid\theta)\pi(\theta\mid x)\,d\theta$; it averages the data model over the posterior, so predictions include parameter uncertainty.
2. It accounts for uncertainty in $\theta$ rather than conditioning on a single estimate.
3. Sample $\theta^{(i)}\sim\pi(\theta\mid x)$, then $y^{(i)}\sim\pi(y\mid\theta^{(i)})$, and keep only the $y^{(i)}$.

---

# Topic 9: Monte Carlo Integration and the Law of Large Numbers

## 9.1 The idea

Posterior quantities are expectations (integrals). If we can sample $\theta^{(1)},\dots,\theta^{(N)}\sim\pi(\theta\mid x)$, then

$$E_\pi[g(\theta)]=\int_\Theta g(\theta)\pi(\theta\mid x)\,d\theta\approx\frac1N\sum_{i=1}^N g(\theta^{(i)}).$$

Examples: posterior mean $\approx\frac1N\sum_i\theta^{(i)}$; probabilities $\Pr(\theta<-1)\approx\frac1N\sum_i\mathbb{I}(\theta^{(i)}<-1)$ (the indicator is a function $g$).

## 9.2 Why it works — the discrete measure

Approximate the posterior by

$$\pi(\theta\mid x)\approx\frac1N\sum_{i=1}^N\delta_{\theta^{(i)}}(\theta),\qquad \delta_b(A)=\begin{cases}1&b\in A\\0&\text{otherwise.}\end{cases}$$

Then

$$E_\pi[g(\theta)]\approx\int g(\theta)\frac1N\sum_i\delta_{\theta^{(i)}}(\theta)\,d\theta=\frac1N\sum_i g(\theta^{(i)}).$$

The rigorous justification is the [[Law of Large Numbers]]: for i.i.d. $X_i=g(\theta^{(i)})$ with mean $\mu$, $\frac1N\sum X_i\to\mu$ almost surely.

> [!note] LLN vs CLT
> The [[Law of Large Numbers]] gives *consistency* (the estimate converges). The [[Central Limit Theorem]] gives *precision* (how it fluctuates, at rate $1/\sqrt N$) — see [[Monte Carlo Error]].

## 9.3 Multivariate Monte Carlo

- **Marginals:** if $(\theta_1^{(i)},\theta_2^{(i)})\sim\pi(\theta_1,\theta_2\mid x)$, discarding the $\theta_2$ values gives samples from $\pi(\theta_1\mid x)$.
- **Functions of parameters:** compute $\theta_1^{(i)}-\theta_2^{(i)}$ and histogram — no Jacobian needed.
- **Predictives:** sample $\theta^{(i)}$, then $y^{(i)}\sim\pi(y\mid\theta^{(i)})$, discard $\theta^{(i)}$.

## 9.4 Integration over arbitrary ranges

| Range | Trick |
|---|---|
| $\int_0^1 g$ | $U\sim U(0,1)$, average $g(u)$ |
| $\int_a^b g$ | transform $u=(x-a)/(b-a)$, or simulate $U(a,b)$ and multiply by $(b-a)$ |
| $\int_0^\infty g$ | substitute $u=1/(x+1)$ |
| multivariate | same average works |

> [!tip] Cost and benefit
> The method is remarkably easy to use even in high dimensions (no curse of dimensionality for the *method*). The price is high variance; reduce it with [[Importance Sampling]].

## Check your understanding

1. Write the Monte Carlo estimator of $E_\pi[g(\theta)]$ and the LLN justification.
2. How do you get a marginal posterior from joint samples?
3. State a benefit and a cost of Monte Carlo integration.

### Answers

1. $\frac1N\sum_i g(\theta^{(i)})$ with $\theta^{(i)}\sim\pi(\theta\mid x)$; by the LLN the average converges to the integral.
2. Sample from the joint and discard the components you are not interested in.
3. Benefit: easy even in high dimensions, constant variance-ish scaling. Cost: high variance / needs many samples for precision.

---

# Topic 10: The Water Consumption Example

## 10.1 Setup

Melbourne per-capita daily water use (litres), 1940–2004: $n=65$, $\sum_i x_i=24890$. Model $x_i\sim\text{Poisson}(\theta)$. (Independence and constant rate are unrealistic for a time series; they simplify things.)

## 10.2 The four steps

**1. Likelihood.**
$$L(x\mid\theta)=\prod_{i=1}^n\frac{\theta^{x_i}}{x_i!}e^{-\theta}\propto\theta^{\sum_i x_i}e^{-n\theta}.$$

**2. Prior.** $\theta\sim\text{Gamma}(\alpha,\beta)\propto\theta^{\alpha-1}e^{-\beta\theta}$.

**3. Posterior (conjugate update).**
$$\pi(\theta\mid x)\propto\theta^{\alpha+\sum_i x_i-1}e^{-(\beta+n)\theta}\ \Longrightarrow\ \boxed{\theta\mid x\sim\text{Gamma}\Big(\alpha+\textstyle\sum_i x_i,\ \beta+n\Big)}.$$

**4. Inference.**
- Posterior mean: $\dfrac{\alpha+\sum_i x_i}{\beta+n}$.
- Posterior variance: $\dfrac{\alpha+\sum_i x_i}{(\beta+n)^2}$.
- 95% credible interval from Gamma quantiles.
- Predictive: $p(y\mid x)=\text{NegBin}\big(y\mid\alpha+\sum_i x_i,\ \frac{\beta+n}{\beta+n+1}\big)$.

## 10.3 Prior sensitivity

| Prior | $\alpha$ | $\beta$ | Effect |
|---|---|---|---|
| Moderate | 1 | 0.01 | posterior close to the data |
| Strongly informative | 1 | 10 | posterior pulled toward the prior |

Enough data can overwhelm the prior. This motivates the different prior types in [[Week 2 Overview]].

## 10.4 Toward realistic models

Constant $\theta$ is unrealistic. A linear trend $\theta=(\theta_0,\theta_1)$, a piecewise-linear model $(\theta_0,\theta_1,\theta_2)$ with known change-point $\kappa$, or an unknown change-point $(\theta_0,\theta_1,\theta_2,\kappa)$ quickly make the algebra intractable → [[Monte Carlo Integration]].

## Check your understanding

1. Derive the Poisson–Gamma posterior.
2. Write the posterior mean and variance.
3. Why does making the model more realistic force us toward Monte Carlo?

### Answers

1. Multiply $\theta^{\sum x_i}e^{-n\theta}$ by $\theta^{\alpha-1}e^{-\beta\theta}$ to get $\theta^{\alpha+\sum x_i-1}e^{-(\beta+n)\theta}$, i.e. $\text{Gamma}(\alpha+\sum x_i,\ \beta+n)$.
2. Mean $\frac{\alpha+\sum x_i}{\beta+n}$, variance $\frac{\alpha+\sum x_i}{(\beta+n)^2}$.
3. Because additional parameters create high-dimensional, non-conjugate integrals with no closed form.

---

## Connections

- **Builds on:** [[Probability Basics]] · [[Bayes Theorem]] · [[Likelihood Function]]
- **Leads to:** [[Prior Distribution]] · [[Posterior Distribution]] · [[Credible Intervals]] · [[Monte Carlo Integration]] · [[Conjugate Priors]]
- **See also:** [[Week 1 Overview]] · [[Water Consumption Example]] · [[Tutorial Week 1]] · [[Frequentist Statistics]]
