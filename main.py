# import modules
import discord
from discord.ext import commands
from typing import Optional
import time

# import other files
import settings

# logger
logger = settings.logging.getLogger("bot")

# make bot
bot = commands.Bot(
    command_prefix=".", intents=discord.Intents.all(), status=discord.Status.dnd
)

# prefix stuff
if settings.Config.debug:
    bot.command_prefix = "n."
else:
    bot.command_prefix = "b."

# activity
activity = discord.Activity(
    type=discord.ActivityType.watching, name="the BBC News channel"
)


# when reeady :)
@bot.event
async def on_ready():
    # load extensions
    await bot.load_extension("ext.events.suggestions")
    await bot.load_extension("ext.commands.bloopers")
    # set status
    await bot.change_presence(status=discord.Status.online, activity=activity)
    # send info in log
    logger.info("bot redy :)")


@bot.command(
    brief="My source code!!!",
    description="I'm hosted on Google Cloud and my code is hosted on Github!",
)
async def source(ctx: commands.Context):
    return await ctx.reply(
        content="https://github.com/valbuilds/bee-bee-see-bot", mention_author=False
    )


@bot.command(
    brief="Syncs application commands with Discord.",
    description="(OWNER ONLY) Syncs application commands with Discord.",
)
@commands.is_owner()
async def sync(ctx: commands.Context):
    async with ctx.typing():
        await bot.tree.sync()
    return await ctx.reply(content="Commands synced!", mention_author=False)


@bot.command(
    brief="that bin be floating tho",
    description="silly little bin floating video :)))))",
)
async def bin(ctx: commands.Context):
    async with ctx.typing():
        return await ctx.reply(file=discord.File("src/bin.mp4"), mention_author=False)


@bot.command(
    breif="FACTS ON BAGUETTES",
    description="Christian Frazier brings you some very cool facts on baguettes!",
)
async def baguette(ctx: commands.Context):
    async with ctx.typing():
        return await ctx.reply(
            file=discord.File("src/baguette.mp4"), mention_author=False
        )


@bot.command(breif="hoo™️ and its subsidiaries :)", description="hoo™️")
async def hoo(ctx: commands.Context, subsidiary: str):
    async with ctx.typing():
        time.sleep(5)
        embed = discord.Embed(
            title="the hoo™ corporation and its subsidiaries",
            description="hoocorder™\nhooter™\nhoocord™\nhoolite™\nhoolink™\nhoogo™\nhooplayer™\nhootube™\nhoopedia™\nhooview™\nhootv™\nhooair™\nhooimageremovebgpreview_1™\nhoolabs™\nhoobot™\nhooradio™\nhooPhone™\nhooflix™\nhooNLI™\nhoopay™\nhooparty™\nhoonews™\nhoopolice™\nhoomusic™",
            colour=0xFF0500,
        )
        r = await ctx.reply(embed=embed, mention_author=False)
        return await r.reply(
            content="Need the hoo™️ council? No you don't.",
            file=discord.File("src/hoo.mov"),
            mention_author=False,
        )


@bot.command(
    breif="dont mess with maryam >:)", description="maryam doesn't mess around!"
)
async def dontmess(ctx: commands.Context):
    async with ctx.typing():
        return await ctx.reply(
            file=discord.File("src/dontmesswithmaryam.mp4"), mention_author=False
        )


# run bot
bot.run(settings.Config.token, root_logger=False)
