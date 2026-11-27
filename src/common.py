"""Shared, clip-safe Manim visual language for Weeks 8-10 animated lessons.

Every lesson is described as a list of steps (card, equation, diagram, note).
The ``LessonScene`` class lays them out, fits them inside the frame, reveals
them one at a time with subtitles, and exits cleanly.  This keeps every scene
consistent and guarantees no text is cut off at the screen edge.
"""

from manim import *
import math
import random

from speech import spoken_duration

# ---------------------------------------------------------------------------
# Palette / typography
# ---------------------------------------------------------------------------
BG = "#1C1C1C"
BLUE = "#58C4DD"
GREEN = "#83C167"
YELLOW = "#FFFF00"
GREY = "#888888"
RED = "#FF6B6B"
PINK = "#FF9EC4"
MONO = "Menlo"

TITLE_SIZE = 42
HEAD_SIZE = 28
BODY_SIZE = 26
LABEL_SIZE = 21
CAP_SIZE = 18

SAFE_W = 12.2
SAFE_H = 6.7


# ---------------------------------------------------------------------------
# Safety helpers
# ---------------------------------------------------------------------------
def fit(obj, max_w=SAFE_W, max_h=SAFE_H):
    """Scale a mobject into the safe frame so nothing is clipped."""
    if obj.width > 0 and obj.height > 0:
        k = min(1.0, max_w / obj.width, max_h / obj.height)
        if k < 1.0:
            obj.scale(k)
    return obj


def base(scene):
    scene.camera.background_color = BG


def cap(scene, text, duration=4.0):
    """Attach a subtitle and hold the scene long enough for natural narration."""
    duration = max(duration, spoken_duration(text, base=4.0))
    if hasattr(scene, "add_subcaption"):
        scene.add_subcaption(text, duration=duration)
    scene.wait(duration)


def clean(scene):
    # Tail hold lets the final subtitle run its full spoken duration.
    scene.wait(2.0)
    if scene.mobjects:
        scene.play(FadeOut(Group(*scene.mobjects)), run_time=0.45)
    scene.wait(0.25)


def txt(s, size=BODY_SIZE, color=WHITE, weight=None, max_w=SAFE_W, max_h=1.6):
    kwargs = dict(font=MONO, font_size=size, color=color)
    if weight is not None:
        kwargs["weight"] = weight
    return fit(Text(s, **kwargs), max_w=max_w, max_h=max_h)


def tex(s, size=BODY_SIZE, color=WHITE, max_w=SAFE_W, max_h=2.2):
    return fit(MathTex(s, font_size=size, color=color), max_w=max_w, max_h=max_h)


def multiple_tex(*parts, size=BODY_SIZE, color=WHITE, spacing=0.18, max_w=SAFE_W, max_h=2.2):
    group = VGroup(*[MathTex(p, font_size=size, color=color) for p in parts])
    group.arrange(DOWN, buff=spacing)
    return fit(group, max_w=max_w, max_h=max_h)


def card(head, body, width=5.6, height=1.0, color=BLUE):
    box = RoundedRectangle(corner_radius=0.1, width=width, height=height,
                           color=color, stroke_width=2,
                           fill_color=color, fill_opacity=0.09)
    t = fit(txt(head, size=LABEL_SIZE, color=color, weight=BOLD),
            max_w=width - 0.3, max_h=0.42)
    b = fit(txt(body, size=CAP_SIZE, color=WHITE),
            max_w=width - 0.3, max_h=0.42)
    t.move_to(box.get_center() + UP * 0.22)
    b.move_to(box.get_center() + DOWN * 0.22)
    return VGroup(box, t, b)


# ---------------------------------------------------------------------------
# Reusable diagrams
# ---------------------------------------------------------------------------
def axes_diagram(x_range, y_range, curves, width=7.4, height=2.8, xlab="", ylab=""):
    """curves: list of (lambda, color) pairs."""
    ax = Axes(x_range=x_range, y_range=y_range, x_length=width, y_length=height, tips=False)
    parts = [ax]
    for func, color in curves:
        parts.append(ax.plot(func, x_range=(x_range[0] + 0.01, x_range[1] - 0.01),
                             color=color, stroke_width=3))
    if xlab:
        parts.append(txt(xlab, size=CAP_SIZE, color=GREY).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08))
    if ylab:
        parts.append(txt(ylab, size=CAP_SIZE, color=GREY).next_to(ax.y_axis.get_end(), UP, buff=0.08))
    return fit(VGroup(*parts), max_w=SAFE_W, max_h=3.2)


def dag_diagram(nodes, edges, width=8.6, height=2.8):
    """nodes: {label: (x,y,color)}; edges: list of (from_label, to_label)."""
    positions = {k: np.array([v[0], v[1], 0]) for k, v in nodes.items()}
    dots = {k: Dot(positions[k], radius=0.11, color=v[2]) for k, v in nodes.items()}
    labels = VGroup(*[txt(k, size=CAP_SIZE, color=v[2]).next_to(dots[k], UP, buff=0.08)
                      for k, v in nodes.items()])
    arrows = VGroup(*[Arrow(positions[u], positions[v], color=GREY, buff=0.14, stroke_width=2)
                      for u, v in edges])
    return fit(VGroup(arrows, *dots.values(), labels), max_w=width, max_h=height)


def bars_diagram(values, labels, colors=None, width=8.4, height=2.6):
    colors = colors or [BLUE] * len(values)
    lo = min(0, min(values))
    hi = max(0, max(values))
    span = max(hi - lo, 1.0)
    ymin = lo - 0.15 * span
    ymax = hi + 0.15 * span
    ax = Axes(x_range=[0, len(values) + 1, 1], y_range=[ymin, ymax, span / 3],
              x_length=width, y_length=height, tips=False)
    bars = VGroup()
    for i, (v, c) in enumerate(zip(values, colors)):
        top = ax.c2p(i + 1, max(v, 0))[1]
        bottom = ax.c2p(i + 1, min(v, 0))[1]
        bar = Rectangle(width=0.55, height=max(abs(top - bottom), 0.02),
                        color=c, fill_color=c, fill_opacity=0.55)
        bar.move_to([ax.c2p(i + 1, 0)[0], (top + bottom) / 2, 0])
        lab = txt(str(labels[i]), size=CAP_SIZE, color=GREY)
        lab.next_to(bar, DOWN if v >= 0 else UP, buff=0.12)
        bars.add(bar, lab)
    return fit(VGroup(ax, bars), max_w=SAFE_W, max_h=3.0)


def flow_diagram(labels, colors=None, width=11.4, height=1.1):
    colors = colors or [BLUE] * len(labels)
    boxes = []
    for lab, c in zip(labels, colors):
        b = card(lab, "", width=width / len(labels) - 0.5, height=height, color=c)
        # remove empty body child for a compact box
        boxes.append(VGroup(b[0], b[1]))
    group = VGroup()
    for i, b in enumerate(boxes):
        if i:
            group.add(Arrow(group[-1].get_right(), b.get_left(), color=GREY, buff=0.1, stroke_width=2))
        group.add(b)
    group.arrange(RIGHT, buff=0.3)
    return fit(group, max_w=width, max_h=height + 0.4)


def mixture_diagram(width=7.6, height=2.8):
    def norm(x, m, s):
        return math.exp(-0.5 * ((x - m) / s) ** 2) / (s * math.sqrt(2 * math.pi))
    curves = [
        (lambda x: norm(x, 160, 8), BLUE),
        (lambda x: norm(x, 180, 9), GREEN),
        (lambda x: 0.5 * norm(x, 160, 8) + 0.5 * norm(x, 180, 9), YELLOW),
    ]
    return axes_diagram([135, 205, 10], [0, 0.055, 0.01], curves, width, height, "height (cm)", "density")


def changepoint_diagram(width=8.0, height=2.6):
    ax = Axes(x_range=[1851, 1962, 2], y_range=[0, 7, 1],
              x_length=width, y_length=height, tips=False)
    early = ax.plot(lambda x: 3.0 + 0.0 * x, x_range=[1851, 1895], color=BLUE, use_smoothing=False)
    late = ax.plot(lambda x: 0.8 + 0.0 * x, x_range=[1895, 1962], color=GREEN, use_smoothing=False)
    line = DashedLine(ax.c2p(1895, 0), ax.c2p(1895, 6.5), color=YELLOW)
    tau = txt("tau", size=CAP_SIZE, color=YELLOW).next_to(line.get_top(), UP, buff=0.1)
    return fit(VGroup(ax, early, late, line, tau), max_w=SAFE_W, max_h=3.2)


def normal_pairs_diagram(width=7.6, height=2.8):
    def norm(x, m, s):
        return math.exp(-0.5 * ((x - m) / s) ** 2) / (s * math.sqrt(2 * math.pi))
    return axes_diagram([-4, 4, 1], [0, 0.45, 0.1],
                        [(lambda x: norm(x, 0, 1), BLUE),
                         (lambda x: norm(x, 1.5, 1), GREEN)], width, height)


def hierarchy_diagram(width=9.0, height=3.0):
    nodes = {
        "lambda": (-3.4, 1.2, PINK), "a": (-1.6, 1.2, PINK),
        "theta_1": (-2.6, -0.2, BLUE), "theta_2": (0.0, -0.2, BLUE),
        "theta_3": (2.6, -0.2, BLUE),
        "y_1": (-2.6, -1.6, GREEN), "y_2": (0.0, -1.6, GREEN),
        "y_3": (2.6, -1.6, GREEN),
    }
    edges = [("lambda", "theta_1"), ("lambda", "theta_2"), ("lambda", "theta_3"),
             ("a", "theta_1"), ("a", "theta_2"), ("a", "theta_3"),
             ("theta_1", "y_1"), ("theta_2", "y_2"), ("theta_3", "y_3")]
    return dag_diagram(nodes, edges, width, height)


# ---------------------------------------------------------------------------
# Generic lesson scene
# ---------------------------------------------------------------------------
DIAGRAMS = {
    "mixture": mixture_diagram,
    "changepoint": changepoint_diagram,
    "normal_pairs": normal_pairs_diagram,
    "hierarchy": hierarchy_diagram,
}


def _build_step(step):
    kind = step["kind"]
    if kind == "card":
        return card(step["head"], step.get("body", ""),
                    color=step.get("color", BLUE))
    if kind == "eq":
        return tex(step["tex"], size=step.get("size", BODY_SIZE),
                   color=step.get("color", WHITE))
    if kind == "eqs":
        return multiple_tex(*step["parts"], size=step.get("size", BODY_SIZE),
                            color=step.get("color", WHITE))
    if kind == "note":
        return txt(step["text"], size=step.get("size", HEAD_SIZE),
                   color=step.get("color", YELLOW))
    if kind == "flow":
        return flow_diagram(step["labels"], step.get("colors"))
    if kind == "bars":
        return bars_diagram(step["values"], step["labels"], step.get("colors"))
    if kind == "dag":
        return dag_diagram(step["nodes"], step["edges"])
    if kind == "axes":
        return axes_diagram(step["x_range"], step["y_range"], step["curves"],
                            xlab=step.get("xlab", ""), ylab=step.get("ylab", ""))
    if kind == "diagram":
        name = step["diagram"]
        if name == "axes":
            return axes_diagram(step["x_range"], step["y_range"], step["curves"],
                                xlab=step.get("xlab", ""), ylab=step.get("ylab", ""))
        if name == "dag":
            return dag_diagram(step["nodes"], step["edges"])
        if name == "bars":
            return bars_diagram(step["values"], step["labels"], step.get("colors"))
        if name == "flow":
            return flow_diagram(step["labels"], step.get("colors"))
        return DIAGRAMS[name]()
    raise ValueError(f"Unknown step kind: {kind}")


class LessonScene(Scene):
    """A scene that reveals a list of steps with subtitles and a clean exit."""

    spec = {}

    def construct(self):
        base(self)
        title = fit(txt(self.spec.get("title", ""), size=TITLE_SIZE,
                        color=BLUE, weight=BOLD), max_h=0.9)
        title.to_edge(UP, buff=0.28)
        self.play(Write(title), run_time=0.9)
        cap(self, self.spec.get("intro", self.spec.get("title", "")), duration=4.0)
        self.wait(0.4)

        items = []
        for step in self.spec.get("steps", []):
            obj = _build_step(step)
            items.append((obj, step.get("cap", "")))

        stack = VGroup(*[o for o, _ in items])
        if len(stack) > 1:
            stack.arrange(DOWN, buff=0.2)
        fit(stack, max_w=SAFE_W, max_h=5.75).move_to(DOWN * 0.12)

        for obj, subtitle in items:
            self.play(FadeIn(obj, shift=UP * 0.16), run_time=0.85)
            if subtitle:
                cap(self, subtitle, duration=4.0)
            self.wait(0.4)

        self.wait(0.7)
        clean(self)


def make_lesson_module(specs, prefix, globals_dict):
    """Create one Scene subclass per spec and register it in a module namespace."""
    classes = []
    for i, spec in enumerate(specs, 1):
        name = f"{prefix}_S{i:02d}_{spec['slug']}"
        cls = type(name, (LessonScene,), {"spec": spec, "__module__": globals_dict["__name__"]})
        globals_dict[name] = cls
        classes.append(cls)
    globals_dict["SCENE_CLASSES"] = classes
    globals_dict["SCENE_NAMES"] = [c.__name__ for c in classes]
    return classes
