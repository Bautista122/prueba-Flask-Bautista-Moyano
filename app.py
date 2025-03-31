from flask import Flask

app = Flask(__name__)

@app.route("/boca")
def boca():
    return "<p>Aguante Boca</p>"

@app.route("/river")
def river():
    return "<p>Aguante River</p>"    