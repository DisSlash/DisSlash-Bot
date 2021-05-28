import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord.ext.commands import has_permissions, CheckFailure
from discord.ext.commands import has_role
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext.commands import cooldown, BucketType

class Error(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_slash_command_error(self, ctx: SlashContext, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You Can Not Use This Command.", hidden=True)
            
        elif isinstance(error, commands.NoPrivateMessage):
            try:
                await ctx.send("You Can Not Use This Command In A DM.", hidden=True)
            except discord.HTTPException:
                pass
            
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send("Sorry, DisSlash Does Not Have The Proper Perms To Execute This Command", hidden=True)
            
        elif isinstance(error, commands.CommandNotFound):
            print("A Invalid Command Has Been Used")
        
        else:
            raise error

def setup(client):
    client.add_cog(Error(client))
