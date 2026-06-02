from app import db

class Venta(db.Model):
    __tablename__ = 'ventas'
    id_venta = db.Column(db.Integer, primary_key=True)
    fecha_venta = db.Column(db.DateTime, default=db.func.current_timestamp())
    monto = db.Column(db.Numeric(10, 2), nullable=False)
    id_pasajero = db.Column(db.Integer, db.ForeignKey('pasajeros.id_pasajero'), nullable=False)
    id_viaje = db.Column(db.Integer, db.ForeignKey('viajes.id_viaje'), nullable=False)
    id_asiento = db.Column(db.Integer, db.ForeignKey('asientos.id_asiento'), nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=False)
    
    # Relaciones
    pasajero = db.relationship('Pasajero', backref='ventas')
    viaje = db.relationship('Viaje', backref='ventas')
    asiento = db.relationship('Asiento', backref='ventas')
    factura = db.relationship('Factura', backref='venta', uselist=False)