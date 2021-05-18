import discord
import asyncio
from covid import Covid
import json
import aiohttp
import random
import math
from dotenv import load_dotenv
import wikipediaapi
from discord_slash.utils.manage_commands import create_option, create_choice
from discord_slash import SlashCommand
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure
from discord.ext.commands import has_role
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext.commands import cooldown, BucketType
from os import getenv
from discord_slash import SlashContext
import os
from yahoo_fin.stock_info import *
from pyrandmeme import *
import validators
import pyqrcode
from pyqrcode import QRCode
import qrcode
import datetime, time

# Intents
intents = discord.Intents.default()
intents.members = True

# Bot Info Setup
client = commands.Bot(command_prefix = '#', intents=intents)
slash = SlashCommand(client, sync_commands=True, sync_on_cog_reload=True)
client.remove_command('help')

# Load ENV

# Loop
async def status_task():
  while True:
        await client.change_presence(activity=discord.Game(name='/help | #help'))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(name=f"{len(client.guilds)} servers!"))
        await asyncio.sleep(10)

@client.event
async def on_ready():
    print("Bot Is Online")
    client.loop.create_task(status_task())
    
@client.command()
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs/help'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.help.{filename[:-3]}')

for filename in os.listdir('./cogs/automated'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.automated.{filename[:-3]}')

for filename in os.listdir('./cogs/economy'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.economy.{filename[:-3]}')

for filename in os.listdir('./cogs/games'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.games.{filename[:-3]}')

for filename in os.listdir('./cogs/moderation'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.moderation.{filename[:-3]}')

for filename in os.listdir('./cogs/search'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.search.{filename[:-3]}')

for filename in os.listdir('./cogs/text'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.text.{filename[:-3]}')


TOKEN = os.environ["TOKEN"]
client.run(TOKEN)
