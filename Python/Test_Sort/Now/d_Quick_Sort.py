# -*-coding:utf-8-*-

"""
快速排序实现
"""



def quickSort(lst):

    def func02(arr, left, right):   # 寻找出中间值
        key = left
        while left < right:

            # 右边
            while left < right and arr[right] > arr[key]:
                right = right -1

            # 左边
            while left < right and arr[left] < arr[key]:
                left += 1
            # 当右边找到小值，当左边找到大值的时候
            (arr[left], arr[right]) = (arr[right], arr[left])

        (arr[left], arr[key]) = (arr[key], arr[left])

        return left

    # 递归主体
    def func01(arr, left, right):
        if left > right:
            return

        min = func02(arr, left, right)

        func01(arr, left, min -1)   # 左节点
        func01(arr, min + 1, right)
    n = len(lst)
    func01(lst,0, n -1)
    return lst



# def quick_sort(mylist):
#     def func2(arr, left, right):
#         key = left
#         while left < right:
#             while left < right and arr[right] >= arr[key]:
#                 right -= 1
#             while left < right and arr[left] <= arr[key]:
#                 left += 1
#             (arr[left], arr[right]) = (arr[right], arr[left])
#
#         (arr[left], arr[key]) = (arr[key], arr[left])
#         return left
#
#     def fun1(arr, left, right):
#         if left > right:
#             return
#         min = func2(arr, left, right)
#         fun1(arr, left, min-1)
#         fun1(arr, min+1, right)
#
#
#     n = len(mylist)
#     fun1(mylist, 0, n - 1)
#     return mylist







if __name__ == '__main__':
    print("实现快速排序")
    print(quickSort([3, 10, 4, 6, 5, 2, 8, 7, 9]))


"""
快速的测试时间概览：

百级排序消耗时间： 0.00038695335388183594
千级排序消耗时间： 0.006429910659790039
万级排序消耗时间： 0.08614110946655273
十万级排序消耗时间： 1.0215158462524414
"""