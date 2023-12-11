from flask import Flask, render_template, request, redirect , url_for, flash

app = Flask(__name__)

from database import app, db, AnimalSchema,EspecieSchema,HabitatSchema
from modelos import Animal,Especie,Habitat

animal_schema = AnimalSchema()
animales_schema = AnimalSchema(many=True)

@app.route('/')
def index():
    todosAnimales = Animal.query.all()
    return render_template('index.html', animales=todosAnimales)

@app.route('/insertar', methods=['POST'])
def insertar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        fecha_nacimiento = request.form['fecha_nacimiento']
        edad = request.form['edad']
        imagen = request.form['imagen']
        id_especie = request.form['id_especie']
        id_habitat = request.form['id_habitat']

        animal = Animal(nombre, fecha_nacimiento, edad, imagen, id_especie, id_habitat)
        db.session.add(animal)
        db.session.commit()

        flash('Animal añadido correctamente')
        return redirect(url_for('index'))

@app.route('/editar', methods=['GET', 'POST'])
def editar():
    if request.method == 'POST':
        animal = Animal.query.get(request.form.get('id'))
        animal.nombre = request.form['nombre']
        animal.fecha_nacimiento = request.form['fecha_nacimiento']
        animal.edad = request.form['edad']
        animal.imagen = request.form['imagen']
        animal.id_especie = request.form['id_especie']
        animal.id_habitat = request.form['id_habitat']

        db.session.commit()
        flash('Animal actualizado correctamente')
        return redirect(url_for('index'))

@app.route('/eliminar/<id>', methods=['GET', 'POST'])
def eliminar(id):
    animal = Animal.query.get(id)
    db.session.delete(animal)
    db.session.commit()
    flash('Animal eliminado correctamente')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)