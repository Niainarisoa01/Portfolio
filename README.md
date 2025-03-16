# Portfolio de Niainarisoa

Un portfolio moderne et responsive développé avec Flask et Tailwind CSS.

## 🚀 Fonctionnalités

- Design moderne et responsive avec Tailwind CSS
- Mode sombre/clair
- Animations et transitions fluides
- Formulaire de contact fonctionnel
- Options d'accessibilité
- Mode d'impression optimisé

## 🛠️ Technologies utilisées

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript, Tailwind CSS
- **Déploiement**: Docker, GitHub Actions, Railway, Render

## 📋 Prérequis

- Python 3.10+
- Node.js 18+
- npm ou yarn

## 🔧 Installation

1. Clonez le dépôt:
   ```bash
   git clone https://github.com/votre-username/portfolio.git
   cd portfolio
   ```

2. Créez un environnement virtuel et installez les dépendances:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Sur Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Installez les dépendances Node.js:
   ```bash
   npm install
   ```

4. Créez un fichier `.env` à la racine du projet:
   ```
   DEBUG=True
   SECRET_KEY=votre_clé_secrète
   MAIL_SERVER=smtp.gmail.com
   MAIL_PORT=587
   MAIL_USE_TLS=True
   MAIL_USERNAME=votre_email@gmail.com
   MAIL_PASSWORD=votre_mot_de_passe_app
   MAIL_DEFAULT_SENDER=votre_email@gmail.com
   ```

## 🏃‍♂️ Exécution locale

### Méthode 1: Exécution directe

1. Compilez les assets CSS:
   ```bash
   npm run build
   ```

2. Lancez l'application:
   ```bash
   python run.py
   ```

3. Pour le développement, vous pouvez utiliser le mode watch pour Tailwind:
   ```bash
   npm run watch
   ```

### Méthode 2: Utilisation de Docker Compose

1. Lancez l'application avec Docker Compose:
   ```bash
   docker-compose up
   ```

## 🚢 Déploiement

### Configuration CI/CD avec GitHub Actions

Ce projet est configuré pour un déploiement automatique via GitHub Actions. À chaque push sur la branche `main` ou `master`, le workflow suivant est exécuté:

1. **Test**: Vérifie que le code est conforme aux standards
2. **Build**: Compile les assets et prépare l'application pour le déploiement
3. **Deploy**: Déploie l'application sur Railway et/ou Render

### Configuration des secrets GitHub

Pour que le déploiement fonctionne, vous devez configurer les secrets suivants dans votre dépôt GitHub:

1. Allez dans Settings > Secrets and variables > Actions
2. Ajoutez les secrets suivants:
   - `SECRET_KEY`: Clé secrète pour Flask
   - `MAIL_SERVER`: Serveur SMTP
   - `MAIL_PORT`: Port SMTP
   - `MAIL_USE_TLS`: Utilisation de TLS (True/False)
   - `MAIL_USERNAME`: Nom d'utilisateur SMTP
   - `MAIL_PASSWORD`: Mot de passe SMTP
   - `MAIL_DEFAULT_SENDER`: Expéditeur par défaut
   - `RAILWAY_TOKEN`: Token d'API Railway (si vous utilisez Railway)
   - `RENDER_API_KEY`: Clé API Render (si vous utilisez Render)
   - `RENDER_SERVICE_ID`: ID du service Render (si vous utilisez Render)

### Déploiement manuel

#### Railway

1. Installez le CLI Railway:
   ```bash
   npm install -g @railway/cli
   ```

2. Connectez-vous à Railway:
   ```bash
   railway login
   ```

3. Liez votre projet:
   ```bash
   railway link
   ```

4. Déployez:
   ```bash
   railway up
   ```

#### Render

1. Créez un nouveau service Web sur Render
2. Connectez votre dépôt GitHub
3. Configurez les variables d'environnement
4. Déployez

## 📝 Personnalisation

### Modification du contenu

- Les templates se trouvent dans `app/templates/`
- Les styles CSS personnalisés sont dans `app/static/css/custom.css`
- Les scripts JavaScript sont dans `app/static/js/main.js`

### Ajout d'images

Placez vos images dans le dossier `app/static/images/`

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 📧 Contact

Pour toute question ou suggestion, n'hésitez pas à me contacter à [niainarisoa.mail@gmail.com](mailto:niainarisoa.mail@gmail.com).