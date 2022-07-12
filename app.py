# Importing the necessary libraries for the project.
from datetime import datetime
from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Producto, Region, Comuna, Vendedor, Cliente, Venta, Despacho, Detalle
from flask_cors import CORS, cross_origin

# Creating the app and configuring it.
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.url_map.strict_slashes = False

app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

Migrate(app, db)

'''
@app.route('/')
def index():
    return 'Hola'
'''

#Productos
@app.route('/productos', methods=['GET'])
def getProductos():
    user = Producto.query.all()
    user = list(map(lambda x: x.serialize(), user))
    return jsonify(user),200

@app.route('/productos/<id_producto>', methods=['DELETE'])
def deleteProducto(id_producto):
    user = Producto.query.get(id_producto)
    Producto.delete(user)
    return jsonify(user.serialize()),200

@app.route('/productos', methods=['POST'])
def addProductos():
    user = Producto()
    user.id_producto = request.json.get('id_producto')
    user.codigo = request.json.get('codigo')
    user.nombre = request.json.get('nombre')
    user.valor_venta = request.json.get('valor_venta')
    user.stock = request.json.get('stock')
    user.descripcion = request.json.get('descripcion')
    user.imagen = request.json.get('imagen')
    user.estado = request.json.get('estado')

    Producto.save(user)

    return jsonify(user.serialize()),200

@app.route('/productos/<id_producto>', methods=['GET'])
def getProducto(id_producto):
    user = Producto.query.get(id_producto)
    return jsonify(user.serialize()),200

@app.route('/productos/<id_producto>', methods=['PUT'])
def updateProducto(id_producto):
    user = Producto.query.get(id_producto)

    user.id_producto = request.json.get('id_producto')
    user.codigo = request.json.get('codigo')
    user.nombre = request.json.get('nombre')
    user.valor_venta = request.json.get('valor_venta')
    user.stock = request.json.get('stock')
    user.descripcion = request.json.get('descripcion')
    user.imagen = request.json.get('imagen')
    user.estado = request.json.get('estado')

    Producto.update(user)

    return jsonify(user.serialize()),200


# Region
@app.route('/regiones', methods=['GET'])
def getRegiones():
    user = Region.query.all()
    user = list(map(lambda x: x.serialize(), user))
    return jsonify(user),200

@app.route('/regiones', methods=['POST'])
def addRegiones():
    user = Region()
    user.id_region = request.json.get('id_region')
    user.nombre_region = request.json.get('nombre_region')

    Region.save(user)

    return jsonify(user.serialize()),200

@app.route('/regiones/<id_region>', methods=['GET'])
def getRegion(id_region):
    user = Region.query.get(id_region)
    return jsonify(user.serialize()),200

@app.route('/regiones/<id_region>', methods=['DELETE'])
def deleteRegion(id_region):
    user = Region.query.get(id_region)
    Region.delete(user)
    return jsonify(user.serialize()),200

@app.route('/regiones/<id_region>', methods=['PUT'])
def updateRegion(id_region):
    user = Region.query.get(id_region)

    user.id_region = request.json.get('id_region')
    user.nombre_region = request.json.get('nombre_region')

    Region.update(user)

    return jsonify(user.serialize()),200


#Comuna
@app.route('/comunas', methods=['GET'])
def getComunas():
    user = Comuna.query.all()
    user = list(map(lambda x: x.serialize(), user))
    return jsonify(user),200

@app.route('/comunas', methods=['POST'])
def addComunas():
    user = Comuna()
    user.id_comuna = request.json.get('id_comuna')
    user.nombre_comuna = request.json.get('nombre_comuna')
    user.region_id = request.json.get('region_id')

    Comuna.save(user)

    return jsonify(user.serialize()),200

@app.route('/comunas/<id_comuna>', methods=['GET'])
def getComuna(id_comuna):
    user = Comuna.query.get(id_comuna)
    return jsonify(user.serialize()),200

@app.route('/comunas/<id_comuna>', methods=['DELETE'])
def deleteComuna(id_comuna):
    user = Comuna.query.get(id_comuna)
    Comuna.delete(user)
    return jsonify(user.serialize()),200

@app.route('/comunas/<id_comuna>', methods=['PUT'])
def updateComuna(id_comuna):
    user = Comuna.query.get(id_comuna)

    user.id_comuna = request.json.get('id_comuna')
    user.nombre_comuna = request.json.get('nombre_comuna')
    user.region_id = request.json.get('region_id')

    Comuna.update(user)

    return jsonify(user.serialize()),200


# Vendedor
@app.route('/vendedores', methods=['GET'])
def getVendedores():
    user = Vendedor.query.all()
    user = list(map(lambda x: x.serialize(), user))
    return jsonify(user),200

@app.route('/vendedores/<id_vendedor>', methods=['DELETE'])
def deleteVendedor(id_vendedor):
    user = Vendedor.query.get(id_vendedor)
    Vendedor.delete(user)
    return jsonify(user.serialize()),200

@app.route('/vendedores', methods=['POST'])
def addVendedor():
    user = Vendedor()
    user.id_vendedor = request.json.get('id_vendedor')
    user.nombre = request.json.get('nombre')
    Vendedor.save(user)

    return jsonify(user.serialize()),200

@app.route('/vendedores/<id_vendedor>', methods=['GET'])
def getVendedor(id_vendedor):
    user = Vendedor.query.get(id_vendedor)
    return jsonify(user.serialize()),200

@app.route('/vendedores/<id_vendedor>', methods=['PUT'])
def updateVendedor(id_vendedor):
    user = Vendedor.query.get(id_vendedor)

    user.id_vendedor = request.json.get('id_vendedor')
    user.nombre = request.json.get('nombre')

    Vendedor.update(user)

    return jsonify(user.serialize()),200

#Compra

@app.route('/compra', methods=['POST'])
def comprar():

    #Cliente
    cliente = Cliente()
    cliente.id_usuario = request.json.get('id_usuario')
    cliente.rut = request.json.get('rut')
    cliente.dv = request.json.get('dv')
    cliente.primer_nombre = request.json.get('primer_nombre')
    cliente.segundo_nombre = request.json.get('segundo_nombre')
    cliente.primer_apellido = request.json.get('primer_apellido')
    cliente.segundo_apellido = request.json.get('segundo_apellido')
    cliente.direccion = request.json.get('direccion')
    cliente.fono = request.json.get('fono')
    cliente.correo = request.json.get('correo')
    cliente.comuna_id = request.json.get('comuna_id')
    cliente.save()

    #Venta
    
    data = request.values
    userid = data.get('id_usuario')
    voucher = []
    venta = Venta()
    venta.fecha = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    venta.sub_total = request.json.get('sub_total')
    venta.iva = request.json.get('iva')
    venta.total = request.json.get('total')
    venta.estado = 0
    venta.cliente_id = cliente.id_usuario 
    venta.vendedor_id = 1
    venta.despacho_id = 1
    venta.save()

    #Despacho
    
    despacho = Despacho()
    despacho.direccion = request.json.get('direccion')
    despacho.rut_recibe = request.json.get('rut_recibe')
    despacho.nombre_recibe = request.json.get('nombre_recibe')
    despacho.estado_despacho = 0 
    despacho.venta_id = venta.id_venta
    despacho.comuna_id = cliente.comuna_id
    despacho.save()
    venta = Venta.query.filter_by(id_venta=venta.id_venta).first()
    venta.despacho_id = despacho.id_despacho
    venta.save()
    return jsonify(cliente.serialize(), venta.serialize(), despacho.serialize()), 200

# Cliente
@app.route('/clientes', methods=['GET'])
def getClientes():
    user = Cliente.query.all()
    user = list(map(lambda x: x.serialize(), user))
    return jsonify(user),200

@app.route('/clientes/<id_usuario>', methods=['DELETE'])
def deleteCliente(id_usuario):
    user = Cliente.query.get(id_usuario)
    Cliente.delete(user)
    return jsonify(user.serialize()),200

# Venta
@app.route('/ventas', methods=['GET'])
def getVentas():
    user = Venta.query.all()
    user = list(map(lambda x: x.serialize(), user))
    return jsonify(user),200

@app.route('/ventas/<id_venta>', methods=['DELETE'])
def deleteVenta(id_venta):
    user = Venta.query.get(id_venta)
    Venta.delete(user)
    return jsonify(user.serialize()),200

@app.route('/ventas/<id_venta>', methods=['GET'])
def getVenta(id_venta):
    user = Venta.query.get(id_venta)
    return jsonify(user.serialize()),200

#Despacho
@app.route('/despachos', methods=['GET'])
def getDespachos():
    user = Despacho.query.all()
    user = list(map(lambda x: x.serialize(), user))
    return jsonify(user),200

@app.route('/despachos/<id_despacho>', methods=['DELETE'])
def deleteDespacho(id_despacho):
    user = Despacho.query.get(id_despacho)
    Despacho.delete(user)
    return jsonify(user.serialize()),200



# Running the app on port 5000.
if __name__ == '__main__':
    app.run(port=5000, debug=True)