#!/bin/bash

# Mise à jour de pip
python -m pip install --upgrade pip

# Installation des dépendances Python
pip install -r requirements.txt

# Installation explicite de gunicorn
pip install gunicorn

# Création des dossiers nécessaires
mkdir -p static/css

# Installation des dépendances Node.js et build de Tailwind
npm install
npm run build

# Ajout du chemin Python au PATH
export PATH=$PATH:/usr/local/python3/bin