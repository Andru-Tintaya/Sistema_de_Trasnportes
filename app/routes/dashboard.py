from flask import Blueprint, render_template
from app import db
from app.models.venta import Venta
from app.models.pasajero import Pasajero
from app.models.bus import Bus
from app.models.viaje import Viaje
from datetime import datetime

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.route('/')
def index():
    hoy = datetime.now().date()
    
    # Contar ventas de hoy
    total_ventas_hoy = db.session.query(Venta).filter(
        db.func.date(Venta.fecha_venta) == hoy
    ).count()
    
    total_pasajeros = Pasajero.query.count()
    total_buses = Bus.query.count()
    total_viajes = Viaje.query.count()
    
    return render_template('dashboard/index.html', 
                     ventas_hoy=total_ventas_hoy,
                     pasajeros=total_pasajeros,
                     buses=total_buses,
                     viajes=total_viajes)