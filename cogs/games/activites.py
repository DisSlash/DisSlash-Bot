import discord
from discord.ext import commands
from discordTogether import DiscordTogether
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice
from chessdotcom import get_player_profile

class Activites(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.togetherControl = DiscordTogether(client)
    
    @cog_ext.cog_slash(
        name="activites",
        description="Play Games Right In The Discord Voice Chat",
        options=[
            create_option(
                name="game",
                description="Pick The Game You Want To Play (More Comming)",
                option_type=3,
                required=True,
                choices=[
                    create_choice(name="youtube", value="youtube"),
                    create_choice(name="poker", value="poker"),
                ],
            )
        ],
    )
    async def activites(self, ctx, game):
        if game == "youtube":
            voice_state = ctx.member.voice
            if voice_state is None:
                await ctx.send("You must be in a VC to use this command", hidden=True)
            else:
                link = await self.togetherControl.create_link(ctx.author.voice.channel.id, 'Youtube')
                embed = discord.Embed(title="Join The YouTube Together Session!", description=f'Link: {link}')
                embed.set_image(url='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Logo_of_YouTube_(2015-2017).svg/1280px-Logo_of_YouTube_(2015-2017).svg.png')
                await ctx.send(embed=embed)
        elif game == "poker":
            voice_state = ctx.member.voice
            if voice_state is None:
                await ctx.send("You must be in a VC to use this command", hidden=True)
            else:
                link = await self.togetherControl.create_link(ctx.author.voice.channel.id, 'Youtube')
                embed = discord.Embed(title="Join The Live Poker Game!", description=f'Link: {link}')
                embed.set_image(url='https://support.discord.com/hc/article_attachments/1500015218941/Screen_Shot_2021-05-06_at_1.46.50_PM.png')
                await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Activites(client))