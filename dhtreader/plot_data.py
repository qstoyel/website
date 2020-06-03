import sqlite3
import sys
import os
import pandas as pd
import datetime
import matplotlib.pyplot as plt
from config import data_directory, db_filename, timestamp_format


db_filename = data_directory + "apartment.db"
tmp_directory = data_directory +"tmp/"

def plot_data():
	#queries db
	con = sqlite3.connect(db_filename)
	data = pd.read_sql_query("SELECT * FROM apartment", con)
	con.close()
	data["timestamp"] = data["timestamp"].apply(string_to_datetime)
	now = datetime.datetime.now()
	hour_ago = now - datetime.timedelta(hours=1)
	day_ago = now - datetime.timedelta(days=1)
	week_ago = now - datetime.timedelta(days = 7)
	#make and save plots
	save_data_to_fig(data[data["timestamp"] > hour_ago], "hour")
	save_data_to_fig(data[data["timestamp"] > day_ago], "day")
	save_data_to_fig(data[data["timestamp"] > week_ago], "week")	
	return

def save_data_to_fig(data, n):
	plt.figure(figsize=(12,6))
	plt.plot(data["timestamp"], data["hum"])
	plt.title("Humidity")
	plt.ylabel("Humidity (%)")
	plt.xlabel("Time")
	plot_file = tmp_directory+"hum_"+n+".png"
	if os.path.isfile(plot_file):
		os.remove(plot_file) 
	plt.savefig(plot_file)
	plt.figure(figsize=(12,6))
	plt.plot(data["timestamp"], data["temp"])
	plt.title("Temperature")
	plt.xlabel("Time")
	plt.ylabel("Temperature (C)")
	plot_file = tmp_directory+"temp_"+n +".png"
	if os.path.isfile(plot_file):
		os.remove(plot_file) 
	plt.savefig(plot_file)

def string_to_datetime(timestr):
		return datetime.datetime.strptime(timestr, timestamp_format)
		
		
plot_data()
