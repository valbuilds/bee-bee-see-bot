# import modules
import discord
from discord.ext import commands

# import other files
import settings

# logger
logger = settings.logging.getLogger("bot")


# make cog
class Suggestions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # look for messages
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        # if debug, conf should be this and if not, conf should be that
        if not settings.Config.debug:
            conf = settings.Config.Main
        else:
            conf = settings.Config.Debug

        # checks if the message is in the target guild, in the taget channel, if the author is a bot, and if the message has embeds
        if (
            message.channel.guild.id == conf.guildid
            and message.channel.id == conf.suggestionchannelid
            and message.author.bot
            and message.embeds != None
        ):
            # creates a thread on the message :)
            await message.create_thread(name=message.embeds[0].description[:100])


# add cog to bot
async def setup(bot: commands.Bot):
    await bot.add_cog(Suggestions(bot))
    logger.info("ext.events.suggestions okay")
