
import discord
from discord.ext import commands
import json
from urllib.request import urlopen
import requests
from weather import *

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>w ', intents=intents)
command_prf = '>w '
api_key = '22d61c33cdf75e0d888a28ec9e07f71e'

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=">w "), status=discord.Status.online)

@bot.event
async def on_message(message):
    if message.author != bot.user and message.content.startswith(command_prf):
        if len(message.content.replace(command_prf, '')) >= 1:
            location = message.content.replace(command_prf, '').lower()
            url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
            try:
                data = parse_data(json.loads(requests.get(url).content)['main'])
                await message.channel.send(embed=weather_message(data, location))
            except KeyError:
                await message.channel.send(embed=error_message(location))


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run('MTA0MzE2MTMwOTgwNzY0NDc4OQ.GpYgDP.-xrnI6cuHhANoGszjhTr4hTjo2ab5oM_AN05_8')


#if message.author != bot.user and message.content.startswith(command_prf):
#        location = message.content.replace(command_prf,'').lower()
#        if len(location) >= 1:
#            url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&APPID={api_key}&units=metric'
#            
#            response = urlopen(url)
#            
#            data = json.loads(response.read())
#            print(data)
