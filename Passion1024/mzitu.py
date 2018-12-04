# coding=utf-8

'''
妹子图图片抓取并实现多线程下载
后期还有许多需要改善，优化处理
'''
import os
import requests
import socket
import time
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED


# 该函数用于下载图片
# 传入函数： 网页的网址url
def download_picture(url):
    print(u'图片下载地址：', url)
    # 获取网页的源代码
    # r = requests.get(url)
    r = request(url, 'www.mzitu.com')
    # 利用BeautifulSoup将获取到的文本解析成HTML
    soup = BeautifulSoup(r.text, "lxml")
    # 获取网页中的电影图片
    content = soup.find('div', class_='main-image')
    images = content.find_all('img')
    # 获取电影图片的名称和下载地址
    picture_name_list = [image['alt'] for image in images]
    picture_link_list = [image['src'] for image in images]

    # print(picture_name_list, '\n', picture_link_list)

    # 利用urllib.request..urlretrieve正式下载图片
    for picture_name, picture_link in zip(picture_name_list, picture_link_list):
        # print(u'图片浏览地址：', picture_link)
        # print(u'图片描述：', picture_name)
        print(picture_name, u':%s' % picture_link)
        # urllib.request.urlretrieve(picture_link, 'E://meizitu/%s.jpg' % picture_name)
        # urllib.request.urlretrieve(picture_link, 'E://douban/%s.jpg' % picture_link[-9,-5], Schedule)
        mkDir(picture_name, 'E:\\meizitu')
        saveFile(picture_link)


# 记录文件下载记录https://i.meizitu.net/2018/06/17b06.jpg
'''
a:已经下载的数据块
b:数据块的大小
c:远程文件的大小
'''


# def Schedule(a, b, c):
#     per = 100.0 * a * b / c
#     if per > 100:
#         per = 100
#     print('%.2f%%' % per)

# 创建文件夹
def mkDir(path, realIOPath):
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


# 保存图片
def saveFile(img_url):
    name = img_url[-9:-4]
    try:
        img = request(img_url, 'i.meizitu.net')
        f = open(name + '.jpg', 'ab')
        f.write(img.content)
    except socket.timeout or FileNotFoundError or IOError or ConnectionError or ConnectionRefusedError or ConnectionAbortedError:
        pass
    finally:
        f.close()


# 找到图片最中心模块地址
def main():
    for index in range(11,20):
        url = 'https://www.mzitu.com/page/%d/' % index
        html = request(url, 'www.mzitu.com')
        page_urls = BeautifulSoup(html.text, 'lxml').find('div', class_='postlist').find_all('a')
        num = 1
        for page_url in page_urls:
            if num > 0 and num <= 24:
                # print(page_url['href'])
                getMainPicUrls(page_url['href'])
            else:
                continue
            num = num + 1


def getMainPicUrls(url):
    # 全部10个网页
    # start_urls = ["https://movie.douban.com/top250"]
    start_urls = []
    for i in range(1, 30):
        # print(url+'/%d/' % i)
        start_urls.append(url + '/%d/' % i)

    # 统计该爬虫的消耗时间
    print('*' * 50)
    t3 = time.time()

    # 利用并发下载电影图片
    executor = ThreadPoolExecutor(max_workers=10)  # 可以自己调整max_workers,即线程的个数
    # submit()的参数： 第一个为函数， 之后为该函数的传入参数，允许有多个
    future_tasks = [executor.submit(download_picture, url) for url in start_urls]
    # 等待所有的线程完成，才进入后续的执行
    wait(future_tasks, return_when=ALL_COMPLETED)

    t4 = time.time()
    print('使用多线程，总共耗时：%s' % (t4 - t3))
    print('*' * 50)


def request(url, host):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'Referer': 'https://www.mzitu.com/139218/',
        'Host': host
    }
    try:
        content = requests.get(url, headers=headers)
        return content
    except FileNotFoundError or socket.timeout:
        pass


main()
