from flask import Blueprint, render_template, url_for
from app.services import factura_service
from app.models.venta import Venta

bp = Blueprint('facturas', __name__, url_prefix='/facturas')

@bp.route('/detalle/<int:id_venta>')
def detalle(id_venta):
    venta = Venta.query.get_or_404(id_venta)
    factura = factura_service.obtener_factura_por_venta(id_venta)
    return render_template('facturas/detalle.html', venta=venta, factura=factura)