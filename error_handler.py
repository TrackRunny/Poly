import traceback
import sys

from discord.ext import commands
import discord


class CommandErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """The event triggered when an error is raised while invoking a command.
        ctx   : Context
        error : Exception"""

        if hasattr(ctx.command, 'on_error'):
            return

        ignored = (commands.CommandNotFound, commands.UserInputError)
        error = getattr(error, 'original', error)

        if isinstance(error, ignored):
            return

        print(ctx.args)

        if ctx.guild.me.top_role < ctx.get_member.top_role:
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="➜ Permission information",
                description="‣ The specified user has higher permissions than me."
            )
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))
