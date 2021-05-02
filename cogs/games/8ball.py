import discord
import random
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice

answers = ["It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely", "You may rely on it", "As I see it, yes", "Most likely", "Signs point to yes", 
"Better not tell you now", "My reply is no", "Outlook not so good", "My sources say no"]

class EightBall(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @cog_ext.cog_slash(name="8ball",
             description="Ask The Magic 8 Ball A Question",
             options=[
               create_option(
                 name="Question",
                 description="Ask Your Question Here",
                 option_type=3,
                 required=True
               )
             ])
    async def ball(self, ctx, Question: str):
        answer = random.choice(answers)
        embedVar = discord.Embed(title=f'{Question}?', description=f'🎱 Says {answer}')
        await ctx.send(embed=embedVar)

def setup(client):
    client.add_cog(EightBall(client))