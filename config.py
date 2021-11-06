import joblib
import yaml

# yamlから設定を取得
with open('botconfig.yml') as file:
    conf = yaml.safe_load(file)

# yamlからオブジェクトを分割して使いやすくします

# token
token = conf['token']

# helpオブジェクト
helpob = conf['help']

# mapオブジェクト
mapob = conf['map']
map_list = joblib.load(mapob['file'])

# todoオブジェクト
todoob = conf['todo']

# channelidオブジェクト
channelid = conf['channel_id']

# botの隠し機能的なヤツ
botcom = conf['bot_response']

pepper = conf['pepper']
