from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy() 

class Descuento(db.Model):
    __tablename__ = 'Descuento' 
    id_descuento = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    fecha = db.Column(db.Integer, nullable=False)
    porcentaje= db.Column(db.Integer, nullable=False)
    estado = db.Column(db.Integer, nullable=False)

    def serialize(self):

        return{
            "id_descuento": self.id_descuento,
            "nombre": self.nombre,
            "fecha": self.fecha,
            "porcentaje": self.porcentaje,
            "estado": self.estado
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Producto(db.Model):
    __tablename__ = 'Producto' 
    id_producto = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(250), nullable=False)
    nombre = db.Column(db.String(250), nullable=False)
    valor_venta= db.Column(db.Integer, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    descripcion = db.Column(db.String(250), nullable=False)
    imagen = db.Column(db.String(250), nullable=True)
    estado = db.Column(db.String(1), nullable=False)

    def serialize(self):

        return{
            "id_producto": self.id_producto,
            "codigo": self.codigo,
            "nombre": self.nombre,
            "valor_venta": self.valor_venta,
            "stock": self.stock,
            "descripcion": self.descripcion,
            "imagen": self.imagen,
            "estado": self.estado
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Region(db.Model):
    __tablename__ = 'Region'
    id_region = db.Column(db.Integer, primary_key=True)
    nombre_region = db.Column(db.String(250), nullable= False)

    def serialize(self):
        return{
            "id_region": self.id_region,
            "nombre_region": self.nombre_region
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Descuento_Producto(db.Model):
    __tablename__ = 'Descuento_Producto' 
    descuento_producto_id = db.Column(db.Integer, primary_key=True) 
    producto_id = db.Column(db.Integer,  nullable=False)
    descuento_id = db.Column(db.Integer,  nullable=False)
    fecha_inicio = db.Column(db.Integer, nullable=False)
    fecha_termino = db.Column(db.Integer, nullable=False)

    def serialize(self):

        return{
            "descuento_producto_id": self.descuento_producto_id,
            "producto_id": self.producto_id,
            "descuento_id": self.descuento_id,
            "fecha_inicio": self.fecha_inicio,
            "fecha_termino": self.fecha_termino
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Comuna(db.Model):
    __tablename__ = 'Comuna'
    id_comuna = db.Column(db.Integer, primary_key=True)
    nombre_comuna = db.Column(db.String(250), nullable= False)
    region_id = db.Column(db.Integer, nullable= False)

    def serialize(self):
        return{
            "id_comuna": self.id_comuna,
            "nombre_comuna": self.nombre_comuna, 
            "region_id": self.region_id
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Cliente(db.Model):
    __tablename__ = 'Cliente' 
    id_usuario = db.Column(db.Integer, primary_key=True)
    rut = db.Column(db.Integer, nullable=False)
    dv = db.Column(db.String(1), nullable=False)
    primer_nombre= db.Column(db.String(250), nullable=False)
    segundo_nombre = db.Column(db.String(250), nullable=True)
    primer_apellido = db.Column(db.String(250), nullable=False)
    segundo_apellido = db.Column(db.String(250), nullable=True)
    direccion = db.Column(db.String(250), nullable=False)
    fono = db.Column(db.Integer, nullable=False)
    correo = db.Column(db.String(250), nullable=False)
    comuna_id = db.Column(db.Integer, nullable=False)
    region_id = db.Column(db.Integer, nullable=False)
    clave = db.Column(db.String(15), nullable=False)
    def serialize(self):

        return{
            "id_usuario": self.id_usuario,
            "rut": self.rut,
            "dv": self.dv,
            "primer_nombre": self.primer_nombre,
            "segundo_nombre": self.segundo_nombre,
            "primer_apellido": self.primer_apellido,
            "segundo_apellido": self.segundo_apellido,
            "direccion": self.direccion, 
            "fono": self.fono,
            "correo": self.correo,
            "comuna_id": self.comuna_id,
            "region_id": self.region_id,
            "clave": self.clave 
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Vendedor(db.Model):

    __tablename__ = 'Vendedor' 
    id_vendedor = db.Column(db.Integer, primary_key=True)
    rut = db.Column(db.Integer, nullable=False)
    dv = db.Column(db.String(1), nullable=False)
    primer_nombre= db.Column(db.String(250), nullable=False)
    segundo_nombre = db.Column(db.String(250), nullable=True)
    primer_apellido = db.Column(db.String(250), nullable=False)
    segundo_apellido = db.Column(db.String(250), nullable=True)
    direccion = db.Column(db.String(250), nullable=False)
    fono = db.Column(db.Integer, nullable=False)
    correo = db.Column(db.String(250), nullable=False)
    estado = db.Column(db.String(1), nullable=False)
    comuna_id = db.Column(db.Integer, nullable=False)
    region_id = db.Column(db.Integer, nullable=False)

    def serialize(self):

        return{
            "id_vendedor": self.id_vendedor,
            "rut": self.rut,
            "dv": self.dv,
            "primer_nombre": self.primer_nombre,
            "segundo_nombre": self.segundo_nombre,
            "primer_apellido": self.primer_apellido,
            "segundo_apellido": self.segundo_apellido,
            "direccion": self.direccion, 
            "fono": self.fono,
            "correo": self.correo,
            "estado": self.estado,
            "comuna_id": self.comuna_id,
            "region_id": self.region_id
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Suscripcion(db.Model):
    __tablename__ = 'Suscripcion' 
    id_suscripcion = db.Column(db.Integer, primary_key=True) 
    fecha_inicio = db.Column(db.Integer, nullable=False)
    fecha_termino = db.Column(db.Integer, nullable=False)
    cliente_id = db.Column(db.Integer,  nullable=False)

    def serialize(self):

        return{
            "id_suscripcion": self.id_suscripcion,
            "fecha_inicio": self.fecha_inicio,
            "fecha_termino": self.fecha_termino,
            "cliente_id": self.cliente_id
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Donacion(db.Model):
    __tablename__ = 'Donacion' 
    id_donacion = db.Column(db.Integer, primary_key=True) 
    valor = db.Column(db.Integer, nullable=False)
    fecha = db.Column(db.Integer, nullable=False)
    cliente_id = db.Column(db.Integer,  nullable=False)

    def serialize(self):

        return{
            "id_donacion": self.id_donacion,
            "valor": self.valor,
            "fecha": self.fecha,
            "cliente_id": self.cliente_id
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()       

class Despacho(db.Model):
    __tablename__ = 'Despacho' 
    id_despacho = db.Column(db.Integer, primary_key=True)
    direccion = db.Column(db.String(250), nullable=False)
    fecha_entrega = db.Column(db.Integer, nullable=True)
    hora_entrega= db.Column(db.Integer, nullable=True)
    rut_recibe = db.Column(db.Integer, nullable=True)
    nombre_recibe = db.Column(db.Integer, nullable=True)
    estado_despacho = db.Column(db.Integer, nullable=False)
    venta_id = db.Column(db.Integer, nullable=False)
    comuna_ida = db.Column(db.Integer, nullable=False)
    region_id = db.Column(db.Integer, nullable=False)

    def serialize(self):

        return{
            "id_despacho": self.id_despacho,
            "direccion": self.direccion,
            "fecha_entrega": self.fecha_entrega,
            "hora_entrega": self.hora_entrega,
            "rut_recibe": self.rut_recibe,
            "nombre_recibe": self.nombre_recibe,
            "estado_despacho": self.estado_despacho,
            "venta_id": self.venta_id, 
            "comuna_ida": self.comuna_ida,
            "region_id": self.region_id
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Venta(db.Model):
    __tablename__ = 'Venta' 
    id_venta = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Integer, nullable=False)
    descuento = db.Column(db.Integer, nullable=True)
    sub_total= db.Column(db.Integer, nullable=False)
    iva = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Integer, nullable=False)
    estado = db.Column(db.String(1), nullable=False)
    cliente_id = db.Column(db.Integer, nullable=False)
    vendedor_id = db.Column(db.Integer, nullable=False)
    despacho_id = db.Column(db.Integer, nullable=False)

    def serialize(self):

        return{
            "id_venta": self.id_venta,
            "fecha": self.fecha,
            "descuento": self.descuento,
            "sub_total": self.sub_total,
            "iva": self.iva,
            "total": self.total,
            "estado": self.estado,
            "cliente_id": self.cliente_id, 
            "vendedor_id": self.vendedor_id,
            "despacho_id": self.despacho_id
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
