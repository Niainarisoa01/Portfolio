from flask import Flask
from dotenv import load_dotenv
import os
from flask_mail import Mail
from app.config import Config

# Charger les variables d'environnement
load_dotenv()

mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    mail.init_app(app)
    
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    # Enregistrer les blueprints
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app