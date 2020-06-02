import sqlite3
import sys
import pandas as pd
import datetime
import matplotlib.pyplot as plt



db_filename = "./DHT22_reader/apartment.db"
def get_data():
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
	return data[-1:]

def save_data_to_fig(data, n):
	plt.figure(figsize=(12,6))
	plt.plot(data["timestamp"], data["hum"])
	plt.title("Humidity")
	plt.ylabel("Humidity (%)")
	plt.xlabel("Time")
	plt.savefig("./static/tmp/hum_"+n+".png")
	plt.figure(figsize=(12,6))
	plt.plot(data["timestamp"], data["temp"])
	plt.title("Temperature")
	plt.xlabel("Time")
	plt.ylabel("Temperature (C)")
	plt.savefig("./static/tmp/temp_"+n+".png")

def string_to_datetime(timestr):
		return datetime.datetime.strptime(timestr, '%Y-%m-%d %H:%M:%S')
