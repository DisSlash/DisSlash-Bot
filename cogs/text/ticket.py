from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice

class Ticket(commands.Cog):
  
  def __init__(self, client):
    self.client = client
   
  @cog_ext.cog_slash(
        name="ticket",
        description="Open A Support Ticket In The Server",
    )
  
  async def ticket(self, ctx):
    await ctx.send("Sorry, this command is unavalable as of right now 😔", hidden=True)
    
    
def setup(client):
  client.add_cog(Ticket(client))
