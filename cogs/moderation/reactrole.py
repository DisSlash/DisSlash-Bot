import os
import discord
from discord.ext import commands
from discord_slash.utils.manage_commands import create_option
from discord_slash import cog_ext
from pymongo import MongoClient

MONGODB = os.environ["MONGODB"]
cluster = MongoClient(MONGODB)
db = cluster["disslash"]
roles = db["roles"]


class ReactRole(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(
        name="reactrole",
        description="Make A Reaction Role",
        options=[
            create_option(
                name="emoji",
                description="Pick An Emoji For The Reaction Role",
                option_type=3,
                required=True,
            ),
            create_option(
                name="role",
                description="Pick The Role You Want To Give (DisSlash Must Be Higher)",
                option_type=8,
                required=True,
            ),
            create_option(
                name="message",
                description="Enter The Message You Want The Embed To Contain",
                option_type=3,
                required=True,
            ),
        ],
    )
    @commands.has_permissions(manage_server=True)
    @commands.guild_only()
    async def reactrole(self, ctx, emoji, role: discord.Role, message):
        try:
            embed = discord.Embed(description=message)
            msg = await ctx.channel.send(embed=embed)
            await msg.add_reaction(emoji)

            count = roles.count_documents({})
            new_react_role = {
                "_id": count + 1,
                "role_name": role.name,
                "role_id": role.id,
                "emoji": emoji,
                "message_id": msg.id,
            }

            roles.insert_one(new_react_role)

        except:
            await ctx.send(
                "Please Enter Only The Emoji, No Text. If It Still Does Not Work, Please DM Neil Shah!",
                hidden=True,
            )


def setup(client):
    client.add_cog(ReactRole(client))
