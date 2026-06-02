from app.models.viaje_asiento import ViajeAsiento
from app import db

def get_estado_asiento(id_viaje, id_asiento):
    rel = ViajeAsiento.query.filter_by(id_viaje=id_viaje, id_asiento=id_asiento).first()
    return rel.estado if rel else None