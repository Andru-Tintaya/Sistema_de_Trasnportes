from flask import Blueprint, render_template, request, redirect, url_for, session, flash
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
        
        user = Usuario.query.filter_by(usuario=usuario).first()
        if user and check_password_hash(user.password, password):
            session['id_usuario'] = user.id_usuario
            session['usuario'] = user.usuario
            return redirect(url_for('dashboard.index'))
        else:
            flash('Credenciales incorrectas', 'error')
    return render_template('auth/login.html')

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))