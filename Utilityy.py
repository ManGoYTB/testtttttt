import discord
from discord.ext import commands


class Utilityy(commands.Cog):
    """Provides basic Utilityy commands"""
    def __init__(self, bot):
        self.bot = bot
        self.db = bot.plugin_db.get_partition(self)

    @commands.command()
    async def say(self, ctx, *, message: commands.clean_content):
        """Repeats after you"""
        await ctx.send(message)


def setup(bot):
    bot.add_cog(Utilityy(bot))
