# -*-coding:utf-8 -*-

import math
import sys

print(u'the dynamic arrays is:', sys.argv)


# 计算欧几里德距离：
def euclidean(p, q):
    # 如果两数据集数目不同，计算两者之间都对应有的数
    same = 0
    for i in p:
        if i in q:
            same += 1

    # 计算欧几里德距离,并将其标准化
    e = sum([(p[i] - q[i]) ** 2 for i in range(same)])
    return 1 / (1 + e ** .5)


arrs = [[1, 3, 2, 3, 4, 3, 0], [3, 4, 3, 2, 3, 4, 3], [2, 3, 4, 5, 6, 7, 8], [1, 3, 4, 6, 8, 7, 5]]

for i in range(len(sys.argv)):
    print(u'the similarity is:', euclidean(arrs[i], arrs[len(sys.argv) % 5]))

# p = [1, 3, 2, 3, 4, 3, 0]
# q = [3, 4, 3, 2, 3, 4, 3]
# m = [2, 3, 4, 5, 6, 7, 8]
# n = [1, 3, 4, 6, 8, 7, 5]

# print(u'p，q用户相似度：', euclidean(p, q))
# print(u'p，m用户相似度：', euclidean(p, m))
# print(u'p，n用户相似度：', euclidean(p, n))
# print(u'm，q用户相似度：', euclidean(m, q))
# print(u'n，q用户相似度：', euclidean(n, q))
# print(u'm，n用户相似度：', euclidean(m, n))
# print(u'm，m用户相似度：', euclidean(m, m))

# print(u'p与q的用户相似度为：', euclidean(p, q))
