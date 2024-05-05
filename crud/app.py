from flask import Flask, render_template, g, request, redirect, url_for
from mariadb import Cursor, connect, Connection
from typing import Dict

app: Flask = Flask(__name__)


def obtenerConexion() -> Connection:
    from configparser import ConfigParser

    if "db" not in g:
        lectorDatosConexion: ConfigParser = ConfigParser()
        lectorDatosConexion.read("conn.ini")
        datosConexion: Dict[str, str] = lectorDatosConexion["connection"]
        g.db = connect(
            user=datosConexion["user"],
            password=datosConexion["password"],
            host=datosConexion["host"],
            database=datosConexion["database"],
            port=int(datosConexion["port"]),
        )
    return g.db


@app.teardown_appcontext
def cerrarConexionBase(error) -> None:
    db = g.pop("db", None)
    if db is not None:
        db.close()


@app.get("/")
def index():
    carritoBase: list[Dict[str, str]] = []
    conexionBase: Connection = obtenerConexion()
    cursorBase: Cursor = conexionBase.cursor()
    cursorBase.execute("select claveProducto, descripcion, precio from Producto")
    # iterar y agregar diccionario con los datos regresados
    for producto in cursorBase:
        claveProducto, descripcion, precio = producto
        carritoBase.append(
            {
                "claveProducto": claveProducto,
                "descripcion": descripcion,
                "precio": precio,
            }
        )
    return render_template("mostrar.jinja", carrito=carritoBase)


@app.route("/agregar", methods=["GET", "POST"])
def agregarCarroForm():
    if request.method == "GET":
        return render_template("agregar.jinja")
    elif request.method == "POST":
        return redirect(url_for("index"))


@app.route("/borrar", methods=["DELETE"])
def borrarCarroBase():
    pass


@app.route("/actualizar", methods=["PUT", "GET"])
def actualizarCarroForm():
    if request.method == "GET":
        return render_template("actualizar.jinja")
    elif request.method == "PUT":
        return redirect(url_for("index"))
