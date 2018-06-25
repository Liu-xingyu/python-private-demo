# -*-coding:utf-8 -*-
# 计算曼哈顿距离：
def manhattan(p, q):
    # 只计算两者共同有的
    same = 0
    for i in p:
        if i in q:
            same += 1
    # 计算曼哈顿距离
    n = same
    vals = range(n)
    distance = sum(abs(p[i] - q[i]) for i in vals)
    return distance


p = [1, 3, 2, 3, 4, 3]
q = [1, 3, 4, 3, 2, 3, 4, 3]
m = [2, 3, 4, 5, 6, 7]
n = [1, 3, 4, 6, 8, 7, 5]
print(u'p，q用户相似度：', manhattan(p, q))
print(u'p，m用户相似度：', manhattan(p, m))
print(u'p，n用户相似度：', manhattan(p, n))
print(u'm，q用户相似度：', manhattan(m, q))
print(u'n，q用户相似度：', manhattan(n, q))
print(u'm，n用户相似度：', manhattan(m, n))
print(u'm，m用户相似度：', manhattan(m, m))

