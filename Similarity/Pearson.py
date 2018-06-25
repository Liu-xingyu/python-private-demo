# -*-coding:utf-8 -*-
# 计算皮尔逊相关度：
def pearson(p, q):
    # 只计算两者共同有的
    same = 0
    for i in p:
        if i in q:
            same += 1

    n = same
    # 分别求p，q的和
    sumx = sum([p[i] for i in range(n)])
    sumy = sum([q[i] for i in range(n)])
    # 分别求出p，q的平方和
    sumxsq = sum([p[i] ** 2 for i in range(n)])
    sumysq = sum([q[i] ** 2 for i in range(n)])
    # 求出p，q的乘积和
    sumxy = sum([p[i] * q[i] for i in range(n)])
    # print sumxy
    # 求出pearson相关系数
    up = sumxy - sumx * sumy / n
    down = ((sumxsq - pow(sumxsq, 2) / n) * (sumysq - pow(sumysq, 2) / n)) ** .5
    # 若down为零则不能计算，return 0
    if down == 0: return 0
    r = up / down
    return r


p = [1, 3, 2, 3, 4, 3, 6]
q = [1, 3, 4, 5, 2, 3, 4, 3]
print(pearson(p, q))
print(pearson(p, p))

