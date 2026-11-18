#!/usr/bin/env python3
"""Entry for make.fun news-image-20261118: sum up 18 November 2026 world news in one image.

The image (entry.png, JPEG bytes, 1024x1024, <1 MiB) is a newspaper front
page for Wednesday 18 November 2026, built from that day's reported news:
Iran strikes Bahrain and Kuwait after the U.S. hits a missile site on
Qeshm Island; the Kerch Bridge span falls into the strait on the second
day of Ukrainian strikes; APEC opens in Shenzhen as Xi hosts Putin ahead
of Thursday's first Trump-Xi-Putin summit, with the Quad meeting in
Manila; Ebola in Congo more than doubles past 11,000 cases and 5,400
deaths; and the U.S. loses its measles-free status held for 26 years.
Ticker: Cyclone Xavier hits the Cook Islands, a Russian military plane
crash kills 19, Democrats win the Alaska Senate seat, and Gaza cold
kills in tents. The program copies it to /output/entry.png (or
$MAKEFUN_OUTPUT_DIR/entry.png). Deterministic: same input bytes always
produce the same output bytes. No network, stdlib only.
"""
import hashlib
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUT = os.path.join(OUT_DIR, "entry.png")
os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(SRC, OUT)


def _sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


# Self-check: the copied file must be byte-identical to the source image.
# A partial or failed copy must fail loudly instead of scoring a corrupt image.
if _sha256(SRC) != _sha256(OUT):
    raise SystemExit("entry.png copy failed verification")
print("wrote {} ({} bytes, sha256 {})".format(OUT, os.path.getsize(OUT), _sha256(OUT)[:16]))
