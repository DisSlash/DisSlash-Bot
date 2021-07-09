import discord
import os
from pymongo import MongoClient
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice

# Database Setup
MONGODB = os.environ["MONGODB"]
cluster = MongoClient(MONGODB)

db = cluster["disslash"]
warns = db["warns"]

# Start Of Command
class Warn(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(
        name="warn",
        description="Warn A Member From This Server",
        options=[
            create_option(
                name="action",
                description="Pick To Either Warn A User, Or View Warns (If Warning, You Have To Add Reason)",
                option_type=3,
                required=True,
                choices=[
                    create_choice(name="warn", value="warn"),
                    create_choice(name="logs", value="logs"),
                ],
            ),
            create_option(
                name="member",
                description="This Command Will Only Work If You Are A Mod",
                option_type=6,
                required=True,
            ),
            create_option(
                name="reason",
                description="Add A Reason For Warning This User",
                option_type=3,
                required=False,
            ),
        ],
    )
    @commands.has_permissions(kick_members=True)
    @commands.guild_only()
    async def warn(self, ctx, action: str, member: discord.Member, reason=None):
        memberid = member.id
        guildid = ctx.guild.id
        if action == "warn":
            if reason == "None":
                await ctx.send("Please Add A Reason In Order To Warn This User")
            else:

                post = {
                    "user": memberid,
                    "reason": reason,
                    "guild": guildid,
                }
                warns.insert_one(post)

                embedVar = discord.Embed(
                    description=f"{member.mention} has been warned",
                    color = 0x242736
                )
                await ctx.send(embed=embedVar)

                await member.send(f"You have been warned, Reason: {reason}")

        elif action == "logs":
            search = warns.find({"user": memberid, "guild": guildid})
            for query in search:
                user = query["user"]
                reason = query["reason"]
                guild = query["guild"]

            reasonCount = warns.count_documents({"user": memberid, "guild": guildid})

            if reasonCount == 0:
                await ctx.send("This User Has Never Been Warned", hidden=True)
            else:
                embed = discord.Embed(title=f"Warn Stats For {member.name}")
                embed.add_field(
                    name=f"Amount Of Warns",
                    value=f"{member.mention} Has Been Warned {reasonCount} Times",
                )
                await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Warn(client))
