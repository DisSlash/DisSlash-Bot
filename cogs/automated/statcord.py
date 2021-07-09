from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash import cog_ext, SlashContext

import statcord


class StatcordPost(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.key = "statcord.com-hniEzrGCuz5q7RkaDqj0"
        self.api = statcord.Client(self.client, self.key)
        self.api.start_loop()

    @commands.Cog.listener()
    async def on_command(self, ctx):
        self.api.command_run(ctx)
    
    @commands.Cog.listener()
    async def on_slash_command(self, ctx: SlashContext):
        name = ctx.name
        print(name)



def setup(client):
    client.add_cog(StatcordPost(client))
