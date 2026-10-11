---
tags: [lesson, week-2]
week: 2
type: lesson
---

# Week 2 Lesson Notes

> [!abstract] How to use this note
> A guided walk-through of the Week 2 material, topic by topic, with derivations, intuition, and checkpoint questions. Read alongside [[Week 2 Overview]] and the individual concept notes. Covers all seven topics for Week 2.

## Teaching order

1. [[#Topic 1 The Normalising Constant|The Normalising Constant]] — *why* the whole week exists
2. [[#Topic 2 Conjugate Priors|Conjugate Priors]] — the algebra shortcut
3. [[Exponential Family]] — *why* conjugacy works
4. [[Improper Priors]] — adding "no information"
5. [[Fisher Information]] → [[Jeffreys Prior]] — the invariant ignorance prior
6. [[Maximum A Posteriori]] — mode vs MLE
7. [[Probability Integral Transform]] → [[Inversion Sampling]] — first sampler

---

# Topic 1: The Normalising Constant

## 1.1 The setup

[[Bayes Theorem]] for a parameter $\theta$ given data $x$:

$$\pi(\theta\mid x)=\frac{L(x\mid\theta)\,\pi(\theta)}{\int_\Theta L(x\mid\theta)\,\pi(\theta)\,d\theta}$$

Read each piece:

- $L(x\mid\theta)$ — [[Likelihood Function|likelihood]]: how plausible the data is for each $\theta$.
- $\pi(\theta)$ — [[Prior Distribution|prior]]: what we believed about $\theta$ before seeing data.
- The numerator $L(x\mid\theta)\pi(\theta)$ — the **unnormalised posterior**. It is "posterior-shaped" but does not integrate to 1.
- The denominator — the **normalising constant**.

## 1.2 What the constant actually is

$$m(x)=\int_\Theta L(x\mid\theta)\,\pi(\theta)\,d\theta$$

Intuition: $m(x)$ is the **average likelihood**, averaging over all possible $\theta$ weighted by the prior. Another name is the **marginal likelihood** (or "evidence"), because by the law of total probability it is the probability of the observed data $x$ under the model.

Its only job is to rescale the numerator so the posterior integrates to 1:

$$\int \pi(\theta\mid x)\,d\theta = \frac{\int L(x\mid\theta)\pi(\theta)\,d\theta}{m(x)} = \frac{m(x)}{m(x)} = 1.$$

> [!important] Key identity
> $$\pi(\theta\mid x)\propto L(x\mid\theta)\,\pi(\theta)$$
> The constant is *independent of $\theta$*, so anything that is a function of $\theta$ only is kept; anything that is just a number can be dropped and re-found later.

## 1.3 Why it is "the hardest part"

**Example.** $x_1,\dots,x_n \sim \text{Poisson}(\theta)$, with prior $\pi(\theta)=1$ for $0<\theta\le 1$.

The likelihood is $L=\prod_i \frac{e^{-\theta}\theta^{x_i}}{x_i!} \propto e^{-n\theta}\theta^{\sum x_i}$. So

$$m(x)=\int_0^1 e^{-n\theta}\,\theta^{\sum x_i}\,d\theta.$$

This has **no elementary closed form** — it is a *lower incomplete gamma function*. Substituting $t=n\theta$ gives

$$\int_0^{n} e^{-t}\,(t/n)^{s}\,dt \propto \gamma(s+1,\,n),\qquad s=\textstyle\sum x_i.$$

A *complete* gamma integral $\int_0^\infty t^s e^{-t}\,dt=\Gamma(s+1)$ is closed-form; it is the **upper limit being 1** (the truncation) that spoils it. It must be evaluated numerically. Now imagine $\theta$ is a *vector* $(\theta_1,\dots,\theta_d)$: you get a $d$-dimensional integral and it quickly becomes hopeless. This is exactly why Bayesian computation exists.

> [!warning] Terminology trap
> Do not confuse this with the **digamma** function $\psi(\theta)=\frac{d}{d\theta}\log\Gamma(\theta)$, which appears in *other* places (e.g. expected log-likelihood). The obstruction here is the *incomplete gamma*, not the digamma.

## 1.4 Why we can often *ignore* the constant

This is the crucial takeaway. Many methods never compute $m(x)$:

| Method | Why the constant cancels |
|---|---|
| [[Conjugate Priors]] | The constant becomes a known normalising factor of a recognised distribution (Beta, Gamma, ...). |
| [[Rejection Sampling]] | Only ratios $f(x)/g(x)$ appear → constants cancel. |
| [[Importance Sampling]] | Weights are ratios → constants cancel. |
| [[Monte Carlo Integration]] | Expectations $\frac1N\sum g(\theta^{(i)})$ normalise themselves. |

## 1.5 Worked mini-example

Let $x\sim\text{Binomial}(n,\theta)$ and $\theta\sim\text{Beta}(a,b)$. Ignoring the constant,

$$\pi(\theta\mid x)\propto \underbrace{\theta^x(1-\theta)^{n-x}}_{\text{likelihood}}\cdot\underbrace{\theta^{a-1}(1-\theta)^{b-1}}_{\text{prior}}=\theta^{a+x-1}(1-\theta)^{b+n-x-1}.$$

Instead of integrating to find $m(x)$, we **recognise** this as an unnormalised $\text{Beta}(a+x,\,b+n-x)$ density. The constant was never needed — this is what the next topic formalises.

## Check your understanding

1. In one sentence, what is $m(x)$ and what is its role?
2. Why is $\pi(\theta\mid x)\propto L(x\mid\theta)\pi(\theta)$ true? (What are we dropping, and why is dropping it allowed?)
3. For the Poisson example above, why can we not write down $m(x)$ in closed form?
4. Give one reason it is often fine to never compute $m(x)$.

### Answers

1. $m(x)$ is the normalising constant (marginal likelihood); its role is to make the posterior integrate to 1.
2. We drop the denominator because it is **independent of $\theta$**; it changes the height of the posterior but not its shape, so the posterior is known up to proportionality.
3. The truncated integration range $[0,1]$ yields a lower incomplete gamma, which has no elementary closed form; it must be computed numerically.
4. When we only need the posterior up to proportionality — e.g. when it can be recognised as a known family by inspecting likelihood × prior.

---

# Topic 2: Conjugate Priors

## 2.1 The definition

Let $\mathcal{F}$ be a family of likelihoods and $\mathcal{P}$ a family of priors. We say $\mathcal{P}$ is **conjugate** for $\mathcal{F}$ if

$$\pi(\theta)\in\mathcal{P}\quad\Rightarrow\quad \pi(\theta\mid x)\in\mathcal{P}\ \text{for all } x.$$

In words: **pick a prior from a family such that the posterior lands back in the *same* family.** Only the parameters change. So instead of doing an integral, you do **arithmetic on the parameters**.

For example: Binomial likelihood + Beta prior → **Beta posterior**. You never integrate anything. See [[Conjugate Priors]].

## 2.2 Why it works — the "kernel matching" recipe

The entire technique is one move: **multiply likelihood × prior, then recognise the algebraic shape.**

$$\pi(\theta\mid x)\propto \underbrace{L(x\mid\theta)}_{\text{likelihood}}\times\underbrace{\pi(\theta)}_{\text{prior}}$$

Collect the $\theta$-terms into a kernel you recognise (Beta, Gamma, Normal, ...), then read off the new parameters. The constant was never needed (Topic 1, point 2).

## 2.3 Binomial + Beta → Beta

$x\sim\text{Binomial}(n,\theta)$, prior $\theta\sim\text{Beta}(a,b)$:

$$L=\binom nx\theta^x(1-\theta)^{n-x},\qquad \pi(\theta)\propto\theta^{a-1}(1-\theta)^{b-1}.$$

Multiply and **add the exponents** (same base):

$$\pi(\theta\mid x)\propto\theta^{\,x+(a-1)}(1-\theta)^{\,n-x+(b-1)}=\theta^{\,a+x-1}(1-\theta)^{\,b+n-x-1}.$$

Recognise Beta: $p(\theta)\propto\theta^{\alpha-1}(1-\theta)^{\beta-1}$. Therefore

$$\boxed{\theta\mid x\sim\text{Beta}(a+x,\ b+n-x)}.$$

**Prior params act like "pseudo-counts":** $a$ = pretend successes, $b$ = pretend failures. Data just adds real counts.

## 2.4 Poisson + Gamma → Gamma

$x_1,\dots,x_n\stackrel{iid}\sim\text{Poisson}(\theta)$, prior $\theta\sim\text{Gamma}(a,b)\propto\theta^{a-1}e^{-b\theta}$:

$$L\propto e^{-n\theta}\theta^{\sum x_i}.$$

Multiply — exponents add on $\theta$, exponents add on $e^{-\theta}$:

$$\pi(\theta\mid x)\propto\theta^{\,a+\sum x_i-1}e^{-(b+n)\theta}\ \Rightarrow\ \boxed{\theta\mid x\sim\text{Gamma}\Big(a+\textstyle\sum x_i,\ b+n\Big)}.$$

## 2.5 Normal + Normal (known variance) → Normal

$x_1,\dots,x_n\sim N(\theta,\sigma^2)$ with $\sigma^2$ **known**, prior $\theta\sim N(b,d^2)$. Write precisions $c=1/d^2$ (prior) and $\tau=1/\sigma^2$ (data). Then

$$\boxed{\theta\mid x\sim N\!\left(\frac{cb+n\tau\bar x}{c+n\tau},\ \frac{1}{c+n\tau}\right)}.$$

Three messages:

1. **Posterior mean is a weighted average:** $E(\theta\mid x)=\gamma b+(1-\gamma)\bar x$ with $\gamma=\dfrac{c}{c+n\tau}$. More prior precision → pull toward prior mean; more data → pull toward $\bar x$.
2. **Posterior precision adds:** $\dfrac{1}{\text{Var}(\theta\mid x)}=c+n\tau$. Information adds.
3. **Sufficiency:** $\bar x$ is all that matters — the posterior depends on the data only through $\bar x$.

## 2.6 When is conjugacy *not* appropriate?

- **Pros:** closed-form posterior → fast, exact, easy to summarise; interpretable (pseudo-counts, precision addition).
- **Con:** if your genuine prior beliefs **cannot be expressed by that family**, forcing a conjugate prior is dishonest. Conjugacy is an algebraic convenience, not a statement about your beliefs.

## 2.7 Common misconception

Conjugate priors are **not** "the correct priors," and a conjugate posterior is **not** automatically better than a numerical one. They are a computational shortcut that trades flexibility for tractability.

## Check your understanding

1. State the definition of a conjugate prior in one sentence.
2. $x\sim\text{Binomial}(10,\theta)$, prior $\theta\sim\text{Beta}(2,3)$, and you observe $x=7$. Write the posterior *immediately*.
3. In the Normal case, what happens to the posterior mean as $n\to\infty$? As the prior variance $d^2\to\infty$?
4. Why might using a conjugate prior be a bad idea?

### Answers

1. A prior whose family is closed under Bayesian updating: the posterior stays in the same family as the prior.
2. $\theta\mid x\sim\text{Beta}(2+7,\ 3+10-7)=\text{Beta}(9,6)$.
3. As $n\to\infty$ the posterior mean $\to\bar x$ (prior washes out); as $d^2\to\infty$ (so $c\to0$) the posterior mean $\to\bar x$ again — a diffuse prior gives the same answer.
4. When the conjugate family is not flexible enough to express your actual prior beliefs.

---

# Topic 3: Exponential Family

## 3.1 The definition

A likelihood belongs to the **exponential family** if it can be written as

$$f(x\mid\theta)=h(x)\,g(\theta)\exp\{t(x)\,c(\theta)\},$$

for functions $h,g,t,c$ such that $\int f(x\mid\theta)\,dx=1$. Read each piece:

| Piece | Name | Depends on |
|---|---|---|
| $h(x)$ | base measure / carrier | data only |
| $g(\theta)$ | normalising function | parameter only |
| $t(x)$ | sufficient statistic | data only |
| $c(\theta)$ | natural parameter | parameter only |

## 3.2 Which distributions are in it?

Includes: Exponential, Poisson, one-parameter Gamma, Binomial, Normal (with known variance), Geometric, Negative Binomial. These are exactly the models for which the [[Conjugate Prior Reference Table|standard conjugate pairs]] exist.

## 3.3 Why conjugacy follows

With prior $\pi(\theta)$ and i.i.d. data, the posterior is

$$\pi(\theta\mid x)\propto\pi(\theta)\,g(\theta)^n\exp\!\Big\{c(\theta)\sum_i t(x_i)\Big\}.$$

Now choose a prior of the **same algebraic form** as the likelihood's $\theta$-part:

$$\pi(\theta)\propto g(\theta)^d\exp\{b\,c(\theta)\}\quad\text{for some } d,b.$$

Then

$$\pi(\theta\mid x)\propto g(\theta)^{d+n}\exp\!\Big\{c(\theta)\big[\textstyle\sum_i t(x_i)+b\big]\Big\}=g(\theta)^{\tilde d}\exp\{\tilde b\,c(\theta)\},$$

which is **back in the same family**, with the parameters updated $d\mapsto\tilde d=d+n$ and $b\mapsto\tilde b=b+\sum_i t(x_i)$. This is exactly [[Conjugate Priors|conjugacy]].

> [!important] The one-line reason
> Conjugate priors exist because multiplying two members of the exponential family keeps you in the exponential family — the sufficient statistics just add.

## 3.4 Worked construction (Binomial)

Write the Binomial as an exponential family. Start with the mass function and force the $x$-dependence into an exponential:

$$f(x\mid\theta)=\binom nx\theta^x(1-\theta)^{n-x}=\binom nx(1-\theta)^n\left(\frac{\theta}{1-\theta}\right)^x=\binom nx(1-\theta)^n\exp\!\left\{x\log\frac{\theta}{1-\theta}\right\}.$$

So

$$h(x)=\binom nx,\quad g(\theta)=(1-\theta)^n,\quad t(x)=x,\quad c(\theta)=\log\frac{\theta}{1-\theta}.$$

The conjugate prior must therefore be

$$\pi(\theta)\propto[(1-\theta)^n]^d\exp\!\left\{b\log\frac{\theta}{1-\theta}\right\}=(1-\theta)^{nd-b}\,\theta^{b},$$

which is the [[Beta Distribution|Beta]] family. **So the Beta prior is not a coincidence — it is forced by the form of the Binomial likelihood.**

## 3.5 Outside the family

A few non-exponential-family conjugacies exist (e.g. $U(0,\theta)$ likelihood with a Pareto prior), but these are rare and out of scope. "Essentially, conjugacy holds only for the exponential family."

## Check your understanding

1. Write down the general exponential-family form and label what each function depends on.
2. In the Binomial construction, what are $g(\theta)$ and $c(\theta)$?
3. Why does choosing $\pi(\theta)\propto g(\theta)^d\exp\{b\,c(\theta)\}$ guarantee a conjugate posterior?
4. Which of these is *not* in the exponential family: Poisson, Binomial, $U(0,\theta)$?

### Answers

1. $f(x\mid\theta)=h(x)g(\theta)\exp\{t(x)c(\theta)\}$; $h,t$ depend on $x$; $g,c$ depend on $\theta$.
2. $g(\theta)=(1-\theta)^n$ and $c(\theta)=\log\frac{\theta}{1-\theta}$.
3. Because the posterior becomes $g(\theta)^{d+n}\exp\{c(\theta)[\sum t(x_i)+b]\}$, the same functional form with updated parameters.
4. $U(0,\theta)$.

---

# Topic 4: Improper Priors

## 4.1 The definition

A prior $\pi(\theta)$ is **improper** if it does not integrate to a finite constant:

$$\int\pi(\theta)\,d\theta=\infty\qquad\left(\text{or }\sum_i\pi(\theta_i)\to\infty\text{ for discrete }\theta\right).$$

It is therefore not a genuine probability density, yet it can still be a useful device.

## 4.2 How it arises naturally

Recall (Topic 2) the Normal model with known variance:

$$\theta\mid x\sim N\!\left(\frac{cb+n\tau\bar x}{c+n\tau},\ \frac{1}{c+n\tau}\right),\qquad c=1/d^2.$$

Let the prior variance $d^2\to\infty$, i.e. $c\to0$. Then

$$\theta\mid x\sim N\!\left(\bar x,\ \frac{\sigma^2}{n}\right),$$

and the limiting prior is $\theta\sim N(b,\infty)$, i.e. $\pi(\theta)\propto1$ — **uniform on $\mathbb{R}$**, which is improper since $\int_{\mathbb{R}}1\,d\theta=\infty$.

## 4.3 Rules of use

> [!important] Conditions
> - It is OK to use an improper prior **as long as the posterior is proper**: $\int\pi(\theta\mid x)\,d\theta<\infty$.
> - If the posterior is also improper, that prior **cannot** be used (no valid inference, e.g. the 2025 exam's uniform prior on $n$).
> - Small $c$ = weak prior information (very large variance); $c\to0$ = complete uninformativeness.
>
> A flat prior is not "no assumptions" — it is an assumption of *uniform ignorance on that scale*, which is scale-dependent (see 4.5).

## 4.4 Uninformative prior is not the same as frequentist inference

It is tempting to think a flat prior reduces Bayes to frequentist inference. It does not:

- Bayesian inference returns a **distribution on $\theta$**; frequentist inference (generally) returns point estimators and intervals with long-run guarantees.
- With $\theta\sim U(0,1)$, $\log\pi(\theta)=0$, so [[Maximum A Posteriori|MAP]] $=$ [[Maximum Likelihood Estimation|MLE]]. But other Bayes estimators (e.g. the posterior mean) need not equal the MLE.

## 4.5 The invariance problem

Representing ignorance by a flat prior does **not** survive reparameterisation. If $\pi(\theta)\propto1$ and we change variable to $\phi=\theta^2$, the density transforms as

$$\pi(\phi)=\pi(\theta)\left|\frac{d\theta}{d\phi}\right|\propto\frac{1}{\sqrt\phi},$$

which is **not** flat. Yet ignorance about $\theta$ "should" mean ignorance about $\phi$ too. This inconsistency is exactly what the [[Jeffreys Prior]] is designed to fix.

## Check your understanding

1. Define an improper prior, and state the condition under which it may be used for inference.
2. How does the uniform prior $\pi(\theta)\propto1$ arise as a limit of the Normal prior?
3. True or false: a flat prior makes Bayesian inference equivalent to frequentist inference. Explain briefly.
4. Why does a flat prior fail to represent "ignorance" consistently?

### Answers

1. A prior with $\int\pi(\theta)\,d\theta=\infty$; usable only if the resulting posterior is proper.
2. Take the prior variance $d^2\to\infty$ (prior precision $c\to0$); the prior becomes $N(b,\infty)\propto1$.
3. False. Bayesian inference gives a posterior distribution; a flat prior makes MAP = MLE, but other Bayes estimators (posterior mean, etc.) can differ.
4. Because a flat density on $\theta$ becomes non-flat after a nonlinear reparameterisation ($\phi=\theta^2$ gives $\pi(\phi)\propto\phi^{-1/2}$), so "ignorance" depends on the chosen scale.

---

# Topic 5: Fisher Information and Jeffreys Prior

## 5.1 Fisher information — definition and intuition

The (univariate) [[Fisher Information]] is

$$I(\theta)=-E\!\left[\frac{d^2\log L(x\mid\theta)}{d\theta^2}\right],$$

the expected **curvature** of the log-likelihood at $\theta$. A sharply peaked log-likelihood (lots of curvature) means the data pin down $\theta$ precisely, so $I(\theta)$ is large. An equivalent form is $I(\theta)=E\!\left[\left(\frac{d\log L}{d\theta}\right)^2\right]$.

For $n$ i.i.d. observations, information adds: $I_n(\theta)=nI(\theta)$.

## 5.2 Standard examples

| Model | $I(\theta)$ | Jeffreys prior |
|---|---|---|
| $\text{Binomial}(n,\theta)$ | $n\,\theta^{-1}(1-\theta)^{-1}$ | $\propto\theta^{-1/2}(1-\theta)^{-1/2}$ |
| $N(\theta,\sigma^2)$, $\sigma^2$ known | $n/\sigma^2$ | $\propto1$ |
| $N(m,\theta)$ (variance unknown) | $n/(2\theta^2)$ | $\propto\theta^{-1}$ |
| $N(\mu,\sigma^2)$, both unknown | $\mathrm{diag}\!\left(n/\sigma^2,\ n/(2\sigma^4)\right)$ | $\propto\sigma^{-3}$ |

## 5.3 Jeffreys prior — definition and invariance

The [[Jeffreys Prior]] is defined as

$$\pi_J(\theta)\propto|I(\theta)|^{1/2},\qquad I(\theta)=-E\!\left[\frac{d^2\log L(x\mid\theta)}{d\theta^2}\right].$$

Harold Jeffreys argued that a statement of prior ignorance should be **consistent across one-to-one transformations**. Here is why $\pi_J$ achieves that: if $\phi=g(\theta)$ is monotone, then by the change-of-variable rule and the transformation property of information,

$$\pi_J(\phi)=\pi_J(\theta)\left|\frac{d\theta}{d\phi}\right|\propto|I(\theta)|^{1/2}\left|\frac{d\theta}{d\phi}\right|=\left|I(\theta)\left(\frac{d\theta}{d\phi}\right)^2\right|^{1/2}=|I(\phi)|^{1/2}.$$

So applying the **same rule** $\pi_J\propto|I|^{1/2}$ in *any* parameterisation gives the correct (consistent) prior.

## 5.4 Worked example: Binomial

$x\mid\theta\sim\text{Bin}(n,\theta)$. Then $\log L=x\log\theta+(n-x)\log(1-\theta)+$const, so

$$\frac{d^2\log L}{d\theta^2}=-\frac{x}{\theta^2}-\frac{n-x}{(1-\theta)^2}.$$

Taking expectations with $E[X]=n\theta$:

$$I(\theta)=\frac{n\theta}{\theta^2}+\frac{n(1-\theta)}{(1-\theta)^2}=\frac{n}{\theta}+\frac{n}{1-\theta}=n\,\theta^{-1}(1-\theta)^{-1}.$$

Hence

$$\pi_J(\theta)\propto\theta^{-1/2}(1-\theta)^{-1/2},$$

which is the **proper** $\text{Beta}(\tfrac12,\tfrac12)$ distribution. Note: a Jeffreys prior can be proper!

## 5.5 The three Normal cases

- **N1 (mean, known variance):** $I(\theta)=n/\sigma^2\Rightarrow\pi_J(\theta)\propto1$ (improper uniform on $\mathbb{R}$).
- **N2 (variance, known mean):** $I(\theta)=n/(2\theta^2)\Rightarrow\pi_J(\theta)\propto\theta^{-1}$ (improper on $\mathbb{R}^+$).
- **N3 (both unknown):** the information matrix is block diagonal,
  $$I(\theta)=\begin{pmatrix}n/\sigma^2&0\\0&n/(2\sigma^4)\end{pmatrix}\Rightarrow\pi_J(\mu,\sigma^2)\propto\left[\frac{n}{\sigma^2}\cdot\frac{n}{2\sigma^4}\right]^{1/2}\propto\sigma^{-3}.$$

## 5.6 Objections

> [!warning] Two standard criticisms
> 1. **Data-dependence:** the Jeffreys prior depends on the likelihood $L(x\mid\theta)$ — i.e. on what data you *intend* to collect. A prior "should not" depend on the data.
> 2. **Non-factorisation:** $N3\ne N2\times N1$. If we think ignorance about $\mu$ and $\sigma^2$ should be represented by *independent* ignorance priors, then Jeffreys' rule disagrees. This motivates the product form $\pi(\mu,\sigma^2)=1/\sigma^2$ used in [[Normal Model with Unknown Mean and Variance]].

## 5.7 Extra worked example (geometric, Tutorial Q6)

For $p(x\mid\theta)=(1-\theta)^{x-1}\theta$, $\log L=(x-1)\log(1-\theta)+\log\theta$, so

$$\frac{d^2\log L}{d\theta^2}=-\frac{x-1}{(1-\theta)^2}-\frac1{\theta^2}.$$

With $E[X]=1/\theta$ (so $E[X-1]=\frac{1-\theta}{\theta}$):

$$I(\theta)=\frac{1}{\theta(1-\theta)}+\frac1{\theta^2}=\frac{1}{\theta^2(1-\theta)}\ \Longrightarrow\ \pi_J(\theta)\propto\theta^{-1}(1-\theta)^{-1/2}.$$

## Check your understanding

1. Give the two equivalent definitions of $I(\theta)$ and the intuition for it.
2. State the Jeffreys prior and explain in one sentence why it is invariant.
3. Derive the Jeffreys prior for the Binomial — is it proper or improper?
4. What is the factorisation objection to the Jeffreys prior?

### Answers

1. $I(\theta)=-E\!\left[\frac{d^2\log L}{d\theta^2}\right]=E\!\left[\left(\frac{d\log L}{d\theta}\right)^2\right]$; it is the expected curvature of the log-likelihood — large means the data are informative about $\theta$.
2. $\pi_J(\theta)\propto|I(\theta)|^{1/2}$; the $\tfrac12$ power is exactly what's needed so that the same rule yields the correct prior under any monotone reparameterisation.
3. $I(\theta)=n\theta^{-1}(1-\theta)^{-1}$, so $\pi_J\propto\theta^{-1/2}(1-\theta)^{-1/2}=\text{Beta}(\tfrac12,\tfrac12)$, which is **proper**.
4. $\pi_J(\mu,\sigma^2)\propto\sigma^{-3}$ does not equal the product of the single-parameter Jeffreys priors ($\propto\sigma^{-1}$ for the variance times a constant for the mean), contradicting the idea that independent ignorance should factorise.

---

# Topic 6: Maximum A Posteriori

## 6.1 Definition

The [[Maximum A Posteriori]] estimate is the **posterior mode**:

$$\hat\theta_{\text{MAP}}=\arg\max_\theta\log\pi(\theta\mid x)=\arg\max_\theta\big\{\log L(x\mid\theta)+\log\pi(\theta)\big\}.$$

Compare the [[Maximum Likelihood Estimation|MLE]]: $\hat\theta_{\text{MLE}}=\arg\max_\theta\log L(x\mid\theta)$.

## 6.2 The bridge to the MLE

MAP is the MLE **plus a penalty** $\log\pi(\theta)$ — a form of regularisation (it pulls the estimate toward high-prior-density regions). With a flat/uninformative prior, $\log\pi(\theta)$ is constant in $\theta$, so

$$\hat\theta_{\text{MAP}}=\hat\theta_{\text{MLE}}.$$

## 6.3 Worked example: coin tossing (Tutorial Q7)

$n$ tosses, $x$ heads, uniform prior $\theta\sim U(0,1)$ (i.e. $\text{Beta}(1,1)$):

- $\hat\theta_{\text{MLE}}=x/n$.
- Posterior is $\text{Beta}(1+x,\ 1+n-x)$; its mode is $\dfrac{(1+x)-1}{(1+x)+(1+n-x)-2}=\dfrac xn$, so $\hat\theta_{\text{MAP}}=x/n$ — same as the MLE.
- Posterior **mean** is $\dfrac{1+x}{2+n}$, shrunk slightly toward $1/2$.

This shows the three summaries can coincide (MLE = MAP) or differ (mean).

## 6.4 Bayesis gives more than a point

Bayesian inference also provides the posterior **mean**, **median**, and **mode**. These need not coincide. Which one you report depends on the [[Loss Functions|loss function]] — see [[Posterior Decision Theory]]. In particular: quadratic loss → mean; absolute loss → median; 0–1 loss → mode (which is why MAP is the Bayes estimator for 0–1 loss).

## Check your understanding

1. Write down $\hat\theta_{\text{MAP}}$ and show how it relates to the MLE.
2. When does MAP equal the MLE?
3. For the coin example with a uniform prior, why is $\hat\theta_{\text{MAP}}=x/n$ but the posterior mean is $(1+x)/(2+n)$?
4. Which loss function makes the posterior mode the optimal decision?

### Answers

1. $\hat\theta_{\text{MAP}}=\arg\max_\theta\{\log L(x\mid\theta)+\log\pi(\theta)\}$; it is the MLE with an added prior-penalty term.
2. When the prior is flat (constant in $\theta$), since then $\log\pi(\theta)$ drops out.
3. The posterior is $\text{Beta}(1+x,1+n-x)$; its mode is $x/n$ but its mean is $(1+x)/(2+n)$ because the uniform prior adds one pseudo-success and one pseudo-failure, shrinking the mean toward $1/2$.
4. 0–1 loss.

---

# Topic 7: Probability Integral Transform and Inversion Sampling

## 7.1 The Probability Integral Transform (PIT)

> [!abstract] Theorem
> If $X\sim F_X$ has CDF $F_X$, then $U=F_X(X)$ is uniformly distributed on $[0,1]$ (where $F_X^{-1}$ exists).

**Proof.** Let $U=F_X(X)$, so $u\in[0,1]$. Then

$$F_U(u)=\Pr(U\le u)=\Pr(F_X(X)\le u)=\Pr(X\le F_X^{-1}(u))=F_X(F_X^{-1}(u))=u,$$

which is the CDF of a $U(0,1)$ variable. $\blacksquare$

**The useful direction (inverted).** If $U\sim U(0,1)$ and we set $X=F_X^{-1}(U)$, then $X$ has CDF $F_X$. Check:

$$\Pr(X\le x)=\Pr(F_X^{-1}(U)\le x)=\Pr(U\le F_X(x))=\int_0^{F_X(x)}1\,du=F_X(x).\ \blacksquare$$

This is precisely the [[Inversion Sampling]] algorithm.

## 7.2 Inversion sampling algorithm

To draw $n$ samples from $F(x)$:

1. Draw $u_1,\dots,u_n\sim U(0,1)$.
2. Set $x_i=F^{-1}(u_i)$.
3. Return $x_1,\dots,x_n$ as i.i.d. samples from $F(x)$.

It is the natural way to sample from a [[Posterior Distribution|posterior]] whose CDF you can invert in closed form.

## 7.3 Worked example 1

$f(x)=3x^2$ on $(0,1)$. Then $F(x)=x^3$. Solve $u=x^3$:

$$x=u^{1/3}\sim f(x).$$

In R: `x = runif(5000)^(1/3)`.

## 7.4 Worked example 2 (piecewise)

$$f(x)=\begin{cases}(x-2)/2 & 2\le x\le 3\\ (2-x/3)/2 & 3<x\le 6\\ 0 & \text{otherwise}\end{cases}\qquad F(x)=\begin{cases}0 & x<2\\ (x-2)^2/4 & 2\le x\le 3\\ 1-\tfrac34(2-x/3)^2 & 3<x\le6\\ 1 & x>6\end{cases}$$

Inverting on each piece gives

$$F^{-1}(u)=\begin{cases}2+2\sqrt u & u\in(0,\tfrac14]\\[2pt] 6\left(1-\sqrt{(1-u)/3}\right) & u\in(\tfrac14,1)\end{cases}$$

```r
Finv = function(u){
  out = rep(0, length(u))
  ind = (u <= 0.25)
  out[ind]  = 2 + 2*sqrt(u[ind])
  out[!ind] = 6*(1 - sqrt((1 - u[!ind])/3))
  out
}
x = Finv(runif(5000))
```

## 7.5 Limitations

- Needs a **closed-form, invertible CDF**. For distributions like $\text{Beta}(2,2)$ numerical inversion is inefficient — use [[Rejection Sampling]] instead.
- Does **not** generalise well to [[Multivariate Bayesian Models|multivariate]] / non-standard posteriors (a CDF is not invertible in the same way).

## 7.6 Benefit and weakness (exam-style)

- **Benefit:** produces independent, exact samples; simple and fast when $F^{-1}$ is available.
- **Weakness:** restricted essentially to univariate distributions with an invertible closed-form CDF.

## Check your understanding

1. State the PIT and prove that $F_X(X)\sim U(0,1)$.
2. Why does $X=F_X^{-1}(U)$ have distribution $F_X$?
3. For $f(x)=3x^2$ on $(0,1)$, write down the inversion sampler.
4. Give one benefit and one weakness of inversion sampling.

### Answers

1. If $X\sim F_X$ then $F_X(X)\sim U(0,1)$; proof: $F_U(u)=\Pr(F_X(X)\le u)=\Pr(X\le F_X^{-1}(u))=u$.
2. Because $\Pr(F_X^{-1}(U)\le x)=\Pr(U\le F_X(x))=F_X(x)$.
3. Draw $u\sim U(0,1)$ and return $u^{1/3}$.
4. Benefit: independent exact samples. Weakness: needs a closed-form invertible CDF, so limited to (mostly univariate) cases.

---

## Connections

- **Builds on:** [[Normalising Constant]] · [[Conjugate Priors]] · [[Bayes Theorem]] · [[Likelihood Function]]
- **Leads to:** [[Exponential Family]] · [[Improper Priors]] · [[Fisher Information]] · [[Jeffreys Prior]] · [[Maximum A Posteriori]] · [[Probability Integral Transform]] · [[Inversion Sampling]]
- **See also:** [[Week 2 Overview]] · [[Conjugate Prior Reference Table]] · [[Tutorial Week 2]] · [[Rejection Sampling]] · [[Normal Model with Unknown Mean and Variance]]
