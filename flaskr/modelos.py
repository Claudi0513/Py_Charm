from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
import enum

db = SQLAlchemy()


class Cancion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(128))
    minutos = db.Column(db.Integer)
    segundos = db.Column(db.Integer)
    interprete = db.Column(db.String(128))

    def __repr__(self):
        return "{}-{}-{}-{}".format(self.titulo, self.minutos, self.segundos, self.interprete)


class Usuario(db.Model):
    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(128))
    contrasena = db.Column(db.String(128))

    def __repr__(self):
        return "{}-{}".format(self.nombre_usuario, self.contrasena)


class Album(db.Model):
    id_album = db.Column(db.Integer, primary_key=True)
    titulo_album = db.Column(db.String(128))
    anio = db.Column(db.Integer)
    descripcion = db.Column(db.String(128))
    medio = db.Column(db.String(128))

    def __repr__(self):
        return "{}-{}-{}-{}".format(self.titulo_album, self.anio, self.descripcion, self.medio)
