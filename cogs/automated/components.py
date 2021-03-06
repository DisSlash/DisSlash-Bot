import os
import discord
from discord.ext import commands
from pymongo import MongoClient
from discord_slash.utils import manage_components
from discord_slash.model import ButtonStyle
from discord_slash.context import ComponentContext

MONGODB = os.environ["MONGODB"]
cluster = MongoClient(MONGODB)
db = cluster["disslash"]
roles = db["roles"]

class ReactionsComp(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_component(self, ctx: ComponentContext):
        try:
            data = roles.find({"button_id": str(ctx.custom_id)})
            for i in data:
                role_id = i["role_id"]


            role = discord.utils.get(self.client.get_guild(ctx.guild_id).roles, id=role_id)
            if role in ctx.author.roles:
                await self.client.get_guild(ctx.guild_id).get_member(ctx.author_id).remove_roles(role)
                await ctx.send(f"Hey, You No Longer The {role.name} Role!", hidden=True)
            else:
                await ctx.author.add_roles(role)
                await ctx.send(f"Hey, You Now Have The {role.name} Role!", hidden=True)
        except:
            await ctx.send("Looks Like I Am Missing Perms, So I Will Unable To Give The Role!", hidden=True)

def setup(client):
    client.add_cog(ReactionsComp(client))
        