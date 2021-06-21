# -*- coding: utf-8 -*-
# @Time    : 2019-05-30 18:09
# @Author  : xinquan
# @File    : mytest_insert.py

def insertSort_1(mylist):
    for i in range(1, len(mylist)):
        target = mylist[i]
        j = i
        while j > 0:
            if target < mylist[j-1]:
                mylist[j] = mylist[j - 1]
            else:
                break
            j = j-1
        mylist[j] = target
    return mylist


def insertSort(lst):
    n = len(lst)
    for i in range(1, n):
        j = i
        target = lst[i]  # 每次循环的一个待插入的数
        while j > 0 and target < lst[j - 1]:  # 比较、后移，给target腾位置
            lst[j] = lst[j - 1]     # 后移
            j = j - 1
        lst[j] = target  # 把target插到空位
    return lst


def insertSort_2(mylist):
    for i in range(1, len(mylist)):
        target = mylist[i]
        j = i
        while j > 0 and target < mylist[j-1]:
            mylist[j] = mylist[j-1]
            j = j-1
        mylist[j] = target
    return mylist


def insert_sort_3(mylist):
    for i in range(1, len(mylist)):
        target = mylist[i]
        j = i
        while j > 0 and target < mylist[j - 1]:

            mylist[j] = mylist[j - 1]
            j -= 1

        mylist[j] = target
    return mylist




if __name__ == '__main__':
    print("实现插入排序")
    print(insert_sort_3([10, 1, 4, 6, 5, 2, 8, 7, 9]))