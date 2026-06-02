from app import db
from app.models.viaje import Viaje
from app.models.viaje_asiento import ViajeAsiento

def crear_viaje(origen, destino, fecha_viaje, hora_salida, id_bus, id_chofer):
    nuevo_viaje = Viaje(
        origen=origen,
        destino=destino,
        fecha_viaje=fecha_viaje,
        hora_salida=hora_salida,
        id_bus=id_bus,
        id_chofer=id_chofer
    )
    db.session.add(nuevo_viaje)
    db.session.commit()
    
    # Inicializar estados de asientos para este viaje (tabla asociativa)
    from app.models.asiento import Asiento
    asientos = Asiento.query.filter_by(id_bus=id_bus).all()
    
    for a in asientos:
        va = ViajeAsiento(
            id_viaje=nuevo_viaje.id_viaje,
            id_asiento=a.id_asiento,
            estado='libre'
        )
        db.session.add(va)
    
    db.session.commit()
    return nuevo_viaje