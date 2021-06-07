import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice


class Nickname(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(
        name="nickname",
        description="Change/Add A Nickname For A Member",
        options=[
            create_option(
                name="member",
                description="This Will Only Work If You Are A Mod",
                option_type=6,
                required=True,
            ),
            create_option(
                name="nickname",
                description="Pick The Name You Want To Assign To The User",
                option_type=3,
                required=True,
            ),
        ],
    )
    @commands.has_permissions(kick_members=True)
    @commands.guild_only()
    async def nick(self, ctx, member: discord.Member, nickname: str):
        await member.edit(nick=nickname)
        embedVar = discord.Embed(
            description=f"Nickname was changed to {nickname} succsesfuly"
        )
        await ctx.send(embed=embedVar)


def setup(client):
    client.add_cog(Nickname(client))
