import discord
import datetime, time
from discord.ext import commands
from datetime import datetime


now = datetime.now()
current_time = now.strftime("%H:%M:%S")

class Stats(commands.Cog):
  
  def __init__(self, client):
        self.client = client
  
  @commands.command()
  async def stats(self, ctx):
    uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
    embed = discord.Embed(title=f'Hey! This Is My Stats Since Last Check')
    embed.set_thumbnail(url='https://i.imgur.com/US4aSgW.png')
    embed.set_footer(text=f'The Time This Command Was Requested Was {current_time}')
    embed.add_feild(name="Uptime", value=f'DisSlash Has Been Online For {uptime}')
    embed.add_feild(name="Servers", value=f'DisSlash Is In {len(client.guilds)} Servers')
    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Stats(client))
