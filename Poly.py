#!/usr/bin/env python3

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
