from nextcord.ext import commands
from functools import wraps

import config



class UserFilters:
	def __init__(self, user):
		self.user = user
		self.guild = self.user.guild or None
	
	
	def is_dev(self):
		return self.user.id == config.dev_id





def has_permissions(**perms):
	return commands.has_permissions(**perms)



