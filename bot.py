import discord                                   # Main Discord Package (where all the magic happens).
from discord.ext import commands                 # Do not rename or remove!
from discord.ext.commands import CommandNotFound # For command error handling.
from os import system, getlogin                  # Used for executing console commands and getting PC username.
from datetime import datetime                    # For getting the current local time of the user.
from platform import system as opsys             # Used for detecting the OS.

''' ! Bot Configuration ! '''
bot_prefix = '>'          # The prefix for your bot.
bot_token = 'Enter Token' # The token of your bot.
bot = commands.Bot(command_prefix=bot_prefix, intents=discord.Intents.all())

dt_now = datetime.now()
local_time = dt_now.strftime("%H:%M:%S")

@bot.event
async def on_ready():
    system("title Bot Template")

    if "Windows" in opsys():
        system("cls")
    elif "Linux" in opsys():
        system("clear")

    print(f"> Hello, {getlogin()}!")
    print(f"> Logged in as {bot.user} at {local_time}!")
    print(f"> Current ping: {round(bot.latency * 1000)} MS.")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.reply("Please enter a valid command!")
        return
    return error

@bot.command()
async def ping(ctx):
    await ctx.reply(f'Responded within {round(bot.latency * 1000)} MS.')

@bot.command()
async def say(ctx, *arg):
    words = ' '.join(arg) 
    await ctx.reply(words)

try:
    bot.run(bot_token)
except discord.errors.LoginFailure:
    input("> There was an error trying to log in.")
