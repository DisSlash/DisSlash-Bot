import os
import discord
from discord.ext import commands
from pymongo import MongoClient

MONGODB = os.environ["MONGODB"]
cluster = MongoClient(MONGODB)

db = cluster['disslash']
users = db['premium']

class AddUser(commands.Cog):
  
  def __init__(self, client):
        self.client = client
  
  @commands.command()
  @commands.is_owner()
  async def adduser(self, ctx, member: discord.Member):
    author = ctx.author.id
    userid = member.id
    count = users.count_documents({})
    post = {"_id": count + 1, "userid": userid}
    users.insert_one(post)
    print("Added Post")
    await ctx.send("I Have Succsessfully Added A New User To Receve Premium Benifits") 
    
    try:
      embed = discord.Embed(title="You Now Have Premium Benifits!!!!!")
      embed.add_field(name="**What Command Perks Are There?**", value="You Now Get Certain Commands That Only Are Accsessible By Premium Users, As Well As Accsess To Any Developemnt Commands!", inline=False)
      embed.add_field(name="**Any Server Benifits?**", value="If You Join Our Server, You Will Automaticly Get Accsess To The VIP Role, And Accsess To Testing Channels", inline=False)
      embed.set_thumbnail(url="https://i.imgur.com/US4aSgW.png")
      await member.send(embed=embed)
    except:
      await ctx.send("Sorry, I Was Unable To Send The User A Message")
      
def setup(client):
  client.add_cog(AddUser(client))
