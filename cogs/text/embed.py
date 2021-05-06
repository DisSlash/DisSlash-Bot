import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice

class Embed(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @cog_ext.cog_slash(name="embed",
             description="Send An Embed In Your Discord Server",
             options=[
               create_option(
                 name="Title",
                 description="Please Enter A Title For Your Embed",
                 option_type=3,
                 required=True
               ),
               create_option(
                 name="Content",
                 description="Please Type In The Main Body Of The Embed",
                 option_type=3,
                 required=True
               )
             ])
    async def embed(self, ctx, Title: str, Content: str):
        if len(Content) > 225:
            await ctx.send("Sorry, Plase Make Sure That The Embed Is Less Than 250 Characters", hidden=True)
        else:
            embedVar = discord.Embed(title=f'{Title}', color=0xFF0000)
            embedVar.add_field(name=f'{Content}', value="Powered By InSight3D Development")
            await ctx.send(embed=embedVar)

def setup(client):
    client.add_cog(Embed(client))
