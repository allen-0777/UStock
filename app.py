from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html") 

@app.route("/templates/index.html")
def index():
    return render_template("index.html")

@app.route("/templates/charts.html")
def charts():
    return render_template("charts.html")

app.run()