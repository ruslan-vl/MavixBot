from os import environ

from version import version, last_update

token = environ["TOKEN"]


log_off_on_sending_channel_id = 1119145257372749887
dev_id = 740590351466889217
default_prefix = ":"
ignor_files = {
	"cogs": ("__init__.py"),
	
}
database_name = "database.db"


MAIN_API = "https://api.mcstatus.io/v2/status/bedrock/%s"
IP_SERVER = "46.17.104.106" #106
PORT_SERVER = 19132

ADDRESS_SERVER = "%s:%s" % (IP_SERVER, PORT_SERVER)
