from app import db

class ViajeAsiento(db.Model):
    __tablename__ = 'viaje_asientos'
    id_viaje_asiento = db.Column(db.Integer, primary_key=True)
    id_viaje = db.Column(db.Integer, db.ForeignKey('viajes.id_viaje'), nullable=False)
    id_asiento = db.Column(db.Integer, db.ForeignKey('asientos.id_asiento'), nullable=False)
    estado = db.Column(db.String(20), default='libre') # libre, ocupado, reservado
    
    # Relaciones
    viaje = db.relationship('Viaje', backref='asientos_asignados')
    asiento = db.relationship('Asiento', backref='viajes_en_buso')