import discord
import os
from pymongo import MongoClient
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice
from pymongo.common import validate_uuid_representation

MONGODB = os.environ["MONGODB"]
cluster = MongoClient(MONGODB)

db = cluster['disslash']
notes = db['notes']

class NotePad(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @cog_ext.cog_slash(name="notepad",
          description="A Simple Notepad That Can Be Accsessible In Any Server",
          options=[
            create_option(
              name="action",
              description="Pick To Either Warn A User, Or View Warns (If Warning, You Have To Add Reason)",
              option_type=3,
              required=True,
              choices=[
              create_choice(
                name="add",
                value="add"
              ),
              create_choice(
                name="view",
                value="view"
              )
              ]),
            create_option(
              name="content",
              description="Please Enter The Body Of The Note",
              option_type=3,
              required=True
            ),
            create_option(
              name="name",
              description="Enter The Name Of The Note",
              option_type=3,
              required=True
            )
          ])
    async def notepad(self, ctx, action: str, content: str, name: str):
      author = ctx.author.id
      docCount = notes.count_documents({})
      noteName = name.lower()
      if action == "add":

        # Add Post
        post = {"_id": docCount + 1, "user": author, "note": content, "name": noteName}
        notes.insert_one(post)

        # Embed
        embed = discord.Embed(title=f'A New Note Has Been Made!')
        embed.add_field(name="Name Of Note", value=f'{name}')
        embed.add_field(name="Content", value=f'{content}')
        await ctx.send(embed=embed)

      elif action == "view":
        
        try:
          search = notes.find({"user": author})

          for query in search:
            nameNote = query['name']

          if noteName in nameNote:
            noteFinal = notes.find({"name": noteName})
            for query in noteFinal:
              nameOfNote = query['name']
              contentOfNote = query['note']
            embed = discord.Embed(title=f'New Note Query')
            embed.add_field(name=f'Note Name: {nameOfNote}', vlaue=f'{contentOfNote}')
            await ctx.send(embed=embed)

          else:
            await ctx.send("That Is Not A Valid Note!", hidden=True)
        except:
          await ctx.send("There Has Been An Error, Please DM Neil Shah#6469", hidden=True)
        
