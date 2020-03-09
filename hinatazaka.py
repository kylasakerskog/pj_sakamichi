# coding: UTF-8
import urllib.request
from bs4 import BeautifulSoup
import ssl
import datetime

def acquire(url, h, dfrom, dto):
    request = urllib.request.Request(url, headers=h) 
    html = urllib.request.urlopen(request)
    soup = BeautifulSoup(html, "html.parser")
    div = soup.find_all("div")

    news = ""
    l = []

    for i, tag in enumerate(div):
        try:
            string_ = tag.get("class").pop(0)

            if string_ in "p-schedule__list-group":
                l.append(div[i])
        except:
            pass

    s = ""
    for el in l:
        try:
            span = el.find("span").text
            if int(dfrom) <= int(span) and int(span) < int(dto):
                s += span + "日\n"
                p = el.findAll("p")
                for j, li in enumerate(el.findAll("p")):
                    s += "    " + li.text.replace(' ', '').replace('\n', '') + "\n"
        except:
            pass

    return s
def output():
    ssl._create_default_https_context = ssl._create_unverified_context
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"
    }
    
    d_today = datetime.date.today() + datetime.timedelta(days=1)
    l_today = str(d_today).split("-")
    url = "https://www.hinatazaka46.com/s/official/media/list?ima=0000&dy=" + l_today[0] + l_today[1]
    
    d_3day = d_today + datetime.timedelta(days=3)
    l_3day = str(d_3day).split("-")
    
    msg = "日向坂46 スケジュール (今後3日)\n" + str(int(l_today[0])) + "年" + str(int(l_today[1])) + "月\n"
    
    if l_today[1] == l_3day[1]:
        msg += acquire(url, headers, l_today[2], l_3day[2])
    else:
        if int(l_today[1]) < 12:
            year = l_today[0]
            month = str(int(l_today[1])+1).zfill(2)
        else:
            year = str(int(l_today[0])+1).zfill(4)
            month = "01"
        
        nmonth = "https://www.hinatazaka46.com/s/official/media/list?ima=0000&dy=" + year + month
        msg += acquire(url, headers, l_today[2], "32")
        msg += year + "年" + str(int(month)) + "月\n"    
        msg += acquire(nmonth, headers, "01", l_3day[2])
        
    return msg

if __name__ == "__main__":
    msg = output()
    print(msg)
