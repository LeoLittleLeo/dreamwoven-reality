#!/usr/bin/env python3
"""Inspect image dimensions and reliable embedded capture metadata."""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path
from typing import Any

from PIL import ExifTags, Image


DATE_TAGS = ("DateTimeOriginal", "DateTimeDigitized", "DateTime")


def normalize_date(value: Any) -> str | None:
    if not value:
        return None
    text = str(value).strip().replace("\x00", "")
    for pattern in ("%Y:%m:%d %H:%M:%S", "%Y-%m-%d %H:%M:%S"):
        try:
            return datetime.strptime(text[:19], pattern).isoformat(sep=" ")
        except ValueError:
            pass
    return None


def inspect(path: Path) -> dict[str, Any]:
    with Image.open(path) as image:
        exif = image.getexif()
        named = {ExifTags.TAGS.get(tag, str(tag)): value for tag, value in exif.items()}
        capture_tag = None
        capture_date = None
        for tag in DATE_TAGS:
            capture_date = normalize_date(named.get(tag))
            if capture_date:
                capture_tag = tag
                break
        return {
            "path": str(path),
            "format": image.format,
            "width": image.width,
            "height": image.height,
            "orientation": "landscape" if image.width > image.height else "portrait" if image.height > image.width else "square",
            "capture_date": capture_date,
            "capture_date_source": capture_tag,
            "camera_make": named.get("Make"),
            "camera_model": named.get("Model"),
            "embedded_description": named.get("ImageDescription"),
            "filesystem_times_are_capture_metadata": False,
        }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("image", type=Path)
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args()
    if not args.image.is_file():
        parser.error(f"image not found: {args.image}")
    print(json.dumps(inspect(args.image), ensure_ascii=False, indent=2 if args.pretty else None, default=str))


if __name__ == "__main__":
    main()
