from flask import Flask, render_template
import controladores
import controladores.controlador_usuario

app = Flask(__name__)

@app.route('/')
@app.route('/inicio_sesion')
def inicio_sesion():
    controladores.controlador_usuario.listar_usuarios()
    return render_template('login.html')

@app.route('/maestra')
def maestra():
    return render_template('maestra.html')


@app.route('/prueba')
def prueba():
    return render_template('prueba.html')

@app.route('/crear_cuenta')
def crearCuenta():
    return render_template('nuevaCuenta.html')

if __name__ == "__main__":
    app.run(debug=True)
