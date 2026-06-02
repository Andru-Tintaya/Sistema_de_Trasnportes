from app import db
from app.models.factura import Factura
from datetime import datetime
import random
import string

def generar_factura(id_venta, monto):
    # Generar número único de factura
    nro_factura = generar_nro_factura_unico()
    
    nueva_factura = Factura(
        nro_factura=nro_factura,
        total=monto,
        id_venta=id_venta
    )
    db.session.add(nueva_factura)
    db.session.commit()
    return nueva_factura

def generar_nro_factura_unico():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    random_suffix = ''.join(random.choices(string.digits, k=4))
    return f"FAC-{timestamp}-{random_suffix}"

def obtener_factura_por_venta(id_venta):
    return Factura.query.filter_by(id_venta=id_venta).first()