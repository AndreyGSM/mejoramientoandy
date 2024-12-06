from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from modelos.modelos import db, Usuario

usuario_bp = Blueprint('usuario', __name__)

@usuario_bp.route('/registro', methods=['POST'])
def registro():
    data = request.json
    if Usuario.query.filter_by(email=data['email']).first():
        return jsonify({'mensaje': 'Usuario ya registrado'}), 400

    hashed_password = generate_password_hash(data['password'], method='sha256')
    nuevo_usuario = Usuario(
        nombre=data['nombre'],
        email=data['email'],
        password=hashed_password
    )
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify({'mensaje': 'Usuario registrado exitosamente'})

@usuario_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    usuario = Usuario.query.filter_by(email=data['email']).first()
    if not usuario or not check_password_hash(usuario.password, data['password']):
        return jsonify({'mensaje': 'Credenciales inválidas'}), 401

    return jsonify({'mensaje': 'Inicio de sesión exitoso', 'usuario_id': usuario.id})

def crear_superadmin():
    if not Usuario.query.filter_by(es_superadmin=True).first():
        superadmin = Usuario(
            nombre='SuperAdmin',
            email='admin@empresa.com',
            password=generate_password_hash('admin123', method='sha256'),
            es_superadmin=True
        )
        db.session.add(superadmin)
        db.session.commit()
