from flask import Flask
from threading import Thread
import datetime as dtime
import pytz

time_start_old = dtime.datetime.now()
time_start = time_start_old.strftime("%d.%m.%Y %H:%M:%S")

app = Flask("app")

@app.route("/")
def main():
	time = dtime.datetime.now(tz=pytz.timezone("Europe/Moscow"))
	time = time.strftime("%d.%m.%Y %H:%M:%S")
	output = f"Start: {time_start} Now: {time}"
	return output

def run():
	app.run(host="0.0.0.0", port=8080)

def keep():
	serv = Thread(target=run)
	serv.start()