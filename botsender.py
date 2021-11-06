import re
import discord

# if文でメッセージ内から条件ワードが含まれているかを検出したあと
# help_embed_senderを呼び出します


async def if_help_embed_sender(message, obj):
    if(re.match(obj['targetwd'], message.content) != None):
        await help_embed_sender(message=message, obj=obj)

# Help用のembed関数 先頭文字列から targetwd を正規表現で検索します


async def help_embed_sender(message, obj):
    helpEmbed = discord.Embed(
        title=obj['title'],
        color=obj['color'],
        description=obj['description'])
    await message.channel.send(embed=helpEmbed)

# BOTがなんか読み取ってresponseします


async def if_bot_response(message, obj):
    if(re.search(obj['targetwd'], message.content) != None):
        await bot_response(message=message, obj=obj)


async def bot_response(message, obj):
    file_img = discord.File(obj['img'])
    await message.channel.send(file=file_img)


async def bot_mesimg_response(message, obj):
    await message.channel.send(obj['content'])
    await bot_response(message=message, obj=obj)
