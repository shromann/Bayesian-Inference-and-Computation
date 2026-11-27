# Bayesian Inference and Computation — animated walkthroughs

Subtitled, narrated Manim walkthroughs for Weeks 7–10, built from the lecture
and tutorial PDFs in `lectures/` and `tutorial/`.

## Repository layout

```
src/                 Manim source and build tooling
  common.py            shared clip-safe scene framework (Weeks 8–10)
  build_week.py        stitch scenes, merge SRTs, generate narration, mux
  narrate.py           macOS `say` narration timed from SRT cues
  speech.py            pronunciation map and spoken-length estimates
  verify.py            final QA: streams, durations, SRT indices, decode
  week7/               Week 7 scenes, plan, README
  week8/               Week 8 scenes and plan
  week9/               Week 9 scenes and plan
  week10/              Week 10 scenes and plan
videos/              final artifacts
  week7/               final.mp4, final.srt, final_subtitled.mp4,
                       narration.m4a, final_narrated.mp4
  week8/               (same)
  week9/               (same)
  week10/              (same)
```

`final_narrated.mp4` is the finished video: burned-in-safe layout, soft
subtitles (`mov_text`), and a local macOS narration track. `final.srt` is a
standalone subtitle file for the whole week.

## Rebuild

```sh
# render every scene of a week (LaTeX needs MacTeX on PATH)
cd src/week8
PATH="/Library/TeX/texbin:$PATH" ../../.venv/bin/manim -ql script.py

# stitch + subtitle + narrate + mux
cd ../..
.venv/bin/python src/build_week.py week8
```

## Design notes

- All text is fitted into a safe frame (`fit()` in `src/common.py` and
  `src/week7/script.py`), so equations and labels never leave the 854×480 frame.
- Subtitles come from Manim's `add_subcaption`, merged into one SRT per week.
- Narration is generated locally with `say -v Samantha` at a fixed natural rate
  (210 wpm), so no external API key is required. Each caption's on-screen hold is
  computed from its *spoken* length (`src/speech.py`), so mathematical symbols
  never force the voice to speed up or overlap the next cue.
