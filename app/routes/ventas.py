from flask import Blueprint, render_template, request, redirect, url_for, session, flash, jsonify
from app import db
from app.models.viaje import Viaje
from app.models.asiento import Asiento
from app.models.viaje_asiento import ViajeAsiento
from app.models.venta import Venta
from app.models.pasajero import Pasajero
from app.models.factura import Factura
from datetime import datetime
import random

bp = Blueprint('ventas', __name__, url_prefix='/ventas')

@bp.route('/crear', methods=['GET', 'POST'])
def crear():
    viajes = Viaje.query.all()
    
    if request.method == 'POST':
        try:
            id_viaje = int(request.form['id_viaje'])
            id_asiento = int(request.form['id_asiento'])
            ci_pasajero = request.form['ci_pasajero']
            monto = float(request.form['monto'])
            
            # Verificar que el asiento esté libre
            asiento_viaje = ViajeAsiento.query.filter_by(
                id_viaje=id_viaje, 
                id_asiento=id_asiento
            ).first()
            
            if not asiento_viaje or asiento_viaje.estado != 'libre':
                flash('El asiento ya está ocupado. Seleccione otro.', 'error')
                return render_template('ventas/crear.html', viajes=viajes)
            
            # Buscar o crear pasajero
            pasajero = Pasajero.query.filter_by(ci=ci_pasajero).first()
            if not pasajero:
                pasajero = Pasajero(
                    ci=ci_pasajero,
                    nombres=request.form['nombres'],
                    apellidos=request.form['apellidos']
                )
                db.session.add(pasajero)
                db.session.flush()
            
            # Marcar asiento como ocupado
            asiento_viaje.estado = 'ocupado'
            
            # Crear venta
            nueva_venta = Venta(
                monto=monto,
                id_pasajero=pasajero.id_pasajero,
                id_viaje=id_viaje,
                id_asiento=id_asiento,
                id_usuario=session['id_usuario']
            )
            db.session.add(nueva_venta)
            db.session.flush()
            
            # Crear factura automáticamente
            nro_factura = f"FAC-{datetime.now().strftime('%Y%m%d')}-{random.randint(1000, 9999)}"
            factura = Factura(
                nro_factura=nro_factura,
                total=monto,
                id_venta=nueva_venta.id_venta
            )
            db.session.add(factura)
            db.session.commit()
            
            flash('Venta registrada exitosamente', 'success')
            return redirect(url_for('facturas.detalle', id_venta=nueva_venta.id_venta))
            
        except Exception as e:
            db.session.rollback()
            flash(f'Error: {str(e)}', 'error')
            
    return render_template('ventas/crear.html', viajes=viajes)

@bp.route('/asientos/<int:id_viaje>')
def get_asientos(id_viaje):
    # Devuelve JSON con estados de asientos para el grid
    datos = db.session.query(ViajeAsiento, Asiento).join(
        Asiento, 
        ViajeAsiento.id_asiento == Asiento.id_asiento
    ).filter(ViajeAsiento.id_viaje == id_viaje).all()
    
    asientos_dict = []
    for va, a in datos:
        asientos_dict.append({
            'id_asiento': a.id_asiento,
            'numero': a.numero,
            'estado': va.estado
        })
    
    return jsonify(asientos_dict)