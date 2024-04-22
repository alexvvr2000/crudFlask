from flask import Flask

app: Flask = Flask(__name__)


@app.get("/")
def index():
    return "index"


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
