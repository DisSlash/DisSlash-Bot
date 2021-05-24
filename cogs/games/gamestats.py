import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice

import hypixel

whitelist = [710194014569234462]
API_KEYS = ['fa8266d7-65bc-4aba-b01c-fc8c4ceb04e2']
hypixel.setKeys(API_KEYS)


class GameStats(commands.Cog):

    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(name="gamestats",
                       description="Get Live Stats For Any Player On Game!",
                       options=[
                           create_option(
                               name="game",
                               description="Pick The Game You Want To Get Stats For",
                               option_type=3,
                               required=True,
                               choices=[
                                   create_choice(
                                       name="fortnite",
                                       value="fortnite"
                                   ),
                                   create_choice(
                                       name="hypixel",
                                       value="hypixel"
                                   )
                               ]),
                           create_option(
                               name="username",
                               description="Enter The Username Of The Player",
                               option_type=3,
                               required=True
                           )
                       ])
    async def gamestats(self, ctx, game: str, username=None):
        author = ctx.author.id
        usernameLower = username.lower()
        if author in whitelist:
            if game == "fortnite":
                await ctx.send("Sorry, This Command Is Disabled")

            elif game == "hypixel":
                try:
                    PlayerHypixel = hypixel.Player(usernameLower)
                    PlayerHypixel = PlayerHypixel.getName()
                    PlayerLevel = PlayerHypixel.getLevel()
                    PlayerGuild = PlayerHypixel.getGuildID()
                    PlayerKarma = PlayerHypixel.JSON['karma']

                    embed = discord.Embed(title=f'Hypixel Stats For {PlayerHypixel}')
                    embed.add_field(name='Player Level', value=f'{PlayerHypixel}\'s Level Is {PlayerLevel}')
                    embed.add_field(name='Player Karma', value=f'{PlayerHypixel}\'s Karma Is {PlayerKarma}')
                    embed.add_field(name='Player Guild', value=f'{PlayerHypixel}\'s Is In Guild {PlayerGuild}')
                    embed.set_image(url='https://i.imgur.com/kpuiDZf.jpg')
                    await ctx.send(embed=embed)

                except hypixel.PlayerNotFoundException:
                    await ctx.send("Please Enter A Valid Username", hidden=True)

        else:
            await ctx.send(
                "Looks Like You Found A Special Command, Become A Pateron Today To Use It, Or Wait Until It Is Out of Beta!",
                hidden=True)


def setup(client):
    client.add_cog(GameStats(client))


