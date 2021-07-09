import discord
from discord.ext import commands
from discord.ext.commands.core import has_guild_permissions
from discordTogether import DiscordTogether
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice


class Activites(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.togetherControl = DiscordTogether(client)
    
    @cog_ext.cog_slash(
        name="activities",
        description="Play Games Right In The Discord Voice Chat",
        options=[
            create_option(
                name="game",
                description="Pick The Game You Want To Play (More Coming)",
                option_type=3,
                required=True,
                choices=[
                    create_choice(name="youtube", value="youtube"),
                    create_choice(name="poker", value="poker"),
                    create_choice(name="chess", value="chess"),
                    create_choice(name="fishing", value="fishing")
                ]
            )
        ]
    )
    async def activities(self, ctx, game: str):
        print(ctx.member.voice)
        if game == "youtube":

            try:
                link = await self.togetherControl.create_link(ctx.author.voice.channel.id, 'Youtube')
                embed = discord.Embed(title="Join The YouTube Together Session!", description=f'Link: {link}', color = 0x242736)
                embed.set_image(url='https://i.imgur.com/Zlr2KRf.png')
                await ctx.send(embed=embed)
            except:
                await ctx.send("You must be in a VC to run this command", hidden=True)

        elif game == "poker":

            try:
                link = await self.togetherControl.create_link(ctx.author.voice.channel.id, 'Poker')
                embed = discord.Embed(title="Join The Live Poker Game!", description=f'Link: {link}', color = 0x242736)
                embed.set_image(url='https://support.discord.com/hc/article_attachments/1500015218941/Screen_Shot_2021-05-06_at_1.46.50_PM.png')
                await ctx.send(embed=embed)
            except:
               await ctx.send("You must be in a VC to run this command", hidden=True) 
        
        elif game == "chess":

            try:
                link = await self.togetherControl.create_link(ctx.author.voice.channel.id, 'Chess')
                embed = discord.Embed(title="Join The Live Chess Game!", description=f'Link: {link}', color = 0x242736)
                embed.set_image(url='https://i.imgur.com/IOBgl51.png')
                await ctx.send(embed=embed)
            except:
               await ctx.send("You must be in a VC to run this command", hidden=True) 

        elif game == "fishing":

            try:
                link = await self.togetherControl.create_link(ctx.author.voice.channel.id, 'Fishing')
                embed = discord.Embed(title="Join The Live Fishing Game!", description=f'Link: {link}', color = 0x242736)
                embed.set_image(url='https://i.imgur.com/uF3onBd.png')
                await ctx.send(embed=embed)
            except:
               await ctx.send("You must be in a VC to run this command", hidden=True) 
        

def setup(client):
    client.add_cog(Activites(client))