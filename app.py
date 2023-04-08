from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def menu():
    return render_template('menu.html')
@app.route("/juego")
def juego():
    return render_template('juego.html')
@app.route("/juego/submitquiz", methods = ["POST","GET"])
def submit():
    value = request.form["option"]
    return value
@app.route("/results", methods = ["POST","GET"])
def results():
    return render_template('results.html')

