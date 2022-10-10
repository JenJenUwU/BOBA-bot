import discord
from discord import app_commands
from discord.ext import commands
from config import TOKEN, prefix

bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

bot.run(TOKEN)
