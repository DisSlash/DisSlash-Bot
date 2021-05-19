import discord
from discord.ext import commands
from dhooks import Webhook

class Guild(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
      hook = Webhook('https://discord.com/api/webhooks/840407485973397504/PjCzZSld9GwAiCfL7QcyXqhb_8PurN3lXqM-w0fpns6ZkcgQuqCaLCQTjnmrpNPEXgDP')
      name= guild.name
      owner = guild.owner
      guildid = guild.id
      memberCount = guild.member_count
      icon = guild.icon_url
      
      embed = discord.Embed(title="DisSlash Is In A New Guild!")
      embed.add_feild(name="Guild Name", value=f'{name}')
      embed.add_feild(name="Guild ID", value=f'{guildid}')
      embed.add_feild(name="Member Count", value=f'{memberCount}')  
      embed.set_thumbnail(url=icon)
      hook.send(embed=embed)
      
      
def setup(client):
    client.add_cog(Guild(client))
