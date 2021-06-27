import discord
import wikipediaapi
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice


class Wikipedia(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(
        name="wiki",
        description="A Simple Wikipedea Search",
        options=[
            create_option(
                name="query",
                description="What Do You Want To Search Up?",
                option_type=3,
                required=True,
            )
        ],
    )
    async def wiki(self, ctx, query):
        await ctx.send("I have sent the result to your DM.", hidden=True)
        author = ctx.author
        
        query = " ".join(query)
        wiki_wiki = wikipediaapi.Wikipedia("en")
        page_py = wiki_wiki.page(query)
        question = query
        query = query.replace(" ", "")

        if page_py.exists():
            embedVar = discord.Embed(
                title=f"Result:",
                description=f"%s" % page_py.summary[0:400]
                + f"[...](https://en.wikipedia.org/wiki/{query})",
            )
            await author.send(embed=embedVar)
        else:
            embedVar = discord.Embed(description="Sorry, this page does not exist.", hidden=True)
            await ctx.send(embed=embedVar)



def setup(client):
    client.add_cog(Wikipedia(client))
