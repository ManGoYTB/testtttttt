import asyncio
import aiohttp
import discord
import math
import random
import time
from datetime import datetime
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

class Comm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot	

    @commands.command(pass_context=True)
    async def discord(self,ctx):
        """DiscordForum"""
        embed = discord.Embed(
            title="**HelpMe**",
            color=0x7691eb,
            description="**getting started**")
        embed.set_thumbnail(url="http://www.ethicon.com/sites/all/themes/ethicon/img/ajax-loader.gif")    
        embed.set_author(name="DiscordHelp", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")
        embed.add_field(name="🇫🇷👈👇", value="🔥**https://support.discordapp.com/hc/fr**🔥", inline=False)
        embed.add_field(name="🇺🇸👈👇", value="🔥**https://support.discordapp.com/hc/en-us**🔥", inline=False)
        embed.add_field(name="🇩🇪👈👇", value="🔥**https://support.discordapp.com/hc/de**🔥", inline=False)
        embed.add_field(name="🇪🇸👈👇", value="🔥**https://support.discordapp.com/hc/es**🔥", inline=False)
        embed.add_field(name="🇮🇹👈👇", value="🔥**https://support.discordapp.com/hc/it**🔥", inline=False)
        await self.bot.send_message(discord.Object(ctx.message.channel.id), embed=embed)


def setup(bot):
    bot.add_cog(Comm(bot))
