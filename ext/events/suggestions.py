# import modules
import discord
from discord.ext import commands
import random

# import other files
import settings

# logger
logger = settings.logging.getLogger("bot")

# if debug, conf should be this and if not, conf should be that
if not settings.Config.debug:
    conf = settings.Config.Main
else:
    conf = settings.Config.Debug


# make cog
class Suggestions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # look for messages
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        ...
        # checks if the message is in the target guild, in the taget channel, if the author is a bot, if the message has embeds, and if the author is not itself
        if (
            message.type == discord.MessageType.default
            and message.channel.guild.id == conf.guildid
            and message.channel.id == conf.suggestionchannelid
            and message.author.bot
            and message.embeds != None
            and message.author != self.bot
        ):
            # creates a thread on the message :)
            await message.create_thread(name=message.embeds[0].description[:100])
    
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction: discord.Reaction, user: [discord.Member, discord.User]):
        if user.bot == False:
            msg = reaction.message
            if reaction.message.channel == self.bot.get_guild(conf.guildid).get_channel(conf.suggestionchannelid):
                for r in msg.reactions:
                    if r != reaction:
                        async for u in r.users():
                            if u == user:
                                await r.remove(u)

    @commands.group(breif="Suggestion commands", description="Suggestion commands")
    async def suggest(self, ctx: commands.Context):
        if ctx.subcommand_passed is None:
            return ctx.reply(
                content="{ctx.subcommand_passed} is not part of the suggest group.",
                delete_after=60,
                mention_author=False,
            )

    @suggest.command(
        breif="Suggest a server feature.", description="Suggest a server feature."
    )
    async def create(self, ctx: commands.Context, *feature: str):
        if feature == ():
            return await ctx.reply(content="Please put in a suggestion...", mention_author=False)
        description = " ".join(feature)
        suggestion_id = random.randrange(1001, 10001)
        embed = discord.Embed(
            description=description,
            colour=discord.Colour.blurple(),
        )
        embed.set_author(icon_url=ctx.author.display_avatar, name=ctx.author.display_name)
        channel = self.bot.get_guild(conf.guildid).get_channel(conf.suggestionchannelid)
        async with ctx.typing():
            msg = await channel.send(embed=embed)
            await msg.add_reaction("<:agree:1167505718535008256>")
            await msg.add_reaction("<:neutral:1167505790723170414>")
            await msg.add_reaction("<:disagree:1167505754098507817>")
            return await ctx.reply(content=f"I've sent your suggestion to {msg.channel.mention}.", mention_author=False)

    @suggest.command(
        breif="(STAFF) Note that a server suggestion has been implemented.", description="(STAFF) Note that a server suggestion has been implemented."
    )
    async def implemented(self, ctx: commands.Context):
        if commands.has_permissions(manage_channels=True) or commands.has_permissions(administrator=True):
            if ctx.channel.type == discord.ChannelType.public_thread:
                message = await ctx.channel.parent.fetch_message(ctx.channel.id)
                if message.channel.id != conf.suggestionchannelid or message.embeds == None:
                    return await ctx.reply(content="Please make sure you are in the thread attached to a suggestion!")
                embed = message.embeds[0]
                emb = discord.Embed(title=embed.title, description=embed.description, colour=discord.Colour.brand_green())
                emb.set_author(icon_url=ctx.author.display_avatar, name=ctx.author.display_name)
                for reaction in message.reactions:
                    emb.add_field(name=reaction.emoji, value=(reaction.count - 1), inline=True)
                await message.edit(embed=emb)
                await message.clear_reactions()
                await ctx.reply(content="Marked as implemented!", mention_author=False)
                return await ctx.channel.edit(archived=True)
            else:
                return await ctx.reply(content="Please make sure you are in the thread attached to a suggestion!")
        else:
            return await ctx.reply(content="You don't have the permissions to mark this suggestion as implemented.")


# add cog to bot
async def setup(bot: commands.Bot):
    await bot.add_cog(Suggestions(bot))
    logger.info("ext.events.suggestions okay")
