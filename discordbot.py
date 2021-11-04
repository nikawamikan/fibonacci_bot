import discord
import joblib
import fibomap
import todo
import yaml
import bump

with open('botconfig.yml') as file:
    conf = yaml.safe_load(file)
    print(conf['help']['cin']['targetwd'])

mapob = conf['map']
map_list = joblib.load(mapob['file'])

todoob = conf['todo']
Todo_list = joblib.load(todoob['file'])

client = discord.Client()


@client.event
async def on_message(message):

    await bump.bump(message=message)
    await bump.dissoku(message=message)

    # ----------------------その他コマンド---------------------------#
    if ("すみません" in message.content) or ("ごめん" in message.content):
        file_img = discord.File("image/sorry.gif")
        await message.channel.send(file=file_img)

    if("やがれください" in message.content):
        file_yagare = discord.File("image/simple_yagare.gif")
        await message.channel.send(file=file_yagare)
    if("ふぃぼなっち" in message.content):
        file_img = discord.File("image/fibonacci.png")
        await message.channel.send(file=file_img)

    if message.author.bot:
        return

    if (message.channel.id != conf['channel_id']['fibo_chat']) & (message.channel.id != conf['channel_id']['bot']):
        return

    command = message.content.split()

    if "/test" in message.content:
        await message.channel.send(":gg::+1:")
# ------------------------help-------------------------------#
    if(conf['help']['help']['targetwd'] in message.content) or (conf['help']['help']['targetwd2'] in message.content):
        helpEmbed = discord.Embed(
            title=conf['help']['help']['title'],
            color=conf['help']['help']['color'],
            description=conf['help']['help']['description'])
        await message.channel.send(embed=helpEmbed)

    if(conf['help']['cin']['targetwd'] in message.content):
        helpEmbed = discord.Embed(
            title=conf['help']['cin']['title'],
            color=conf['help']['cin']['color'],
            description=conf['help']['help']['description'])
        await message.channel.send(embed=helpEmbed)

# -----------------------Todoリスト----------------------------#
    if("/todo" in message.content) or ("・とど" in message.content):
        await todo.get_todo(message, command, Todo_list, map)

# -----------------------map----------------------------#

    if("/map" in message.content) or ("・まp" in message.content):
        await fibomap.get_map(message, command, map_list, todoob)


client.run(conf['token'])
