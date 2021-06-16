import discord
import contextlib
import io
import textwrap
from discord.ext import commands
from discord.ext.buttons import Paginator

class Pag(Paginator):
    async def teardown(self):
        try:
            await self.page.clear_reactions()
        except discord.HTTPException:
            pass


def clean_code(content):
    if content.startwith("```") and content.endwith("```"):
        return "\n".join(content.split("\n")[1:][:-3])

    return content

class Eval(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def eval(self, ctx, *, code):
        code = clean_code(code)

        local_variables = {
            "discord": discord,
            "commands": commands,
            "ctx": ctx,
            "channel": ctx.channel,
            "author": ctx.author,
            "guild": ctx.guild,
            "message": ctx.message
        }

        stdout = io.StringIO()

        try:
            with contextlib.redirect_stdout(stdout):
                exec(
                    f"async def func():\n{textwrap.indent(code, '    ')}", local_variables,
                )

                obj = await local_variables["func"]()
                result = f"{stdout.getvalue()}\n-- {obj}\n"
        except Exception as e:
            result = "".join(format_exception(e, e, e.__traceback__))

        pager = Pag(
            timeout=100,
            entries=[result[i: i + 2000] for i in range(0, len(result), 2000)],
            length=1,
            prefix="```py\n",
            suffix="```"
        )

        await pager.start(ctx)
