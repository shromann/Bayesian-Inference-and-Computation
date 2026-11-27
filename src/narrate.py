#!/usr/bin/env python3
"""Generate a timed narration track from a Manim-generated SRT file.

Uses macOS ``say`` (local, no API key).  Every cue is synthesised at one fixed,
natural speaking rate; the scenes are held long enough for the speech to fit.
The resulting PCM is mixed onto a timeline at each cue's start time.  Output is
a 22.05 kHz mono WAV which can be muxed with ffmpeg.
"""

from __future__ import annotations

import argparse
from array import array
import re
import subprocess
import sys
import tempfile
import wave
from pathlib import Path

from speech import pronounce

RATE = 22050          # samples / second
SAMPLE_WIDTH = 2      # 16-bit mono
VOICE = "Samantha"
SPEAKING_RATE = 210  # words per minute — natural, unhurried narration


def parse_srt(path: Path):
    raw = path.read_text(encoding="utf-8", errors="replace").replace("\r", "")
    blocks = re.split(r"\n\s*\n", raw.strip())
    cues = []
    for block in blocks:
        lines = [ln for ln in block.splitlines() if ln.strip()]
        if len(lines) < 3:
            continue
        m = re.match(r"(\d+):(\d+):(\d+)[,.](\d+)\s*-->\s*"
                     r"(\d+):(\d+):(\d+)[,.](\d+)", lines[1])
        if not m:
            continue
        g = [int(x) for x in m.groups()]
        start = g[0] * 3600 + g[1] * 60 + g[2] + g[3] / (10 ** len(str(g[3])))
        end = g[4] * 3600 + g[5] * 60 + g[6] + g[7] / (10 ** len(str(g[7])))
        text = " ".join(lines[2:]).strip()
        text = re.sub(r"<[^>]+>", "", text)
        cues.append((start, end, text))
    return cues


def seconds(script: str) -> float:
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "default=nw=1:nk=1", script],
                         capture_output=True, text=True, check=True).stdout.strip()
    return float(out)


def synthesise(text: str, rate: int, tmp: Path) -> bytes:
    aiff = tmp / f"cue_{rate}.aiff"
    subprocess.run(["say", "-v", VOICE, "-r", str(rate), "-o", str(aiff), text],
                   check=True, capture_output=True)
    pcm = subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(aiff),
                          "-f", "s16le", "-ac", "1", "-ar", str(RATE), "-"],
                         capture_output=True, check=True).stdout
    return pcm


def build(srt: Path, out: Path, voice: str = VOICE):
    global VOICE
    VOICE = voice
    cues = parse_srt(srt)
    if not cues:
        raise SystemExit(f"No cues found in {srt}")
    total = max(c[1] for c in cues) + 0.5
    buffer = array("h", [0]) * int(total * RATE)
    with tempfile.TemporaryDirectory(prefix="narration-") as td:
        tmp = Path(td)
        for i, (start, end, text) in enumerate(cues, 1):
            if not text:
                continue
            text = pronounce(text)
            pcm = synthesise(text, SPEAKING_RATE, tmp)
            spoken = len(pcm) / (RATE * SAMPLE_WIDTH)
            window = max(0.6, end - start)
            if spoken > window + 0.25:
                print(f"  cue {i}: speech {spoken:.1f}s exceeds {window:.1f}s window; "
                      "aligning its end to the cue end", file=sys.stderr)
                start = max(0.0, end - spoken)
            samples = array("h")
            samples.frombytes(pcm)
            offset = int(start * RATE)
            # Mix into the timeline with hard clipping (cues do not overlap in SRT).
            for j, sample in enumerate(samples):
                pos = offset + j
                if pos < len(buffer):
                    buffer[pos] = max(-32768, min(32767, buffer[pos] + sample))
            if i % 20 == 0 or i == len(cues):
                print(f"  narrated {i}/{len(cues)} cues", file=sys.stderr)
    wav = out.with_suffix(".wav")
    with wave.open(str(wav), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(SAMPLE_WIDTH)
        w.setframerate(RATE)
        w.writeframes(buffer)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(wav),
                    "-c:a", "aac", "-b:a", "128k", str(out)], check=True)
    wav.unlink()
    print(f"Narration written to {out} ({total:.1f}s)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("srt", type=Path)
    ap.add_argument("out", type=Path)
    ap.add_argument("--voice", default=VOICE)
    a = ap.parse_args()
    build(a.srt, a.out, a.voice)
