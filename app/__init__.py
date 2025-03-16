from flask import Flask
from flask_mail import Mail
from app.config import Config

mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    mail.init_app(app)
    
    # Enregistrer les blueprints
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app