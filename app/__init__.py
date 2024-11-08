from flask import Flask
from dotenv import load_dotenv
import os

def create_app():
    app = Flask(__name__, 
                static_folder='../static',
                template_folder='../templates')
    
    # Charger les variables d'environnement
    load_dotenv()
    
    # Configuration
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-secret-key')
    
    # Enregistrer les routes
    from app.routes import main_bp
    app.register_blueprint(main_bp)
    
    return app 