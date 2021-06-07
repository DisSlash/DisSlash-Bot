import discord
from covid import Covid
from discord.ext import commands
from discord_slash import cog_ext, SlashContext

# Pull Covid Info
covid = Covid(source="worldometers")
covid.get_data()
active = covid.get_total_active_cases()
confirmed = covid.get_total_confirmed_cases()
recovered = covid.get_total_recovered()
deaths = covid.get_total_deaths()


class Covid(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(name="covid", description="Get Info On Worldwide Covid Cases")
    async def covid(self, ctx):
        embedVar = discord.Embed(title="Worldwide Covid Cases")
        embedVar.add_field(name="Active Cases", value=active, inline=False)
        embedVar.add_field(name="Confirmed Cases", value=confirmed, inline=False)
        embedVar.add_field(name="Recovered", value=recovered, inline=False)
        embedVar.add_field(name="Deaths", value=deaths, inline=False)
        await ctx.send(embed=embedVar)


def setup(client):
    client.add_cog(Covid(client))
