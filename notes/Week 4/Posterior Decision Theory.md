---
tags: [decision, week-4]
week: 4
type: concept
---

# Posterior Decision Theory

> [!abstract] One-line summary
> The posterior is the inference; decisions require an extra ingredient — a loss function. Choose the decision minimising expected posterior loss.

## Inference vs decision
$\pi(\theta\mid x)$ is a complete description of the inference about $\theta$. But for applications we often want:
1. The "best" point estimate $\hat\theta$ — see [[Loss Functions]].
2. The optimal decision $d^*\in\mathcal{D}=\{d_1,d_2,\dots\}$.
Examples: how many loaves of bread to bake; how high to build sea walls; how much rail infrastructure to build.

## Loss and expected posterior loss
A loss function $L(\theta,d)$ defines the penalty of decision $d$ when the parameter is $\theta$ (negative loss = gain; utility $U=-L$). If $\theta$ were known,
$$d^*=\arg\min_d L(\theta,d).$$
But $\theta\sim\pi(\theta\mid x)$, so we minimise the **expected posterior loss**:
$$\boxed{d^*=\arg\min_d \mathbb{E}_\pi[L(\theta,d)]=\arg\min_d\int_\Theta L(\theta,d)\,\pi(\theta\mid x)\,d\theta.}$$

## A full Bayesian decision problem
> [!important] Three ingredients
> 1. Prior distribution $\pi(\theta)$
> 2. Model $f(x\mid\theta)$ (likelihood $L(x\mid\theta)$)
> 3. Loss function $L(\theta,d)$
>
> Most people stop at the first two; decisions require the third.

## Examples
- **Sea walls:** $L(\theta,d_h)=C(h)+K\Pr(\text{wall exceeded in 50y}\mid\theta,h)$; balance construction cost against failure impact. Taller walls cost more to build but reduce breach chance. See [[Loss Functions]].
- **Baking loaves:** profit model reduces to **linear loss**, so the optimal stock is a posterior quantile. See [[Loss Functions]].

## Connections
- **Builds on:** [[Posterior Distribution]] · [[Posterior Inference]]
- **Leads to:** [[Loss Functions]] · [[Credible Intervals]] (intervals as decisions)
- **See also:** [[Bayesian Predictive Distribution]]

## Source
- [[Lecture Week 4.pdf]], slides 4–7, 14–15
