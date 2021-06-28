import discord
from discord import player

# import hypixel
import fortnite_api
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice
from chessdotcom import get_player_profile

# Starting API
fortnite = fortnite_api.FortniteAPI()



class GameStat(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(
        name="gamestat",
        description="Get Your Game Stats Right From Discord",
        options=[
            create_option(
                name="game",
                description="Pick The Game You Want To Get Stats From (More Comming)",
                option_type=3,
                required=True,
                choices=[
                    create_choice(name="fortnite", value="fortnite"),
                    create_choice(name="chess", value="chess"),
                ],
            ),
            create_option(
                name="username",
                description="Enter The Username Of The Player (Not Case Sensitive)",
                option_type=3,
                required=True,
            ),
        ],
    )
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
                data = data["all"]
                overall = data["overall"]
                solo = data["solo"]
                duo = data["duo"]

                # Colleting Used Data

                # Battle Pass/Account
                level = battle["level"]
                name = name.name

                # Overalll
                overallWins = overall["wins"]
                overallTop3 = overall["top3"]
                overallKills = overall["kills"]

                # Solo
                soloWins = solo["wins"]
                soloTop3 = solo["top10"]
                soloKills = solo["kills"]

                # Duo
                duoWins = duo["wins"]
                duoTop3 = duo["top5"]
                duoKills = duo["kills"]

                # Title
                embed = discord.Embed(
                    title=f"Player Stats For {name}",
                    description=f"{name} Is On Battle Pass Level {level}",
                )

                # Overall
                embed.add_field(name="Overall Wins", value=f"{overallWins} Games")
                embed.add_field(name="Overall Top 3", value=f"{overallTop3} Games")
                embed.add_field(name="Overall Kills", value=f"{overallKills} Players")

                # Solo
                embed.add_field(name="Solo Wins", value=f"{soloWins} Games")
                embed.add_field(name="Solo Top 10", value=f"{soloTop3} Games")
                embed.add_field(name="Solo Kills", value=f"{soloKills} Players")

                # Duo
                embed.add_field(name="Duo Wins", value=f"{duoWins} Games")
                embed.add_field(name="Duo Top 5", value=f"{duoTop3} Games")
                embed.add_field(name="Duo Kills", value=f"{duoKills} Players")

                await ctx.send(embed=embed)

            except fortnite_api.NotFound:
                await ctx.send("This Is Not A Player", hidden=True)

        elif game == "chess":
            try:
                response = get_player_profile(username)
                avatar = response.json['player']['avatar']
                user_url = response.json['player']['url']
                user_name = response.json['player']['name']
                followers = response.json['player']['followers']
                player_id = response.json['player']['player_id']
                
                embed = discord.Embed(title=f"[Chess.com](https://www.chess.com) Info For {user_name}", inline=False)
                embed.add_field(name="Player ID", value=f'{user_name}\'s Player ID Is {player_id}', inline=False)
                embed.add_field(name="Follwers", value=f"{user_name} Has {followers} Followers", inline=False)
                embed.add_field(name="Player Account", value=f"{user_name}\'s Account [URL]({user_url})", inline=False)
                embed.set_thumbnail(url=avatar)
                await ctx.send(embed=embed)

            except:
                await ctx.send("Sorry, This Is Not A User!")




def setup(client):
    client.add_cog(GameStat(client))

# {'player': {'avatar': 'https://images.chesscomfiles.com/uploads/v1/user/11177810.d53953f7.200x200o.3ef259191986.png', 'player_id': 11177810, 
# '@id': 'https://api.chess.com/pub/player/fabianocaruana', 'url': 'https://www.chess.com/member/FabianoCaruana', 'name': 'Fabiano Caruana', 'username': 'fabianocaruana', 
# 'title': 'GM', 'followers': 12441, 'country': 
# 'https://api.chess.com/pub/country/US', 'last_online': 1622667484, 'joined': 1363533272, 'status': 'premium', 'is_streamer': False}}