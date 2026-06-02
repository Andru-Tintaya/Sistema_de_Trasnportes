from app import db

class Chofer(db.Model):
    __tablename__ = 'choferes'
    id_chofer = db.Column(db.Integer, primary_key=True)
    ci = db.Column(db.String(15), unique=True, nullable=False)
    nombres = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    licencia = db.Column(db.String(20), nullable=False)
    telefono = db.Column(db.String(20), nullable=True)
    id_bus = db.Column(db.Integer, db.ForeignKey('buses.id_bus'), nullable=True)