import sqlite3
import sys
import pandas as pd
import datetime
import matplotlib.pyplot as plt
from dhtreader.config import data_directory, db_filename, timestamp_format


def get_data():
	db_filename = data_directory + "apartment.db"
	#queries db
	con = sqlite3.connect(db_filename)
	data = pd.read_sql_query("SELECT * FROM apartment", con)
	con.close()
	data["timestamp"] = data["timestamp"].apply(string_to_datetime)
	return data[-1:]

def string_to_datetime(timestr):
		return datetime.datetime.strptime(timestr, timestamp_format)
