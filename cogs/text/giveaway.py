import discord
import asyncio
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice
import random

class Giveaway(commands.Cog):

    def __init__(self, client):
        self.client = client
    

    @cog_ext.cog_slash(name="giveaway",
             description="Make A Giveaway For Your Server",
             options=[
               create_option(
                 name="Hours",
                 description="Enter How Many Hours You Want This To Run (This Value Can Be 0)",
                 option_type=4,
                 required=True
                ),
               create_option(
                 name="Minuets",
                 description="Enter How Many Mineuts You Want This To Run (This Value Can Be 0)",
                 option_type=4,
                 required=True
                ),
                create_option(
                 name="Prize",
                 description="Enter The Prize You Want To Give Away",
                 option_type=3,
                 required=True
                )
               ])
    @commands.guild_only()
    async def giveaway(self, ctx, hours, mins, prize):
        if hours + mins == 0:
            await ctx.send("Sorry, please enter a time that is greater than 0.", hidden=True)
        else:
            embed = discord.Embed(title = "Giveaway!", description = f'Prize: {prize}')
            embed.add_field(name="To Enter:", value="To enter this giveaway react with a 🎉!")
            min_set = hours*60
            hour_set = mins
            embed.set_footer(text=f"Ends {min_set+hour_set} mintues from now")
            my_msg = await ctx.send(embed = embed)

            await my_msg.add_reaction("🎉")

            new_hour = hours*60*60
            new_min = mins*60
            await asyncio.sleep(new_hour+new_min)

            new_msg = await ctx.channel.fetch_message(my_msg.id)

            users = await new_msg.reactions[0].users().flatten()
            users.pop(users.index(self.client.user))

            winner = random.choice(users)
            await ctx.send(f"Congrats To {winner.mention} For Winning!")



def setup(client):
    client.add_cog(Giveaway(client))