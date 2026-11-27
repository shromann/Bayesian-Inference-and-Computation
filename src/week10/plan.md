# Week 10: Mixture models, change-points, reaction times

Generated walkthrough plan — 29 scenes. Each scene is rendered at 480p15, subtitled, narrated, then stitched.

## 01. Week 10: Mixture models

Week 10 combines latent indicators with MCMC and predictive checking.

- Four stories: fitting mixtures, latent labels, temporal change, and a psychology application.
- Priors, hierarchies, MCMC and Bayes factors all reappear here.

## 02. What is a mixture distribution?

Combine component distributions with mixing weights.

- Male and female height densities combine into a bimodal-looking mixture.
- The mixture density is a weighted sum of component densities.
- Each observation is drawn from one of M components.

## 03. Why mixtures are useful

Flexible densities, classification, and cluster inference.

- Normal mixtures can approximate almost any continuous density.
- Latent labels tell us which subpopulation an observation belongs to.
- We may infer the number of clusters and their characteristics.

## 04. Why fitting mixtures is hard

The log of a sum destroys the usual simplifications.

- The sum sits inside the log, so log-likelihoods do not decompose.
- Standard conjugate updates disappear in the marginalised model.
- Latent labels are the key to restoring simple conditionals.

## 05. Latent indicator variables

One-hot encoding turns component membership into a random variable.

- Exactly one element of the vector z_i equals one.
- The prior probability that i belongs to component m is lambda_m.
- This is the trick that makes Gibbs sampling possible.

## 06. The joint likelihood

With z observed, the complete-data likelihood factorises.

- Only the component selected by z_im contributes for each observation.
- Multiplying by the indicator prior gives a clean product.
- The augmented model is much easier to work with.

## 07. Priors for the weights

Dirichlet is the multivariate Beta and is conjugate to multinomial labels.

- The Dirichlet lives on the simplex, so the weights sum to one.
- Each marginal weight is Beta distributed.
- All ones is a common non-informative specification.

## 08. Posterior with indicators

Three blocks of unknowns with three simple conditional updates.

- The augmented posterior exposes three tractable conditional structures.
- Gibbs cycles through component parameters, weights, and labels.
- This is the main motivation for introducing the indicators.

## 09. Gibbs step 1: component parameters

Given labels, each component is fitted only to its own observations.

- Only observations currently allocated to component m remain.
- This is just the standard posterior for that component's data.

## 10. Gibbs step 2: mixture weights

Dirichlet-multinomial conjugacy gives a direct Gibbs draw.

- Count how many observations are currently in each component.
- Posterior Dirichlet parameters are prior counts plus allocated counts.
- A straightforward conjugate update.

## 11. Gibbs step 3: latent labels

Each label is a categorical draw with posterior membership probabilities.

- Unnormalised weight is prior weight times component density.
- Draw a one-hot label with these normalised probabilities.
- Each observation can be updated separately.

## 12. Eyes data: fitted mixture

Peak sensitivity wavelengths of 2-component eye data.

- Posterior ordering mu1 < mu2 and weights near 60:40.
- Label probabilities near 545 nm are close to 0.5.
- MCMC explores uncertainty in component membership.

## 13. Posterior predictive simulation

Generate new observations by propagating posterior uncertainty.

- Sample parameters, then a component, then a new observation.
- The predictive density averages the mixture over the joint posterior.
- Only theta and lambda are needed for a new observation.

## 14. Classifying a future observation

Which component is a new value y most likely from?

- This is the conditional membership probability given parameters.
- Average this ratio over posterior draws.
- This gives a principled classification of future cases.

## 15. Classifying observed data

Two equivalent ways to estimate membership for an existing xi.

- Plug posterior draws into the conditional membership formula.
- If z_i was recorded, just count how often it was allocated to m.
- The Monte Carlo frequency estimates E[I(z_im=1)].

## 16. Label switching

A mixture is invariant to permuting the component labels.

- Any permutation of M labels gives the same mixture density.
- Label switching makes un constrained component inference meaningless.
- Ordering constraints select one representative permutation.

## 17. Change-point models

A mixture whose labels have temporal structure.

- Coal-mining disasters per year suggest a rate change around 1890.
- The change point tau is itself an unknown parameter.
- The posterior on tau answers 'when'; Bayes factors answer 'whether'.

## 18. Change-point: three questions

Existence, timing, and number of changes.

- A diffuse posterior on tau means the timing is not identified.
- The modal year is the estimated change point.
- Multiple change points extend the same idea.

## 19. Reaction times and schizophrenia

17 subjects, 30 trials each — a psychology application.

- 11 non-schizophrenic and 6 schizophrenic subjects.
- Two effects: general slowing and occasional long delays.

## 20. Psychological model

Two mechanisms produce slow responses in schizophrenic subjects.

- On some trials a schizophrenic subject has an attentional lapse.
- A general slowing applies to every response.
- We model log times since raw times are positive and skewed.

## 21. The basic hierarchical model

Individual effects plus a two-component mixture for schizophrenics.

- S_i is 0 for controls and 1 for schizophrenic subjects.
- These are the three parameters of primary interest.

## 22. Priors and identifiability

A sign constraint is needed for the delay parameter.

- Diffuse priors with a positive constraint on tau.
- The constraint breaks a symmetry and makes the model identifiable.
- A proper prior keeps inference well-defined in that case.

## 23. Posterior summaries

All three parameters show schizophrenic effects.

- Posterior medians with 2.5% and 97.5% quantiles in brackets.
- A typical 38% increase in response time from motor retardation.
- Attentional lapses roughly double the response time.

## 24. Posterior predictive checking

The model assumes equal variances — is that plausible?

- Compare observed spread statistics to predictive simulations.
- Some schizophrenic subjects are far more variable than the model allows.
- Predictive checking tells us how to improve the model.

## 25. An expanded model

Add individual susceptibility W_i and an extra variance component.

- Some subjects are prone to delays, and delayed trials have larger variance.
- The old model is nested inside the new one.
- More trials are delayed, but each delay is shorter.

## 26. Final comments on mixtures

Flexibility, latent variables, and model choice.

- Latent labels are the computational workhorse of mixture modelling.
- Both diagnostic and formal approaches are available.
- The tools from this course are the foundation for modern research.

## 27. Tutorial 10 Q1 — hierarchical normal model

School means with known sampling variances.

- A two-level normal hierarchy for the eight schools.
- The full conditional is a precision-weighted average of data and hypermean.
- Marginalising theta_j gives the marginal likelihood for the hyperparameters.
- Sample theta, mu and tau in a Gibbs-style scheme.

## 28. Tutorial 10 Q2 — two hospitals

A beta-binomial hierarchy for surgical mortality.

- Hospital 1: 3/97 deaths; Hospital 2: 18/148 deaths.
- The full conditional for each mortality rate is conjugate Beta.
- The hyperparameter conditional needs a non-conjugate update such as MH.
- Mortality looks higher in Hospital 2, but partly may be chance.

## 29. Tutorial 10 Q3 — mixture identifiability

A two-component mixture prior for school effects.

- Most schools near zero, a few strongly positive.
- Ordering or fixing labels prevents symmetry in the component posteriors.
- Marginalising theta_j gives a mixture of normals for the data.
- This posterior weight shows how each observation changes the classification.
