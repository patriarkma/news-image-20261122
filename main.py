"""Entrypoint: copy the front-page image to /output/entry.png.

Verifies the image is a whole PNG within the competition's caps
(<=1 MiB, <=1024x1024) before copying, so the run is deterministic:
the same bytes are written on every run.
"""
import os
import shutil
import struct
import sys

MAX_BYTES = 1_048_576
MAX_SIDE = 1024


def read_png_size(path):
    with open(path, "rb") as f:
        head = f.read(33)
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("entry.png is not a PNG file")
    if head[12:16] != b"IHDR":
        raise ValueError("entry.png has no IHDR chunk")
    width, height = struct.unpack(">II", head[16:24])
    return width, height


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    # The grader sets MAKEFUN_OUTPUT_DIR; /output is the documented default.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")

    size = os.path.getsize(src)
    if size > MAX_BYTES:
        raise ValueError(f"entry.png is {size} bytes, over the 1 MiB cap")
    width, height = read_png_size(src)
    if width > MAX_SIDE or height > MAX_SIDE:
        raise ValueError(f"entry.png is {width}x{height}, over 1024x1024")
    if width != 1024 or height != 1024:
        raise ValueError(f"entry.png is {width}x{height}, expected 1024x1024")

    shutil.copyfile(src, dst)
    print(f"wrote {dst} ({size} bytes, {width}x{height})")


if __name__ == "__main__":
    try:
        main()
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
