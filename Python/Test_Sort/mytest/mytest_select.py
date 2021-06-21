# -*- coding: utf-8 -*-
# @Time    : 2019-05-30 18:09
# @Author  : xinquan
# @File    : mytest_insert.py


def select_sort(mylist):
    for i in range(len(mylist)):
        minindex = i
        for j in range(i+1, len(mylist)):
            if mylist[j] < mylist[minindex]:
                minindex = j
        if minindex != i:
            (mylist[i], mylist[minindex]) = (mylist[minindex], mylist[i])

    return mylist


def select_sort_1(mylist):
    for i in range(len(mylist)):
        min_index = i
        for j in range(i+1, len(mylist)):
            if mylist[j] > mylist[min_index]:
                min_index = j
        (mylist[i], mylist[min_index]) = (mylist[min_index], mylist[i])

    return mylist


def select_sort_02(mylist):
    for i in range(len(mylist)):
        mindex = i
        for j in range(i+1, len(mylist)):
            if mylist[j] > mylist[mindex]:
                mindex = j

        (mylist[mindex], mylist[i]) = (mylist[i], mylist[mindex])
    return mylist

if __name__ == '__main__':
    print("选择排序的实现")
    mylist = [10, 1, 4, 6, 5, 2, 8, 7, 7, 9, 3]
    print(select_sort_02(mylist))