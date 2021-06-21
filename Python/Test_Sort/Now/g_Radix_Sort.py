# -*-coding:utf-8-*-

"""
基数排序实现
"""
import math


def radixSort(lst):
    def getbit(x, i):  # 返回x的第i位（从右向左，个位为0）数值
        y = x // pow(10, i)
        z = y % 10
        return z

    def CountSort(lst):
        n = len(lst)
        num = max(lst)
        count = [0] * (num + 1)
        for i in range(0, n):
            count[lst[i]] += 1
        arr = []
        for i in range(0, num + 1):
            for j in range(0, count[i]):
                arr.append(i)
        return arr

    Max = max(lst)
    for k in range(0, int(math.log10(Max)) + 1):  # 对k位数排k次,每次按某一位来排
        arr = [[] for i in range(0, 10)]
        for i in lst:  # 将ls（待排数列）中每个数按某一位分类（0-9共10类）存到arr[][]二维数组（列表）中
            arr[getbit(i, k)].append(i)
        for i in range(0, 10):  # 对arr[]中每一类（一个列表）  按计数排序排好
            if len(arr[i]) > 0:
                arr[i] = CountSort(arr[i])
        j = 9
        n = len(lst)
        for i in range(0, n):  # 顺序输出arr[][]中数到ls中，即按第k位排好
            while len(arr[j]) == 0:
                j -= 1
            else:
                lst[n - 1 - i] = arr[j].pop()
    return lst



if __name__ == '__main__':
    print("实现归并排序")
    print(RadixSort([1, 4, 6, 5, 2, 8, 7, 9]))
