import discord
import random
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice


class RPS(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(
        name="rps",
        description="Play A Simple Game Of Rock Paper Scissors",
        options=[
            create_option(
                name="move",
                description="Pick Your Move (Rock, Paper, Scissors)",
                option_type=3,
                required=True,
                choices=[
                    create_choice(name="rock", value="rock"),
                    create_choice(name="paper", value="paper"),
                    create_choice(name="scissors", value="scissors"),
                ],
            )
        ],
    )
    async def rps(self, ctx, move: str):
        elments = ["rock", "paper", "scissors"]
        winner = random.choice(elments)
        if move == winner:
            embedVar = discord.Embed(description=f"You tied, you both had {move}.", color = 0x242736)
            await ctx.send(embed=embedVar)
        elif move == "rock":
            if winner == "scissors":
                embedVar = discord.Embed(description="Rock smashes scissors! You win!", color = 0x242736)
                await ctx.send(embed=embedVar)
            else:
                embedVar = discord.Embed(description="Paper covers rock! You lose.", color = 0x242736)
                await ctx.send(embed=embedVar)
        elif move == "paper":
            if winner == "rock":
                embedVar = discord.Embed(description="Paper covers rock! You win.", color = 0x242736)
                await ctx.send(embed=embedVar)
            else:
                embedVar = discord.Embed(description="Scissors cuts paper! You lose.", color = 0x242736)
                await ctx.send(embed=embedVar)
        elif move == "scissors":
            if winner == "paper":
                embedVar = discord.Embed(description="Scissors cuts paper! You win.", color = 0x242736)
                await ctx.send(embed=embedVar)
            else:
                embedVar = discord.Embed(description="Rock smashes scissors! You lose.", color = 0x242736)
                await ctx.send(embed=embedVar)


def setup(client):
    client.add_cog(RPS(client))
