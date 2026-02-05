# Fall Detection (YOLO - Ultralytics)

Détection de chute sur une image avec Ultralytics YOLO.

## Modèle
Télécharger `best.pt` ici et le placer à la racine du projet :
- https://huggingface.co/melihuzunoglu/human-fall-detection/resolve/main/best.pt

## Installation

```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows (PowerShell)
# .\.venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

## Utilisation

1) Place `best.pt` à la racine du projet  
2) Place une image de test à la racine (ex: `images2.jpeg`)  
3) Lance :

```bash
python main.py
```

## Notes
- Le script affiche **"Y a chute"** si la classe détectée est `0`.
