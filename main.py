#!/usr/bin/env python3
"""news-image-20261121: publish the committed front page for 21 Nov 2026.

The picture is the entry. It is a newspaper-style summary of the day's
world news, drawn when the entry was built and stored beside this file as
entry.png. At grade time this program does nothing clever: it places an
exact copy of that picture at the output path the harness asks for. It
needs no network, no third-party package and no clock, so running it
twice writes the same bytes twice.
"""
import os
import shutil
import sys
from pathlib import Path


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target = out_dir / "entry.png"
    if not source.is_file():
        print(f"missing committed image: {source}", file=sys.stderr)
        return 1
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)
    print(f"wrote {target} ({target.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
