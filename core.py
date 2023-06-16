from datetime import datetime, timezone
import requests
import os

import config


def get_cog_files(path = "."):
	ignor_files = config.ignor_files["cogs"]
	answer = []
	for file in os.listdir("./cogs/"):
		if file not in ignor_files:
			answer.append(file)
	return answer



def get_cog_names(path = "."):
	answer = []
	for file in get_cog_files():
		if file.endswith(".py"):
			answer.append(file[:-3])
	return answer



def get_info_server(address = config.ADDRESS_SERVER):
	data = requests.get(config.MAIN_API % address).json()
	return data


convert_to_cmd = lambda cmd: f"`{config.default_prefix}{cmd}`"




class Time:
	def now(tz = timezone.utc):
		return datetime.now(tz)
	
	def now_unix(tz = timezone.utc):
		return Time.now(tz).timestamp()
	
	def in_normal(unix, tz = timezone.utc):
		return datetime.fromtimestamp(unix, tz)
	
	def in_unix(time, tz = timezone.utc):
		return time.timestamp()
	
	def seconds_to_time(seconds):
		d, h = divmod(seconds, 86400)
		h, m = divmod(h, 3600)
		m, s = divmod(m, 60)
		return d, h, m, s
	
	def to_text(d, h, m, s):
		return f"{int(d)} дней, {int(h)} часов, {int(m)} минут, {round(s)} секунд"



time_difference = lambda q: Time.to_text(*Time.seconds_to_time(Time.now_unix() - q))