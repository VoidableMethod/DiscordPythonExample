import discord # Main Discord Package
import os # Used for executing console commands
import platform # Used for detecting the OS

from discord.ext import commands # Do not rename or remove!

# Configuration
prefix = "!" # The prefix for your bot
token = "YourTokenhere" # The token of your bot

bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

@bot.event
async def on_ready():
    if 'Windows' in platform.system():
        os.system("cls")
        os.system("title 'Discord Python Example'")
    elif 'Linux' in platform.system():
        os.system("clear")
    print(f"> Logged in as {bot.user}")
    print(f"> Current ping: {round(bot.latency * 1000)} ms")

@bot.command()
async def ping(ctx):
    await ctx.reply(f"Responded within {round(bot.latency * 1000)} ms")

@bot.command()
async def say(ctx, *arg):
    words = ' '.join(arg)
    await ctx.reply(words)

bot.run(token)
