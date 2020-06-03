import Adafruit_DHT
import sqlite3
import sys
import datetime



data_directory = "/var/opt/website-data/"
db_filename = data_directory+"apartment.db"
timestamp_format = '%Y-%m-%d %H:%M:%S'

#connect to db
try:
	con = sqlite3.connect(db_filename)
except Error as e:
        print(e)
        sys.exit()
cur = con.cursor()

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4 #GPIO pin 4, physical pin 7

#read sensor
humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
if humidity is not None and temperature is not None:
	#see if it worked
	now = datetime.datetime.now().strftime(timestamp_format)
	data = (now,str("%.2f" % temperature), str("%.2f" % humidity))
	print(data)
	cur.execute("INSERT INTO apartment (timestamp, temp, hum) VALUES (?, ?, ?)",
	             data)
	con.commit()
	con.close()

