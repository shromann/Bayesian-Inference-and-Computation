# Bayesian Inference and Computation

[![Obsidian](https://img.shields.io/badge/Obsidian-Vault-7C3AED?logo=obsidian&logoColor=white)](https://obsidian.md)
[![Markdown](https://img.shields.io/badge/Markdown-Notes-000000?logo=markdown&logoColor=white)](https://commonmark.org)
[![LaTeX](https://img.shields.io/badge/LaTeX-Math-008080?logo=latex&logoColor=white)](https://www.latex-project.org)

An Obsidian vault of course notes for **MATH3871/MATH5960 — Bayesian Inference and Computation** (Term 3, 2026, Prof. Scott Sisson), turned into a linked knowledge graph so the material can be learned by following how one idea builds on the next.

## How to use this vault

1. Open the folder as an Obsidian vault.
2. Start at **`notes/Bayesian Inference and Computation.md`** — the Home map.
3. Follow the **Builds on** / **Leads to** links in each note's *Connections* section.
4. Use **Graph view** (colour-coded by week/type) and the **Backlinks** panel to explore.
5. Follow any note's **Source** link to jump back to the original lecture/tutorial PDF.

## Structure

```
.
├── lectures/   # Lecture PDFs (Weeks 1–4)
├── tutorial/   # Tutorial problem PDFs (Weeks 1–4)
└── notes/      # The knowledge graph (60 interlinked markdown notes)
    ├── Bayesian Inference and Computation.md   # Home map (start here)
    ├── Week 1/   # Foundations, frequentist vs Bayesian, Monte Carlo basics
    ├── Week 2/   # Conjugate/improper/Jeffreys priors, inversion sampling
    ├── Week 3/   # Mixture priors, multivariate models, rejection sampling
    ├── Week 4/   # Decisions, asymptotics, importance sampling
    └── Reference/ # Distribution notes, Glossary, Probability Distributions, History
```

## Note conventions

Every concept note follows the same template:

- **Frontmatter** — `tags`, `week`, `type` (used by the colour-coded graph).
- **One-line summary** — an `> [!abstract]` callout.
- **Body** — intuition, formal results, and worked examples with LaTeX maths.
- **Connections** — `Builds on` (prerequisites), `Leads to` (what's next), `See also`.
- **Source** — links to the originating slide(s)/question(s).

Links use Obsidian `[[wikilinks]]`, which resolve by note name regardless of folder, so moving a note never breaks the graph. Notes are placed in the week they are introduced (per `week` frontmatter); cross-cutting reference notes live in `Reference/`.

## Course roadmap

| Week | Theme | Overview |
|---|---|---|
| 1 | Foundations & Monte Carlo | `notes/Week 1/Week 1 Overview.md` |
| 2 | Priors & inversion sampling | `notes/Week 2/Week 2 Overview.md` |
| 3 | Multivariate models & rejection sampling | `notes/Week 3/Week 3 Overview.md` |
| 4 | Decisions, asymptotics & importance sampling | `notes/Week 4/Week 4 Overview.md` |

## Reference

- `notes/Reference/Probability Distributions.md` — index of distributions used.
- `notes/Week 2/Conjugate Prior Reference Table.md` — all standard conjugate pairs.
- `notes/Reference/Glossary.md` — every symbol and term in one place.

## Notes

- The vault is plain markdown; no plugins beyond Obsidian core are required.
- PDFs are the original source material and are linked from the notes, not modified.
