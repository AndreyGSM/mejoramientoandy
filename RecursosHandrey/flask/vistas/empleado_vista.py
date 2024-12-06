from flask import Blueprint, request, jsonify
from modelos.modelos import db, Empleado, Departamento

empleado_bp = Blueprint('empleado', __name__)

@empleado_bp.route('/empleados', methods=['GET'])
def obtener_empleados():
    empleados = Empleado.query.all()
    return jsonify([{
        'id': emp.id,
        'nombre': emp.nombre,
        'departamento': emp.departamento.nombre
    } for emp in empleados])

@empleado_bp.route('/empleados', methods=['POST'])
def crear_empleado():
    data = request.json
    nuevo_empleado = Empleado(
        nombre=data['nombre'],
        departamento_id=data['departamento_id']
    )
    db.session.add(nuevo_empleado)
    db.session.commit()
    return jsonify({'mensaje': 'Empleado creado exitosamente'})
