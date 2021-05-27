import discord
from discord.ext import commands
from pyongo import MongoClient

MONGODB = os.environ["MONGODB"]
cluster = MongoClient(MONGODB)

db = cluster['disslash']
users = db['premium']

class AddUser(commands.Cog):
  
  def __init__(self, client):
        self.client = client
  
  @client.command()
  @commands.is_owner()
  async def adduser(self, ctx, userid):
    author = ctx.author.id
    count = users.count_documents({})
    post = {"_id": count + 1, "userid": userid}
    users.insert_one(post)
    
    await author.send("I Have Succsessfully Added A New User To Receve Premium Benifits") 
    
    try:
      embed = discord.Embed(title="You Now Have Premium Benifits!!!!!")
      embed.add_field(name="**What Command Perks Are There?**", value="You Now Get Certain Commands That Only Are Accsessible By Premium Users, As Well As Accsess To Any Developemnt Commands!")
      embed.add_field(name="**Any Server Benifits**", value="If You Join Our Server, You Will Automaticly Get Accsess To The VIP Role, And Accsess To Testing Channels")
      embed.set_thumbnail(url="https://i.imgur.com/US4aSgW.png")
      await userid.send(embed=embed)
    except:
      await author.send("Sorry, I Was Unable To Send The User A Message")
      
def setup(client):
  client.add_cog(Stats(client))
