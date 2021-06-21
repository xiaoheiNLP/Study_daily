# -*- coding: utf-8 -*-
# @Time    : 2019-05-30 20:38
# @Author  : xinquan
# @File    : mytest_quick.py



def quick_sort(mylist):
    def func2(arr, left, right):
        key = left
        while left < right:
            while left < right and arr[right] >= arr[key]:
                right -= 1
            while left < right and arr[left] <= arr[key]:
                left += 1
            (arr[left], arr[right]) = (arr[right], arr[left])

        (arr[left], arr[key]) = (arr[key], arr[left])
        return left

    def fun1(arr, left, right):
        if left > right:
            return
        min = func2(arr, left, right)
        fun1(arr, left, min-1)
        fun1(arr, min+1, right)


    n = len(mylist)
    fun1(mylist, 0, n - 1)
    return mylist


def quickSort(lst):
    # 此函数完成分区操作
    def partition(arr, left, right):
        key = left  # 划分参考数索引,默认为第一个数为基准数，可优化
        while left < right:
            # 如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
            while left < right and arr[right] >= arr[key]:
                right -= 1

            # 如果列表前边的数,比基准数小或相等,则后移一位直到有比基准数大的数出现
            while left < right and arr[left] <= arr[key]:
                left += 1
            # 此时已找到一个比基准大的书，和一个比基准小的数，将他们互换位置
            (arr[left], arr[right]) = (arr[right], arr[left])

        # 当从两边分别逼近，直到两个位置相等时结束，将左边小的同基准进行交换
        (arr[left], arr[key]) = (arr[key], arr[left])
        # 返回目前基准所在位置的索引
        return left

    def quicksort(arr, left, right):
        if left >= right:
            return
        # 从基准开始分区
        mid = partition(arr, left, right)
        # print(mid)
        # print(arr)
        # print()
        # 递归调用
        quicksort(arr, left, mid - 1)
        quicksort(arr, mid + 1, right)

    # 主函数
    n = len(lst)
    quicksort(lst, 0, n - 1)
    return lst


def quickSort_1(mylist):

    def func02(mylist, left, right):
        key = left
        while left < right:

            while left < right and mylist[right] >= mylist[key]:
                right -= 1

            while left < right and mylist[left] <= mylist[key]:
                left += 1

            (mylist[right], mylist[left]) = (mylist[left], mylist[right])

        (mylist[key], mylist[right]) = (mylist[right], mylist[key])
        return left

    def func01(mylist, left, right):
        if left >= right:
            return

        mid = func02(mylist, left, right)

        func02(mylist, left, mid-1)
        func02(mylist, mid+1, right)

    # 主函数
    n = len(mylist)
    func01(mylist, 0, n - 1)
    return mylist


if __name__ == '__main__':
    print("实现快速排序")
    print(quickSort_1([3, 10, 4, 6, 5, 2, 8, 7, 9]))

