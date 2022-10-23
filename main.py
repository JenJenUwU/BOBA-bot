import discord
from discord.ext import commands
from config import botPrefix
from dotenv import load_dotenv
import os
# environment variables
load_dotenv()
token = os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix=botPrefix, intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


# import bot token from github environment secret\
bot.run(token)
