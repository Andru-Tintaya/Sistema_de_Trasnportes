from app import db

class Asiento(db.Model):
    __tablename__ = 'asientos'
    id_asiento = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(10), nullable=False)
    id_bus = db.Column(db.Integer, db.ForeignKey('buses.id_bus'), nullable=False)
    
    # Relación simple
    bus_obj = db.relationship('Bus', back_populates='asientos')