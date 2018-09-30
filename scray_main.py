#coding:utf-8
import requests
from bs4 import BeautifulSoup

sach={'q':'Pthon','users':'1000'}
url = 'http://b.hatena.ne.jp/search/text'
req = requests.get(url, params = sach, timeout = 15)

with open('sample.htm','w',encoding='utf-8') as f:
    f.write(req.text)

