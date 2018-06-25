# coding:utf-8
''' 实现在1024网站下载抓去图片 '''

import os
import socket

import requests
from bs4 import BeautifulSoup


class PassionPictures():
    # url_prefix = 'http://1024.hlork9.rocks/pw/'
    # save_dir = "D:\passions"
    url_prefix = 'http://1024.qdldd.biz/pw/'
    save_dir = "D:\portray001"

    def get_url(self, url):
        index = 0
        html = self.request(url)
        all_a = BeautifulSoup(html.text, 'lxml').find('div', class_='t z').find_all('h3')
        for a in all_a:
            index += 1
            if index > 5:
                real_url = a.find('a')
                self.mkDir(real_url.get_text(), self.save_dir)
                # href = 'http://d2.sku117.com/pw/' + real_url['href']
                href = self.url_prefix + real_url['href']
                # http://1024.hlork9.rocks/pw/thread.php?fid=16
                print(href)
                # 保存图片
                self.get_imgUrl(href)

    def get_perPage(self, url):
        html = self.request(url)
        real_page = ''
        page_urls = BeautifulSoup(html.text, 'lxml').find('div', class_='pages').find_all('a')
        for page_url in page_urls:
            real_page = self.url_prefix + page_url['href']
            # print(real_page)
        temp = real_page[:-3]  # 把得到的地址最后面的三位数字去掉，组合下面任意数字表示多少页
        # print(temp)
        for i in range(1, 2):
            perUrl = temp + str(i)
            self.get_url(perUrl)

    def get_imgUrl(self, url):
        index = 0
        html = self.request(url)
        img_urls = BeautifulSoup(html.text, 'lxml').find('div', class_='tpc_content').find_all('img')
        for img_url in img_urls:
            index = index + 1
            src = img_url['src']
            print(u'第', index, u'张图片        详细地址：', src)
            self.saveFile(src)

    ''' 创建文件夹 '''

    def mkDir(self, path, realIOPath):
        # realIOPath = "D:\portray001"
        path = path.strip()
        spath = path.encode('ISO-8859-1', 'ignore').decode('utf-8')
        isExists = os.path.exists(os.path.join(realIOPath, spath))
        if not isExists:
            print('建了一个名字叫做   ' + spath + '  的文件夹！')
            os.makedirs(os.path.join(realIOPath, spath))
            os.chdir(os.path.join(realIOPath, spath))  # #切换到目录
            return True
        else:
            print('名字叫做' + spath + '的文件夹已经存在了！')
            return False

    ''' 保存图片到文件夹 '''

    def saveFile(self, img_url):
        name = img_url[-9:-4]
        try:
            img = self.request(img_url)
            f = open(name + '.jpg', 'ab')
            f.write(img.content)
        except socket.timeout or FileNotFoundError or IOError or ConnectionError or ConnectionRefusedError or ConnectionAbortedError:
            pass
        finally:
            f.close()

    def request(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
        try:
            content = requests.get(url, headers=headers)
            return content
        except FileNotFoundError or socket.timeout:
            pass


passion = PassionPictures()
# passion.get_perPage('http://1024.hlork9.rocks/pw/thread.php?fid=16')
passion.get_perPage('http://1024.qdldd.biz/pw/thread.php?fid=14')

# http://y3.1024yxy.net/pw/thread.php?fid=14
