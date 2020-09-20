import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='Сова ')
# TOKEN = 'Your token'
TOKEN = "NzU3MzMwMTU2MTYyNTE0OTY1.X2e0qw.EFJQio3U2H2qRGlDqt43BPF1EJw"  # Чтобы не переделывать токен

@bot.event
async def on_ready():
    print("{0.user} пришел на сервера".format(bot))


@bot.event
async def on_member_join(member):
    server = member.guild
    role = discord.utils.get(server.roles, name="Участник")
    await member.add_roles(role)


@bot.command(pass_context=True)
async def привет(ctx):
    text = "Привет, {}!".format(str(ctx.message.author.name))
    await ctx.send(text)


def main():
    #bot.loop.create_task(daily_loop())
    bot.run(TOKEN)


if __name__ == "__main__":
    main()