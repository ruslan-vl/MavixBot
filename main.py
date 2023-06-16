# cd /storage/emulated/0/prog/MavixBot/ && python main.py
from nextcord.ext import commands, tasks
from typing import Optional
from nextcord import SlashOption
import nextcord
import os

from dispatcher import bot
import filters
import core
import config


#@bot.slash_command(dm_permission = True, )
async def cogs_manager(interaction, cog: Optional[str] = SlashOption(choices = ["all"]), action: Optional[str] = SlashOption(choices = ["load", "unload", "reload"])):
	filter = filters.UserFilters(interaction.user)
	if filter.is_dev():
		cogs = []
		if cog == "all":
			cogs = core.get_cog_names()
		else:
			cogs = [cog]
		for i in cogs:
			if action == "load":
				bot.load_extension(f"cogs.{i}")
			elif action == "unload":
				bot.unload_extension(f"cogs.{i}")
			elif action == "reload":
				bot.unload_extension(f"cogs.{i}")
				bot.load_extension(f"cogs.{i}")
		await interaction.response.send_message(f"Cog {cog!r} executed {action!r}")
	else:
		await interaction.response.send_message("Пашел нахуй")

@tasks.loop(seconds = 5)
async def dhbf(self):
	print("djbdnrb")

for i in core.get_cog_names():
	bot.load_extension("cogs.%s" % i)


import keep_alive
#keep_alive.keep()
bot.run(config.token)
print("\nbye")