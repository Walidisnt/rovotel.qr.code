"""Genere une carte QR code illustree par chambre, assortie au design du site.

Usage : python3 generer_qr_codes.py
Les fichiers sont ecrits dans qr_codes/chambre-<numero>.png
"""

import os

import qrcode
from PIL import Image, ImageDraw, ImageFont

SITE_URL = "https://walidisnt.github.io/rovotel.qr.code/"

ROOMS = [str(n) for n in range(1, 19)]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "qr_codes")

INK = (27, 31, 39)
PAPER = (250, 247, 242)
GOLD = (201, 163, 92)
GOLD_LIGHT = (232, 213, 168)
MUTED = (168, 175, 189)

CARD_W, CARD_H = 1000, 1500
FONT_DIR = "/usr/share/fonts/truetype/liberation"


def load_font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


def draw_centered_text(draw, xc, y, text, font, fill, tracking=0):
    if tracking:
        widths = [draw.textlength(ch, font=font) for ch in text]
        total = sum(widths) + tracking * (len(text) - 1)
        x = xc - total / 2
        for ch, w in zip(text, widths):
            draw.text((x, y), ch, font=font, fill=fill)
            x += w + tracking
    else:
        w = draw.textlength(text, font=font)
        draw.text((xc - w / 2, y), text, font=font, fill=fill)


def make_qr_image(url, box_size=14):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)
    return qr.make_image(fill_color=INK, back_color=PAPER).convert("RGB")


def generer_carte(room: str) -> Image.Image:
    url = f"{SITE_URL}?chambre={room}"

    card = Image.new("RGB", (CARD_W, CARD_H), INK)
    draw = ImageDraw.Draw(card)

    margin = 36
    draw.rounded_rectangle(
        [margin, margin, CARD_W - margin, CARD_H - margin],
        radius=28, outline=GOLD, width=3,
    )

    logo_font = load_font("LiberationSerif-Regular.ttf", 42)
    title_font = load_font("LiberationSerif-Regular.ttf", 56)
    room_font = load_font("LiberationSerif-Bold.ttf", 72)
    hint_font = load_font("LiberationSerif-Regular.ttf", 32)
    footer_font = load_font("LiberationSerif-Regular.ttf", 26)

    xc = CARD_W / 2

    draw_centered_text(draw, xc, 110, "R O V O T E L", logo_font, GOLD)
    draw_centered_text(draw, xc, 190, "Votre avis, votre cadeau", title_font, (255, 255, 255))

    # Cream frame holding the QR code
    qr_img = make_qr_image(url)
    frame_pad = 40
    frame_w = qr_img.width + frame_pad * 2
    frame_h = qr_img.height + frame_pad * 2
    frame_x0 = xc - frame_w / 2
    frame_y0 = 330
    draw.rounded_rectangle(
        [frame_x0, frame_y0, frame_x0 + frame_w, frame_y0 + frame_h],
        radius=24, fill=PAPER, outline=GOLD, width=3,
    )
    card.paste(qr_img, (int(frame_x0 + frame_pad), int(frame_y0 + frame_pad)))

    room_y = frame_y0 + frame_h + 60
    draw_centered_text(draw, xc, room_y, f"Chambre {room}", room_font, GOLD_LIGHT)

    hint_y = room_y + 110
    draw_centered_text(draw, xc, hint_y, "Scannez pour laisser un avis Google", hint_font, (255, 255, 255))
    draw_centered_text(draw, xc, hint_y + 42, "et recevoir votre carte cadeau", hint_font, (255, 255, 255))

    footer_y = CARD_H - margin - 60
    draw_centered_text(draw, xc, footer_y, "Rovotel  ·  3 Rue du Douard, 13740 Le Rove", footer_font, MUTED)

    return card


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for room in ROOMS:
        carte = generer_carte(room)
        carte.save(os.path.join(OUTPUT_DIR, f"chambre-{room}.png"))
    print(f"{len(ROOMS)} cartes QR generees dans : {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
