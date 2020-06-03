# website
Flask Webstie

#Virtual Env:
start with:
```
source venv/bin/activate
pip install -r requirements.txt
 pip freeze > requirements.txt
```

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```


#Set up db:
```
cd DHT22_reader
touch apartment.db
sqlite3 apartment.db
CREATE TABLE apartment (timestamp DATETIME, temp NUMERIC, hum NUMERIC);
```
