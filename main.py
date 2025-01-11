import os
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import controladores.controlador_usuario

app = Flask(__name__)
app.secret_key = "nada"

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

@app.route('/')
@app.route('/inicio_sesion')
def inicio_sesion():
    controladores.controlador_usuario.listar_usuarios()
    print("fsf")
    return render_template('login.html')

@app.route('/maestra')
def maestra():
    return render_template('maestra.html')


@app.route('/prueba')
def prueba():
    return render_template('prueba.html')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/crear_cuenta', methods=['GET', 'POST'])
def crearCuenta():
    if request.method == 'POST':
        nombre_apellido = request.form.get('nombre_apellido')
        password = request.form.get('password')
        correo = request.form.get('correo')
        tipo_usuario = False  

        if 'imagen' not in request.files:
            flash('Debe seleccionar una imagen.', 'danger')
            return redirect(url_for('crearCuenta'))
        
        file = request.files['imagen']
        if file.filename == '':
            flash('Debe seleccionar un archivo válido.', 'danger')
            return redirect(url_for('crearCuenta'))

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
        else:
            flash('Formato de archivo no permitido. Solo PNG, JPG o JPEG.', 'danger')
            return redirect(url_for('crearCuenta'))
       
        try:
            controladores.controlador_usuario.insertar_usuario(nombre_apellido, tipo_usuario, filepath, password, correo)
            return redirect(url_for('inicio_sesion'))
        except Exception as e:
            flash(f'Error al registrar el usuario: {e}', 'danger')
            return redirect(url_for('crearCuenta'))

    return render_template('nuevaCuenta.html')

if __name__ == "__main__":
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
    
