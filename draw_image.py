"""Draw the front-page image for 22 November 2026.

Renders a 1024x1024 newspaper front page with PIL and saves it as
entry.png next to this script. Run: python3 draw_image.py
"""
import os

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (248, 244, 236)
INK = (26, 26, 26)
RED = (163, 22, 33)
MUTED = (90, 84, 74)
RULE = (26, 26, 26)
LIGHT_RULE = (180, 172, 158)

SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Wrap text to fit max_w pixels, returning a list of lines."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_wrapped(draw, x, y, text, fnt, max_w, fill, spacing=6):
    lines = wrap(draw, text, fnt, max_w)
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + spacing
    return y


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # --- masthead ---
    masthead = font(SERIF_BOLD, 62)
    title = "THE WORLD IN ONE DAY"
    tw = d.textlength(title, font=masthead)
    d.text(((W - tw) / 2, 28), title, font=masthead, fill=INK)
    d.line([(48, 108), (976, 108)], fill=RULE, width=3)
    d.line([(48, 114), (976, 114)], fill=RULE, width=1)

    date_font = font(SANS_BOLD, 34)
    date = "SUNDAY, 22 NOVEMBER 2026"
    tw = d.textlength(date, font=date_font)
    d.text(((W - tw) / 2, 128), date, font=date_font, fill=RED)
    d.line([(48, 178), (976, 178)], fill=RULE, width=2)

    # --- lead story: COP31 ---
    y = 196
    kick = font(SANS_BOLD, 22)
    d.text((48, y), "CLIMATE  •  ANTALYA, TURKEY", font=kick, fill=RED)
    y += 34
    head = font(SERIF_BOLD, 78)
    d.text((48, y), "COP31 COLLAPSES", font=head, fill=INK)
    y += 96
    deck = font(SERIF, 31)
    y = draw_wrapped(
        d, 48, y,
        "Climate summit ends with no deal as the EU rejects a draft "
        "with no mention of fossil fuels.",
        deck, 928, INK, spacing=8,
    )
    y += 6
    d.line([(48, y), (976, y)], fill=RULE, width=2)
    y += 18

    # --- story grid: 2 columns x 3 rows ---
    stories = [
        ("MIDDLE EAST", "IRAN HITS 3 TANKERS",
         "Strait of Hormuz attacks as the Gulf crisis widens."),
        ("UKRAINE", "DRONE HITS KYIV FLATS",
         "14 missing after a strike on an apartment block in Dymer."),
        ("MEXICO", "\u2018CHAPO ISIDRO\u2019 CAPTURED",
         "Cartel boss seized in Sinaloa; 11 killed in the raid."),
        ("JUSTICE", "MYANMAR GUILTY OF GENOCIDE",
         "World Court rules on the Rohingya in a landmark verdict."),
        ("INDONESIA", "FACTORY FIRE KILLS 3",
         "Dozens missing after a blaze at a candy plant in Cikande."),
        ("SPACE", "BEPICOLOMBO REACHES MERCURY",
         "Probe enters orbit after an eight-year journey."),
    ]
    col_w = 452
    xs = [48, 524]
    row_h = 156
    kick_f = font(SANS_BOLD, 19)
    head_f = font(SERIF_BOLD, 29)
    deck_f = font(SANS, 22)
    for i, (kicker, headline, deck_text) in enumerate(stories):
        col = i % 2
        row = i // 2
        x = xs[col]
        top = y + row * row_h
        d.text((x, top), kicker, font=kick_f, fill=RED)
        hy = top + 26
        hy = draw_wrapped(d, x, hy, headline, head_f, col_w, INK, spacing=4)
        draw_wrapped(d, x, hy + 2, deck_text, deck_f, col_w, MUTED, spacing=4)
        if col == 0:
            d.line([(500, top + 4), (500, top + row_h - 16)],
                   fill=LIGHT_RULE, width=1)
        if row < 2:
            d.line([(x, top + row_h - 8), (x + col_w, top + row_h - 8)],
                   fill=LIGHT_RULE, width=1)

    y = y + 3 * row_h + 8
    d.line([(48, y), (976, y)], fill=RULE, width=2)
    y += 14

    # --- footer briefs ---
    brief_f = font(SANS, 22)
    brief_f_b = font(SANS_BOLD, 22)
    d.text((48, y), "ALSO: ", font=brief_f_b, fill=INK)
    x = 48 + d.textlength("ALSO: ", font=brief_f_b)
    y = draw_wrapped(
        d, x, y,
        "FBI probes reported hack of crime database  •  M\u00e1rquez wins eighth MotoGP title",
        brief_f, 976 - x, MUTED, spacing=4,
    )

    # --- bottom line: date repeated, fills the page foot ---
    foot_f = font(SANS, 20)
    foot = "All stories from Sunday, 22 November 2026"
    tw = d.textlength(foot, font=foot_f)
    d.text(((W - tw) / 2, 984), foot, font=foot_f, fill=MUTED)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out, "PNG")
    print("wrote", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
