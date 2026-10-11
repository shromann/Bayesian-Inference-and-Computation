The change-of-variable mechanics
Start with the transformation $\phi = \theta^2$, so the inverse is
$$\theta = \sqrt{\phi} \quad\Longrightarrow\quad \frac{d\theta}{d\phi} = \frac{1}{2\sqrt{\phi}} = \frac{1}{2}\,\phi^{-1/2}.$$
A density transforms by the Jacobian of the inverse map:
$$\pi(\phi) = \pi\big(\theta(\phi)\big)\left|\frac{d\theta}{d\phi}\right|.$$
Plug in the flat prior $\pi(\theta)\propto 1$:
$$\pi(\phi) \propto 1 \cdot \frac{1}{2\sqrt{\phi}} \propto \frac{1}{\sqrt{\phi}}.$$
Why it's not flat
The key point: a flat prior in $\theta$ gives equal probability to equal widths $d\theta$. But equal widths $d\theta$ do not map to equal widths $d\phi$ — near $\phi=0$ the map $\theta=\sqrt\phi$ is steep ($d\theta/d\phi \to \infty$), so a unit interval in $\phi$ corresponds to a larger interval in $\theta$. Probability gets compressed toward small $\phi$, producing the $1/\sqrt\phi$ blow-up.
Formally, $\int \pi(\theta)\,d\theta \propto \theta$ is invariant, but probabilities must agree:
$$\Pr(a<\theta<b) = \int_a^b d\theta = \int_{a^2}^{b^2} \frac{1}{2\sqrt\phi}\,d\phi.$$
The integrand on the right is the induced density $1/(2\sqrt\phi)$ — flatness did not carry over.
The invariance fix (Jeffreys)
A prior that transforms consistently is $\pi(\theta)\propto\sqrt{\det I(\theta)}$, the Jeffreys prior, where $I$ is the Fisher information. Under reparameterisation it satisfies
$$\pi(\phi) = \pi(\theta)\left|\frac{d\theta}{d\phi}\right|$$
automatically, so "ignorance" is represented the same way in every coordinate system — unlike the flat prior, which is flat only in the coordinate you happened to pick.
One caveat worth noting: $\phi=\theta^2$ is not one-to-one (both $\pm\sqrt\phi$ map to the same $\phi$), so strictly one should split $\theta$ into branches or use $\theta\in[0,\infty)$. The Jacobian computation above holds locally on each branch.

Change of variables for probability densities
The core idea
A probability density is not a probability. It's a rate — probability per unit of the variable. So when you rescale the variable, you must rescale the rate to keep the actual probability the same.
The invariant quantity is probability mass over a region:
$$\Pr(\theta \in A) = \int_A \pi_\theta(\theta)\, d\theta.$$
Whatever happens to the density, this integral must stay the same.
Step 1 — Think in terms of tiny intervals
Take a one-to-one map $\phi = g(\theta)$, with inverse $\theta = g^{-1}(\phi)$.
The probability that $\theta$ lies in a small interval $[\theta, \theta + d\theta]$ equals the probability that $\phi$ lies in the corresponding interval:
$$\pi_\theta(\theta)\, d\theta = \pi_\phi(\phi)\, d\phi.$$
The two densities are joined by the rule "probability of the little slice is the same."
Step 2 — Relate the interval widths
From $\phi = g(\theta)$, a small change $d\theta$ produces a small change $d\phi$:
$$d\phi = g'(\theta)\, d\theta \quad\Longleftrightarrow\quad d\theta = \frac{1}{g'(\theta)}\, d\phi.$$
So the widths are related by the derivative — this is the Jacobian.
Step 3 — Solve for the new density
Substitute $d\theta$ into the invariant:
$$\pi_\theta(\theta)\, d\theta = \pi_\theta(\theta)\left|\frac{d\theta}{d\phi}\right| d\phi.$$
Since this must equal $\pi_\phi(\phi)\, d\phi$ for every interval:
$$\boxed{\;\pi_\phi(\phi) = \pi_\theta\big(\theta(\phi)\big)\left|\frac{d\theta}{d\phi}\right|\;}$$
Three parts to never forget:
1. Evaluate the old density at the inverse map $\theta(\phi)$, not at $\phi$.
2. Multiply by the absolute value of the Jacobian $\left|d\theta/d\phi\right|$.
3. Absolute value because densities are non-negative (handles decreasing maps).
Why the inverse Jacobian?
The transformation sends $\theta \to \phi$. But the density value at a point changes with the inverse map's slope, because you're asking "how much $\theta$-width fits into a unit of $\phi$-width."
- If the map is stretching ($|d\phi/d\theta| > 1$), then a unit of $d\theta$ becomes a big slice of $d\phi$, so the density must be smaller → multiply by $|d\theta/d\phi| < 1$.
- If the map is compressing ($|d\phi/d\theta| < 1$), a unit of $d\theta$ is squeezed into a tiny $d\phi$ slice, so the density is larger.
The Jacobian $\left|d\theta/d\phi\right| = 1/|g'(\theta)|$ exactly encodes this.
Worked example: $\phi = \theta^2$
Inverse: $\theta = \sqrt{\phi}$, so
$$\frac{d\theta}{d\phi} = \frac{1}{2\sqrt{\phi}}, \qquad \left|\frac{d\theta}{d\phi}\right| = \frac{1}{2\sqrt{\phi}}.$$
With flat prior $\pi_\theta(\theta)\propto 1$, evaluated at $\theta=\sqrt\phi$ it's still $1$:
$$\pi_\phi(\phi) = 1 \cdot \frac{1}{2\sqrt{\phi}} \propto \frac{1}{\sqrt\phi}.$$
Sanity check via CDF
The CDF must match: $\Pr(\phi \le t) = \Pr(\theta^2 \le t) = \Pr(-\sqrt t \le \theta \le \sqrt t) = 2\sqrt t$ (for flat $\theta$ on $[-c,c]$, up to constants). Differentiating:
$$\pi_\phi(t) = \frac{d}{dt}\left(2\sqrt t\right) = \frac{1}{\sqrt t} \propto \frac{1}{\sqrt\phi}.$$
Same answer. This is the best way to verify any transform: differentiate the CDF.
Operations checklist
Operation
Increasing map $g$
Multivariate $\boldsymbol\phi = g(\boldsymbol\theta)$
Non one-to-one (e.g. $\theta^2$)
The non-one-to-one wrinkle
$\phi=\theta^2$ gives two preimages $\theta = \pm\sqrt\phi$. Probability from both branches lands on the same $\phi$, so we add them:
$$\pi_\phi(\phi) = \pi_\theta(\sqrt\phi)\frac{1}{2\sqrt\phi} + \pi_\theta(-\sqrt\phi)\frac{1}{2\sqrt\phi} = \frac{\pi_\theta(\sqrt\phi)+\pi_\theta(-\sqrt\phi)}{2\sqrt\phi}.$$
If $\theta$ ranges over all of $\mathbb{R}$ with a symmetric flat prior, both terms contribute and you'd get a factor of 2 (still $\propto 1/\sqrt\phi$). If $\theta \ge 0$ only, just the first term. This is the caveat from before — always check whether the map is one-to-one.
Takeaway
Density transform = re-express the old density at the inverse point, then multiply by the inverse Jacobian, then (if needed) sum over branches.
Verify with the CDF. The reason it's not flat is that "flat" is an interval-width statement, and interval widths don't commute with nonlinear maps.