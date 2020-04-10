import discord
from discord.ext import commands
import json

with open("setting.json",'r',encoding='UTF-8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='/')
token = "Njk4MjIwMzY2Njg2MDYwNTY1.XpCqhA.uE5AiiTTohaoKHexGEOM-kxCEf8"

@bot.event
async def on_ready():
    print("嗶啵，啵嗶?")

bot.run(token)
