from app import create_app
from app.utils.email import send_email

def test_real_email():
    app = create_app()
    with app.app_context():
        try:
            send_email(
                subject='Test Email Configuration',
                recipients=['niainarisoa.mail@gmail.com'],
                body='Ceci est un test de configuration email',
                html='<h1>Test de Configuration Email</h1><p>Si vous voyez cet email, la configuration fonctionne correctement!</p>',
                async_=False
            )
            print("Email envoyé avec succès!")
        except Exception as e:
            print(f"Erreur lors de l'envoi de l'email: {str(e)}")

if __name__ == '__main__':
    test_real_email() 