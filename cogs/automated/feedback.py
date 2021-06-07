import discord
from dhooks import Webhook
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice


class Feedback(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(
        name="feedback",
        description="Have Feedback For DisSlash, Send It Here",
        options=[
            create_option(
                name="responce",
                description="Please Enter You Feedback Here",
                option_type=3,
                required=True,
            )
        ],
    )
    async def feedback(self, ctx, responce: str):
        hook = Webhook(
            "https://discord.com/api/webhooks/836672592294576158/rMr69PZ8I7uNYhxMS_7zO1Oay29u7OZ1T7Rj_tI2oQ1mklpqC8JypUfUHcSekLUWRzVq"
        )
        await ctx.send("Thanks for your feedback, it means a lot to us!", hidden=True)
        user = ctx.author.id
        embed = discord.Embed(title=f"DisSlash Feedback!", description=f"{responce}")
        hook.send(embed=embed)


def setup(client):
    client.add_cog(Feedback(client))
