from flask import Blueprint, render_template, request, redirect, url_for
from app.services import bus_service

bp = Blueprint('buses', __name__, url_prefix='/buses')

@bp.route('/')
def listar():
    buses = bus_service.obtener_buses()
    return render_template('buses/listar.html', buses=buses)

@bp.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        bus_service.crear_bus(
            request.form['placa'],
            request.form['modelo'],
            int(request.form['capacidad'])
        )
        return redirect(url_for('buses.listar'))
    return render_template('buses/crear.html')