#!usr/bin/env python3

import discord
from discord.ext import commands
from configparser import ConfigParser

parser = ConfigParser()
parser.read('cfg.ini')

bot = commands.Bot(command_prefix='>')


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(parser['Discord']['token'])
