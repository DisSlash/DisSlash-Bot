import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice


class Poll(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(
        name="poll",
        description="Make A Simple Yes Or No Poll",
        options=[
            create_option(
                name="question",
                description="What Do You Want The Poll To Say",
                option_type=3,
                required=True,
            )
        ],
    )
    @commands.guild_only()
    async def poll(self, ctx, question: str):
        embedVar = discord.Embed(title=f"{question}", color=0x242736)
        embedVar.add_field(
            name="Created With A Slash Command", value="Powered By InSight3D"
        )
        embedVar.add_field(name="👍", value="Yes", inline=True)
        embedVar.add_field(name="👎", value="No", inline=True)
        message = await ctx.send(embed=embedVar)
        await message.add_reaction("👍")
        await message.add_reaction("👎")


def setup(client):
    client.add_cog(Poll(client))
