from flask import Flask

app = Flask(__name__)

@app.route("/boca")
def boca():
    return "<p>Aguante Boca</p>"

@app.route("/river")
def river():
    return "<p>Aguante River</p>"   

@app.route("/tirar-dado<int:caras")
def caras():
    from random import randint
    n = randint(1,caras)
    return f"<p>Tire un dado de {caras} caras, slaio {n}</p>"   
