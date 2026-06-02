from app import db

class Bus(db.Model):
    __tablename__ = 'buses'
    id_bus = db.Column(db.Integer, primary_key=True)
    placa = db.Column(db.String(15), unique=True, nullable=False)
    modelo = db.Column(db.String(50), nullable=False)
    capacidad = db.Column(db.Integer, nullable=False)
    
    # Relación simple sin backref automático
    asientos = db.relationship('Asiento', back_populates='bus_obj')