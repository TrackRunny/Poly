import discord

color = (34, 255, 145)

higher_permissions = discord.Embed(
    color=discord.Color.from_rgb(color[0], color[1], color[2]),
    title="➜ Permission Information",
    description="‣ The specified user has higher permissions than me."
)

bot_missing_permissions = discord.Embed(
    color=discord.Color.from_rgb(color[0], color[1], color[2]),
    title="➜ Bot Missing Permissions!",
    description="‣ Please give me permissions to use this command!"
)

user_missing_permissions = discord.Embed(
    color=discord.Color.from_rgb(color[0], color[1], color[2]),
    title="➜ Missing Permissions",
    description="‣ You do not have permissions to run this command!"
)

user_higher_permissions = discord.Embed(
    color=discord.Color.from_rgb(color[0], color[1], color[2]),
    title="➜ Permission Information",
    description="‣ The specified user has higher permissions than you or equal permissions."
)
