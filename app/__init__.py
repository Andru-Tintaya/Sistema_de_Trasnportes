from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Registro de Blueprints
    from app.routes import auth, dashboard, buses, choferes, viajes, pasajeros, ventas, facturas
    
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
        # Crear usuario admin si no existe
        from app.models.usuario import Usuario
        from werkzeug.security import generate_password_hash
        if not Usuario.query.filter_by(usuario='admin').first():
            admin = Usuario(
                usuario='admin',
                password=generate_password_hash('admin123'),
                nombres='Administrador'
            )
            db.session.add(admin)
            db.session.commit()
            print("Usuario 'admin' creado con password 'admin123'")
        
    return app