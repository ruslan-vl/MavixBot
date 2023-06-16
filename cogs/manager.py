from nextcord.ext import commands, tasks
from datetime import datetime
import nextcord
import platform
import os

import config
import errors


class ManagerCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	
	@commands.Cog.listener()
	async def on_ready(self):
		print(f"Logged in as {self.bot.user.name!r}")
		print(f"Python version: {platform.python_version()}")
		print(f"Running on: {platform.system()} {platform.release()} ({os.name})")
		print(run_in:=f"Running in: {datetime.utcnow().strftime('%H:%M %d.%m.%Y')} UTC")
		print("-" *25)
		await self.bot.change_presence(activity = nextcord.Game(run_in))
		
		self.bot.cogs["ServerManager"].server_cheak_task.start()




"""
	@commands.Cog.listener()
	async def on_command_error(ctx, error):
		emb = nextcord.Embed(title = "Error", color = 0xFF0000)
		if isinstance(error, errors.ErrorUnknown):
			emb.add_field(name = "ErrorUnknown", value = ":x:")
		await ctx.reply(embed = emb)
"""





def setup(bot):
	bot.add_cog(ManagerCog(bot))