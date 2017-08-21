#coding:utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://realdgame.jp/")
bsObj = BeautifulSoup(html, "html.parser")
allText = bsObj.findAll(id="text")
print(allText[0].get_text())
