import discord
from discord.ext import commands
from logging_files.moderation_logging import logger
from utils.moderation_errors import higher_permissions, bot_missing_permissions, user_missing_permissions, user_higher_permissions


class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.color = (34, 255, 145)
        self.mod_logging = self.client.get_channel(645801032193933312)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def warn(self, ctx, member: discord.Member, *, reason="No valid reason provided."):
        if ctx.guild.me.top_role < member.top_role:
            await ctx.send(embed=higher_permissions)
        elif ctx.guild.me.top_role > member.top_role:
            embed = discord.Embed(
                color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
                title="➜ Warning sent",
                description=f"‣ Successfully warned: {member.mention}"
                            f"\n‣ Reason: `{reason}`"
            )

            await ctx.send(embed=embed)

            embed2 = discord.Embed(
                color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
                title=f"➜ Warning Sent To: {member}"
            )
            embed2.add_field(name=f"‣ Moderator:", value=f"`{ctx.author}`")
            embed2.add_field(name="‣  Reason:", value=f"`{reason}`")
            embed2.set_footer(icon_url=ctx.guild.icon_url_as(size=4096, format=None, static_format="png"),
                              text=f"— Warning sent from: {ctx.guild}")

            logger.info(f"Moderation | Sent Warn: {ctx.author} | Warned: {member} | Reason: {reason}")

            await member.send(embed=embed2)

            embed3 = discord.Embed(
                color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
                title=f"➜ Moderation Logs",
                description=f"‣ **Warned:** {member}"
            )
            embed3.add_field(name="➜ Moderator:", value=ctx.author)
            embed3.add_field(name="➜ Reason:", value=reason)

            await self.mod_logging.send(embed=embed3)

    @warn.error
    async def warn_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
                title="➜ Passed Invalid Member",
                description="‣ Please mention a valid member. Example: `p!warn @user [reason]`"
            )
            await ctx.send(embed=embed)
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
                title="➜ Passed Invalid Argument",
                description="‣ Please put a valid parameter. Example: `p!warn @user [reason]`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=user_missing_permissions)
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(embed=bot_missing_permissions)

    @commands.command(pass_context=True)
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="No valid reason provided."):
        if ctx.guild.me.top_role < member.top_role:
            await ctx.send(embed=higher_permissions)
        elif ctx.author.top_role <= member.top_role:
            await ctx.send(embed=user_higher_permissions)
        elif ctx.guild.me.top_role > member.top_role:
            embed = discord.Embed(
                color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
                title="➜ User Successfully Kicked",
                description=f"‣ Successfully kicked: {member.mention}"
                            f"\n‣ Reason: `{reason}`"
            )
            await member.kick(reason=reason)

            await ctx.send(embed=embed)

            embed2 = discord.Embed(
                color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
                title=f"Kick Sent To: {member}"
            )
            embed2.add_field(name=f"‣ Moderator:", value=f"`{ctx.author}`")
            embed2.add_field(name="‣  Reason:", value=f"`{reason}`")
            embed2.set_footer(icon_url=ctx.guild.icon_url_as(size=4096, format=None, static_format="png"),
                              text=f"— Kicked from: {ctx.guild}")

            logger.info(f"Moderation | Sent Kick: {ctx.author} | Kicked: {member} | Reason: {reason}")

            embed3 = discord.Embed(
                color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
                title=f"➜ Moderation Logs",
                description=f"‣ **Kicked:** {member}"
            )
            embed3.add_field(name="➜ Moderator:", value=ctx.author)
            embed3.add_field(name="➜ Reason:", value=reason)

            await self.mod_logging.send(embed=embed3)

            await member.send(embed=embed2)

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
                title="➜ Passed Invalid Member",
                description="‣ Please mention a valid member. Example: `p!kick @user [reason]`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
                title="➜ Passed Invalid Argument",
                description="‣ Please put a valid parameter. Example: `p!kick @user [reason]`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=user_missing_permissions)
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(embed=bot_missing_permissions)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason="No valid reason provided."):
        if ctx.guild.me.top_role < member.top_role:
            await ctx.send(embed=higher_permissions)
        elif ctx.author.top_role <= member.top_role:
            await ctx.send(embed=user_higher_permissions)
        elif ctx.guild.me.top_role > member.top_role:
            embed = discord.Embed(
                color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
                title="➜ User Successfully Banned",
                description=f"‣ Successfully banned: {member.mention}"
                            f"\n‣ Reason: `{reason}`"
            )

            await member.ban(reason=reason)

            await ctx.send(embed=embed)

            embed2 = discord.Embed(
                color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
                title=f"Kick Ban To: {member}"
            )
            embed2.add_field(name=f"‣ Moderator:", value=f"`{ctx.author}`")
            embed2.add_field(name="‣  Reason:", value=f"`{reason}`")
            embed2.set_footer(icon_url=ctx.guild.icon_url_as(size=4096, format=None, static_format="png"),
                              text=f"— Banned from: {ctx.guild}")

            logger.info(f"Moderation | Sent Ban: {ctx.author} | Banned: {member} | Reason: {reason}")

            embed3 = discord.Embed(
                color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
                title=f"➜ Moderation Logs",
                description=f"‣ **Banned:** {member}"
            )
            embed3.add_field(name="➜ Moderator:", value=ctx.author)
            embed3.add_field(name="➜ Reason:", value=reason)

            await self.mod_logging.send(embed=embed3)

            await member.send(embed=embed2)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
                title="➜ Passed Invalid Member",
                description="‣ Please mention a valid member. Example: `p!ban @user [reason]`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
                title="➜ Passed Invalid Argument",
                description="‣ Please put a valid parameter. Example: `p!ban @user [reason]`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=user_missing_permissions)
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(embed=bot_missing_permissions)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def forceban(self, ctx, *, id: int):
        await ctx.guild.ban(discord.Object(id))
        embed = discord.Embed(
            color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
            title="➜ User Successfully Forcebanned",
            description=f"‣ Successfully unbanned: <@{id}>"
        )

        await ctx.send(embed=embed)

        embed3 = discord.Embed(
            color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
            title=f"➜ Moderation Logs",
            description=f"‣ **Force Banned:** {id}"
        )
        embed3.add_field(name="➜ Moderator:", value=ctx.author)
        embed3.add_field(name="➜ Reason:", value="N/A")

        await self.mod_logging.send(embed=embed3)

        logger.info(f"Moderation | Sent Force Ban: {ctx.author} | Force Banned: {id}")

    @forceban.error
    async def forceban_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
                title="➜ Passed Invalid ID",
                description="‣ Please put a valid ID. Example: `p!forceban <ID>`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
                title="➜ Passed Invalid Argument",
                description="‣ Please put a valid parameter. Example: `p!forceban <ID>`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=user_missing_permissions)
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(embed=bot_missing_permissions)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def unban(self, ctx, *, id: int):
        await ctx.guild.unban(discord.Object(id))
        embed = discord.Embed(
            color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
            title="➜ User Successfully Unbanned",
            description=f"‣ Successfully unbanned: <@{id}>"
        )
        await ctx.send(embed=embed)

        embed3 = discord.Embed(
            color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
            title=f"➜ Moderation Logs",
            description=f"‣ **Unbanned:** <@{id}>"
        )
        embed3.add_field(name="➜ Moderator:", value=ctx.author)
        embed3.add_field(name="➜ Reason:", value="N/A")

        await self.mod_logging.send(embed=embed3)

        logger.info(f"Moderation | Sent Unban: {ctx.author} | Unbanned: {id}")

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
                title="➜ Passed Invalid ID",
                description="‣ Please put a valid ID. Example: `p!unban <ID>`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
                title="➜ Passed Invalid Argument",
                description="‣ Please put a valid parameter. Example: `p!unban <ID>`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=user_missing_permissions)
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(embed=bot_missing_permissions)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount)

        embed3 = discord.Embed(
            color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
            title=f"➜ Moderation Logs",
            description=f"‣ **Purged:** {amount} messages"
        )
        embed3.add_field(name="➜ Moderator:", value=ctx.author)
        embed3.add_field(name="➜ Reason:", value="N/A")

        await self.mod_logging.send(embed=embed3)

        logger.info(f"Moderation | Sent Purge: {ctx.author} | Purged: {amount} messages")

    @purge.error
    async def purge_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
                title="➜ Invalid Amount Of Messages",
                description="• Please use a valid number! Example: `l!purge <number>`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
                title="➜ Passed Invalid Argument",
                description="‣ Please put a valid parameter. Example: `p!purge <number>`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=user_missing_permissions)
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(embed=bot_missing_permissions)

    @commands.command()
    @commands.has_permissions(manage_nicknames=True)
    @commands.bot_has_permissions(manage_nicknames=True)
    async def nickname(self, ctx, member: discord.Member, *, nickname):
        if ctx.guild.me.top_role < member.top_role:
            await ctx.send(embed=higher_permissions)
        elif ctx.author.top_role <= member.top_role:
            await ctx.send(embed=user_higher_permissions)
        elif ctx.guild.me.top_role > member.top_role:
            embed = discord.Embed(
                color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
                title="➜ Nickname Successfully Changed",
                description=f"‣ Successfully Changed: {member.mention}"
                            f"\n‣ New Nickname: `{nickname}`"
            )

            await member.edit(nick=nickname)
            await ctx.send(embed=embed)

            embed3 = discord.Embed(
                color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
                title=f"➜ Moderation Logs",
                description=f"‣ **Changed Nickname:** {member}"
            )
            embed3.add_field(name="➜ Moderator:", value=ctx.author)
            embed3.add_field(name="➜ Reason:", value="N/A")

            await self.mod_logging.send(embed=embed3)

            logger.info(f"Moderation | Sent Change Nickname: {ctx.author} | Nickname: {nickname} | To: {member}")

    @nickname.error
    async def nickname_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
                title="➜ Passed Invalid Member",
                description="‣ Please mention a valid member. Example: `p!nickname @user`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
                title="➜ Passed Invalid Argument",
                description="‣ Please put a valid parameter. Example: `p!nickname @user`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=user_missing_permissions)
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(embed=bot_missing_permissions)

    @commands.command()
    @commands.has_permissions(manage_nicknames=True)
    @commands.bot_has_permissions(manage_nicknames=True)
    async def resetnick(self, ctx, member: discord.Member):
        if ctx.guild.me.top_role < member.top_role:
            await ctx.send(embed=higher_permissions)
        elif ctx.author.top_role <= member.top_role:
            await ctx.send(embed=user_higher_permissions)
        elif ctx.guild.me.top_role > member.top_role:
            embed = discord.Embed(
                color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
                title="➜ Nickname Successfully Reset",
                description=f"‣ Successfully Changed: {member.mention}"
            )

            await member.edit(nick=None)
            await ctx.send(embed=embed)

            embed3 = discord.Embed(
                color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
                title=f"➜ Moderation Logs",
                description=f"‣ **Reset Nickname:** {member}"
            )
            embed3.add_field(name="➜ Moderator:", value=ctx.author)
            embed3.add_field(name="➜ Reason:", value="N/A")

            await self.mod_logging.send(embed=embed3)

            logger.info(f"Moderation | Sent Reset Nickname: {ctx.author} | To: {member}")

    @resetnick.error
    async def nickname_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
                title="➜ Passed Invalid Member",
                description="‣ Please mention a valid member. Example: `p!resetnick @user`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
                title="➜ Passed Invalid Argument",
                description="‣ Please put a valid parameter. Example: `p!resetnick @user`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
                title="→ Missing Permissions!",
                description="• You do not have permissions to run this command!"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=user_missing_permissions)
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(embed=bot_missing_permissions)


def setup(client):
    client.add_cog(Moderation(client))
