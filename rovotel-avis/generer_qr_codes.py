"""Génère un QR code PNG par chambre pointant vers le site d'avis Rovotel.

Usage : python3 generer_qr_codes.py
Les fichiers sont écrits dans qr_codes/chambre-<numero>.png
"""

import os

import qrcode

SITE_URL = "https://walidisnt.github.io/rovotel.qr.code/"

ROOMS = [str(n) for n in range(1, 19)]

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "qr_codes")


def generer_qr_code(room: str) -> None:
    url = f"{SITE_URL}?chambre={room}"

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    image = qr.make_image(fill_color="black", back_color="white")
    image.save(os.path.join(OUTPUT_DIR, f"chambre-{room}.png"))


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for room in ROOMS:
        generer_qr_code(room)
    print(f"{len(ROOMS)} QR codes générés dans : {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
