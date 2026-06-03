from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config
import os
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Agregar credenciales de admin desde variables de entorno
    app.config['ADMIN_USUARIO'] = os.environ.get('ADMIN_USUARIO', 'admin')
    app.config['ADMIN_PASSWORD'] = os.environ.get('ADMIN_PASSWORD', 'admin456')
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Registro de Blueprints
    from app.routes import auth, dashboard, buses, choferes, viajes,pasajeros, ventas, facturas
    
    app.register_blueprint(auth.bp)
    app.register_blueprint(dashboard.bp)
    app.register_blueprint(buses.bp)
    app.register_blueprint(choferes.bp)
    app.register_blueprint(viajes.bp)
    app.register_blueprint(pasajeros.bp)
    app.register_blueprint(ventas.bp)
    app.register_blueprint(facturas.bp)
    
    # Crear tablas si no existen
    with app.app_context():
        db.create_all()
        
    return app