import discord
from discord import user
from discord.ext import commands
from discord.ext.commands.core import has_guild_permissions
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice

# API's
from fortnite_python import Fortnite
from fortnite_python.domain import Mode, Stats
import hypixel

fortnite = Fortnite('a3e167be-5718-4102-9cc2-6045089e7f0b')
whitelist = [710194014569234462]
API_KEYS = ['fa8266d7-65bc-4aba-b01c-fc8c4ceb04e2']
hypixel.setKeys(API_KEYS)

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
                    name="hypixel",
                    value="hypixel"
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
              await ctx.send("Sorry, This Command Is Disabled")
                
        elif game == "hypixel":
          try:
            Player = hypixel.Player(username)
            PlayerName = Player.getName()
            PlayerLevel = Player.getLevel()
            PlayerGuild = Player.getGuildID()
            PlayerKarma = Player.JSON['karma']
            
            embed = discord.Embed(titel=f'Hypixel Stats For {PlayerName}')
            embed.add_field(name='Player Level', value=f'{PlayerName}\'s Level Is {PlayerLevel}')
            embed.add_field(name='Player Karma', value=f'{PlayerName}\'s Karma Is {PlayerKarma}')
            if PlayerGuild == None:
                embed.add_field(name=f'Player Guild', value=f'{PlayerName}\'s Is Not In Any Guild')
            else:
                embed.add_field(name=f'Player Guild', value=f'{PlayerName}\'s Is In Guild {PlayerGuild}')
            embed.set_image(url='https://i.imgur.com/kpuiDZf.jpg')
            await ctx.send(embed=embed)
               
          except hypixel.PlayerNotFoundException:
            await ctx.send("Please Enter A Valid Username", hidden=True)
          
          except hypixel.HypixelAPIError:
            await ctx.send('Sorry, There Has Been A API Problem, Please DM Neil Shah#6469 To Report', hidden=True)
                                
                                
      else:
        await ctx.send("Looks Like You Found A Special Command, Become A Pateron Today To Use It, Or Wait Until It Is Out of Beta!", hidden=True)


def setup(client):
    client.add_cog(GameStats(client))

