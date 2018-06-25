# coding:utf-8
'''
爬虫抓去直播吧数据
'''
import socket

import requests
from bs4 import BeautifulSoup


class Zhibo8():
    def get_html(self, url):
        html = self.request(url)
        all_a = BeautifulSoup(html.text, 'lxml').find('div', class_='nav').find_all('li')
        for a in all_a:
            real_url = a.find('a')
            secondUrl = real_url['href']
            if 'http' not in secondUrl:
                secondUrl = 'https:' + secondUrl
            else:
                continue

            # 必须先编码，后解码
            print('栏目名称=' + real_url.get_text().encode('ISO-8859-1', 'ignore').decode('utf-8') + '   地址=' + secondUrl)

    def request(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
        try:
            content = requests.get(url, headers=headers)
            return content
        except FileNotFoundError or socket.timeout:
            pass


zhibo8 = Zhibo8()
zhibo8.get_html('https://www.zhibo8.cc/')
