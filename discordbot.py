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
Todo_list = joblib.load(todoob['file'])

# channelidオブジェクト
channelid = conf['channel_id']

# botの隠し機能的なヤツ
botcom = conf['bot_response']

pepper = conf['pepper']

client = discord.Client()

# Help用のembed関数 先頭文字列から targetwd を正規表現で検索します


async def help_embed_sender(message, obj: map):
    if(re.match(obj['targetwd'], message.content) != None):
        helpEmbed = discord.Embed(
            title=obj['title'],
            color=obj['color'],
            description=obj['description'])
        await message.channel.send(embed=helpEmbed)

# BOTがなんか読み取ってresponseします


async def bot_response(message, obj: map):
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
    if message.author.bot:
        await bump.bot_observer(message=message, pepper=pepper['disboard'])
        await bump.bot_observer(message=message, pepper=pepper['dissoku'])

        return

    if (message.channel.id != channelid['fibo_chat']) & (message.channel.id != channelid['bot']):
        return

    command = message.content.split()

    if "/test" in message.content:
        await message.channel.send(":gg::+1:")

# ------------------------help-------------------------------#

    await help_embed_sender(message, obj=helpob['cin'])
    await help_embed_sender(message, obj=helpob['help'])

# -----------------------Todoリスト----------------------------#

    if("/todo" in message.content) or ("・とど" in message.content):
        await todo.get_todo(message, command, Todo_list, map)

# -----------------------map----------------------------#

    if("/map" in message.content) or ("・まp" in message.content):
        await fibomap.get_map(message, command, map_list, todoob)


client.run(conf['token'])
