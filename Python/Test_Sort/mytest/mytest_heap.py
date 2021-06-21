# -*- coding: utf-8 -*-
# @Time    : 2019-05-31 12:02
# @Author  : xinquan
# @File    : mytest_heap.py



def heapSort(mylist):


    def func(arr, start, end):
        tmp = arr[start]
        son = start * 2 + 1
        while son < end:
            if son < end and arr[son] < arr[son + 1]:
                son += 1
            if tmp >= arr[son]:
                break
            arr[start] = arr[son]
            start = son
            son = son * 2 + 1
        arr[start] = tmp

    n = len(mylist)
    root = n//2 - 1  # 最小非叶节点
    while root >= 0:
        func(mylist, root, n - 1)
        root -= 1

    i = n - 1
    while i >= 0:
        print(mylist[0])
        (mylist[i], mylist[0]) = (mylist[0], mylist[i])
        func(mylist, 0, i - 1)
        i -= 1
    return mylist


if __name__ == '__main__':
    print("实现归并排序")
    print(heapSort([10, 1, 4, 6, 5, 2, 8, 8, 7, 9, 3]))

