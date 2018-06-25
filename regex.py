# coding:utf-8

'''
测试使用Python的正则表达式
'''

import re

pattern = re.compile(r'(\w+) (\w+)')
str = 'i say, hello word'

print(re.subn(pattern, r'\2 \1', str))


def regexFun(m):
    return m.group(1).title() + ' ' + m.group(2).title()


print(re.subn(pattern, regexFun, str))
