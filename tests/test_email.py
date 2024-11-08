import pytest
from app import mail
from app.utils.email import send_email

def test_email_configuration(app):
    """Test de la configuration email"""
    assert app.config['MAIL_SERVER'] == 'localhost'
    assert app.config['MAIL_PORT'] == 25
    assert app.config['MAIL_USE_TLS'] is False
    assert app.config['MAIL_USERNAME'] is not None
    assert app.config['MAIL_PASSWORD'] is not None

def test_send_email(app, mail_outbox):
    """Test d'envoi d'email"""
    with app.app_context():
        msg = send_email(
            subject='Test Subject',
            recipients=['test@example.com'],
            body='Test body',
            html='<h1>Test HTML</h1>',
            async_=False
        )
        
        # Vérifier que le message est correctement configuré
        assert msg.subject == 'Test Subject'
        assert msg.recipients == ['test@example.com']
        assert msg.body == 'Test body'
        assert msg.html == '<h1>Test HTML</h1>'

def test_contact_route_success(client, app):
    """Test de succès de la route /contact"""
    with app.app_context():
        response = client.post('/contact', json={
            'email': 'test@example.com',
            'message': 'Test message'
        })
        assert response.status_code == 200
        data = response.get_json()
        assert data['message'] == 'Email envoyé avec succès'

def test_contact_route_error(client, app):
    """Test de la gestion d'erreur dans la route /contact"""
    with app.app_context():
        # Test avec des données manquantes
        response = client.post('/contact', json={})
        assert response.status_code == 400
        
        # Test avec des données invalides
        response = client.post('/contact', json={
            'email': '',
            'message': ''
        })
        assert response.status_code == 400