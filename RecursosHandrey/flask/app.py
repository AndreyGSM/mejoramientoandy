from flask import Flask
from flask_migrate import Migrate
from modelos.modelos import db
from vistas.usuario_vista import usuario_bp, crear_superadmin
from vistas.empleado_vista import empleado_bp
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Inicializar la base de datos y las migraciones
db.init_app(app)
migrate = Migrate(app, db)

# Registrar los blueprints
app.register_blueprint(usuario_bp, url_prefix='/usuario')
app.register_blueprint(empleado_bp, url_prefix='/empleado')

@app.before_first_request
def setup():
    # Crear tablas y el superadmin si no existen
    db.create_all()
    crear_superadmin()

if __name__ == '__main__':
    app.run(debug=True)
