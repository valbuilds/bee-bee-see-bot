import discord
from discord import app_commands
from discord.ext import commands
import datetime

class SuggestionsA(app_commands.Group):
    @app_commands.command(description="Suggest a profile picture")
    @app_commands.describe(text="Suggest a string of text to Google or something.")
    async def profile(self, interaction: discord.Interaction, text: str):
        c = interaction.client.get_guild(1162403787097509889).get_channel(1162443267082813530)
        e = discord.Embed(title="Suggestion", description=text, timestamp=datetime.datetime.now(), colour=discord.Colour.blurple())
        e.add_field(name="Suggested by", value=interaction.user.mention)
        await c.send(embed=e)
        return await interaction.response.send_message(content="Suggested!", embed=e, ephemeral=True)
    @app_commands.command(description="Suggest a profile picture (Image)")
    @app_commands.describe(image="Suggest an image.")
    async def profile_image(self, interaction: discord.Interaction, image: discord.Attachment):
        c = interaction.client.get_guild(1162403787097509889).get_channel(1162443267082813530)
        if image.content_type.startswith("image"):
            e = discord.Embed(title="Suggestion", timestamp=datetime.datetime.now(), colour=discord.Colour.blurple())
            e.add_field(name="Suggested by", value=interaction.user.mention)
            e.set_image(url=image.proxy_url)
            await c.send(embed=e)
            return await interaction.response.send_message(content="Suggested!", embed=e, ephemeral=True)
        else:
            return await interaction.response.send_message(content="Must be an image!", ephemeral=True)
        
    @app_commands.command(description="Suggest a activity for the bot.")
    @app_commands.describe(name="The name of activity the bot should be doing.")
    @app_commands.describe(type="The type of activity the bot should be doing.")
    @app_commands.choices(type=[
        app_commands.Choice(name="Playing", value=0),
        app_commands.Choice(name="Streaming", value=1),
        app_commands.Choice(name="Listening to", value=2),
        app_commands.Choice(name="Watching", value=3),
        app_commands.Choice(name="Custom", value=4),
        app_commands.Choice(name="Competing in", value=5),
    ])
    async def activity(self, interaction: discord.Interaction, type: int, name: str):
        t = ""
        if type == 0:
            t = "Playing "
        elif type == 1:
            t = "Streaming "
        elif type == 2:
            t = "Listening to "
        elif type == 3:
            t = "Watching "
        elif type == 5:
            t = "Competing in "

        c = interaction.client.get_guild(1162403787097509889).get_channel(1162457439627661312)
        e = discord.Embed(title="Suggestion", timestamp=datetime.datetime.now(), colour=discord.Colour.blurple())
        e.description = t + name
        e.add_field(name="Suggested by", value=interaction.user.mention)
        await c.send(embed=e)
        return await interaction.response.send_message(content="Suggested!", embed=e, ephemeral=True)



class Suggestions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="suggest-profile")
    async def suggest_profile(self, ctx: commands.Context, *text: str):
        if ctx.message.attachments is not None:
            if ctx.message.attachments[0].content_type.startswith('image'):
                c = ctx.bot.get_guild(1162403787097509889).get_channel(1162443267082813530)
                e = discord.Embed(title="Suggestion", description=t, timestamp=datetime.datetime.now(), colour=discord.Colour.blurple())
                e.add_field(name="Suggested by", value=ctx.author.mention)
                e.set_image(url=ctx.message.attachments[0].proxy_url)
                await c.send(embed=e)
                return await ctx.reply(content="Suggested!", embed=e)
            else:
                return
        else:
            t = " ".join(text)
            if t is None:
                return await ctx.reply(content="I need some text!")
            else:
                c = ctx.bot.get_guild(1162403787097509889).get_channel(1162443267082813530)
                e = discord.Embed(title="Suggestion", description=t, timestamp=datetime.datetime.now(), colour=discord.Colour.blurple())
                e.add_field(name="Suggested by", value=ctx.author.mention)
                await c.send(embed=e)
                return await ctx.reply(content="Suggested!", embed=e)
        
    @commands.command(name="suggest-activity")
    async def suggest_activity(self, ctx: commands.Context, type: int, *name: str):
        n = " ".join(name)
        t = ""
        if type == 0:
            t = "Playing "
        elif type == 1:
            t = "Streaming "
        elif type == 2:
            t = "Listening to "
        elif type == 3:
            t = "Watching "
        elif type == 5:
            t = "Competing in "
        
        c = ctx.bot.get_guild(1162403787097509889).get_channel(1162457439627661312)
        e = discord.Embed(title="Suggestion", timestamp=datetime.datetime.now(), colour=discord.Colour.blurple())
        e.description = t + name
        e.add_field(name="Suggested by", value=ctx.author.mention)
        await c.send(embed=e)
        return await ctx.reply(content="Suggested!", embed=e)

async def setup(bot):
    bot.tree.add_command(SuggestionsA(name="suggest", description="Suggestions"))
    await bot.add_cog(Suggestions(bot))
    print("commands.suggestions ready :)")