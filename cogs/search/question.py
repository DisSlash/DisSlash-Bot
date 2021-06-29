import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice
import os
import openai

class Questions(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @cog_ext.cog_slash(
        name="question",
        description="Ask OpenAI Any Question!",
        options=[
            create_option(
                name="query",
                description="What Question Do You Want To Ask Open AI?",
                option_type=3,
                required=True,
            )
        ],
    )
    async def question(self, ctx, query):

        openai.api_key = os.environ['OPENAI']

        response = openai.Answer.create(
            model="curie",
            question=query, 
            examples_context="In 2017, U.S. life expectancy was 78.6 years.", 
            examples=[["What is human life expectancy in the United States?","The human life expectancy is 78 years."]],
            stop=["\n", "<|endoftext|>"],
            documents=[], 
        )

        answer_list = response['answers']
        answer = answer_list[0]
        embed = discord.Embed(title="You Asked OpenAI A Question!")
        embed.add_field(name=f'Question: {query}', value=f'Answer: {answer}')
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Questions(client))        