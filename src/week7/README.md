# Week 7 animated explainer

Animated, subtitled, narrated walkthrough of `lectures/Lecture Week 7.pdf`
(46 pages) and `tutorial/Tutorial Week 7.pdf` (5 questions), produced with the
`manim-video` skill.

## Files

- `plan.md` — narrative arc, 21-scene outline, and verified numerics.
- `script.py` — one Manim `Scene` class per chapter/tutorial problem. Text is
  auto-fitted into the safe frame so nothing clips at 854×480.
- `media/videos/script/480p15/` — draft MP4s and matching `.srt` tracks.
- `../../videos/week7/` — stitched, subtitled and narrated final artifacts.

## Reproduce

```bash
cd src/week7
export PATH="/Library/TeX/texbin:$PATH"   # MacTeX is installed outside the default PATH
../../.venv/bin/manim -ql script.py        # renders all 21 scenes
cd ../..
.venv/bin/python src/build_week.py week7   # stitch + subtitle + narrate + mux
```

For higher quality, replace `-ql` with `-qm` or `-qh` (outputs land in
`720p30` / `1080p60`; update the build script's media directory accordingly).
