import discord
from discord.ext import commands
from logging_files.information_logging import logger


class Information(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.color = (34, 255, 145)

    @commands.group(invoke_without_command=True, aliases=["commands"])
    async def poly_commands(self, ctx):
        # ➜ ‣ —
        embed = discord.Embed(
            color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
            title="➜ Bot Command Categories"
        )
        embed.set_thumbnail(url=ctx.guild.icon_url_as(size=4096, format=None, static_format="png"))
        embed.add_field(name="‣ Moderation commands:", inline=False, value="`p!commands moderation`")
        embed.add_field(name="‣ Utility commmands:", inline=False, value="`p!commands utility`")
        embed.add_field(name="‣ Information commands: (Coming Soon)", inline=False, value="`p!commands information`")
        embed.add_field(name="‣ Fun commands: (Coming Soon)", inline=False, value="`p!commands fun`")
        embed.add_field(name="‣ Settings: (Coming Soon)", inline=False, value="`p!commands settings`")
        embed.add_field(name="‣ Music commands: (Coming Soon)", inline=False, value="`p!commands music`")
        embed.set_footer(icon_url=ctx.author.avatar_url_as(size=4096, format=None, static_format="png"),
                         text="— Created by Poly Developer Team")

        await ctx.send(embed=embed)

        logger.info(f"Information | Sent Commands: {ctx.author}")

    @poly_commands.command()
    async def moderation(self, ctx):
        moderation = "`p!purge`, `p!warn`, `p!kick`, `p!ban`, `p!forceban`, `p!unban`," \
                     " `p!nickname`, `p!resetnick`"

        embed = discord.Embed(
            color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
            title="➜ Listing all commands",
            description=f"‣ All **Moderation** Commands \n—\n{moderation}"
        )

        await ctx.send(embed=embed)

        logger.info(f"Information | Sent Moderation Commands: {ctx.author}")

    @poly_commands.command()
    async def utility(self, ctx):
        utility = "`p!suggest"

        embed = discord.Embed(
            color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
            title="➜ Listing all commands",
            description=f"‣ All **Utility** Commands \n—\n{utility}"
        )

        await ctx.send(embed=embed)

        logger.info(f"Information | Sent Utility Commands: {ctx.author}")


def setup(client):
    client.add_cog(Information(client))
