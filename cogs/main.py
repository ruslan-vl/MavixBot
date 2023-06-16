from nextcord.ext import commands
import platform
import nextcord

from dispatcher import bot
import filters
import config
import urls


class MainCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	
	
	def general_info(self, ctx, cmd_type):
		emb = nextcord.Embed(title = "MavixBot", description = "Информация обо мне \n\nМой префикс `;`, но ты также можешь просто @обратиться ко мне, а ещё я поддержываю слеш-команды :sunglasses:. Взгляни на команду `;help` для более детальной информации о моих возможностях :disguised_face:", color = 0x4FFFD5)
		emb.set_thumbnail(url = urls.info_thumbnail)
		emb.add_field(name = "Сборка: ", value = f"{config.version} (`{config.last_update.strftime('%d.%m.%Y')}`)", inline = False)
		emb.add_field(name = "ЯП: ", value = f"Python {platform.python_version()}", inline = False)
		emb.add_field(name = "Библиотека: ", value = f"NextCord {nextcord.__version__}", inline = False)
		emb.add_field(name = "Мой разработчик: ", value = "<:head_ryslanvipgg:1093844229383528558> IWT-T0#5155", inline = False)
		return emb
	
	@bot.slash_command(name = "info")
	async def _info_slash(self, ctx):
		emb = self.general_info(ctx, "slash")
		await ctx.response.send_message(embed = emb)
	@commands.command(name = "info")
	async def _info(self, ctx):
		emb = self.general_info(ctx, "command")
		await ctx.send(embed = emb)





#add_field
def setup(bot):
	bot.add_cog(MainCog(bot))



