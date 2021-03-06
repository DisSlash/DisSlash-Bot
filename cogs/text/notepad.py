import discord
import os
from pymongo import MongoClient
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice

MONGODB = os.environ["MONGODB"]


class NotePad(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(
        name="notepad",
        description="A Simple Notepad That Can Be Accsessible In Any Server",
        options=[
            create_option(
                name="action",
                description="Pick To Either Warn A User, Or View Warns (If Warning, You Have To Add Reason)",
                option_type=3,
                required=True,
                choices=[
                    create_choice(name="add", value="add"),
                    create_choice(name="view", value="view"),
                    create_choice(name="list", value="list"),
                ],
            ),
            create_option(
                name="name",
                description="Enter The Name Of The Note",
                option_type=3,
                required=True,
            ),
            create_option(
                name="content",
                description="Please Enter The Body Of The Note",
                option_type=3,
                required=False,
            ),
        ],
    )
    async def notepad(self, ctx, action: str, name: str, *, content=None):
        author = ctx.author.id
        cluster = MongoClient(MONGODB)
        db = cluster["disslash"]
        notes = db["notes"]

        noteName = name.lower()

        if action == "add":

            if name == "None":
                await ctx.send("Please Enter A Name For This Note", hidden=True)
            else:
                # Add Post

                post = {
                    "user": author,
                    "note": content,
                    "name": noteName,
                }
                notes.insert_one(post)

                # Embed
                embed = discord.Embed(title=f"A New Note Has Been Made!", color = 0x242736)
                embed.add_field(name="Name Of Note", value=f"{name}", inline=False)
                embed.add_field(name="Content", value=f"{content}", inline=False)
                await ctx.send(embed=embed)

        elif action == "view":
            try:

                noteFinal = notes.find({"name": noteName, "user": author})

                for query in noteFinal:
                    contentOfNote = query["note"]

                embed = discord.Embed(title=f"New Note Query", color = 0x242736)
                embed.add_field(name=f"Note Name", value=f"{noteName}", inline=False)
                embed.add_field(
                    name="Note Content", value=f"{contentOfNote}", inline=False
                )
                await ctx.send(embed=embed)

            except:
                await ctx.send("This Is Not A Valid Note", hidden=True)

        elif action == "list":
            userNote = notes.find({"user": author})

            embed = discord.Embed(title=f"Notes Listing Query",color = 0x242736)

            for notes in userNote:
                name = notes["name"]
                _id = notes["_id"]
                embed.add_field(
                    name=f"Note ID (Query): {_id}",
                    value=f"Name Of Note: {name}",
                    inline=False,
                )

            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(NotePad(client))
