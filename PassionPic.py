# coding:gb2312
import requests
from bs4 import BeautifulSoup
import os


class PassionPic():
    def all_url(self, url):
        title = 1001;
        html = self.request(url)  # 调用request函数把套图地址传进去会返回给我们一个response
        all_a = BeautifulSoup(html.text, 'lxml').find('div', class_='t z').find_all('h3')
        for a in all_a:
            real_href = a.find('a')
            # real_imgUrl = 'http://1024v3.org/pw/'+real_href['href']
            # title = real_href.get_text()
            title = title + 1
            if title > 1010:
                print(u'开始保存：', title)  # 加点提示不然太枯燥了
                path = str(title).replace("?", '_')  ##我注意到有个标题带有 ？  这个符号Windows系统是不能创建文件夹的所以要替换掉
                self.mkdir(path)  ##调用mkdir函数创建文件夹！这儿path代表的是标题title哦！！！！！不要糊涂了哦！
                href = 'http://1024v3.org/pw/' + real_href['href']
                print('真的地址：', href)
                self.img(href)  ##调用html函数把href参数传递过去！href是啥还记的吧？ 就是套图的地址哦！！不要迷糊了哦！

                # class_='tpc_content' find_all('img')['src']

    def html(self, href):  ##这个函数是处理套图地址获得图片的页面地址
        html = self.request(href)
        print(html)
        max_span = BeautifulSoup(html.text, 'lxml').find('div', class_='tpc_content').find_all('span')[-2].get_text()
        for page in range(1, int(max_span) + 1):
            page_url = href + '/' + str(page)
            print('page_url:', page_url)
            self.img(page_url)  ##调用img函数

    def img(self, page_url):  ##这个函数处理图片页面地址获得图片的实际地址
        img_html = self.request(page_url)
        img_urls = BeautifulSoup(img_html.text, 'lxml').find('div', class_='tpc_content').find_all('img')
        for img_url in img_urls:
            print('img_url:', img_url['src'])
            self.save(img_url['src'])

    def save(self, img_url):  ##这个函数保存图片
        name = img_url[-9:-4]
        img = self.request(img_url)
        f = open(name + '.jpg', 'ab')
        f.write(img.content)
        f.close()

    def mkdir(self, path):  ##这个函数创建文件夹
        path = path.strip()
        isExists = os.path.exists(os.path.join("D:\passions", path))
        if not isExists:
            print(u'建了一个名字叫做', path, u'的文件夹！')
            os.makedirs(os.path.join("D:\passions", path))
            os.chdir(os.path.join("D:\passions", path))  ##切换到目录
            return True
        else:
            print(u'名字叫做', path, u'的文件夹已经存在了！')
            return False

    def request(self, url):  ##这个函数获取网页的response 然后返回
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
        content = requests.get(url, headers=headers)
        return content


passion = PassionPic()  ##实例化
passion.all_url('http://1024v3.org/pw/thread.php?fid=16')  ##给函数all_url传入参数  你可以当作启动爬虫（就是入口）
