import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice

class Kick(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @cog_ext.cog_slash(name="kick",
             description="Kick A Member From This Server",
             options=[
               create_option(
                 name="member",
                 description="This Command Will Only Work If You Are A Mod",
                 option_type=6,
                 required=True
               ),
               create_option(
                 name="reason",
                 description="Add A Reason For Kicking This User",
                 option_type=3,
                 required=False
               )
             ])
    @commands.has_permissions(kick_members=True)
    @commands.guild_only()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        embedVar = discord.Embed(description=f'{member.mention} has been kicked successfully for {reason}', color=0xFF0000)
        await ctx.send(embed=embedVar)

def setup(client):
    client.add_cog(Kick(client))