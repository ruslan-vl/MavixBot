from mcstatus import BedrockServer
from datetime import datetime
import sqlite3
import os

import config


db = sqlite3.connect("database")
sql = db.cursor()

sql.execute("""create table if not exists history (
	id integer PRIMARY KEY AUTOINCREMENT, 
	time real,
	is_online integer
)""")


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




class AnswerInfoServer:
	def __init__(self, host, port, server):
		self.host = host
		self.port = port
		self._version = server.version
		self.version = server.version.version
		self.latency = server.latency
		self.players_online = server.players_online
		self.players_max = server.players_max
		self.motd = server.motd
		self.map = server.map
		self.gamemode = server.gamemode
	def __repl__(self):
		return str(self.__dict__)
	def __str__(self):
		return str(self.__dict__)


def is_online(host = None, port = None):
	host = host or config.server_info["host"]
	port = port or config.server_info["port"]
	try:
		BedrockServer(host, port).status()
		return True
	except TimeoutError:
		return False


def getInfoServer(host = None, port = None):
	host = host or config.server_info["host"]
	port = port or config.server_info["port"]
	
	server = BedrockServer(host, port).status()
	return AnswerInfoServer(host, port, server)


class AnswerHistory:
	def __init__(self, data):
		self.id = data[0]
		self.time = datetime.fromtimestamp(data[1])
		self.time_unix = data[1]
		self.is_online = bool(data[2])
	def __repl__(self):
		return str(self.__dict__)
	def __str__(self):
		return str(self.__dict__)


def get_history(limit: int = 10):
	_ = sql.execute("select * from history order by id desc limit %d" % (limit)).fetchall()
	for i in range(len(_)):
		_[i] = AnswerHistory(_[i])
	return _


def get_last_status():
	_ = get_history(limit = 1)
	return _[0] if _ else None