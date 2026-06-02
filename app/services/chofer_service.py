from app import db
from app.models.chofer import Chofer

def crear_chofer(ci, nombres, apellidos, licencia, telefono, id_bus=None):
    # Validar duplicado
    if Chofer.query.filter_by(ci=ci).first():
        raise Exception("Ya existe un chofer con este CI.")
    
    nuevo_chofer = Chofer(
        ci=ci, nombres=nombres, apellidos=apellidos,
        licencia=licencia, telefono=telefono, id_bus=id_bus
    )
    db.session.add(nuevo_chofer)
    db.session.commit()
    return nuevo_chofer

def obtener_choferes():
    return Chofer.query.all()

def actualizar_chofer(id_chofer, datos):
    chofer = Chofer.query.get(id_chofer)
    for key, value in datos.items():
        setattr(chofer, key, value)
    db.session.commit()
    return chofer