from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("home.html")
	
@app.route("/apartment")
def apartment():
	return render_template("apartment.html")
	
