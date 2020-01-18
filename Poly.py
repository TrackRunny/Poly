#!/usr/bin/env python3

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Poly - Discord bot                                                        #
# Copyright (C) 2019 TrackRunny                                             #
#                                                                           #
# This program is free software: you can redistribute it and/or modify      #
# it under the terms of the GNU General Public License as published by      #
# the Free Software Foundation, either version 3 of the License, or         #
# (at your option) any later version.                                       #
#                                                                           #
# This program is distributed in the hope that it will be useful,           #
# but WITHOUT ANY WARRANTY; without even the implied warranty of            #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
# GNU General Public License for more details.                              #
#                                                                           #
# You should have received a copy of the GNU General Public License         #
# along with this program. If not, see <https://www.gnu.org/licenses/>.     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import discord
from discord.ext import commands

client = commands.Bot("p!", owner_id=546812331213062144, case_insensitive=False)
client.remove_command('help')
valid = "TrackRunny#3900"
line_divide = "\n———————————————————————————————"


poly_token = "TOKEN HERE"


@client.event
async def on_ready():
    # change_status.start()
    await client.change_presence(activity=discord.Activity(type=0, name="↩ Polymortal ↪"))
    client.load_extension('jishaku')
    extensions = ["Moderation", "Information", "Utility", "Owner"]

    for extension in extensions:
        client.load_extension("cogs." + extension)

    print(f"---------------Polymortal-----------------------"
          f"\nBot is online and connected to {str(client.user)}"
          f"\nCreated by TrackRunny#3900 on Discord"
          f"\nConnected to {str(len(client.guilds))} Guilds."
          f"\n----------------------------------------------")


@commands.is_owner()
@client.command()
async def say(ctx, *, message):
    await ctx.send(message)


client.run(poly_token)
