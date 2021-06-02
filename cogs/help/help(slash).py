import discord
import os
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_components import DiscordComponents, Button, component
from discord_components.button import ButtonStyle

update = "Hello Everyone, Today I Would Like To Announce That DisSlash Has Officially Been Verified! Now, You Can Add DisSlash To As Many Servers As You Want. If You Need Help, Feel Free To Join Our Support Server, Or Email Us At `info@disslash.me`!"


class HelpSlash(commands.Cog):
    def __init__(self, client):
        self.client = client
    

    # Also Help Command
    @cog_ext.cog_slash(name="help",
                description="Open Our Help Command")
    async def help(self, ctx: SlashContext):
        embedVar = discord.Embed(title='Hey! Im DisSlash, I am a Discord Bot that adds Slash Commands to your Discord Server', color=0xFF0000)
        embedVar.add_field(name="DisSlash News", value=update, inline=False)
        embedVar.add_field(name="`Slash Commands`", value="To use slash commands, type `/` into the message box to bring up my commands.", inline=False)
        embedVar.add_field(name="`Invite Bot`", value="Are you loving this Discord Bot? why not invite it to your server [here](https://bit.ly/3ml5Lbf).", inline=False)
        embedVar.add_field(name="`Command Request`", value="To request a command to be added to be added, send a request form [here](https://forms.gle/Y1y8XYTEtsQoPaGq6).", inline=False)
        embedVar.add_field(name="`Support`", value="Need help using the Discord Bot? Join our server [here](https://discord.gg/kPhuc65q2u), and open a ticket.", inline=False)
        embedVar.add_field(name="`Contact Us`", value="Want to contact us to get info about our bot, email us as info@disslash.me.", inline=False)
        await ctx.send(embed=embedVar,
        components=[
            Button(style=ButtonStyle.URL, label="Website", url="https://disslash.me"),
            Button(style=ButtonStyle.URL, label="Invite", url="https://disslash.me/invite"),
            Button(style=ButtonStyle.URL, label="Contact", url="mailto:hello@disslash.me?subject=Contanct&body=Hey%20DisSlash%2C%0A%0A%0A%0AThanks%2C%0AYour%20Name")
            ])

def setup(client):
    client.add_cog(HelpSlash(client))
