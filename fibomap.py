import discord
import joblib
import isnum


def help(message):
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
    message.channel.send(embed=helpEmbed)
    return


async def get_map(message, command, map_list, map_file):
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
            if (not title == "") & isnum.is_num(command[-3]) & isnum.is_num(command[-2]) &\
                    isnum.is_num(command[-1]):
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
        if (not isnum.is_num(command[-1])) & isnum.is_num(command[2]):
            # /map update ＜更新したい項目(番号指定)＞ ＜更新後の名目＞ : リストの＜更新したい項目＞の名目を＜更新後の名目＞に更新
            title = ""
            for i in command:
                if (not isnum.is_num(i)) & (i != "/map") & (i != "update") & (i != "・まp") &\
                        (i != "うpだて"):
                    title += i
                    title += " "
            await message.channel.send(map_list[int(command[2])-1][0]+"→"+title + "に変更しました")
            map_list[int(command[2])-1][0] = title
        elif isnum.is_num(command[-3]) & isnum.is_num(command[-2]) & isnum.is_num(command[-1]) &\
                isnum.is_num(command[2]):
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

        help(message)
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
