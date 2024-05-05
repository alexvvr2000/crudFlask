from flask import Flask, render_template, g, request, redirect, url_for
from mariadb import Cursor, connect, Connection
from typing import Dict, Tuple
from markupsafe import escape

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
        conexionBase: Connection = obtenerConexion()
        cursorBase: Cursor = conexionBase.cursor()
        query = "INSERT INTO Producto (descripcion, precio) values (?,?)"
        datos: Tuple[str, str] = (
            escape(request.form["descripcion"]),
            escape(request.form["precio"]),
        )
        cursorBase.execute(query, datos)
        conexionBase.commit()
        return redirect(url_for("index"))


@app.route("/borrar", methods=["DELETE"])
def borrarCarroBase():
    pass


@app.route("/actualizar/<int:claveProducto>", methods=["PUT", "GET"])
def actualizarCarroForm(claveProducto: int):
    conexionBase: Connection = obtenerConexion()
    cursorBase: Cursor = conexionBase.cursor()
    if request.method == "GET":
        cursorBase.execute(
            "SELECT descripcion, precio FROM Producto WHERE claveProducto=?",
            (claveProducto,),
        )
        descripcion, precio = cursorBase.fetchone()
        datosTemplate: Dict[str, str] = {
            "claveProducto": claveProducto,
            "descripcion": descripcion,
            "precio": precio,
        }
        return render_template("actualizar.jinja", campo=datosTemplate)
    elif request.method == "PUT":
        query: str = "UPDATE Producto SET descripcion=?,precio=? WHERE claveProducto=?"
        cursorBase.execute(
            query,
            (
                escape(request.form["descripcion"]),
                escape(request.form["precio"]),
                claveProducto,
            ),
        )
        conexionBase.commit()
        return "Datos actualizados en base"
