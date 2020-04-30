import discord
from discord.ext import commands

# Get the token (You can replace the input by the actual token to not need to input it all the time
token = input('What is your Discord token?> ')

bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    with open('script.txt', 'r') as f:
        for line in f.readlines():
            for word in line.split():
                print(word)
                await ctx.send(word)

# Run the bot
bot.run(token)
