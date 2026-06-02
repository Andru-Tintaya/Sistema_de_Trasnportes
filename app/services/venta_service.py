from app import db
from app.models.venta import Venta
from app.models.viaje_asiento import ViajeAsiento
from app.models.factura import Factura
import random
from datetime import datetime

def registrar_venta(id_viaje, id_asiento, id_pasajero, id_usuario, monto):
    # Verificar que el asiento esté libre
    asiento_viaje = ViajeAsiento.query.filter_by(
        id_viaje=id_viaje, 
        id_asiento=id_asiento
    ).first()
    
    if not asiento_viaje or asiento_viaje.estado != 'libre':
        raise Exception("El asiento ya está ocupado.")
    
    # Marcar asiento como ocupado
    asiento_viaje.estado = 'ocupado'
    
    # Crear la venta
    nueva_venta = Venta(
        monto=monto,
        id_pasajero=id_pasajero,
        id_viaje=id_viaje,
        id_asiento=id_asiento,
        id_usuario=id_usuario
    )
    db.session.add(nueva_venta)
    db.session.flush()
    
    # Generar factura automáticamente
    nro_factura = f"FAC-{datetime.now().year}-{random.randint(1000, 9999)}"
    factura = Factura(
        nro_factura=nro_factura,
        total=monto,
        id_venta=nueva_venta.id_venta
    )
    db.session.add(factura)
    db.session.commit()
    
    return nueva_venta