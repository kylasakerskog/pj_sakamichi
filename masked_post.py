import hinatazaka
import requests, json
import schedule
import time

def job():
    msg = hinatazaka.output()
    WEB_HOOK_URL = "WEB_HOOK_URL"
    
    requests.post(WEB_HOOK_URL, data = json.dumps({
        'text': msg,  #通知内容
        'username': u'hinatazaka-bot',  #ユーザー名
        'icon_emoji': u':hinatazaka:',  #アイコン
        'link_names': 1,  #名前をリンク化
    }))

schedule.every().day.at("00:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
