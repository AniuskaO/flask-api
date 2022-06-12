from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'Usuario'
    id = db.Column(db.Integer, primary_key=True)
    rut = db.Column(db.Integer, nullable=False)
    dv = db.Column(db.String(1), nullable=False)
    primer_nombre = db.Column(db.String(250), nullable=False)
    segundo_nombre = db.Column(db.String(250), nullable=True)
    primer_apellido = db.Column(db.String(250), nullable=False)
    segundo_apellido = db.Column(db.String(250), nullable=True)
    direccion = db.Column(db.String(250), nullable=False)
    fono = db.Column(db.Integer, nullable=False)
    correo = db.Column(db.String(250), nullable=False)
    estado = db.Column(db.String(1), nullable=False)
    id_comuna = db.Column(db.Integer, db.ForeignKey(Comuna.id_comuna))
    id_region = db.Column(db.Integer, db.ForeignKey(Region.id_region))

    def serialize(self):

        return{
            "id": self.id,
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
            "id_comuna": self.id_comuna, 
            "id_region": self.id_region

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
    nombre = db.Column(db.String(250), nullable=False)

    def serialize(self):

        return{
            "id_region": self.id_region,
            "nombre": self.nombre
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

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

class Suscripcion(db.Model):
    __tablename__ = 'Suscripcion'
    id_suscripcion = db.Column(db.Integer, primary_key=True)
    fecha_inicico = db.Column(db.Integer, nullable=False)
    fecha_termino = db.Column(db.Integer, nullable=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey(Usuario.id))
    estado = db.Column(db.Integer, nullable=False)

    def serialize(self):

        return{
            "id_suscripcion": self.id_suscripcion,
            "fecha_inicico": self.fecha_inicico,
            "fecha_termino": self.fecha_termino,
            "cliente_id": self.cliente_id,
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


class Donacion(db.Model):
    __tablename__ = 'Donacion'
    id_donacion = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Integer, nullable=False)
    fecha = db.Column(db.Integer, nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey(Usuario.id))

    def serialize(self):

        return{
            "id_donacion": self.id_donacion,
            "valor": self.valor,
            "fecha": self.fecha,
            "porcentaje": self.porcentaje,
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

class Comuna(db.Model):
    __tablename__ = 'Comuna'
    id_comuna = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False)
    id_region = db.Column(db.Integer, db.ForeignKey(Region.id_region))

    def serialize(self):

        return{
            "id_comuna": self.id_comuna,
            "nombre": self.nombre,
            "id_region": self.id_region
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
    primer_nombre = db.Column(db.String(250), nullable=False)
    segundo_nombre = db.Column(db.String(250), nullable=True)
    primer_apellido = db.Column(db.String(250), nullable=False)
    segundo_apellido = db.Column(db.String(250), nullable=True)
    direccion = db.Column(db.String(250), nullable=False)
    fono = db.Column(db.Integer, nullable=False)
    correo = db.Column(db.String(250), nullable=False)
    estado = db.Column(db.String(1), nullable=False)
    id_comuna = db.Column(db.Integer, db.ForeignKey(Comuna.id_comuna))
    id_region = db.Column(db.Integer, db.ForeignKey(Region.id_region))

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
            "id_comuna": self.id_comuna, 
            "id_region": self.id_region

        }


