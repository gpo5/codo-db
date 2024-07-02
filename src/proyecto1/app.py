#importamos el modulo de flask para que funcione el proyecto
from flask import Flask, render_template

#importamos el modulo os para acceder mas facil a los directorios
import os

# importamos para la base de datos
import database as db

#definimos la ruta absoluta del proyecto
template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

#unimos las rutas de las carpetas src y templates a la ruta del proyecto de la línea anterior
template_dir = os.path.join(template_dir, 'src', 'templates')

#indicamos que se busque el archivo index.html (en carpeta templates) al lanzar la aplicación
app = Flask(__name__, template_folder = template_dir)

#A continuación, vamos a generar nuestra primera ruta para poder ejecutar la aplicación.
#Rutas de la aplicación
# @app.route('/') es un decorador que vincula una función con una URL específica del sitio web. En este caso, '/' representa la ruta raíz o homepage del sitio web.

# La función home() que sigue al decorador es la que se ejecutará cuando un usuario visite la página principal (homepage) del sitio. La declaración return render_template('index.html') dentro de esta función indica que Flask debe buscar y renderizar el archivo HTML llamado index.html, que generalmente contiene el contenido que se mostrará en la página principal del sitio web.

# IMPORTANTE: importar en la linea 2 del código el módulo render_template para lanzar la página index.html. Debe quedar asi:
# from flask import Flask, render_template

@app.route('/')
def home():
    return render_template('index.html')

#ejecucion directa de este archivo en modo de desarrollador en el puerto 4000 del localhost o servidor local creado por flask.
if __name__ == '__main__':
    app.run(debug=True, port=4000)