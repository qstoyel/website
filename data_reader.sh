#!bin/bash
. /home/pi/.bashrc
cd /home/pi/website/dhtreader

source ../venv/bin/activate
python read_sensor.py


