from app import db
from app.models.bus import Bus
from app.models.asiento import Asiento

def crear_bus(placa, modelo, capacidad):
    nuevo_bus = Bus(placa=placa, modelo=modelo, capacidad=capacidad)
    db.session.add(nuevo_bus)
    db.session.commit()
    
    # Generar asientos automáticamente según capacidad
    for i in range(1, capacidad + 1):
        nuevo_asiento = Asiento(numero=str(i), id_bus=nuevo_bus.id_bus)
        db.session.add(nuevo_asiento)
    
    db.session.commit()
    return nuevo_bus

def obtener_buses():
    return Bus.query.all()

def obtener_bus_por_id(id_bus):
    return Bus.query.get(id_bus)