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
