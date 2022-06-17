from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Descuento, Producto, Region, Descuento_Producto, Comuna, Cliente, Vendedor, Suscripcion, Donacion
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Conten-Type'
app.url_map.strict_slashes = False
app.config['DEBUG'] = False
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

Migrate(app, db)

"""
@app.route('/')
def index():
    return 'Hola'
"""

# Descuentos
@app.route('/descuentos', methods=['GET'])
def getDescuentos():
    user = Descuento.query.all()
    user = list(map(lambda x: x.serialize(), user))
    return jsonify(user),200

@app.route('/descuentos', methods=['POST'])
def addDescuentos():
    user = Descuento()
    user.id_descuento = request.json.get('id_descuento')
    user.nombre = request.json.get('nombre')
    user.fecha = request.json.get('fecha')
    user.porcentaje = request.json.get('porcentaje')
    user.estado = request.json.get('estado')

    Descuento.save(user)

    return jsonify(user.serialize()),200

@app.route('/descuentos/<id_descuento>', methods=['GET'])
def getDescuento(id_descuento):
    user = Descuento.query.get(id_descuento)
    return jsonify(user.serialize()),200

@app.route('/descuentos/<id_descuento>', methods=['DELETE'])
def deleteDescuento(id_descuento):
    user = Descuento.query.get(id_descuento)
    Descuento.delete(user)
    return jsonify(user.serialize()),200

@app.route('/descuentos/<id_descuento>', methods=['PUT'])
def updateDescuento(id_descuento):
    user = Descuento.query.get(id_descuento)

    user.id_descuento = request.json.get('id_descuento')
    user.nombre = request.json.get('nombre')
    user.fecha = request.json.get('fecha')
    user.porcentaje = request.json.get('porcentaje')
    user.estado = request.json.get('estado')
    
    Descuento.update(user)

    return jsonify(user.serialize()),200

# Productos
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

# Descuento_Producto
@app.route('/descuento_producto', methods=['GET'])
def getDescuentos_Productos():
    user = Descuento_Producto.query.all()
    user = list(map(lambda x: x.serialize(), user))
    return jsonify(user),200

@app.route('/descuento_producto', methods=['POST'])
def addDescuento_producto():
    user = Descuento_Producto()
    user.descuento_producto_id = request.json.get('descuento_producto_id')
    user.producto_id = request.json.get('producto_id')
    user.descuento_id = request.json.get('descuento_id')
    user.fecha_inicio = request.json.get('fecha_inicio')
    user.fecha_termino = request.json.get('fecha_termino')

    Descuento_Producto.save(user)

    return jsonify(user.serialize()),200
@app.route('/descuento_producto/<descuento_producto_id>', methods=['GET'])
def getDescuento_Producto(descuento_producto_id):
    user = Descuento_Producto.query.get(descuento_producto_id)
    return jsonify(user.serialize()),200

@app.route('/descuento_producto/<descuento_producto_id>', methods=['DELETE'])
def deleteDescuento_Producto(descuento_producto_id):
    user = Descuento_Producto.query.get(descuento_producto_id)
    Descuento_Producto.delete(user)
    return jsonify(user.serialize()),200

@app.route('/descuento_producto/<descuento_producto_id>', methods=['PUT'])
def updateDescuento_Producto(descuento_producto_id):
    user = Descuento_Producto.query.get(descuento_producto_id)

    user.descuento_producto_id = request.json.get('descuento_producto_id')
    user.producto_id = request.json.get('producto_id')
    user.descuento_id = request.json.get('descuento_id')
    user.fecha_inicio = request.json.get('fecha_inicio')
    user.fecha_termino = request.json.get('fecha_termino')

    Descuento_Producto.update(user)

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

@app.route('/clientes', methods=['POST'])
def addCliente():
    user = Cliente()
    user.id_usuario = request.json.get('id_usuario')
    user.rut = request.json.get('rut')
    user.dv = request.json.get('dv')
    user.primer_nombre = request.json.get('primer_nombre')
    user.segundo_nombre = request.json.get('segundo_nombre')
    user.primer_apellido = request.json.get('primer_apellido')
    user.segundo_apellido = request.json.get('segundo_apellido')
    user.direccion = request.json.get('direccion')
    user.fono = request.json.get('fono')
    user.correo = request.json.get('correo')
    user.estado = request.json.get('estado')
    user.comuna_id = request.json.get('comuna_id')
    user.region_id = request.json.get('region_id')

    Cliente.save(user)

    return jsonify(user.serialize()),200

@app.route('/clientes/<id_usuario>', methods=['GET'])
def getCliente(id_usuario):
    user = Cliente.query.get(id_usuario)
    return jsonify(user.serialize()),200

@app.route('/clientes/<id_usuario>', methods=['PUT'])
def updateCliente(id_usuario):
    user = Cliente.query.get(id_usuario)

    user.id_usuario = request.json.get('id_usuario')
    user.rut = request.json.get('rut')
    user.dv = request.json.get('dv')
    user.primer_nombre = request.json.get('primer_nombre')
    user.segundo_nombre = request.json.get('segundo_nombre')
    user.primer_apellido = request.json.get('primer_apellido')
    user.segundo_apellido = request.json.get('segundo_apellido')
    user.direccion = request.json.get('direccion')
    user.fono = request.json.get('fono')
    user.correo = request.json.get('correo')
    user.estado = request.json.get('estado')
    user.comuna_id = request.json.get('comuna_id')
    user.region_id = request.json.get('region_id')

    Cliente.update(user)

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
    user.rut = request.json.get('rut')
    user.dv = request.json.get('dv')
    user.primer_nombre = request.json.get('primer_nombre')
    user.segundo_nombre = request.json.get('segundo_nombre')
    user.primer_apellido = request.json.get('primer_apellido')
    user.segundo_apellido = request.json.get('segundo_apellido')
    user.direccion = request.json.get('direccion')
    user.fono = request.json.get('fono')
    user.correo = request.json.get('correo')
    user.estado = request.json.get('estado')
    user.comuna_id = request.json.get('comuna_id')
    user.region_id = request.json.get('region_id')

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
    user.rut = request.json.get('rut')
    user.dv = request.json.get('dv')
    user.primer_nombre = request.json.get('primer_nombre')
    user.segundo_nombre = request.json.get('segundo_nombre')
    user.primer_apellido = request.json.get('primer_apellido')
    user.segundo_apellido = request.json.get('segundo_apellido')
    user.direccion = request.json.get('direccion')
    user.fono = request.json.get('fono')
    user.correo = request.json.get('correo')
    user.estado = request.json.get('estado')
    user.comuna_id = request.json.get('comuna_id')
    user.region_id = request.json.get('region_id')

    Vendedor.update(user)

    return jsonify(user.serialize()),200

# Suscripcion
@app.route('/suscripciones', methods=['GET'])
def getSuscripciones():
    user = Suscripcion.query.all()
    user = list(map(lambda x: x.serialize(), user))
    return jsonify(user),200

@app.route('/suscripciones', methods=['POST'])
def addSuscripcion():
    user = Suscripcion()
    user.id_suscripcion = request.json.get('id_suscripcion')
    user.fecha_inicio = request.json.get('fecha_inicio')
    user.fecha_termino = request.json.get('fecha_termino')
    user.cliente_id = request.json.get('cliente_id')

    Suscripcion.save(user)

    return jsonify(user.serialize()),200
@app.route('/suscripciones/<id_suscripcion>', methods=['GET'])
def getSuscripcion(id_suscripcion):
    user = Suscripcion.query.get(id_suscripcion)
    return jsonify(user.serialize()),200

@app.route('/suscripciones/<id_suscripcion>', methods=['DELETE'])
def deleteSuscripcion(id_suscripcion):
    user = Suscripcion.query.get(id_suscripcion)
    Suscripcion.delete(user)
    return jsonify(user.serialize()),200

@app.route('/suscripciones/<id_suscripcion>', methods=['PUT'])
def updateSuscripcion(id_suscripcion):
    user = Suscripcion.query.get(id_suscripcion)

    user.id_suscripcion = request.json.get('id_suscripcion')
    user.fecha_inicio = request.json.get('fecha_inicio')
    user.fecha_termino = request.json.get('fecha_termino')
    user.cliente_id = request.json.get('cliente_id')

    Suscripcion.update(user)

    return jsonify(user.serialize()),200

# Donacion
@app.route('/donaciones', methods=['GET'])
def getDonaciones():
    user = Donacion.query.all()
    user = list(map(lambda x: x.serialize(), user))
    return jsonify(user),200

@app.route('/donaciones', methods=['POST'])
def addDonacion():
    user = Donacion()
    user.id_donacion = request.json.get('id_donacion')
    user.valor = request.json.get('valor')
    user.fecha = request.json.get('fecha')
    user.cliente_id = request.json.get('cliente_id')

    Donacion.save(user)

    return jsonify(user.serialize()),200

@app.route('/donaciones/<id_donacion>', methods=['GET'])
def getDonacion(id_donacion):
    user = Donacion.query.get(id_donacion)
    return jsonify(user.serialize()),200

@app.route('/donaciones/<id_donacion>', methods=['DELETE'])
def deleteDonacion(id_donacion):
    user = Donacion.query.get(id_donacion)
    Donacion.delete(user)
    return jsonify(user.serialize()),200

@app.route('/donaciones/<id_donacion>', methods=['PUT'])
def updateDonacion(id_donacion):
    user = Donacion.query.get(id_donacion)

    user.id_donacion = request.json.get('id_donacion')
    user.valor = request.json.get('valor')
    user.fecha = request.json.get('fecha')
    user.cliente_id = request.json.get('cliente_id')

    Donacion.update(user)

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

@app.route('/ventas', methods=['POST'])
def addVenta():
    user = Venta()

    user.id_venta = request.json.get('id_venta')
    user.fecha = request.json.get('fecha')
    user.descuento = request.json.get('descuento')
    user.sub_total = request.json.get('sub_total')
    user.iva = request.json.get('iva')
    user.total = request.json.get('total')
    user.estado = request.json.get('estado')
    user.cliente_id = request.json.get('cliente_id')
    user.vendedor_id = request.json.get('vendedor_id')
    user.despacho_id = request.json.get('despacho_id')

    Venta.save(user)

    return jsonify(user.serialize()),200

@app.route('/ventas/<id_venta>', methods=['GET'])
def getVenta(id_venta):
    user = Venta.query.get(id_venta)
    return jsonify(user.serialize()),200

@app.route('/ventas/<id_venta>', methods=['PUT'])
def updateVenta(id_venta):
    user = Venta.query.get(id_venta)

    user.id_venta = request.json.get('id_venta')
    user.fecha = request.json.get('fecha')
    user.descuento = request.json.get('descuento')
    user.sub_total = request.json.get('sub_total')
    user.iva = request.json.get('iva')
    user.total = request.json.get('total')
    user.estado = request.json.get('estado')
    user.cliente_id = request.json.get('cliente_id')
    user.vendedor_id = request.json.get('vendedor_id')
    user.despacho_id = request.json.get('despacho_id')

    Venta.update(user)

    return jsonify(user.serialize()),200

# Despacho
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

@app.route('/despachos', methods=['POST'])
def addDespacho():
    user = Despacho()

    user.id_despacho = request.json.get('id_despacho')
    user.direccion = request.json.get('direccion')
    user.fecha_entrega = request.json.get('fecha_entrega')
    user.hora_entrega = request.json.get('hora_entrega')
    user.rut_recibe = request.json.get('rut_recibe')
    user.nombre_recibe = request.json.get('nombre_recibe')
    user.estado_despacho = request.json.get('estado_despacho')
    user.venta_id = request.json.get('venta_id')
    user.comuna_ida = request.json.get('comuna_ida')
    user.region_id = request.json.get('region_id')

    Despacho.save(user)

    return jsonify(user.serialize()),200

@app.route('/despachos/<id_despacho>', methods=['GET'])
def getDespacho(id_despacho):
    user = Despacho.query.get(id_despacho)
    return jsonify(user.serialize()),200

@app.route('/despachos/<id_despacho>', methods=['PUT'])
def updateDespacho(id_despacho):
    user = Despacho.query.get(id_despacho)

    user.id_venta = request.json.get('id_venta')
    user.fecha = request.json.get('fecha')
    user.descuento = request.json.get('descuento')
    user.sub_total = request.json.get('sub_total')
    user.iva = request.json.get('iva')
    user.total = request.json.get('total')
    user.estado = request.json.get('estado')
    user.cliente_id = request.json.get('cliente_id')
    user.vendedor_id = request.json.get('vendedor_id')
    user.despacho_id = request.json.get('despacho_id')

    Despacho.update(user)

    return jsonify(user.serialize()),200


if __name__ == '__main__':
    app.run(port=5000, debug=True)  