import os
from datetime import timedelta

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-2024-transporte'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # URI absoluta para evitar problemas de ruta
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(BASE_DIR, 'database', 'transporte.db')
    # Configuración de Sesión
    PERMANENT_SESSION_LIFETIME = timedelta(hours=12)

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}