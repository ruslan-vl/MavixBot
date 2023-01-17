from nextcord.ext import commands, tasks
from datetime import datetime
import nextcord
import platform
import os

from .server_manager import ServerManager



class Manager(commands.Cog):
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
		ServerManager.server_cheak_task.start(self)









def setup(bot):
	bot.add_cog(Manager(bot))