import hinatazaka
import nogizaka
import requests, json
import schedule
import time

def job():
    WEB_HOOK_URL = "*****"
    channel= "#pj_sakamichi"
    msg = nogizaka.output(3)
    requests.post(WEB_HOOK_URL, data = json.dumps({
        'text': msg,  #通知内容
        'username': u'nogizaka-bot',  #ユーザー名
        'icon_emoji': u':nogizaka-mark:',  #アイコン
        'link_names': 1,  #名前をリンク化
        'channel': channel
    }))
    
    msg = hinatazaka.output(5)
    requests.post(WEB_HOOK_URL, data = json.dumps({
        'text': msg,
        'username': u'hinatazaka-bot',
        'icon_emoji': u':hinatazaka:',
        'link_names': 1,
        'channel': channel
    }))

schedule.every().day.at("00:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
