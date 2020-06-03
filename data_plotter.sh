#!bin/bash
. /home/pi/.bashrc
cd /home/pi/website/dhtreader

source ../venv/bin/activate
python plot_data.py

