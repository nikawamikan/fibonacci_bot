import discord
import time

client = discord.Client()

# BOTを監視してEmbedオブジェクトを送信します


def bot_observer(message, pepper: map):
    try:
        print(message.embeds[0].title)
        print(message.embeds[0].field[0])

        if (message.author.id == pepper['id']) &\
                (pepper['trigger'] in message.embeds[0].description):
            time.sleep(pepper['sleep'])
            message.channel.send(pepper['channel'])
            embed = discord.Embed(color=pepper['embed']['color'],
                                  title=pepper['embed']['title'],
                                  description=pepper['embed']['description'])
            message.channel.send(embed=embed)
    except TypeError:
        return
    except IndexError:
        return
