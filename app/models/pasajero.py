from app import db

class Pasajero(db.Model):
    __tablename__ = 'pasajeros'
    id_pasajero = db.Column(db.Integer, primary_key=True)
    ci = db.Column(db.String(15), unique=True, nullable=False)
    nombres = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20), nullable=True)