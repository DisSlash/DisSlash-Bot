import discord
import random
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice

class RPS(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @cog_ext.cog_slash(name="rps",
             description="Play A Simple Game Of Rock Paper Scissors",
             options=[
               create_option(
                 name="move",
                 description="Pick Your Move (Rock, Paper, Scissors)",
                 option_type=3,
                 required=True,
                 choices=[
                  create_choice(
                    name="Rock",
                    value="Rock"
                  ),
                  create_choice(
                    name="Paper",
                    value="Paper"
                  ),
                  create_choice(
                    name="Scissors",
                    value="Scissors"
                  )
                ]
               )
             ])
    async def rps(self, ctx, move: str):
        elments=["Rock", "Paper", "Scissors"]
        winner = random.choice(elments)
        if move == winner:
            embedVar = discord.Embed(description=f'You tied, you both had {move}.')
            await ctx.send(embed=embedVar)
        elif move == "Rock":
            if winner == "Scissors":
                embedVar = discord.Embed(description="Rock smashes scissors! You win!")
                await ctx.send(embed=embedVar)
            else:
                embedVar = discord.Embed(description="Paper covers rock! You lose.")
                await ctx.send(embed=embedVar)
        elif move == "Paper":
            if winner == "Rock":
                embedVar = discord.Embed(description="Paper covers rock! You win.")
                await ctx.send(embed=embedVar)
            else:
                embedVar = discord.Embed(description="Scissors cuts paper! You lose.")
                await ctx.send(embed=embedVar)
        elif move == "Scissors":
            if winner == "Paper":
                embedVar = discord.Embed(description="Scissors cuts paper! You win.")
                await ctx.send(embed=embedVar)
            else:
                embedVar = discord.Embed(description="Rock smashes scissors! You lose.")
                await ctx.send(embed=embedVar)

def setup(client):
    client.add_cog(RPS(client))