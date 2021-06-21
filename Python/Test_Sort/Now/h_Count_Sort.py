# -*-coding:utf-8-*-
"""
计数排序实现
"""


def countSort(lst):
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


if __name__ == '__main__':
    print("实现计数排序")
    print(CountSort([1, 4, 6, 5, 2, 8, 7, 9]))
