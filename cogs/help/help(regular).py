import discord
import os
from discord.ext import commands
from pymongo import MongoClient


MONGODB = os.environ["MONGODB"]


class HelpRegular(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Help Command
    @commands.command()
    async def help(self, ctx):

        cluster = MongoClient(MONGODB)
        db = cluster["disslash"]
        news = db["news"]

        count = news.count_documents({})

        newsList = news.find({"_id": count})

        for new in newsList:
            newsUpdate = new["news"]

        embedVar = discord.Embed(
            title="Hey! Im DisSlash, I am a Discord Bot that adds Slash Commands to your Discord Server",
            color=0xFF0000,
        )
        embedVar.add_field(name="DisSlash News", value=newsUpdate, inline=False)
        embedVar.add_field(
            name="`Slash Commands`",
            value="To use slash commands, type `/` into the message box to bring up my commands.",
            inline=False,
        )
        embedVar.add_field(
            name="`Invite Bot`",
            value="Are you loving this Discord Bot? why not invite it to your server [here](https://disslash.me/invite).",
            inline=False,
        )
        embedVar.add_field(
            name="`Command Request`",
            value="To request a command to be added to be added, send a request form [here](https://forms.gle/Y1y8XYTEtsQoPaGq6).",
            inline=False,
        )
        embedVar.add_field(
            name="`Support`",
            value="Need help using the Discord Bot? Join our server [here](https://discord.gg/TtVXGuuxPy), and open a ticket.",
            inline=False,
        )
        embedVar.add_field(
            name="`Contact Us`",
            value="Want to contact us to get info about our bot, email us as info@disslash.me.",
            inline=False,
        )
        await ctx.send(embed=embedVar)


def setup(client):
    client.add_cog(HelpRegular(client))
