import os
import topgg
import asyncio
from pyrandmeme import *
from discord.ext import tasks
from datetime import datetime
from discord.ext import commands
from discord_slash import SlashCommand
from loadcog import list_ext

# Intents
intents = discord.Intents.default()
intents.members = True

# Bot Info Setup
client = commands.Bot(command_prefix="#", intents=intents)
slash = SlashCommand(client, sync_commands=True, sync_on_cog_reload=True)
client.remove_command("help")
client.launch_time = datetime.utcnow()

# Load TOPGG

dbl_token = os.environ["TOPTOKEN"]
client.topggpy = topgg.DBLClient(client, dbl_token, autopost=True)

# Loop
async def status_task():
    while True:
        await client.change_presence(activity=discord.Game(name="/help | #help"))
        await asyncio.sleep(10)
        await client.change_presence(
            activity=discord.Game(name=f"{len(client.guilds)} servers!")
        )
        await asyncio.sleep(10)


@client.event
async def on_ready():
    print("Bot Is Online")
    client.loop.create_task(status_task())


@client.command()
@commands.is_owner()
async def load(ctx, folder, extension):
    client.load_extension(f"{folder}.{extension}")


@client.command()
@commands.is_owner()
async def unload(ctx, folder, extension):
    client.unload_extension(f"{folder}.{extension}")

all_cogs = list_ext()
for cogs in all_cogs:
    client.load_extension(cogs)

@tasks.loop(minutes=30)
async def update_stats():
    """This function runs every 30 minutes to automatically update your server count."""
    try:
        await client.topggpy.post_guild_count()
        print(f"Posted server count ({client.topggpy.guild_count})")
    except Exception as e:
        print("Failed to post server count\n{}: {}".format(type(e).__name__, e))



@client.command()
@commands.is_owner()
async def update(ctx, news):
    await ctx.send(news)


@client.event
async def on_message(message):
    if client.user in message.mentions:
        embed = discord.Embed(
            title="Hey! Im DisSlash",
            description="Use `#help` Or `/help` For More Info!",
        )
        await message.channel.send(embed=embed)
    await client.process_commands(message)

@client.command()
async def uptime(ctx):
    delta_uptime = datetime.utcnow() - client.launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    await ctx.send(f"{days}d, {hours}h, {minutes}m, {seconds}s")
    

update_stats.start()
TOKEN = os.environ["TOKEN"]
client.run(TOKEN)
