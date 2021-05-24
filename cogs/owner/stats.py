import discord
import datetime, time
from discord.ext import commands
from datetime import datetime, timedelta


now = datetime.now()
current = now.strftime("%H:%M:%S")
start_time = time.time()

class Stats(commands.Cog):
  
  def __init__(self, client):
        self.client = client
  
  
  @commands.command()
  async def stats(self, ctx):
    
    # Getting Time
    current_time = time.time()
    difference = int(round(current_time - start_time))
    uptime = str(datetime.timedelta(seconds=difference))
    
    # Embed
    embed = discord.Embed(title=f'Hey! This Is My Stats Since Last Check')
    embed.set_thumbnail(url='https://i.imgur.com/US4aSgW.png')
    embed.set_footer(text=f'The Time This Command Was Requested Was {current}')
    embed.add_feild(name="Uptime", value=f'DisSlash Has Been Online For {uptime}')
    embed.add_feild(name="Servers", value=f'DisSlash Is In {len(client.guilds)} Servers')
    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Stats(client))
