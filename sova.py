import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='Сова ')
# TOKEN = 'Your token'
TOKEN = "NzU3MzMwMTU2MTYyNTE0OTY1.X2e0qw.t87U9_" + "0iI1qzshNsiPdv3k3OZEA"  # Чтобы не переделывать токен

channel_memory_id = 757635310405288007

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

@bot.command(pass_context=True)
async def вопрос(ctx, question, *ans):
    channel_memory = bot.get_channel(channel_memory_id)
    text = question + "\n"
    i = 1
    for item in ans:
        text += str(i) + " - " + item + "\n"
        i += 1
    await channel_memory.send(text)

def main():
    #bot.loop.create_task(daily_loop())
    bot.run(TOKEN)


if __name__ == "__main__":
    main()