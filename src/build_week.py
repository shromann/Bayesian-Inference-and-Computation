#!/usr/bin/env python3
"""Stitch Manim scenes of one week into a subtitled, narrated final video."""

from __future__ import annotations

import argparse
import importlib.util
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def scene_names(week: str) -> list[str]:
    path = ROOT / week / "script.py"
    spec = importlib.util.spec_from_file_location(f"script_{week}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if hasattr(module, "SCENE_NAMES"):
        return list(module.SCENE_NAMES)
    return [n for n in dir(module) if re.match(r"^S\d+_", n)]


def dur(path: Path) -> float:
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "default=nw=1:nk=1", str(path)],
                         capture_output=True, text=True, check=True).stdout.strip()
    return float(out)


def shift_srt(src: Path, offset: float) -> list[str]:
    text = src.read_text(encoding="utf-8", errors="replace").replace("\r", "")
    out = []
    for block in re.split(r"\n\s*\n", text.strip()):
        lines = [ln for ln in block.splitlines() if ln.strip()]
        if len(lines) < 3:
            continue
        def fmt_parts(parts):
            h, mi, s, ms = (int(x) for x in parts)
            total = h * 3600 + mi * 60 + s + ms / 1000 + offset
            h = int(total // 3600)
            mi = int((total % 3600) // 60)
            s = int(total % 60)
            ms = int(round((total - int(total)) * 1000))
            return f"{h:02d}:{mi:02d}:{s:02d},{ms:03d}"
        lines[1] = re.sub(
            r"(\d+):(\d+):(\d+),(\d+)\s*-->\s*(\d+):(\d+):(\d+),(\d+)",
            lambda m: f"{fmt_parts(m.groups()[:4])} --> {fmt_parts(m.groups()[4:])}",
            lines[1])
        out.append("\n".join(lines))
    return out


def build(week: str, narration: bool = True):
    names = scene_names(week)
    wdir = ROOT / week
    media = wdir / "media/videos/script/480p15"
    videos = ROOT.parent / "videos" / week
    videos.mkdir(parents=True, exist_ok=True)
    clips = []
    for name in names:
        mp4 = media / f"{name}.mp4"
        srt = media / f"{name}.srt"
        if not mp4.exists():
            raise SystemExit(f"Missing render: {mp4}")
        clips.append((mp4, srt, dur(mp4)))

    concat = wdir / "concat.txt"
    concat.write_text("".join(f"file '{c[0]}'\n" for c in clips))
    final = videos / "final.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0",
                    "-i", str(concat), "-c", "copy", str(final)], check=True)

    cues = []
    offset = 0.0
    for mp4, srt, length in clips:
        if srt.exists():
            cues.extend(shift_srt(srt, offset))
        offset += length
    for i, block in enumerate(cues, 1):
        lines = block.splitlines()
        lines[0] = str(i)
        cues[i - 1] = "\n".join(lines)
    srt_out = videos / "final.srt"
    srt_out.write_text("\n\n".join(cues) + "\n", encoding="utf-8")

    subtitled = videos / "final_subtitled.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(final),
                    "-i", str(srt_out), "-map", "0:v", "-map", "0:a?", "-map", "1:s",
                    "-c:v", "copy", "-c:a", "copy", "-c:s", "mov_text",
                    str(subtitled)], check=True)

    audio = videos / "narration.m4a"
    if narration or not audio.exists():
        subprocess.run([sys.executable, str(ROOT / "narrate.py"), str(srt_out), str(audio)],
                       check=True)

    if audio.exists():
        narrated = videos / "final_narrated.mp4"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(subtitled), "-i", str(audio),
                        "-map", "0:v", "-map", "0:s?", "-map", "1:a",
                        "-c", "copy", "-shortest", str(narrated)], check=True)
        print(f"{week}: {len(clips)} scenes, {offset:.1f}s -> {narrated}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("week")
    ap.add_argument("--no-narration", action="store_true",
                    help="reuse an existing narration.m4a instead of regenerating it")
    a = ap.parse_args()
    build(a.week, narration=not a.no_narration)
