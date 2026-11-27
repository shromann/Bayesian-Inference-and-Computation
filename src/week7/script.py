"""Week 7 Bayesian Inference and Computation — animated explainer (Manim CE)."""

from manim import *
import math
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from speech import spoken_duration

# ---------------------------------------------------------------------------
# Shared visual language
# ---------------------------------------------------------------------------
BG = "#1C1C1C"
BLUE = "#58C4DD"
GREEN = "#83C167"
YELLOW = "#FFFF00"
GREY = "#888888"
RED = "#FF6B6B"
PINK = "#FF9EC4"
MONO = "Menlo"

TITLE_SIZE = 48
HEAD_SIZE = 36
BODY_SIZE = 30
LABEL_SIZE = 24
CAP_SIZE = 20
FAST = 0.6
NORMAL = 1.3
SLOW = 2.2


def base(scene):
    scene.camera.background_color = BG


def cap(scene, text, duration=6.0):
    """Subtitle via Manim's SRT track, held long enough for natural narration."""
    duration = max(duration, spoken_duration(text, base=6.0))
    if hasattr(scene, "add_subcaption"):
        scene.add_subcaption(text, duration=duration)
    scene.wait(duration)


def clean(scene):
    # Tail hold lets the final subtitle run its full spoken duration.
    scene.wait(2.0)
    if scene.mobjects:
        scene.play(FadeOut(Group(*scene.mobjects)), run_time=0.5)
    scene.wait(0.3)


def fit(obj, max_w=12.0, max_h=2.6):
    """Scale any mobject into the safe frame so text never clips."""
    if obj.width > 0 and obj.height > 0:
        k = min(1.0, max_w / obj.width, max_h / obj.height)
        if k < 1.0:
            obj.scale(k)
    return obj


def txt(s, size=BODY_SIZE, color=WHITE, weight=None):
    kwargs = dict(font=MONO, font_size=size, color=color)
    if weight is not None:
        kwargs["weight"] = weight
    return fit(Text(s, **kwargs))


def maths(tex, size=BODY_SIZE, color=WHITE):
    return fit(MathTex(tex, font_size=size, color=color), max_h=2.0)


def formula(*parts, size=BODY_SIZE, color=WHITE, spacing=0.25):
    group = VGroup(*[MathTex(p, font_size=size, color=color) for p in parts]).arrange(DOWN, buff=spacing)
    return fit(group, max_h=3.0)


def card(title, body, width=4.2, height=1.7, color=BLUE):
    box = RoundedRectangle(corner_radius=0.12, width=width, height=height,
                           color=color, stroke_width=2, fill_color=color, fill_opacity=0.08)
    t = fit(txt(title, size=LABEL_SIZE, color=color, weight=BOLD), max_w=width - 0.3, max_h=0.6)
    b = fit(txt(body, size=CAP_SIZE, color=WHITE), max_w=width - 0.3, max_h=0.7)
    t.move_to(box.get_top() + DOWN * 0.32)
    b.move_to(box.get_bottom() + UP * 0.38)
    return VGroup(box, t, b)


def chain_line(axes, ys, color=BLUE, width=2.0):
    pts = [axes.c2p(i, y) for i, y in enumerate(ys)]
    path = VMobject(color=color, stroke_width=width)
    path.set_points_as_corners(pts)
    return path


def axes_pair(x_range, y_range, width=5.2, height=2.4):
    return Axes(x_range=x_range, y_range=y_range, x_length=width, y_length=height, tips=False)


def label_axes(axes, xlab, ylab):
    x = txt(xlab, size=CAP_SIZE, color=GREY).next_to(axes.x_axis.get_end(), RIGHT, buff=0.1)
    y = txt(ylab, size=CAP_SIZE, color=GREY).next_to(axes.y_axis.get_end(), UP, buff=0.1)
    return VGroup(x, y)


def normal_rw_chain(n=180, rho=0.8, seed=7):
    rng = random.Random(seed)
    x, y = 10.0, 0.0
    xs, ys, acc = [x], [y], 0
    for _ in range(n):
        px, py = x + rng.gauss(0, math.sqrt(0.2)), y + rng.gauss(0, math.sqrt(0.2))
        logr = -0.5 * ((px * px + py * py - 2 * rho * px * py) - (x * x + y * y - 2 * rho * x * y)) / (1 - rho * rho)
        if math.log(rng.random()) < logr:
            x, y, acc = px, py, acc + 1
        xs.append(x)
        ys.append(y)
    return xs, ys, acc / n


# ---------------------------------------------------------------------------
# 1. Roadmap
# ---------------------------------------------------------------------------
class S01_Roadmap(Scene):
    def construct(self):
        base(self)
        title = txt("Week 7: MCMC beyond Gibbs", size=TITLE_SIZE, color=BLUE, weight=BOLD)
        self.play(Write(title), run_time=1.5)
        cap(self, "Week 7 has three connected stories: a better sampler, a graph language, and software that uses both.")

        cards = VGroup(
            card("1  METROPOLIS–HASTINGS", "sample what Gibbs cannot", color=BLUE),
            card("2  DAGs", "read conditional independence", color=GREEN),
            card("3  rJAGS", "let the DAG write the sampler", color=YELLOW),
        ).arrange(DOWN, buff=0.35).scale(0.92)
        self.play(LaggedStart(*[FadeIn(c, shift=RIGHT * 0.4) for c in cards], lag_ratio=0.25), run_time=2.0)
        cap(self, "First we fix Gibbs; then we learn to describe a model visually; then JAGS turns that picture into samples.")

        q = txt("What if the full conditional has no easy sampler?", size=HEAD_SIZE, color=YELLOW)
        q.next_to(cards, DOWN, buff=0.5)
        self.play(FadeIn(q), run_time=1.0)
        cap(self, "The question that motivates everything today.")
        clean(self)


# ---------------------------------------------------------------------------
# 2. Gibbs recap
# ---------------------------------------------------------------------------
class S02_GibbsRecap(Scene):
    def construct(self):
        base(self)
        h = txt("Gibbs: sweep through full conditionals", size=HEAD_SIZE, color=BLUE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Write(h), run_time=1.2)
        cap(self, "Gibbs sampling updates one coordinate at a time, using the most up-to-date values of the others.")

        ax = axes_pair([-3, 3, 1], [-3, 3, 1], width=5.4, height=4.4).shift(LEFT * 2.4)
        labs = label_axes(ax, "θ1", "θ2")
        ell = VGroup(
            Ellipse(width=4.2, height=2.1, color=BLUE, stroke_opacity=0.55),
            Ellipse(width=3.2, height=1.6, color=BLUE, stroke_opacity=0.35),
            Ellipse(width=2.2, height=1.1, color=BLUE, stroke_opacity=0.2),
        ).rotate(PI / 4).move_to(ax.get_center())
        self.play(Create(ax), FadeIn(labs), Create(ell), run_time=1.8)
        cap(self, "Target: a bivariate normal with correlation ρ = 0.8. The contours tilt because the coordinates are coupled.")

        rng = random.Random(3)
        x, y = 2.6, -1.6
        pts = [(x, y)]
        for _ in range(26):
            x = rng.gauss(0.8 * y, math.sqrt(1 - 0.64))
            pts.append((x, y))
            y = rng.gauss(0.8 * x, math.sqrt(1 - 0.64))
            pts.append((x, y))
        dots = VGroup(*[Dot(ax.c2p(px, py), radius=0.045, color=GREEN) for px, py in pts])
        segs = VGroup(*[Line(ax.c2p(pts[i][0], pts[i][1]), ax.c2p(pts[i + 1][0], pts[i + 1][1]),
                             color=GREEN, stroke_opacity=0.55, stroke_width=2) for i in range(len(pts) - 1)])
        self.play(LaggedStart(Create(segs), FadeIn(dots), lag_ratio=0.4), run_time=3.5)
        cap(self, "Each horizontal move samples θ1 given θ2; each vertical move samples θ2 given the new θ1.")

        note = VGroup(
            txt("θ1 | θ2 ~ N(ρθ2, 1−ρ²)", size=LABEL_SIZE, color=BLUE),
            txt("θ2 | θ1 ~ N(ρθ1, 1−ρ²)", size=LABEL_SIZE, color=BLUE),
        ).arrange(DOWN, buff=0.2).to_edge(RIGHT, buff=0.5)
        self.play(FadeIn(note), run_time=1.0)
        cap(self, "For this model the full conditionals are available, so Gibbs moves axis by axis.")
        clean(self)


# ---------------------------------------------------------------------------
# 3. Why MH
# ---------------------------------------------------------------------------
class S03_WhyMH(Scene):
    def construct(self):
        base(self)
        h = txt("When Gibbs breaks down", size=TITLE_SIZE, color=RED, weight=BOLD).to_edge(UP, buff=0.6)
        self.play(Write(h), run_time=1.2)
        cap(self, "Gibbs needs a sample from every full conditional. That is often the hardest part of the problem.")

        rows = VGroup(
            card("INVERSION", "univariate + normalisable CDF", color=BLUE),
            card("REJECTION", "needs a good envelope g and tight K", color=GREEN),
            card("IMPORTANCE", "weighted samples cannot enter Gibbs", color=YELLOW),
        ).arrange(DOWN, buff=0.3).scale(0.9)
        self.play(LaggedStart(*[FadeIn(r, shift=LEFT * 0.3) for r in rows], lag_ratio=0.25), run_time=2.2)
        cap(self, "Inversion needs an invertible CDF; rejection needs a good proposal; importance sampling gives weights, not draws.")

        crosses = VGroup(*[Cross(r, stroke_color=RED, stroke_width=3) for r in rows])
        self.play(LaggedStart(*[Create(c) for c in crosses], lag_ratio=0.2), run_time=1.6)
        cap(self, "In a complicated model, none of these is reliably available.")

        need = txt("Need: arbitrary blocks + unnormalised π", size=HEAD_SIZE, color=YELLOW).next_to(rows, DOWN, buff=0.5)
        self.play(FadeIn(need), run_time=1.0)
        cap(self, "We want a method that works for arbitrary blocks and only knows π up to proportionality.")
        clean(self)


# ---------------------------------------------------------------------------
# 4. MH loop
# ---------------------------------------------------------------------------
class S04_MHLoop(Scene):
    def construct(self):
        base(self)
        h = txt("Metropolis–Hastings: propose, then decide", size=HEAD_SIZE, color=BLUE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Write(h), run_time=1.1)
        cap(self, "MH replaces an exact conditional draw with an easy proposal and a carefully chosen accept–reject step.")

        cur = card("CURRENT", "θ^t", color=BLUE).shift(LEFT * 4.3)
        prop = card("PROPOSE", "θ* ~ q(θ | θ^t)", color=GREEN).shift(UP * 1.2)
        u = card("DRAW", "u ~ Uniform(0,1)", color=YELLOW).shift(DOWN * 1.2)
        acc = card("ACCEPT", "θ^{t+1} = θ*", color=GREEN).shift(RIGHT * 4.2 + UP * 1.2)
        rej = card("REJECT", "θ^{t+1} = θ^t", color=RED).shift(RIGHT * 4.2 + DOWN * 1.2)

        a1 = Arrow(cur.get_right(), prop.get_left(), color=GREY)
        a2 = Arrow(cur.get_right(), u.get_left(), color=GREY)
        a3 = Arrow(prop.get_right(), acc.get_left(), color=GREEN)
        a4 = Arrow(u.get_right(), rej.get_left(), color=RED)
        self.play(FadeIn(cur), Create(a1), FadeIn(prop), run_time=1.3)
        cap(self, "Step 1: propose a candidate from a distribution q that we can easily sample from.")
        self.play(Create(a2), FadeIn(u), run_time=1.0)
        cap(self, "Step 2: draw a uniform random number to make the decision probabilistic.")
        self.play(Create(a3), Create(a4), FadeIn(acc), FadeIn(rej), run_time=1.3)
        cap(self, "Step 3: accept the candidate with probability α, otherwise stay exactly where you are.")

        alpha = formula(
            r"\alpha(\theta,\theta^*)=\min\left\{1,\ \frac{\pi(\theta^*)\,q(\theta\mid\theta^*)}{\pi(\theta)\,q(\theta^*\mid\theta)}\right\}",
            size=34, color=YELLOW,
        ).to_edge(DOWN, buff=0.4)
        self.play(Write(alpha), run_time=1.8)
        cap(self, "The acceptance ratio compares target-and-proposal mass in both directions. Normalising constants cancel.")
        clean(self)


# ---------------------------------------------------------------------------
# 5. Random-walk demo
# ---------------------------------------------------------------------------
class S05_RandomWalkDemo(Scene):
    def construct(self):
        base(self)
        h = txt("Random-walk MH in action", size=HEAD_SIZE, color=BLUE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Write(h), run_time=1.0)
        cap(self, "Same bivariate target, but now proposals are small isotropic normal jumps around the current point.")

        ax = axes_pair([-3, 12, 2], [-3, 3, 1], width=6.2, height=3.3).shift(LEFT * 2.6 + DOWN * 0.4)
        ell = VGroup(*[Ellipse(width=w, height=hgt, color=BLUE, stroke_opacity=o)
                       for w, hgt, o in [(4.2, 2.1, 0.5), (3.0, 1.5, 0.3)]]).rotate(PI / 4).move_to(ax.c2p(0, 0))
        self.play(Create(ax), Create(ell), run_time=1.4)
        cap(self, "The chain starts far away at θ0 = (10, 0); the target is centred at zero.")

        xs, ys, rate = normal_rw_chain()
        dots = VGroup()
        for i in range(0, len(xs), 3):
            dots.add(Dot(ax.c2p(xs[i], ys[i]), radius=0.025, color=GREEN, fill_opacity=0.7))
        path = VMobject(color=GREEN, stroke_opacity=0.5, stroke_width=1.5)
        path.set_points_as_corners([ax.c2p(x, y) for x, y in zip(xs, ys)])
        self.play(Create(path), FadeIn(dots), run_time=4.0)
        cap(self, "Most small steps are accepted; the chain diffuses toward the high-density region and then wanders inside it.")

        trace = axes_pair([0, 180, 40], [-3, 11, 3], width=3.6, height=2.4).shift(RIGHT * 3.7 + UP * 0.7)
        line = chain_line(trace, xs[:180], color=BLUE, width=1.6)
        self.play(Create(trace), Create(line), run_time=1.6)
        cap(self, "The trace shows slow mixing: neighbouring draws are highly correlated because proposals are local.")

        stats = VGroup(
            txt("acceptance ≈ 70%", size=LABEL_SIZE, color=YELLOW),
            txt("only ~1409 / 2000 unique", size=CAP_SIZE, color=GREY),
        ).arrange(DOWN, buff=0.2).shift(RIGHT * 3.7 + DOWN * 1.4)
        self.play(FadeIn(stats), run_time=1.0)
        cap(self, "High acceptance is not automatically good: many repeated states mean a large autocorrelated sample.")
        clean(self)


# ---------------------------------------------------------------------------
# 6. Detailed balance
# ---------------------------------------------------------------------------
class S06_DetailedBalance(Scene):
    def construct(self):
        base(self)
        h = txt("Why the accept step works: detailed balance", size=HEAD_SIZE, color=BLUE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Write(h), run_time=1.1)
        cap(self, "A Markov chain has π as its stationary distribution if probability flow out of each state equals flow in.")

        a = Circle(radius=0.55, color=BLUE).shift(LEFT * 3.2)
        b = Circle(radius=0.55, color=GREEN).shift(RIGHT * 3.2)
        at = txt("θ", size=HEAD_SIZE, color=BLUE).move_to(a.get_center())
        bt = txt("θ*", size=HEAD_SIZE, color=GREEN).move_to(b.get_center())
        pa = VGroup(Rectangle(width=1.4, height=0.9, color=BLUE, fill_color=BLUE, fill_opacity=0.4),
                    txt("π(θ) = 0.7", size=CAP_SIZE)).shift(LEFT * 3.2 + DOWN * 1.6)
        pb = VGroup(Rectangle(width=1.4, height=0.9, color=GREEN, fill_color=GREEN, fill_opacity=0.4),
                    txt("π(θ*) = 0.3", size=CAP_SIZE)).shift(RIGHT * 3.2 + DOWN * 1.6)
        self.play(Create(a), Create(b), FadeIn(at), FadeIn(bt), FadeIn(pa), FadeIn(pb), run_time=1.5)
        cap(self, "Imagine two states with stationary probabilities 0.7 and 0.3.")

        f1 = Arrow(a.get_right() + UP * 0.1, b.get_left() + UP * 0.1, color=BLUE, stroke_width=4)
        f2 = Arrow(b.get_left() + DOWN * 0.1, a.get_right() + DOWN * 0.1, color=GREEN, stroke_width=2)
        self.play(Create(f1), Create(f2), run_time=1.2)
        cap(self, "At equilibrium, the flow from θ to θ* must equal the flow back: π(θ)P(θ,θ*) = π(θ*)P(θ*,θ).")

        eq = formula(r"\underbrace{\pi(\theta)q(\theta,\theta^*)}_{\text{too large}}",
                     r"\;\neq\;\underbrace{\pi(\theta^*)q(\theta^*,\theta)}_{\text{too small}}",
                     size=32, color=YELLOW).to_edge(DOWN, buff=0.5)
        self.play(Write(eq), run_time=1.4)
        cap(self, "An arbitrary proposal q does not balance these flows. The acceptance probability α repairs it.")
        clean(self)


# ---------------------------------------------------------------------------
# 7. Deriving alpha
# ---------------------------------------------------------------------------
class S07_DeriveAlpha(Scene):
    def construct(self):
        base(self)
        h = txt("Deriving the acceptance probability", size=HEAD_SIZE, color=BLUE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Write(h), run_time=1.0)
        cap(self, "Suppose the forward weighted proposal is larger than the backward one. We must slow the forward move or speed up the return.")

        lhs = formula(r"\pi(\theta)q(\theta,\theta^*) > \pi(\theta^*)q(\theta^*,\theta)",
                      size=34, color=YELLOW).shift(UP * 1.4)
        self.play(Write(lhs), run_time=1.4)
        cap(self, "Assume, without loss of generality, that the forward flow is too large.")

        steps = VGroup(
            formula(r"\pi(\theta)q(\theta,\theta^*)\alpha(\theta,\theta^*) = \pi(\theta^*)q(\theta^*,\theta)\alpha(\theta^*,\theta)", size=28, color=WHITE),
            txt("Set α(θ*, θ) = 1 — maximise the return trip.", size=LABEL_SIZE, color=GREEN),
            formula(r"\Rightarrow\ \alpha(\theta,\theta^*) = \frac{\pi(\theta^*)q(\theta^*,\theta)}{\pi(\theta)q(\theta,\theta^*)}", size=30, color=WHITE),
            formula(r"\Rightarrow\ \alpha(\theta,\theta^*) = \min\left\{1, \frac{\pi(\theta^*)q(\theta^*,\theta)}{\pi(\theta)q(\theta,\theta^*)}\right\}", size=30, color=YELLOW),
        ).arrange(DOWN, buff=0.35).shift(DOWN * 0.9)
        for i, s in enumerate(steps):
            self.play(FadeIn(s, shift=UP * 0.2), run_time=1.0)
            cap(self, [
                "Balance the two flows after multiplying each by its acceptance probability.",
                "The return move is already too rare, so never reject it.",
                "Solving gives the ratio needed on the forward move.",
                "In general cap the ratio at one: accept everything, or accept proportionally.",
            ][i], duration=2.0)
            self.wait(0.8)
        clean(self)


# ---------------------------------------------------------------------------
# 8. Verify balance
# ---------------------------------------------------------------------------
class S08_VerifyBalance(Scene):
    def construct(self):
        base(self)
        h = txt("Verification: the min makes it symmetric", size=HEAD_SIZE, color=BLUE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Write(h), run_time=1.1)
        cap(self, "Now check that this choice really satisfies detailed balance, for both distinct states and stays.")

        lhs = formula(r"\pi(\theta)P(\theta,\theta^*) = \pi(\theta)q(\theta,\theta^*)\min\left\{1,\frac{\pi(\theta^*)q(\theta^*,\theta)}{\pi(\theta)q(\theta,\theta^*)}\right\}",
                      size=26, color=WHITE).shift(UP * 1.0)
        self.play(Write(lhs), run_time=1.6)
        cap(self, "For θ ≠ θ*, the transition density is just q times α.")

        arrow = Arrow(ORIGIN, DOWN * 0.7, color=GREY).next_to(lhs, DOWN, buff=0.1)
        self.play(Create(arrow), run_time=0.6)
        mid = formula(r"\min\{\pi(\theta)q(\theta,\theta^*),\ \pi(\theta^*)q(\theta^*,\theta)\}",
                      size=30, color=BLUE).shift(DOWN * 0.55)
        self.play(Write(mid), run_time=1.3)
        cap(self, "Multiplying out collapses both sides to the minimum of the two weighted proposal flows.")

        eq = formula(r"\min\{a,b\} = \min\{b,a\}\quad\checkmark", size=34, color=GREEN).shift(DOWN * 1.8)
        self.play(Write(eq), run_time=1.2)
        cap(self, "The minimum is symmetric, so the identity holds. For θ = θ* it is trivially true.")
        clean(self)


# ---------------------------------------------------------------------------
# 9. Gibbs is MH
# ---------------------------------------------------------------------------
class S09_GibbsIsMH(Scene):
    def construct(self):
        base(self)
        h = txt("Gibbs is a special case of MH", size=HEAD_SIZE, color=BLUE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Write(h), run_time=1.1)
        cap(self, "If we propose from the full conditional itself, the MH correction disappears.")

        prop = formula(r"\tilde q(\theta_i^* \mid \theta) = \pi(\theta_i^* \mid \theta_{-i})",
                       size=34, color=GREEN).shift(UP * 1.2)
        self.play(Write(prop), run_time=1.4)
        cap(self, "Pick the proposal to be exactly the full conditional distribution.")

        ratio = formula(
            r"\alpha = \min\left\{1, \frac{\pi(\theta_i^*|\theta_{-i})\,\pi(\theta_{-i})\,\pi(\theta_i|\theta^*_{-i})}{\pi(\theta_i|\theta_{-i})\,\pi(\theta_{-i})\,\pi(\theta_i^*|\theta_{-i})}\right\}",
            r"= \min\{1,1\} = 1",
            size=25, color=YELLOW, spacing=0.4).shift(DOWN * 0.5)
        self.play(Write(ratio), run_time=2.0)
        cap(self, "Every factor cancels: the acceptance probability is one, so Gibbs never rejects.")

        benefits = VGroup(
            txt("✓ no algebra for full conditionals", size=LABEL_SIZE, color=GREEN),
            txt("✓ block updates handle correlation", size=LABEL_SIZE, color=GREEN),
        ).arrange(DOWN, buff=0.3).to_edge(DOWN, buff=0.5)
        self.play(FadeIn(benefits), run_time=1.0)
        cap(self, "MH buys two things: you no longer need exact conditionals, and you can propose whole correlated blocks.")
        clean(self)


# ---------------------------------------------------------------------------
# 10. Proposal families
# ---------------------------------------------------------------------------
class S10_Proposals(Scene):
    def construct(self):
        base(self)
        h = txt("Three useful proposal designs", size=HEAD_SIZE, color=BLUE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Write(h), run_time=1.1)
        cap(self, "The proposal q is a design choice; different shapes give different samplers.")

        centers = [-3.6, 0, 3.6]
        c0 = Dot(centers[0] * RIGHT + DOWN * 0.3, color=YELLOW, radius=0.09)
        ring = Circle(radius=1.0, color=BLUE, stroke_opacity=0.6).move_to(c0.get_center())
        p0 = Dot(c0.get_center() + RIGHT * 0.7 + UP * 0.4, color=GREEN, radius=0.07)
        a0 = Arrow(c0.get_center(), p0.get_center(), color=GREY)

        gcurve = ax = axes_pair([-3, 3, 1], [0, 1.2, 0.4], width=2.6, height=1.8).move_to(RIGHT * centers[1] + DOWN * 0.3)
        dens = gcurve.plot(lambda x: math.exp(-x * x / 2) / math.sqrt(2 * math.pi), color=BLUE)
        p1 = Dot(gcurve.c2p(0.8, math.exp(-0.64 / 2) / math.sqrt(2 * math.pi)), color=GREEN, radius=0.07)

        c2 = Dot(RIGHT * centers[2] + DOWN * 0.3 + LEFT * 0.4, color=YELLOW, radius=0.09)
        p2 = Dot(c2.get_center() + UP * 0.9, color=GREEN, radius=0.07)
        a2 = Arrow(c2.get_center(), p2.get_center(), color=GREY)
        ghost = Dot(c2.get_center() + RIGHT * 0.5, color=GREY, radius=0.06, fill_opacity=0.3)

        self.play(FadeIn(c0), Create(ring), Create(a0), FadeIn(p0), run_time=1.2)
        self.play(Create(gcurve), Create(dens), FadeIn(p1), run_time=1.2)
        self.play(FadeIn(c2), FadeIn(ghost), Create(a2), FadeIn(p2), run_time=1.2)
        cap(self, "Random walk: symmetric jumps. Independence: fixed g. Single-site: only one coordinate moves.")

        names = VGroup(txt("RANDOM WALK", size=CAP_SIZE, color=BLUE).move_to(LEFT * 3.6 + DOWN * 1.6),
                       txt("INDEPENDENCE", size=CAP_SIZE, color=BLUE).move_to(DOWN * 1.6),
                       txt("SINGLE SITE", size=CAP_SIZE, color=BLUE).move_to(RIGHT * 3.6 + DOWN * 1.6))
        self.play(FadeIn(names), run_time=0.8)
        cap(self, "Random-walk symmetry cancels q in α; independence has α = π*/g / (π/g); single-site reduces to a conditional MH update.")

        sym = formula(r"\text{symmetric }q:\quad \alpha = \min\left\{1,\frac{\pi(\theta^*)}{\pi(\theta)}\right\}",
                      size=28, color=YELLOW).to_edge(DOWN, buff=0.4)
        self.play(Write(sym), run_time=1.4)
        cap(self, "The original Metropolis algorithm is exactly this symmetric case; Hastings generalised q in 1970.")
        clean(self)


# ---------------------------------------------------------------------------
# 11. Tuning
# ---------------------------------------------------------------------------
class S11_Tuning(Scene):
    def construct(self):
        base(self)
        h = txt("Tuning the proposal: finding the sweet spot", size=HEAD_SIZE, color=BLUE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Write(h), run_time=1.1)
        cap(self, "Proposal scale controls a trade-off: tiny steps are accepted often but explore slowly; huge steps explore but get rejected.")

        rng = random.Random(11)
        panels = []
        labels = [("σ LARGE  ·  4%", RED), ("σ RIGHT  ·  46%", GREEN), ("σ SMALL  ·  92%", YELLOW)]
        for idx, (lab, col) in enumerate(labels):
            ax = axes_pair([0, 90, 30], [-3, 12, 3], width=3.6, height=2.6).shift(RIGHT * (idx - 1) * 4.0)
            x = 8.0
            ys = [x]
            scale = [1.7, 0.45, 0.06][idx]
            for _ in range(90):
                p = x + rng.gauss(0, scale)
                if math.log(rng.random()) < -(p * p - x * x) / 2:
                    x = p
                ys.append(x)
            line = chain_line(ax, ys, color=col, width=1.4)
            panels.append(VGroup(ax, line, txt(lab, size=CAP_SIZE, color=col).next_to(ax, DOWN, buff=0.2)))
        self.play(LaggedStart(*[Create(p) for p in panels], lag_ratio=0.2), run_time=3.0)
        cap(self, "Large jumps stick near the start; well-scaled jumps mix; tiny jumps creep along in a nearly straight line.")

        rules = VGroup(
            txt("rule of thumb: 0.234 (multivariate)  ·  0.44 (univariate)", size=LABEL_SIZE, color=YELLOW),
            formula(r"\log\alpha = \log\pi(\theta^*)+\log q(\theta^*,\theta)-\log\pi(\theta)-\log q(\theta,\theta^*)", size=24, color=WHITE),
        ).arrange(DOWN, buff=0.35).to_edge(DOWN, buff=0.4)
        self.play(FadeIn(rules), run_time=1.3)
        cap(self, "Aim for roughly 23% acceptance in many dimensions or 44% in one dimension; compare in log space for stability.")
        clean(self)


# ---------------------------------------------------------------------------
# 12. DAG basics
# ---------------------------------------------------------------------------
class S12_DAGBasics(Scene):
    def construct(self):
        base(self)
        h = txt("A DAG encodes the joint distribution", size=HEAD_SIZE, color=BLUE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Write(h), run_time=1.1)
        cap(self, "Nodes are parameters or data; arrows say which variables a node's distribution depends on.")

        def small_dag(kind, x):
            a, b, c = [Dot(x * RIGHT + pos, radius=0.12, color=WHITE) for pos in [UP * 1.0, DOWN * 0.7 + LEFT * 0.9, DOWN * 0.7 + RIGHT * 0.9]]
            if kind == "fork":
                edges = [Arrow(a.get_center(), b.get_center(), color=GREY), Arrow(a.get_center(), c.get_center(), color=GREY)]
                f = formula(r"\pi(A)\pi(B|A)\pi(C|A)", size=24, color=BLUE)
            elif kind == "chain":
                edges = [Arrow(a.get_center(), b.get_center(), color=GREY), Arrow(b.get_center(), c.get_center(), color=GREY)]
                f = formula(r"\pi(A)\pi(B|A)\pi(C|B)", size=24, color=BLUE)
            else:
                edges = [Arrow(a.get_center(), c.get_center(), color=GREY), Arrow(b.get_center(), c.get_center(), color=GREY)]
                f = formula(r"\pi(A)\pi(B)\pi(C|A,B)", size=24, color=BLUE)
            lab = VGroup(txt("A", size=CAP_SIZE).next_to(a, UP, buff=0.1),
                         txt("B", size=CAP_SIZE).next_to(b, DOWN, buff=0.1),
                         txt("C", size=CAP_SIZE).next_to(c, DOWN, buff=0.1))
            return VGroup(*edges, a, b, c, lab, f.next_to(VGroup(a, b, c), DOWN, buff=0.45))

        dags = VGroup(small_dag("fork", -3.6), small_dag("chain", 0), small_dag("collider", 3.6))
        self.play(LaggedStart(*[FadeIn(d, shift=UP * 0.3) for d in dags], lag_ratio=0.25), run_time=2.6)
        cap(self, "Factorise the joint by multiplying each node's density conditional on its parents — fork, chain and collider.")

        rule = formula(r"\pi(V) = \prod_{v\in V} \pi\bigl(v \mid \mathrm{parents}(v)\bigr)",
                       size=32, color=YELLOW).to_edge(DOWN, buff=0.5)
        self.play(Write(rule), run_time=1.4)
        cap(self, "This product is the whole model: JAGS, BUGS and Stan all read models this way.")
        clean(self)


# ---------------------------------------------------------------------------
# 13. Conditional independence
# ---------------------------------------------------------------------------
class S13_CI(Scene):
    def construct(self):
        base(self)
        h = txt("Independence vs conditional independence", size=HEAD_SIZE, color=BLUE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Write(h), run_time=1.1)
        cap(self, "Two variables can be dependent overall yet independent once a third variable is known.")

        z = Dot(UP * 1.3, radius=0.14, color=YELLOW)
        x = Dot(DOWN * 0.7 + LEFT * 1.2, radius=0.14, color=BLUE)
        y = Dot(DOWN * 0.7 + RIGHT * 1.2, radius=0.14, color=GREEN)
        e1 = Arrow(z.get_center(), x.get_center(), color=GREY)
        e2 = Arrow(z.get_center(), y.get_center(), color=GREY)
        labs = VGroup(txt("Z (parents)", size=CAP_SIZE, color=YELLOW).next_to(z, UP, buff=0.15),
                      txt("X", size=LABEL_SIZE, color=BLUE).next_to(x, DOWN, buff=0.15),
                      txt("Y", size=LABEL_SIZE, color=GREEN).next_to(y, DOWN, buff=0.15))
        dep = Line(x.get_center(), y.get_center(), color=RED, stroke_width=3, stroke_opacity=0.8)
        self.play(Create(e1), Create(e2), FadeIn(z), FadeIn(x), FadeIn(y), FadeIn(labs), run_time=1.5)
        cap(self, "Children inherit dependence through their shared parents — think genotypes of children and parents.")
        self.play(Create(dep), run_time=0.8)
        cap(self, "Without information about the parents, the children's genotypes are marginally dependent.")

        self.play(FadeOut(dep), z.animate.set_opacity(0.25), e1.animate.set_opacity(0.25), e2.animate.set_opacity(0.25), run_time=1.0)
        eq = formula(r"\pi(X,Y\mid Z) = \pi(X\mid Z)\,\pi(Y\mid Z)", size=30, color=GREEN).to_edge(DOWN, buff=0.6)
        self.play(Write(eq), run_time=1.3)
        cap(self, "Condition on Z and the link vanishes: the children are conditionally independent given the parents.")
        clean(self)


# ---------------------------------------------------------------------------
# 14. Moralisation / global Markov
# ---------------------------------------------------------------------------
class S14_Moralise(Scene):
    def construct(self):
        base(self)
        h = txt("From DAG to conditional-independence graph", size=HEAD_SIZE, color=BLUE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Write(h), run_time=1.1)
        cap(self, "Two operations turn a DAG into an undirected graph that displays all conditional independencies.")

        pos = {
            "a": LEFT * 4.5 + UP * 1.3, "b": LEFT * 3.0 + UP * 0.2, "c": LEFT * 3.0 + DOWN * 1.2,
            "d": LEFT * 1.2 + DOWN * 0.5, "e": LEFT * 4.5 + DOWN * 1.8, "f": LEFT * 1.2 + UP * 1.6,
        }
        nodes = {k: Dot(v, radius=0.11, color=WHITE) for k, v in pos.items()}
        edges = [("a", "b"), ("a", "c"), ("b", "d"), ("c", "d"), ("e", "c"), ("f", "d")]
        arrows = VGroup(*[Arrow(pos[u], pos[v], color=GREY, buff=0.12) for u, v in edges])
        labels = VGroup(*[txt(k.upper(), size=CAP_SIZE).next_to(nodes[k], UP, buff=0.08, aligned_edge=LEFT) for k in pos])
        dag = VGroup(arrows, *nodes.values(), labels)
        self.play(FadeIn(dag), run_time=1.5)
        cap(self, "Start with the DAG: note that D has parents B and C, which are not joined.")

        marry = ArcBetweenPoints(pos["b"], pos["c"], angle=-0.5, color=YELLOW, stroke_width=3)
        self.play(Create(marry), run_time=1.0)
        cap(self, "Step 1: 'marry' the parents — connect any two nodes that share a child.")

        und = VGroup(*[Line(pos[u], pos[v], color=GREEN, stroke_width=2) for u, v in edges], marry)
        und.set_color(GREEN)
        self.play(Transform(arrows, und), run_time=1.2)
        cap(self, "Step 2: drop the arrowheads. The result is the conditional-independence graph.")

        stmt = formula(r"D \perp\!\!\!\perp (A,E,F)\mid (B,C)", size=32, color=YELLOW).shift(RIGHT * 3.0)
        note = txt("Only B and C matter when updating D.", size=CAP_SIZE, color=GREEN).next_to(stmt, DOWN, buff=0.3)
        self.play(FadeIn(stmt), FadeIn(note), run_time=1.3)
        cap(self, "Global Markov property: once B and C are known, D is separated from A, E and F — a local Gibbs update.")
        clean(self)


# ---------------------------------------------------------------------------
# 15. Dugongs
# ---------------------------------------------------------------------------
class S15_Dugongs(Scene):
    def construct(self):
        base(self)
        h = txt("Dugong growth: building the DAG", size=HEAD_SIZE, color=BLUE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Write(h), run_time=1.1)
        cap(self, "27 ages and lengths; model length as a nonlinear growth curve with normal noise.")

        model = formula(r"Y_i \sim N(\mu_i,\sigma^2),\qquad \mu_i = \alpha - \beta\gamma^{X_i}",
                        size=30, color=WHITE).shift(UP * 1.5)
        self.play(Write(model), run_time=1.4)
        cap(self, "The mean μᵢ is deterministic given α, β, γ and the observed age Xᵢ.")

        pos = {"α": (-3.4, 0.6), "β": (-2.4, 1.7), "γ": (-1.3, 0.6), "τ": (-3.4, -1.3),
               "μ": (0.3, 0.2), "X": (1.9, 1.5), "Y": (2.4, -0.8), "σ": (-1.4, -2.0)}
        dots = {k: Dot(np.array([v[0], v[1], 0]), radius=0.11,
                       color=PINK if k in ["α", "β", "γ", "τ"] else (BLUE if k in ["X", "μ", "Y"] else GREY))
                for k, v in pos.items()}
        labs = VGroup(*[txt(k, size=CAP_SIZE).next_to(dt, UP, buff=0.08) for k, dt in dots.items()])
        edges = [("α", "μ"), ("β", "μ"), ("γ", "μ"), ("X", "μ"), ("μ", "Y"), ("τ", "Y"), ("τ", "σ")]
        arrows = VGroup(*[Arrow(dots[u].get_center(), dots[v].get_center(), color=GREY, buff=0.12) for u, v in edges])
        dag = VGroup(arrows, *dots.values(), labs)
        self.play(FadeIn(dag), run_time=2.0)
        cap(self, "Pink: priors on α, β, γ, τ. Blue: data and deterministic mean. Arrows carry the dependencies into the likelihood.")

        post = formula(
            r"\pi(\theta\mid x,y) \propto \pi(\alpha)\pi(\beta)\pi(\gamma)\pi(\tau)\prod_{i=1}^{27}\pi(Y_i\mid X_i,\alpha,\beta,\gamma,\tau)",
            size=23, color=YELLOW).to_edge(DOWN, buff=0.4)
        self.play(Write(post), run_time=1.6)
        cap(self, "The DAG factorisation is literally the posterior: priors times a product of 27 likelihood terms.")
        clean(self)


# ---------------------------------------------------------------------------
# 16. rJAGS
# ---------------------------------------------------------------------------
class S16_JAGS(Scene):
    def construct(self):
        base(self)
        h = txt("Posterior simulation with rJAGS", size=HEAD_SIZE, color=BLUE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Write(h), run_time=1.1)
        cap(self, "JAGS builds and runs the MCMC sampler for you — you supply data, a model and starting values.")

        inputs = VGroup(card("DATA", "list(N, x, Y)", color=BLUE),
                        card("MODEL", "dugongs.bug", color=GREEN),
                        card("INITS", "alpha, beta, tau", color=YELLOW)).arrange(RIGHT, buff=0.35).scale(0.85).shift(UP * 1.5)
        self.play(LaggedStart(*[FadeIn(c) for c in inputs], lag_ratio=0.2), run_time=1.8)
        cap(self, "Three inputs: the observed data, the BUGS model file, and initial values for the stochastic nodes.")

        flow = VGroup(txt("jags.model(n.chains=3)", size=LABEL_SIZE, color=WHITE).shift(DOWN * 0.2),
                      txt("→ update(2000) → coda.samples(1000)", size=LABEL_SIZE, color=GREEN).shift(DOWN * 0.9))
        self.play(FadeIn(flow), run_time=1.2)
        cap(self, "Compile the DAG, burn in 2000 iterations, then keep 1000 samples per chain.")

        code = VGroup(
            txt("for (i in 1:N) {", size=CAP_SIZE, color=WHITE),
            txt("  mu[i] = alpha - beta * pow(gamma, x[i])", size=CAP_SIZE, color=BLUE),
            txt("  Y[i] ~ dnorm(mu[i], tau)   # precision!", size=CAP_SIZE, color=GREEN),
            txt("}", size=CAP_SIZE, color=WHITE),
            txt("tau ~ dgamma(0.001, 0.001)", size=CAP_SIZE, color=PINK),
        ).arrange(DOWN, buff=0.12, aligned_edge=LEFT).move_to(DOWN * 2.3).scale(0.85)
        self.play(FadeIn(code), run_time=1.2)
        cap(self, "JAGS uses precision, not variance, in dnorm — and pow(gamma,x[i]) implements the growth curve.")

        diag = VGroup(*[txt(s, size=CAP_SIZE, color=col) for s, col in
                        [("traceplot", BLUE), ("densplot", GREEN), ("acfplot", YELLOW), ("gelman.diag", PINK)]]).arrange(RIGHT, buff=0.5).to_edge(DOWN, buff=0.3)
        self.play(FadeIn(diag), run_time=1.0)
        cap(self, "Then diagnose: trace plots, densities, autocorrelation and Gelman–Rubin shrink factors across chains.")
        clean(self)


# ---------------------------------------------------------------------------
# 17. Tutorial 1
# ---------------------------------------------------------------------------
class S17_Tut1(Scene):
    def construct(self):
        base(self)
        h = txt("Tutorial 1 — Gibbs for a bivariate normal", size=HEAD_SIZE, color=BLUE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Write(h), run_time=1.1)
        cap(self, "We can analyse this Gibbs sampler exactly — a perfect laboratory for understanding convergence.")

        parts = VGroup(
            formula(r"\theta_1\mid\theta_2 \sim N(\rho\theta_2,\,1-\rho^2)", size=28, color=BLUE),
            formula(r"\theta_2\mid\theta_1 \sim N(\rho\theta_1,\,1-\rho^2)", size=28, color=GREEN),
        ).arrange(DOWN, buff=0.3).shift(UP * 1.3)
        self.play(Write(parts), run_time=1.6)
        cap(self, "The two full conditionals are normal with variance 1−ρ².")

        rec = formula(
            r"\theta_2^{(t)} = \rho^{2t}\theta_2^{(0)} + \sum_{i=0}^{2t-1}\rho^{i}\epsilon_i",
            r"\mathbb{E}\theta_2^{(t)}=\rho^{2t}\theta_2^{(0)},\qquad \mathrm{Var}=\frac{1-\rho^{4t}}{1-\rho^2}(1-\rho^2)=1-\rho^{4t}",
            size=26, color=YELLOW, spacing=0.35).shift(DOWN * 0.6)
        self.play(Write(rec), run_time=2.0)
        cap(self, "Each sweep multiplies the old state by ρ² and adds fresh noise; mean forgets the start as ρ^{2t}→0, variance relaxes to 1.")

        ax = axes_pair([0, 20, 5], [0, 1.05, 0.2], width=5.4, height=2.2).shift(DOWN * 2.2)
        for rho, col in [(0.3, GREEN), (0.8, BLUE), (0.98, RED)]:
            curve = ax.plot(lambda t, r=rho: r ** (2 * t), x_range=[0, 20], color=col)
            self.add(curve)
            lab = txt(f"ρ={rho}", size=CAP_SIZE, color=col).move_to(ax.c2p(16, rho ** 32) + UP * 0.25)
            self.add(lab)
        self.play(FadeIn(ax), run_time=0.8)
        cap(self, "As ρ approaches ±1 the decay ρ^{2t} becomes painfully slow: highly correlated coordinates mix badly.")
        clean(self)


# ---------------------------------------------------------------------------
# 18. Tutorial 2
# ---------------------------------------------------------------------------
class S18_Tut2(Scene):
    def construct(self):
        base(self)
        h = txt("Tutorial 2 — a mixture Beta prior", size=HEAD_SIZE, color=BLUE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Write(h), run_time=1.1)
        cap(self, "The prior is neither a single Beta nor flat — it is a 50–50 mixture of two Beta distributions.")

        dec = formula(
            r"\pi(\theta)=\tfrac12\left[\frac{\Gamma(6)}{\Gamma(2)\Gamma(4)}\theta^{2-1}(1-\theta)^{4-1}+\frac{\Gamma(2)}{\Gamma(1)\Gamma(1)}\theta^{1-1}(1-\theta)^{1-1}\right]",
            size=25, color=WHITE).shift(UP * 1.2)
        self.play(Write(dec), run_time=1.8)
        cap(self, "The normalising constant is k₀ = 1/2, giving ½ Beta(2,4) + ½ Beta(1,1).")

        ax = axes_pair([0, 1, 0.25], [0, 3, 1], width=5.2, height=2.6).shift(LEFT * 2.6 + DOWN * 0.9)
        f1 = ax.plot(lambda t: 0.5 * 20 * t * (1 - t) ** 3, x_range=[0.01, 0.99], color=BLUE)
        f2 = ax.plot(lambda t: 0.5, x_range=[0.01, 0.99], color=GREEN)
        fm = ax.plot(lambda t: 0.5 * (20 * t * (1 - t) ** 3 + 1), x_range=[0.01, 0.99], color=YELLOW)
        self.play(Create(ax), Create(f1), Create(f2), Create(fm), run_time=2.0)
        cap(self, "Blue: Beta(2,4) component; green: uniform component; yellow: the mixture that is our prior.")

        stats = VGroup(
            txt("prior mean = 5/12 ≈ 0.4167", size=LABEL_SIZE, color=YELLOW),
            txt("prior sd ≈ 0.2539", size=LABEL_SIZE, color=YELLOW),
        ).arrange(DOWN, buff=0.25).shift(RIGHT * 3.4 + UP * 0.3)
        self.play(FadeIn(stats), run_time=1.0)
        cap(self, "Mixture moments mix component moments: mean 0.4167, standard deviation about 0.254.")

        post = VGroup(
            txt("n=10, x=4  →  weights 20/33 : 13/33", size=CAP_SIZE, color=GREEN),
            txt("posterior = (20/33)Beta(6,10) + (13/33)Beta(5,7)", size=CAP_SIZE, color=GREEN),
            txt("posterior mean ≈ 0.3914", size=CAP_SIZE, color=YELLOW),
        ).arrange(DOWN, buff=0.2).shift(RIGHT * 3.4 + DOWN * 1.3)
        self.play(FadeIn(post), run_time=1.4)
        cap(self, "The binomial likelihood updates each component separately; the posterior is a new mixture with mean 0.3914.")
        clean(self)


# ---------------------------------------------------------------------------
# 19. Tutorial 3
# ---------------------------------------------------------------------------
class S19_Tut3(Scene):
    def construct(self):
        base(self)
        h = txt("Tutorial 3 — Poisson sales, Gamma prior", size=HEAD_SIZE, color=BLUE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Write(h), run_time=1.1)
        cap(self, "Twenty weekly sales counts, independent Poisson(λ); a Gamma prior with mean 16 and sd 8.")

        solve = formula(
            r"\frac{a}{b}=16,\quad \frac{a}{b^2}=64 \;\Rightarrow\; b=\frac{16}{64}=0.25,\ a=4",
            size=28, color=YELLOW).shift(UP * 1.4)
        self.play(Write(solve), run_time=1.6)
        cap(self, "For a Gamma(shape=a, rate=b), mean = a/b and variance = a/b², so a=4 and b=0.25.")

        ax = axes_pair([14, 24, 2], [0, 1.05, 0.2], width=7.2, height=2.8).shift(DOWN * 0.5)
        def gp_shape(x, a, b):
            # log-density shifted to its mode: stable even for shape=404
            mode = (a - 1) / b
            log_mode = (a - 1) * math.log(mode) - b * mode
            return math.exp((a - 1) * math.log(x) - b * x - log_mode)
        prior = ax.plot(lambda x: gp_shape(x, 4, 0.25), x_range=[14.1, 24], color=BLUE)
        post = ax.plot(lambda x: gp_shape(x, 404, 20.25), x_range=[17.5, 23.5], color=GREEN)
        self.play(Create(ax), Create(prior), Create(post), run_time=2.0)
        cap(self, "Blue: diffuse prior centred at 16. Green: sharp posterior centred near 20 after 400 total sales.")

        info = VGroup(
            txt("Σy = 400  →  λ|y ~ Gamma(404, 20.25)", size=LABEL_SIZE, color=GREEN),
            txt("posterior mean = 404/20.25 ≈ 19.95", size=CAP_SIZE, color=WHITE),
            txt("95% HPD ≈ [18.03, 21.90]", size=LABEL_SIZE, color=YELLOW),
        ).arrange(DOWN, buff=0.25).to_edge(DOWN, buff=0.35)
        self.play(FadeIn(info), run_time=1.4)
        cap(self, "Conjugacy updates shape to a+Σy and rate to b+n; the highest-density interval is [18.03, 21.90].")
        clean(self)


# ---------------------------------------------------------------------------
# 20. Tutorial 4
# ---------------------------------------------------------------------------
class S20_Tut4(Scene):
    def construct(self):
        base(self)
        h = txt("Tutorial 4 — 500 g rice packets", size=HEAD_SIZE, color=BLUE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Write(h), run_time=1.1)
        cap(self, "Known precision τ likelihood, Gamma prior on τ, and a conditional normal prior on μ centred at 500.")

        hier = VGroup(
            formula(r"y_i\mid\mu,\tau \sim N(\mu,\tau^{-1})", size=26, color=WHITE),
            formula(r"\tau\sim\mathrm{Gamma}(2,9),\qquad \mu\mid\tau\sim N(500,(0.005\tau)^{-1})", size=26, color=BLUE),
        ).arrange(DOWN, buff=0.3).shift(UP * 1.1)
        self.play(Write(hier), run_time=1.8)
        cap(self, "The prior on μ has precision 0.005τ — very weak compared with 20 observations at precision τ.")

        post = VGroup(
            txt("ȳ = 492.85,   Σ(y−ȳ)² = 444.55", size=LABEL_SIZE, color=GREEN),
            formula(r"\mu\mid\tau,y \sim N\!\left(492.852,\ [22.005\tau]^{-1}\right)", size=26, color=WHITE),
            formula(r"\tau\mid y \sim \mathrm{Gamma}(12,\ 231.40)", size=26, color=WHITE),
        ).arrange(DOWN, buff=0.3).shift(DOWN * 0.55)
        self.play(FadeIn(post), run_time=1.8)
        cap(self, "Conjugacy gives a normal conditional for μ and a Gamma conditional for τ; marginalising τ yields a Student-t.")

        ax = axes_pair([488, 498, 2], [0, 0.45, 0.1], width=6.4, height=2.0).shift(DOWN * 2.3)
        df, mu0, scale = 24, 492.8518, 0.9818
        def tpdf(z):
            return math.exp(math.lgamma((df + 1) / 2) - math.lgamma(df / 2)) / math.sqrt(df * math.pi) * (1 + (z - mu0) ** 2 / (scale ** 2 * df)) ** (-(df + 1) / 2)
        curve = ax.plot(tpdf, x_range=[488.2, 497.8], color=YELLOW)
        shade = ax.get_area(curve, x_range=[488.2, 495], color=GREEN, opacity=0.45)
        self.play(Create(ax), Create(curve), FadeIn(shade), run_time=1.6)
        cap(self, "The posterior for μ is a t distribution with 24 degrees of freedom, centred at 492.85. The green region is μ below 495.")
        ans = txt("P(μ < 495) ≈ 0.981", size=HEAD_SIZE, color=YELLOW).shift(RIGHT * 3.9 + DOWN * 1.8)
        self.play(FadeIn(ans), run_time=1.0)
        cap(self, "Shading everything below 495 gives about 98.1% posterior probability.")
        clean(self)


# ---------------------------------------------------------------------------
# 21. Tutorial 5 — regression conditionals
# ---------------------------------------------------------------------------
class S21_Tut5(Scene):
    def construct(self):
        base(self)
        h = txt("Tutorial 5 — Gibbs for linear regression", size=HEAD_SIZE, color=BLUE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Write(h), run_time=1.1)
        cap(self, "The lab builds a Gibbs sampler from these three full conditionals. Here is where they come from.")

        block = VGroup(
            txt("BLOCK UPDATE", size=CAP_SIZE, color=BLUE),
            formula(r"\beta\mid y,\phi \sim N_2\!\left(\hat\beta,\ \phi^{-1}(X^\top X)^{-1}\right)", size=25, color=WHITE),
            formula(r"\hat\beta=(X^\top X)^{-1}X^\top Y", size=24, color=GREY),
        ).arrange(DOWN, buff=0.25).shift(UP * 1.6)
        self.play(FadeIn(block), run_time=1.6)
        cap(self, "Complete the square in β: the quadratic form is (Y−Xβ)ᵀ(Y−Xβ), giving β̂ and covariance φ⁻¹(XᵀX)⁻¹.")

        phi = VGroup(
            txt("PRECISION UPDATE", size=CAP_SIZE, color=GREEN),
            formula(r"\phi\mid y,\beta \sim \mathrm{Gamma}\!\left(\frac{n_1}{2},\ \frac{S_\beta}{2}\right)", size=25, color=WHITE),
            formula(r"n_1=n+n_0,\quad S_\beta=(\beta-\hat\beta)^\top X^\top X(\beta-\hat\beta)+S_e+n_0S_0", size=22, color=GREY),
        ).arrange(DOWN, buff=0.25).shift(UP * 0.1)
        self.play(FadeIn(phi), run_time=1.6)
        cap(self, "Holding β fixed, the φ terms are powers of φ times one exponential — Gamma with updated shape and scale.")

        singles = VGroup(
            txt("SINGLE-COORDINATE UPDATES", size=CAP_SIZE, color=YELLOW),
            formula(r"\beta_0\mid\beta_1,y,\phi \sim N\!\left(\hat\beta_0-\bar x(\beta_1-\hat\beta_1),\ \frac{1}{n\phi}\right)", size=23, color=WHITE),
            formula(r"\beta_1\mid\beta_0,y,\phi \sim N\!\left(\hat\beta_1-\frac{\bar x}{\sum x_i^2}(\beta_0-\hat\beta_0),\ \frac{1}{\phi\sum x_i^2}\right)", size=23, color=WHITE),
        ).arrange(DOWN, buff=0.25).shift(DOWN * 1.9)
        self.play(FadeIn(singles), run_time=1.8)
        cap(self, "Splitting the 2-dimensional block into β₀ and β₁ conditionals gives the scalar updates used in the lab.")
        clean(self)
