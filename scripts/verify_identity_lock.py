#!/usr/bin/env python3
"""Block delivery unless protected source pixels survive unchanged.

The aligned source and final artwork must share the exact output canvas. Masks
are binary PNGs where white pixels are protected. A successful run writes a
JSON receipt bound to the final file's SHA-256 digest.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def load_rgb(path: Path) -> Image.Image:
    return Image.open(path).convert("RGB")


def load_binary_mask(path: Path, size: tuple[int, int], name: str) -> tuple[Image.Image, int]:
    mask = Image.open(path).convert("L")
    if mask.size != size:
        raise ValueError(f"{name} size {mask.size} does not match final canvas {size}")
    pixels = mask.get_flattened_data()
    values = set(pixels)
    if not values.issubset({0, 255}):
        raise ValueError(f"{name} must be binary (only 0 and 255); found {sorted(values)[:8]}")
    count = sum(1 for value in pixels if value == 255)
    if count == 0:
        raise ValueError(f"{name} contains no protected pixels")
    return mask, count


def max_delta(source: Image.Image, final: Image.Image, mask: Image.Image) -> int:
    maximum = 0
    for expected, actual, locked in zip(
        source.get_flattened_data(), final.get_flattened_data(), mask.get_flattened_data()
    ):
        if locked == 255:
            maximum = max(maximum, *(abs(a - b) for a, b in zip(expected, actual)))
    return maximum


def white_bbox(mask: Image.Image) -> tuple[int, int, int, int]:
    box = mask.getbbox()
    if box is None:
        raise ValueError("mask contains no protected pixels")
    return box


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--aligned-source", type=Path, required=True)
    parser.add_argument("--final", type=Path, required=True)
    parser.add_argument("--person-mask", type=Path, required=True)
    parser.add_argument("--face-mask", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()

    try:
        source = load_rgb(args.aligned_source)
        final = load_rgb(args.final)
        if source.size != final.size:
            raise ValueError(f"aligned source size {source.size} does not match final {final.size}")
        person, person_pixels = load_binary_mask(args.person_mask, final.size, "person mask")
        face, face_pixels = load_binary_mask(args.face_mask, final.size, "face mask")
        if any(
            f == 255 and p != 255
            for f, p in zip(face.get_flattened_data(), person.get_flattened_data())
        ):
            raise ValueError("face mask must be completely contained inside person mask")
        if person_pixels < face_pixels * 1.5:
            raise ValueError("person mask is too small relative to face mask; face-only restoration is forbidden")
        person_box, face_box = white_bbox(person), white_bbox(face)
        if person_box[3] <= face_box[3]:
            raise ValueError("person mask must extend below the face to cover the visible body")
        person_delta = max_delta(source, final, person)
        face_delta = max_delta(source, final, face)
        if person_delta != 0 or face_delta != 0:
            raise ValueError(
                f"P00 face-lock-breach: person max delta={person_delta}, face max delta={face_delta}"
            )

        report = {
            "status": "PASS",
            "gate": "P00-deterministic-identity-lock",
            "verified_at": datetime.now(timezone.utc).isoformat(),
            "canvas": {"width": final.width, "height": final.height},
            "person_mask_pixels": person_pixels,
            "face_mask_pixels": face_pixels,
            "person_max_pixel_delta": person_delta,
            "face_max_pixel_delta": face_delta,
            "final_path": str(args.final.resolve()),
            "final_sha256": digest(args.final),
            "aligned_source_sha256": digest(args.aligned_source),
            "person_mask_sha256": digest(args.person_mask),
            "face_mask_sha256": digest(args.face_mask),
        }
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(report, indent=2))
        return 0
    except Exception as error:
        print(f"BLOCKED: {error}", file=sys.stderr)
        if args.report.exists():
            args.report.unlink()
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
