import discord
import time

client = discord.Client()

# BOTを監視してEmbedオブジェクトを送信します


async def bot_observer(message, pepper):
    try:

        if (message.author.id == pepper['id']) &\
                (pepper['trigger'] in message.embeds[0].description):
            time.sleep(pepper['sleep'])
            await message.channel.send(pepper['channel'])
            embed = discord.Embed(color=pepper['embed']['color'],
                                  title=pepper['embed']['title'],
                                  description=pepper['embed']['description'])
            await message.channel.send(embed=embed)
    except TypeError:
        return
    except IndexError:
        return
