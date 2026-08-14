#!/usr/bin/env python3
"""Compose the single processed 53/2/43/2 editorial artwork."""

from __future__ import annotations

import argparse
import colorsys
import platform
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageStat


FONT_CANDIDATES = {
    "Darwin": [
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
        "/Library/Fonts/Arial Unicode.ttf",
        "/System/Library/Fonts/STHeiti Light.ttc",
    ],
    "Windows": ["C:/Windows/Fonts/msyhl.ttc", "C:/Windows/Fonts/msyh.ttc"],
    "Linux": [
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Light.ttc",
        "/usr/share/fonts/opentype/source-han-sans/SourceHanSansCN-Light.otf",
        "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
    ],
}

ROBOT_DREAMS_BOARD_BASES = {
    "warm-ivory": (239, 228, 207),
    "dusty-peach": (232, 207, 196),
    "powder-blue": (205, 220, 229),
    "soft-lilac": (220, 211, 228),
    "mineral-sage": (210, 220, 204),
}


def parse_color(value: str) -> tuple[int, int, int]:
    value = value.strip().lstrip("#")
    if len(value) != 6:
        raise argparse.ArgumentTypeError("color must be a 6-digit hex value")
    try:
        return tuple(int(value[i : i + 2], 16) for i in (0, 2, 4))  # type: ignore[return-value]
    except ValueError as error:
        raise argparse.ArgumentTypeError("color must be hexadecimal") from error


def find_font(explicit: Path | None) -> Path:
    if explicit:
        if explicit.is_file():
            return explicit
        raise FileNotFoundError(f"font not found: {explicit}")
    for candidate in FONT_CANDIDATES.get(platform.system(), []):
        path = Path(candidate)
        if path.is_file():
            return path
    raise FileNotFoundError("No suitable font found. Pass --font /path/to/CJK-font.ttf or .ttc")


def fit_source_cover(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    """Proportionally cover the target, allowing centered source-aware cropping."""
    return ImageOps.fit(image.convert("RGB"), size, method=Image.Resampling.LANCZOS, centering=(0.5, 0.5))


def derive_ground(image: Image.Image) -> tuple[int, int, int]:
    """Select a pale Robot Dreams board base from the source palette relationship."""
    sample = ImageOps.fit(image.convert("RGB"), (96, 96), method=Image.Resampling.BILINEAR)
    colors = sample.quantize(colors=8, method=Image.Quantize.MEDIANCUT).convert("RGB").getcolors()
    assert colors is not None
    total = sum(count for count, _ in colors)
    hue_weights = {"warm": 0.0, "blue": 0.0, "green": 0.0, "neutral": 0.0}
    mean_luminance = 0.0
    for count, color in colors:
        weight = count / total
        red, green, blue = (channel / 255 for channel in color)
        hue, saturation, value = colorsys.rgb_to_hsv(red, green, blue)
        mean_luminance += weight * value
        if saturation < 0.13:
            hue_weights["neutral"] += weight
        elif hue < 0.12 or hue >= 0.92:
            hue_weights["warm"] += weight
        elif 0.12 <= hue < 0.47:
            hue_weights["green"] += weight
        else:
            hue_weights["blue"] += weight

    dominant = max(("warm", "blue", "green"), key=hue_weights.get)
    if hue_weights["neutral"] >= 0.62:
        base_name = "soft-lilac" if mean_luminance > 0.68 else "warm-ivory"
    elif dominant == "blue":
        base_name = "dusty-peach"
    elif dominant == "warm":
        base_name = "powder-blue"
    else:
        base_name = "warm-ivory" if mean_luminance < 0.62 else "mineral-sage"

    base = ROBOT_DREAMS_BOARD_BASES[base_name]
    source_mean = ImageStat.Stat(sample).mean
    return tuple(round(base[i] * 0.88 + source_mean[i] * 0.12) for i in range(3))  # type: ignore[return-value]


def fit_processed_band_font(font_path: Path, texts: tuple[str, ...], max_width: int, start_size: int):
    """Return one shared font size that fits every non-empty band line."""
    active = tuple(text for text in texts if text)
    for size in range(max(12, start_size), 11, -2):
        font = ImageFont.truetype(str(font_path), size)
        if all(font.getlength(text) <= max_width for text in active):
            return font
    return ImageFont.truetype(str(font_path), 12)


def fit_upper_authored_image(
    artwork: Image.Image,
    board_size: tuple[int, int],
    target_occupancy: float = 0.80,
) -> tuple[Image.Image, Image.Image, float]:
    """Fit visible RGBA area to the board while preserving the authored contour."""
    source = artwork.convert("RGBA")
    source_alpha = source.getchannel("A")
    bbox = source_alpha.getbbox()
    if not bbox:
        raise ValueError("upper authored image has no visible alpha content")
    source = source.crop(bbox)
    source_alpha = source_alpha.crop(bbox)

    alpha_area = sum(ImageStat.Stat(source_alpha).sum) / 255.0
    board_area = board_size[0] * board_size[1]
    desired_scale = (target_occupancy * board_area / max(alpha_area, 1.0)) ** 0.5
    fit_scale = min(board_size[0] / source.width, board_size[1] / source.height)
    scale = min(desired_scale, fit_scale)
    fitted_size = (max(1, round(source.width * scale)), max(1, round(source.height * scale)))

    fitted = source.resize(fitted_size, Image.Resampling.LANCZOS)
    fitted_alpha = fitted.getchannel("A")
    visible_area = sum(ImageStat.Stat(fitted_alpha).sum) / 255.0
    occupancy = visible_area / board_area
    return fitted.convert("RGB"), fitted_alpha, occupancy


def prepare_upper_artwork(artwork: Image.Image, mask_path: Path | None) -> Image.Image:
    """Return an RGBA upper artwork from true alpha or one explicit contour mask."""
    has_alpha = artwork.mode in ("RGBA", "LA")
    if has_alpha and mask_path:
        raise ValueError("use either upper RGBA alpha or --art-mask, not both")
    if has_alpha:
        return artwork.convert("RGBA")
    if not mask_path:
        raise ValueError("--upper-poster must have authored alpha or use --art-mask")
    if not mask_path.is_file():
        raise FileNotFoundError(f"mask not found: {mask_path}")
    mask = Image.open(mask_path).convert("L")
    if mask.size != artwork.size:
        raise ValueError("--art-mask dimensions must match --upper-poster")
    upper = artwork.convert("RGBA")
    upper.putalpha(mask)
    return upper


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("processed",), default="processed")
    parser.add_argument("--original", required=True, type=Path)
    parser.add_argument("--upper-poster", required=True, type=Path, help="free-edged RGBA partial abstraction")
    parser.add_argument("--poster", required=True, type=Path, help="rectangular extreme lower abstraction")
    parser.add_argument("--title", default="")
    parser.add_argument("--subtitle", default="")
    parser.add_argument("--copy-free", action="store_true", help="omit title and subtitle")
    parser.add_argument("--single-text-level", choices=("title", "subtitle"))
    parser.add_argument("--art-mask", type=Path, help="explicit upper outer-contour mask; use only with RGB upper art")
    parser.add_argument("--mask-preview", action="store_true", help="export the fitted upper alpha mask")
    parser.add_argument("--output-dir", type=Path, default=Path("outputs"))
    parser.add_argument("--basename", default=None)
    parser.add_argument("--font", type=Path)
    parser.add_argument("--background-color", type=parse_color)
    parser.add_argument("--text-color", type=parse_color)
    parser.add_argument("--width", type=int, default=None, help="optional proportional export width cap")
    parser.add_argument("--height", type=int, default=None, help="optional proportional export height cap")
    parser.add_argument("--export-long-edge", type=int, default=3000, help="maximum output long edge; 0 disables")
    args = parser.parse_args()

    if args.copy_free and (args.title or args.subtitle or args.single_text_level):
        parser.error("--copy-free cannot be combined with title, subtitle, or --single-text-level")
    if args.single_text_level == "title" and (not args.title or args.subtitle):
        parser.error("--single-text-level title requires --title and prohibits --subtitle")
    if args.single_text_level == "subtitle" and (not args.subtitle or args.title):
        parser.error("--single-text-level subtitle requires --subtitle and prohibits --title")
    if any(value is not None and value <= 0 for value in (args.width, args.height)):
        parser.error("width and height caps must be positive")
    if args.export_long_edge < 0:
        parser.error("--export-long-edge may be 0 to disable but cannot be negative")
    for path in (args.original, args.upper_poster, args.poster):
        if not path.is_file():
            parser.error(f"image not found: {path}")

    original_source = Image.open(args.original)
    upper_source = Image.open(args.upper_poster)
    lower_source = Image.open(args.poster)
    try:
        upper_source = prepare_upper_artwork(upper_source, args.art_mask)
    except (ValueError, FileNotFoundError) as error:
        parser.error(str(error))

    original = original_source.convert("RGB")
    raw_width = original.width
    raw_height = round(original.height / 0.53)
    limits = [1.0]
    if args.width:
        limits.append(args.width / raw_width)
    if args.height:
        limits.append(args.height / raw_height)
    if args.export_long_edge:
        limits.append(args.export_long_edge / max(raw_width, raw_height))
    scale = min(limits)
    paper_width = max(1, round(raw_width * scale))
    paper_height = max(1, round(raw_height * scale))

    upper_h = round(paper_height * 0.53)
    title_band_h = max(1, round(paper_height * 0.02))
    lower_h = round(paper_height * 0.43)
    subtitle_band_h = max(1, paper_height - upper_h - title_band_h - lower_h)

    ground = args.background_color or derive_ground(original)
    canvas = Image.new("RGB", (paper_width, paper_height), ground)
    draw = ImageDraw.Draw(canvas)

    upper_art, upper_mask, upper_occupancy = fit_upper_authored_image(upper_source, (paper_width, upper_h))
    if not 0.75 <= upper_occupancy <= 0.85:
        parser.error(
            f"upper authored image occupies {upper_occupancy:.1%} of its 53% board; "
            "provide a contour that can reach 75%-85% without clipping or distortion"
        )
    upper_x = (paper_width - upper_art.width) // 2
    upper_y = (upper_h - upper_art.height) // 2
    canvas.paste(upper_art, (upper_x, upper_y), upper_mask)

    title_band_y = upper_h
    lower_y = title_band_y + title_band_h
    lower = fit_source_cover(lower_source, (paper_width, lower_h))
    canvas.paste(lower, (0, lower_y))
    subtitle_band_y = lower_y + lower_h

    black_ink = (28, 28, 28)
    band_text = args.text_color or (244, 239, 226)
    draw.rectangle((0, title_band_y, paper_width, lower_y), fill=black_ink)
    draw.rectangle((0, subtitle_band_y, paper_width, subtitle_band_y + subtitle_band_h), fill=black_ink)

    has_copy = bool(args.title or args.subtitle)
    if has_copy:
        font_path = find_font(args.font)
        band_font = fit_processed_band_font(
            font_path,
            (args.title, args.subtitle),
            round(paper_width * 0.82),
            max(10, round(min(title_band_h, subtitle_band_h) * 0.52)),
        )
        if args.title:
            bounds = draw.textbbox((0, 0), args.title, font=band_font)
            x = (paper_width - (bounds[2] - bounds[0])) / 2
            y = title_band_y + (title_band_h - band_font.size) // 2 - 2
            draw.text((x, y), args.title, font=band_font, fill=band_text)
        if args.subtitle:
            bounds = draw.textbbox((0, 0), args.subtitle, font=band_font)
            x = (paper_width - (bounds[2] - bounds[0])) / 2
            y = subtitle_band_y + (subtitle_band_h - band_font.size) // 2 - 2
            draw.text((x, y), args.subtitle, font=band_font, fill=band_text)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    base = args.basename or args.poster.stem
    if args.mask_preview:
        upper_mask.save(args.output_dir / f"{base}-upper-mask.png")
    output = args.output_dir / f"{base}-processed.png"
    canvas.save(output)
    print(f"upper authored-image occupancy: {upper_occupancy:.1%}", file=sys.stderr)
    print(output.resolve())


if __name__ == "__main__":
    main()
