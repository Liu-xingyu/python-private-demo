# coding:gb2312
import requests
from bs4 import BeautifulSoup
import os


class PassionPic():
    def all_url(self, url):
        title = 1001;
        html = self.request(url)  # ����request��������ͼ��ַ����ȥ�᷵�ظ�����һ��response
        all_a = BeautifulSoup(html.text, 'lxml').find('div', class_='t z').find_all('h3')
        for a in all_a:
            real_href = a.find('a')
            # real_imgUrl = 'http://1024v3.org/pw/'+real_href['href']
            # title = real_href.get_text()
            title = title + 1
            if title > 1010:
                print(u'��ʼ���棺', title)  # �ӵ���ʾ��Ȼ̫������
                path = str(title).replace("?", '_')  ##��ע�⵽�и�������� ��  �������Windowsϵͳ�ǲ��ܴ����ļ��е�����Ҫ�滻��
                self.mkdir(path)  ##����mkdir���������ļ��У����path������Ǳ���titleŶ������������Ҫ��Ϳ��Ŷ��
                href = 'http://1024v3.org/pw/' + real_href['href']
                print('��ĵ�ַ��', href)
                self.img(href)  ##����html������href�������ݹ�ȥ��href��ɶ���ǵİɣ� ������ͼ�ĵ�ַŶ������Ҫ�Ժ���Ŷ��

                # class_='tpc_content' find_all('img')['src']

    def html(self, href):  ##��������Ǵ�����ͼ��ַ���ͼƬ��ҳ���ַ
        html = self.request(href)
        print(html)
        max_span = BeautifulSoup(html.text, 'lxml').find('div', class_='tpc_content').find_all('span')[-2].get_text()
        for page in range(1, int(max_span) + 1):
            page_url = href + '/' + str(page)
            print('page_url:', page_url)
            self.img(page_url)  ##����img����

    def img(self, page_url):  ##�����������ͼƬҳ���ַ���ͼƬ��ʵ�ʵ�ַ
        img_html = self.request(page_url)
        img_urls = BeautifulSoup(img_html.text, 'lxml').find('div', class_='tpc_content').find_all('img')
        for img_url in img_urls:
            print('img_url:', img_url['src'])
            self.save(img_url['src'])

    def save(self, img_url):  ##�����������ͼƬ
        name = img_url[-9:-4]
        img = self.request(img_url)
        f = open(name + '.jpg', 'ab')
        f.write(img.content)
        f.close()

    def mkdir(self, path):  ##������������ļ���
        path = path.strip()
        isExists = os.path.exists(os.path.join("D:\passions", path))
        if not isExists:
            print(u'����һ�����ֽ���', path, u'���ļ��У�')
            os.makedirs(os.path.join("D:\passions", path))
            os.chdir(os.path.join("D:\passions", path))  ##�л���Ŀ¼
            return True
        else:
            print(u'���ֽ���', path, u'���ļ����Ѿ������ˣ�')
            return False

    def request(self, url):  ##���������ȡ��ҳ��response Ȼ�󷵻�
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
        content = requests.get(url, headers=headers)
        return content


passion = PassionPic()  ##ʵ����
passion.all_url('http://1024v3.org/pw/thread.php?fid=16')  ##������all_url�������  ����Ե����������棨������ڣ�
