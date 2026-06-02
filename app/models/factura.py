from app import db

class Factura(db.Model):
    __tablename__ = 'facturas'
    id_factura = db.Column(db.Integer, primary_key=True)
    nro_factura = db.Column(db.String(20), unique=True, nullable=False)
    fecha_emision = db.Column(db.DateTime, default=db.func.current_timestamp())
    total = db.Column(db.Numeric(10, 2), nullable=False)
    id_venta = db.Column(db.Integer, db.ForeignKey('ventas.id_venta'), unique=True, nullable=False)