from nextcord.ext import commands
import nextcord

from dispatcher import bot
import filters
import config
import errors
import core



help_commands = {
	"__None__": {
		"Информация": ("Info", ["info", "help", "status"]),
		
	},

	"Info": { #category
		"help": None,
		"description": None,
		"commands": ["info", "help", "status"],
	},

	"info": {
		"help": "Полезная информация о MavixBot",
		"description": "Показывает полезную информацию о MavixBot (версию, автора).",
		"using": "info",
		"examples": [],
	},
	"status": {
		"help": "Информация об игровом сервере Mavix",
		"description": "Показывает полезную информацию о сервере (статус, текущий онлайн, описание и т.д.)",
		"using": "status",
		"examples": [],
	},
	"help": {
		"help": "Справка по всем командам и категориям",
		"description": "Показывает справку по всем командам и категориям или по указанной категории команд.",
		"using": "help [категория или название команды]",
		"examples": [
			f"`{config.default_prefix}help` \n┗ Покажет весь список команд, доступный вызвавшему участнику.", 
			f"`{config.default_prefix}help Info` \n┗ Покажет весь список команд категории Информация, доступный вызвавшему участнику.",
			f"`{config.default_prefix}help status` \n┗ Покажет справку по команде информации о сервере.",
		],
	},
	
}




class HelpsCommand:
	def default(self, ctx, emb):
		[emb.add_field(name = f"{category} (`{config.default_prefix}help {cmds[0]}`)", value = " ".join(map(core.convert_to_cmd, cmds[1]))) for category, cmds in help_commands["__None__"].items()]

	def general(self, ctx, command, cmd_type):
		emb = nextcord.Embed(title = "Доступные команды:", 
			description = "Вы можете получить детальную справку по каждой команде, выполнив команду помощи и указав её название. Например: `;help help` или `;help info`", color = 0x71006E)
		try:
			if cmd_type == "command" or cmd_type == "slash":
				if not command:
					HelpsCommand.default(self, ctx, emb)
				else:
					if command in help_commands.keys():
						if not command == command.title():
							emb.title = f"Команда {command!r}"
							emb.description = None
							data = help_commands[command]
							emb.add_field(name = data["help"], value = data["description"], inline = False)
							if data["using"]: emb.add_field(name = "Использование", value = core.convert_to_cmd(data["using"]))
							if data["examples"]: [emb.add_field(name = f"Пример {n}", value = i, inline = False) for n, i in enumerate(data["examples"], 1)]
						else: 
							emb.title = f"Категория {command!r}"
							for i in help_commands[command]["commands"]:
								emb.add_field(name = f"> {core.convert_to_cmd(i)}", value = help_commands[i]["help"])
					else:
						raise errors.ErrorUnknown()
			
			else:
				raise errors.ErrorUnknown()
		except errors.ErrorUnknown:
			emb.title = ":x:"
			emb.description = "Произошла какая то ошибка!!!!"
			emb.color = 0xFF0000
		return emb




class HelpCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	
	
	@commands.command(name = "help")
	async def _help(self, ctx, command = None):
		emb = HelpsCommand.general(self, ctx, command, "command")
		await ctx.send(embed = emb)
	
	@bot.slash_command(name = "help")
	async def _help_slash(self, ctx, command = None):
		emb = HelpsCommand.general(self, ctx, command, "slash")
		await ctx.response.send_message(embed = emb)
	
	
	
	


#add_field
def setup(bot):
	bot.add_cog(HelpCog(bot))



