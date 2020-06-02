from flask import Flask, render_template
from DHT22_reader.get_data import get_data
import os
import sys
import shutil

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("home.html")
	
@app.route("/apartment")
def apartment():
	#empties /tmp
	shutil.rmtree('static/tmp')
	os.mkdir('static/tmp')
	current_data = get_data() #queries db, generates plots
	temp = float(current_data["temp"])
	hum = float(current_data["hum"])
	return render_template("apartment.html", temp=temp, hum=hum)
	
@app.route("/DHT22_reader/tmp/")
def get_tmp_path():
	return "this has to be a string"

	
