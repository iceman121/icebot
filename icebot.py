#!/usr/bin/python3

import discord
from discord.ext import commands

from configparser import ConfigParser

import requests
import psutil

parser = ConfigParser()
parser.read('cfg.ini')

bot = commands.Bot(command_prefix='>')


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def ip(ctx):
    ip_query = requests.request('GET', 'https://icanhazip.com')
    await ctx.send(ip_query.text.replace('\\n', ''))


@bot.command()
async def status(ctx):
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    await ctx.send(f'CPU util = {cpu:.2f}%, RAM util = {ram:.2f}%')


bot.run(parser['Discord']['token'])
