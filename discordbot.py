import discord
import joblib

TOKEN = "TOKEN"
chat2_channel_id = 000
bot_channel_id = 00

map_file = "map.txt"
map_list = joblib.load(map_file)

todo_file = "todo.txt"
Todo_list = joblib.load(todo_file)

client = discord.Client()


def is_num(text):
    try:
        int(text)
    except ValueError:
        return False
    return True


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

    if (message.channel.id != chat2_channel_id) & (message.channel.id != bot_channel_id):
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

        if(len(command) < 2):
            pass
        elif("add" == command[1]) or ("あっd" == command[1]):
            text = ""
            for i in command:
                if (i != "/todo") & (i != "add") & (i != "あっd") & (i != "・とど"):
                    text += i
                    text += " "

            if(text in Todo_list):
                await message.channel.send("ｿﾚﾓｳﾘｽﾄﾆｱﾙﾖ")
            else:
                if not(text == ""):
                    Todo_list.append([text, message.author.name, "未定"])
                    await message.channel.send("「"+text+"」を追加しました")
                    joblib.dump(Todo_list, todo_file, compress=3)
                else:
                    await message.channel.send("書式しっかりしやがれください")
                    file_img = discord.File("image/sikkari.gif")
                    await message.channel.send(file=file_img)
                    return
        elif("done" == command[1]) or ("どね" == command[1]):
            try:
                await message.channel.send("「"+Todo_list.pop(int(command[2])-1)[0]+"」を完了しました🎉")
                joblib.dump(Todo_list, todo_file, compress=3)
            except ValueError:
                await message.channel.send("このリストの数字で指定しやがれください")
                file_img = discord.File("image/sitei.gif")
                await message.channel.send(file=file_img)
            except IndexError:
                await message.channel.send("そんなリストないわ!出直しやがれください")
                file_img = discord.File("image/denaosi.gif")
                await message.channel.send(file=file_img)
        elif("do" == command[1]) or ("ど" == command[1]):
            try:
                if ("cancel" == command[-1]) or ("cあんcえl" == command[-1]):
                    Todo_list[int(command[2])-1][2] = "未定"
                    await message.channel.send(command[2]+"の実行をキャンセルしました")
                    joblib.dump(Todo_list, todo_file, compress=3)
                else:
                    Todo_list[int(command[2])-1][2] = message.author.name
                    await message.channel.send("えー、なんか"+message.author.name+"さんが"+command[2] +
                                               "を実行するらしいです")
                    joblib.dump(Todo_list, todo_file, compress=3)
            except ValueError:
                await message.channel.send("このリストの数字で指定しやがれください")
                file_img = discord.File("image/sitei.gif")
                await message.channel.send(file=file_img)
            except IndexError:
                await message.channel.send("そんなリストないわ!出直しやがれください")
                file_img = discord.File("image/denaosi.gif")
                await message.channel.send(file=file_img)
        elif("help" == command[1]) or ("へlp" == command[1]):
            helpEmbed = discord.Embed(
                title="＜TODOリスト機能＞",
                color=0x00ff00,
                description="by...リストに追加した人です\n\
do...その項目を実行する人です\n\
\n\
/todo : TODOリストを表示\n\
\n\
/todo add ＜やること＞ : リストに＜やること＞を追加\n\
\n\
/todo done ＜やったこと(番号指定)＞ : リストから＜やったこと＞を削除\n\
\n\
/todo do ＜やること(番号指定)＞ : ＜やること＞の do が自分の名前になる\n\
\n\
/todo do ＜やっぱやらないこと(番号指定)＞ cancel : 上のやつをキャンセル"
            )
            await message.channel.send(embed=helpEmbed)
            return
        else:
            await message.channel.send("そんなコマンドねーよ!出直しやがれください")
            file_img = discord.File("image/denaosi.gif")
            await message.channel.send(file=file_img)

        embed = discord.Embed(
            title="＜TODOリスト＞",
            color=0x00ff00,
        )

        for i in range(len(Todo_list)):
            embed.add_field(
                name=str(i+1)+", "+Todo_list[i][0], value="by : "+Todo_list[i][1]+"\n"+"do : " +
                Todo_list[i][2])

        await message.channel.send(embed=embed)

# -----------------------map----------------------------#

    if("/map" in message.content) or ("・まp" in message.content):

        if(len(command) < 2):
            pass
        elif("add" == command[1]) or ("あっd" == command[1]):
            place = "("+command[-3]+","+command[-2]+","+command[-1]+")"
            title = ""
            for i in command:
                if (i != command[-3]) & (i != command[-2]) & (i != command[-1]) &\
                        (i != command[0]) & (i != command[1]):
                    title += i
                    title += " "

            if(title in map_list):
                await message.channel.send("ｿﾚﾓｳﾘｽﾄﾆｱﾙﾖ")
            else:
                if (not title == "") & is_num(command[-3]) & is_num(command[-2]) &\
                        is_num(command[-1]):
                    map_list.append([title, place])
                    await message.channel.send("「"+title+"」とその座標を追加しました")
                    joblib.dump(map_list, map_file, compress=3)
                else:
                    await message.channel.send("書式しっかりしやがれください")
                    file_img = discord.File("image/sikkari.gif")
                    await message.channel.send(file=file_img)
                    return
        elif("delete" == command[1]) or ("でぇて" == command[1]):
            try:
                await message.channel.send("「"+map_list.pop(int(command[2])-1)[0]+"」とその座標を削除しました")
                joblib.dump(map_list, map_file, compress=3)
            except ValueError:
                await message.channel.send("このリストの数字で指定しやがれください")
                file_img = discord.File("image/sitei.gif")
                await message.channel.send(file=file_img)
            except IndexError:
                await message.channel.send("そんなリストないわ!出直しやがれください")
                file_img = discord.File("image/denaosi.gif")
                await message.channel.send(file=file_img)
        elif("update" == command[1]) or ("うpだて" == command[1]):
            if (not is_num(command[-1])) & is_num(command[2]):
                # /map update ＜更新したい項目(番号指定)＞ ＜更新後の名目＞ : リストの＜更新したい項目＞の名目を＜更新後の名目＞に更新
                title = ""
                for i in command:
                    if (not is_num(i)) & (i != "/map") & (i != "update") & (i != "・まp") &\
                            (i != "うpだて"):
                        title += i
                        title += " "
                await message.channel.send(map_list[int(command[2])-1][0]+"→"+title + "に変更しました")
                map_list[int(command[2])-1][0] = title
            elif is_num(command[-3]) & is_num(command[-2]) & is_num(command[-1]) &\
                    is_num(command[2]):
                place = "("+command[-3]+","+command[-2]+","+command[-1]+")"
                await message.channel.send(map_list[int(command[2])-1][0]+"の座標を" +
                                           map_list[int(command[2])-1][1]+"→"+place + "に変更しました")
                map_list[int(command[2])-1][1] = place
            else:
                await message.channel.send("書式しっかりしやがれください")
                file_img = discord.File("image/sikkari.gif")
                await message.channel.send(file=file_img)
                return
            joblib.dump(map_list, map_file, compress=3)

        elif("help" == command[1]) or ("へlp" == command[1]):

            helpEmbed = discord.Embed(
                title="＜map機能＞",
                color=0x00ff00,
                description="建物やトラップタワーなどの座標を保存する機能\n\
\n\
/map : 登録されている名目と座標を表示\n\
\n\
/map add ＜名目＞ ＜X座標＞ ＜Y座標＞ ＜Z座標＞: リストに＜名目＞と座標を追加\n\
\n\
/map delete ＜削除したい項目(番号指定)＞ : リストから＜削除したい項目＞を削除\n\
\n\
/map update ＜更新したい項目(番号指定)＞ ＜更新後の名目＞ : リストの＜更新したい項目＞の名目を＜更新後の名目＞に更新\n\
\n\
/map update ＜更新したい項目(番号指定)＞ ＜更新後のX座標＞ ＜更新後のY座標＞ ＜更新後のZ座標＞: リストの＜更新したい項目＞の座標を更新"
            )
            await message.channel.send(embed=helpEmbed)
            return
        else:
            await message.channel.send("そんなコマンドねーよ!出直しやがれください")
            file_img = discord.File("image/denaosi.gif")
            await message.channel.send(file=file_img)

        embed = discord.Embed(
            title="＜名目と座標＞",
            color=0x00ff00,
        )
        for i in range(len(map_list)):
            embed.add_field(name=str(i+1)+"," +
                            map_list[i][0], value="座標"+map_list[i][1]+"\n")

        await message.channel.send(embed=embed)


client.run(TOKEN)
