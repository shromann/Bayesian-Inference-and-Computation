# Week 8: Hypothesis testing, Bayes factors, coherence

Generated walkthrough plan — 20 scenes. Each scene is rendered at 480p15, subtitled, narrated, then stitched.

## 01. Week 8: Testing, Bayes factors, coherence

Week 8 asks how to compare hypotheses and models, and why Bayesian updating is coherent.

- Four ideas: test hypotheses, compare models, check sensitivity, update sequentially.
- The Bayes factor will be the central object of the lecture.

## 02. Simple null vs simple alternative

Jeffreys' test: put prior probabilities on two point hypotheses and use Bayes' theorem.

- Two mutually exclusive, exhaustive point hypotheses.
- Bayes' theorem gives the posterior probability of the null.
- Posterior odds = Bayes factor x prior odds.
- No significance level, and no awkward 'fail to reject' language.

## 03. Worked example: two point hypotheses

Normal data with known variance and two candidate means.

- The sample mean is sufficient; T|H0 is N(0,1/n) and T|H1 is N(1,1/n).
- With equal prior odds, the posterior odds collapse to this exponential.
- At xbar = 2 the odds are 3.1e-7, so H1 is overwhelmingly favoured.
- The log-odds are linear in xbar; the switch-over point is exactly xbar = 1/2.

## 04. Simple null vs composite alternative

Now the alternative is a whole range of parameter values with a prior attached.

- The alternative spreads its prior across all theta not equal to theta0.
- The denominator is an average likelihood under H1, weighted by its prior.
- This averaging is what makes Bayes factors automatically penalise flexibility.

## 05. Composite example: the integral worked out

The same normal model, but theta under H1 has a N(1,1) prior.

- Complete the square in the exponent to perform the integral analytically.
- The posterior odds reduce to this closed form.
- Evidence strongly favours the alternative; the integral is centred near 1.

## 06. Extra parameters and composite nulls

A hypothesis is a subset of the parameter space; nuisance parameters are integrated out.

- Integrate over sigma^2 under each hypothesis to get marginal likelihoods.
- Both numerator and denominator marginalise the nuisance variance.
- For a composite null, integrate the same prior over two disjoint regions.

## 07. The encompassing model

To compare many models, embed them all in one joint model indexed by m.

- The augmented parameter records both the model label and its parameters.
- The prior factorises into a within-model prior and a model prior.
- Prior probabilities of overlapping model features must be added carefully.

## 08. Three regression models

Predicting building electricity use from temperature.

- Linear, quadratic, and a heavy-tailed error variant.
- On hot days consumption can rise again, motivating the quadratic term.
- Different dimensions and interpretations make priors hard to compare naively.

## 09. Marginal likelihood = evidence

The normalising constant of each model is the key to model probabilities.

- The evidence is the average likelihood over the prior.
- The joint posterior factorises into parameter and model posteriors.
- Posterior model probability is prior model probability reweighted by evidence.
- Model averaging propagates model uncertainty into predictions.

## 10. Experiment calibration example

Are measurement errors centred on zero, or is the device miscalibrated?

- Model 1 has unknown mean and variance with a normal-inverse-gamma prior.
- Model 2 fixes the mean at zero and uses the same marginal prior for sigma^2.
- The marginal likelihoods differ only through these updated scale parameters.
- Posterior model probabilities follow directly from the two evidences.

## 11. Bayes factors: the normalising constant cancels

When there are many models, compare pairs instead of computing every posterior probability.

- The common m(x) cancels, leaving prior odds times the Bayes factor.
- The Bayes factor is the ratio of marginal likelihoods.
- With two models, posterior probability increases whenever B12 > 1.

## 12. Bayes factor example: exponential vs truncated normal

Two nonnegative likelihoods with the same Gamma prior on theta.

- Both models use the same Gamma(t,b) prior on the rate.
- The ratio has a compact form with three pieces.
- A is a Gamma-ratio, B uses the mean square, C uses the sample mean.

## 13. Bayes factors for nested models

The smaller model is the larger model at a special parameter value.

- Nested means the small model is a slice of the large one at phi0.
- The prior is a spike at phi0 plus a density elsewhere.
- The Bayes factor is the posterior-to-prior density ratio at phi0.

## 14. Computing marginal likelihoods

Evidence is an integral; Monte Carlo estimates need care.

- Prior Monte Carlo is cheap but wasteful for diffuse priors.
- Importance sampling is efficient when g is close to the posterior.
- A ratio of unbiased evidence estimates is itself biased.
- The harmonic mean estimator is not recommended in practice.

## 15. Bayes factor sensitivity to vague priors

Diffuse priors can make Bayes factors behave strangely.

- Spreading a uniform prior thinner shrinks the evidence.
- The posterior stabilises but the prior density goes to zero, so B01 diverges.
- Jeffreys' improper variance prior always favours the smaller model.
- Careful prior choice and sensitivity analysis are essential.

## 16. Sequential updating and coherence

Bayesian updating gives the same answer no matter how data are batched.

- Use each posterior as the next prior when blocks arrive sequentially.
- Coherence means the order of the two loss contributions is irrelevant.
- Bissiri et al.: only the exponential form is coherent.
- With log-likelihood loss, coherence follows from commutativity of multiplication.

## 17. Partial Bayes factors remove sensitivity

Split data into a training block and a test block.

- Evidence factorises into a training term and a conditional term.
- The full Bayes factor is the product of two partial factors.
- Any arbitrary multiplicative constant cancels in the partial Bayes factor.
- Training-sample methods make model comparison robust to vague priors.

## 18. Tutorial 8 Q1 — detailed balance

Verify that Metropolis-Hastings satisfies detailed balance in both cases.

- The transition kernel is proposal times acceptance probability.
- For a stay, both sides are identical, so balance holds trivially.
- Multiplying out gives a symmetric minimum.
- Swapping theta and theta* leaves the expression unchanged.

## 19. Tutorial 8 Q2 — log-scale random walk

For a positive parameter, propose on the log scale and transform back.

- The transformed target picks up the Jacobian e^phi.
- The proposal is symmetric on the log scale, so only the target ratio remains.
- Back on the theta scale this is the familiar ratio with an extra theta factor.
- The lognormal ratio q(theta*,theta)/q(theta,theta*) equals theta*/theta.

## 20. Tutorial 8 Q3 — reversible Gibbs

Palindromic scan orders make a deterministic Gibbs sampler reversible.

- Chain the kernels in a forward-then-backward order.
- Each Pi preserves pi, and reversing a palindromic product reproduces it.
- Hence the combined kernel satisfies detailed balance.
- A reversible deterministic-scan Gibbs sampler updates in palindromic order.
