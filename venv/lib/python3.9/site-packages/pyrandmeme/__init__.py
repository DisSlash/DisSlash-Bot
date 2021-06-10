import aiohttp
import discord
import random2


async def pyrandmeme():
    pymeme = discord.Embed(title="Meme", description="Meme Request", color=0xe91e63)
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/memes/new.json?sort=hot') as r:
            res = await r.json()
            pymeme.set_image(url=res['data']['children'][random2.randint(0, 25)]['data']['url'])
            return pymeme
        await pyrandmeme()