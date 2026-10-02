"""Make the link-preview image shown when the site is shared (LinkedIn, Slack, etc.).

Writes assets/media/sharing.jpg (1200 x 630), which the theme uses as og:image for
pages without their own featured image or avatar.

Usage:  python3 tools/make_sharing_image.py
Requires Pillow and the CMU Sans Serif fonts (cmunsx.ttf, cmunss.ttf) installed.
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFont

ROOT = Path(__file__).resolve().parent.parent
MEDIA = ROOT / "assets" / "media"
W, H = 1200, 630


def font(name, size):
    for folder in (Path.home() / "Library" / "Fonts", Path("/Library/Fonts")):
        if (folder / name).exists():
            return ImageFont.truetype(str(folder / name), size)
    raise SystemExit(f"Font {name} not found; install CMU Sans Serif.")


# Background: the home slider's research illustration, cropped to 1200x630 and dimmed.
bg = Image.open(MEDIA / "research-background.jpg").convert("RGB")
scale = max(W / bg.width, H / bg.height)
bg = bg.resize((round(bg.width * scale), round(bg.height * scale)), Image.LANCZOS)
left, top = (bg.width - W) // 2, (bg.height - H) // 2
bg = bg.crop((left, top, left + W, top + H))
bg = ImageEnhance.Brightness(bg).enhance(0.45)

# Logo, centred in the upper part.
logo = Image.open(MEDIA / "logo_orange.png").convert("RGBA")
logo = logo.crop(logo.getbbox())
logo_w = 620
logo = logo.resize((logo_w, round(logo.height * logo_w / logo.width)), Image.LANCZOS)
bg.paste(logo, ((W - logo_w) // 2, 150), logo)

draw = ImageDraw.Draw(bg)
y = 150 + logo.height + 45
draw.text((W / 2, y), "Learning and Optimisation Of Process Systems",
          font=font("cmunsx.ttf", 46), fill="white", anchor="ma")
draw.text((W / 2, y + 68), "UCL Department of Chemical Engineering",
          font=font("cmunss.ttf", 34), fill=(220, 220, 230), anchor="ma")

bg.save(MEDIA / "sharing.jpg", quality=90, optimize=True)
print("wrote", MEDIA / "sharing.jpg")
