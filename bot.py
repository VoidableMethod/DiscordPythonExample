import discord # Main Discord Package.
from os import system # Used for executing console commands.
from platform import system as syst # Used for detecting the OS.

from discord.ext import commands # Do not rename or remove!

''' ! Bot Configuration ! '''
bot_prefix = '>' # The prefix for your bot.
bot_token = 'Token Goes Here' # The token of your bot.

bot = commands.Bot(command_prefix=bot_prefix, intents=discord.Intents.all())

@bot.event
async def on_ready():
    if 'Windows' in syst():
        system('cls')
    elif 'Linux' in syst():
        system('clear')

    print(f'> Logged in as {bot.user}!')
    print(f'> Current ping: {round(bot.latency * 1000)} MS.')

@bot.command()
async def ping(ctx):
    await ctx.reply(f'Responded within {round(bot.latency * 1000)} MS.')

@bot.command()
async def say(ctx, *arg):
    words = ' '.join(arg) 
    await ctx.reply(words)

bot.run(bot_token)
