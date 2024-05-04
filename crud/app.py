from flask import Flask, render_template, g
from mariadb import connect, Connection

app: Flask = Flask(__name__)


def obtenerConexion() -> Connection:
    from configparser import ConfigParser
    from typing import Dict

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
def cerrarConexionBase() -> None:
    db = g.pop("db", None)
    if db is not None:
        db.close()


@app.get("/")
def index():
    return render_template("mostrar.jinja", carrito=[])


@app.get("/agregar")
def agregarCarroForm():
    return "agregar"


@app.post("/agregar")
def agregarCarroBase():
    return "agregar"


@app.delete("/borrar")
def borrarCarroBase():
    return "borrar"


@app.get("/actualizar")
def actualizarCarroForm():
    return "actualizar"


@app.put("/actualizar")
def actualizarCarroBase():
    pass
