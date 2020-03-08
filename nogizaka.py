# coding: UTF-8
import urllib.request
from bs4 import BeautifulSoup

headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"
        }

url = "http://www.nogizaka46.com/schedule/"
request = urllib.request.Request(url, headers=headers) 
html = urllib.request.urlopen(request)

soup = BeautifulSoup(html, "html.parser")

div = soup.find_all("div")

news = ""
l = []

for i, tag in enumerate(div):
    try:
        string_ = tag.get("class").pop(0)

        if string_ in "last-child":
            l.append(div[i])
    except:
        pass


for i, el in enumerate(l):
    try:
        print(i)
        for li in el.findAll("a"):
            print(li.text)
            
    except:
        pass

