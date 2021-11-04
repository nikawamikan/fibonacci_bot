import discord
import time

TOKEN = "ODkzNDUwNzUxODk5MjIyMDQ2.YVbo2g.HMywC8wQ70lCBBD5xwyLD9eDNmQ"
client = discord.Client()

embed = discord.Embed(
    color=0x00ff00,
    title='Bumpできます！',
)


async def bump(message):

    try:
        if (message.author.id == 302050872383242240) &\
                ("Bump done!" in message.embeds[0].description):
            time.sleep(7200)
            await message.channel.send("<@&904965422019932190>")
            embed.title = 'Bumpできます！'
            embed.description = '`!d bump` でサーバーの掲載順を上にできます!'
            await message.channel.send(embed=embed)
    except TypeError:
        return
    except IndexError:
        return


async def dissoku(message):
    try:
        if(message.author.id == 761562078095867916) &\
                ("をアップしたよ!" in message.embeds[0].description):
            time.sleep(3600)
            await message.channel.send("<@&904965422019932190>")
            embed.title = 'dissoku upできます！'
            embed.description = '`!dissoku up` でサーバーの掲載順を上にできます!'
            await message.channel.send(embed=embed)
    except TypeError:
        return
    except IndexError:
        return
