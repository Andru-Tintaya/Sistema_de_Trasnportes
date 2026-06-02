from app import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id_usuario = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    nombres = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f'<Usuario {self.usuario}>'