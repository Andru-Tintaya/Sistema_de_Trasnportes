from app import db
from app.models.pasajero import Pasajero

def buscar_pasajero_por_ci(ci):
    return Pasajero.query.filter_by(ci=ci).first()

def registrar_pasajero(ci, nombres, apellidos, telefono):
    nuevo = Pasajero(ci=ci, nombres=nombres, apellidos=apellidos, telefono=telefono)
    db.session.add(nuevo)
    db.session.commit()
    return nuevo