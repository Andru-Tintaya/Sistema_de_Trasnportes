from flask import Blueprint, render_template, request, redirect, url_for
from app.services import viaje_service
from datetime import datetime

bp = Blueprint('viajes', __name__, url_prefix='/viajes')

@bp.route('/')
def listar():
    from app.models.viaje import Viaje
    viajes = Viaje.query.order_by(Viaje.fecha_viaje.desc()).all()
    return render_template('viajes/listar.html', viajes=viajes)

@bp.route('/crear', methods=['GET', 'POST'])
def crear():
    from app.models.bus import Bus
    from app.models.chofer import Chofer
    if request.method == 'POST':
        viaje_service.crear_viaje(
            request.form['origen'], request.form['destino'],
            datetime.strptime(request.form['fecha_viaje'], '%Y-%m-%d').date(),
            datetime.strptime(request.form['hora_salida'], '%H:%M').time(),
            int(request.form['id_bus']), int(request.form['id_chofer'])
        )
        return redirect(url_for('viajes.listar'))
    
    buses = Bus.query.all()
    choferes = Chofer.query.all()
    return render_template('viajes/crear.html', buses=buses, choferes=choferes)