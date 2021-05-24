import discord
from discord import user
from discord.ext import commands
from discord.ext.commands.core import has_guild_permissions
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice

# API's
from fortnite_python import Fortnite
from fortnite_python.domain import Mode, Stats

fortnite = Fortnite('a3e167be-5718-4102-9cc2-6045089e7f0b')
whitelist = [710194014569234462]

# a3e167be-5718-4102-9cc2-6045089e7f0b
class GameStats(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @cog_ext.cog_slash(name="gamestats",
             description="Get Live Stats For Any Player On Game!",
             options=[
               create_option(
                 name="game",
                 description="Pick The Game You Want To Get Stats For",
                 option_type=3,
                 required=True,
                 choices=[
                  create_choice(
                    name="fortnite",
                    value="fortnite"
                  ),
                  create_choice(
                    name="apexlegends",
                    value="apexlegends"
                  )
                 ]),
               create_option(
                 name="username",
                 description="Enter The Username Of The Player",
                 option_type=3,
                 required=True
                )
                 ])
    async def gamestats(self, ctx, game: str, username: str):
      author = ctx.author.id
      username = username.lower()
      nusernameShow = username.capitalize()
      if author in whitelist:
        if game == "fortnite":
          try:
            player = fortnite.player(username)
            statsSolo = player.get_stats(Mode.SOLO)
            statsDuo = player.get_stats(Mode.DUO)
            embed = discord.Embed(title=f"Fortnite Stats For {nusernameShow}")
            embed.add_field(name="Solo Wins", value=f'{nusernameShow} Has Won {statsSolo.top1} Games')
            embed.add_field(name="Solo Kills", value=f'{nusernameShow} Has Killed {statsSolo.kills} Players')
            embed.add_field(name="‎", value="‎")
            embed.add_field(name="Duo Wins", value=f'{nusernameShow} Has Killed {statsDuo.kills} Players')
            embed.add_field(name="Duo Kills", value=f'{nusernameShow} Has Killed {statsDuo.kills} Players')
            embed.set_image(url="https://mediavideo.blastingnews.com/p/4/2020/02/16/310e9a24-255b-4a4e-9aff-bddf312b01a9.jpg")
            await ctx.send(embed=embed)
          except:
            await ctx.send("Please Enter A Valid Player Username", hidden=True)
        elif game == "apexlegends":
          try:
            await ctx.send("Sorry, This Command Is Still In Dev", hidden=True)
          except:
            pass
      else:
        await ctx.send("Looks Like You Found A Special Command, Become A Pateron Today To Use It, Or Wait Until It Is Out of Beta!", hidden=True)

        

def setup(client):
    client.add_cog(GameStats(client))

