import os
from datetime import timedelta

class Config:
    # Clave secreta desde variable de entorno o usar una fija
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-2024-transporte'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # URI absoluta para evitar problemas de ruta
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(BASE_DIR, 'database', 'transporte.db')
    
    # Configuración de Sesión - durará 12 horas
    PERMANENT_SESSION_LIFETIME = timedelta(hours=12)
    SESSION_COOKIE_SECURE = False  # Cambiar a True en producción con HTTPS
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    SESSION_COOKIE_SECURE = True

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}