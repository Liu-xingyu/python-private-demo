#coding:utf-8

''' 测试CSDN登录 '''

import urllib.request
import urllib

class csdnLogin():
    def _login(self,url,values):
        resp = urllib.request.urlopen(url,values)
        print(resp.read())

values = {'username':'873750200@qq.com','password':'yrp19930128'}
Login = csdnLogin()
Login._login('https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn',values)
