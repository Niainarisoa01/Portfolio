# Utiliser une image Python officielle
FROM python:3.9-slim

# Installer Node.js
RUN apt-get update && apt-get install -y \
    curl \
    && curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de dépendances
COPY requirements.txt package.json package-lock.json ./

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt
RUN npm install

# Copier le reste du code
COPY . .

# Construire les assets
RUN npm run build

# Exposer le port
EXPOSE $PORT

# Commande de démarrage
CMD gunicorn wsgi:app --bind=0.0.0.0:$PORT --log-file - 