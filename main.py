from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/inicio_sesion')
def inicio_sesion():
    return render_template('login.html')

@app.route('/maestra')
def maestra():
    return render_template('maestra.html')


@app.route('/prueba')
def prueba():
    return render_template('prueba.html')


if __name__ == "__main__":
    app.run(debug=True)
