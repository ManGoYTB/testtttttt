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


class subscommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))
        # self.message = '**{}** Subscribers|Subscribe  -> :link: __**https://www.youtube.com/channel/UCnFHsZfaCwgBzbmt89Nmj3A**__ '

    def subs_emb(self, subs):
        emb = discord.Embed(title="**{}** Subscribers|Subscribe 👇".format(subs),
                            description="🔗 **[ClickHere](https://www.youtube.com/channel/UCnFHsZfaCwgBzbmt89Nmj3A)**<:kk:332133470572642317><:mg:332139374244265984> ",
                            color=0x4634e7)
        emb.set_author(name="MaGeClan", url="https://www.youtube.com/channel/UCnFHsZfaCwgBzbmt89Nmj3A", icon_url="https://yt3.ggpht.com/-palNhXtV33c/AAAAAAAAAAI/AAAAAAAAAAA/DgJik9EDvqA/s100-c-k-no-mo-rj-c0xffffff/photo.jpg")
        emb.set_thumbnail(url='https://yt3.ggpht.com/-palNhXtV33c/AAAAAAAAAAI/AAAAAAAAAAA/DgJik9EDvqA/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
        emb.set_footer(text="MaGeClan", icon_url="https://cdn.discordapp.com/emojis/329991214327660544.png")
        return emb

    @commands.command(pass_context=True)
    async def subsmage(self, ctx):
        parameters = {"id": "UCnFHsZfaCwgBzbmt89Nmj3A", "key": "AIzaSyCssyjjfIcJpvl4CYoD20LbKcWIxQPNvw8", "part": "statistics",
                      "fields": "items/statistics/subscriberCount"}
        async with aiohttp.ClientSession() as session:
            async with session.get("https://www.googleapis.com/youtube/v3/channels", params=parameters) as r:
                if r.status == 200:
                    json_data = await r.json()
                    sub_count = json_data['items'][0]['statistics']['subscriberCount']
                    await self.bot.send_message(ctx.message.channel, embed=self.subs_emb(sub_count))


def setup(bot):
    bot.add_cog(subscommand(bot))
