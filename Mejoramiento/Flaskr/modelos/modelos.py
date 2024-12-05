from flask import Flask
from marshmallow import Schema, fields
from flask_sqlalchemy import SQLAlchemy
import enum
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

# Inicialización de la base de datos
db = SQLAlchemy()

# Enumeración para roles de usuario
class RolEnum(enum.Enum):
    admin = "admin"
    empleado = "empleado"

# Modelo Usuario
class Usuario(db.Model):
    __tablename__ = "usuario"
    id_usuario = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(45), unique=True, nullable=False)
    contraseña = db.Column(db.String(255), nullable=False)
    rol = db.Column(db.Enum(RolEnum), nullable=False, default=RolEnum.empleado)
    empleado_id = db.Column(db.Integer, db.ForeignKey('empleado.id_empleado'), nullable=True)

    
    empleado = db.relationship("Empleado", back_populates="usuario")

    def __init__(self, correo, contraseña, rol, empleado):
        self.correo = correo
        self.contraseña = contraseña
        self.rol = rol
        self.empleado = empleado


# Modelo Empleado
class Empleado(db.Model):
    __tablename__ = "empleado"

    id_empleado = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45), nullable=False)
    apellido = db.Column(db.String(45), nullable=False)
    celular = db.Column(db.String(15), nullable=True)
    departamento_id = db.Column(db.Integer, db.ForeignKey('departamento.id_departamento'), nullable=True)

    usuario = db.relationship("Usuario", back_populates="empleado")
    familiares = db.relationship("Familiar", back_populates="empleado")

    def __init__(self, nombre, apellido, celular, departamento):
        self.nombre = nombre
        self.apellido = apellido
        self.celular = celular
        self.departamento = departamento


# Modelo Departamento
class Departamento(db.Model):
    __tablename__ = "departamento"

    id_departamento = db.Column(db.Integer, primary_key=True)
    nombre_departamento = db.Column(db.String(45), nullable=False)

    empleados = db.relationship("Empleado", backref="departamento")

    def __init__(self, nombre_departamento):
        self.nombre_departamento = nombre_departamento


# Modelo Familiar
class Familiar(db.Model):
    __tablename__ = "familiar"

    id_familiar = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45), nullable=False)
    relacion_empleado = db.Column(db.String(45), nullable=False)
    vive_con_empleado = db.Column(db.Boolean, nullable=False)
    empleado_id = db.Column(db.Integer, db.ForeignKey('empleado.id_empleado'), nullable=False)

    # Relación con Empleado
    empleado = db.relationship("Empleado", back_populates="familiares")

    def __init__(self, nombre, relacion_empleado, vive_con_empleado, empleado):
        self.nombre = nombre
        self.relacion_empleado = relacion_empleado
        self.vive_con_empleado = vive_con_empleado
        self.empleado = empleado

#serializacion de modelos

class UsuarioSchema(SQLAlchemyAutoSchema):
    class Meta:
        Mode = Usuario
        include_relationships = True

class EmpleadoSchema(SQLAlchemyAutoSchema):
    class Meta:
        Mode = Empleado
        include_relationships = True

class DepartamenoSchema(SQLAlchemyAutoSchema):
    class Meta:
        Mode = Departamento
        include_relationships = True

class UsuarioSchema(SQLAlchemyAutoSchema):
    class Meta:
        Mode = Usuario
        include_relationships = True