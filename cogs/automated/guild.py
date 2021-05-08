import discord
from discord.ext import commands
from dhooks import Webhook

class Guild(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
      hook = Webhook('https://discord.com/api/webhooks/840407485973397504/PjCzZSld9GwAiCfL7QcyXqhb_8PurN3lXqM-w0fpns6ZkcgQuqCaLCQTjnmrpNPEXgDP')
      embed = discord.Embed(title=f'DisSlash Has Been Added To A New Guild!', description=f'Congrats DisSlash Team!')
      hook.send(embed=embed)
      
      
def setup(client):
    client.add_cog(Guild(client))
