from flask import Blueprint, render_template, request, redirect, url_for, session, flash, current_app
from werkzeug.security import check_password_hash
from app.models.usuario import Usuario
from app import db

bp = Blueprint('auth', __name__)

@bp.route('/')
def index():
    return redirect(url_for('auth.login'))

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        
        # Obtener credenciales de config
        admin_usuario = current_app.config.get('ADMIN_USUARIO')
        admin_password = current_app.config.get('ADMIN_PASSWORD')
        
        # PRIMERO verificar contra variables de entorno (más seguro)
        if usuario == admin_usuario and password == admin_password:
            session['id_usuario'] = 0
            session['usuario'] = 'admin'
            session.permanent = True
            return redirect(url_for('dashboard.index'))
        
        # LUEGO verificar en la base de datos
        user = Usuario.query.filter_by(usuario=usuario).first()
        if user and check_password_hash(user.password, password):
            session['id_usuario'] = user.id_usuario
            session['usuario'] = user.usuario
            session.permanent = True
            return redirect(url_for('dashboard.index'))
        
        flash('Credenciales incorrectas', 'error')
    
    return render_template('auth/login.html')

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))