# coding=utf-8

'''
妹子图图片抓取并实现多线程下载
'''
import socket
import time
import requests
import urllib.request
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED


# 该函数用于下载图片
# 传入函数： 网页的网址url
def download_picture(url):
    print(u'图片下载地址：', url)
    # 获取网页的源代码
    # r = requests.get(url)
    r = request(url)
    # 利用BeautifulSoup将获取到的文本解析成HTML
    soup = BeautifulSoup(r.text, "lxml")
    # 获取网页中的电影图片
    content = soup.find('div', class_='main-image')
    images = content.find_all('img')
    # 获取电影图片的名称和下载地址
    picture_name_list = [image['alt'] for image in images]
    picture_link_list = [image['src'] for image in images]

    print(picture_name_list, '\n', picture_link_list)

    # 利用urllib.request..urlretrieve正式下载图片
    for picture_name, picture_link in zip(picture_name_list, picture_link_list):
        urllib.request.urlretrieve(picture_link, 'D://meizitu/%s.jpg' % picture_name)

# 记录文件下载记录
# def Schedule(a, b, c):
#     '''''
#     a:已经下载的数据块
#     b:数据块的大小
#     c:远程文件的大小
#    '''
#     per = 100.0 * a * b / c
#     if per > 100:
#         per = 100
#     print('%.2f%%' % per)


def main():
    # 全部10个网页
    # start_urls = ["https://movie.douban.com/top250"]
    start_urls = []
    for i in range(1, 48):
        start_urls.append("http://www.mzitu.com/139218/%d/" % i)

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


def request(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'Referer': 'http://www.mzitu.com/139218'
    }
    try:
        content = requests.get(url, headers=headers)
        return content
    except FileNotFoundError or socket.timeout:
        pass


main()
