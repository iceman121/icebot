#!/usr/bin python3

import discord
from discord.ext import commands

from configparser import ConfigParser

import requests

parser = ConfigParser()
parser.read('cfg.ini')

bot = commands.Bot(command_prefix='>')


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def ip(ctx):
    ip_query = requests.request('GET', 'https://icanhazip.com').replace('\\n', '')
    await ctx.send(ip_query.text)


bot.run(parser['Discord']['token'])
