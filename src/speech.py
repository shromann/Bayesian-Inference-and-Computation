"""Shared text-to-speech timing helpers.

Subtitle text contains mathematical notation; when read aloud these symbols
expand into several words.  Estimating the spoken length from the *pronounced*
text lets each scene hold exactly long enough for natural-rate narration.
"""

PRONOUNCE = {
    "α": "alpha", "β": "beta", "γ": "gamma", "δ": "delta", "ε": "epsilon",
    "θ": "theta", "λ": "lambda", "μ": "mu", "π": "pi", "σ": "sigma",
    "τ": "tau", "φ": "phi", "ω": "omega", "Δ": "delta", "Σ": "sum",
    "∫": "integral", "≈": "about", "≥": "at least", "≤": "at most",
    "≠": "not equal to", "→": "to", "∈": "in", "∝": "proportional to",
    "ᵀ": " transpose", "⁻¹": " inverse", "₀": "0", "₁": "1", "₂": "2",
    "₃": "3", "ᵢ": "i", "ⱼ": "j", "̄": "", "×": " times", "−": "-",
    "ρ": "rho", "ψ": "psi", "κ": "kappa", "ζ": "zeta", "η": "eta",
    "Γ": "Gamma", "Ω": "Omega", "∞": "infinity", "∑": "sum",
    "²": " squared", "³": " cubed", "√(1−ρ²)": "square root of one minus rho squared",
}


def pronounce(text: str) -> str:
    for src, dst in PRONOUNCE.items():
        text = text.replace(src, dst)
    return text


def spoken_duration(text: str, base: float = 4.0) -> float:
    """Seconds needed to say ``text`` at the fixed natural narration rate."""
    words = len(pronounce(text).split())
    # Conservative: mathematical punctuation is read out letter-by-letter.
    return max(base, round(0.55 * words + 1.2, 2))
