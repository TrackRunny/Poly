#!/usr/bin/env python3

import discord
from discord.ext import commands
from itertools import cycle

client = commands.Bot("p!", owner_id=546812331213062144, case_insensitive=False)
client.remove_command('help')
status = cycle([f'Linux videos | l!help', 'FOSS software | l!help', 'Windows getting worse',
                'Server members | l!help', 'Cryptocurrency | l!help', 'Linux getting popular'])
valid = "TrackRunny#3900"
line_divide = "\n———————————————————————————————"


token = "NjQ1NTA4OTAwMTI0MzYwNzE0.XdDnCA.SPHVU19HmfxRT-YJuUrMEDiyI80"
testing_token = "NjExMDI0NDMwNjUwNjIxOTcy.XYbJ2w.76U9r1wH7BHdSX0nVVVaGUi-u2U"


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


client.run(token)
