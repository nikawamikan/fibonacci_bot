import discord
import joblib
import fibomap
import todo
import personal


map_file = "map.txt"
map_list = joblib.load(map_file)

todo_file = "todo.txt"
Todo_list = joblib.load(todo_file)

client = discord.Client()


@client.event
async def on_message(message):
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

    if (message.channel.id != personal.CHAT2_CHANNEL_ID) & (message.channel.id != personal.BOT_CHANNEL_ID):
        return

    command = message.content.split()

    if "/test" in message.content:
        await message.channel.send(":gg::+1:")

    if("/help" in message.content) or ("・へlp" in message.content):
        helpEmbed = discord.Embed(
            title="＜コマンド一覧＞",
            color=0x00ff00,
            description="/todo help : TODOリスト機能の詳細はこちら！\n\
\n\
/map help : MAP機能の詳細はこちら！\n\
\n\
/cinnamon help : しなもんbotの詳細はこちら!\n\
\n\
他にも隠しコマンドがあるよ！")
        await message.channel.send(embed=helpEmbed)

    if(("/cinnamon" in message.content) or ("・cいんあもん" in message.content)) &\
            (("help" in message.content) or ("へlp" in message.content)):
        helpEmbed = discord.Embed(
            title="＜しなもんbotの使い方！！＞",
            color=0x00ff00,
            description="!nether 〈x座標〉〈y座標〉\n\
オーバーワールドの座標をネザー座標に変換してくれます。\n\
\n\
!world〈x座標〉〈y座標〉\n\
ネザーの座標をオーバーワールド座標に変換してくれます。\n\
\n\
!gotobed\n\
眠い時に...\n\
\n\
!cin\n\
???????\n\
\n\
!dynmap\n\
拠点回りのmap画像を出してくれます。\n\
更新は手動で気まぐれです。\n\
\n\
!bigdynmap\n\
拠点回りのmap画像を広範囲で出してくれます\n\
周りのバイオームを確認したいときなどにおすすめです。\n\
更新は手動で気まぐれです。\n\
\n\
!vdynmap\n\
拠点を斜めから見ることができます\n\
\n\
しなもんbotが稼働しているかどうかは\n\
https: // knowingnormalexecutables.cinnamon2073new.repl.co /\n\
で確認できます！！\n\
（しなもんbotは今日も元気に稼働中です！！）と出れば稼働中です\n\
ほかの場合は稼働してません。")
        await message.channel.send(embed=helpEmbed)

# -----------------------Todoリスト----------------------------#
    if("/todo" in message.content) or ("・とど" in message.content):
        await todo.get_todo(message, command, Todo_list, todo_file)

# -----------------------map----------------------------#

    if("/map" in message.content) or ("・まp" in message.content):
        await fibomap.get_map(message, command, map_list, map_file)


client.run(personal.TOKEN)
