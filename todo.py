import discord
import joblib


async def get_todo(message, command, Todo_list, todo_file):

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
