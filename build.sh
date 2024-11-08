#!/bin/bash

# Installation de pip de manière sûre
python -m ensurepip --upgrade
python -m pip install --no-cache-dir --upgrade pip setuptools wheel

# Installation des dépendances Python sans utiliser le cache
pip install --no-cache-dir -r requirements.txt

# Installation explicite de gunicorn
pip install --no-cache-dir gunicorn

# Création des dossiers nécessaires
mkdir -p static/css

# Installation des dépendances Node.js et build de Tailwind
npm install
npm run build

# Ajout du chemin Python au PATH
export PATH=$PATH:/usr/local/python3/bin