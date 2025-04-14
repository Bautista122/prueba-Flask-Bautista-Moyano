
from flask import Flask, url_for
import sqlite3


app = Flask(__name__)


def dict_factory(cursor, row):
   """Arma un diccionario con los valores de la fila."""
   fields = [column[0] for column in cursor.description]
   return {key: value for key, value in zip(fields, row)}


def AbrirConexion():
   global db
   db = sqlite3.connect("instance/datos.sqlite")
   db.row_factory = dict_factory


def CerrarConexion():
   global db
   db.close
   db = None


@app.route("/test-db")
def testDB():
   AbrirConexion()
   cursor = db.cursor()
   cursor.execute("SELECT COUNT(*) AS cant FROM usuarios: ")
   res = cursor.fetchone
   registro = res["cant"]
   CerrarConexion()
   return f"Hay {registro} registros en la tabla usuarios"

##sin argumentos
@app.route("/crear-usuario")
def testCrear():
   nombre = "leandro"
   email = "leandro@etec.uba.ar"
   AbrirConexion()
   cursor = db.cursor()
   consulta = "INSERT INTO usuarios(usuario, email) VALUES (?,?)"
   cursor.execute(consulta, (nombre, email))
   db.commit()
   CerrarConexion()
   return f"Registro agregado ({nombre})"

##con ARGUMENTOS
@app.route("/crear-usuario/<string:nombre>/<string:email>")
def testCrear(nombre,email):
   AbrirConexion()
   cursor = db.cursor()
   consulta = "INSERT INTO usuarios(usuario, email) VALUES (?,?)"
   cursor.execute(consulta, (nombre, email))
   db.commit()
   CerrarConexion()
   return f"Registro agregado ({nombre})"


@app.route("/")
def main():
   url_hola = url_for("hello")
   url_dado = url_for("dados", Caras=6)
   url_logo = url_for("static", filename="img/logo.jpg")
   return f"""
   <a href="{url_hola}">Hola</a>
   <br>
   <a href="{url_for("bye")}">Chau</a>
   <br>
   <a href="{url_logo}">Logo</a>
   <br>
   <a href="{url_dado}">Tirar_Dados</a>
   """
@app.route("/hola")
def hello():
   return """
   <p>Hola</p>
   <br>
   <a href="/Chau">Chau</a>
   <br>
   <a href="Chau">Chau2</a>
"""
