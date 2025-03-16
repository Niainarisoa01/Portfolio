FROM python:3.10-slim

WORKDIR /app

# Installer Node.js pour Tailwind CSS
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    && curl -sL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copier les fichiers de configuration
COPY requirements.txt package.json tailwind.config.js ./

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code avant de construire les assets
COPY . .

# Installer les dépendances Node.js et construire les assets
RUN npm install && npm run build

# Exposer le port
EXPOSE 5000

# Définir les variables d'environnement
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=5000

# Commande pour démarrer l'application
CMD ["python", "run.py"] 