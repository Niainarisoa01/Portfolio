from flask import current_app
from flask_mail import Message
from app import mail
from threading import Thread
import logging
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class EmailError(Exception):
    """Exception personnalisée pour les erreurs d'email"""
    pass

def send_async_email(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
            logger.info(f"Email envoyé avec succès à {msg.recipients}")
        except Exception as e:
            logger.error(f"Erreur lors de l'envoi de l'email: {str(e)}")
            raise EmailError(f"Échec de l'envoi de l'email: {str(e)}")

def send_email(subject, recipients, body, html=None, async_=True, retry_count=3):
    """
    Envoie un email avec retry et backoff exponentiel
    
    Args:
        subject (str): Sujet de l'email
        recipients (list): Liste des destinataires
        body (str): Corps du message en texte brut
        html (str, optional): Corps du message en HTML
        async_ (bool): Si True, envoie l'email de manière asynchrone
        retry_count (int): Nombre de tentatives en cas d'échec
    """
    try:
        msg = Message(subject,
                     sender=current_app.config['MAIL_DEFAULT_SENDER'],
                     recipients=recipients,
                     body=body,
                     html=html)
        
        logger.info(f"Tentative d'envoi d'email à {recipients}")
        
        if current_app.config.get('TESTING', False):
            logger.info("Mode test: email simulé")
            return msg

        for attempt in range(retry_count):
            try:
                if async_ and not current_app.config.get('TESTING', False):
                    Thread(target=send_async_email,
                           args=(current_app._get_current_object(), msg)).start()
                    logger.info("Email envoyé en mode asynchrone")
                else:
                    mail.send(msg)
                    logger.info("Email envoyé en mode synchrone")
                return msg
            except Exception as e:
                if attempt == retry_count - 1:  # Dernière tentative
                    raise
                # Backoff exponentiel: attendre 2^attempt secondes avant de réessayer
                wait_time = 2 ** attempt
                logger.warning(f"Tentative {attempt + 1} échouée, nouvelle tentative dans {wait_time}s...")
                time.sleep(wait_time)
                
    except Exception as e:
        error_msg = f"Erreur lors de la création/envoi de l'email: {str(e)}"
        logger.error(error_msg)
        raise EmailError(error_msg)