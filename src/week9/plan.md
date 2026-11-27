# Week 9: Optimal Bayesian updating and hierarchical models

Generated walkthrough plan — 23 scenes. Each scene is rendered at 480p15, subtitled, narrated, then stitched.

## 01. Week 9: Optimal learning and hierarchy

Week 9 has two halves: why Bayes is optimal, and how to model related units.

- First an information-theoretic justification, then hierarchical models.
- Bayes' rule is not just a convention — it solves an optimisation problem.

## 02. Kullback-Leibler divergence

KL divergence measures how far one distribution is from another.

- KL is an expected log-ratio under the first distribution.
- Nonnegativity follows from Jensen's inequality.
- The direction matters throughout this lecture.

## 03. Maximum likelihood minimises KL

As the sample size grows, the MLE is the closest model to the truth in KL.

- Maximise the log-likelihood; constants do not matter.
- The law of large numbers turns the average into an expectation.
- Subtracting the constant entropy of p_true converts the max into a KL min.

## 04. The Bayesian optimisation objective

We want a whole distribution over theta that stays close to the prior.

- Fit the data on average, but penalise moving too far from the prior.
- The data term by itself would collapse to a degenerate distribution.
- The prior term forbids point masses and enforces the prior's support.

## 05. Result: the posterior is optimal

The solution of that optimisation is exactly the standard Bayesian posterior.

- The optimum is prior times likelihood, normalised — Bayes' rule.
- Substituting Z into the objective turns it into one KL divergence.
- Bayesian updating is the optimal belief update in this information-theoretic sense.

## 06. Motivation: 12 hospitals

Cardiac surgery mortality rates across hospitals with very different sample sizes.

- Deaths per hospital range from 0 to 29 across 47 to 360 operations.
- Basic model component is binomial, but data are grouped by hospital.

## 07. Model 1: identical parameters

The extreme of pooling: every hospital shares one probability p.

- One node p feeds all hospitals; hospital labels are ignored.
- Pooling combines counts into one binomial likelihood.
- A Beta prior gives a conjugate Beta posterior.
- The pooled model ignores hospital-level differences entirely.

## 08. Model 2: separate parameters

The opposite extreme: each hospital has its own unrelated p_i.

- Each p_i has its own likelihood, but shares a fixed Beta(a,b) prior.
- Posteriors are independent given the fixed prior parameters.
- The prior variance controls how similar hospitals are forced to be.
- A fixed prior can have a huge effect on the posterior.

## 09. Model 3: a hierarchical model

Put a prior on the prior parameters and let the data estimate them.

- Three levels: data, hospital effects, and population hyperparameters.
- Hyperpriors on a and b complete the three-level model.
- Uncertainty about the population is propagated into each hospital.

## 10. Borrowing strength

Hyperparameters couple the hospitals without making them identical.

- The posterior on (a,b) gives population mean and between-hospital variability.
- Marginally the hospital effects share information through the hyperparameters.
- Small-sample hospitals are pulled toward the population mean.

## 11. Three ways to treat related units

Identical, separate, or exchangeable parameters.

- Assumption 1: no differences at all.
- Assumption 2: no shared structure and high variance.
- Assumption 3: a middle ground justified by exchangeability.

## 12. Exchangeability

Labels should not change the joint probability assignment.

- Permuting the indices leaves the joint distribution unchanged.
- Drawing without replacement from 1 red and 2 white balls is exchangeable.
- Dependence is allowed; only the ordering of labels is irrelevant.

## 13. de Finetti representation theorem

Exchangeability implies a hierarchical model without assuming one.

- An exchangeable sequence can be written as iid draws given a common theta.
- The representation introduces a latent parameter that induces dependence.
- Hierarchical models follow from exchangeability alone.

## 14. Arbitrary hierarchical depth

Exchangeability can be asserted at several structural levels.

- Student, school, state, national level — each conditionally independent at its level.
- The hierarchy is just a structured factorisation of the prior.
- Higher levels encode structural exchangeability judgements.

## 15. Shrinkage: the algebra

This is the precise form of borrowing strength.

- Normal data with a normal population distribution.
- The posterior mean is a weighted average of prior mean and observation.
- Noisy units (large s_i^2) shrink more toward mu.
- Shrinkage buys precision at the cost of some bias toward the group.

## 16. Education testing: eight schools

SAT coaching effects with very noisy school-level estimates.

- Estimated effects range from -3 to 28, with standard errors 9 to 18.
- Each school provides a noisy mean with known sampling variance.
- Naive separate analyses are inconclusive.

## 17. Why both extremes fail

Pooling and separating give contradictory answers about the same data.

- The pooled posterior is a precision-weighted average.
- Pooling gives N(7.7, 16.6) and a 95% interval of about (-0.5, 15.9).
- Both extremes force implausible statements; we need a compromise.

## 18. Hierarchical model for the schools

School effects are conditionally independent given the population parameters.

- A normal population distribution links the eight schools.
- The hierarchy interpolates between the two extremes.
-  diffusely specified hyperparameters let the data decide the amount of pooling.

## 19. Education testing: conclusions

Averaging over uncertainty in tau changes the conclusions.

- A coaching effect as large as 28 is unlikely once schools share information.
- The population coaching effect is positive but modest.
- Conditioning on the most likely tau^2 gives the wrong inference.

## 20. Tutorial 9 Q1-Q2 — normal and Poisson tests

Two Bayes-factor calculations with proper priors.

- H0: theta=3 vs H1: theta!=3 with prior N(1,1).
- The two normal densities give B01 about 3.82; posterior odds 5.7 with prior odds 1.5.
- H0: lambda=1 vs an Exp(2) alternative.
- Here the point null slightly outpredicts the diffuse alternative.

## 21. Tutorial 9 Q3-Q4 — binomial and calibration

An exact binomial factor and the calibration marginal likelihoods.

- With r=3 and n=10 the binomial coefficients cancel, giving B01=256.
- Both models share the same inverse-gamma prior on sigma^2.
- The evidences differ through the scale parameters a1 and a2.
- B12 is the ratio of these two integrated likelihoods.

## 22. Tutorial 9 Q5-Q6 — unknown variance and improper priors

A Bayes factor identity and the limits of improper priors.

- The unknown-variance Bayes factor depends on this total sum of squares.
- Conjugacy yields the stated closed-form Bayes factor.
- The evidence integral converges only when sum(x_i)-t+1 > 0.

## 23. Tutorial 9 Q7-Q8 — Jeffreys prior and partial factors

Asymptotic behaviour and cancelling arbitrary constants.

- Comparing N(0,1) to N(theta,1) with a flat prior on theta.
- Occam's razor emerges from the integration over theta.
- Partial Bayes factors remove the arbitrary scaling constant c2.
- Both averages remove the constant, but they behave differently as n grows.
