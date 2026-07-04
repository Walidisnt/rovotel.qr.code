# Rovotel — Avis Google contre carte cadeau

Système de QR codes à poser dans les chambres de l'hôtel Rovotel (3 Rue du
Douard, 13740 Le Rove). Le client scanne le code, laisse un avis Google, puis
ouvre une enveloppe animée qui révèle un code cadeau unique à présenter à la
réception.

## Site en ligne

**URL publique : https://walidisnt.github.io/rovotel.qr.code/**

Le site est hébergé gratuitement sur GitHub Pages, servi directement depuis
ce dépôt (dossier `rovotel-avis/`) via le workflow
`.github/workflows/pages.yml`. Toute modification poussée sur les branches
`main` ou `claude/rovotel-avis-deployment-x89g8v` republie automatiquement
le site — aucune action manuelle n'est nécessaire pour les mises à jour
futures.

## Contenu du dépôt

- `rovotel-avis/index.html` — page destination du QR code (design, textes et
  logique complets : bouton d'avis Google + enveloppe animée qui révèle un
  code cadeau unique par appareil).
- `rovotel-avis/generer_qr_codes.py` — génère un QR code PNG par chambre
  (chambres 1 à 18), pointant vers l'URL ci-dessus.
- `rovotel-avis/qr_codes/` — les 18 QR codes déjà générés
  (`chambre-1.png` … `chambre-18.png`), prêts à imprimer.
- `.github/workflows/pages.yml` — déploiement automatique sur GitHub Pages.

## Mode d'emploi pour la réceptionniste

1. Ouvrir le dossier `rovotel-avis/qr_codes/` sur l'ordinateur de la
   réception (ou le télécharger depuis GitHub : bouton vert **Code → Download
   ZIP**, puis dézipper).
2. Chaque fichier `chambre-XX.png` correspond au numéro de la chambre.
3. Imprimer chaque image (clic droit → Imprimer, ou les insérer dans un
   document Word/Canva pour un rendu plus soigné avec le logo de l'hôtel).
4. Coller ou glisser une image imprimée dans la chambre correspondante
   (près de la porte, sur le bureau, ou dans le livret d'accueil).
5. Le client scanne le code avec l'appareil photo de son téléphone, arrive
   sur la page Rovotel, clique sur « Laisser un avis Google », puis ouvre
   l'enveloppe pour découvrir son code cadeau. Il présente ce code à la
   réception au moment de son départ.

## Régénérer les QR codes

Si l'URL du site change un jour, modifier `SITE_URL` dans
`rovotel-avis/generer_qr_codes.py`, puis relancer :

```bash
pip3 install qrcode[pil]
python3 rovotel-avis/generer_qr_codes.py
```

Les 18 fichiers PNG seront régénérés dans `rovotel-avis/qr_codes/`.
