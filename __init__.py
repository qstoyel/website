from flask import Flask, render_template
import os
import sys

from dhtreader.config import data_directory
from dhtreader.get_current_data import get_data

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("home.html")
	
@app.route("/apartment")
def apartment():
	current_data = get_data() #queries db,gets latest point
	temp = float(current_data["temp"])
	hum = float(current_data["hum"])
	return render_template("apartment.html", temp=temp, hum=hum)
	
if __name__ == "__main__":
    app.run(host='0.0.0.0')
	
