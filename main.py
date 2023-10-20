# import modules
import discord
from discord.ext import commands

# import other files
import settings

# logger
logger = settings.logging.getLogger("bot")

# make bot
bot = commands.Bot(command_prefix=".", intents=discord.Intents.all(), status=discord.Status.dnd)

# prefix stuff
if settings.Config.debug:
    bot.command_prefix = "n."
else:
    bot.command_prefix = "b."

# activity
activity = discord.Activity(type=discord.ActivityType.watching, name="the BBC News channel")

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

@bot.command(brief="My source code!!!", description="I'm hosted on Google Cloud and my code is hosted on Github!")
async def source(ctx: commands.Context):
    return await ctx.reply(content="https://github.com/valbuilds/bee-bee-see-bot", mention_author=False)

@bot.command(brief="Syncs application commands with Discord.", description="(OWNER ONLY) Syncs application commands with Discord.")
@commands.is_owner()
async def sync(ctx: commands.Context):
    async with ctx.typing():
        await bot.tree.sync()
    return await ctx.reply(content="Commands synced!", mention_author=False)

# run bot
bot.run(settings.Config.token, root_logger=False)