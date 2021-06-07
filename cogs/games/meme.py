import discord
from pyrandmeme import *
from discord.ext import commands
from discord_slash import cog_ext, SlashContext


class Meme(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(name="meme", description="Get A Random Juicy Meme")
    async def meme(self, ctx):
        await ctx.send(embed=await pyrandmeme())


def setup(client):
    client.add_cog(Meme(client))
