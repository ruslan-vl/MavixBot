from nextcord.ext import commands, tasks
from nextcord import SlashOption
from typing import Optional
from datetime import datetime
import nextcord

from dispatcher import bot
import database
import filters
import core
import config

class ServerManager(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	

	
	@tasks.loop(seconds = 65)
	#@commands.command()
	async def server_cheak_task(self):
		data = core.get_info_server()
		response = database.get("history", ["action", "time_at", "id"], order_by = "id desc", limit = 1)
		print("response", response)
		if not response:
			id = database.add("history", time_at = core.Time.now_unix(), action = (1 if data["online"] else 0))
			response = database.get("history", ["action", "time_at", "id"], id = id)
		
		emb = nextcord.Embed()
		emb.timestamp = core.Time.now()
		if bool(response[0][0]) != data["online"]:
			database.add("history", time_at = core.Time.now_unix(), action = (1 if data["online"] else 0))
			if data["online"]: # online
				emb.title = ":white_check_mark:"
				emb.description = "Сервер проснулся"
				emb.color = 0x80FF00
				emb.add_field(name = "Сервер примерно был в откючке: ", value = core.time_difference(response[0][1]), inline = False)
			else: # offline 
				emb.title = ":x:"
				emb.description = "Сервер вырубился"
				emb.color = 0xFF0000
				emb.add_field(name = "Сервер пахал: ", value = core.time_difference(response[0][1]), inline = False)
			try:
				await self.bot.get_channel(config.log_off_on_sending_channel_id).send(embed = emb)
			except:
				pass
	
	
	
	def general_status(self, ctx, cmd_type):
		data = core.get_info_server()
		emb = nextcord.Embed(color = 0xC61D95)
		emb.timestamp = datetime.fromtimestamp(round(data["retrieved_at"] /1000))
		emb.add_field(name = "Статус", value = "Онлайн" if data["online"] else "Оффлайн", inline = False)
		if data["online"]:
			emb.add_field(name = "Текущий онлайн", value = "%s/%s" % (data["players"]["online"], data["players"]["max"]), inline = False)
			#emb.add_field(name = "Версия", value = data["version"]["name"], inline = False)
			emb.add_field(name = "Описание", value = data["motd"]["clean"], inline = False)
		emb.set_footer(text = "Информация обновлена")
		return emb
	
	@bot.slash_command(name = "status")
	async def _status_slash(self, ctx):
		emb = self.general_status(ctx, "slash")
		await ctx.response.send_message(embed = emb)
	@commands.command(name = "status")
	async def _status(self, ctx):
		emb = self.general_status(ctx, "command")
		await ctx.send(embed = emb)
	



def setup(bot):
	bot.add_cog(ServerManager(bot))



#default = config.server_info["host"]

"""
	@tasks.loop(minutes = 1)
	async def server_cheak_task(self):
		last = core.get_last_status()
		is_online = core.is_online()
		if not last or last.is_online != is_online:
			core.sql.execute("insert into history (time, is_online) values (?, ?)", (datetime.utcnow().timestamp(), (1 if is_online else 0)))
			core.db.commit()
			if is_online == True:
				answer = "Сервер очнулся, %s UTC\nБыл в сне: %s"
			else:
				answer = "Сервер спит, %s UTC\nРаботал: %s"
			
			last_status = core.get_last_status()
			before_last_status = core.get_history(2)[-1]
			m, s = divmod(last_status.time_unix - before_last_status.time_unix, 60)
			h, m = divmod(m, 60)
			d, h = divmod(h, 24)
			passed_time = f"{int(d)} дней {int(h)} часов {int(m)} минут"
			answer = answer % (last_status.time.strftime("%d.%m.%Y %H:%M"), passed_time)
			await self.bot.get_channel(config.sending_channel_id).send(answer)
			#await self.bot.get_user(config.sending_user_id).send(answer)
	
	
	@bot.slash_command(name = "status_server")
	async def status_server_slash(self, interaction, host: Optional[str] = SlashOption(required = False), port: Optional[int] = SlashOption(required = False)):
		filter = filters.UserFilters(interaction.user)
		if filter.is_admin():
			r = core.getInfoServer(host, port)
			answer = f"{r.host}:{r.port} v{r.version}\n{r.gamemode}, {r.players_online}/{r.players_max}, {round(r.latency, 2)}ms\n{r.motd}, {r.map}"
		else: answer = self.text_not_filter % interaction.user.name
		await interaction.response.send_message(answer)
		
	
	
	@bot.slash_command(name = "history")
	async def history_server_slash(self, interaction, limit: Optional[int] = SlashOption(min_value = 1, max_value = 20, default = 10)):
		filter = filters.UserFilters(interaction.user)
		if filter.is_admin():
			emb = nextcord.Embed()
			for i in core.get_history(limit):
				emb.add_field(name = str(i.id), value = f"is_online: {i.is_online}, time: {i.time}, time_unix: {i.time_unix}", inline = False)
		else: emb = nextcord.Embed(description = f"**{interaction.user.name}**, пашел нахуй")
		await interaction.response.send_message(embed = emb)"""

