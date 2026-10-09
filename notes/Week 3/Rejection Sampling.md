---
tags: [monte-carlo, sampling, week-3]
week: 3
type: concept
---

# Rejection Sampling

> [!abstract] One-line summary
> Sample from an easy proposal $g$ and accept with probability $f(x)/(Kg(x))$. The accepted points are exact samples from the target $f$.

## Idea
We want samples from $f(x)$, but that is hard. Instead:
1. Sample $x^*\sim g(x)$ from an easy distribution.
2. Accept $x^*$ with a probability chosen so accepted points follow $f$.

## Bounding requirement
Choose $g$ and a constant $K>0$ with
$$f(x)\le K\,g(x)\quad\forall x.$$
$g(x)$ is any easy-to-simulate density; $K$ must satisfy the bound.

## Algorithm (two equivalent forms)
**Version 1**
1. Generate $x^*\sim g(x)$.
2. Generate $y^*\sim U(0,Kg(x^*))$.
3. Accept $x^*$ if $y^*\le f(x^*)$.

**Version 2**
1. Generate $x^*\sim g(x)$.
2. Accept $x^*$ with probability $\dfrac{f(x^*)}{Kg(x^*)}$.

> [!note] Why they are the same
> Under Version 1, $\Pr(\text{accept }x^*)=\Pr(y^*\le f(x^*))=\int_0^{f(x^*)}\frac{1}{Kg(x^*)}\,dz=\frac{f(x^*)}{Kg(x^*)}$.

## Why it works
With acceptance probability $h(x)=f(x)/(Kg(x))$,
$$\Pr(X\le x\mid X\text{ accepted})=\frac{\int_{-\infty}^x h(y)g(y)\,dy}{\int_{-\infty}^\infty h(y)g(y)\,dy}=\frac{\int_{-\infty}^x f(y)\,dy}{\int_{-\infty}^\infty f(y)\,dy},$$
which is the CDF of $f$. So accepted values have pdf $f$. Note $f$ need **not** be normalised — only known up to proportionality (constants cancel in ratios).

## Efficiency and choosing $K$
$$\Pr(X\text{ accepted})=\int h(y)g(y)\,dy=\frac1K\int f(y)\,dy\propto\frac1K.$$
- Want $K$ as small as possible subject to $f\le Kg$.
- Optimal choice: $K=\max_x f(x)/g(x)$, giving maximum acceptance probability 1.
- Accuracy improves as $g$ gets closer to $f$ (smaller $K$).

## Worked example
Target $f(x)\propto x(1-x)^3$ on $[0,1]$, proposal $g(x)=U(0,1)$ (so $g=1$).
$$K=\max_x f(x).\qquad f'(x)=(1-x)^2(1-4x)=0\Rightarrow x=\tfrac14,$$
$$K=f(1/4)=\tfrac14(3/4)^3=\tfrac{27}{256}.$$
```r
L <- 5000; K <- 27/256
xstar <- runif(L)
ind <- (runif(L) < (xstar*(1-xstar)^3/K))
hist(xstar[ind], probability = TRUE)
```

Efficiency example (target $\text{Beta}(2,2)$): proposal $\text{Beta}(1,1)$ gives efficiency 0.681; proposal $\text{Beta}(1.5,1.5)$ gives 0.848.

## Connections
- **Builds on:** [[Monte Carlo Integration]] · [[Inversion Sampling]] (when inversion is inefficient)
- **Leads to:** [[Importance Sampling]] (the "keep everything and weight" variant)
- **See also:** [[Effective Sample Size]]

## Source
- [[Lecture Week 3.pdf]], slides 39–48
- [[Lecture Week 4.pdf]], slides 31–33
