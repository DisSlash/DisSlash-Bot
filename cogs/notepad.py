import discord
from pymongo import MongoClient
from discord.ext import commands

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
          post = {"_id": docCount + 1, "user": author, "note": content}
        elif action == "view":
          pass
