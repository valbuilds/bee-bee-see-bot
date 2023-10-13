import discord
from discord.ext import commands
from discord import app_commands
from typing import Optional

class IncompetencyA(app_commands.Group):
    @app_commands.command(description="Report a blooper.")
    async def blooper(self, interaction: discord.Interaction, description: str, attachment: Optional[discord.Attachment]):
        c = interaction.client.get_guild(1016626731785928715).get_channel(1016692053280817172)
        e = discord.Embed(title="Blooper reported!", description=f"Reported by: {interaction.user.mention}", colour=discord.Colour.brand_red())
        e.add_field(name="Description of blooper", value=description)
        if attachment is not None:
            if attachment.content_type.startswith('image') or attachment.content_type.startswith('video'):
                e.set_image(url=attachment.proxy_url)
        cm = await c.send(embed=e)
        await cm.create_thread(name=f"Thread for {interaction.user.display_name}", reason="Blooper reported")
        await interaction.response.send_message(content=cm.jump_url, ephemeral=True)

class Incompetency(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def blooper(self, ctx: commands.Context, *description: str):
        d = " ".join(description)
        c = ctx.bot.get_guild(1016626731785928715).get_channel(1016692053280817172)
        e = discord.Embed(title="Blooper reported!", description=f"Reported by: {ctx.author.mention}", colour=discord.Colour.brand_red())
        e.add_field(name="Description of blooper", value=d)
        if ctx.message.attachments is not None:
            if ctx.message.attachments[0].content_type.startswith('image') or ctx.message.attachments[0].content_type.startswith('video'):
                e.set_image(url=ctx.message.attachments[0].proxy_url)
        cm = await c.send(embed=e)
        await cm.create_thread(name=f"Thread for {ctx.author.display_name}", reason="Blooper reported")
        await ctx.reply(content=cm.jump_url)

async def setup(bot):
    await bot.add_cog(Incompetency(bot))
    bot.tree.add_command(IncompetencyA(name="incompetency", description="Incompetency commands"))
    print("commands.incompetency ready :)")