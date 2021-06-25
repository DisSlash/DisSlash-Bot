import discord
import os
import png
import qrcode
import pyqrcode
from pyqrcode import QRCode
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice


class QRCode(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(
        name="qr",
        description="Make A QR Code",
        options=[
            create_option(
                name="link",
                description="Please Enter The Link For The QR Code",
                option_type=3,
                required=True,
            )
        ],
    )
    async def qr(self, ctx, link: str):
        await ctx.defer()
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=2,
        )
        qr.add_data(link)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("qr.png")
        embed = discord.Embed(title = "Here Is Your QR Code:")
        embed.set_image(url="qr.png")
#         await ctx.channel.send(file=discord.File("qr.png"))
        await ctx.send(embed=embed)
        os.remove("qr.png")


def setup(client):
    client.add_cog(QRCode(client))
