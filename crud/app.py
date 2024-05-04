from flask import Flask, render_template
from mariadb import connect, Connection

app: Flask = Flask(__name__)


def obtenerConexion() -> Connection:
    from configparser import ConfigParser
    from typing import Dict

    lectorDatosConexion: ConfigParser = ConfigParser()
    conexion: Connection
    try:
        lectorDatosConexion.read("conn.ini")
        datosConexion: Dict[str, str] = lectorDatosConexion["connection"]
        conexion = connect(
            user=datosConexion["user"],
            password=datosConexion["password"],
            host=datosConexion["host"],
            database=datosConexion["database"],
            port=int(datosConexion["port"]),
        )
        return conexion
    except Exception as e:
        print(e)


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
