import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice

class Google(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    
    @cog_ext.cog_slash(name="google",
             description="Create A Quick Search Link",
             options=[
               create_option(
                 name="Search",
                 description="Once Sent, I Will Make A Google Search Link",
                 option_type=3,
                 required=True
               )
             ])
    async def google(self, ctx, Search: str):
        Search = Search.replace(" ", "")
        embedVar = discord.Embed(description=f'[Here Is Your Quick Search Link](https://www.google.com/search?q={Search})')
        await ctx.send(embed=embedVar)


def setup(client):
    client.add_cog(Google(client))