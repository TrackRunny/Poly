import discord
from discord.ext import commands


class Owner(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def roles(self, ctx):
        embed = discord.Embed(
            color=discord.Color.from_rgb(54, 57, 63),
            title="➜ Color Roles",
            description="‣ Choose your favorite chat color!"
        )
        embed.add_field(name="‣ Red", value=":rose:")
        embed.add_field(name="‣ Orange", value=":tangerine:")
        embed.add_field(name="‣ Yellow", value=":banana:")
        embed.add_field(name="‣ Green", value=":green_apple:")
        embed.add_field(name="‣ Blue", value=":cyclone:")
        embed.add_field(name="‣ Purple", value=":space_invader:")
        embed.add_field(name="‣ Black", value=":new_moon_with_face:")
        embed.add_field(name="‣ White", value=":white_circle:")
        embed.add_field(name="‣ Pink", value=":heartpulse:")

        await ctx.send(embed=embed)

        embed2 = discord.Embed(
            color=discord.Color.from_rgb(54, 57, 63),
            title="➜ Platform Roles",
            description="‣ Choose the platforms you use!"
        )
        embed2.add_field(name="‣ Computer", value=":computer:")
        embed2.add_field(name="‣ Mobile", value=":iphone:")
        embed2.add_field(name="‣ Console", value=":video_game:")

        await ctx.send(embed=embed2)

        '''
        embed3 = discord.Embed(
            color=discord.Color.from_rgb(54, 57, 63),
            title="➜ Other Roles",
            description="‣ Roles that do not follow into the other categories!"
        )
        embed3.add_field(name="‣ Penguin Iceberg", value=":penguin: ― This role gives access to **#penguin-iceberg**, where programming and technical talk goes.")

        await ctx.send(embed=embed3)
        '''

    @commands.command()
    @commands.is_owner()
    async def poly(self, ctx):
        embed = discord.Embed(
            color=discord.Color.from_rgb(34, 255, 145),
            title="➜ Poly Studios",
        )

        await ctx.send(embed=embed)

        embed2 = discord.Embed(
            color=discord.Color.from_rgb(54, 57, 63),
            description="‣ Ahoy there, adventurer! "
                        "I see you have traveled across the far lands to join us here at **Poly Studios.** "
                        "Keep reading to get acquainted before wandering across these sacred lands. "
                        "But most importantly, be sure to have a great time here!"
        )

        await ctx.send(embed=embed2)

        embed3 = discord.Embed(
            color=discord.Color.from_rgb(54, 57, 63),
            title="➜ The Rulebook",
            description="•The official server regulations for Poly Studios, please notice and understand the following: "
                        "\n\n‣ Staff have the authority to punish you if they feel your actions were not deemed appropriate for our server. "
                        "\n‣ You may not argue with a staff member. Please inquire with an executive respectfully so we can handle the situation properly."
                        "\n‣ Game rules can be found at (soon). You must follow Discord's terms of service, which can be found [**here**](https://discordapp.com/terms).\n"
        )

        embed3.add_field(name="\n\nI.", inline=False, value="Use all channels appropriately; each channel has been assigned a purpose.")
        embed3.add_field(name="II.", inline=False, value="Please avoid spamming or use of all-caps.")
        embed3.add_field(name="III.", inline=False,  value="Use of racial, sexual, or any offensive slurs are not tolerated.")
        embed3.add_field(name="IV.", inline=False, value="Be respectful toward everyone, in spite of who they are.")
        embed3.add_field(name="V.", inline=False, value="Threats or harassment directed to anyone here is absolutely prohibited."),
        embed3.add_field(name="VI.", inline=False, value="Utilization of profanity is restricted.")
        embed3.add_field(name="VII.", inline=False,  value="Refrain from sending malicious content or any types of advertisements, especially via DM.")

        await ctx.send(embed=embed3)

        embed4 = discord.Embed(
            color=discord.Color.from_rgb(54, 57, 63),
            title="➜ Significant",
            description="• Listed below are several significant redirections!"
        )

        embed4.add_field(name="‣ Main Chat", value="<#506866539782471690>")
        embed4.add_field(name="‣ Newsletters", value="<#645483412437729280>")
        embed4.add_field(name="‣ Our Events", value="<#645483412437729280>")
        embed4.add_field(name="‣ Free Roles", value="<#645815363719790633>")

        await ctx.send(embed=embed4)

        embed5 = discord.Embed(
            color=discord.Color.from_rgb(54, 57, 63),
            title="➜ Our Poly Studios Team",
            description="» Executives"
                        "\n\n― Denic"
                        "\n― AlexPads"
                        "\n― JustTal"
                        "\n― TrackRunny"
                        "\n― Alandis"
                        "\n― salty"
                        "\n― TheHunted "
        )

        await ctx.send(embed=embed5)

        embed6 = discord.Embed(
            color=discord.Color.from_rgb(54, 57, 63),
            title="➜ Our Projects",
            description="• Below are a couple of our projects that our development & technical team have created! "
                        "\n\n‣ Hosting Service"
                        "\nOur hosting service provides affordable hosting with powerful performance ― [**Witherhosting**](https://witherhosting.com)"
        )

        await ctx.send(embed=embed6)


def setup(client):
    client.add_cog(Owner(client))