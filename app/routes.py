from asyncio.log import logger
from flask import Blueprint, render_template, jsonify, request, current_app
from flask_cors import CORS
from app.utils.email import send_email, EmailError
import dns.resolver
import socket
from datetime import datetime, timedelta
from functools import wraps
import redis
import html
import logging

logger = logging.getLogger(__name__)

main_bp = Blueprint('main', __name__)
CORS(main_bp)

# Dictionnaire pour stocker les tentatives d'envoi (en mémoire)
email_attempts = {}

def rate_limit(limit=5, window=3600):
    """
    Décorateur pour limiter le nombre de requêtes par IP
    limit: nombre maximum de requêtes
    window: fenêtre de temps en secondes
    """
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            ip = request.remote_addr
            now = datetime.now()
            
            # Nettoyer les anciennes entrées (optimisation)
            current_time = datetime.now()
            cutoff_time = current_time - timedelta(seconds=window)
            
            # Utiliser une liste de compréhension pour filtrer les entrées expirées
            expired_ips = [k for k, v in email_attempts.items() if v['timestamp'] < cutoff_time]
            for expired_ip in expired_ips:
                email_attempts.pop(expired_ip, None)
            
            # Vérifier les tentatives pour cette IP
            if ip in email_attempts:
                if email_attempts[ip]['count'] >= limit:
                    retry_after = window - (now - email_attempts[ip]['timestamp']).seconds
                    return jsonify({
                        'error': 'Trop de tentatives. Veuillez réessayer plus tard.',
                        'retry_after': retry_after
                    }), 429
                email_attempts[ip]['count'] += 1
            else:
                email_attempts[ip] = {'count': 1, 'timestamp': now}
            
            return f(*args, **kwargs)
        return wrapped
    return decorator

def sanitize_input(text):
    """Nettoie les entrées utilisateur"""
    if text is None:
        return ""
    # Échapper les caractères HTML
    return html.escape(text.strip())

@main_bp.route('/contact', methods=['GET', 'POST', 'OPTIONS'])
@rate_limit(limit=5, window=3600)  # 5 emails par heure
def contact():
    if request.method == 'GET':
        return render_template('contact.html', active_page='contact')
        
    if request.method == 'OPTIONS':
        return '', 204
        
    if request.method == 'POST':
        try:
            data = request.get_json()
            if not data:
                return jsonify({'error': 'Aucune donnée reçue'}), 400
                
            # Nettoyer les entrées
            email = sanitize_input(data.get('email', '')).lower()
            message = sanitize_input(data.get('message', ''))
            name = sanitize_input(data.get('name', '')) or 'Anonymous'
            subject = sanitize_input(data.get('subject', '')) or 'Nouveau message de contact'
            
            # Validation des données
            validation_errors = validate_contact_data(email, message)
            if validation_errors:
                return jsonify({'error': validation_errors}), 400

            try:
                # Envoi de l'email principal
                html_content = create_html_content(name, email, subject, message)
                text_content = create_text_content(name, email, subject, message)
                
                # Ajouter des informations supplémentaires
                additional_info = {
                    'ip': request.remote_addr,
                    'user_agent': str(request.user_agent),
                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'referrer': request.referrer or 'Direct'
                }
                
                html_content += create_additional_info_html(additional_info)
                text_content += create_additional_info_text(additional_info)
                
                send_email(
                    subject=f'Portfolio Contact: {subject}',
                    recipients=['niainarisoa.mail@gmail.com'],
                    body=text_content,
                    html=html_content,
                    async_=True
                )
                
                if is_valid_email(email):
                    send_confirmation_email(email, name)
                
                return jsonify({
                    'message': 'Message envoyé avec succès',
                    'details': 'Vous recevrez une confirmation par email'
                }), 200
                
            except EmailError as e:
                logger.error(f"Erreur d'envoi d'email: {str(e)}")
                return jsonify({
                    'error': "Échec de l'envoi du message",
                    'details': str(e) if current_app.debug else None
                }), 500
                
        except Exception as e:
            logger.error(f"Erreur inattendue: {str(e)}")
            return jsonify({
                'error': 'Une erreur inattendue est survenue',
                'details': str(e) if current_app.debug else None
            }), 500

def create_additional_info_html(info):
    """Crée le HTML pour les informations supplémentaires"""
    return f"""
    <div style="margin-top: 20px; padding-top: 20px; border-top: 1px solid #eee; font-size: 12px; color: #666;">
        <h3 style="color: #333;">Informations supplémentaires</h3>
        <p>IP: {info['ip']}</p>
        <p>Navigateur: {info['user_agent']}</p>
        <p>Date: {info['timestamp']}</p>
        <p>Source: {info['referrer']}</p>
    </div>
    """

def create_additional_info_text(info):
    """Crée le texte pour les informations supplémentaires"""
    return f"""
    
    Informations supplémentaires:
    IP: {info['ip']}
    Navigateur: {info['user_agent']}
    Date: {info['timestamp']}
    Source: {info['referrer']}
    """

@main_bp.route('/')
def index():
    return render_template('index.html', active_page='home')

@main_bp.route('/about')
def about():
    return render_template('about.html', active_page='about')

@main_bp.route('/projects')
def projects():
    return render_template('projects.html', active_page='projects')

def validate_contact_data(email, message):
    """Valide les données du formulaire de contact"""
    if not email or not message:
        return 'Email et message sont requis'
    if not is_valid_email(email):
        return 'Format d\'email invalide ou adresse inexistante'
    if len(message.strip()) < 10:
        return 'Le message doit contenir au moins 10 caractères'
    return None

def is_valid_email(email):
    """Valide le format de l'email et vérifie le domaine"""
    import re
    if not email:
        return False
    
    # Nettoyage de l'email
    email = email.strip().lower()
    
    # Validation du format
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        return False
    
    # Vérification des domaines autorisés
    domain = email.split('@')[-1]
    allowed_domains = {
        'gmail.com': True,
        'yahoo.com': True,
        'hotmail.com': True,
        'outlook.com': True
    }
    
    return domain in allowed_domains

def send_confirmation_email(visitor_email, visitor_name):
    """Envoie un email de confirmation au visiteur"""
    if not is_valid_email(visitor_email):
        logger.warning(f"Tentative d'envoi de confirmation à une adresse invalide : {visitor_email}")
        return
        
    try:
        html_content = f"""
        <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
            <h2 style="color: #333;">Confirmation de votre message</h2>
            <p>Bonjour {visitor_name},</p>
            <p>Nous avons bien reçu votre message et nous vous répondrons dans les plus brefs délais.</p>
            <p>Merci de nous avoir contacté !</p>
            <p style="color: #666; font-size: 12px; margin-top: 30px;">
                Ceci est un message automatique, merci de ne pas y répondre.
            </p>
        </div>
        """
        
        send_email(
            subject='Confirmation de votre message',
            recipients=[visitor_email],  # Email du visiteur
            body='Nous avons bien reçu votre message et nous vous répondrons dans les plus brefs délais.',
            html=html_content,
            async_=True
        )
        logger.info(f"Email de confirmation envoyé à {visitor_email}")
    except Exception as e:
        logger.error(f"Erreur lors de l'envoi de l'email de confirmation à {visitor_email}: {str(e)}")

def create_html_content(name, email, subject, message):
    """Crée le contenu HTML de l'email"""
    return f"""
    <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
        <h2 style="color: #333; border-bottom: 2px solid #eee; padding-bottom: 10px;">
            Nouveau message de contact
        </h2>
        <div style="margin: 20px 0;">
            <p><strong>De:</strong> {name} ({email})</p>
            <p><strong>Sujet:</strong> {subject}</p>
        </div>
        <div style="background: #f9f9f9; padding: 15px; border-left: 4px solid #007bff; margin: 20px 0;">
            {message}
        </div>
        <p style="color: #666; font-size: 12px; margin-top: 30px; border-top: 1px solid #eee; padding-top: 10px;">
            Ce message a été envoyé via le formulaire de contact du portfolio.
        </p>
    </div>
    """

def create_text_content(name, email, subject, message):
    """Crée le contenu texte de l'email"""
    return f"""
    Nouveau message de contact
    
    De: {name} ({email})
    Sujet: {subject}
    
    Message:
    {message}
    
    Ce message a été envoyé via le formulaire de contact du portfolio.
    """
  