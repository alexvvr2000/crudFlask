from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "index"


@app.route("/agregar", methods=["GET", "POST"])
def agregarCarro():
    return "agregar"


@app.route("/borrar", methods=["GET", "DELETE"])
def borrarCarro():
    return "borrar"


@app.route("/actualizar", methods=["GET", "PUT"])
def actualizarCarro():
    return "actualizar"
