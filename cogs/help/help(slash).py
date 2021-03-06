import discord
import os
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from pymongo import MongoClient
from discord_slash.utils import manage_components
from discord_slash.model import ButtonStyle

MONGODB = os.environ["MONGODB"]


class HelpSlash(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Also Help Command
    @cog_ext.cog_slash(name="help", description="Open Our Help Command")
    async def help(self, ctx: SlashContext):

        cluster = MongoClient(MONGODB)
        db = cluster["disslash"]
        news = db["news"]

        count = news.count_documents({})

        newsList = news.find({"_id": count})

        for new in newsList:
            newsUpdate = new["news"]

        embedVar = discord.Embed(
            title="Hey! Im DisSlash, I am a Discord Bot that adds Slash Commands to your Discord Server",
            color = 0x242736
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
        
        buttons = [
            manage_components.create_button(
                style=ButtonStyle.URL,
                label="Website",
                url = "https://disslash.me"
            ),
            manage_components.create_button(
                style=ButtonStyle.URL,
                label="Invite",
                url = "https://disslash.me/invite"
            ),
            manage_components.create_button(
                style=ButtonStyle.URL,
                label="Support",
                url = "https://disslash.me/support"
            ),
        ]
        
        action_row = manage_components.create_actionrow(*buttons)
        
        await ctx.send(embed=embedVar, components=[action_row])


def setup(client):
    client.add_cog(HelpSlash(client))
