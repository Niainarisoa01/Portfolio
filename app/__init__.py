from flask import Flask
from dotenv import load_dotenv
import os

# Charger les variables d'environnement
load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    # Enregistrer les blueprints
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app