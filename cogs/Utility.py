import discord
from discord.ext import commands
from logging_files.utility_logging import logger

class Utility(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.color = (34, 255, 145)
        self.suggestion_box = self.client.get_channel(646170475726110720)

    @commands.command()
    @commands.cooldown(rate=1, per=3600, type=commands.BucketType.user)
    async def suggest(self, ctx, *, suggestion):
        embed = discord.Embed(
            color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
            title=f"➜ New Suggestion From: {ctx.author}",
            description=f"‣ Suggestion: `{suggestion}`"
        )
        embed.set_thumbnail(url=ctx.author.avatar_url_as(size=4096, format=None, static_format="png"))

        await ctx.send("( <:verified:639525974496772106> ) ‣ **Successfully** sent your suggestion! "
                       "Please view <#646170475726110720> to view it.")

        message = await self.suggestion_box.send(embed=embed)
        await message.add_reaction(self.client.get_emoji(646176222325243924))
        await message.add_reaction(self.client.get_emoji(646176188263301141))

        logger.info(f"Utility | Sent Suggestion: {ctx.author} | Suggestion: {suggestion}")

    @suggest.error
    async def suggest_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
                title="➜ Passed Invalid Argument",
                description="‣ Please put a valid parameter. Example: `p!suggest <suggestion>`"
            )
            await ctx.send(embed=embed)
            ctx.command.reset_cooldown(ctx)
        elif isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(
                color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
                title="➜ Cool Down Error",
                description="‣ You are only allowed to suggest an idea every hour."
            )
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Utility(client))