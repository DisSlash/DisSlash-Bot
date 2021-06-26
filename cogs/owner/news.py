import os
import discord
from pymongo import MongoClient
from discord.ext import commands

MONGODB = os.environ["MONGODB"]


class News(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def news(self, ctx, newsUpdate):

        author = ctx.author.id
        cluster = MongoClient(MONGODB)
        db = cluster["disslash"]
        news = db["news"]
        count = news.count_documents({})

        post = {"_id": count + 1, "news": newsUpdate}
        news.insert_one(post)

        embed = discord.Embed(title="New News Update")
        embed.add_field(name="`New News`", value=newsUpdate)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(News(client))
