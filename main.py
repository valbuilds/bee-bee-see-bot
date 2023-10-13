import discord
from discord.ext import commands
import settings
import datetime

def run():
    a = discord.Activity(type=discord.ActivityType.watching, name="the BBC News Channel")
    bot = commands.Bot(command_prefix='b.', activity=a, intents=discord.Intents.all())

    @bot.event
    async def on_ready():
        await bot.load_extension("commands.suggestions")
        await bot.load_extension("commands.incompetency")
        print("bee bee see bot ready :)")
    
    @bot.event
    async def on_message(message: discord.Message):
        if message.author.bot == False and bot.user.mentioned_in(message):
            await message.channel.send("<a:pepeWut:1110185838463160420>")
        else:
            await bot.process_commands(message)
    
    @bot.command()
    async def aaron(ctx: commands.Context):
        await ctx.reply(content="[.](https://cdn.discordapp.com/attachments/1097533655682912416/1162441481148170252/aaron.png?ex=653bf2fe&is=65297dfe&hm=8f17e3c5a6243c508caa8bf0907f359fd84b09fd2ee1f6782e749960929cce69&)")

    @bot.command()
    async def baguette(ctx: commands.Context):
        await ctx.reply(content="[.](https://cdn.discordapp.com/attachments/1016691910158590032/1162430490981171270/baguette.mov?ex=653be8c1&is=652973c1&hm=db630770104c537f21ff2e3609ba2515c8ebfa9717615855beea973becc71be5&)")

    @bot.command()
    async def botbotsource(ctx: commands.Context):
        return await ctx.reply(content="egg wont share <:broWhat:1100474984738070639>")
    
    @bot.command()
    async def mint(ctx: commands.Context):
        return await ctx.reply(content="<:greenfrog:1115049036735594506>")
    
    @bot.command()
    async def sophie(ctx: commands.Context):
        return await ctx.reply(content="[.](https://cdn.discordapp.com/attachments/1162403788175454251/1162460726951170078/p0fh3vw0.jpg?ex=653c04ea&is=65298fea&hm=62866c61f2fb5ae388314dff55badc28a43bb1aebf834858cfcb0136f1c2e093&)")

    @bot.tree.command(description="Test modal")
    async def test_modal(interaction: discord.Interaction):
        class TestModal(discord.ui.Modal, title="test modal"):
            t1 = discord.ui.TextInput(label='test1', style=discord.TextStyle.short)
            t2 = discord.ui.TextInput(label='test2', style=discord.TextStyle.paragraph)
            e = discord.Embed(title="test modal filled out", timestamp=datetime.datetime.now(), colour=discord.Colour.brand_green())

            async def on_submit(self, interaction: discord.Interaction):
                self.e.add_field(name="Test 1", value=self.t1)
                self.e.add_field(name="Test 2", value=self.t2)
                self.e.description = "Submitted by: " + interaction.user.mention
                await interaction.response.send_message(embed=self.e)

        await interaction.response.send_modal(TestModal())

    @bot.command()
    async def sync(ctx: commands.Context):
        await bot.tree.sync()
        await ctx.reply("Synced.")

    bot.run(settings.TOKEN)

if __name__ == "__main__":
    run()