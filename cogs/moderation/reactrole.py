import os
import discord
from discord.ext import commands
from discord_slash.utils.manage_commands import create_option
from discord_slash import cog_ext
from pymongo import MongoClient
from discord_slash.utils import manage_components
from discord_slash.model import ButtonStyle

MONGODB = os.environ["MONGODB"]
cluster = MongoClient(MONGODB)
db = cluster["disslash"]
roles = db["roles"]


class ReactRole(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(
        name="buttonrole",
        description="Make A Button Role",
        options=[
            create_option(
                name="role",
                description="Pick The Role You Want To Give (DisSlash Must Be Higher)",
                option_type=8,
                required=True,
            ),
            create_option(
                name="body",
                description="Enter The Message You Want The Embed To Contain",
                option_type=3,
                required=True,
            ),
            create_option(
                name="title",
                description="Enter The Title You Want The Embed To Contain",
                option_type=3,
                required=False,
            )
        ],
    )
    @commands.has_permissions(kick_members=True)
    @commands.guild_only()
    async def reactrole(self, ctx, role: discord.Role, body, title=None):
        if title == None:
            embed = discord.Embed(description=body, color = 0x242736)
        else:
            embed = discord.Embed(title = title, description=body, color=0x36393F)

        button = manage_components.create_button(
                style=ButtonStyle.blue,
                label=f"Press For The {role.name} Role"
            )


        action_row = manage_components.create_actionrow(button)

        msg = await ctx.send(embed=embed, components=[action_row])



        count = roles.count_documents({})
        new_react_role = {
            "_id": count + 1,
            "role_name": role.name,
            "role_id": role.id,
            "button_id": button["custom_id"],
            "message_id": msg.id
        }

        roles.insert_one(new_react_role)
        


def setup(client):
    client.add_cog(ReactRole(client))
