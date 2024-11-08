import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-à-changer'
    FLASK_ENV = os.environ.get('FLASK_ENV') or 'development'