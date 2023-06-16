from nextcord.ext import commands
import nextcord

import config


def get_prefix(bot, message):
	prefix = config.default_prefix
	return commands.when_mentioned_or(prefix)(bot, message)


intents = nextcord.Intents.all()
#intents.message_content = True

bot = commands.Bot(command_prefix = get_prefix, intents = intents)
bot.remove_command("help")


#print(bot.help_command)
