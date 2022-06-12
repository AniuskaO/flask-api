from flask import Flask, request, jsonify
from flask_migrate import Migrate 
from models import db, Usuario, Region, Descuento, Suscripcion
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Conten=Type'
app.url_map.strict_slashes = False
app.config['DEBUG'] = False
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

Migrate(app, db)

@app.route('/')
def index():
    return 'Hola'


@app.route('/usuarios', methods=['GET'])
def getUsuarios():
    user = Usuario.query.all()
    user = list(map(lambda x: x.serialize(), user))
    return jsonify(user),200

@app.route('/usuario', methods=['POST'])
def addUsuario():
    user = Usuario()

    user.rut = request.json.get("rut")
    user.dv = request.json.get("dv")
    user.primer_nombre = request.json.get('primer_nombre')
    user.segundo_nombre = request.json.get('segundo_nombre')
    user.primer_apellido = request.json.get('primer_apellido')
    user.segundo_apellido = request.json.get('segundo_apellido')
    user.direccion = request.json.get('direccion')
    user.fono = request.json.get('fono')
    user.correo = request.json.get('correo')
    user.estado = request.json.get('estado')

    Usuario.save(user)

    return jsonify(user.serialize()),200

@app.route('/usuarios/<id>', methods=['DELETE'])
def deleteUsuario(id):
    user = Usuario.query.get(id)
    Usuario.delete(user)
    return jsonify(user.serialize()),200


@app.route('/usuarios/<id>', methods=['PUT'])
def updateUsuario(id):
    user = Usuario.query.get(id)

    user.rut = request.json.get("rut")
    user.dv = request.json.get("dv")
    user.primer_nombre = request.json.get('primer_nombre')
    user.segundo_nombre = request.json.get('segundo_nombre')
    user.primer_apellido = request.json.get('primer_apellido')
    user.segundo_apellido = request.json.get('segundo_apellido')
    user.direccion = request.json.get('direccion')
    user.fono = request.json.get('fono')
    user.correo = request.json.get('correo')
    user.estado = request.json.get('estado')

    Usuario.save(user)

    return jsonify(user.serialize()),200






if __name__ == '__main__':
    app.run(port=5000, debug=True)


