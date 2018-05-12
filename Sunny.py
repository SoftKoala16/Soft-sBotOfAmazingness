import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

bot =commands.Bot(command_prefix="!")

@bot.command(pass_context=True)
async def boast(ctx):
    msg = 'Wow, {0.author.mention} , you are AMAZING!'.format(ctx.message)
    await bot.say(msg)

@bot.command(pass_context=True)
async def amiamazing(ctx):
 msg = 'Well {0.author.mention} , you are..Original!'.format(ctx.message)
 await bot.say(msg)

@bot.command(pass_context=True)
async def ping(ctx):
    msg = 'Pong!'.format(ctx.message)
    await bot.say(msg)

@bot.command(pass_context=True)
async def savage(ctx):
    msg = 'Sorry, my skills are to advanced..For you.'.format(ctx.message)
    await bot.say(msg)

@bot.command(pass_context=True)
async def flip(ctx):
    msg = 'Flip!? I shall not! My CPU will break. Some people >:/'.format(ctx.message)
    await bot.say(msg)


bot.run("NDQ0OTE0NDIwMDI0NDc1NjU4.Ddi32A.KFmJLaYde-AYT51GyBj9Bi0wcSA")
