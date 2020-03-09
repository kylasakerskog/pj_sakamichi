# coding: UTF-8
import requests
import urllib.request
from bs4 import BeautifulSoup
import json
import datetime
import ssl

def acquire(url, headers, dfrom, dto, js=False):
    soup = ""
    if js:
        payload = {
            "member" : "",
            "category" : "",
            "monthly": "",
            "member" : "",
            "category" : "",
            "monthly": "202004"
        }

        r = requests.post(url, headers=headers, data=payload)
        if r.status_code == requests.codes.ok:
            soup = BeautifulSoup(r.content, "html.parser")
    else:
        request = urllib.request.Request(url, headers=headers) 
        html = urllib.request.urlopen(request)
        soup = BeautifulSoup(html, "html.parser")

    div = soup.find_all("div")

    d = []
    l = []

    for i, tag in enumerate(div):
        try:
            string_ = tag.get("class").pop(0)

            if string_ in "first-child":
                d.append(div[i].text.split()[0])
            
            elif string_ in "last-child":
                l.append(div[i])
        except:
            pass

    s = ""

    for i, el in enumerate(l):
        try:
            if i > 0:
                num = int(d[i-1].replace("日", ""))
                if int(dfrom) <= num and num < int(dto):
                    s += d[i-1] + "\n"
                    for li in el.findAll("a"):
                        s += "    " + li.text + "\n"
        except:
            pass

    return s

def output(period=3):
    ssl._create_default_https_context = ssl._create_unverified_context
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"
        }

    url = "http://www.nogizaka46.com/schedule/"

    d_today = datetime.date.today() + datetime.timedelta(days=1)
    l_today = str(d_today).split("-")
    d_endday = d_today + datetime.timedelta(days=period)
    l_endday = str(d_endday).split("-")

    nmonth = l_endday[0] + l_endday[1]

    msg = "乃木坂46 スケジュール (今後" + str(period) + "日)\n" + str(int(l_today[0])) + "年" + str(int(l_today[1])) + "月\n"

    if l_today[1] == l_endday[1]:
        msg += acquire(url, headers, l_today[2], l_endday[2])
    else:
        if int(l_today[1]) < 12:
            year = l_today[0]
            month = str(int(l_today[1])+1).zfill(2)
        else:
            year = str(int(l_today[0])+1).zfill(4)
            month = "01"

        msg += acquire(url, headers, l_today[2], "33")
        msg += year + "年" + str(int(month)) + "月\n"
        msg += acquire(url, headers, "01", l_endday[2], True)

    return msg

if __name__ == "__main__":
    msg = output(5)
    print(msg)
