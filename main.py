import http
import os
import ssl
import discord
import nextcord
import wavelink
from nextcord.ext import commands
from config import botPrefix
from dotenv import load_dotenv

# environment variables
load_dotenv()
token = os.getenv("DISCORD_TOKEN")
intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=botPrefix, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    bot.loop.create_task(node_connect())


@bot.event
async def on_wavelink_node_ready(node: wavelink.Node):
    print(f'Node {node.identifier} is ready.')


async def node_connect():
    await bot.wait_until_ready()
    await wavelink.NodePool.create_node(bot=bot, host='node1.gglvxd.tk', port=443, password='free', https=True)


@bot.command()
async def play(ctx: commands.Context, *, search: wavelink.YouTubeTrack):
    if not ctx.voice_client:
        vc: wavelink.Player = await ctx.author.voice.channel.connect(cls=wavelink.Player)
    elif not ctx.author.voice_client:
        return await ctx.send("You are not connected to a voice channel.")
    else:
        vc: wavelink.Player = ctx.voice_client
    vc.play(search)
# import bot token from github environment secret
bot.run(token)
