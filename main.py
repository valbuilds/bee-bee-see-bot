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
    # await bot.load_extension("ext.commands.utility")
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


@bot.tree.command(description="hoo™️ and its subsidiaries :)")
async def hoo(interaction: discord.Interaction):
    embed = discord.Embed(
        title="the hoo™ corporation and its subsidiaries",
        description="hoocorder™\nhooter™\nhoocord™\nhoolite™\nhoolink™\nhoogo™\nhooplayer™\nhootube™\nhoopedia™\nhooview™\nhootv™\nhooair™\nhooimageremovebgpreview_1™\nhoolabs™\nhoobot™\nhooradio™\nhooPhone™\nhooflix™\nhooNLI™\nhoopay™\nhooparty™\nhoonews™\nhoopolice™\nhoomusic™",
        colour=0xFF0500,
    )
    embed.set_image(url="https://cdn.discordapp.com/attachments/1016691910158590032/1163233026797486120/youtube-VG5WkQEybY0.mov?ex=65480ead&is=653599ad&hm=e41d8ce15b0b15486063ec78909247877c2d3c118c7c3852ada80e1b45fd8e10&")
    r = await interaction.response.send_message(embed=embed, ephemeral=True)


@bot.command(
    breif="dont mess with maryam!!!!!", description="maryam doesn't mess around!"
)
async def dontmess(ctx: commands.Context):
    async with ctx.typing():
        return await ctx.reply(
            file=discord.File("src/dontmesswithmaryam.mp4"), mention_author=False
        )

@bot.command(
    breif="utter chaos :)",description="real bbc news countdown 2034"
)
async def chaos(ctx: commands.Context):
    async with ctx.typing():
        return await ctx.reply(content="[.](https://cdn.discordapp.com/attachments/1016691910158590032/1166740804728000592/help.mp4?ex=654b970c&is=6539220c&hm=1b8669e00b9a9e715f37092cc95b1ae8529e3a9d4f789c7ba987b6595e2d8289&)", mention_author=False)

@bot.command(
    breif="good morning from aaron :)))",
    description="good morning from aaron :)))"
)
async def gm(ctx: commands.Context):
    async with ctx.typing():
        return await ctx.reply(file=discord.File('src/gm.mp4'), mention_author=False)

# run bot
bot.run(settings.Config.token, root_logger=False)
