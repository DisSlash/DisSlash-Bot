import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice


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
                  ),
                  create_choice(
                    name="scissors",
                    value="scissors"
                  )
                ])
    async def ball(self, ctx, question: str):
        answer = random.choice(answers)
        embedVar = discord.Embed(title=f'{question}?', description=f'🎱 Says {answer}')
        await ctx.send(embed=embedVar)

def setup(client):
    client.add_cog(EightBall(client))

