from flask import Blueprint, render_template, request, redirect, url_for
from app.services import chofer_service

bp = Blueprint('choferes', __name__, url_prefix='/choferes')

@bp.route('/')
def listar():
    choferes = chofer_service.obtener_choferes()
    return render_template('choferes/listar.html', choferes=choferes)

@bp.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        chofer_service.crear_chofer(
            request.form['ci'], request.form['nombres'],
            request.form['apellidos'], request.form['licencia'],
            request.form.get('telefono')
        )
        return redirect(url_for('choferes.listar'))
    return render_template('choferes/crear.html')