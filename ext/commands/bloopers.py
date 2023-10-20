# import modules
import discord
from discord.ext import commands
import random
import datetime
import time
import pytz

# import other files
import settings

# logger
logger = settings.logging.getLogger("bot")

# check time
async def check_time(time: str):
    if time[2] != ":":
        return False
    else:
        if time.split(':')[0].isnumeric() and time.split(':')[1].isnumeric():
            return True
        else:
            return False

# turn text into timestamp
def texttime_to_timestamp(timee: str):
    now = datetime.datetime.now(pytz.timezone('Europe/London'))
    t = timee.split(":")
    timea = datetime.datetime(now.year, now.month, now.day, int(t[0]) + 6, int(t[1]), 0, 0)
    return str(int(time.mktime(timea.timetuple())))

# cog
class Bloopers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # command group
    @commands.group(breif="Blooper commands!")
    async def blooper(self, ctx: commands.Context):
        if ctx.subcommand_passed is None:
            return ctx.reply(content="{ctx.subcommand_passed} is not part of the bloopers group.", delete_after=60, mention_author=False)

    # blooper report command
    @blooper.command(breif="Reports a blooper!", description="Reports a blooper to the current channel!")
    async def report(self, ctx: commands.Context, time: str, *description: str):
        id = random.randrange(1001, 10001)
        embed = discord.Embed(title=f"Blooper #{id}", description=f"*Reported by {ctx.author.mention}.*", colour=0x6260DE)
        istime = await check_time(time)
        if not istime:
            return await ctx.reply(content="Please make sure to provide a valid time!", delete_after=60, mention_author=False)
        t = texttime_to_timestamp(time)
        if t != None:
            embed.add_field(name="Time", value=f"<t:{t}:f>")
        embed.add_field(name="Description", value=" ".join(description))
        
        return await ctx.reply(embed=embed, mention_author=False)
    
# add cog to bot
async def setup(bot: commands.Bot):
    await bot.add_cog(Bloopers(bot))
    logger.info("ext.events.suggestions okay")