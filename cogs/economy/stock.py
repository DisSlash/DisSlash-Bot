import discord
from yahoo_fin.stock_info import *
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice

with open("tickers.txt") as input_file:
    long_list = [line.strip() for line in input_file]


class Stock(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(
        name="stock",
        description="Get Live Trading Value",
        options=[
            create_option(
                name="ticker",
                description="Please Enter The Stock Symbol",
                option_type=3,
                required=True,
            )
        ],
    )
    async def stock(self, ctx, ticker):
        symbol = ticker.upper()
        with open("tickers.txt") as input_file:
            long_list = [line.strip() for line in input_file]
        if symbol in long_list:
            price = get_live_price(symbol)
            price_new = round(price, 2)
            embed = discord.Embed(
                title=f"The Current Trading Value Of {symbol} Is: ",
                description=f"{price_new} USD",
            )
            await ctx.send(embed=embed)
        else:
            await ctx.send("Sorry, this is not a valid ticker.", hidden=True)


def setup(client):
    client.add_cog(Stock(client))
