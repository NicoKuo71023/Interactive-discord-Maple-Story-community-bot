import discord
from discord.ext import commands
import json 
import random
with open('setting.json', mode='r', encoding='utf8') as jfile:   # r=read 讀取模式 encoding 解碼 可能用中文
    jdata = json.load(jfile)


bot = commands.Bot(command_prefix = '')

@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.event
async def on_member_join(member):
    print(F'{member}join!')
    channel = bot.get_channel(755994529013694584) #記得要做資料轉換 轉成int int()
    await channel.send(F'{member}嘿嘿嘿 歡迎加入~')    #await 呼叫斜成 

@bot.event
async def on_member_remove(member):
    print(F'{member}Leave!')
    channel = bot.get_channel(755994529013694584)
    await channel.send(F"{member}不要走~") 
@bot.command()
async def ping(ctx):
    await ctx.send(F'{round(bot.latency*1000)} ms') #round()四捨五入進位

@bot.command()
async def 圖片(ctx):
    pic = discord.File(jdata['pic']) #有特殊服號 \改\\ ex. \n) #有特殊服號 \改\\ ex. \n
    await ctx.send(file = pic)

@bot.command()
async def 隨圖(ctx):
    random_pic = random.choice(jdata['pic']) #路徑可以試圖片的url
    pic = discord.File(random_pic) #有特殊服號 \改\\ ex. \n) #有特殊服號 \改\\ ex. \n 
    await ctx.send(file = pic)

@bot.command()
async def 咚神(ctx):
    random_dong = random.choice(jdata['dong'])
    await ctx.send(random_dong) 

@bot.command()
async def 叮咚(ctx):
    random_dong = random.choice(jdata['dong'])
    await ctx.send(random_dong) 

@bot.command()
async def exp(ctx):
    await ctx.send("基礎經驗\n基礎經驗　：100%\n\n消耗品類\n經驗加倍卡　：+50% / +100% /+200%\n經驗密藥　：+10%\n怪公藥水　：+10%\n天氣加持　：+50%\n\n裝備效果\n精靈墜飾　：+10%~+30%\n伊露納項鍊　：+10%\n降魔十字旅團戒　：+2%\n真降魔的十字旅團戒：+3%\n異世界生活勳章　：+5%\n\n分身給予\n戰地經驗格　：+10%\n神之子角色卡　：+4%~+12%\n精靈遊俠傳授　：+15%\n\n技能效果\n祈禱　：+50%\n實用的祈禱　：+35%\n幸運骰子　：+30%\n\n其他\n商城加倍　：*200%(可與加倍卡或苦行疊加)\n苦行戒指　：+15%\n極限屬性　：+0.5%~10%\n燃燒　：+10%~+100%(~+150%)\n經驗寵物　：+7%~+20%\n高級服務　：+30%\n地圖輪　：+100% (3分鐘/4.5分鐘)\n克服的經驗　：+50% (被擊100次20秒)") 

bot.run(jdata['TOKEN'])
