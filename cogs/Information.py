"""
Poly - Discord bot
Copyright (C) 2019 TrackRunny

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

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
        embed.add_field(name="‣ Information commands:", inline=False, value="`p!commands information`")
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
        utility = "`p!suggest`"

        embed = discord.Embed(
            color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
            title="➜ Listing all commands",
            description=f"‣ All **Utility** Commands \n—\n{utility}"
        )

        await ctx.send(embed=embed)

        logger.info(f"Information | Sent Utility Commands: {ctx.author}")

    @poly_commands.command()
    async def information(self, ctx):
        information = "`p!whois`"

        embed = discord.Embed(
            color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
            title="➜ Listing all commands",
            description=f"‣ All **Information** Commands \n—\n{information}"
        )

        await ctx.send(embed=embed)

        logger.info(f"Information | Sent Information Commands: {ctx.author}")

    @commands.command(aliases=["whois"])
    async def userinfo(self, ctx, member: discord.Member):
        status = {
            "online": "<:online:648014037010874419>",
            "idle": "<:idle:648014173543989261>",
            "offline": "<:offline:648014210525298688>",
            "dnd": "<:dnd:648014190417674250>"
        }

        embed = discord.Embed(
            color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
            title=f"➜ Userinfo for: {member}",
            description=f"• Information will be displayed about the user below."
        )
        roles = [role for role in member.roles]
        roles = f" ".join([f"@{role}, " for role in roles])

        embed.set_thumbnail(url=member.avatar_url_as(size=4096, format=None, static_format="png"))
        embed.add_field(name="‣ Account Name", value=str(member))
        embed.add_field(name="‣ Discord ID", value=str(member.id))
        embed.add_field(name="‣ Nickname", value=member.nick or "No nickname.")
        embed.add_field(name="‣ Account Created At", value=member.created_at.strftime("%A %d, %B %Y"))
        embed.add_field(name="‣ Account Joined At", value=member.joined_at.strftime("%A %d, %B %Y"))
        if member.activity is None:
            embed.add_field(name="‣ Current Activity", value="No current activity.")
        else:
            embed.add_field(name="‣ Current Activity", value=member.activity.name)
        if member.bot is True:
            embed.add_field(name="‣ Discord Bot? ", value=":robot:")
        else:
            embed.add_field(name="‣ Discord Bot?", value=":no_entry_sign:")
        if member.is_on_mobile() is True:
            embed.add_field(name="‣ On Mobile Device? ", value=":iphone:")
        else:
            embed.add_field(name="‣ On Mobile Device?", value=":no_mobile_phones:")
        embed.add_field(name="‣ Current Status", value=status[member.status.name])
        embed.add_field(name="‣ Highest Role", inline=False, value=f"```@{member.top_role}```")
        # embed.add_field(name="‣ All Roles", inline=False, value=f"```{roles}```")

        await ctx.send(embed=embed)

        logger.info(f"Information | Sent Whois: {ctx.author} | To: {member}")

    @userinfo.error
    async def userinfo_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
                title="➜ Passed Invalid Member",
                description="‣ Please mention a valid member. Example: `p!whois @user`"
            )
            await ctx.send(embed=embed)
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
                title="➜ Passed Invalid Argument",
                description="‣ Please put a valid parameter. Example: `p!whois @user`"
            )
            await ctx.send(embed=embed)



def setup(client):
    client.add_cog(Information(client))
