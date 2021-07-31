from pymongo.uri_parser import _handle_option_deprecations
from cogs.games.activities import setup
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice
import os
from pymongo import MongoClient

MONGODB = os.environ["MONGODB"]
cluster = MongoClient(MONGODB)
db = cluster["disslash"]
tickets = db["tickets"]

class Ticket(commands.Cog):
  
  def __init__(self, client):
    self.client = client
   
  @cog_ext.cog_slash(
        name="ticket",
        description="Open A Support Ticket In The Server",
    )
  
  async def ticket(self, ctx):
    server_data = tickets.find({"server": ctx.guild.id})
    for i in server_data:
      server_bool = i['is_setup']

    if server_bool:
      await ctx.send("All Setup") 

    else:
      await ctx.send("Nope!")   


    
    
def setup(client):
  client.add_cog(Ticket(client))
