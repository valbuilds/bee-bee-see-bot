import discord
from discord.ext import commands
from typing import Optional

class Incompetency(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def blooper(self, ctx: commands.Context, *description: str):
        d = " ".join(description)
        c = ctx.bot.get_guild(1016626731785928715).get_channel(1016692053280817172)
        e = discord.Embed(title="Blooper reported!", description=f"Reported by: {ctx.author.mention}", colour=discord.Colour.brand_red())
        e.add_field(name="Description of blooper", value=d)
        cm = await c.send(embed=e)
        await cm.create_thread(name=f"Thread for {ctx.author.display_name}", reason="Blooper reported")
        await ctx.reply(content=cm.jump_url)

async def setup(bot):
    await bot.add_cog(Incompetency(bot))
    print("commands.incompetency ready :)")