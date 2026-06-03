from flask import Blueprint, render_template, request, jsonify
from app.services import pasajero_service

bp = Blueprint('pasajeros', __name__, url_prefix='/pasajeros')

@bp.route('/buscar', methods=['POST'])
def buscar():
    data = request.json
    pasajero = pasajero_service.buscar_pasajero_por_ci(data['ci'])
    if pasajero:
        return jsonify({'existe': True, 'id': pasajero.id_pasajero, 'nombres': pasajero.nombres, 'apellidos': pasajero.apellidos})
    return jsonify({'existe': False})

@bp.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        pasajero_service.registrar_pasajero(
            request.form['ci'], request.form['nombres'],
            request.form['apellidos'], request.form.get('telefono')
        )
        return "ok" 
    return render_template('pasajeros/crear.html')