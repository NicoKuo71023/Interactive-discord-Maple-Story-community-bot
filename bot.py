import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '[')

@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.event
async def on_member_join(member):
    print(F'{member}join!')
    channel = bot.get_channel(755994529013694584)
    await channel.send(F'@{member}嘿嘿嘿 歡迎加入~')    #await 呼叫斜成

@bot.event
async def on_member_remove(member):
    print(F'{member}Leave!')
    channel = bot.get_channel(755994529013694584)
    await channel.send(F"@{member}不要走~") 

bot.run('NzU1OTYwMDUwMjA3NDI0Njgy.X2K4qQ.T2bNsQjeOUKCq-vcCQvGv5p78n0')