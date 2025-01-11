
import controladores
from flask import Flask, render_template, request, redirect, url_for
import controladores.controlador_usuario as cusu
from hashlib import sha256

app = Flask(__name__)

@app.route('/')
@app.route('/inicio_sesion')
def inicio_sesion():
    cusu.listar_usuarios()
    print("fsf")
    return render_template('login.html')

@app.route('/maestra')
def maestra():
    return render_template('maestra.html')


@app.route('/verificar_usuario', methods=["POST"])
def verificar_usuario():
    correo = request.form.get('correo')
    password = request.form.get('password')
    password_cod =  sha256(password.encode('utf-8')).hexdigest()
    try:
        usuario = cusu.verificar_usuario(correo,password)
        if(usuario == False):
            return redirect(url_for('inicio_sesion'))
        else:
            print(usuario)
            return render_template('maestra.html', usuario=usuario)
    except:
       return redirect(url_for('inicio_sesion'))


@app.route('/prueba')
def prueba():
    return render_template('prueba.html')

@app.route('/crear_cuenta')
def crearCuenta():
    return render_template('nuevaCuenta.html')

if __name__ == "__main__":
    app.run(debug=True)
