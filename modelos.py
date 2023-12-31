from database import db

# Para crear las tablas, desde el entorno de ejecución de Python, ejecutar:
# from database import app, db
# from empleado import Empleado
# app.app_context().push()
# db.create_all()

class Especie(db.Model):
    __tablename__ = 'especies'

    id_especie = db.Column(db.Integer, primary_key=True)
    nombre_especie = db.Column(db.String(255), nullable=False, unique=True)
    descripcion = db.Column(db.String(255))

class Habitat(db.Model):
    __tablename__ = 'habitats'

    id_habitat = db.Column(db.Integer, primary_key=True)
    nombre_habitat = db.Column(db.String(255), nullable=False, unique=True)
    nombre_imagen = db.Column(db.String(255), nullable=False, unique=True)
    imagen_habitat = db.Column(db.BLOB)

class Animal(db.Model):
    __tablename__ = 'animales'

    id_animal = db.Column(db.Integer, primary_key=True)
    nombre_animal = db.Column(db.String(255), nullable=False)
    fecha_nacimiento = db.Column(db.Date)
    edad = db.Column(db.Integer)   
    id_especie = db.Column(db.Integer, db.ForeignKey('especies.id_especie'), nullable=False)
    id_habitat = db.Column(db.Integer, db.ForeignKey('habitats.id_habitat'))
    nombre_Imagen = db.Column(db.String(255), nullable=False, unique=True)
    imagen = db.Column(db.BLOB)
    especie = db.relationship('Especie', backref='animales')
    habitat = db.relationship('Habitat', backref='animales')

    def __init__(self, nombre_animal, fecha_nacimiento, edad, id_especie, nombre_Imagen, imagen, id_habitat=None):
        self.nombre_animal = nombre_animal
        self.fecha_nacimiento = fecha_nacimiento
        self.edad = edad        
        self.id_especie = id_especie
        self.id_habitat = id_habitat
        self.nombre_Imagen = nombre_Imagen
        self.imagen = imagen

    def __repr__(self):
        return f'<Animal {self.id_animal}>: {self.nombre_animal}, {self.fecha_nacimiento}, {self.edad} años'