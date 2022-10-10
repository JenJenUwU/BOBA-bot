import discord
from discord import app_commands
from discord.ext import commands
from config import prefix

bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

#import bot token from github environment secret 
bot.run(os.environ['TOKEN'])
