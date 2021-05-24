import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice

class Warn(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @cog_ext.cog_slash(name="warn",
             description="Warn A Member From This Server",
             options=[
               create_option(
                 name="member",
                 description="This Command Will Only Work If You Are A Mod",
                 option_type=6,
                 required=True
               ),
               create_option(
                 name="reason",
                 description="Add A Reason For Warning This User",
                 option_type=3,
                 required=True
               )
             ])
    @commands.has_permissions(kick_members=True)
    @commands.guild_only()
    async def warn(self, ctx, member: discord.Member, *, reason=None):
        embedVar = discord.Embed(description=f'{member.mention} has been warned')
        await ctx.send(embed=embedVar)
        await member.send(f'You have been warned, Reason: {reason}')

def setup(client):
    client.add_cog(Warn(client))