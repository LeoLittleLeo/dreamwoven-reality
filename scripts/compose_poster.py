#!/usr/bin/env python3
"""Compose the single processed 53/2/43/2 editorial artwork."""

from __future__ import annotations

import argparse
import colorsys
import math
import platform
import sys
from collections import deque
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont, ImageOps, ImageStat


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
POSITIONS = ("top-left", "top-right", "bottom-left", "bottom-right")
POSTCARD_PROFILES = {
    "landscape": {"ratio": 3 / 2, "image_fraction": 0.74, "stamp_width_fraction": 0.20},
    "portrait": {"ratio": 2 / 3, "image_fraction": 0.68, "stamp_width_fraction": 0.30},
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


def cover(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    return ImageOps.fit(image, size, method=Image.Resampling.LANCZOS, centering=(0.5, 0.5))


def contain(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    copy = image.copy()
    copy.thumbnail(size, Image.Resampling.LANCZOS)
    return copy


def source_orientation(image: Image.Image) -> str:
    ratio = image.width / image.height
    if 0.90 <= ratio <= 1.10:
        return "near-square"
    return "landscape" if ratio > 1 else "portrait"


def fit_source_contain(image: Image.Image, size: tuple[int, int], ground: tuple[int, int, int]) -> Image.Image:
    """Proportionally contain the complete source without independent x/y scaling."""
    fitted = contain(image.convert("RGB"), size)
    layer = Image.new("RGB", size, ground)
    layer.paste(fitted, ((size[0] - fitted.width) // 2, (size[1] - fitted.height) // 2))
    return layer


def fit_source_cover(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    """Proportionally cover the complete target, allowing centered cropping without distortion."""
    return cover(image.convert("RGB"), size)


def source_derived_canvas(
    original: Image.Image,
    mode: str,
    width_cap: int | None,
    height_cap: int | None,
    export_long_edge: int | None,
) -> tuple[int, int, str]:
    """Derive composition geometry from the source; explicit sizes are export caps only."""
    orientation = source_orientation(original)
    if mode == "fullbleed":
        raw_width, raw_height = original.size
    else:
        # Choose postcard direction from the user's image, then use the familiar
        # 3:2 / 2:3 postcard geometry instead of extending the source into a long poster.
        postcard_orientation = "landscape" if original.width >= original.height else "portrait"
        ratio = POSTCARD_PROFILES[postcard_orientation]["ratio"]
        if postcard_orientation == "landscape":
            raw_width = original.width
            raw_height = round(raw_width / ratio)
        else:
            raw_height = original.height
            raw_width = round(raw_height * ratio)
        orientation = postcard_orientation

    limits = [1.0]
    if width_cap:
        limits.append(width_cap / raw_width)
    if height_cap:
        limits.append(height_cap / raw_height)
    if export_long_edge:
        limits.append(export_long_edge / max(raw_width, raw_height))
    scale = min(limits)
    return max(1, round(raw_width * scale)), max(1, round(raw_height * scale)), orientation


ROBOT_DREAMS_BOARD_BASES = {
    "warm-ivory": (239, 228, 207),
    "dusty-peach": (232, 207, 196),
    "powder-blue": (205, 220, 229),
    "soft-lilac": (220, 211, 228),
    "mineral-sage": (210, 220, 204),
}


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
        r, g, b = (channel / 255 for channel in color)
        hue, saturation, value = colorsys.rgb_to_hsv(r, g, b)
        mean_luminance += weight * value
        if saturation < 0.12:
            hue_weights["neutral"] += weight
        elif hue < 0.12 or hue >= 0.91:
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
    # Retain a restrained source echo without allowing the board to become noisy.
    return tuple(round(base[i] * 0.88 + source_mean[i] * 0.12) for i in range(3))  # type: ignore[return-value]


def luminance(color: tuple[int, int, int]) -> float:
    return color[0] * 0.2126 + color[1] * 0.7152 + color[2] * 0.0722


def text_palette(ground: tuple[int, int, int]):
    warm = ground[0] >= ground[2]
    return ((55, 52, 47), (91, 84, 74), (130, 101, 79)) if warm else ((45, 52, 60), (74, 84, 95), (91, 111, 130))


def tracked_width(font: ImageFont.FreeTypeFont, text: str, tracking: int = 0) -> float:
    return sum(font.getlength(char) for char in text) + max(0, len(text) - 1) * tracking


def split_units(text: str) -> list[str]:
    """Use words for spaced text and characters for CJK-like unspaced text."""
    return text.split() if " " in text.strip() else list(text.strip())


def wrap_text(text: str, font: ImageFont.FreeTypeFont, max_width: int, tracking: int, max_lines: int) -> list[str] | None:
    if not text:
        return []
    units = split_units(text)
    separator = " " if " " in text.strip() else ""
    lines: list[str] = []
    current = ""
    for unit in units:
        candidate = unit if not current else current + separator + unit
        if tracked_width(font, candidate, tracking) <= max_width:
            current = candidate
        else:
            if not current:
                return None
            lines.append(current)
            current = unit
    if current:
        lines.append(current)
    return lines if len(lines) <= max_lines else None


def fit_wrapped(font_path: Path, text: str, max_width: int, start_size: int, max_lines: int, tracking: int = 0):
    for size in range(max(12, start_size), 11, -2):
        font = ImageFont.truetype(str(font_path), size)
        lines = wrap_text(text, font, max_width, tracking, max_lines)
        if lines is not None:
            return font, lines
    font = ImageFont.truetype(str(font_path), 12)
    return font, wrap_text(text, font, max_width, tracking, max_lines) or [text]


def fit_processed_band_font(font_path: Path, texts: tuple[str, ...], max_width: int, start_size: int):
    """Return one shared font size that fits every non-empty processed-band line."""
    active = tuple(text for text in texts if text)
    for size in range(max(12, start_size), 11, -2):
        font = ImageFont.truetype(str(font_path), size)
        if all(font.getlength(text) <= max_width for text in active):
            return font
    return ImageFont.truetype(str(font_path), 12)


def draw_tracked_text(draw, position, text, font, fill, tracking=0):
    x, y = position
    cursor = float(x)
    for character in text:
        draw.text((round(cursor), y), character, font=font, fill=fill)
        cursor += font.getlength(character) + tracking
    box = font.getbbox(text or " ")
    return (x, y, round(cursor - tracking), y + box[3] - box[1])


def draw_lines(draw, x, y, lines, font, fill, tracking, line_gap):
    bottom = y
    for line in lines:
        box = draw_tracked_text(draw, (x, bottom), line, font, fill, tracking)
        bottom = box[3] + line_gap
    return bottom - line_gap


def position_box(canvas_size, position, margin, box_w, box_h):
    width, height = canvas_size
    x = margin if position.endswith("left") else width - margin - box_w
    y = margin if position.startswith("top") else height - margin - box_h
    return (x, y, x + box_w, y + box_h)


def quietness(image: Image.Image, box: tuple[int, int, int, int]) -> float:
    crop = image.convert("L").crop(box).resize((64, 64), Image.Resampling.BILINEAR)
    edges = crop.filter(ImageFilter.FIND_EDGES)
    return ImageStat.Stat(crop).var[0] + ImageStat.Stat(edges).mean[0] * 14


def choose_position(image: Image.Image, requested: str, margin: int, box_w: int, box_h: int):
    if requested != "auto":
        return requested
    candidates = [(quietness(image, position_box(image.size, p, margin, box_w, box_h)), p) for p in POSITIONS]
    return min(candidates)[1]


def flood_connected_background(candidate: Image.Image) -> Image.Image:
    """Keep only background candidates connected to an image edge."""
    width, height = candidate.size
    src = candidate.load()
    result = Image.new("L", candidate.size, 0)
    dst = result.load()
    queue: deque[tuple[int, int]] = deque()
    for x in range(width):
        queue.extend(((x, 0), (x, height - 1)))
    for y in range(height):
        queue.extend(((0, y), (width - 1, y)))
    while queue:
        x, y = queue.popleft()
        if dst[x, y] or src[x, y] == 0:
            continue
        dst[x, y] = 255
        if x:
            queue.append((x - 1, y))
        if x + 1 < width:
            queue.append((x + 1, y))
        if y:
            queue.append((x, y - 1))
        if y + 1 < height:
            queue.append((x, y + 1))
    return result


def edge_key_mask(art: Image.Image, feather: int) -> Image.Image:
    corner = max(4, min(art.width, art.height) // 18)
    samples = [art.crop((0, 0, corner, corner)), art.crop((art.width - corner, 0, art.width, corner)), art.crop((0, art.height - corner, corner, art.height)), art.crop((art.width - corner, art.height - corner, art.width, art.height))]
    means = [ImageStat.Stat(sample).mean for sample in samples]
    paper = tuple(sum(mean[c] for mean in means) / len(means) for c in range(3))
    candidate = Image.new("L", art.size, 0)
    pixels, marks = art.load(), candidate.load()
    for y in range(art.height):
        for x in range(art.width):
            distance = sum((pixels[x, y][c] - paper[c]) ** 2 for c in range(3)) ** 0.5
            marks[x, y] = 255 if distance < 54 else 0
    connected = flood_connected_background(candidate)
    foreground = ImageChops.invert(connected)
    return foreground.filter(ImageFilter.GaussianBlur(max(0.8, feather / 10)))


def artwork_layer(artwork: Image.Image, size, removal: str, mask_path: Path | None, feather: int):
    if removal == "alpha" and artwork.mode in ("RGBA", "LA"):
        source = artwork.convert("RGBA")
        source_alpha = source.getchannel("A")
        bbox = source_alpha.getbbox()
        if bbox:
            source = source.crop(bbox)
            source_alpha = source_alpha.crop(bbox)
        art = contain(source, size)
        alpha = contain(source_alpha, art.size)
        return art.convert("RGB"), alpha
    art = contain(artwork.convert("RGBA"), size)
    if removal == "mask":
        if not mask_path or not mask_path.is_file():
            raise FileNotFoundError("--background-removal mask requires --art-mask")
        source_mask = Image.open(mask_path).convert("L")
        bbox = source_mask.getbbox()
        if bbox:
            source = artwork.convert("RGBA").crop(bbox)
            source_mask = source_mask.crop(bbox)
            art = contain(source, size)
        return art.convert("RGB"), contain(source_mask, art.size)
    if removal == "none" or (removal == "alpha" and artwork.mode not in ("RGBA", "LA")):
        return art.convert("RGB"), Image.new("L", art.size, 255)
    return art.convert("RGB"), edge_key_mask(art.convert("RGB"), feather)


def fit_upper_authored_image(
    artwork: Image.Image,
    board_size: tuple[int, int],
    target_occupancy: float = 0.80,
) -> tuple[Image.Image, Image.Image, float]:
    """Fit an RGBA authored image by visible alpha area, preserving its free contour."""
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


def build_copy(font_path, title, subtitle, date_text, max_width, scale, max_title_lines):
    title_font, title_lines = fit_wrapped(font_path, title, max_width, round(scale * 0.052), max_title_lines)
    subtitle_font, subtitle_lines = fit_wrapped(font_path, subtitle, max_width, round(scale * 0.020), 3, max(0, round(scale / 900)))
    date_font = ImageFont.truetype(str(font_path), max(12, round(scale * 0.014)))
    title_gap = max(3, round(title_font.size * 0.22))
    subtitle_gap = max(2, round(subtitle_font.size * 0.28))
    height = len(title_lines) * (title_font.size + title_gap) + len(subtitle_lines) * (subtitle_font.size + subtitle_gap)
    if title_lines and (subtitle_lines or date_text):
        height += round(scale * 0.020)
    if subtitle_lines and date_text:
        height += round(scale * 0.018)
    if date_text:
        height += date_font.size * 2
    return title_font, title_lines, subtitle_font, subtitle_lines, date_font, max(height, 1)


def draw_copy(draw, x, y, copy, palette, scale, date_text, rule_color=None):
    title_font, title_lines, subtitle_font, subtitle_lines, date_font, _ = copy
    title_color, subtitle_color, date_color = palette
    if title_lines:
        y = draw_lines(draw, x, y, title_lines, title_font, title_color, 0, max(3, round(title_font.size * 0.22))) + round(scale * 0.020)
    if subtitle_lines:
        y = draw_lines(draw, x, y, subtitle_lines, subtitle_font, subtitle_color, max(0, round(scale / 900)), max(2, round(subtitle_font.size * 0.28))) + round(scale * 0.018)
    if date_text:
        if rule_color:
            draw.line((x, y, x + round(scale * 0.22), y), fill=rule_color, width=max(1, round(scale / 900)))
            y += round(scale * 0.014)
        cell = max(date_font.size + round(scale * 0.010), round(scale * 0.025))
        gap = max(3, round(scale * 0.004))
        stroke = max(1, round(scale / 1200))
        for index, character in enumerate(date_text):
            left = x + index * (cell + gap)
            draw.rectangle((left, y, left + cell, y + cell), outline=date_color, width=stroke)
            bounds = draw.textbbox((0, 0), character, font=date_font)
            tw, th = bounds[2] - bounds[0], bounds[3] - bounds[1]
            draw.text((left + (cell - tw) / 2, y + (cell - th) / 2 - bounds[1]), character, font=date_font, fill=date_color)


def make_stamp(artwork: Image.Image, width: int, border: int) -> Image.Image:
    """Build a small bordered abstract-art sticker with a quiet postcard shadow."""
    ratio = artwork.width / max(1, artwork.height)
    art_w = max(1, width - border * 2)
    art_h = max(1, round(art_w / ratio))
    art = fit_source_cover(artwork, (art_w, art_h))
    stamp = Image.new("RGBA", (width, art_h + border * 2), (248, 244, 234, 255))
    stamp.paste(art, (border, border))
    outline = ImageDraw.Draw(stamp)
    outline.rectangle((0, 0, stamp.width - 1, stamp.height - 1), outline=(116, 105, 91, 210), width=max(1, border // 5))
    return stamp


def draw_postmark(draw: ImageDraw.ImageDraw, stamp_x: int, stamp_y: int, stamp_w: int, scale: int, ink) -> None:
    """Draw a quiet text-free cancellation mark partly behind the sticker."""
    radius = max(24, round(stamp_w * 0.28))
    center_x = stamp_x - round(radius * 0.18)
    center_y = stamp_y + round(radius * 0.92)
    stroke = max(1, round(scale / 1300))
    draw.ellipse(
        (center_x - radius, center_y - radius, center_x + radius, center_y + radius),
        outline=ink,
        width=stroke,
    )
    inner = round(radius * 0.76)
    draw.ellipse(
        (center_x - inner, center_y - inner, center_x + inner, center_y + inner),
        outline=ink,
        width=stroke,
    )
    wave_start = center_x - round(radius * 1.45)
    wave_end = center_x - round(radius * 0.42)
    amplitude = max(3, round(radius * 0.08))
    for row in range(3):
        baseline = center_y - round(radius * 0.28) + row * round(radius * 0.28)
        points = []
        segments = 18
        for step in range(segments + 1):
            px = wave_start + (wave_end - wave_start) * step / segments
            py = baseline + math.sin(step * math.pi / 3) * amplitude
            points.append((round(px), round(py)))
        draw.line(points, fill=ink, width=stroke)


def draw_board_motif(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], motif: str, base, scale: int) -> None:
    """Draw one source-semantic family as broad colored board fields, not line decoration."""
    x0, y0, x1, y1 = box
    width, height = x1 - x0, y1 - y0
    color_a = tuple(max(0, channel - 18) for channel in base)
    color_b = tuple(max(0, channel - 32) for channel in base)
    color_c = tuple(min(255, max(0, channel - 8 + (7 if index == 1 else 0))) for index, channel in enumerate(base))
    if motif == "waves":
        for layer, (baseline_fraction, amplitude_fraction, fill) in enumerate(((0.64, 0.050, color_c), (0.76, 0.065, color_a), (0.88, 0.040, color_b))):
            crest = []
            for step in range(65):
                px = x0 + width * step / 64
                phase = step * math.pi / (5.2 - layer * 0.5) + layer * 0.9
                py = y0 + height * baseline_fraction + math.sin(phase) * height * amplitude_fraction
                crest.append((round(px), round(py)))
            draw.polygon(crest + [(x1, y1), (x0, y1)], fill=fill)
    elif motif == "mountains":
        points = [(x0, y0 + round(height * 0.72)), (x0 + round(width * 0.18), y0 + round(height * 0.46)),
                  (x0 + round(width * 0.31), y0 + round(height * 0.62)), (x0 + round(width * 0.52), y0 + round(height * 0.28)),
                  (x0 + round(width * 0.70), y0 + round(height * 0.60)), (x1, y0 + round(height * 0.38)), (x1, y1), (x0, y1)]
        draw.polygon(points, fill=color_a)
    elif motif == "city":
        baseline = y0 + round(height * 0.72)
        points = [(x0, baseline), (x0 + round(width * 0.12), baseline), (x0 + round(width * 0.12), y0 + round(height * 0.46)),
                  (x0 + round(width * 0.23), y0 + round(height * 0.46)), (x0 + round(width * 0.23), y0 + round(height * 0.30)),
                  (x0 + round(width * 0.34), y0 + round(height * 0.30)), (x0 + round(width * 0.34), y0 + round(height * 0.56)),
                  (x0 + round(width * 0.50), y0 + round(height * 0.56)), (x0 + round(width * 0.50), y0 + round(height * 0.38)),
                  (x0 + round(width * 0.64), y0 + round(height * 0.38)), (x0 + round(width * 0.64), baseline), (x1, baseline), (x1, y1), (x0, y1)]
        draw.polygon(points, fill=color_a)
    elif motif == "foliage":
        for index, fraction in enumerate((0.10, 0.30, 0.53, 0.76, 0.94)):
            cx = x0 + round(width * fraction)
            cy = y0 + round(height * (0.80 - fraction * 0.28))
            leaf_w, leaf_h = round(width * 0.16), round(height * 0.23)
            draw.ellipse((cx - leaf_w, cy - leaf_h, cx + leaf_w, cy + leaf_h), fill=color_a if index % 2 else color_c)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("processed",), default="processed")
    parser.add_argument("--original", required=True, type=Path)
    parser.add_argument("--upper-poster", type=Path, help="photographic-led partial abstraction; required for processed mode")
    parser.add_argument("--poster", required=True, type=Path, help="strong lower abstraction without final typography")
    parser.add_argument("--title", default="")
    parser.add_argument("--subtitle", default="")
    parser.add_argument("--copy-free", action="store_true", help="processed mode: explicitly omit postcard copy and date")
    parser.add_argument("--single-text-level", choices=("title", "subtitle"), help="processed mode: explicitly use only the selected text level")
    parser.add_argument("--date", dest="date_text", default=None, help="optional reliable capture date or user-supplied postcard date")
    parser.add_argument("--no-date", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("--text-position", choices=("auto", "lower-left", "bottom-centered", "source-aware-quiet-zone") + POSITIONS, default="auto")
    parser.add_argument("--max-title-lines", type=int, default=3)
    parser.add_argument("--background-removal", choices=("alpha", "edge-key", "none", "mask"), default="alpha")
    parser.add_argument("--art-mask", type=Path)
    parser.add_argument("--mask-preview", action="store_true")
    parser.add_argument("--output-dir", type=Path, default=Path("outputs"))
    parser.add_argument("--basename", default=None)
    parser.add_argument("--font", type=Path)
    parser.add_argument("--background-color", type=parse_color)
    parser.add_argument("--board-motif", choices=("none", "waves", "mountains", "city", "foliage"), default="none",
                        help="quiet source-semantic line motif for the processed message field")
    parser.add_argument("--text-color", type=parse_color, help="override editorial copy color for contrast")
    parser.add_argument("--width", type=int, default=None, help="optional export width cap; never changes composition ratio")
    parser.add_argument("--height", type=int, default=None, help="optional export height cap; never changes composition ratio")
    parser.add_argument("--export-long-edge", type=int, default=3000, help="maximum output long edge; use 0 to disable the cap")
    parser.add_argument("--paper-orientation", choices=("auto", "portrait", "landscape"), default="auto", help="legacy export hint; source orientation remains authoritative")
    args = parser.parse_args()

    required_paths = [args.original, args.poster]
    if not args.upper_poster:
        parser.error("processed mode requires --upper-poster")
    required_paths.append(args.upper_poster)
    if args.text_position != "auto":
        parser.error("processed mode uses fixed centered title and subtitle bands")
    if args.date_text:
        parser.error("processed mode has no date field")
    if args.copy_free and (args.title or args.subtitle or args.single_text_level):
        parser.error("--copy-free cannot be combined with title, subtitle, or --single-text-level")
    if args.single_text_level == "title" and (not args.title or args.subtitle):
        parser.error("--single-text-level title requires --title and prohibits --subtitle")
    if args.single_text_level == "subtitle" and (not args.subtitle or args.title):
        parser.error("--single-text-level subtitle requires --subtitle and prohibits --title")
    if Image.open(args.upper_poster).mode not in ("RGBA", "LA"):
        parser.error("processed mode requires --upper-poster with an authored alpha contour")
    for path in required_paths:
        if not path.is_file():
            parser.error(f"image not found: {path}")
    if any(value is not None and value <= 0 for value in (args.width, args.height)) or args.export_long_edge < 0 or args.max_title_lines <= 0:
        parser.error("width/height caps and --max-title-lines must be positive; --export-long-edge may be 0 to disable")

    original_source = Image.open(args.original)
    upper_artwork_source = Image.open(args.upper_poster) if args.upper_poster else None
    artwork_source = Image.open(args.poster)
    original = original_source.convert("RGB")
    artwork = artwork_source.convert("RGB")
    date_text = "" if args.no_date else (args.date_text or "")
    has_copy = bool(args.title or args.subtitle or date_text)
    font_path = find_font(args.font) if has_copy else None
    args.output_dir.mkdir(parents=True, exist_ok=True)
    base = args.basename or args.poster.stem
    orientation = source_orientation(original)
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

    assert upper_artwork_source is not None
    ground = args.background_color or derive_ground(original)
    canvas = Image.new("RGB", (paper_width, paper_height), ground)
    draw = ImageDraw.Draw(canvas)
    upper_h = round(paper_height * 0.53)
    band_h = max(1, round(paper_height * 0.02))
    lower_h = round(paper_height * 0.43)
    upper_h += paper_height - upper_h - lower_h - band_h * 2

    upper_art, upper_mask, upper_occupancy = fit_upper_authored_image(upper_artwork_source, (paper_width, upper_h))
    if not 0.75 <= upper_occupancy <= 0.85:
        parser.error(
            f"upper authored image occupies {upper_occupancy:.1%} of its 53% board; "
            "provide a free-edged RGBA artwork that reaches 75%-85% without clipping or distortion"
        )
    upper_x = (paper_width - upper_art.width) // 2
    upper_y = (upper_h - upper_art.height) // 2
    canvas.paste(upper_art, (upper_x, upper_y), upper_mask)

    title_band_y = upper_h
    lower_y = title_band_y + band_h
    lower = fit_source_cover(artwork_source.convert("RGB"), (paper_width, lower_h))
    canvas.paste(lower, (0, lower_y))
    subtitle_band_y = lower_y + lower_h
    black_ink = (28, 28, 28)
    band_text = args.text_color or (244, 239, 226)
    draw.rectangle((0, title_band_y, paper_width, title_band_y + band_h), fill=black_ink)
    draw.rectangle((0, subtitle_band_y, paper_width, subtitle_band_y + band_h), fill=black_ink)
    if has_copy and font_path:
        band_font = fit_processed_band_font(font_path, (args.title, args.subtitle), round(paper_width * 0.82), max(10, round(band_h * 0.52)))
        if args.title:
            bounds = draw.textbbox((0, 0), args.title, font=band_font)
            draw.text(((paper_width - (bounds[2] - bounds[0])) / 2, title_band_y + (band_h - band_font.size) // 2 - 2), args.title, font=band_font, fill=band_text)
        if args.subtitle:
            bounds = draw.textbbox((0, 0), args.subtitle, font=band_font)
            draw.text(((paper_width - (bounds[2] - bounds[0])) / 2, subtitle_band_y + (band_h - band_font.size) // 2 - 2), args.subtitle, font=band_font, fill=band_text)
    if args.mask_preview:
        upper_mask.save(args.output_dir / f"{base}-upper-mask.png")
    output = args.output_dir / f"{base}-processed.png"
    canvas.save(output)
    print(f"upper authored-image occupancy: {upper_occupancy:.1%}", file=sys.stderr)
    print(output.resolve())


if __name__ == "__main__":
    main()
