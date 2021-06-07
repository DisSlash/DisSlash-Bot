import discord
import random
from discord.ext import commands
from discord_slash import cog_ext, SlashContext


class Flip(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(name="flip", description="Spin A Quick Heads Or Tail Coin")
    async def flip(self, ctx):
        sides = ["Heads", "Tails"]
        pick = random.choice(sides)
        embedVar = discord.Embed(description=f"I Flipped {pick}!", color=0xFF0000)
        await ctx.send(embed=embedVar)


def setup(client):
    client.add_cog(Flip(client))
