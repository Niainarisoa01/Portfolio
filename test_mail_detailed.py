from app import create_app
from app.utils.email import send_email
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_real_email():
    app = create_app()
    with app.app_context():
        try:
            # Test de la configuration
            logger.info(f"MAIL_SERVER: {app.config['MAIL_SERVER']}")
            logger.info(f"MAIL_PORT: {app.config['MAIL_PORT']}")
            logger.info(f"MAIL_USE_TLS: {app.config['MAIL_USE_TLS']}")
            logger.info(f"MAIL_USERNAME: {app.config['MAIL_USERNAME']}")
            logger.info(f"MAIL_DEFAULT_SENDER: {app.config['MAIL_DEFAULT_SENDER']}")
            
            # Envoi de l'email test
            send_email(
                subject='Test Email Configuration Détaillé',
                recipients=['niainarisoa.mail@gmail.com'],
                body='Test détaillé de la configuration email',
                html='''
                <h1>Test Détaillé de Configuration Email</h1>
                <p>Si vous voyez cet email, la configuration fonctionne correctement!</p>
                <p>Ceci est un test avec logging détaillé.</p>
                ''',
                async_=False  # Mode synchrone pour voir les erreurs immédiatement
            )
            print("Email envoyé avec succès!")
        except Exception as e:
            logger.error(f"Erreur détaillée lors de l'envoi de l'email: {str(e)}", exc_info=True)
            raise

if __name__ == '__main__':
    test_real_email() 