# coding=utf-8

import time
import requests
import urllib.request
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED


# 该函数用于下载图片
# 传入函数： 网页的网址url
def download_picture(url):
    # 获取网页的源代码
    r = requests.get(url)
    # 利用BeautifulSoup将获取到的文本解析成HTML
    soup = BeautifulSoup(r.text, "lxml")
    # 获取网页中的电影图片
    content = soup.find('div', class_='article')
    images = content.find_all('img')
    # 获取电影图片的名称和下载地址
    picture_name_list = [image['alt'] for image in images]
    picture_link_list = [image['src'] for image in images]

    # 利用urllib.request..urlretrieve正式下载图片
    for picture_name, picture_link in zip(picture_name_list, picture_link_list):
        urllib.request.urlretrieve(picture_link, 'D://douban/%s.jpg' % picture_name)

# 记录文件下载记录
def Schedule(a, b, c):
    '''''
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
   '''
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print('%.2f%%' % per)


def main():
    # 全部10个网页
    start_urls = ["https://movie.douban.com/top250"]
    for i in range(1, 10):
        start_urls.append("https://movie.douban.com/top250?start=%d&filter=" % (25 * i))

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


main()
