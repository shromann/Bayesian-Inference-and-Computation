#!/usr/bin/env python3
"""Final QA for the narrated week videos."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def probe(path: Path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                          "format=duration:stream=codec_type,codec_name",
                          "-of", "json", str(path)], capture_output=True,
                         text=True, check=True).stdout
    return json.loads(out)


def main():
    ok = True
    for week in ("week7", "week8", "week9", "week10"):
        d = ROOT / "videos" / week
        final = d / "final.mp4"
        out = d / "final_narrated.mp4"
        srt = d / "final.srt"
        problems = []
        if not (final.exists() and out.exists() and srt.exists()):
            problems.append("missing artifact")
            print(f"{week}: FAIL {problems}")
            ok = False
            continue
        info = probe(out)
        types = {s["codec_type"] for s in info["streams"]}
        if not {"video", "audio", "subtitle"} <= types:
            problems.append(f"streams={sorted(types)}")
        fd = float(probe(final)["format"]["duration"])
        od = float(info["format"]["duration"])
        if abs(fd - od) > 1.5:
            problems.append(f"duration mismatch {fd:.1f} vs {od:.1f}")
        blocks = srt.read_text().strip().split("\n\n")
        ids = [b.splitlines()[0] for b in blocks]
        if ids != [str(i) for i in range(1, len(ids) + 1)]:
            problems.append("SRT indices not sequential")
        dec = subprocess.run(["ffmpeg", "-v", "error", "-i", str(out),
                              "-f", "null", "-"], capture_output=True, text=True)
        if dec.returncode != 0:
            problems.append("decode failed")
        status = "OK" if not problems else "FAIL"
        print(f"{week}: {status}  {od:.1f}s  {len(ids)} cues  "
              f"streams={sorted(types)}" + (f"  problems={problems}" if problems else ""))
        ok = ok and not problems
    raise SystemExit(0 if ok else 1)


if __name__ == "__main__":
    main()
