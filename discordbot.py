import discord
import joblib
import fibomap
import todo
import yaml
import bump
import re

# yamlから設定を取得
with open('botconfig.yml') as file:
    conf = yaml.safe_load(file)

# yamlからオブジェクトを分割して使いやすくします

# helpオブジェクト
helpob = conf['help']

# mapオブジェクト
mapob = conf['map']
map_list = joblib.load(mapob['file'])

# todoオブジェクト
todoob = conf['todo']

# channelidオブジェクト
channelid = conf['channel_id']

# botの隠し機能的なヤツ
botcom = conf['bot_response']

pepper = conf['pepper']

client = discord.Client()

# 正規表現のプリコンパイル
todopt = re.compile(todoob['targetwd'])

# if文でメッセージ内から条件ワードが含まれているかを検出したあと
# help_embed_senderを呼び出します


async def if_help_embed_sender(message, obj):
    if(re.match(obj['targetwd'], message.content) != None):
        help_embed_sender(message=message, obj=obj)

# Help用のembed関数 先頭文字列から targetwd を正規表現で検索します


async def help_embed_sender(message, obj):
    helpEmbed = discord.Embed(
        title=obj['title'],
        color=obj['color'],
        description=obj['description'])
    await message.channel.send(embed=helpEmbed)

# BOTがなんか読み取ってresponseします


async def bot_response(message, obj):
    if(re.search(obj['targetwd'], message.content) != None):
        file_img = discord.File(obj['img'])
        await message.channel.send(file=file_img)


@client.event
async def on_message(message):

    #  ----------------------隠しコマンド---------------------------#
    await bot_response(message=message, obj=botcom['yagarekudasai'])
    await bot_response(message=message, obj=botcom['gomennasorry'])
    await bot_response(message=message, obj=botcom['fibo'])

# bumpとかdissokuとか検知する子
    await bump.bot_observer(message=message, pepper=pepper['disboard'])
    await bump.bot_observer(message=message, pepper=pepper['dissoku'])

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
        await todo.get_todo(message, command)
        return

# -----------------------map----------------------------#

    if("/map" in message.content) or ("・まp" in message.content):
        await fibomap.get_map(message, command, map_list, todoob)
        return


client.run(conf['token'])
