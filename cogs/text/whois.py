import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice


class WhoIs(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(
        name="whois",
        description="Get Info About A User",
        options=[
            create_option(
                name="user",
                description="Pick A Member To Get Info About",
                option_type=6,
                required=True,
            )
        ],
    )
    @commands.guild_only()
    async def whois(self, ctx, *, user: discord.Member = None):
        if user is None:
            user = ctx.author
        date_format = "%a, %d %b %Y %I:%M %p"
        embed = discord.Embed(color=0x242736, description=user.mention)
        embed.set_author(name=str(user), icon_url=user.avatar_url)
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(
            name="Joined Server",
            value=user.joined_at.strftime(date_format),
            inline=False,
        )
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        embed.add_field(
            name="Join Position", value=str(members.index(user) + 1), inline=False
        )
        embed.add_field(
            name="Joined Discord",
            value=user.created_at.strftime(date_format),
            inline=False,
        )
        if len(user.roles) > 1:
            role_string = " ".join([r.mention for r in user.roles][1:])
            embed.add_field(
                name="Roles [{}]".format(len(user.roles) - 1),
                value=role_string,
                inline=False,
            )
        embed.set_footer(text="ID: " + str(user.id))
        return await ctx.send(embed=embed)


def setup(client):
    client.add_cog(WhoIs(client))
