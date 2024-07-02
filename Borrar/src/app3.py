from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/clientes')
def clientes():
    return render_template('clientes.html')

'''
# Para servir archivos estáticos desde la raíz
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('../static', filename)
'''
    
if __name__ == '__main__':
    app.run(debug=True)