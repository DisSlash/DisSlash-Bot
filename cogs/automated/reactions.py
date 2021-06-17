import os
import discord
from pymongo import MongoClient
from discord.ext import commands

MONGODB = os.environ["MONGODB"]
cluster = MongoClient(MONGODB)
db = cluster["disslash"]
roles = db["roles"]

class Reactions(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):

        if payload.member.bot:
            pass

        else:
            try:
                data = roles.find({"emoji": payload.emoji.name, "message_id": payload.message_id})
                for i in data:
                    role_id = i["role_id"]
                role = discord.utils.get(self.client.get_guild(payload.guild_id).roles, id=role_id)

                await payload.member.add_roles(role)

            except UnboundLocalError:
                pass
    
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):

        try:
            data = roles.find({"emoji": payload.emoji.name, "message_id": payload.message_id})
            for i in data:
                role_id = i["role_id"]
            role = discord.utils.get(self.client.get_guild(payload.guild_id).roles, id=role_id)

            await self.client.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(role)

        except UnboundLocalError:
            pass

    
def setup(client):
    client.add_cog(Reactions(client))
