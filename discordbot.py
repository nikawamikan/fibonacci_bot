from todo import get_todo
from config import todoob
from config import botcom
from config import channelid
from config import map_list
from config import helpob
from config import token
import os
from dotenv import load_dotenv

import discord
import re
import fibomap

from botsender import if_bot_response
from botsender import if_help_embed_sender


load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = discord.Bot()


# 正規表現のプリコンパイル
todopt = re.compile(todoob['targetwd'])

client = discord.Client()


@client.event
async def on_message(message):

    #  ----------------------隠しコマンド---------------------------#
    await if_bot_response(message=message, obj=botcom['yagarekudasai'])
    await if_bot_response(message=message, obj=botcom['gomennasorry'])
    await if_bot_response(message=message, obj=botcom['fibo'])

# 通常のコマンド判定の為botかどうかなどを判定
    if message.author.bot or (message.channel.id != channelid['fibo_chat']) & (message.channel.id != channelid['bot']):
        return

    if "/test" in message.content:
        await message.channel.send(":gg::+1:")

# ------------------------help-------------------------------#

    await if_help_embed_sender(message, obj=helpob['cin'])
    await if_help_embed_sender(message, obj=helpob['help'])

# コマンドオブジェクトの定義
    command = message.content.split()
# -----------------------Todoリスト----------------------------#

    if(todopt.match(message.content) != None):
        await get_todo(message, command)
        return

# -----------------------map----------------------------#

    if("/map" in message.content) or ("・まp" in message.content):
        await fibomap.get_map(message, command, map_list, todoob)
        return


client.run(TOKEN)
