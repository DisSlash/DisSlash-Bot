import discord
from discord.ext import commands
from dhooks import Webhook


class Guild(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        hook = Webhook(
            "https://discord.com/api/webhooks/844645105235132436/KJwdVbkrYLeD8EKPhQsvKK2uRUR7nSH9lysHJC2hsH1Esr9-97zEl2UPcbhBmiCKwSrr"
        )
        name = str(guild.name)
        owner = str(guild.owner)
        guildid = str(guild.id)
        memberCount = str(guild.member_count)
        icon = str(guild.icon_url)

        embed = discord.Embed(title="DisSlash Is In A New Guild!")
        embed.set_thumbnail(url=icon)
        embed.add_field(name="Guild Name", value=f"{name}", inline=False)
        embed.add_field(name="Guild ID", value=f"{guildid}", inline=False)
        embed.add_field(name="Member Count", value=f"{memberCount}", inline=False)
        hook.send(embed=embed)


def setup(client):
    client.add_cog(Guild(client))
