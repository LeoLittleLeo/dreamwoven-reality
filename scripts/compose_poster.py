#!/usr/bin/env python3
"""Compose an adaptive two-generated-stage poster or full-bleed interpretation."""

from __future__ import annotations

import argparse
import platform
from collections import deque
from datetime import date
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
ORIENTATION_PROFILES = {
    "landscape": {"panel_fraction": 0.44, "band_fraction": 0.04},
    "portrait": {"panel_fraction": 0.44, "band_fraction": 0.04},
    "near-square": {"panel_fraction": 0.44, "band_fraction": 0.04},
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
        photo_fraction = ORIENTATION_PROFILES[orientation]["panel_fraction"]
        raw_width = original.width
        raw_height = round(original.height / photo_fraction)

    limits = [1.0]
    if width_cap:
        limits.append(width_cap / raw_width)
    if height_cap:
        limits.append(height_cap / raw_height)
    if export_long_edge:
        limits.append(export_long_edge / max(raw_width, raw_height))
    scale = min(limits)
    return max(1, round(raw_width * scale)), max(1, round(raw_height * scale)), orientation


def derive_ground(image: Image.Image) -> tuple[int, int, int]:
    sample = ImageOps.fit(image.convert("RGB"), (64, 64), method=Image.Resampling.BILINEAR)
    return tuple(round(channel * 0.24 + 236 * 0.76) for channel in ImageStat.Stat(sample).mean)  # type: ignore[return-value]


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
        draw_tracked_text(draw, (x, y), date_text, date_font, date_color, max(0, round(scale / 800)))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("processed", "fullbleed"), default="processed")
    parser.add_argument("--original", required=True, type=Path)
    parser.add_argument("--upper-poster", type=Path, help="photographic-led partial abstraction; required for processed mode")
    parser.add_argument("--poster", required=True, type=Path, help="strong lower abstraction without final typography")
    parser.add_argument("--title", default="")
    parser.add_argument("--subtitle", default="")
    parser.add_argument("--date", dest="date_text", default=None, help="explicit date text; processed mode defaults to today's date")
    parser.add_argument("--no-date", action="store_true")
    parser.add_argument("--text-position", choices=("auto", "lower-left", "bottom-centered", "source-aware-quiet-zone") + POSITIONS, default="auto")
    parser.add_argument("--max-title-lines", type=int, default=3)
    parser.add_argument("--background-removal", choices=("alpha", "edge-key", "none", "mask"), default="alpha")
    parser.add_argument("--art-mask", type=Path)
    parser.add_argument("--mask-preview", action="store_true")
    parser.add_argument("--output-dir", type=Path, default=Path("outputs"))
    parser.add_argument("--basename", default=None)
    parser.add_argument("--font", type=Path)
    parser.add_argument("--background-color", type=parse_color)
    parser.add_argument("--text-color", type=parse_color, help="override editorial copy color for contrast")
    parser.add_argument("--width", type=int, default=None, help="optional export width cap; never changes composition ratio")
    parser.add_argument("--height", type=int, default=None, help="optional export height cap; never changes composition ratio")
    parser.add_argument("--export-long-edge", type=int, default=3000, help="maximum output long edge; use 0 to disable the cap")
    parser.add_argument("--paper-orientation", choices=("auto", "portrait", "landscape"), default="auto", help="legacy export hint; source orientation remains authoritative")
    args = parser.parse_args()

    required_paths = [args.original, args.poster]
    if args.mode == "processed":
        if not args.upper_poster:
            parser.error("processed mode requires --upper-poster")
        if Image.open(args.upper_poster).mode not in ("RGBA", "LA"):
            parser.error("processed mode requires --upper-poster with an alpha channel for the non-rectangular upper panel")
        required_paths.append(args.upper_poster)
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
    date_text = "" if args.no_date else (args.date_text or (date.today().strftime("%Y.%m.%d") if args.mode == "processed" else ""))
    has_copy = bool(args.title or args.subtitle or date_text)
    font_path = find_font(args.font) if has_copy else None
    args.output_dir.mkdir(parents=True, exist_ok=True)
    base = args.basename or args.poster.stem
    canvas_width, canvas_height, orientation = source_derived_canvas(
        original, args.mode, args.width, args.height, args.export_long_edge or None
    )

    if args.mode == "fullbleed":
        ground = args.background_color or derive_ground(original)
        canvas = fit_source_contain(artwork, (canvas_width, canvas_height), ground)
        if has_copy and font_path:
            margin = round(min(canvas.size) * 0.045)
            copy_w = round(canvas.width * 0.34)
            copy = build_copy(font_path, args.title, args.subtitle, date_text, copy_w, round(canvas.width * 0.62), args.max_title_lines)
            box_h = min(copy[-1], canvas.height - margin * 2)
            position = choose_position(canvas, args.text_position, margin, copy_w, box_h)
            box = position_box(canvas.size, position, margin, copy_w, box_h)
            draw_copy(ImageDraw.Draw(canvas), box[0], box[1], copy, text_palette(derive_ground(canvas)), canvas.width, date_text)
        output = args.output_dir / f"{base}-processed.png"
        canvas.save(output)
        print(output.resolve())
        return

    if args.mode == "processed":
        assert upper_artwork_source is not None
        paper_width, paper_height = canvas_width, canvas_height
        ground = args.background_color or derive_ground(original)
        canvas = Image.new("RGB", (paper_width, paper_height), ground)
        draw = ImageDraw.Draw(canvas)

        profile = ORIENTATION_PROFILES[orientation]
        panel_h = round(paper_height * profile["panel_fraction"])
        band_h = max(1, round(paper_height * profile["band_fraction"]))
        upper_h = panel_h
        lower_h = panel_h
        title_band_h = band_h
        subtitle_band_h = band_h
        date_band_h = paper_height - upper_h - lower_h - title_band_h - subtitle_band_h
        if date_band_h <= 0:
            parser.error("source-derived canvas leaves no room for the fixed five-band layout")

        # The upper artwork must carry an authored alpha contour; the lower panel is
        # always a complete rectangle.
        upper_box = (paper_width, upper_h)
        upper_art, upper_mask = artwork_layer(upper_artwork_source, upper_box, "alpha", None, max(8, paper_width // 110))
        upper_x = (paper_width - upper_art.width) // 2
        upper_y = date_band_h
        canvas.paste(upper_art, (upper_x, upper_y), upper_mask)

        title_y = date_band_h + upper_h
        lower_y = title_y + title_band_h
        lower_art = fit_source_contain(artwork_source.convert("RGB"), (paper_width, lower_h), ground)
        canvas.paste(lower_art, (0, lower_y))

        subtitle_y = lower_y + lower_h
        black = (28, 28, 28)
        canvas.paste(Image.new("RGB", (paper_width, title_band_h), black), (0, title_y))
        canvas.paste(Image.new("RGB", (paper_width, subtitle_band_h), black), (0, subtitle_y))
        # The date strip is a dedicated warm-white editorial band, independent
        # of the source-derived paper ground used around the authored upper edge.
        date_band_color = (246, 238, 220)
        canvas.paste(Image.new("RGB", (paper_width, date_band_h), date_band_color), (0, 0))

        if args.mask_preview:
            upper_mask.save(args.output_dir / f"{base}-upper-mask.png")
        if has_copy and font_path:
            ink = args.text_color or (244, 239, 226)
            dark = args.text_color or (44, 42, 38)
            title_font, title_lines = fit_wrapped(font_path, args.title, round(paper_width * 0.82), max(12, round(title_band_h * 0.58)), args.max_title_lines)
            subtitle_font, subtitle_lines = fit_wrapped(font_path, args.subtitle, round(paper_width * 0.82), max(12, round(subtitle_band_h * 0.42)), 2)
            date_font = ImageFont.truetype(str(font_path), max(12, round(date_band_h * 0.44)))

            def centered(draw_obj, text_value, font_obj, y, fill):
                bbox = draw_obj.textbbox((0, 0), text_value, font=font_obj)
                x = (paper_width - (bbox[2] - bbox[0])) // 2
                draw_obj.text((x, y), text_value, font=font_obj, fill=fill)

            if date_text:
                centered(draw, date_text, date_font, max(1, (date_band_h - date_font.size) // 2 - 2), dark)
            if args.title:
                line = title_lines[0] if title_lines else args.title
                centered(draw, line, title_font, max(1, title_y + (title_band_h - title_font.size) // 2 - 3), ink)
            if args.subtitle:
                line = subtitle_lines[0] if subtitle_lines else args.subtitle
                centered(draw, line, subtitle_font, max(1, subtitle_y + (subtitle_band_h - subtitle_font.size) // 2 - 2), ink)
        output = args.output_dir / f"{base}-processed.png"
        canvas.save(output)
        print(output.resolve())
        return

    parser.error("unsupported mode")


if __name__ == "__main__":
    main()
