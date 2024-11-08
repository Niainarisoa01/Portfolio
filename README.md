# Portfolio Personnel - Développeur Full Stack

Un portfolio moderne et responsive développé avec Flask, Tailwind CSS et JavaScript.

## 🚀 Fonctionnalités

- Design moderne et responsive
- Mode sombre/clair
- Animations fluides
- Filtrage des projets
- Formulaire de contact
- Interface utilisateur intuitive
- Optimisé pour les performances
- Base de données SQLite intégrée

## 🛠️ Technologies Utilisées

- **Frontend**:
  - HTML5
  - Tailwind CSS
  - JavaScript
  - Font Awesome Icons

- **Backend**:
  - Python 3.x
  - Flask
  - Flask-Mail
  - Flask-SQLAlchemy

## 📋 Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)
- Node.js et npm (pour Tailwind CSS)
- Git

## 🔧 Installation

1. Clonez le repository :
```bash
git clone https://github.com/votre-username/portfolio.git
cd portfolio
```

2. Créez un environnement virtuel Python :
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Installez les dépendances Python :
```bash
pip install -r requirements.txt
```

4. Installez les dépendances Node.js :
```bash
npm install
```

5. Configurez les variables d'environnement :
```bash
cp .env.example .env
# Modifiez le fichier .env avec vos configurations
```

## 🚀 Démarrage

1. Compilez les assets CSS :
```bash
npm run build
# ou en mode développement :
npm run watch
```

2. Lancez le serveur Flask :
```bash
python app.py
```

3. Accédez à l'application :
```
http://localhost:5000
```

## 📁 Structure du Projet

```
portfolio/
├── app.py              # Application Flask principale
├── requirements.txt    # Dépendances Python
├── package.json        # Dépendances Node.js
├── static/
│   ├── css/           # Fichiers CSS compilés
│   ├── js/            # Scripts JavaScript
│   └── images/        # Images et assets
├── templates/         # Templates HTML
│   ├── layout.html    # Template de base
│   ├── index.html     # Page d'accueil
│   ├── about.html     # Page À propos
│   ├── projects.html  # Page Projets
│   └── contact.html   # Page Contact
└── venv/             # Environnement virtuel Python
```

## 🔧 Configuration

### Variables d'environnement (.env)

```env
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=votre-clé-secrète
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=votre-email@gmail.com
MAIL_PASSWORD=votre-mot-de-passe
```

### Base de données

La base de données SQLite est automatiquement créée au premier lancement.

## 🎨 Personnalisation

### Tailwind CSS

Modifiez le fichier `tailwind.config.js` pour personnaliser :
- Couleurs
- Polices
- Animations
- Breakpoints

### Contenu

1. Images : Placez vos images dans `static/images/`
2. Projets : Modifiez `templates/projects.html`
3. Informations personnelles : Modifiez `templates/about.html`

## 📱 Responsive Design

Le site est optimisé pour :
- Mobile (< 640px)
- Tablette (640px - 1024px)
- Desktop (> 1024px)

## 🌙 Mode Sombre

Activez/désactivez le mode sombre avec le bouton dans la navigation.

## 🚀 Déploiement

### Heroku
```bash
heroku create
git push heroku main
```

### VPS/Serveur
```bash
# Installez gunicorn
pip install gunicorn

# Lancez avec gunicorn
gunicorn app:app
```

## 📝 Maintenance

### Mise à jour des dépendances
```bash
pip install --upgrade -r requirements.txt
npm update
```

### Backup
```bash
# Base de données
sqlite3 instance/database.db .dump > backup.sql

# Images
cp -r static/images/ backup/
```

## 🤝 Contribution

1. Fork le projet
2. Créez votre branche (`git checkout -b feature/AmazingFeature`)
3. Commit vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## 📄 Licence

Distribué sous la licence MIT. Voir `LICENSE` pour plus d'informations.

## 📧 Contact

NOMENJANAHARY Niainarisoa - niainarisoa.mail@gmail.com

Lien du projet : [https://github.com/votre-username/portfolio](https://github.com/votre-username/portfolio)