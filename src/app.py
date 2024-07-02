from flask import Flask, render_template, request, redirect, url_for

import os

import database as db

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

template_dir = os.path.join(template_dir, 'src', 'templates')

app = Flask(__name__, template_folder = template_dir)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sucursales')
def sucursales():
    return render_template('sucursales.html')

@app.route('/productos')
def productos():
    return render_template('productos.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/clientes')
def clientes():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM usuarios")
    miResultado = cursor.fetchall()
    
    #Convertir los datos a diccionario
    insertarObjectos = [] 
    nombreDeColumnas = [columna[0] for columna in cursor.description]
    
    for unRegistro in miResultado:
        insertarObjectos.append(dict(zip(nombreDeColumnas, unRegistro)))
    
    # Cierra el cursor para liberar recursos de memoria.    
    cursor.close()
    
    return render_template('clientes.html', data=insertarObjectos)

#Ruta para guardar usuarios en la bd
@app.route('/usuario', methods=['POST'])
def addUser():
    nombre = request.form['nombre']
    usuario = request.form['usuario']
    clave = request.form['clave']

    if usuario and nombre and clave:
        cursor = db.database.cursor()
        sql = "INSERT INTO usuarios (nombre, usuario, clave) VALUES (%s, %s, %s)"
        data = (usuario, nombre, clave)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('clientes'))


# Eliminar usuarios de la bd
@app.route('/eliminar/<string:id>', methods=['POST'])
def eliminar(id):
    cursor = db.database.cursor()
    sql = "DELETE FROM usuarios WHERE id=%s"
    data = (id,)
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('clientes'))

# Editar usuarios de la bd

@app.route('/editar/<string:id>', methods=['POST'])
def edit(id):
    nombre = request.form['nombre']
    usuario = request.form['usuario']
    clave = request.form['clave']


    if nombre and usuario and clave:
        cursor = db.database.cursor()
        sql = "UPDATE usuarios SET nombre = %s, usuario = %s, clave = %s WHERE id = %s"
        data = (nombre, usuario, clave, id)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('clientes'))

if __name__ == '__main__':
    app.run(debug=True, port=4000)