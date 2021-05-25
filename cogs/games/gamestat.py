import discord
import fortnite_api
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice

# Starting API
fortnite = fortnite_api.FortniteAPI()

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
    username = username.lower()
    if game == "fortnite":
      try:
        # Get User Data And Dict
        stats = api.stats.fetch_by_name(username).stats
        battle_pass = api.stats.fetch_by_name(username).battle_pass
        name = api.stats.fetch_by_name(username).user
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
        soloTop3 = solo['top3']
        soloKills = solo['kills']

        # Duo
        duoWins = duo['wins']
        duoTop3 = duo['top3']
        duoKills = duo['kills']
     
        # Title
        embed = discord.Embed(title=f'Player Stats For {name}', description=f'{name} Is On Battle Pass Level {level}')
        
        # Overall
        embed.add_field(name="Overall Wins", value=f'{name} Has Won {overallWins} Games')
        embed.add_field(name="Overall Top 3", value=f'{name} Has Been On The Leaderboard {overallTop3} Games')
        embed.add_field(name="Overall Kills", vlaue=f'{name} Has Killed {overallKills} Players')
        
        # Duo 
        
        
      except fortnite_api.NotFound:
        await ctx.send("This Is Not A Player", hidden=True)
    
    elif game == "hypixel":
      pass
