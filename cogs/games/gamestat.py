import discord
# import hypixel
import fortnite_api
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice

# Starting API
fortnite = fortnite_api.FortniteAPI()
# API_KEYS = ['fa8266d7-65bc-4aba-b01c-fc8c4ceb04e2']
# hypixel.setKeys(API_KEYS)

class GameStat(commands.Cog):
  
  def __init__(self, client):
    self.client = client
  
  @cog_ext.cog_slash(name="gamestat",
          description="Get Your Game Stats Right From Discord",
          options=[
            create_option(
              name="game",
              description="Pick The Game You Want To Get Stats From (More Comming)",
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
              description="Enter The Username Of The Player (Not Case Sensitive)",
              option_type=3,
              required=True
            )
          ])
  async def gamestat(self, ctx, game: str, username=None):
    await ctx.defer()
    username = username.lower()
    if game == "fortnite":
      try:
        # Get User Data And Dict
        stats = fortnite.stats.fetch_by_name(username).stats
        battle_pass = fortnite.stats.fetch_by_name(username).battle_pass
        name = fortnite.stats.fetch_by_name(username).user
        data = stats.raw_data
        battle = battle_pass.raw_data

        # Narrow Down Serach Results
        data = data['all']
        overall = data['overall']
        solo = data['solo']
        duo = data['duo']

        # Colleting Used Data
    
        # Battle Pass/Account
        level = battle['level']
        name = name.name
        
        # Overalll
        overallWins = overall['wins']
        overallTop3 = overall['top3']
        overallKills = overall['kills']

        # Solo
        soloWins = solo['wins']
        soloTop3 = solo['top10']
        soloKills = solo['kills']

        # Duo
        duoWins = duo['wins']
        duoTop3 = duo['top5']
        duoKills = duo['kills']
     
        # Title
        embed = discord.Embed(title=f'Player Stats For {name}', description=f'{name} Is On Battle Pass Level {level}')
        
        # Overall
        embed.add_field(name="Overall Wins", value=f'{overallWins} Games')
        embed.add_field(name="Overall Top 3", value=f'{overallTop3} Games')
        embed.add_field(name="Overall Kills", value=f'{overallKills} Players')
        
        # Solo
        embed.add_field(name="Solo Wins", value=f'{soloWins} Games')
        embed.add_field(name="Solo Top 10", value=f'{soloTop3} Games')
        embed.add_field(name="Solo Kills", value=f'{soloKills} Players')
        
        # Duo
        embed.add_field(name="Duo Wins", value=f'{duoWins} Games')
        embed.add_field(name="Duo Top 5", value=f'{duoTop3} Games')
        embed.add_field(name="Duo Kills", value=f'{duoKills} Players')
        
        await ctx.send(embed=embed)
        
      except fortnite_api.NotFound:
        await ctx.send("This Is Not A Player", hidden=True)
    
    elif game == "hypixel":
      await ctx.send("Sorry, This Command Is Not Built Yet", hidden=True)
#       try:
#         Player = hypixel.Player(username)
#         PlayerName = Player.getName()
#         PlayerLevel = Player.getLevel()
#         PlayerRank = Player.getRank()
#         embed = discord.Embed(title=f'Hypixel Stats For {PlayerName}')
#         embed.add_field(name="Player Level", value=f"{PlayerName} Is Level {PlayerLevel}")
#         embed.add_field(name="PlayerRank", value=f'{PlayerName} Is Rank {PlayerRank}')
#         await ctx.send(embed=embed)
        
#       except hypixel.PlayerNotFoundException:
#         await ctx.send("Sorry, This Is Not A Player")
        
def setup(client):
    client.add_cog(GameStat(client))
