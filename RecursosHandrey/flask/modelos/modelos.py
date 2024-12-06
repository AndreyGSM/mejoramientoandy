from marshmallow import Schema, fields
from flask import Flask
from datetime import datetime
import bcrypt
import enum
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    es_superadmin = db.Column(db.Boolean, default=False)

class Departamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

class Empleado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    departamento_id = db.Column(db.Integer, db.ForeignKey('departamento.id'), nullable=False)
    foto_url = db.Column(db.String(300))
    departamento = db.relationship('Departamento', backref='empleados')

class Familiar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    parentesco = db.Column(db.String(50), nullable=False)
    vive_con_empleado = db.Column(db.Boolean, default=True)
    empleado_id = db.Column(db.Integer, db.ForeignKey('empleado.id'), nullable=False)
    empleado = db.relationship('Empleado', backref='familiares')

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