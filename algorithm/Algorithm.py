# coding=utf-8

'''
数据结构基本算法

'''


class Algorithm():
    # 值得推敲
    def bubble(self, arrs):
        for i in range(len(arrs)):
            for j in range(i + 1, len(arrs)):
                if arrs[i] > arrs[j]:
                    temp = arrs[i]
                    arrs[i] = arrs[j]
                    arrs[j] = temp

        print(u'第一种冒泡排序方法结果：', arrs)

    # 冒泡排序算法
    def bubbleSort(self, arrs):
        for i in range(len(arrs))[::-1]:  # 数组从后到前的倒序遍历
            for j in range(i):
                if arrs[j] > arrs[j + 1]:
                    arrs[j], arrs[j + 1] = arrs[j + 1], arrs[j]

        print(u'The second bubble sort method：', arrs)
        # print('%s:%' % ('The second bubble sort method', arrs))

    # python实现快速排序，递归实现，python没有自增一个单位
    def quickSort(self, arrs, low, high):
        if low < high:
            left, right = low, high
            pivot = arrs[left]
            while left <= right:
                while arrs[left] < pivot:
                    left += 1
                while arrs[right] > pivot:
                    right -= 1
                if left < right:
                    arrs[left], arrs[right] = arrs[right], arrs[left]
                    left += 1
                    right -= 1
            self.quickSort(arrs, low, right)
            self.quickSort(arrs, left, high)
            print(u'打印输出结果:', left, right, pivot)
        return arrs


arrs = [31, 2, 53, 1, 43, 5, 1, 6]
bubbleArrs, quickArrs = arrs, arrs
# print(arrs, '\n')
algorithm = Algorithm()
# algorithm.bubble(bubbleArrs)
# algorithm.bubbleSort(bubbleArrs)
# print(arrs, '\n')


print(quickArrs, '\n')
print(u'快速排序：', algorithm.quickSort(quickArrs, 0, len(quickArrs) - 1), '\n')
print(quickArrs)
