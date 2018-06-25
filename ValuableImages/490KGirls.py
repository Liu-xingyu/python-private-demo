# coding=utf-8
'''
抓取https://www.490k.com/图片
'''
import os
import random
import socket

import requests
from bs4 import BeautifulSoup


class BeautifulGirls():
    # 初始化URL
    def __init__(self, url):
        self.url = url

    # 得到二级标题
    def secondTitle(self, url):
        html = self.request(url)
        all_links = BeautifulSoup(html.text, 'lxml').find('dd', class_='page').find_all('a')
        index = 0
        for link in all_links:
            index = index + 1
            if index > 5:
                tempUrl = self.url + link['href']
                print('第', index, '页，地址=', tempUrl)
                self.get_pageUrl(tempUrl)

    # 得到界面
    def get_pageUrl(self, url):
        html = self.request(url)
        # all_links = BeautifulSoup(html.text, 'lxml').find('dl', class_='hot public-box').find_all('dd')
        # all_links = BeautifulSoup(html.text, 'lxml').find('dl', class_='channel public-box').find_all('dd')
        # all_links = BeautifulSoup(html.text, 'lxml').find('ul', class_='new public-box').find_all('li')

        all_links = BeautifulSoup(html.text, 'lxml').find('dl', class_='list-left public-box').find_all('dd')

        # 序号
        serialNo = 0
        for link in all_links:
            serialNo = serialNo + 1
            if serialNo <= 30:
                # 得到a标签
                _href = link.find('a')
                # 得到a标签标题
                _title = _href.get_text()
                # 得到a标签具体路径
                _url = self.url + _href['href']
                self.mkDir(_title)
                self.get_imgsUrl(_url)

    # 得到下一界面中所有图片的真实地址
    def get_imgsUrl(self, url):
        index = 0
        content = self.request(url)
        all_imgsUrl = BeautifulSoup(content.text, 'lxml').find('div', class_='content-page').find_all('a')
        for imgsUrl in all_imgsUrl:
            index = index + 1
            if index > 1:
                img_url = imgsUrl['href']
                real_url = self.url + img_url
                self.getImg(real_url)

    # 得到真正的图片
    def getImg(self, imgUrl):
        content = self.request(imgUrl)
        image = BeautifulSoup(content.text, 'lxml').find('div', class_='content-pic').find('img')
        print(image['title'] + "   " + image['src'])
        self.saveImgs(image['src'])

    # 请求页面资源
    def request(self, url):
        user_agents = [
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
            'Opera/9.25 (Windows NT 5.1; U; en)',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
            'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
            'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
            'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
            "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
            "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ",
        ]
        # 反盗链 'Referer': 'https://www.490k.com/' 加上之后可以是别为从服务器跳转，否则被屏蔽 返回403 forbidden
        headers = {'User-Agent': random.choice(user_agents), 'Referer': 'https://www.490k.com/', 'host': 'www.490k.com'}
        content = requests.get(url, headers=headers)

        return content

    # 创建文件夹
    def mkDir(self, dirName):
        # 去除字符串首尾空格 类似于java的trim()
        dirName = dirName.strip()
        isExists = os.path.exists(os.path.join("D:\Beautiful\girls", dirName))
        if not isExists:
            print('建了一个名字叫做   ' + dirName + '  的文件夹！')
            os.makedirs(os.path.join("D:\Beautiful\girls", dirName))
            os.chdir(os.path.join("D:\Beautiful\girls", dirName))  # #切换到目录
            return True
        else:
            print('名字叫做' + dirName + '的文件夹已经存在了！')
            return False

    # 存储图片
    def saveImgs(self, img_url):
        name = img_url[-9:-4]
        try:
            img = self.request(img_url)
            f = open(name + '.jpg', 'ab')
            f.write(img.content)
        except socket.timeout or FileNotFoundError or IOError or ConnectionError or ConnectionRefusedError or ConnectionAbortedError:
            pass
        finally:
            f.close()


girls = BeautifulGirls('https://www.490k.com')
girls.secondTitle('https://www.490k.com/xinggan/list_2.html')
