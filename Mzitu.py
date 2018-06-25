#coding:utf-8

import urllib.request
from bs4 import BeautifulSoup

resp = urllib.request.urlopen('http://www.baidu.com')
html = BeautifulSoup(resp.read(),'lxml')
print(html)

def url_open(self,url):
    _url = url
    for i in _url:
        print(self.i)
