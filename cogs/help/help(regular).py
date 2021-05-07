import discord
import json
from discord.ext import commands


update = os.environ.get('NEWS')

class HelpRegular(commands.Cog):
    def __init__(self, client):
        self.client = client
    

    # Help Command
    @commands.command()
    async def help(self, ctx):
        embedVar = discord.Embed(title='Hey! Im DisSlash, I am a Discord Bot that adds Slash Commands to your Discord Server', color=0xFF0000)
        embedVar.add_field(name="DisSlash News", value=update, inline=False)
        embedVar.add_field(name="`Slash Commands`", value="To use slash commands, type `/` into the message box to bring up my commands.", inline=False)
        embedVar.add_field(name="`Invite Bot`", value="Are you loving this Discord Bot? why not invite it to your server [here](https://bit.ly/3ml5Lbf).", inline=False)
        embedVar.add_field(name="`Command Request`", value="To request a command to be added to be added, send a request form [here](https://forms.gle/Y1y8XYTEtsQoPaGq6).", inline=False)
        embedVar.add_field(name="`Support`", value="Need help using the Discord Bot? Join our server [here](https://discord.gg/kPhuc65q2u), and open a ticket.", inline=False)
        embedVar.add_field(name="`Contact Us`", value="Want to contact us to get info about our bot, email us as discorddisslash@gmail.com.", inline=False)
        await ctx.send(embed=embedVar)

def setup(client):
    client.add_cog(HelpRegular(client))
