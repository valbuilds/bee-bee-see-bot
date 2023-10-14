import discord
from discord.ext import commands
from discord import app_commands
from typing import Optional
import time

class SharedMethods:
    @staticmethod
    async def timestamp_check(t: str):
        if t.startswith('t:'):
            if t.split(':')[1].isnumeric():
                return "<" + t + ":F>"
            if t.split(':')[1] == "now":
                return "<t:" + str(int(time.time())) + ":F>"
        else:
            return t

class IncompetencyA(app_commands.Group):
    @app_commands.command(description="Report a blooper.")
    @app_commands.describe(time="The time in BST that the blooper occured.")
    @app_commands.describe(description="Describe the blooper.")
    @app_commands.describe(attachment="Image/video of the blooper.")
    async def blooper(self, interaction: discord.Interaction, time: str, description: str, attachment: Optional[discord.Attachment]):
        c = interaction.client.get_guild(1162403787097509889).get_channel(1162443267082813530)
        e = discord.Embed(title="Blooper", description=f"Reported by: {interaction.user.mention}", colour=discord.Colour.brand_red())
        t = await SharedMethods.timestamp_check(t=time)
        e.add_field(name="Time", value=t)
        e.add_field(name="Description", value=description)
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
    async def blooper(self, ctx: commands.Context):
        class BlooperModal(discord.ui.Modal, title="Reporting a blooper"):
            time = discord.ui.TextInput(label="Time of Blooper (in BST)", style=discord.TextStyle.short)
            description = discord.ui.TextInput(label="Description of Blooper", style=discord.TextStyle.paragraph)
            e = discord.Embed(title="Blooper", colour=discord.Colour.brand_red())
            

            async def on_submit(self, interaction: discord.Interaction):
                t = await SharedMethods.timestamp_check(t=self.time)
                self.e.add_field(name="Time", value=t)
                self.e.add_field(name="Description", value=self.description)
                c = interaction.client.get_guild(1016626731785928715).get_channel(1016692053280817172)
                self.e.description = f"Reported by: {interaction.user.mention}"
                r = await c.send(embed=self.e)
                await r.create_thread(name=f"Thread for {interaction.user.display_name}", reason="Blooper reported")
                return await interaction.response.send_message(embed=self.e)

        class ShowBlooperModal(discord.ui.View):
            @discord.ui.button(label="Fill out form", style=discord.ButtonStyle.blurple, emoji='<:digit_al:1143272455268483184>')
            async def on_click(self: discord.ui.View, interaction: discord.Interaction, button: discord.ui.Button):
                await interaction.response.send_modal(BlooperModal())
            
            async def on_timeout():
                ShowBlooperModal.clear_items()

        await ctx.reply(content="**I need you to fill out this form!** *(skip this by using </incompetency blooper:1162491293256130610>!)*", view=ShowBlooperModal(timeout=180), mention_author=False)

async def setup(bot):
    await bot.add_cog(Incompetency(bot))
    bot.tree.add_command(IncompetencyA(name="incompetency", description="Incompetency commands"))
    print("commands.incompetency ready :)")