from __future__ import print_function
import csv


def readCsv():
    with open("D:\\score.csv", "r") as fr:
        # 这个方法返回的是迭代类型
        rows = csv.reader(fr)
        userid, count, tempList = 0, 0, []
        for row in rows:
            if userid == row[0]:
                tempList.append(row[1])
            else:
                if (len(tempList) > 0) and (count < 15):
                    print(u'学号:', row[0], u' 课程:', tempList)
                    tempList = []
                    count = count + 1
                userid = row[0]
                tempList.append(row[1])


readCsv()
