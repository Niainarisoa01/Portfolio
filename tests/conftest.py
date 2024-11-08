import pytest
from app import create_app, mail
from app.config import Config

class TestConfig(Config):
    TESTING = True
    MAIL_SUPPRESS_SEND = True
    MAIL_DEFAULT_SENDER = "test@example.com"
    MAIL_USERNAME = "test@example.com"
    MAIL_PASSWORD = "test_password"
    MAIL_SERVER = "localhost"
    MAIL_PORT = 25
    MAIL_USE_TLS = False
    WTF_CSRF_ENABLED = False

@pytest.fixture
def app():
    app = create_app()
    app.config.from_object(TestConfig)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def mail_outbox():
    with mail.record_messages() as outbox:
        yield outbox 