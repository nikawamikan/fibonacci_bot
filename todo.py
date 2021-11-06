import re
import discord
from discord.message import Attachment
import joblib
from discordbot import bot_response
from discordbot import help_embed_sender
from discordbot import todoob
Todo_list = joblib.load(todoob['file'])

# コマンドごとのオブジェクトを設定
fpath = todoob['file']
excep = todoob['except']
add = todoob['add']
done = todoob['done']
do = todoob['do']
helpob = todoob['help']
response_embed = todoob['response_embed']

# 正規表現のパフォーマンス向上のため先にコンパイル
addpt = re.compile(add['targetwd'])
donept = re.compile(done['tagertwd'])
dopt = re.compile(do['targetwd'])
cancelpt = re.compile(do['cancel']['targetwd'])

# ToDoリストをDiscordに表示するための関数


async def send_todo(message: discord, Todo_list: list):
    embed = discord.Embed(
        title=response_embed['title'],
        color=response_embed['color'],
    )
    for i in range(0, len(Todo_list)):
        embed.add_field(
            name=response_embed['field']['name'].format(
                str(i+1), Todo_list[i][0]),
            value=response_embed['field']['name'].format(Todo_list[i][1], Todo_list[i][2]))

    await message.channel.send(embed=embed)

# discordbot側から呼び出す判定関数


async def get_todo(message: discord, command):

    try:
        # commandが1の場合は条件式を飛ばす (0以下はありえないので条件から除外)
        if(len(command) == 1):
            pass
        # TODO追加コマンドだった場合
        elif(addpt.fullmatch(command[1]) != None):
            # コマンド配列から代入する値のみを取得
            text = ""
            for i in range(2, len(command)):
                text += command[i] + " "

            # 値があるかをチェック
            if (text != ""):

                if (text in Todo_list):
                    # すでにある場合は例外的に処理
                    await message.channel.send(add['except'])

                else:
                    # add成功時
                    Todo_list.append([text, message.author.name, do["mitei"]])
                    await message.channel.send(add['base'].format(text))
                    joblib.dump(Todo_list, fpath, compress=3)

            else:
                # 値がなかった場合 は例外的に処理
                bot_response(message, excep['syntax'])

        # done 完了だった場合の処理
        elif(donept.fullmatch(command[1]) != None):

            # 配列の量が2を超えることはありえないので弾く
            if(len(command) > 2):

                text = Todo_list.pop(int(command[2])-1)[0]
                await message.channel.send(done['base'].format(text))
                joblib.dump(Todo_list, fpath, compress=3)

            # 弾かれたらメッセージ出しとく
            else:
                bot_response(message, excep['syntax'])
        # do やります系の処理
        elif(dopt.fullmatch(command[1]) != None):

            # 配列の量が3を超えることはありえないので弾く
            if(len(command) > 3):

                # command配列の一番うしろにcancelが含まれる場合
                if (cancelpt.fullmatch(command[2]) != None):
                    Todo_list[int(command[2])-1][2] = do['mitei']
                    await message.channel.send(do['cancel']['base'].format(command[2]))

                # それ以外はそれをやることにする
                else:
                    Todo_list[int(command[2])-1][2] = message.author.name
                    await message.channel.send(do['base'].format(message.author.name, command[2]))

                joblib.dump(Todo_list, fpath, compress=3)

            # 弾かれたらメッセージ出しとく
            else:
                bot_response(message, excep['syntax'])

        # Helpコマンドの場合の処理
        elif(re.fullmatch(help['targetwd'], message.content) != None):
            help_embed_sender(message=message, obj=helpob)
            return

        # どの条件にも当てはまらない場合の処理
        else:
            await bot_response(message=message, obj=excep['nonecom'])

    # 例外発生時のメッセージ
    except ValueError:
        await bot_response(message=message, obj=excep['indexout'])
    except IndexError:
        await bot_response(message=message, obj=excep['nonelist'])

    # 必ずTodoを送るので最後に記述する
    await send_todo(message=message, Todo_list=Todo_list)
