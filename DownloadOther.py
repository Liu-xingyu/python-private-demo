# coding:utf-8
''' 实现在1024网站下载抓去图片 '''

import requests
import os
from bs4 import BeautifulSoup


class DownloadOther():
    def download(self, url):
        self.mkDir(url.get_text())
        # href = 'http://w3.nat789.info/pw/htm_data/16/1712/936021.html'
        print(url)
        self.get_imgUrl(url)

    def mkDir(self, path):
        path = path.strip()
        isExists = os.path.exists(os.path.join("D:\portray002", path))
        if not isExists:
            print('建了一个名字叫做   ' + path + '  的文件夹！')
            os.makedirs(os.path.join("D:\portray002", path))
            os.chdir(os.path.join("D:\portray002", path))  # #切换到目录
            return True
        else:
            print('名字叫做' + path + '的文件夹已经存在了！')
            return False

    def get_imgUrl(self, url):
        index = 0
        html = self.request(url)
        print(html)
        img_urls = BeautifulSoup(html.text, 'lxml').find('div', class_='tpc_content').find_all('img')
        for img_url in img_urls:
            index = index + 1
            src = img_url['src']
            print(u'第', index, u'张图片        详细地址：', src)
            self.saveFile(src)

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


download = DownloadOther()
download.download('http://w3.nat789.info/pw/htm_data/16/1712/936021.html')
