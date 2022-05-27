import discord
import json
from discord.ext import commands,tasks
import time
import os
import sys

def getCreds():
	with open(os.path.expanduser('~/.bot_creds'), 'r') as file:
		content = file.read()
	return content;
	
bot_cred = getCreds()

print(bot_cred)
intents = discord.Intents().default()
bot = commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_ready():
	print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(bot))
	
	

	

@bot.command(name='order', help='Order a delicious drink! Make sure to include the list of flavors you want')
async def stop(ctx):
	orders = ctx.message.content[1:]
	print(orders)
	os.system("python3 main.py " + orders)


bot.run(bot_cred)
