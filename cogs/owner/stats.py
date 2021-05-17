import discord
import datetime, time
from discord.ext import commands

class Stats(commands.Cog):
  
  def __init__(self, client):
        self.client = client
