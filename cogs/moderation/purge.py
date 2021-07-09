import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice


class Purge(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(
        name="purge",
        description="Warn A Member From This Server",
        options=[
            create_option(
                name="ammount",
                description="Pick An Amount Of Numbers You Want To Delete",
                option_type=4,
                required=True,
            )
        ],
    )
    @commands.has_permissions(kick_members=True)
    @commands.guild_only()
    async def purge(self, ctx, ammount):
        if ammount > 50:
            await ctx.send(
                "Sorry, you can not purge over 50 massages at 1 time.", hidden=True
            )
        else:
            await ctx.channel.purge(limit=ammount)
            embedVar = discord.Embed(
                description=f"{ammount} messages were successfully purged",
                color = 0x242736
            )
            await ctx.send(embed=embedVar)


def setup(client):
    client.add_cog(Purge(client))
