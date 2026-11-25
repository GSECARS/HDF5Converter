#!/usr/bin/env python3
"""Generate .ico and .icns from sciconvert/assets/sciconvert.png"""
import struct
import zlib
from pathlib import Path
from PIL import Image

SRC = Path("sciconvert/assets/sciconvert.png")
ASSETS = SRC.parent

ICO_SIZES = [16, 32, 48, 64, 128, 256]
ICNS_SIZES = {
    "icp4": 16,
    "icp5": 32,
    "icp6": 64,
    "ic07": 128,
    "ic08": 256,
    "ic09": 512,
    "ic10": 1024,
    "ic11": 32,   # @2x of 16
    "ic12": 64,   # @2x of 32
    "ic13": 256,  # @2x of 128
    "ic14": 512,  # @2x of 256
}

img = Image.open(SRC).convert("RGBA")


def make_ico():
    out = ASSETS / "sciconvert.ico"
    sizes = [(s, s) for s in ICO_SIZES]
    img.save(out, format="ICO", sizes=sizes)
    print(f"Created {out}")


def make_icns():
    out = ASSETS / "sciconvert.icns"

    def png_bytes(size):
        from io import BytesIO
        buf = BytesIO()
        img.resize((size, size), Image.LANCZOS).save(buf, format="PNG")
        return buf.getvalue()

    chunks = []
    for ostype, size in ICNS_SIZES.items():
        data = png_bytes(size)
        key = ostype.encode("ascii")
        length = 8 + len(data)
        chunks.append(struct.pack(">4sI", key, length) + data)

    body = b"".join(chunks)
    header = struct.pack(">4sI", b"icns", 8 + len(body))

    out.write_bytes(header + body)
    print(f"Created {out}")


make_ico()
make_icns()
