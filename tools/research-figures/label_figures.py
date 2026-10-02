"""Add text labels to the Research page figures.

Reads the unlabelled illustrations in sources/, draws the labels below,
trims the white margins and writes static/media/topic_1.png ... topic_3.png.

Usage (from anywhere):  python3 tools/research-figures/label_figures.py
Requires Pillow and the CMU Sans Serif Bold font (cmunsx.ttf) installed.
"""
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
SOURCES = HERE / "sources"
OUT = HERE.parent.parent / "static" / "media"

FONT_FILE = "cmunsx.ttf"  # CMU Sans Serif Bold, the site's font
FONT_SIZE = 68
INK = (45, 32, 80)  # dark indigo used in the figures (#2d2050)
PAD = 400  # room around the source image for labels outside it
MARGIN = 70  # white space kept around the content after trimming
MAX_SIZE = 1600  # longest side of the published image

# (text, x, y, anchor) in source-image pixels (2000 x 2000).
# anchor: "c" centred on x, "l" starts at x, "r" ends at x; y is the top of the text.
# Use "\n" for a line break. Labels may sit outside the source image.
FIGS = {
    "topic_1": [
        ("Process knowledge", 340, 215, "c"),
        ("Physics-informed ML", 965, 1265, "c"),
        ("Reinforcement learning", 1565, 215, "c"),
        ("Gaussian processes\n& uncertainty", 518, 1790, "c"),
        ("Bayesian optimisation", 1426, 1790, "c"),
    ],
    "topic_2": [
        ("Model predictive control", 770, 300, "c"),
        ("Process +\ndigital twin", 780, 1290, "c"),
        ("Monitoring &\nsetpoint tracking", 1400, 1185, "l"),
        ("Real-time\noptimisation", 1545, 680, "c"),
        ("State estimation\n& uncertainty", 245, 1228, "r"),
    ],
    "topic_3": [
        ("Scientific literature", 966, 250, "c"),
        ("AI hypothesis\ngeneration", 966, 655, "c"),
        ("Optimal\nexperimental design", 1700, 960, "l"),
        ("Automated experiments", 966, 1735, "c"),
        ("Data analysis\n& learning", 295, 960, "r"),
        ("Sustainable materials\ndiscovery", 966, 1290, "c"),
    ],
}


def find_font():
    for folder in (Path.home() / "Library" / "Fonts", Path("/Library/Fonts")):
        if (folder / FONT_FILE).exists():
            return ImageFont.truetype(str(folder / FONT_FILE), FONT_SIZE)
    raise SystemExit(f"Font {FONT_FILE} not found; install CMU Sans Serif.")


def main():
    font = find_font()
    for name, labels in FIGS.items():
        im = Image.open(SOURCES / f"{name}.webp").convert("RGB")
        canvas = Image.new("RGB", (im.width + 2 * PAD, im.height + 2 * PAD), "white")
        canvas.paste(im, (PAD, PAD))
        draw = ImageDraw.Draw(canvas)
        for text, x, y, a in labels:
            draw.multiline_text(
                (x + PAD, y + PAD), text, font=font, fill=INK,
                anchor={"c": "ma", "l": "la", "r": "ra"}[a],
                align={"c": "center", "l": "left", "r": "right"}[a],
                spacing=10,
            )
        # Trim to the content (anything noticeably off-white) plus a margin.
        diff = ImageChops.difference(canvas, Image.new("RGB", canvas.size, "white"))
        left, top, right, bottom = diff.convert("L").point(lambda v: 255 if v > 12 else 0).getbbox()
        canvas = canvas.crop((max(left - MARGIN, 0), max(top - MARGIN, 0),
                              min(right + MARGIN, canvas.width), min(bottom + MARGIN, canvas.height)))
        canvas.thumbnail((MAX_SIZE, MAX_SIZE), Image.LANCZOS)
        canvas.save(OUT / f"{name}.png", optimize=True)
        print(f"{name}.png  {canvas.size[0]}x{canvas.size[1]}")


if __name__ == "__main__":
    main()
