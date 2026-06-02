from app import db

class Viaje(db.Model):
    __tablename__ = 'viajes'
    id_viaje = db.Column(db.Integer, primary_key=True)
    origen = db.Column(db.String(50), nullable=False)
    destino = db.Column(db.String(50), nullable=False)
    fecha_viaje = db.Column(db.Date, nullable=False)
    hora_salida = db.Column(db.Time, nullable=False)
    id_bus = db.Column(db.Integer, db.ForeignKey('buses.id_bus'), nullable=False)
    id_chofer = db.Column(db.Integer, db.ForeignKey('choferes.id_chofer'), nullable=False)
    
    # Relaciones con nombres únicos
    bus_obj = db.relationship('Bus', foreign_keys=[id_bus])
    chofer_obj = db.relationship('Chofer', foreign_keys=[id_chofer])