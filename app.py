from flask import Flask, render_template
from DHT22_reader.get_data import get_data


app = Flask(__name__)

@app.route("/")
def index():
	return render_template("home.html")
	
@app.route("/apartment")
def apartment():
	get_data() #queries db, generates plots
	return render_template("apartment.html")
	

def clean_data():
	return True

clean_data() #empties tmp file
	
